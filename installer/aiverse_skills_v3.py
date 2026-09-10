#!/usr/bin/env python3
"""AI-Verse Skills distribution installer with immutable generations.

The canonical install root is a lifecycle controller. Package bytes are stored in
immutable generations under `.aiverse/generations/`; `active.json` is the only
mutable activation pointer. An execution must pin one generation before reading
SKILL.md or any supporting scripts/assets.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

try:  # package import
    from .generation_lifecycle import (
        ACTIVE_SCHEMA_VERSION,
        GENERATION_SCHEMA_VERSION,
        active_pointer_path,
        activate_generation,
        commit_stage,
        generation_content_digest,
        generation_path,
        generations_dir,
        lifecycle_lock,
        mark_uninstalled,
        new_generation_id,
        pin_active_generation,
        read_active_pointer,
        read_generation_manifest,
        rollback_active_generation,
        verify_generation,
    )
except ImportError:  # direct script execution
    from generation_lifecycle import (
        ACTIVE_SCHEMA_VERSION,
        GENERATION_SCHEMA_VERSION,
        active_pointer_path,
        activate_generation,
        commit_stage,
        generation_content_digest,
        generation_path,
        generations_dir,
        lifecycle_lock,
        mark_uninstalled,
        new_generation_id,
        pin_active_generation,
        read_active_pointer,
        read_generation_manifest,
        rollback_active_generation,
        verify_generation,
    )

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = Path.home() / ".aiverse" / "skills"
DEFAULT_CACHE = Path.home() / ".cache" / "aiverse-skills" / "sources"
FRONT_NAME = re.compile(r"(?m)^name:\s*[\"']?([^\"'\n]+)")
ADAPTER_SCHEMA_VERSION = 2


def load(rel):
    return json.loads((REPO_ROOT / rel).read_text(encoding="utf-8"))


def run(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(f"Command failed ({p.returncode}): {' '.join(map(str, cmd))}\n{p.stderr.strip()}")
    return p.stdout


def cache_name(repo, commit):
    return repo.replace("/", "__") + "@" + commit


def checkout(repo, commit, cache, offline=False):
    dst = cache / cache_name(repo, commit)
    if (dst / ".git").exists():
        try:
            if run(["git", "rev-parse", "HEAD"], dst).strip() == commit:
                return dst
        except Exception:
            pass
        shutil.rmtree(dst, ignore_errors=True)
    if offline:
        raise RuntimeError(f"Offline cache miss: {repo}@{commit}")
    if not shutil.which("git"):
        raise RuntimeError("git is required for upstream-fetch packages")
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".partial-" + uuid.uuid4().hex[:8])
    tmp.mkdir()
    try:
        run(["git", "init", "-q"], tmp)
        run(["git", "remote", "add", "origin", f"https://github.com/{repo}.git"], tmp)
        run(["git", "fetch", "-q", "--depth", "1", "origin", commit], tmp)
        run(["git", "checkout", "-q", "--detach", "FETCH_HEAD"], tmp)
        os.replace(tmp, dst)
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    return dst


def front_name(skill_md):
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    m = FRONT_NAME.search(text[: end if end >= 0 else len(text)])
    return m.group(1).strip() if m else None


def resolve(root, selector, cid):
    typ = selector["type"]
    if typ == "path":
        p = root / selector["path"]
        if not (p / "SKILL.md").exists():
            raise RuntimeError(f"{cid}: no SKILL.md at {selector['path']}")
        return p
    if typ == "repo_root":
        if not (root / "SKILL.md").exists():
            raise RuntimeError(f"{cid}: repository root has no SKILL.md")
        return root
    wanted = selector["name"].casefold()
    found = []
    for rel in selector.get("roots", ["."]):
        start = (root / rel).resolve()
        try:
            start.relative_to(root.resolve())
        except ValueError:
            continue
        if not start.exists():
            continue
        for f in start.rglob("SKILL.md"):
            n = front_name(f)
            if (n and n.casefold() == wanted) or f.parent.name.casefold() == wanted:
                found.append(f.parent.resolve())
    found = list(dict.fromkeys(found))
    if len(found) != 1:
        raise RuntimeError(f"{cid}: selector {selector['name']!r} resolved {len(found)} packages")
    return found[0]


def digest(root):
    root = Path(root)
    h = hashlib.sha256()
    for p in sorted(root.rglob("*")):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(root).as_posix()
        if p.is_symlink():
            h.update(rel.encode() + b"\0SYMLINK\0")
            h.update(os.readlink(p).encode("utf-8") + b"\0")
        elif p.is_file():
            h.update(rel.encode() + b"\0")
            h.update(p.read_bytes())
            h.update(b"\0")
    return h.hexdigest()


def copy_pkg(src, dst):
    if dst.exists() or dst.is_symlink():
        if dst.is_dir() and not dst.is_symlink():
            shutil.rmtree(dst)
        else:
            dst.unlink()
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, symlinks=True, ignore=shutil.ignore_patterns(".git"))


def _atomic_json_write(path, data):
    path = Path(path)
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


def expand_registry(reg):
    employees, support = {}, {}
    for sid, source in reg["sources"].items():
        for p in source.get("packages", []):
            if p.get("root"):
                selector = {"type": "repo_root", "path": "."}
            elif p.get("path"):
                selector = {"type": "path", "path": p["path"]}
            else:
                selector = {
                    "type": "skill_name",
                    "name": p.get("name", p["id"]),
                    "roots": p.get("roots", ["."]),
                }
            employees[p["id"]] = {
                **p,
                "source": sid,
                "repo": source["repo"],
                "commit": source["commit"],
                "namespace": source["namespace"],
                "mode": "vendored" if p.get("vendored") else "upstream-fetch",
                "target": f"imported/{source['namespace']}/{p['id']}",
                "selector": selector,
                "deps": p.get("deps", []),
                "operators": p.get("operators", []),
            }
    for p in reg.get("support", []):
        source = reg["sources"][p["source"]]
        support[p["id"]] = {
            **p,
            "repo": source["repo"],
            "commit": source["commit"],
            "namespace": source["namespace"],
            "target": f"dependencies/{source['namespace']}/{p['id']}",
            "selector": {"type": "path", "path": p["path"]},
        }
    return employees, support


def install_plan(profile_name, root):
    reg = load("registry/packages.json")
    profiles = load("registry/profiles.json")
    employees, support = expand_registry(reg)
    if profile_name not in profiles["profiles"]:
        raise RuntimeError(f"Unknown profile: {profile_name}")
    prof = profiles["profiles"][profile_name]
    out, deps = [], set()
    if prof.get("include_foundation", True):
        for d in sorted((REPO_ROOT / "skills" / "foundation").iterdir()):
            if (d / "SKILL.md").exists():
                out.append(("foundation", d.name, d, root / "foundation" / d.name, None))
    for cid in prof["employee_skills"]:
        p = employees[cid]
        deps.update(p["deps"])
        src = REPO_ROOT / "skills" / p["target"] if p["mode"] == "vendored" else None
        out.append(("employee", cid, src, root / p["target"], p))
    for sid in sorted(deps):
        p = support[sid]
        out.append(("support", sid, None, root / p["target"], p))
    return out


def manifest_for(profile, installed, generation_id, stage):
    return {
        "schema_version": 2,
        "generation_schema_version": GENERATION_SCHEMA_VERSION,
        "distribution": "AI-Verse-Skills",
        "snapshot": load("registry/packages.json").get("snapshot"),
        "profile": profile,
        "generation_id": generation_id,
        "generation_digest_sha256": generation_content_digest(stage),
        "installed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "packages": installed,
    }


def _write_stage_manifest(profile, installed, generation_id, stage):
    meta = stage / ".aiverse"
    meta.mkdir(parents=True, exist_ok=True)
    _atomic_json_write(meta / "installed.json", manifest_for(profile, installed, generation_id, stage))


def build_stage(profile, stage, cache, generation_id, offline=False):
    jobs = install_plan(profile, stage)
    installed, checkouts = [], {}
    for kind, cid, src, dst, p in jobs:
        if src is None:
            key = (p["repo"], p["commit"])
            co = checkouts.get(key)
            if co is None:
                co = checkout(*key, cache, offline)
                checkouts[key] = co
            src = resolve(co, p["selector"], cid)
        if not (src / "SKILL.md").exists():
            raise RuntimeError(f"{cid}: source package missing SKILL.md")
        copy_pkg(src, dst)
        installed.append({
            "kind": kind,
            "id": cid,
            "path": str(dst.relative_to(stage)),
            "source_repo": p.get("repo") if p else "aiverse-filmmakers/AI-Verse-Skills",
            "source_commit": p.get("commit") if p else None,
            "operators": p.get("operators", []) if p else [],
            "digest_sha256": digest(dst),
        })
        print("staged", cid)
    _write_stage_manifest(profile, installed, generation_id, stage)
    return installed


def _read_json(path, label):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Invalid {label} {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Invalid {label} {path}: expected JSON object")
    return data


def verify_stage(stage, expected_generation_id=None):
    mf = stage / ".aiverse" / "installed.json"
    if not mf.is_file():
        return [f"missing install manifest: {mf}"]
    try:
        data = _read_json(mf, "install manifest")
    except RuntimeError as exc:
        return [str(exc)]
    errors = []
    if data.get("generation_schema_version") != GENERATION_SCHEMA_VERSION:
        errors.append("generation manifest schema mismatch")
    if expected_generation_id and data.get("generation_id") != expected_generation_id:
        errors.append("generation id mismatch")
    for p in data.get("packages", []):
        d = stage / p["path"]
        if not (d / "SKILL.md").exists():
            errors.append(f"{p['id']}: missing SKILL.md")
        elif digest(d) != p.get("digest_sha256"):
            errors.append(f"{p['id']}: content digest changed")
    if generation_content_digest(stage) != data.get("generation_digest_sha256"):
        errors.append("generation content digest changed")
    return errors


def _legacy_manifest_path(root):
    return Path(root) / ".aiverse" / "installed.json"


def _is_lifecycle(root):
    return active_pointer_path(Path(root)).is_file()


def _is_legacy_install(root):
    return _legacy_manifest_path(root).is_file() and not _is_lifecycle(root)


def _verify_legacy_root(root):
    mf = _legacy_manifest_path(root)
    errors = []
    if not mf.exists():
        return [f"missing install manifest: {mf}"]
    try:
        data = _read_json(mf, "legacy install manifest")
    except RuntimeError as exc:
        return [str(exc)]
    for p in data.get("packages", []):
        d = Path(root) / p["path"]
        if not (d / "SKILL.md").exists():
            errors.append(f"{p['id']}: missing SKILL.md")
        elif digest(d) != p.get("digest_sha256"):
            errors.append(f"{p['id']}: content digest changed")
    return errors


def verify_root(root):
    root = Path(root).expanduser().resolve()
    if _is_lifecycle(root):
        try:
            pointer = read_active_pointer(root)
        except RuntimeError as exc:
            return [str(exc)]
        return verify_generation(root, str(pointer["generation_id"]), digest)
    if _is_legacy_install(root):
        return _verify_legacy_root(root)
    return [f"No AI-Verse-Skills install found at {root}"]


def backup_dir(root):
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = root.parent / "backups"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{root.name}-{stamp}-{uuid.uuid4().hex[:6]}"


def _finalize_legacy_stage(stage, generation_id):
    mf = stage / ".aiverse" / "installed.json"
    data = _read_json(mf, "legacy install manifest")
    data["generation_schema_version"] = GENERATION_SCHEMA_VERSION
    data["generation_id"] = generation_id
    data["generation_digest_sha256"] = generation_content_digest(stage)
    data.setdefault("installed_at", dt.datetime.now(dt.timezone.utc).isoformat())
    _atomic_json_write(mf, data)


def _migrate_legacy_under_lock(root):
    """Move a mutable schema-2 install into one immutable generation."""

    root = Path(root).resolve()
    errors = _verify_legacy_root(root)
    if errors:
        raise RuntimeError("Legacy install failed verification before migration:\n" + "\n".join(errors))
    backup = backup_dir(root)
    os.replace(root, backup)
    root.mkdir(parents=True, exist_ok=True)
    stage = root.parent / f".{root.name}.legacy-stage-{uuid.uuid4().hex[:8]}"
    generation_id = new_generation_id()
    try:
        shutil.copytree(backup, stage, symlinks=True)
        _finalize_legacy_stage(stage, generation_id)
        errors = verify_stage(stage, generation_id)
        if errors:
            raise RuntimeError("Migrated legacy generation failed verification:\n" + "\n".join(errors))
        commit_stage(root, stage, generation_id)
        activate_generation(root, generation_id)
        return generation_id, backup
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        shutil.rmtree(root, ignore_errors=True)
        if backup.exists():
            os.replace(backup, root)
        raise


def transactional_install(profile, root, cache, offline=False):
    """Build, verify, commit and atomically activate one immutable generation."""

    root = Path(root).expanduser().resolve()
    cache = Path(cache).expanduser()
    root.parent.mkdir(parents=True, exist_ok=True)
    stage = root.parent / f".{root.name}.stage-{uuid.uuid4().hex[:8]}"
    generation_id = new_generation_id()
    stage.mkdir()
    legacy_backup = None
    created_controller = False
    committed = None
    try:
        with lifecycle_lock(root):
            if root.exists() and not _is_lifecycle(root) and not _is_legacy_install(root):
                if any(root.iterdir()):
                    raise RuntimeError(f"Refusing to replace unrecognized non-empty directory: {root}")
            installed = build_stage(profile, stage, cache, generation_id, offline)
            errors = verify_stage(stage, generation_id)
            if errors:
                raise RuntimeError("Staged install failed verification:\n" + "\n".join(errors))

            if _is_legacy_install(root):
                _, legacy_backup = _migrate_legacy_under_lock(root)
            elif not root.exists():
                root.mkdir(parents=True, exist_ok=True)
                created_controller = True

            previous = None
            if _is_lifecycle(root):
                try:
                    before = read_active_pointer(root, allow_uninstalled=True)
                    if before.get("state") == "active":
                        previous = str(before.get("generation_id"))
                except RuntimeError:
                    previous = None

            committed = commit_stage(root, stage, generation_id)
            errors = verify_generation(root, generation_id, digest)
            if errors:
                raise RuntimeError("Committed generation failed verification:\n" + "\n".join(errors))
            activate_generation(root, generation_id)
            return installed, previous, legacy_backup, generation_id
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        if committed and committed.exists():
            try:
                pointer = read_active_pointer(root, allow_uninstalled=True)
                if pointer.get("generation_id") != generation_id:
                    shutil.rmtree(committed, ignore_errors=True)
            except Exception:
                shutil.rmtree(committed, ignore_errors=True)
        if created_controller and root.exists() and not active_pointer_path(root).exists():
            shutil.rmtree(root, ignore_errors=True)
        raise


def load_manifest(root):
    root = Path(root).expanduser().resolve()
    if _is_lifecycle(root):
        return pin_active_generation(root, digest).manifest
    mf = _legacy_manifest_path(root)
    if mf.exists():
        return _read_json(mf, "legacy install manifest")
    raise RuntimeError(f"No AI-Verse-Skills install found at {root}")


def command_exists(*names):
    return any(shutil.which(x) for x in names)


def env_ready(name):
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "ready", "connected"}


def app_exists(kind):
    system = platform.system()
    if kind == "premiere-pro":
        if system == "Darwin":
            return any(Path("/Applications").glob("Adobe Premiere Pro*/Adobe Premiere Pro*.app"))
        if system == "Windows":
            base = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
            return any(base.glob("Adobe/Adobe Premiere Pro*"))
    if kind == "after-effects":
        if system == "Darwin":
            return any(Path("/Applications").glob("Adobe After Effects*/Adobe After Effects*.app"))
        if system == "Windows":
            base = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
            return any(base.glob("Adobe/Adobe After Effects*"))
    return False


def operator_status(op):
    oid = op["id"]
    if oid == "ffmpeg":
        return "ready" if command_exists("ffmpeg") and command_exists("ffprobe") else "missing-local-dependency"
    if oid in {"premiere-pro", "after-effects"}:
        return "ready" if app_exists(oid) else "missing-local-app"
    if oid == "google-workspace":
        return "ready" if (command_exists("gws") or env_ready("AI_VERSE_CONNECTION_GOOGLE_WORKSPACE")) else "needs-connection"
    if oid == "hubspot":
        return "ready" if (command_exists("hs") or env_ready("AI_VERSE_CONNECTION_HUBSPOT")) else "needs-connection"
    env_map = {
        "canva": "AI_VERSE_CONNECTION_CANVA",
        "figma": "AI_VERSE_CONNECTION_FIGMA",
        "shopify": "AI_VERSE_CONNECTION_SHOPIFY",
        "airtable": "AI_VERSE_CONNECTION_AIRTABLE",
        "notion": "AI_VERSE_CONNECTION_NOTION",
    }
    if oid in env_map:
        return "ready" if env_ready(env_map[oid]) else "needs-connection"
    return "host-runtime"


def readiness(root):
    ops = load("registry/operators.json")["operators"]
    statuses = {op["id"]: operator_status(op) for op in ops}
    out = {"operators": statuses, "skills": {"ready": [], "conditional": []}}
    try:
        manifest = load_manifest(root)
    except RuntimeError:
        manifest = None
    if manifest:
        for p in manifest["packages"]:
            if p["kind"] == "support":
                continue
            required = p.get("operators", [])
            if not required or all(statuses.get(x) == "ready" for x in required):
                out["skills"]["ready"].append(p["id"])
            else:
                out["skills"]["conditional"].append({
                    "id": p["id"],
                    "operators": {x: statuses.get(x, "unknown") for x in required},
                })
    return out


def _print_install_result(verb, root, installed, previous, legacy_backup, generation_id):
    print(f"{verb} {len(installed)} packages in immutable generation {generation_id}")
    print("Active root:", root)
    if previous:
        print("Rollback generation:", previous)
    if legacy_backup:
        print("Legacy migration backup:", legacy_backup)


def cmd_install(a):
    root = Path(a.root).expanduser()
    cache = Path(a.cache).expanduser()
    if a.dry_run:
        for kind, cid, src, dst, p in install_plan(a.profile, root):
            origin = str(src) if src else f"{p['repo']}@{p['commit']}::{p['selector']}"
            print(f"{kind:10} {cid:32} -> <new-generation>/{dst.relative_to(root)} [{origin}]")
        return
    installed, previous, legacy_backup, generation_id = transactional_install(a.profile, root, cache, a.offline)
    _print_install_result("Installed", root, installed, previous, legacy_backup, generation_id)


def cmd_update(a):
    root = Path(a.root).expanduser()
    existing = load_manifest(root)
    profile = a.profile or existing.get("profile", "full")
    installed, previous, legacy_backup, generation_id = transactional_install(
        profile, root, Path(a.cache).expanduser(), a.offline
    )
    _print_install_result("Updated", root, installed, previous, legacy_backup, generation_id)


def cmd_rollback(a):
    root = Path(a.root).expanduser().resolve()
    with lifecycle_lock(root):
        if _is_legacy_install(root):
            generation_id, backup = _migrate_legacy_under_lock(root)
            print("Migrated legacy install to generation", generation_id)
            print("Legacy migration backup:", backup)
        if not _is_lifecycle(root):
            raise RuntimeError(f"No immutable generation lifecycle found at {root}")
        pin = rollback_active_generation(root, digest)
    print("Rolled back to immutable generation", pin.generation_id)


def cmd_doctor(a):
    root = Path(a.root).expanduser()
    errors = verify_root(root)
    if errors:
        for e in errors:
            print("ERROR", e)
        raise SystemExit(1)
    if _is_legacy_install(root):
        print("WARNING legacy mutable install layout; run update to migrate to immutable generations")
    else:
        pin = pin_active_generation(root, digest)
        print(f"AI-Verse-Skills doctor: healthy generation={pin.generation_id}")
    if a.readiness:
        r = readiness(root)
        print(f"Skills immediately ready: {len(r['skills']['ready'])}")
        print(f"Skills requiring app/connection/runtime support: {len(r['skills']['conditional'])}")


def cmd_readiness(a):
    root = Path(a.root).expanduser()
    r = readiness(root)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print("Operator readiness")
    for oid, status in r["operators"].items():
        print(f"  {oid:<24} {status}")
    print(f"\nSkills ready now: {len(r['skills']['ready'])}")
    print(f"Skills conditional: {len(r['skills']['conditional'])}")
    if r["skills"]["conditional"]:
        print("\nConditional skills")
        for item in r["skills"]["conditional"]:
            req = ", ".join(f"{k}={v}" for k, v in item["operators"].items())
            print(f"  {item['id']:<32} {req}")


def cmd_list(a):
    reg = load("registry/packages.json")
    rows = []
    for sid, source in reg["sources"].items():
        for p in source.get("packages", []):
            rows.append((p["rank"], p["id"], sid, "vendored" if p.get("vendored") else "upstream-fetch"))
    for rank, cid, sid, mode in sorted(rows):
        print(f"{rank:>2}  {cid:<32} {sid:<20} {mode}")


def cmd_uninstall(a):
    root = Path(a.root).expanduser().resolve()
    with lifecycle_lock(root):
        legacy_backup = None
        if _is_legacy_install(root):
            _, legacy_backup = _migrate_legacy_under_lock(root)
        if not _is_lifecycle(root):
            raise RuntimeError(f"Refusing to uninstall unrecognized directory: {root}")
        pointer = read_active_pointer(root)
        generation_id = str(pointer["generation_id"])
        mark_uninstalled(root)
    print("Uninstalled", root)
    print("Recoverable immutable generation:", generation_id)
    if legacy_backup:
        print("Legacy migration backup:", legacy_backup)


def _replace_adapter_package(src, dst, force, prefer_copy=False):
    dst = Path(dst)
    if (dst.exists() or dst.is_symlink()) and not force:
        raise RuntimeError(f"Adapter destination exists: {dst}")
    tmp = dst.parent / f".{dst.name}.aiverse-stage-{uuid.uuid4().hex[:8]}"
    old = dst.parent / f".{dst.name}.aiverse-old-{uuid.uuid4().hex[:8]}"
    try:
        if not prefer_copy:
            try:
                tmp.symlink_to(src, target_is_directory=True)
                mode = "symlink"
            except OSError:
                shutil.copytree(src, tmp, symlinks=True)
                mode = "copy"
        else:
            shutil.copytree(src, tmp, symlinks=True)
            mode = "copy"
        had_old = dst.exists() or dst.is_symlink()
        if had_old:
            os.replace(dst, old)
        try:
            os.replace(tmp, dst)
        except Exception:
            if had_old and old.exists() and not dst.exists():
                os.replace(old, dst)
            raise
        if old.exists() or old.is_symlink():
            if old.is_dir() and not old.is_symlink():
                shutil.rmtree(old)
            else:
                old.unlink()
        return mode
    finally:
        if tmp.exists() or tmp.is_symlink():
            if tmp.is_dir() and not tmp.is_symlink():
                shutil.rmtree(tmp, ignore_errors=True)
            else:
                tmp.unlink(missing_ok=True)


def materialize_adapter(root, target, runtime, *, force=False, prefer_copy=False):
    root = Path(root).expanduser().resolve()
    target = Path(target).expanduser().resolve()
    pin = pin_active_generation(root, digest)
    runtimes = {x["id"] for x in load("registry/runtime-adapters.json")["adapters"]}
    if runtime not in runtimes or runtime == "aiverse-os":
        raise RuntimeError("AI-Verse OS uses the external library directly; do not materialize skills into the OS repo")
    target.mkdir(parents=True, exist_ok=True)
    index = []
    for p in pin.manifest["packages"]:
        if p["kind"] == "support":
            continue
        src = pin.generation_path / p["path"]
        dst = target / p["id"]
        mode = _replace_adapter_package(src, dst, force, prefer_copy=prefer_copy)
        index.append({
            "id": p["id"],
            "source": str(src),
            "target": str(dst),
            "mode": mode,
            "digest_sha256": p["digest_sha256"],
        })
    adapter_manifest = {
        "schema_version": ADAPTER_SCHEMA_VERSION,
        "runtime": runtime,
        "source_root": str(root),
        "generation_id": pin.generation_id,
        "generation_digest_sha256": pin.generation_digest_sha256,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "packages": index,
    }
    _atomic_json_write(target / ".aiverse-adapter.json", adapter_manifest)
    return adapter_manifest


def verify_adapter_target(root, target, *, require_active=True):
    root = Path(root).expanduser().resolve()
    target = Path(target).expanduser().resolve()
    mf = target / ".aiverse-adapter.json"
    if not mf.is_file():
        return [f"missing adapter manifest: {mf}"]
    try:
        data = _read_json(mf, "adapter manifest")
    except RuntimeError as exc:
        return [str(exc)]
    errors = []
    if data.get("schema_version") != ADAPTER_SCHEMA_VERSION:
        errors.append(f"unsupported adapter schema {data.get('schema_version')!r}")
    generation_id = data.get("generation_id")
    if not isinstance(generation_id, str) or not generation_id:
        return errors + ["adapter manifest is not bound to a generation"]
    try:
        generation_manifest = read_generation_manifest(root, generation_id)
    except RuntimeError as exc:
        return errors + [str(exc)]
    if data.get("generation_digest_sha256") != generation_manifest.get("generation_digest_sha256"):
        errors.append("adapter generation digest does not match canonical generation")
    if require_active:
        try:
            active = read_active_pointer(root)
            if active.get("generation_id") != generation_id:
                errors.append(
                    f"stale adapter generation {generation_id}; active generation is {active.get('generation_id')}"
                )
        except RuntimeError as exc:
            errors.append(str(exc))
    generation_root = generation_path(root, generation_id)
    package_by_id = {p["id"]: p for p in generation_manifest.get("packages", [])}
    for item in data.get("packages", []):
        package_id = item.get("id")
        package = package_by_id.get(package_id)
        if not package:
            errors.append(f"{package_id}: adapter package absent from generation manifest")
            continue
        dst = target / str(package_id)
        expected_src = (generation_root / package["path"]).resolve()
        if item.get("digest_sha256") != package.get("digest_sha256"):
            errors.append(f"{package_id}: adapter manifest digest mismatch")
            continue
        if item.get("mode") == "symlink":
            if not dst.is_symlink():
                errors.append(f"{package_id}: expected adapter symlink")
            else:
                try:
                    if dst.resolve() != expected_src:
                        errors.append(f"{package_id}: adapter symlink targets a different generation")
                except OSError:
                    errors.append(f"{package_id}: broken adapter symlink")
        elif item.get("mode") == "copy":
            if not dst.is_dir():
                errors.append(f"{package_id}: missing copied adapter package")
            elif digest(dst) != package.get("digest_sha256"):
                errors.append(f"{package_id}: copied adapter content changed")
        else:
            errors.append(f"{package_id}: unknown adapter mode {item.get('mode')!r}")
    return errors


def cmd_adapt(a):
    manifest = materialize_adapter(
        a.root, a.target, a.runtime, force=a.force, prefer_copy=getattr(a, "copy", False)
    )
    print(f"Exposed {len(manifest['packages'])} packages to {Path(a.target).expanduser()}")
    print("Pinned adapter generation:", manifest["generation_id"])


def cmd_adapter_verify(a):
    errors = verify_adapter_target(a.root, a.target, require_active=not a.allow_stale)
    if errors:
        for error in errors:
            print("ERROR", error)
        raise SystemExit(1)
    print("Adapter verified against its immutable generation")


def cmd_pin(a):
    root = Path(a.root).expanduser().resolve()
    pin = pin_active_generation(root, digest)
    data = {
        "generation_id": pin.generation_id,
        "generation_path": str(pin.generation_path),
        "generation_digest_sha256": pin.generation_digest_sha256,
    }
    if a.package:
        package = pin.package_path(a.package)
        data["package_id"] = a.package
        data["package_path"] = str(package)
        data["skill_md"] = str(package / "SKILL.md")
    if a.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        for key, value in data.items():
            print(f"{key}: {value}")


def cmd_e2e(a):
    root = Path(a.root).expanduser()
    errors = verify_root(root)
    manifest = load_manifest(root)
    canonical = [p for p in manifest["packages"] if p["kind"] != "support"]
    if manifest.get("profile") == "full" and len(canonical) != 100:
        errors.append(f"full profile materialized {len(canonical)} canonical packages, expected 100")
    if errors:
        for e in errors:
            print("ERROR", e)
        raise SystemExit(1)
    generation = manifest.get("generation_id", "legacy")
    print(f"E2E OK: {len(canonical)} canonical packages; profile={manifest.get('profile')}; generation={generation}")


def parser():
    p = argparse.ArgumentParser(prog="ai-verse-skills")
    p.add_argument("--root", default=str(DEFAULT_ROOT))
    p.add_argument("--cache", default=str(DEFAULT_CACHE))
    sub = p.add_subparsers(dest="cmd", required=True)

    q = sub.add_parser("install")
    q.add_argument("--profile", default="full")
    q.add_argument("--offline", action="store_true")
    q.add_argument("--dry-run", action="store_true")
    q.set_defaults(fn=cmd_install)

    q = sub.add_parser("update")
    q.add_argument("--profile")
    q.add_argument("--offline", action="store_true")
    q.set_defaults(fn=cmd_update)

    q = sub.add_parser("rollback")
    q.set_defaults(fn=cmd_rollback)

    q = sub.add_parser("doctor")
    q.add_argument("--readiness", action="store_true")
    q.set_defaults(fn=cmd_doctor)

    q = sub.add_parser("readiness")
    q.add_argument("--json", action="store_true")
    q.set_defaults(fn=cmd_readiness)

    q = sub.add_parser("list")
    q.set_defaults(fn=cmd_list)

    q = sub.add_parser("uninstall")
    q.set_defaults(fn=cmd_uninstall)

    q = sub.add_parser("adapt")
    q.add_argument("--runtime", required=True)
    q.add_argument("--target", required=True)
    q.add_argument("--force", action="store_true")
    q.add_argument("--copy", action="store_true", help="materialize generation-pinned copies instead of symlinks")
    q.set_defaults(fn=cmd_adapt)

    q = sub.add_parser("adapter-verify")
    q.add_argument("--target", required=True)
    q.add_argument("--allow-stale", action="store_true", help="verify generation integrity without requiring it to be active")
    q.set_defaults(fn=cmd_adapter_verify)

    q = sub.add_parser("pin")
    q.add_argument("--package")
    q.add_argument("--json", action="store_true")
    q.set_defaults(fn=cmd_pin)

    q = sub.add_parser("e2e")
    q.set_defaults(fn=cmd_e2e)
    return p


def main():
    a = parser().parse_args()
    try:
        a.fn(a)
    except RuntimeError as e:
        print("ERROR:", e, file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
