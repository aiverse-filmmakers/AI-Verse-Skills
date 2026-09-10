#!/usr/bin/env python3
"""Capability Provider Contract v1 producer for immutable Skills generations.

This module is intentionally a narrow compatibility layer over the existing
immutable generation installer.  It publishes provider metadata inside each new
generation without making AI-Verse OS part of the Skills lifecycle.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Iterable, List, Mapping, Optional

try:
    from . import generation_lifecycle as lifecycle
except ImportError:  # direct script execution
    import generation_lifecycle as lifecycle

CONTRACT_ID = "aiverse-capability-provider-v1"
PROVIDER_ID = "aiverse-skills"
MANIFEST_SCHEMA_VERSION = 3
DIGEST_ALGORITHM = "aiverse-package-sha256-v1"
INDEX_FILENAME = "capability-index.json"
_INDEX_FIELDS = {"contract", "provider_id", "generation_id", "manifest_sha256", "capabilities"}
_RECORD_FIELDS = {
    "id", "name", "description", "visibility", "version", "path",
    "package_state", "digest", "operators", "dependencies",
}
_SEGMENT_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_HEX64_RE = re.compile(r"^[a-f0-9]{64}$")
_DRIVE_RE = re.compile(r"^[A-Za-z]:")


def _scalar(value: str) -> Optional[str]:
    value = value.strip()
    if not value or value in {"|", ">", "|-", ">-", "|+", ">+"}:
        return None
    if value[0:1] in {"\"", "'"}:
        try:
            parsed = ast.literal_eval(value)
            return str(parsed) if parsed is not None else None
        except Exception:
            return value.strip("\"'") or None
    return value


def skill_metadata(skill_md: Path) -> Dict[str, str]:
    """Read only the simple top-level frontmatter fields needed for discovery."""

    text = Path(skill_md).read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: Dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        if key not in {"name", "description", "version"}:
            continue
        parsed = _scalar(raw)
        if parsed:
            out[key] = parsed
    return out


def qualified_segment(package_id: str) -> str:
    """Map legacy package spellings to the contract's stable lowercase segment."""

    value = re.sub(r"[^a-z0-9-]+", "-", str(package_id).strip().lower())
    value = re.sub(r"-+", "-", value).strip("-")
    if not value or not _SEGMENT_RE.fullmatch(value):
        raise RuntimeError(f"Package id cannot be represented by provider contract v1: {package_id!r}")
    return value


def validate_relative_package_path(generation_root: Path, rel: str) -> Path:
    if not isinstance(rel, str) or not rel or "\x00" in rel or "\\" in rel or _DRIVE_RE.match(rel):
        raise RuntimeError(f"Invalid provider package path: {rel!r}")
    posix = PurePosixPath(rel)
    if posix.is_absolute() or any(part in {"", ".", ".."} for part in posix.parts):
        raise RuntimeError(f"Invalid provider package path: {rel!r}")
    base = Path(generation_root).resolve()
    package = (base / Path(*posix.parts)).resolve(strict=True)
    try:
        package.relative_to(base)
    except ValueError as exc:
        raise RuntimeError(f"Provider package path escapes generation: {rel!r}") from exc
    if not package.is_dir() or not (package / "SKILL.md").is_file():
        raise RuntimeError(f"Provider package is missing SKILL.md: {rel!r}")
    return package


def _validate_symlinks(package_root: Path) -> None:
    base = Path(package_root).resolve()
    for path in package_root.rglob("*"):
        if ".git" in path.relative_to(package_root).parts or not path.is_symlink():
            continue
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            raise RuntimeError(f"Broken symlink in provider package: {path}") from exc
        try:
            resolved.relative_to(base)
        except ValueError as exc:
            raise RuntimeError(f"Symlink escapes provider package: {path}") from exc


