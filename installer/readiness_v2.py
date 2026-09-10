#!/usr/bin/env python3
"""Live readiness verification for AI-Verse Skills.

Readiness v2 deliberately separates static installation/configuration hints from
live proof. Connector/runtime-backed operators are never reported as ``ready``
from a binary existing or an environment flag alone. They require a registered
live probe that succeeds now. Deterministic local tools may self-probe directly.

The public ``operators`` map remains ``{operator_id: status}`` for compatibility.
Structured evidence is published separately under ``operator_details``.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple

READINESS_SCHEMA_VERSION = 2
PROBE_SCHEMA_VERSION = 1
DEFAULT_PROBE_TIMEOUT_SECONDS = 5.0
MAX_PROBE_TIMEOUT_SECONDS = 30.0

# Legacy environment hints are retained only as configuration hints. They can
# never make an operator ready by themselves.
ENV_HINTS = {
    "google-workspace": "AI_VERSE_CONNECTION_GOOGLE_WORKSPACE",
    "hubspot": "AI_VERSE_CONNECTION_HUBSPOT",
    "canva": "AI_VERSE_CONNECTION_CANVA",
    "figma": "AI_VERSE_CONNECTION_FIGMA",
    "shopify": "AI_VERSE_CONNECTION_SHOPIFY",
    "airtable": "AI_VERSE_CONNECTION_AIRTABLE",
    "notion": "AI_VERSE_CONNECTION_NOTION",
}

CLI_HINTS = {
    "google-workspace": ("gws",),
    "hubspot": ("hs",),
}

CONNECTION_TYPES = {"connector", "api", "mcp"}


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _truthy(value: Optional[str]) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "ready", "connected"}


def _type_tokens(operator_type: str):
    value = str(operator_type or "").lower().replace("+", " ").replace("/", " ")
    return {token for token in value.split() if token}


def _requires_authentication(op: Mapping[str, Any]) -> bool:
    return bool(_type_tokens(str(op.get("type", ""))) & CONNECTION_TYPES)


def _probe_registry_path(root: Path, env: Mapping[str, str]) -> Path:
    override = str(env.get("AI_VERSE_READINESS_PROBES", "")).strip()
    if override:
        return Path(override).expanduser()
    # Default install root is ~/.aiverse/skills, so this resolves to the
    # user-owned runtime surface ~/.aiverse/readiness/probes.json.
    return Path(root).expanduser().resolve().parent / "readiness" / "probes.json"


def _load_probe_registry(root: Path, env: Mapping[str, str]) -> Tuple[Dict[str, Mapping[str, Any]], Optional[str], Optional[str]]:
    path = _probe_registry_path(root, env)
    if not path.exists():
        return {}, None, None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}, "invalid-probe-registry", str(path)
    if not isinstance(data, dict) or data.get("schema_version") != PROBE_SCHEMA_VERSION:
        return {}, "invalid-probe-registry", str(path)
    probes = data.get("probes")
    if not isinstance(probes, dict):
        return {}, "invalid-probe-registry", str(path)
    clean: Dict[str, Mapping[str, Any]] = {}
    for oid, raw in probes.items():
        if isinstance(oid, str) and oid and isinstance(raw, dict):
            clean[oid] = raw
    return clean, None, str(path)


def _validate_probe_spec(spec: Mapping[str, Any]) -> Tuple[Optional[list], float, Optional[str]]:
    allowed = {"command", "timeout_seconds"}
    if set(spec) - allowed:
        return None, DEFAULT_PROBE_TIMEOUT_SECONDS, "invalid-probe-config"
    command = spec.get("command")
    if not isinstance(command, list) or not command or not all(isinstance(x, str) and x for x in command):
        return None, DEFAULT_PROBE_TIMEOUT_SECONDS, "invalid-probe-config"
    try:
        timeout = float(spec.get("timeout_seconds", DEFAULT_PROBE_TIMEOUT_SECONDS))
    except (TypeError, ValueError):
        return None, DEFAULT_PROBE_TIMEOUT_SECONDS, "invalid-probe-config"
    if timeout <= 0 or timeout > MAX_PROBE_TIMEOUT_SECONDS:
        return None, DEFAULT_PROBE_TIMEOUT_SECONDS, "invalid-probe-config"
    return list(command), timeout, None


def _run_registered_probe(op: Mapping[str, Any], spec: Mapping[str, Any], env: Mapping[str, str]) -> Dict[str, Any]:
    oid = str(op.get("id", ""))
    command, timeout, config_error = _validate_probe_spec(spec)
    if config_error:
        return {
            "status": config_error,
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": config_error}],
        }

    assert command is not None
    try:
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            shell=False,
            env=dict(env),
        )
    except subprocess.TimeoutExpired:
        return {
            "status": "probe-timeout",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "timeout"}],
        }
    except (OSError, ValueError):
        return {
            "status": "probe-failed",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "launch-failed"}],
        }

    if completed.returncode != 0:
        return {
            "status": "probe-failed",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "nonzero-exit"}],
        }

    try:
        payload = json.loads(completed.stdout)
    except Exception:
        return {
            "status": "invalid-probe-result",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "invalid-json"}],
        }

    allowed = {"schema_version", "operator_id", "authenticated", "reachable", "usable"}
    if not isinstance(payload, dict) or set(payload) - allowed:
        return {
            "status": "invalid-probe-result",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "invalid-shape"}],
        }
    if payload.get("schema_version") != PROBE_SCHEMA_VERSION or payload.get("operator_id") != oid:
        return {
            "status": "invalid-probe-result",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "identity-mismatch"}],
        }
    if not isinstance(payload.get("reachable"), bool) or not isinstance(payload.get("usable"), bool):
        return {
            "status": "invalid-probe-result",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "missing-health-fields"}],
        }
    if _requires_authentication(op) and not isinstance(payload.get("authenticated"), bool):
        return {
            "status": "invalid-probe-result",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "live-probe", "result": "missing-auth-field"}],
        }

    authenticated = payload.get("authenticated")
    reachable = bool(payload["reachable"])
    usable = bool(payload["usable"])
    evidence = [{
        "kind": "live-probe",
        "result": "passed" if reachable and usable else "not-ready",
        "authenticated": authenticated if isinstance(authenticated, bool) else None,
        "reachable": reachable,
        "usable": usable,
    }]

    if _requires_authentication(op) and authenticated is not True:
        return {"status": "authentication-failed", "ready": False, "live_verified": True, "evidence": evidence}
    if not reachable:
        return {"status": "unreachable", "ready": False, "live_verified": True, "evidence": evidence}
    if not usable:
        return {"status": "unusable", "ready": False, "live_verified": True, "evidence": evidence}
    return {"status": "ready", "ready": True, "live_verified": True, "evidence": evidence}


def _run_local_version(binary: str, args) -> bool:
    path = shutil.which(binary)
    if not path:
        return False
    try:
        completed = subprocess.run(
            [path] + list(args),
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
            shell=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return completed.returncode == 0


def _static_operator_report(impl: Any, op: Mapping[str, Any], env: Mapping[str, str]) -> Dict[str, Any]:
    oid = str(op.get("id", ""))
    evidence = []

    if oid == "ffmpeg":
        ffmpeg_present = bool(shutil.which("ffmpeg"))
        ffprobe_present = bool(shutil.which("ffprobe"))
        if not (ffmpeg_present and ffprobe_present):
            return {
                "status": "missing-local-dependency",
                "ready": False,
                "live_verified": False,
                "evidence": [{"kind": "local-install", "ffmpeg": ffmpeg_present, "ffprobe": ffprobe_present}],
            }
        usable = _run_local_version("ffmpeg", ["-version"]) and _run_local_version("ffprobe", ["-version"])
        return {
            "status": "ready" if usable else "installed-unusable",
            "ready": usable,
            "live_verified": usable,
            "evidence": [{"kind": "local-self-test", "result": "passed" if usable else "failed"}],
        }

    if oid in {"premiere-pro", "after-effects"}:
        installed = bool(impl.app_exists(oid))
        return {
            "status": "installed-unverified" if installed else "missing-local-app",
            "ready": False,
            "live_verified": False,
            "evidence": [{"kind": "local-app", "installed": installed}],
        }

    cli_names = CLI_HINTS.get(oid, ())
    cli_present = any(shutil.which(name) for name in cli_names)
    hint_name = ENV_HINTS.get(oid)
    configured = _truthy(env.get(hint_name)) if hint_name else False
    if cli_present:
        evidence.append({"kind": "local-cli", "installed": True})
    if configured:
        evidence.append({"kind": "configuration-hint", "present": True})

    operator_type = str(op.get("type", ""))
    if _requires_authentication(op):
        if configured:
            status = "configured-unverified"
        elif cli_present:
            status = "installed-unverified"
        else:
            status = "needs-connection"
        return {"status": status, "ready": False, "live_verified": False, "evidence": evidence}

    # Non-authenticated runtime/browser/artifact operators still need a live host
    # probe before they can be called usable.
    if any(token in _type_tokens(operator_type) for token in {"runtime", "browser", "artifact"}):
        return {
            "status": "host-runtime-unverified",
            "ready": False,
            "live_verified": False,
            "evidence": evidence,
        }

    return {"status": "unverified", "ready": False, "live_verified": False, "evidence": evidence}


def operator_report(impl: Any, op: Mapping[str, Any], root: Path, probes: Mapping[str, Mapping[str, Any]], env: Mapping[str, str]) -> Dict[str, Any]:
    oid = str(op.get("id", ""))
    checked_at = _utc_now()
    if oid in probes:
        result = _run_registered_probe(op, probes[oid], env)
    else:
        result = _static_operator_report(impl, op, env)
    return {
        "status": result["status"],
        "ready": bool(result["ready"]),
        "live_verified": bool(result["live_verified"]),
        "checked_at": checked_at,
        "evidence": result.get("evidence", []),
    }


def evaluate_readiness(impl: Any, root: Path, env: Optional[Mapping[str, str]] = None) -> Dict[str, Any]:
    env_map: Mapping[str, str] = os.environ if env is None else env
    root = Path(root).expanduser()
    ops = impl.load("registry/operators.json")["operators"]
    probes, registry_error, registry_path = _load_probe_registry(root, env_map)

    details: Dict[str, Dict[str, Any]] = {}
    for op in ops:
        oid = str(op["id"])
        if registry_error and oid in probes:
            details[oid] = {
                "status": registry_error,
                "ready": False,
                "live_verified": False,
                "checked_at": _utc_now(),
                "evidence": [{"kind": "probe-registry", "result": registry_error}],
            }
        else:
            details[oid] = operator_report(impl, op, root, probes, env_map)

    statuses = {oid: report["status"] for oid, report in details.items()}
    output: Dict[str, Any] = {
        "schema_version": READINESS_SCHEMA_VERSION,
        "checked_at": _utc_now(),
        "generation_id": None,
        "operators": statuses,
        "operator_details": details,
        "skills": {"ready": [], "conditional": []},
        "diagnostics": [],
    }
    if registry_error:
        output["diagnostics"].append({"code": registry_error, "probe_registry": registry_path})

    try:
        manifest = impl.load_manifest(root)
    except RuntimeError:
        manifest = None
    if manifest:
        generation_id = manifest.get("generation_id")
        output["generation_id"] = generation_id if isinstance(generation_id, str) else None
        for package in manifest.get("packages", []):
            if package.get("kind") == "support":
                continue
            required = [str(x) for x in package.get("operators", []) if str(x)]
            if not required or all(statuses.get(oid) == "ready" for oid in required):
                output["skills"]["ready"].append(package["id"])
            else:
                output["skills"]["conditional"].append({
                    "id": package["id"],
                    "operators": {oid: statuses.get(oid, "unknown") for oid in required},
                })
    return output


def apply_readiness_v2(impl: Any) -> None:
    """Install readiness v2 into the existing compatibility implementation."""

    if getattr(impl, "_readiness_v2_applied", False):
        return
    impl._readiness_v2_applied = True

    def operator_status_v2(op):
        probes, _, _ = _load_probe_registry(impl.DEFAULT_ROOT, os.environ)
        return operator_report(impl, op, impl.DEFAULT_ROOT, probes, os.environ)["status"]

    def readiness_v2(root):
        return evaluate_readiness(impl, Path(root))

    impl.operator_status = operator_status_v2
    impl.readiness = readiness_v2
