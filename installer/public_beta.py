#!/usr/bin/env python3
"""Public-beta lifecycle UX and orchestration surfaces for AI-Verse Skills."""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from . import learning
except ImportError:
    import learning

SETUP_SCHEMA_VERSION = 1
INTEGRATION_SCHEMA_VERSION = 1
DOCTOR_DEPTHS = ["structural", "discovery", "runtime", "dependency", "operational", "system"]


def _json_load(path: Path, default=None):
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _integration_path(root: Path) -> Path:
    return Path(root).resolve() / ".aiverse" / "integration.json"


def _setup_path(root: Path) -> Path:
    return Path(root).resolve() / ".aiverse" / "setup.json"


def _write_integration(impl: Any, root: Path, action: str) -> None:
    impl._atomic_json_write(_integration_path(root), {
        "schema_version": INTEGRATION_SCHEMA_VERSION,
        "action": action,
        "updated_at": impl.dt.datetime.now(impl.dt.timezone.utc).isoformat(),
    })


def _default_root_discovery(impl: Any, root: Path) -> Dict[str, Any]:
    canonical = Path(impl.DEFAULT_ROOT).expanduser().resolve()
    actual = Path(root).expanduser().resolve()
    return {
        "provider_contract": "aiverse-capability-provider-v1",
        "provider_id": "aiverse-skills",
        "root": str(actual),
        "default_root": actual == canonical,
        "os_discoverability": "default-root" if actual == canonical else "custom-root-host-configuration-required",
        "note": (
            "Default-root generations are dynamically discoverable by the supported AI-Verse OS provider path."
            if actual == canonical
            else "A custom Skills root must be supplied to the host/provider configuration; setup does not edit sibling repositories."
        ),
    }


def _inactive_generation_errors(impl: Any, root: Path) -> List[str]:
    try:
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
    except RuntimeError as exc:
        return [str(exc)]
    history = list(pointer.get("history", []))
    if not history:
        return ["no recoverable immutable generation"]
    generation_id = str(history[0])
    generation = impl.generation_path(root, generation_id)
    errors = list(impl.verify_generation(root, generation_id, impl.digest))
    try:
        from .provider_contract_v1 import verify_provider_generation
        from .admission import verify_admission_generation
    except ImportError:
        from provider_contract_v1 import verify_provider_generation
        from admission import verify_admission_generation
    errors.extend(verify_provider_generation(generation, generation_id))
    errors.extend(verify_admission_generation(impl, generation, generation_id))
    return errors


