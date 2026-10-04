#!/usr/bin/env python3
"""Immutable generation lifecycle primitives for AI-Verse Skills.

A lifecycle root is a small coordination directory. Installed skill content lives
under `.aiverse/generations/<generation_id>/` and is never mutated after commit.
Activation is a single atomic pointer replacement, so readers see either the old
or the new complete generation. Consumers must pin the active generation before
loading SKILL.md or any helper script from that package.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
import datetime as dt
import errno
import hashlib
import json
import os
from pathlib import Path
import socket
import shutil
import tempfile
import time
import uuid
from typing import Dict, Iterator, List, Optional

ACTIVE_SCHEMA_VERSION = 1
GENERATION_SCHEMA_VERSION = 1
LOCK_STALE_SECONDS = 300
LOCK_TIMEOUT_SECONDS = 30.0
GENERATION_LEASE_SCHEMA_VERSION = 1
WINDOWS_REPARSE_POINT = 0x0400


@dataclass(frozen=True)
class GenerationPin:
    generation_id: str
    generation_path: Path
    manifest: Dict[str, object]
    generation_digest_sha256: str

    def package_path(self, package_id: str) -> Path:
        for package in self.manifest.get("packages", []):
            if package.get("id") == package_id:
                return self.generation_path / str(package["path"])
        raise RuntimeError(f"Package not installed in pinned generation: {package_id}")


@dataclass(frozen=True)
class GenerationLease:
    generation_id: str
    lease_id: str
    lease_token: str
    owner_pid: int
    hostname: str
    generation_path: Path
    manifest: Dict[str, object]
    generation_digest_sha256: str

    def package_path(self, package_id: str) -> Path:
        for package in self.manifest.get("packages", []):
            if package.get("id") == package_id:
                return self.generation_path / str(package["path"])
        raise RuntimeError(f"Package not installed in leased generation: {package_id}")


def _absolute_path(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(Path(path).expanduser())))


def _is_symlink_or_reparse(path: Path) -> bool:
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        return False
    if os.path.islink(path):
        return True
    return bool(getattr(info, "st_file_attributes", 0) & WINDOWS_REPARSE_POINT)


def controller_path(root: Path, *parts: str) -> Path:
    """Return a controller path only when its existing chain is confined to root.

    The selected Skills root may not delegate `.aiverse` or any descendant
    controller path through a symlink, Windows junction, or other reparse point.
    Missing controller children are allowed so first install can create them, but
    every existing component is resolved and proven to remain under the selected
    root before the path is returned.
    """

    root_input = _absolute_path(root)
    candidate = root_input / ".aiverse"
    for part in parts:
        if not isinstance(part, str) or not part or part in {".", ".."} or "/" in part or "\\" in part:
            raise RuntimeError(f"Invalid Skills controller path component: {part!r}")
        candidate = candidate / part

    if not root_input.exists():
        return candidate
    if _is_symlink_or_reparse(root_input):
        raise RuntimeError(f"Skills lifecycle root may not be a symlink/junction/reparse point: {root_input}")
    if not root_input.is_dir():
        raise RuntimeError(f"Skills lifecycle root is not a directory: {root_input}")

    root_real = root_input.resolve(strict=True)
    current = root_input
    for part in (".aiverse", *parts):
        current = current / part
        if _is_symlink_or_reparse(current):
            raise RuntimeError(f"Unsafe symlink/junction/reparse point in Skills controller path: {current}")
        if current.exists():
            resolved = current.resolve(strict=True)
            try:
                resolved.relative_to(root_real)
            except ValueError as exc:
                raise RuntimeError(f"Skills controller path resolves outside selected root: {current}") from exc

    parent = candidate.parent
    while parent != root_input and not parent.exists():
        parent = parent.parent
    if _is_symlink_or_reparse(parent):
        raise RuntimeError(f"Unsafe symlink/junction/reparse parent in Skills controller path: {parent}")
    parent_real = parent.resolve(strict=True)
    try:
        parent_real.relative_to(root_real)
    except ValueError as exc:
        raise RuntimeError(f"Skills controller parent resolves outside selected root: {parent}") from exc
    return candidate


def metadata_dir(root: Path) -> Path:
    return controller_path(root)


def generations_dir(root: Path) -> Path:
    return controller_path(root, "generations")


def generation_leases_dir(root: Path) -> Path:
    return controller_path(root, "leases")


def active_pointer_path(root: Path) -> Path:
    return controller_path(root, "active.json")


def lifecycle_lock_path(root: Path) -> Path:
    root = Path(root).resolve()
    return root.parent / f".{root.name}.lifecycle.lock"


def new_generation_id() -> str:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return f"gen-{stamp}-{uuid.uuid4().hex[:8]}"


def _atomic_json_write(path: Path, data: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def _process_is_alive(pid: int) -> Optional[bool]:
    """Return True/False when local process liveness is knowable, else None."""

    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 0:
        return None
    if pid == os.getpid():
        return True

    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            process_query_limited_information = 0x1000
            still_active = 259
            error_invalid_parameter = 87

            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            open_process = kernel32.OpenProcess
            open_process.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            open_process.restype = wintypes.HANDLE
            get_exit_code_process = kernel32.GetExitCodeProcess
            get_exit_code_process.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
            get_exit_code_process.restype = wintypes.BOOL
            close_handle = kernel32.CloseHandle
            close_handle.argtypes = [wintypes.HANDLE]
            close_handle.restype = wintypes.BOOL

            handle = open_process(process_query_limited_information, False, pid)
            if not handle:
                error = ctypes.get_last_error()
                if error == error_invalid_parameter:
                    return False
                return None
            try:
                exit_code = wintypes.DWORD()
                if not get_exit_code_process(handle, ctypes.byref(exit_code)):
                    return None
                return exit_code.value == still_active
            finally:
                close_handle(handle)
        except Exception:
            return None

    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError as exc:
        if exc.errno == errno.ESRCH:
            return False
        if exc.errno == errno.EPERM:
            return True
        return None
    return True


def _read_lock_holder(path: Path) -> Optional[Dict[str, object]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError, UnicodeError):
        return None
    return data if isinstance(data, dict) else None


def _holder_is_alive(path: Path) -> Optional[bool]:
    holder = _read_lock_holder(path)
    if holder is None:
        return None
    holder_host = holder.get("hostname")
    if holder_host not in {None, "", socket.gethostname()}:
        return None
    return _process_is_alive(holder.get("pid"))


def _release_lock_if_owned(path: Path, token: str) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("token") == token:
            path.unlink(missing_ok=True)
    except FileNotFoundError:
        return
    except Exception:
        return


@contextmanager
def lifecycle_lock(root: Path, *, timeout_seconds: float = LOCK_TIMEOUT_SECONDS) -> Iterator[None]:
    """Serialize install/update/rollback/uninstall operations for one root."""

    path = lifecycle_lock_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    token = uuid.uuid4().hex
    deadline = time.monotonic() + max(0.0, timeout_seconds)
    payload = json.dumps({
        "token": token,
        "pid": os.getpid(),
        "hostname": socket.gethostname(),
        "acquired_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }) + "\n"

    while True:
        try:
            fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            try:
                age = time.time() - path.stat().st_mtime
            except FileNotFoundError:
                continue
            if age > LOCK_STALE_SECONDS:
                holder = _read_lock_holder(path)
                holder_live = _holder_is_alive(path)
                if holder is not None and holder_live is False:
                    observed_token = holder.get("token")
                    current = _read_lock_holder(path)
                    if (
                        isinstance(observed_token, str)
                        and observed_token
                        and current is not None
                        and current.get("token") == observed_token
                    ):
                        try:
                            path.unlink()
                        except FileNotFoundError:
                            pass
                    continue
            if time.monotonic() >= deadline:
                raise RuntimeError(f"Skills lifecycle is busy for {root}; another mutation holds {path}")
            time.sleep(0.05)
            continue
        else:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            break

    try:
        yield
    finally:
        _release_lock_if_owned(path, token)


def generation_content_digest(root: Path) -> str:
    """Digest immutable generation content, excluding its self-describing manifest."""

    root = Path(root)
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() or p.is_symlink()):
        rel = path.relative_to(root).as_posix()
        if rel == ".aiverse/installed.json":
            continue
        h.update(rel.encode("utf-8") + b"\0")
        if path.is_symlink():
            h.update(b"SYMLINK\0" + os.readlink(path).encode("utf-8"))
        else:
            h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def _read_json(path: Path, label: str) -> Dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Invalid {label} {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Invalid {label} {path}: expected JSON object")
    return data


def read_active_pointer(root: Path, *, allow_uninstalled: bool = False) -> Dict[str, object]:
    path = active_pointer_path(root)
    if not path.is_file():
        raise RuntimeError(f"No generation lifecycle found at {root}; missing {path}")
    data = _read_json(path, "active generation pointer")
    if data.get("schema_version") != ACTIVE_SCHEMA_VERSION:
        raise RuntimeError(
            f"Unsupported active generation pointer schema {data.get('schema_version')!r}; "
            f"expected {ACTIVE_SCHEMA_VERSION}"
        )
    state = data.get("state")
    if state not in {"active", "uninstalled"}:
        raise RuntimeError(f"Invalid active generation state: {state!r}")
    if state == "uninstalled" and not allow_uninstalled:
        raise RuntimeError(f"AI-Verse-Skills is uninstalled at {root}")
    history = data.get("history", [])
    if not isinstance(history, list) or not all(isinstance(item, str) and item for item in history):
        raise RuntimeError("Invalid active generation history")
    if state == "active" and not isinstance(data.get("generation_id"), str):
        raise RuntimeError("Active generation pointer is missing generation_id")
    return data


def generation_path(root: Path, generation_id: str) -> Path:
    if not generation_id or "/" in generation_id or "\\" in generation_id or generation_id in {".", ".."}:
        raise RuntimeError("Invalid generation id")
    return controller_path(root, "generations", generation_id)


def read_generation_manifest(root: Path, generation_id: str) -> Dict[str, object]:
    path = generation_path(root, generation_id)
    manifest_path = path / ".aiverse" / "installed.json"
    if not manifest_path.is_file():
        raise RuntimeError(f"Generation {generation_id} is missing manifest: {manifest_path}")
    data = _read_json(manifest_path, "generation manifest")
    if data.get("generation_schema_version") != GENERATION_SCHEMA_VERSION:
        raise RuntimeError(
            f"Unsupported generation manifest schema {data.get('generation_schema_version')!r}; "
            f"expected {GENERATION_SCHEMA_VERSION}"
        )
    if data.get("generation_id") != generation_id:
        raise RuntimeError(f"Generation manifest id mismatch: expected {generation_id}")
    return data


def verify_generation(root: Path, generation_id: str, digest_fn) -> List[str]:
    errors: List[str] = []
    try:
        manifest = read_generation_manifest(root, generation_id)
    except RuntimeError as exc:
        return [str(exc)]
    path = generation_path(root, generation_id)
    for package in manifest.get("packages", []):
        if not isinstance(package, dict):
            errors.append("generation manifest contains a non-object package entry")
            continue
        package_id = str(package.get("id", "?"))
        rel = package.get("path")
        if not isinstance(rel, str) or not rel:
            errors.append(f"{package_id}: invalid package path")
            continue
        package_dir = path / rel
        if not (package_dir / "SKILL.md").exists():
            errors.append(f"{package_id}: missing SKILL.md")
        elif digest_fn(package_dir) != package.get("digest_sha256"):
            errors.append(f"{package_id}: content digest changed")
    expected = manifest.get("generation_digest_sha256")
    actual = generation_content_digest(path)
    if expected != actual:
        errors.append(f"{generation_id}: generation content digest changed")
    return errors


def commit_stage(root: Path, stage: Path, generation_id: str) -> Path:
    """Move one fully-built verified stage into immutable generation storage."""

    root = Path(root).resolve()
    stage = Path(stage).resolve()
    parent = generations_dir(root)
    parent.mkdir(parents=True, exist_ok=True)
    target = generation_path(root, generation_id)
    if target.exists():
        raise RuntimeError(f"Generation already exists: {generation_id}")
    os.replace(stage, target)
    return target


def _history_without(history: List[str], *excluded: Optional[str]) -> List[str]:
    blocked = {item for item in excluded if item}
    out: List[str] = []
    for item in history:
        if item not in blocked and item not in out:
            out.append(item)
    return out


def activate_generation(root: Path, generation_id: str) -> Dict[str, object]:
    """Atomically switch the one active generation pointer.

    A missing pointer is valid only for first activation. A malformed existing
    pointer is never treated as absence because overwriting it would silently
    destroy rollback state.
    """

    root = Path(root).resolve()
    path = generation_path(root, generation_id)
    if not path.is_dir():
        raise RuntimeError(f"Cannot activate missing generation: {generation_id}")
    manifest = read_generation_manifest(root, generation_id)
    controller = metadata_dir(root)
    controller.mkdir(parents=True, exist_ok=True)
    pointer_path = active_pointer_path(root)
    if pointer_path.exists():
        current = read_active_pointer(root, allow_uninstalled=True)
    else:
        current = {"state": "uninstalled", "generation_id": None, "history": []}
    current_id = current.get("generation_id") if current.get("state") == "active" else None
    history = list(current.get("history", []))
    if current_id and current_id != generation_id:
        history = [str(current_id)] + _history_without(history, str(current_id), generation_id)
    else:
        history = _history_without(history, generation_id)
    pointer: Dict[str, object] = {
        "schema_version": ACTIVE_SCHEMA_VERSION,
        "state": "active",
        "generation_id": generation_id,
        "generation_digest_sha256": manifest.get("generation_digest_sha256"),
        "activated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "history": history,
    }
    _atomic_json_write(pointer_path, pointer)
    return pointer


def pin_generation(root: Path, generation_id: str, digest_fn) -> GenerationPin:
    """Capture and verify one exact immutable generation."""

    root = Path(root).resolve()
    path = generation_path(root, generation_id)
    errors = verify_generation(root, generation_id, digest_fn)
    if errors:
        raise RuntimeError(f"Generation {generation_id} failed verification:\n" + "\n".join(errors))
    manifest = read_generation_manifest(root, generation_id)
    digest = str(manifest.get("generation_digest_sha256", ""))
    if not digest:
        raise RuntimeError(f"Generation {generation_id} has no content digest")
    return GenerationPin(generation_id, path, manifest, digest)


def pin_active_generation(root: Path, digest_fn) -> GenerationPin:
    """Capture a complete immutable generation for one execution."""

    root = Path(root).resolve()
    pointer = read_active_pointer(root)
    return pin_generation(root, str(pointer["generation_id"]), digest_fn)


def _generation_lease_path(root: Path, generation_id: str, lease_id: str) -> Path:
    generation_path(root, generation_id)  # validates the generation identifier and controller chain
    if (
        not isinstance(lease_id, str)
        or len(lease_id) != 32
        or any(ch not in "0123456789abcdef" for ch in lease_id)
    ):
        raise RuntimeError("Invalid generation lease id")
    return controller_path(root, "leases", generation_id, lease_id + ".json")


def acquire_generation_lease(
    root: Path,
    digest_fn,
    *,
    owner_pid: Optional[int] = None,
    generation_id: Optional[str] = None,
    package_id: Optional[str] = None,
) -> GenerationLease:
    """Atomically pin an active or explicitly selected generation for execution.

    The lease and explicit purge share the lifecycle lock, so purge cannot pass
    its lease scan between generation selection and durable lease publication.
    A lease belongs to a local or remote process identity; only a verifiably
    dead local process can be reaped automatically.
    """

    root = _absolute_path(root)
    pid = os.getpid() if owner_pid is None else owner_pid
    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 0:
        raise RuntimeError("Generation lease owner PID must be a positive integer")
    if _process_is_alive(pid) is not True:
        raise RuntimeError(f"Generation lease owner process is not verifiably live: {pid}")

    with lifecycle_lock(root):
        pin = (
            pin_active_generation(root, digest_fn)
            if generation_id is None
            else pin_generation(root, generation_id, digest_fn)
        )
        # Validate requested package before publishing a durable lease. A failed
        # pin request must never strand a lease the caller cannot release.
        if package_id is not None:
            pin.package_path(package_id)
        lease_id = uuid.uuid4().hex
        token = uuid.uuid4().hex
        hostname = socket.gethostname()
        path = _generation_lease_path(root, pin.generation_id, lease_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        _atomic_json_write(path, {
            "schema_version": GENERATION_LEASE_SCHEMA_VERSION,
            "generation_id": pin.generation_id,
            "lease_id": lease_id,
            "lease_token": token,
            "pid": pid,
            "hostname": hostname,
            "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        })
        return GenerationLease(
            generation_id=pin.generation_id,
            lease_id=lease_id,
            lease_token=token,
            owner_pid=pid,
            hostname=hostname,
            generation_path=pin.generation_path,
            manifest=pin.manifest,
            generation_digest_sha256=pin.generation_digest_sha256,
        )


def release_generation_lease(
    root: Path,
    generation_id: str,
    lease_id: str,
    lease_token: str,
) -> bool:
    """Release one lease only when the caller presents its unguessable token."""

    root = _absolute_path(root)
    if not isinstance(lease_token, str) or not lease_token:
        raise RuntimeError("Generation lease token is required")
    with lifecycle_lock(root):
        path = _generation_lease_path(root, generation_id, lease_id)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return False
        except (json.JSONDecodeError, OSError, UnicodeError) as exc:
            raise RuntimeError(f"Generation lease is unreadable; refusing release: {path}") from exc
        if not isinstance(data, dict) or data.get("lease_token") != lease_token:
            raise RuntimeError("Generation lease token mismatch")
        if data.get("generation_id") != generation_id or data.get("lease_id") != lease_id:
            raise RuntimeError("Generation lease identity mismatch")
        current = None
        try:
            current = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError, OSError, UnicodeError):
            return False
        if not isinstance(current, dict) or current.get("lease_token") != lease_token:
            raise RuntimeError("Generation lease changed before release")
        path.unlink(missing_ok=True)
        try:
            path.parent.rmdir()
        except OSError:
            pass
        return True


def active_generation_leases(root: Path) -> Dict[str, object]:
    """Classify leases while the caller holds lifecycle_lock(root).

    Malformed, foreign-host, and otherwise unverifiable leases protect their
    generation. Age never authorizes reclaim of a live process lease.
    """

    root = _absolute_path(root)
    lease_root = generation_leases_dir(root)
    result: Dict[str, object] = {
        "protected_generation_ids": [],
        "live": [],
        "unverifiable": [],
        "stale_reaped": [],
    }
    if not lease_root.exists():
        return result
    protected = set()
    for generation_entry in sorted(lease_root.iterdir()):
        generation_id = generation_entry.name
        if _is_symlink_or_reparse(generation_entry) or not generation_entry.is_dir():
            raise RuntimeError(f"Unsafe generation lease entry: {generation_entry}")
        generation_path(root, generation_id)
        entries = sorted(generation_entry.iterdir())
        if not entries:
            try:
                generation_entry.rmdir()
            except OSError:
                pass
            continue
        for path in entries:
            identity = {"generation_id": generation_id, "lease_id": path.stem}
            if _is_symlink_or_reparse(path) or not path.is_file() or path.suffix != ".json":
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "unexpected lease entry"})
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError, UnicodeError):
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "unreadable lease"})
                continue
            valid = (
                isinstance(data, dict)
                and data.get("schema_version") == GENERATION_LEASE_SCHEMA_VERSION
                and data.get("generation_id") == generation_id
                and data.get("lease_id") == path.stem
                and isinstance(data.get("lease_token"), str)
                and bool(data.get("lease_token"))
                and isinstance(data.get("pid"), int)
                and not isinstance(data.get("pid"), bool)
                and data.get("pid") > 0
                and isinstance(data.get("hostname"), str)
                and bool(data.get("hostname"))
            )
            if not valid:
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "malformed lease identity"})
                continue
            host = data["hostname"]
            if host != socket.gethostname():
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "foreign-host holder"})
                continue
            alive = _process_is_alive(data["pid"])
            if alive is True:
                protected.add(generation_id)
                result["live"].append({**identity, "pid": data["pid"], "hostname": host})
                continue
            if alive is None:
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "holder liveness unavailable"})
                continue
            # Re-read the lease identity before reclaiming a dead holder, so a
            # concurrent replacement can never be removed using stale evidence.
            current = _read_lock_holder(path)
            if current is None or current.get("lease_token") != data["lease_token"]:
                protected.add(generation_id)
                result["unverifiable"].append({**identity, "reason": "lease changed during stale recovery"})
                continue
            try:
                path.unlink()
            except FileNotFoundError:
                pass
            result["stale_reaped"].append(identity)
        if not any(generation_entry.iterdir()):
            try:
                generation_entry.rmdir()
            except OSError:
                pass
    result["protected_generation_ids"] = sorted(protected)
    return result


def rollback_active_generation(root: Path, digest_fn) -> GenerationPin:
    """Switch to the most recent prior generation without modifying either generation."""

    root = Path(root).resolve()
    pointer = read_active_pointer(root, allow_uninstalled=True)
    history = list(pointer.get("history", []))
    if not history:
        raise RuntimeError(f"No rollback generation found under {generations_dir(root)}")
    chosen = history[0]
    errors = verify_generation(root, chosen, digest_fn)
    if errors:
        raise RuntimeError("Rollback generation failed verification:\n" + "\n".join(errors))
    current = str(pointer.get("generation_id")) if pointer.get("state") == "active" else None
    remaining = history[1:]
    if current and current != chosen:
        remaining = [current] + _history_without(remaining, current, chosen)
    manifest = read_generation_manifest(root, chosen)
    next_pointer: Dict[str, object] = {
        "schema_version": ACTIVE_SCHEMA_VERSION,
        "state": "active",
        "generation_id": chosen,
        "generation_digest_sha256": manifest.get("generation_digest_sha256"),
        "activated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "history": remaining,
    }
    _atomic_json_write(active_pointer_path(root), next_pointer)
    return pin_active_generation(root, digest_fn)


def mark_uninstalled(root: Path) -> Dict[str, object]:
    """Atomically deactivate the library while retaining immutable generations for recovery."""

    root = Path(root).resolve()
    pointer = read_active_pointer(root)
    current = str(pointer["generation_id"])
    history = [current] + _history_without(list(pointer.get("history", [])), current)
    next_pointer: Dict[str, object] = {
        "schema_version": ACTIVE_SCHEMA_VERSION,
        "state": "uninstalled",
        "generation_id": None,
        "generation_digest_sha256": None,
        "deactivated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "history": history,
    }
    _atomic_json_write(active_pointer_path(root), next_pointer)
    return next_pointer


def remove_orphan_stage(stage: Path) -> None:
    if stage.exists():
        shutil.rmtree(stage, ignore_errors=True)
