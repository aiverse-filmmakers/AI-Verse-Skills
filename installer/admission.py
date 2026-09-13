#!/usr/bin/env python3
"""Deterministic package admission and trust reporting for AI-Verse Skills.

Admission is deliberately separate from integrity, source trust, runtime
readiness and execution authorization. A package may be byte-correct and
admitted for inspection while still being external/untrusted, not runtime-ready
and not authorized to act.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional

try:
    from . import generation_lifecycle as lifecycle
except ImportError:
    import generation_lifecycle as lifecycle

ADMISSION_SCHEMA_VERSION = 1
ADMISSION_FILENAME = "admission.json"
_TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".py", ".js", ".ts",
    ".sh", ".ps1", ".cmd", ".bat", ".html", ".xml", ".ini", ".cfg", ".env",
}
_BIDI = {chr(x) for x in list(range(0x202A, 0x202F)) + list(range(0x2066, 0x206A))}
_SECRET_PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
]
_REVIEW_PATTERNS = [
    ("shell-download-chain", re.compile(r"(?:curl|wget)\s+[^\n|;]+(?:\||;)\s*(?:sh|bash|zsh|powershell)", re.I)),
    ("environment-harvest", re.compile(r"(?:printenv|env\s*$|os\.environ|process\.env)", re.I | re.M)),
    ("destructive-shell", re.compile(r"\brm\s+-rf\s+(?:/|~|\$HOME)\b", re.I)),
]


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _load_policy(impl: Any) -> Dict[str, Any]:
    data = impl.load("registry/trust-policy.json")
    if data.get("schema_version") != ADMISSION_SCHEMA_VERSION:
        raise RuntimeError("Unsupported trust-policy schema")
    sources = data.get("sources")
    if not isinstance(sources, dict):
        raise RuntimeError("trust-policy sources must be an object")
    return data


def _policy_for(impl: Any, package: Mapping[str, Any]) -> Dict[str, Any]:
    kind = str(package.get("kind", ""))
    if kind == "learned":
        return {
            "license": "local-private",
            "redistribution": "private-local",
            "trust": "learned-promoted",
            "ownership": str(package.get("ownership") or "agent_learned"),
            "vendoring_allowed": False,
            "auto_mutation": True,
        }
    source_repo = str(package.get("source_repo") or "aiverse-filmmakers/AI-Verse-Skills")
    policy_doc = _load_policy(impl)
    policy = policy_doc["sources"].get(source_repo)
    if not isinstance(policy, dict):
        # Unknown sources are never implicitly trusted or redistributable.
        # Registry validation still requires explicit decisions for every
        # package shipped by the public distribution.
        return {
            "license": "upstream-controlled",
            "redistribution": str(policy_doc.get("policy", {}).get("unknown_redistribution", "fetch-only")),
            "trust": "external",
            "ownership": "external",
            "vendoring_allowed": False,
            "auto_mutation": False,
        }
    return dict(policy)


def _safe_relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def scan_package(package_root: Path, *, max_text_bytes: int = 2_000_000) -> Dict[str, Any]:
    """Run deterministic package safety checks without executing package code."""

    root = Path(package_root).resolve(strict=True)
    findings: List[Dict[str, str]] = []
    text_bytes = 0
    files_scanned = 0

    for path in sorted(root.rglob("*")):
        rel_path = path.relative_to(root)
        if ".git" in rel_path.parts:
            continue
        if path.is_symlink():
            try:
                resolved = path.resolve(strict=True)
            except OSError:
                findings.append({"severity": "deny", "code": "broken-symlink", "path": rel_path.as_posix()})
                continue
            try:
                resolved.relative_to(root)
            except ValueError:
                findings.append({"severity": "deny", "code": "symlink-escape", "path": rel_path.as_posix()})
            continue
        if not path.is_file():
            continue
        files_scanned += 1
        if path.suffix.lower() not in _TEXT_SUFFIXES and path.name != "SKILL.md":
            continue
        try:
            size = path.stat().st_size
        except OSError:
            findings.append({"severity": "deny", "code": "unreadable-file", "path": rel_path.as_posix()})
            continue
        if size > max_text_bytes or text_bytes + size > max_text_bytes:
            findings.append({"severity": "review", "code": "text-scan-budget", "path": rel_path.as_posix()})
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append({"severity": "review", "code": "non-utf8-text", "path": rel_path.as_posix()})
            continue
        text_bytes += len(text.encode("utf-8"))
        if any(ch in text for ch in _BIDI):
            findings.append({"severity": "review", "code": "bidi-control", "path": rel_path.as_posix()})
        for code, pattern in _SECRET_PATTERNS:
            if pattern.search(text):
                findings.append({"severity": "deny", "code": code, "path": rel_path.as_posix()})
        for code, pattern in _REVIEW_PATTERNS:
            if pattern.search(text):
                findings.append({"severity": "review", "code": code, "path": rel_path.as_posix()})

    denied = any(item["severity"] == "deny" for item in findings)
    review = any(item["severity"] == "review" for item in findings)
    return {
        "status": "deny" if denied else ("review-required" if review else "pass"),
        "files_scanned": files_scanned,
        "text_bytes_scanned": text_bytes,
        "findings": findings,
    }


def _package_integrity(impl: Any, generation_root: Path, package: Mapping[str, Any]) -> Dict[str, Any]:
    path = generation_root / str(package.get("path", ""))
    if not path.is_dir():
        return {"status": "invalid", "reason": "package-missing"}
    expected = package.get("digest_sha256")
    actual = impl.digest(path)
    if expected and expected != actual:
        return {"status": "invalid", "reason": "digest-mismatch", "expected": expected, "actual": actual}
    portable = package.get("digest")
    if isinstance(portable, dict) and portable.get("value"):
        try:
            from .provider_contract_v1 import package_digest_v1
        except ImportError:
            from provider_contract_v1 import package_digest_v1
        actual_portable = package_digest_v1(path)
        if portable.get("value") != actual_portable:
            return {"status": "invalid", "reason": "portable-digest-mismatch"}
    return {"status": "verified"}


def build_admission_report(impl: Any, generation_root: Path, manifest: Mapping[str, Any]) -> Dict[str, Any]:
    packages: List[Dict[str, Any]] = []
    blocked = False
    for package in manifest.get("packages", []):
        if not isinstance(package, Mapping):
            blocked = True
            continue
        policy = _policy_for(impl, package)
        package_path = Path(generation_root) / str(package.get("path", ""))
        integrity = _package_integrity(impl, Path(generation_root), package)
        security = scan_package(package_path) if package_path.is_dir() else {
            "status": "deny", "findings": [{"severity": "deny", "code": "package-missing", "path": str(package_path)}]
        }
        source_trust = str(policy.get("trust", "external"))
        trusted = source_trust in {"first-party", "reviewed-upstream", "learned-promoted"} and security["status"] != "deny"
        admitted = integrity.get("status") == "verified" and security["status"] != "deny"
        if not admitted:
            blocked = True
        packages.append({
            "id": package.get("id"),
            "kind": package.get("kind"),
            "source_repo": package.get("source_repo"),
            "ownership": policy.get("ownership"),
            "protected": not bool(policy.get("auto_mutation", False)),
            "license": policy.get("license"),
            "redistribution": policy.get("redistribution"),
            "integrity": integrity,
            "security": security,
            "admission": "admitted" if admitted else "blocked",
            "trust": source_trust,
            "trusted": trusted,
            "readiness": "not-evaluated",
            "authorized": False,
        })
    return {
        "schema_version": ADMISSION_SCHEMA_VERSION,
        "generated_at": _utc_now(),
        "generation_id": manifest.get("generation_id"),
        "separation": {
            "integrity": "package bytes match immutable generation metadata",
            "admission": "package may exist in the library after deterministic policy checks",
            "trusted": "source/package trust classification, not execution permission",
            "ready": "runtime/operator usability, evaluated separately",
            "authorized": "host/user execution authority, never granted by Skills admission",
        },
        "status": "blocked" if blocked else "admitted",
        "packages": packages,
    }


def write_admission_metadata(impl: Any, generation_root: Path) -> Dict[str, Any]:
    generation_root = Path(generation_root)
    manifest = impl._read_json(generation_root / ".aiverse" / "installed.json", "provider manifest")
    report = build_admission_report(impl, generation_root, manifest)
    impl._atomic_json_write(generation_root / ".aiverse" / ADMISSION_FILENAME, report)
    if report["status"] == "blocked":
        blocked = [str(x.get("id")) for x in report["packages"] if x.get("admission") == "blocked"]
        raise RuntimeError("Package admission blocked: " + ", ".join(blocked))
    return report


def verify_admission_generation(impl: Any, generation_root: Path, expected_generation_id: Optional[str] = None) -> List[str]:
    root = Path(generation_root)
    path = root / ".aiverse" / ADMISSION_FILENAME
    if not path.is_file():
        return [f"missing admission report: {path}"]
    try:
        stored = json.loads(path.read_text(encoding="utf-8"))
        manifest = json.loads((root / ".aiverse" / "installed.json").read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid admission metadata: {exc}"]
    errors: List[str] = []
    if stored.get("schema_version") != ADMISSION_SCHEMA_VERSION:
        errors.append("unsupported admission schema")
    generation_id = manifest.get("generation_id")
    if expected_generation_id and generation_id != expected_generation_id:
        errors.append("admission generation id mismatch")
    if stored.get("generation_id") != generation_id:
        errors.append("admission report is bound to a different generation")
    try:
        current = build_admission_report(impl, root, manifest)
    except Exception as exc:
        return errors + [str(exc)]
    stored_by_id = {str(x.get("id")): x for x in stored.get("packages", []) if isinstance(x, dict)}
    current_by_id = {str(x.get("id")): x for x in current.get("packages", []) if isinstance(x, dict)}
    if set(stored_by_id) != set(current_by_id):
        errors.append("admission package set does not match generation manifest")
    for package_id, now in current_by_id.items():
        before = stored_by_id.get(package_id)
        if not before:
            continue
        for key in ("ownership", "protected", "license", "redistribution", "admission", "trust", "trusted"):
            if before.get(key) != now.get(key):
                errors.append(f"{package_id}: admission field changed: {key}")
        if before.get("integrity") != now.get("integrity"):
            errors.append(f"{package_id}: integrity evidence changed")
        if before.get("security") != now.get("security"):
            errors.append(f"{package_id}: security scan result changed")
        if before.get("authorized") is not False:
            errors.append(f"{package_id}: admission metadata must never grant authorization")
    return errors


def package_policy_projection(impl: Any, root: Path, package_id: str) -> Dict[str, Any]:
    pin = impl.pin_active_generation(Path(root), impl.digest)
    report_path = pin.generation_path / ".aiverse" / ADMISSION_FILENAME
    report = json.loads(report_path.read_text(encoding="utf-8"))
    for package in report.get("packages", []):
        if package.get("id") == package_id:
            return dict(package)
    raise RuntimeError(f"Package not present in admission report: {package_id}")


def apply_admission(impl: Any) -> None:
    if getattr(impl, "_admission_v1_applied", False):
        return
    impl._admission_v1_applied = True

    original_write = impl._write_stage_manifest
    original_verify_stage = impl.verify_stage
    original_verify_root = impl.verify_root
    original_pin = impl.pin_active_generation
    original_rollback = impl.rollback_active_generation

    def write_stage_manifest(profile, installed, generation_id, stage):
        original_write(profile, installed, generation_id, stage)
        write_admission_metadata(impl, Path(stage))

    def verify_stage(stage, expected_generation_id=None):
        errors = list(original_verify_stage(stage, expected_generation_id))
        if not errors:
            errors.extend(verify_admission_generation(impl, Path(stage), expected_generation_id))
        return errors

    def verify_root(root):
        errors = list(original_verify_root(root))
        if errors or not impl._is_lifecycle(root):
            return errors
        try:
            pointer = impl.read_active_pointer(Path(root))
            generation_id = str(pointer["generation_id"])
            generation_root = impl.generation_path(Path(root), generation_id)
        except RuntimeError as exc:
            return errors + [str(exc)]
        manifest = impl.read_generation_manifest(Path(root), generation_id)
        if manifest.get("provider_contract") == "aiverse-capability-provider-v1":
            errors.extend(verify_admission_generation(impl, generation_root, generation_id))
        return errors

    def pin(root, digest_fn):
        pinned = original_pin(Path(root), digest_fn)
        if pinned.manifest.get("provider_contract") == "aiverse-capability-provider-v1":
            errors = verify_admission_generation(impl, pinned.generation_path, pinned.generation_id)
            if errors:
                raise RuntimeError("Pinned generation failed package admission verification:\n" + "\n".join(errors))
        return pinned

    def rollback(root, digest_fn):
        pinned = original_rollback(Path(root), digest_fn)
        if pinned.manifest.get("provider_contract") == "aiverse-capability-provider-v1":
            errors = verify_admission_generation(impl, pinned.generation_path, pinned.generation_id)
            if errors:
                raise RuntimeError("Rollback generation failed package admission verification:\n" + "\n".join(errors))
        return pinned

    impl._write_stage_manifest = write_stage_manifest
    impl.verify_stage = verify_stage
    impl.verify_root = verify_root
    impl.pin_active_generation = pin
    impl.rollback_active_generation = rollback
    lifecycle.pin_active_generation = pin
    lifecycle.rollback_active_generation = rollback
    impl.build_admission_report = lambda root, manifest: build_admission_report(impl, Path(root), manifest)
    impl.write_admission_metadata = lambda root: write_admission_metadata(impl, Path(root))
    impl.verify_admission_generation = lambda root, generation_id=None: verify_admission_generation(
        impl, Path(root), generation_id
    )
    impl.package_policy_projection = lambda root, package_id: package_policy_projection(
        impl, Path(root), package_id
    )
