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
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import time
import uuid
from typing import Dict, Iterator, List, Optional

ACTIVE_SCHEMA_VERSION = 1
GENERATION_SCHEMA_VERSION = 1
LOCK_STALE_SECONDS = 300
LOCK_TIMEOUT_SECONDS = 30.0


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


def metadata_dir(root: Path) -> Path:
    return Path(root).resolve() / ".aiverse"


def generations_dir(root: Path) -> Path:
    return metadata_dir(root) / "generations"


def active_pointer_path(root: Path) -> Path:
    return metadata_dir(root) / "active.json"


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
    base = generations_dir(root).resolve()
    path = (base / generation_id).resolve()
    try:
        path.relative_to(base)
    except ValueError as exc:
        raise RuntimeError("Generation path escapes lifecycle root") from exc
    return path


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
    target = generation_path(root, generation_id)
    target.parent.mkdir(parents=True, exist_ok=True)
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


def pin_active_generation(root: Path, digest_fn) -> GenerationPin:
    """Capture a complete immutable generation for one execution."""

    root = Path(root).resolve()
    pointer = read_active_pointer(root)
    generation_id = str(pointer["generation_id"])
    errors = verify_generation(root, generation_id, digest_fn)
    if errors:
        raise RuntimeError("Active generation failed verification:\n" + "\n".join(errors))
    manifest = read_generation_manifest(root, generation_id)
    digest = str(manifest.get("generation_digest_sha256", ""))
    if not digest:
        raise RuntimeError(f"Generation {generation_id} has no content digest")
    return GenerationPin(generation_id, generation_path(root, generation_id), manifest, digest)


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