def package_digest_v1(package_root: Path) -> str:
    """Portable aiverse-package-sha256-v1 digest from the canonical contract."""

    root = Path(package_root).resolve(strict=True)
    _validate_symlinks(root)
    files = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if ".git" in rel.parts or path.is_symlink() or not path.is_file():
            continue
        posix = rel.as_posix()
        files.append((posix.encode("utf-8"), posix, path))
    h = hashlib.sha256()
    for _, rel, path in sorted(files, key=lambda item: item[0]):
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def generation_content_digest(root: Path) -> str:
    """Legacy-compatible generation digest excluding self-describing provider metadata."""

    root = Path(root)
    h = hashlib.sha256()
    excluded = {".aiverse/installed.json", f".aiverse/{INDEX_FILENAME}"}
    entries = [p for p in root.rglob("*") if p.is_file() or p.is_symlink()]
    for path in sorted(entries, key=lambda p: p.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel in excluded:
            continue
        h.update(rel.encode("utf-8") + b"\0")
        if path.is_symlink():
            h.update(b"SYMLINK\0" + os.readlink(path).encode("utf-8"))
        else:
            h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def _distribution_version(impl: Any) -> str:
    try:
        value = (impl.REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        value = ""
    return value or "unversioned"


def _static_packages(impl: Any) -> Dict[str, Mapping[str, Any]]:
    registry = impl.load("registry/packages.json")
    employees, support = impl.expand_registry(registry)
    merged: Dict[str, Mapping[str, Any]] = {}
    merged.update(employees)
    merged.update(support)
    return merged


def enrich_packages(impl: Any, installed: Iterable[Mapping[str, Any]], generation_id: str, stage: Path) -> List[Dict[str, Any]]:
    static = _static_packages(impl)
    enriched: List[Dict[str, Any]] = []
    seen_qualified = set()
    distribution_version = _distribution_version(impl)

    for raw in installed:
        item = dict(raw)
        package_id = str(item.get("id", ""))
        kind = str(item.get("kind", ""))
        if not package_id or not kind:
            raise RuntimeError("Installed package entry is missing id or kind")
        package = validate_relative_package_path(stage, str(item.get("path", "")))
        meta = skill_metadata(package / "SKILL.md")
        static_item = static.get(package_id, {})
        portable = package_digest_v1(package)
        operators = sorted({str(x) for x in item.get("operators", static_item.get("operators", [])) if str(x)})
        dependencies = sorted({str(x) for x in static_item.get("deps", []) if str(x)})
        version = meta.get("version") or item.get("source_commit") or static_item.get("commit") or distribution_version
        name = meta.get("name") or package_id
        description = meta.get("description") or f"Installed AI-Verse capability {name}."

        item.update({
            "name": str(name),
            "description": str(description),
            "version": str(version),
            "operators": operators,
            "dependencies": dependencies,
            "digest": {"algorithm": DIGEST_ALGORITHM, "value": portable},
        })
        if kind != "support":
            segment = qualified_segment(package_id)
            qualified = f"{PROVIDER_ID}:{segment}"
            if qualified in seen_qualified:
                raise RuntimeError(f"Duplicate provider capability id after normalization: {qualified}")
            seen_qualified.add(qualified)
            item["qualified_id"] = qualified
            item["legacy_id"] = package_id
        enriched.append(item)
    return enriched


def build_manifest(impl: Any, profile: str, installed: Iterable[Mapping[str, Any]], generation_id: str, stage: Path) -> Dict[str, Any]:
    packages = enrich_packages(impl, installed, generation_id, stage)
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "generation_schema_version": impl.GENERATION_SCHEMA_VERSION,
        "provider_contract": CONTRACT_ID,
        "provider_id": PROVIDER_ID,
        "distribution": "AI-Verse-Skills",
        "snapshot": impl.load("registry/packages.json").get("snapshot"),
        "profile": profile,
        "generation_id": generation_id,
        "generation_digest_sha256": generation_content_digest(stage),
        "installed_at": impl.dt.datetime.now(impl.dt.timezone.utc).isoformat(),
        "packages": packages,
    }


def build_index(manifest: Mapping[str, Any], manifest_bytes: bytes) -> Dict[str, Any]:
    capabilities = []
    for package in manifest.get("packages", []):
        if not isinstance(package, Mapping) or package.get("kind") == "support":
            continue
        capabilities.append({
            "id": package["qualified_id"],
            "name": package["name"],
            "description": package["description"],
            "visibility": "shared",
            "version": package["version"],
            "path": package["path"],
            "package_state": "valid",
            "digest": package["digest"],
            "operators": list(package.get("operators", [])),
            "dependencies": list(package.get("dependencies", [])),
        })
    capabilities.sort(key=lambda item: item["id"].encode("utf-8"))
    return {
        "contract": CONTRACT_ID,
        "provider_id": PROVIDER_ID,
        "generation_id": manifest["generation_id"],
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "capabilities": capabilities,
    }


def write_provider_metadata(impl: Any, profile: str, installed: Iterable[Mapping[str, Any]], generation_id: str, stage: Path) -> Dict[str, Any]:
    meta = Path(stage) / ".aiverse"
    meta.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest(impl, profile, installed, generation_id, Path(stage))
    manifest_path = meta / "installed.json"
    impl._atomic_json_write(manifest_path, manifest)
    index = build_index(manifest, manifest_path.read_bytes())
    impl._atomic_json_write(meta / INDEX_FILENAME, index)
    errors = verify_provider_generation(Path(stage), expected_generation_id=generation_id)
    if errors:
        raise RuntimeError("Provider v1 metadata failed validation:\n" + "\n".join(errors))
    return manifest


def _unique_string_list(value: Any, label: str, errors: List[str]) -> List[str]:
    if not isinstance(value, list) or not all(isinstance(x, str) and x for x in value):
        errors.append(f"{label} must be an array of non-empty strings")
        return []
    if len(set(value)) != len(value):
        errors.append(f"{label} contains duplicates")
    return list(value)


def _validate_digest(value: Any, label: str, errors: List[str]) -> Optional[Dict[str, str]]:
    if not isinstance(value, dict) or set(value) != {"algorithm", "value"}:
        errors.append(f"{label} must contain only algorithm and value")
        return None
    if value.get("algorithm") != DIGEST_ALGORITHM:
        errors.append(f"{label}.algorithm must be {DIGEST_ALGORITHM}")
    raw = value.get("value")
    if not isinstance(raw, str) or not _HEX64_RE.fullmatch(raw):
        errors.append(f"{label}.value must be lowercase sha256")
    return value  # type: ignore[return-value]


def verify_provider_generation(generation_root: Path, expected_generation_id: Optional[str] = None) -> List[str]:
    """Strictly validate producer output and its semantic binding to package bytes."""

    root = Path(generation_root)
    meta = root / ".aiverse"
    manifest_path = meta / "installed.json"
    index_path = meta / INDEX_FILENAME
    errors: List[str] = []
    if not manifest_path.is_file():
        return [f"missing provider manifest: {manifest_path}"]
    if not index_path.is_file():
        return [f"missing provider capability index: {index_path}"]
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes.decode("utf-8"))
    except Exception as exc:
        return [f"invalid provider manifest: {exc}"]
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid provider capability index: {exc}"]
    if not isinstance(manifest, dict) or not isinstance(index, dict):
        return ["provider manifest and index must be JSON objects"]

    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        errors.append(f"provider manifest schema must be {MANIFEST_SCHEMA_VERSION}")
    if manifest.get("provider_contract") != CONTRACT_ID:
        errors.append("provider manifest contract mismatch")
    if manifest.get("provider_id") != PROVIDER_ID:
        errors.append("provider manifest id mismatch")
    generation_id = manifest.get("generation_id")
    if not isinstance(generation_id, str) or not generation_id:
        errors.append("provider manifest generation_id is required")
        generation_id = ""
    if expected_generation_id and generation_id != expected_generation_id:
        errors.append("provider manifest generation_id mismatch")

    if set(index) != _INDEX_FIELDS:
        errors.append("capability index has missing or unknown top-level fields")
    if index.get("contract") != CONTRACT_ID or index.get("provider_id") != PROVIDER_ID:
        errors.append("capability index contract/provider mismatch")
    if index.get("generation_id") != generation_id:
        errors.append("capability index generation does not match manifest")
    expected_hash = hashlib.sha256(manifest_bytes).hexdigest()
    if index.get("manifest_sha256") != expected_hash:
        errors.append("capability index manifest_sha256 does not match exact installed.json bytes")

    packages = manifest.get("packages")
    if not isinstance(packages, list):
        return errors + ["provider manifest packages must be an array"]
    manifest_caps: Dict[str, Mapping[str, Any]] = {}
    for number, package in enumerate(packages):
        if not isinstance(package, dict):
            errors.append(f"manifest package {number} is not an object")
            continue
        package_id = str(package.get("id", f"#{number}"))
        rel = package.get("path")
        try:
            package_dir = validate_relative_package_path(root, rel)
        except Exception as exc:
            errors.append(f"{package_id}: {exc}")
            continue
        digest_data = _validate_digest(package.get("digest"), f"{package_id}.digest", errors)
        if digest_data and package_digest_v1(package_dir) != digest_data.get("value"):
            errors.append(f"{package_id}: portable package digest changed")
        if package.get("kind") == "support":
            continue
        qid = package.get("qualified_id")
        if not isinstance(qid, str) or not qid.startswith(f"{PROVIDER_ID}:"):
            errors.append(f"{package_id}: missing valid qualified_id")
            continue
        segment = qid.split(":", 1)[1]
        if not _SEGMENT_RE.fullmatch(segment):
            errors.append(f"{package_id}: invalid qualified_id segment")
            continue
        if qid in manifest_caps:
            errors.append(f"duplicate manifest capability id: {qid}")
        manifest_caps[qid] = package
        for field in ("name", "description", "version"):
            if not isinstance(package.get(field), str) or not str(package[field]).strip():
                errors.append(f"{package_id}: missing {field}")
        _unique_string_list(package.get("operators"), f"{package_id}.operators", errors)
        _unique_string_list(package.get("dependencies"), f"{package_id}.dependencies", errors)

    records = index.get("capabilities")
    if not isinstance(records, list):
        return errors + ["capability index capabilities must be an array"]
    index_caps: Dict[str, Mapping[str, Any]] = {}
    for number, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"capability index record {number} is not an object")
            continue
        if set(record) != _RECORD_FIELDS:
            errors.append(f"capability index record {number} has missing or unknown fields")
        qid = record.get("id")
        if not isinstance(qid, str) or not qid.startswith(f"{PROVIDER_ID}:"):
            errors.append(f"capability index record {number} has invalid id")
            continue
        if qid in index_caps:
            errors.append(f"duplicate capability index id: {qid}")
        index_caps[qid] = record
        if record.get("visibility") != "shared":
            errors.append(f"{qid}: distributed capability visibility must be shared")
        if record.get("package_state") not in {"valid", "broken"}:
            errors.append(f"{qid}: invalid package_state")
        _validate_digest(record.get("digest"), f"{qid}.digest", errors)
        _unique_string_list(record.get("operators"), f"{qid}.operators", errors)
        _unique_string_list(record.get("dependencies"), f"{qid}.dependencies", errors)

    if set(index_caps) != set(manifest_caps):
        missing = sorted(set(manifest_caps) - set(index_caps))
        injected = sorted(set(index_caps) - set(manifest_caps))
        if missing:
            errors.append("capability index missing manifest packages: " + ", ".join(missing))
        if injected:
            errors.append("capability index contains uninstalled packages: " + ", ".join(injected))

    for qid in sorted(set(index_caps) & set(manifest_caps)):
        record = index_caps[qid]
        package = manifest_caps[qid]
        expected = {
            "id": qid,
            "name": package.get("name"),
            "description": package.get("description"),
            "visibility": "shared",
            "version": package.get("version"),
            "path": package.get("path"),
            "package_state": "valid",
            "digest": package.get("digest"),
            "operators": package.get("operators", []),
            "dependencies": package.get("dependencies", []),
        }
        if record != expected:
            errors.append(f"{qid}: capability index record does not exactly match manifest metadata")
    return errors