def status_report(impl: Any, root: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    setup = _json_load(_setup_path(root))
    integration = _json_load(_integration_path(root), {})
    if not (root / ".aiverse" / "active.json").is_file() and not impl._is_legacy_install(root):
        return {
            "component_id": "ai-verse-skills",
            "state": "absent",
            "installed": False,
            "setup": False,
            "enabled": False,
            "healthy": False,
            "migration_required": False,
        }
    if impl._is_legacy_install(root):
        errors = impl.verify_root(root)
        return {
            "component_id": "ai-verse-skills",
            "state": "migration-required" if not errors else "unhealthy",
            "installed": True,
            "setup": False,
            "enabled": True,
            "healthy": not errors,
            "migration_required": True,
            "errors": errors,
        }

    try:
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
    except RuntimeError as exc:
        return {
            "component_id": "ai-verse-skills",
            "state": "unhealthy",
            "installed": True,
            "setup": bool(setup),
            "enabled": False,
            "healthy": False,
            "migration_required": False,
            "errors": [str(exc)],
        }

    active = pointer.get("state") == "active"
    action = integration.get("action")
    if active:
        errors = impl.verify_root(root)
    else:
        errors = _inactive_generation_errors(impl, root)
    healthy = not errors

    if not active:
        state = "disabled" if action == "disabled" else ("absent" if action == "uninstalled" else "installed")
    elif not healthy:
        state = "unhealthy"
    elif not setup:
        state = "setup-required"
    else:
        state = "ready"

    return {
        "component_id": "ai-verse-skills",
        "state": state,
        "installed": state != "absent",
        "preserved_state": bool(pointer.get("history")),
        "setup": bool(setup),
        "enabled": active,
        "healthy": healthy,
        "migration_required": False,
        "generation_id": pointer.get("generation_id"),
        "recoverable_generations": list(pointer.get("history", [])),
        "integration_action": action,
        "errors": errors,
        "discoverability": _default_root_discovery(impl, root),
    }


def setup_component(impl: Any, root: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    report = status_report(impl, root)
    if report["state"] in {"absent", "unhealthy", "migration-required"}:
        raise RuntimeError(f"Skills setup cannot continue from state {report['state']}: {report.get('errors', [])}")
    if not report["enabled"]:
        raise RuntimeError("Skills is not enabled; enable or reinstall before setup")
    pin = impl.pin_active_generation(root, impl.digest)
    learning.ensure_learning_state(impl, root)
    setup = {
        "schema_version": SETUP_SCHEMA_VERSION,
        "component_id": "ai-verse-skills",
        "verified_generation_id": pin.generation_id,
        "provider_contract": pin.manifest.get("provider_contract"),
        "provider_id": pin.manifest.get("provider_id"),
        "discoverability": _default_root_discovery(impl, root),
        "authority_transfer": False,
        "permissions_granted": False,
        "authorization_granted": False,
        "learning_mode": learning.learning_status(impl, root)["mode"],
        "setup_at": impl.dt.datetime.now(impl.dt.timezone.utc).isoformat(),
    }
    impl._atomic_json_write(_setup_path(root), setup)
    _write_integration(impl, root, "enabled")
    return setup


def enable_component(impl: Any, root: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
        if pointer.get("state") != "active":
            history = list(pointer.get("history", []))
            if not history:
                raise RuntimeError("No preserved immutable generation is available to enable")
            generation_id = str(history[0])
            impl.activate_generation(root, generation_id)
        _write_integration(impl, root, "enabled")
    return status_report(impl, root)


def disable_component(impl: Any, root: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
        if pointer.get("state") == "active":
            impl.mark_uninstalled(root)
        _write_integration(impl, root, "disabled")
    return status_report(impl, root)


def doctor_report(impl: Any, root: Path, depth: str = "system") -> Dict[str, Any]:
    if depth not in DOCTOR_DEPTHS:
        raise RuntimeError("Unsupported doctor depth")
    root = Path(root).expanduser().resolve()
    status = status_report(impl, root)
    checks = {
        "structural": {"ok": status.get("healthy", False), "errors": status.get("errors", [])},
        "discovery": {"ok": bool(status.get("discoverability")), "detail": status.get("discoverability")},
    }
    if depth in {"runtime", "dependency", "operational", "system"} and status.get("enabled"):
        try:
            runtime = impl.readiness(root)
            checks["runtime"] = {"ok": True, "report": runtime}
        except Exception as exc:
            checks["runtime"] = {"ok": False, "error": str(exc)}
    if depth in {"operational", "system"}:
        try:
            ls = learning.learning_status(impl, root)
            checks["learning"] = {"ok": bool(ls["audit_ledger"]["valid"]), "report": ls}
        except Exception as exc:
            checks["learning"] = {"ok": False, "error": str(exc)}
    if depth == "system":
        checks["setup"] = {
            "ok": status.get("state") == "ready",
            "state": status.get("state"),
            "detail": "System-depth doctor requires completed setup and an enabled healthy provider.",
        }
    ok = all(bool(v.get("ok")) for v in checks.values())
    return {
        "component_id": "ai-verse-skills",
        "depth": depth,
        "ok": ok,
        "state": status.get("state"),
        "checks": checks,
    }


def component_descriptor(impl: Any, root: Path) -> Dict[str, Any]:
    try:
        version = (impl.REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        version = "unknown"
    status = status_report(impl, root)
    return {
        "schema_version": 1,
        "component_id": "ai-verse-skills",
        "version": version,
        "compatibility": {
            "provider_contract": "aiverse-capability-provider-v1",
            "generation_manifest": 3,
            "learning_contract": "aiverse-skills-learning-v1",
        },
        "install_source": "aiverse-filmmakers/AI-Verse-Skills",
        "setup_required": status.get("state") == "setup-required",
        "supported_lifecycle": [
            "install", "setup", "status", "doctor", "enable", "disable", "update", "rollback", "uninstall", "purge"
        ],
        "state": status.get("state"),
        "health": status.get("healthy"),
        "migration_required": status.get("migration_required"),
        "requested_scopes": [],
        "authority_transfer_separate": True,
        "uninstall_preserves_canonical_state": True,
        "learning_mode_default": "propose",
        "platform_paths": {
            "linux": "~/.aiverse/skills",
            "macos": "~/.aiverse/skills",
            "windows": "%USERPROFILE%\\.aiverse\\skills",
        },
    }


def purge_generations(impl: Any, root: Path, *, keep: int, confirmed: bool) -> Dict[str, Any]:
    if not confirmed:
        raise RuntimeError("Destructive purge requires --yes")
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        pointer = impl.read_active_pointer(root, allow_uninstalled=True)
        active = pointer.get("generation_id") if pointer.get("state") == "active" else None
        protected = {str(active)} if active else set()
        history = [str(x) for x in pointer.get("history", [])]
        protected.update(history[:max(0, keep)])

        # Keep every generation referenced by learning rollback/archive provenance.
        base = learning.learning_dir(root)
        proposals = base / "proposals"
        if proposals.exists():
            for d in proposals.iterdir():
                p = _json_load(d / "proposal.json", {})
                for key in ("target_generation_id", "applied_generation_id", "backup_generation_id", "rollback_generation_id"):
                    if p.get(key):
                        protected.add(str(p[key]))
        archive = base / "archive"
        if archive.exists():
            for record in archive.glob("*/archive.json"):
                data = _json_load(record, {})
                for key in ("source_generation_id", "archived_generation_id"):
                    if data.get(key):
                        protected.add(str(data[key]))

        removed = []
        generation_root = impl.generations_dir(root)
        if generation_root.exists():
            for d in sorted(generation_root.iterdir()):
                if d.is_dir() and d.name not in protected:
                    shutil.rmtree(d)
                    removed.append(d.name)
        pointer["history"] = [x for x in history if impl.generation_path(root, x).exists()]
        impl._atomic_json_write(impl.active_pointer_path(root), pointer)
        learning.append_audit(root, "lifecycle.purge", {"removed": removed, "protected": sorted(protected)})
    return {"removed": removed, "protected": sorted(protected), "automatic_purge": False}


def _print(data: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2, sort_keys=True))
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(data)


def _capture(fn, arg) -> str:
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        fn(arg)
    return stream.getvalue().strip()


def _envelope_from_args(args) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if getattr(args, "envelope", None):
        data = json.loads(Path(args.envelope).expanduser().read_text(encoding="utf-8"))
    if getattr(args, "kind", None):
        data["kind"] = args.kind
    if getattr(args, "skill_id", None):
        data["skill_id"] = args.skill_id
    if getattr(args, "target_skill_id", None):
        data["target_skill_id"] = args.target_skill_id
    if getattr(args, "summary", None):
        data["summary"] = args.summary
    data.setdefault("suggested_owner", "skills")
    data.setdefault("evidence_refs", [])
    data.setdefault("risk", "medium")
    data.setdefault("confidence", 1.0 if getattr(args, "explicit", False) else 0.5)
    return data


def apply_public_beta(impl: Any) -> None:
    if getattr(impl, "_public_beta_v1_applied", False):
        return
    impl._public_beta_v1_applied = True
    base_parser = impl.parser

    original = {
        "install": impl.cmd_install,
        "update": impl.cmd_update,
        "rollback": impl.cmd_rollback,
        "doctor": impl.cmd_doctor,
        "uninstall": impl.cmd_uninstall,
    }

    def parser():
        p = base_parser()
        sub_action = next(a for a in p._actions if a.__class__.__name__ == "_SubParsersAction")
        choices = sub_action.choices

        def add_json(name):
            if not any(getattr(x, "dest", None) == "json" for x in choices[name]._actions):
                choices[name].add_argument("--json", action="store_true")

        for name in ("install", "update", "rollback", "doctor", "uninstall"):
            add_json(name)

        if not any(getattr(x, "dest", None) == "depth" for x in choices["doctor"]._actions):
            choices["doctor"].add_argument("--depth", choices=DOCTOR_DEPTHS, default="system")

        def wrap_existing(name):
            def command(a):
                if getattr(a, "json", False):
                    output = _capture(original[name], a)
                    if name == "uninstall":
                        _write_integration(impl, Path(a.root).expanduser().resolve(), "uninstalled")
                    payload = status_report(impl, Path(a.root))
                    payload["command"] = name
                    payload["legacy_output"] = output
                    _print(payload, True)
                else:
                    original[name](a)
                    if name == "uninstall":
                        _write_integration(impl, Path(a.root).expanduser().resolve(), "uninstalled")
            return command

        for name in ("install", "update", "rollback", "uninstall"):
            choices[name].set_defaults(fn=wrap_existing(name))

        def doctor_cmd(a):
            data = doctor_report(impl, Path(a.root), a.depth)
            if a.json:
                _print(data, True)
            else:
                if data["ok"]:
                    print(f"AI-Verse-Skills doctor: healthy depth={data['depth']} state={data['state']}")
                else:
                    print(f"AI-Verse-Skills doctor: unhealthy depth={data['depth']} state={data['state']}")
                    for name, check in data["checks"].items():
                        if not check.get("ok"):
                            print("ERROR", name, check.get("errors") or check.get("error"))
                    raise SystemExit(1)
        choices["doctor"].set_defaults(fn=doctor_cmd)

        q = sub_action.add_parser("setup")
        q.add_argument("--json", action="store_true")
        q.set_defaults(fn=lambda a: _print(setup_component(impl, Path(a.root)), a.json))

        q = sub_action.add_parser("status")
        q.add_argument("--json", action="store_true")
        q.set_defaults(fn=lambda a: _print(status_report(impl, Path(a.root)), a.json))

        q = sub_action.add_parser("enable")
        q.add_argument("--json", action="store_true")
        q.set_defaults(fn=lambda a: _print(enable_component(impl, Path(a.root)), a.json))

        q = sub_action.add_parser("disable")
        q.add_argument("--json", action="store_true")
        q.set_defaults(fn=lambda a: _print(disable_component(impl, Path(a.root)), a.json))

        q = sub_action.add_parser("descriptor")
        q.add_argument("--json", action="store_true", default=True)
        q.set_defaults(fn=lambda a: _print(component_descriptor(impl, Path(a.root)), True))

        q = sub_action.add_parser("purge")
        q.add_argument("--keep", type=int, default=2)
        q.add_argument("--yes", action="store_true")
        q.add_argument("--json", action="store_true")
        q.set_defaults(fn=lambda a: _print(
            purge_generations(impl, Path(a.root), keep=a.keep, confirmed=a.yes), a.json
        ))

        def add_candidate_args(q):
            q.add_argument("--envelope")
            q.add_argument("--candidate-dir")
            q.add_argument("--kind", choices=sorted(learning.ALLOWED_KINDS))
            q.add_argument("--skill-id")
            q.add_argument("--target-skill-id")
            q.add_argument("--summary")
            q.add_argument("--json", action="store_true")

        q = sub_action.add_parser("learn")
        add_candidate_args(q)
        q.set_defaults(explicit=True)
        def learn_cmd(a):
            env = _envelope_from_args(a)
            result = learning.submit_candidate(
                impl, Path(a.root), env,
                Path(a.candidate_dir) if a.candidate_dir else None,
                trigger="explicit-learn", explicit=True,
            )
            _print(result, a.json)
        q.set_defaults(fn=learn_cmd)

        q = sub_action.add_parser("refine")
        add_candidate_args(q)
        q.set_defaults(explicit=True)
        def refine_cmd(a):
            env = _envelope_from_args(a)
            result = learning.submit_candidate(
                impl, Path(a.root), env,
                Path(a.candidate_dir) if a.candidate_dir else None,
                trigger="explicit-refine", explicit=True,
            )
            _print(result, a.json)
        q.set_defaults(fn=refine_cmd)

        q = sub_action.add_parser("learning")
        ls = q.add_subparsers(dest="learning_cmd", required=True)
        x = ls.add_parser("status"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.learning_status(impl, Path(a.root)), a.json))
        x = ls.add_parser("mode"); x.add_argument("mode", choices=["off", "propose", "auto"]); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.set_learning_mode(impl, Path(a.root), a.mode), a.json))
        x = ls.add_parser("submit"); add_candidate_args(x); x.set_defaults(explicit=False)
        x.add_argument("--trigger", default="brain")
        def submit_cmd(a):
            env = _envelope_from_args(a)
            result = learning.submit_candidate(
                impl, Path(a.root), env,
                Path(a.candidate_dir) if a.candidate_dir else None,
                trigger=a.trigger, explicit=False,
            )
            _print(result, a.json)
        x.set_defaults(fn=submit_cmd)

        q = sub_action.add_parser("proposals")
        ps = q.add_subparsers(dest="proposal_cmd", required=True)
        x = ps.add_parser("list"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.list_proposals(Path(a.root)), a.json))
        x = ps.add_parser("inspect"); x.add_argument("proposal_id"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning._load_proposal(Path(a.root), a.proposal_id), a.json))
        x = ps.add_parser("attach"); x.add_argument("proposal_id"); x.add_argument("--candidate-dir", required=True); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.attach_candidate(impl, Path(a.root), a.proposal_id, Path(a.candidate_dir)), a.json))
        x = ps.add_parser("evaluate"); x.add_argument("proposal_id"); x.add_argument("--apply-auto", action="store_true"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.evaluate_proposal(impl, Path(a.root), a.proposal_id, auto_apply=a.apply_auto), a.json))
        x = ps.add_parser("apply"); x.add_argument("proposal_id"); x.add_argument("--approved-by"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.apply_proposal(impl, Path(a.root), a.proposal_id, approved_by=a.approved_by), a.json))
        x = ps.add_parser("reject"); x.add_argument("proposal_id"); x.add_argument("--reason", default=""); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.reject_proposal(impl, Path(a.root), a.proposal_id, a.reason), a.json))
        x = ps.add_parser("quarantine"); x.add_argument("proposal_id"); x.add_argument("--reason", default=""); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.quarantine_proposal(impl, Path(a.root), a.proposal_id, a.reason), a.json))
        x = ps.add_parser("rollback"); x.add_argument("proposal_id"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.rollback_learning_change(impl, Path(a.root), a.proposal_id), a.json))

        q = sub_action.add_parser("curator")
        cs = q.add_subparsers(dest="curator_cmd", required=True)
        x = cs.add_parser("status"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.learning_status(impl, Path(a.root)), a.json))
        x = cs.add_parser("run"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.curator_run(impl, Path(a.root)), a.json))
        x = cs.add_parser("restore"); x.add_argument("skill_id"); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.restore_archived(impl, Path(a.root), a.skill_id), a.json))
        x = cs.add_parser("archive"); x.add_argument("skill_id"); x.add_argument("--approved-by", required=True); x.add_argument("--json", action="store_true")
        x.set_defaults(fn=lambda a: _print(learning.archive_skill(impl, Path(a.root), a.skill_id, approved_by=a.approved_by), a.json))

        q = sub_action.add_parser("usage")
        us = q.add_subparsers(dest="usage_cmd", required=True)
        x = us.add_parser("record"); x.add_argument("skill_id")
        g = x.add_mutually_exclusive_group(); g.add_argument("--success", action="store_true"); g.add_argument("--failure", action="store_true")
        x.add_argument("--json", action="store_true")
        def usage_cmd(a):
            success: Optional[bool] = True if a.success else (False if a.failure else None)
            _print(learning.record_usage(impl, Path(a.root), a.skill_id, success=success), a.json)
        x.set_defaults(fn=usage_cmd)

        return p

    impl.parser = parser
    impl.status_report = lambda root: status_report(impl, Path(root))
    impl.setup_component = lambda root: setup_component(impl, Path(root))
    impl.doctor_report = lambda root, depth="system": doctor_report(impl, Path(root), depth)
    impl.component_descriptor = lambda root: component_descriptor(impl, Path(root))
