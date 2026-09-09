#!/usr/bin/env python3
"""AI-Verse Skills distribution installer.

Original-first, pinned, transactional installer for the 100-capability AI-Verse
Skills distribution. This repository remains physically separate from AI-Verse
OS and all other host runtimes. Installation never writes into an AI-Verse OS
repository.
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
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = Path.home() / ".aiverse" / "skills"
DEFAULT_CACHE = Path.home() / ".cache" / "aiverse-skills" / "sources"
FRONT_NAME = re.compile(r"(?m)^name:\s*[\"']?([^\"'\n]+)")


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
    h = hashlib.sha256()
    for p in sorted(x for x in root.rglob("*") if x.is_file() and ".git" not in x.parts):
        h.update(p.relative_to(root).as_posix().encode() + b"\0")
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


def manifest_for(profile, installed):
    return {
        "schema_version": 2,
        "distribution": "AI-Verse-Skills",
        "snapshot": load("registry/packages.json").get("snapshot"),
        "profile": profile,
        "installed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "packages": installed,
    }


def build_stage(profile, stage, cache, offline=False):
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
    meta = stage / ".aiverse"
    meta.mkdir(parents=True, exist_ok=True)
    (meta / "installed.json").write_text(
        json.dumps(manifest_for(profile, installed), indent=2) + "\n", encoding="utf-8"
    )
    return installed


def verify_root(root):
    mf = root / ".aiverse" / "installed.json"
    errors = []
    if not mf.exists():
        return [f"missing install manifest: {mf}"]
    try:
        data = json.loads(mf.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"invalid install manifest: {e}"]
    for p in data.get("packages", []):
        d = root / p["path"]
        if not (d / "SKILL.md").exists():
            errors.append(f"{p['id']}: missing SKILL.md")
        elif digest(d) != p.get("digest_sha256"):
            errors.append(f"{p['id']}: content digest changed")
    return errors


def backup_dir(root):
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = root.parent / "backups"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{root.name}-{stamp}-{uuid.uuid4().hex[:6]}"


def transactional_install(profile, root, cache, offline=False):
    root = root.resolve()
    root.parent.mkdir(parents=True, exist_ok=True)
    stage = root.parent / f".{root.name}.stage-{uuid.uuid4().hex[:8]}"
    backup = None
    stage.mkdir()
    try:
        installed = build_stage(profile, stage, cache, offline)
        errors = verify_root(stage)
        if errors:
            raise RuntimeError("staged install failed verification:\n" + "\n".join(errors))
        if root.exists():
            backup = backup_dir(root)
            os.replace(root, backup)
        try:
            os.replace(stage, root)
        except Exception:
            if backup and backup.exists() and not root.exists():
                os.replace(backup, root)
            raise
        return installed, backup
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        raise


def load_manifest(root):
    mf = root / ".aiverse" / "installed.json"
    if not mf.exists():
        raise RuntimeError(f"No AI-Verse-Skills install found at {root}")
    return json.loads(mf.read_text(encoding="utf-8"))


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
    if (root / ".aiverse" / "installed.json").exists():
        for p in load_manifest(root)["packages"]:
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


def cmd_install(a):
    root = Path(a.root).expanduser()
    cache = Path(a.cache).expanduser()
    if a.dry_run:
        for kind, cid, src, dst, p in install_plan(a.profile, root):
            origin = str(src) if src else f"{p['repo']}@{p['commit']}::{p['selector']}"
            print(f"{kind:10} {cid:32} -> {dst} [{origin}]")
        return
    installed, backup = transactional_install(a.profile, root, cache, a.offline)
    print(f"Installed {len(installed)} packages into {root}")
    if backup:
        print("Rollback point:", backup)


def cmd_update(a):
    root = Path(a.root).expanduser()
    existing = load_manifest(root)
    profile = a.profile or existing.get("profile", "full")
    installed, backup = transactional_install(profile, root, Path(a.cache).expanduser(), a.offline)
    print(f"Updated {len(installed)} packages in {root}")
    if backup:
        print("Rollback point:", backup)


def cmd_rollback(a):
    root = Path(a.root).expanduser().resolve()
    base = root.parent / "backups"
    candidates = sorted([p for p in base.glob(f"{root.name}-*") if p.is_dir()], reverse=True)
    if not candidates:
        raise RuntimeError(f"No rollback point found under {base}")
    chosen = candidates[0]
    swap = root.parent / f".{root.name}.rollback-{uuid.uuid4().hex[:8]}"
    if root.exists():
        os.replace(root, swap)
    try:
        os.replace(chosen, root)
        if swap.exists():
            os.replace(swap, chosen)
    except Exception:
        if swap.exists() and not root.exists():
            os.replace(swap, root)
        raise
    print("Rolled back using", chosen.name)


def cmd_doctor(a):
    root = Path(a.root).expanduser()
    errors = verify_root(root)
    if errors:
        for e in errors:
            print("ERROR", e)
        raise SystemExit(1)
    print("AI-Verse-Skills doctor: healthy")
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
    root = Path(a.root).expanduser()
    if not (root / ".aiverse" / "installed.json").exists():
        raise RuntimeError(f"Refusing to remove unrecognized directory: {root}")
    backup = backup_dir(root)
    os.replace(root, backup)
    print("Uninstalled", root)
    print("Recoverable copy:", backup)


def cmd_adapt(a):
    root = Path(a.root).expanduser()
    target = Path(a.target).expanduser()
    mf = root / ".aiverse" / "installed.json"
    if not mf.exists():
        raise RuntimeError("Install the library before adapting it")
    runtimes = {x["id"] for x in load("registry/runtime-adapters.json")["adapters"]}
    if a.runtime not in runtimes or a.runtime == "aiverse-os":
        raise RuntimeError("AI-Verse OS uses the external library directly; do not materialize skills into the OS repo")
    target.mkdir(parents=True, exist_ok=True)
    index = []
    for p in json.loads(mf.read_text(encoding="utf-8"))["packages"]:
        if p["kind"] == "support":
            continue
        src = root / p["path"]
        dst = target / p["id"]
        if dst.exists() or dst.is_symlink():
            if not a.force:
                raise RuntimeError(f"Adapter destination exists: {dst}")
            if dst.is_dir() and not dst.is_symlink():
                shutil.rmtree(dst)
            else:
                dst.unlink()
        try:
            dst.symlink_to(src, target_is_directory=True)
            mode = "symlink"
        except OSError:
            shutil.copytree(src, dst, symlinks=True)
            mode = "copy"
        index.append({"id": p["id"], "source": str(src), "target": str(dst), "mode": mode})
    (target / ".aiverse-adapter.json").write_text(
        json.dumps({"runtime": a.runtime, "packages": index}, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Exposed {len(index)} packages to {target}")


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
    print(f"E2E OK: {len(canonical)} canonical packages; profile={manifest.get('profile')}")


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
    q.set_defaults(fn=cmd_adapt)

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