def apply_provider_contract_v1(impl: Any) -> None:
    """Install the producer hooks into the compatibility implementation once."""

    if getattr(impl, "_provider_contract_v1_applied", False):
        return
    impl._provider_contract_v1_applied = True

    original_verify_stage = impl.verify_stage
    original_verify_root = impl.verify_root
    original_activate = lifecycle.activate_generation
    original_pin = lifecycle.pin_active_generation
    original_rollback = lifecycle.rollback_active_generation

    # Provider metadata is derived from package bytes and excluded from the older
    # generation content digest. Existing pre-index generations therefore keep
    # exactly the same digest they had before this producer shipped.
    lifecycle.generation_content_digest = generation_content_digest
    impl.generation_content_digest = generation_content_digest

    def manifest_for(profile: str, installed: Iterable[Mapping[str, Any]], generation_id: str, stage: Path) -> Dict[str, Any]:
        return build_manifest(impl, profile, installed, generation_id, Path(stage))

    def write_stage_manifest(profile: str, installed: Iterable[Mapping[str, Any]], generation_id: str, stage: Path) -> None:
        write_provider_metadata(impl, profile, installed, generation_id, Path(stage))

    def verify_stage(stage: Path, expected_generation_id: Optional[str] = None) -> List[str]:
        errors = list(original_verify_stage(stage, expected_generation_id))
        manifest_path = Path(stage) / ".aiverse" / "installed.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            return errors
        if manifest.get("provider_contract") == CONTRACT_ID:
            errors.extend(verify_provider_generation(Path(stage), expected_generation_id))
        return errors

    def finalize_legacy_stage(stage: Path, generation_id: str) -> None:
        manifest_path = Path(stage) / ".aiverse" / "installed.json"
        data = impl._read_json(manifest_path, "legacy install manifest")
        profile = str(data.get("profile", "full"))
        packages = data.get("packages", [])
        if not isinstance(packages, list):
            raise RuntimeError("Legacy install manifest packages must be an array")
        write_provider_metadata(impl, profile, packages, generation_id, Path(stage))

    def verify_root(root: Path) -> List[str]:
        errors = list(original_verify_root(root))
        if errors or not impl._is_lifecycle(root):
            return errors
        try:
            pointer = lifecycle.read_active_pointer(Path(root))
            generation_id = str(pointer["generation_id"])
            generation_root = lifecycle.generation_path(Path(root), generation_id)
            manifest = lifecycle.read_generation_manifest(Path(root), generation_id)
        except RuntimeError as exc:
            return errors + [str(exc)]
        if manifest.get("provider_contract") == CONTRACT_ID:
            errors.extend(verify_provider_generation(generation_root, generation_id))
        return errors

    def activate(root: Path, generation_id: str) -> Dict[str, object]:
        generation_root = lifecycle.generation_path(Path(root), generation_id)
        manifest = lifecycle.read_generation_manifest(Path(root), generation_id)
        if manifest.get("provider_contract") == CONTRACT_ID:
            errors = verify_provider_generation(generation_root, generation_id)
            if errors:
                raise RuntimeError("Provider generation failed validation before activation:\n" + "\n".join(errors))
        return original_activate(Path(root), generation_id)

    def pin(root: Path, digest_fn: Any):
        pinned = original_pin(Path(root), digest_fn)
        if pinned.manifest.get("provider_contract") == CONTRACT_ID:
            errors = verify_provider_generation(pinned.generation_path, pinned.generation_id)
            if errors:
                raise RuntimeError("Pinned provider generation failed validation:\n" + "\n".join(errors))
        return pinned

    def rollback(root: Path, digest_fn: Any):
        pointer = lifecycle.read_active_pointer(Path(root), allow_uninstalled=True)
        history = list(pointer.get("history", []))
        if history:
            chosen = str(history[0])
            manifest = lifecycle.read_generation_manifest(Path(root), chosen)
            if manifest.get("provider_contract") == CONTRACT_ID:
                errors = verify_provider_generation(lifecycle.generation_path(Path(root), chosen), chosen)
                if errors:
                    raise RuntimeError("Rollback provider generation failed validation:\n" + "\n".join(errors))
        return original_rollback(Path(root), digest_fn)

    impl.manifest_for = manifest_for
    impl._write_stage_manifest = write_stage_manifest
    impl.verify_stage = verify_stage
    impl._finalize_legacy_stage = finalize_legacy_stage
    impl.verify_root = verify_root
    impl.activate_generation = activate
    impl.pin_active_generation = pin
    impl.rollback_active_generation = rollback
    lifecycle.activate_generation = activate
    lifecycle.pin_active_generation = pin
    lifecycle.rollback_active_generation = rollback
