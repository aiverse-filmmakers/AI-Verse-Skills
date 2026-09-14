#!/usr/bin/env python3
"""Governed continual-learning / Skill Workshop lifecycle for AI-Verse Skills."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import shutil
import tempfile
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple

try:
    from .admission import scan_package, write_admission_metadata, verify_admission_generation
    from .provider_contract_v1 import write_provider_metadata, verify_provider_generation
except ImportError:
    from admission import scan_package, write_admission_metadata, verify_admission_generation
    from provider_contract_v1 import write_provider_metadata, verify_provider_generation

LEARNING_SCHEMA_VERSION = 1
DEFAULT_CONFIG = {
    "schema_version": LEARNING_SCHEMA_VERSION,
    "mode": "propose",
    "max_pending_proposals": 50,
    "max_proposal_bytes": 1_000_000,
    "max_background_reviews_per_day": 8,
    "stale_after_days": 30,
    "archive_review_after_days": 90,
    "duplicate_similarity_threshold": 0.88,
    "raw_evidence_storage": False,
    "auto_workspace_local": False,
}
FINAL_STATES = {"applied", "rejected", "quarantined"}
AUTO_OWNERS = {"agent_learned", "workspace_local"}
PROTECTED_OWNERS = {"first_party", "curated_upstream", "user_authored", "external"}
ALLOWED_KINDS = {"create", "repair", "update", "consolidate", "archive-review"}


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _parse_time(value: Optional[str]) -> Optional[dt.datetime]:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def learning_dir(root: Path) -> Path:
    return Path(root).expanduser().resolve() / ".aiverse" / "learning"


def _paths(root: Path) -> Dict[str, Path]:
    base = learning_dir(root)
    return {
        "base": base,
        "config": base / "config.json",
        "proposals": base / "proposals",
        "archive": base / "archive",
        "usage": base / "usage.json",
        "skill_state": base / "skill-state.json",
        "budget": base / "budget.json",
        "ledger": base / "audit.ndjson",
    }


def _read_json(path: Path, default: Any) -> Any:
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Invalid learning state {path}: {exc}") from exc


def ensure_learning_state(impl: Any, root: Path) -> Dict[str, Any]:
    p = _paths(root)
    p["proposals"].mkdir(parents=True, exist_ok=True)
    p["archive"].mkdir(parents=True, exist_ok=True)
    config = _read_json(p["config"], None)
    if config is None:
        config = dict(DEFAULT_CONFIG)
        impl._atomic_json_write(p["config"], config)
    if config.get("schema_version") != LEARNING_SCHEMA_VERSION:
        raise RuntimeError("Unsupported Skills learning configuration schema")
    if config.get("mode") not in {"off", "propose", "auto"}:
        raise RuntimeError("Invalid Skills learning mode")
    if "auto_workspace_local" not in config:
        config["auto_workspace_local"] = False
        impl._atomic_json_write(p["config"], config)
    if not isinstance(config.get("auto_workspace_local"), bool):
        raise RuntimeError("auto_workspace_local must be a boolean")
    for key, default in (("usage", {}), ("skill_state", {}), ("budget", {})):
        if not p[key].is_file():
            impl._atomic_json_write(p[key], default)
    return config


def _proposal_path(root: Path, proposal_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9._-]{3,128}", proposal_id or ""):
        raise RuntimeError("Invalid proposal id")
    return _paths(root)["proposals"] / proposal_id


def _load_proposal(root: Path, proposal_id: str) -> Dict[str, Any]:
    path = _proposal_path(root, proposal_id) / "proposal.json"
    data = _read_json(path, None)
    if not isinstance(data, dict):
        raise RuntimeError(f"Unknown proposal: {proposal_id}")
    return data


def _save_proposal(impl: Any, root: Path, proposal: Mapping[str, Any]) -> None:
    pid = str(proposal["proposal_id"])
    path = _proposal_path(root, pid)
    path.mkdir(parents=True, exist_ok=True)
    impl._atomic_json_write(path / "proposal.json", dict(proposal))


def _canonical_event_payload(event: Mapping[str, Any]) -> bytes:
    return json.dumps(dict(event), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _last_ledger_hash(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    last = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            last = json.loads(line).get("event_hash")
        except Exception:
            return None
    return last if isinstance(last, str) else None


def append_audit(root: Path, event_type: str, data: Mapping[str, Any]) -> Dict[str, Any]:
    path = _paths(root)["ledger"]
    path.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "schema_version": LEARNING_SCHEMA_VERSION,
        "event_id": "evt-" + uuid.uuid4().hex,
        "event_type": event_type,
        "occurred_at": _utc_now(),
        "prev_hash": _last_ledger_hash(path),
        "data": dict(data),
    }
    event_hash = hashlib.sha256(_canonical_event_payload(event)).hexdigest()
    event["event_hash"] = event_hash
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return event


def verify_audit_ledger(root: Path) -> List[str]:
    path = _paths(root)["ledger"]
    if not path.is_file():
        return []
    errors: List[str] = []
    previous = None
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except Exception:
            errors.append(f"audit line {index}: invalid JSON")
            continue
        claimed = event.pop("event_hash", None)
        if event.get("prev_hash") != previous:
            errors.append(f"audit line {index}: broken previous-hash chain")
        actual = hashlib.sha256(_canonical_event_payload(event)).hexdigest()
        if claimed != actual:
            errors.append(f"audit line {index}: event hash mismatch")
        previous = claimed
    return errors


def learning_status(impl: Any, root: Path) -> Dict[str, Any]:
    config = ensure_learning_state(impl, root)
    p = _paths(root)
    proposals = []
    for d in sorted(p["proposals"].iterdir()) if p["proposals"].exists() else []:
        data = _read_json(d / "proposal.json", None)
        if isinstance(data, dict):
            proposals.append(data)
    counts: Dict[str, int] = {}
    for item in proposals:
        state = str(item.get("state", "unknown"))
        counts[state] = counts.get(state, 0) + 1
    skill_state = _read_json(p["skill_state"], {})
    return {
        "schema_version": LEARNING_SCHEMA_VERSION,
        "mode": config["mode"],
        "default_mode": "propose",
        "proposal_counts": counts,
        "pending_total": sum(v for k, v in counts.items() if k not in FINAL_STATES),
        "skill_states": skill_state,
        "audit_ledger": {
            "path": str(p["ledger"]),
            "valid": not verify_audit_ledger(root),
        },
        "limits": {
            "max_pending_proposals": config["max_pending_proposals"],
            "max_proposal_bytes": config["max_proposal_bytes"],
            "max_background_reviews_per_day": config["max_background_reviews_per_day"],
        },
    }


def set_learning_mode(impl: Any, root: Path, mode: str) -> Dict[str, Any]:
    if mode not in {"off", "propose", "auto"}:
        raise RuntimeError("Learning mode must be off, propose, or auto")
    with impl.lifecycle_lock(Path(root).resolve()):
        config = ensure_learning_state(impl, root)
        previous = config["mode"]
        config["mode"] = mode
        impl._atomic_json_write(_paths(root)["config"], config)
        append_audit(root, "learning.mode.changed", {"from": previous, "to": mode})
    return config


def _pending_count(root: Path) -> int:
    count = 0
    proposal_root = _paths(root)["proposals"]
    if not proposal_root.exists():
        return 0
    for d in proposal_root.iterdir():
        data = _read_json(d / "proposal.json", None)
        if isinstance(data, dict) and data.get("state") not in FINAL_STATES:
            count += 1
    return count


def _consume_background_budget(impl: Any, root: Path, config: Mapping[str, Any]) -> None:
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    path = _paths(root)["budget"]
    budget = _read_json(path, {})
    count = int(budget.get(today, 0))
    limit = int(config.get("max_background_reviews_per_day", 0))
    if count >= limit:
        raise RuntimeError("Background learning review budget exhausted for today")
    budget = {today: count + 1}
    impl._atomic_json_write(path, budget)


def _validate_envelope(envelope: Mapping[str, Any]) -> Dict[str, Any]:
    data = dict(envelope)
    kind = str(data.get("kind", "create"))
    if kind not in ALLOWED_KINDS:
        raise RuntimeError(f"Unsupported learning candidate kind: {kind}")
    suggested_owner = data.get("suggested_owner", "skills")
    if suggested_owner != "skills":
        raise RuntimeError(f"Learning candidate belongs to {suggested_owner}, not Skills")
    refs = data.get("evidence_refs", [])
    if not isinstance(refs, list) or not all(isinstance(x, str) and 0 < len(x) <= 500 for x in refs):
        raise RuntimeError("evidence_refs must be bounded string references")
    forbidden = {"raw_transcript", "credentials", "secrets", "private_key", "raw_tool_output"}
    if forbidden.intersection(data):
        raise RuntimeError("Raw private/secret evidence is not accepted into Skills proposals")
    risk = str(data.get("risk", "medium"))
    if risk not in {"low", "medium", "high"}:
        raise RuntimeError("risk must be low, medium, or high")
    confidence = float(data.get("confidence", 0.0))
    if confidence < 0.0 or confidence > 1.0:
        raise RuntimeError("confidence must be within 0..1")
    source_ownership = str(data.get("source_ownership") or "agent_learned")
    if source_ownership not in AUTO_OWNERS | PROTECTED_OWNERS:
        raise RuntimeError(f"Unsupported source ownership: {source_ownership}")
    scope = data.get("scope", {})
    if not isinstance(scope, Mapping):
        raise RuntimeError("scope must be an object")
    scope = dict(scope)
    if source_ownership == "workspace_local":
        workspace_id = scope.get("workspace_id")
        if not isinstance(workspace_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,127}", workspace_id):
            raise RuntimeError("workspace_local candidates require scope.workspace_id")
    for flag in ("requires_connection", "requires_credential"):
        if flag in data and not isinstance(data.get(flag), bool):
            raise RuntimeError(f"{flag} must be boolean")
    data["kind"] = kind
    data["risk"] = risk
    data["confidence"] = confidence
    data["evidence_refs"] = refs
    data["requested_capabilities"] = list(data.get("requested_capabilities", []))
    data["requested_dependencies"] = list(data.get("requested_dependencies", []))
    data["source_ownership"] = source_ownership
    data["scope"] = scope
    data["requires_connection"] = bool(data.get("requires_connection", False))
    data["requires_credential"] = bool(data.get("requires_credential", False))
    return data


def _copy_candidate(src: Path, dst: Path, max_bytes: int) -> Tuple[int, str]:
    src = Path(src).expanduser().resolve(strict=True)
    if not (src / "SKILL.md").is_file():
        raise RuntimeError("Candidate package must contain SKILL.md")
    total = 0
    for path in src.rglob("*"):
        if path.is_symlink():
            raise RuntimeError("Learned candidate packages may not contain symlinks")
        if path.is_file():
            total += path.stat().st_size
            if total > max_bytes:
                raise RuntimeError("Candidate package exceeds configured proposal size limit")
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    digest = hashlib.sha256()
    for path in sorted(p for p in dst.rglob("*") if p.is_file()):
        rel = path.relative_to(dst).as_posix()
        digest.update(rel.encode("utf-8") + b"\0" + path.read_bytes() + b"\0")
    return total, digest.hexdigest()


def _find_package(manifest: Mapping[str, Any], package_id: str) -> Optional[Dict[str, Any]]:
    for package in manifest.get("packages", []):
        if isinstance(package, dict) and package.get("id") == package_id:
            return dict(package)
    return None


def _ownership_for(impl: Any, pin: Any, package_id: str) -> str:
    report = json.loads((pin.generation_path / ".aiverse" / "admission.json").read_text(encoding="utf-8"))
    for item in report.get("packages", []):
        if item.get("id") == package_id:
            return str(item.get("ownership", "external"))
    return "external"


def submit_candidate(
    impl: Any,
    root: Path,
    envelope: Mapping[str, Any],
    candidate_dir: Optional[Path] = None,
    *,
    trigger: str = "brain",
    explicit: bool = False,
) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        config = ensure_learning_state(impl, root)
        if config["mode"] == "off" and not explicit:
            raise RuntimeError("Automatic Skills learning is off; explicit /learn remains available")
        if _pending_count(root) >= int(config["max_pending_proposals"]):
            raise RuntimeError("Maximum pending learning proposals reached")
        if not explicit and trigger in {"background", "curator", "automation", "post-run", "refine"}:
            _consume_background_budget(impl, root, config)

        env = _validate_envelope(envelope)
        pin = impl.pin_active_generation(root, impl.digest)
        proposal_id = str(env.get("candidate_id") or ("learn-" + uuid.uuid4().hex))
        proposal_dir = _proposal_path(root, proposal_id)
        if proposal_dir.exists():
            raise RuntimeError(f"Proposal already exists: {proposal_id}")

        target_skill_id = env.get("target_skill_id")
        target_package = None
        target_ownership = None
        if target_skill_id:
            target_package = _find_package(pin.manifest, str(target_skill_id))
            if not target_package:
                raise RuntimeError(f"Target Skill is not active: {target_skill_id}")
            target_ownership = _ownership_for(impl, pin, str(target_skill_id))

        skill_id = str(env.get("skill_id") or target_skill_id or "")
        if env["kind"] == "create":
            if not skill_id:
                raise RuntimeError("Create candidates require skill_id")
            if _find_package(pin.manifest, skill_id):
                raise RuntimeError(f"Skill already exists: {skill_id}")

        proposal = {
            "schema_version": LEARNING_SCHEMA_VERSION,
            "proposal_id": proposal_id,
            "state": "candidate",
            "kind": env["kind"],
            "skill_id": skill_id or None,
            "target_skill_id": target_skill_id,
            "scope": env["scope"],
            "summary": str(env.get("summary", ""))[:2000],
            "evidence_refs": env["evidence_refs"],
            "success_signal": env.get("success_signal", []),
            "failure_signal": env.get("failure_signal", []),
            "risk": env["risk"],
            "confidence": env["confidence"],
            "requested_capabilities": env["requested_capabilities"],
            "requested_dependencies": env["requested_dependencies"],
            "requires_connection": env["requires_connection"],
            "requires_credential": env["requires_credential"],
            "source_ownership": env["source_ownership"],
            "target_ownership": target_ownership,
            "protected_target": bool(target_ownership in PROTECTED_OWNERS) if target_ownership else False,
            "base_generation_id": pin.generation_id,
            "base_generation_digest": pin.generation_digest,
            "target_generation_id": pin.generation_id if target_package else None,
            "target_package_digest": target_package.get("digest_sha256") if target_package else None,
            "source_skill_ids": list(env.get("source_skill_ids", [])),
            "trigger": trigger,
            "explicit": explicit,
            "created_at": _utc_now(),
            "updated_at": _utc_now(),
            "history": [{"state": "candidate", "at": _utc_now(), "by": trigger}],
        }
        proposal_dir.mkdir(parents=True, exist_ok=False)
        if candidate_dir is not None:
            size, candidate_digest = _copy_candidate(
                Path(candidate_dir), proposal_dir / "candidate", int(config["max_proposal_bytes"])
            )
            proposal["candidate_bytes"] = size
            proposal["candidate_digest_sha256"] = candidate_digest
            proposal["state"] = "proposal"
            proposal["history"].append({"state": "proposal", "at": _utc_now(), "by": "candidate-attached"})
        elif env["kind"] == "archive-review":
            # Archive review mutates lifecycle state rather than Skill package bytes,
            # so there is no candidate directory to attach before evaluation.
            proposal["state"] = "proposal"
            proposal["history"].append({"state": "proposal", "at": _utc_now(), "by": "archive-review"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.candidate.submitted", {
            "proposal_id": proposal_id,
            "kind": proposal["kind"],
            "target_skill_id": target_skill_id,
            "evidence_refs": proposal["evidence_refs"],
            "trigger": trigger,
        })
        return proposal


def attach_candidate(impl: Any, root: Path, proposal_id: str, candidate_dir: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        config = ensure_learning_state(impl, root)
        proposal = _load_proposal(root, proposal_id)
        if proposal.get("state") != "candidate":
            raise RuntimeError("Candidate content can only be attached to a candidate-state proposal")
        size, candidate_digest = _copy_candidate(
            Path(candidate_dir), _proposal_path(root, proposal_id) / "candidate", int(config["max_proposal_bytes"])
        )
        proposal["candidate_bytes"] = size
        proposal["candidate_digest_sha256"] = candidate_digest
        proposal["state"] = "proposal"
        proposal["updated_at"] = _utc_now()
        proposal["history"].append({"state": "proposal", "at": _utc_now(), "by": "candidate-attached"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.candidate.attached", {"proposal_id": proposal_id})
        return proposal


def _tokenize(text: str) -> set:
    return {x for x in re.findall(r"[a-z0-9_]{3,}", text.casefold())}


def _similarity(a: str, b: str) -> float:
    aa, bb = _tokenize(a), _tokenize(b)
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def _dedup_report(impl: Any, root: Path, proposal: Mapping[str, Any], candidate: Path) -> Dict[str, Any]:
    pin = impl.pin_active_generation(Path(root), impl.digest)
    candidate_text = (candidate / "SKILL.md").read_text(encoding="utf-8", errors="replace")
    nearest = []
    target = proposal.get("target_skill_id")
    for package in pin.manifest.get("packages", []):
        if package.get("kind") == "support" or package.get("id") == target:
            continue
        skill_md = pin.generation_path / str(package["path"]) / "SKILL.md"
        if not skill_md.is_file():
            continue
        score = _similarity(candidate_text, skill_md.read_text(encoding="utf-8", errors="replace"))
        if score >= 0.55:
            nearest.append({"id": package.get("id"), "similarity": round(score, 4)})
    nearest.sort(key=lambda x: x["similarity"], reverse=True)
    threshold = float(ensure_learning_state(impl, root)["duplicate_similarity_threshold"])
    return {
        "nearest": nearest[:10],
        "duplicate": bool(nearest and nearest[0]["similarity"] >= threshold),
        "threshold": threshold,
    }


def evaluate_proposal(impl: Any, root: Path, proposal_id: str, *, auto_apply: bool = False) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        config = ensure_learning_state(impl, root)
        proposal = _load_proposal(root, proposal_id)
        if proposal.get("state") not in {"proposal", "evaluating", "pending_approval", "auto_eligible"}:
            raise RuntimeError(f"Proposal cannot be evaluated from state {proposal.get('state')}")
        candidate = _proposal_path(root, proposal_id) / "candidate"
        if proposal.get("kind") != "archive-review" and not (candidate / "SKILL.md").is_file():
            raise RuntimeError("Proposal has no candidate package")

        proposal["state"] = "evaluating"
        proposal["history"].append({"state": "evaluating", "at": _utc_now(), "by": "skills-evaluator"})
        security = {"status": "pass", "findings": []}
        dedup = {"nearest": [], "duplicate": False, "threshold": config["duplicate_similarity_threshold"]}
        if proposal.get("kind") != "archive-review":
            security = scan_package(candidate)
            dedup = _dedup_report(impl, root, proposal, candidate)
        permission_expansion = bool(proposal.get("requested_capabilities") or proposal.get("requested_dependencies"))
        connection_expansion = bool(proposal.get("requires_connection") or proposal.get("requires_credential"))
        pin = impl.pin_active_generation(root, impl.digest)
        base_generation_changed = pin.generation_id != proposal.get("base_generation_id")
        target_changed = False
        if proposal.get("target_skill_id"):
            current = _find_package(pin.manifest, str(proposal["target_skill_id"]))
            target_changed = (
                pin.generation_id != proposal.get("target_generation_id")
                or not current
                or current.get("digest_sha256") != proposal.get("target_package_digest")
            )

        evaluation = {
            "schema_valid": proposal.get("kind") == "archive-review" or (candidate / "SKILL.md").is_file(),
            "security": security,
            "dedup": dedup,
            "permission_expansion": permission_expansion,
            "connection_expansion": connection_expansion,
            "target_changed": target_changed,
            "base_generation_changed": base_generation_changed,
            "provenance_complete": bool(proposal.get("evidence_refs") or proposal.get("explicit")),
            "scope_valid": isinstance(proposal.get("scope"), dict),
            "evaluated_generation_id": pin.generation_id,
            "evaluated_generation_digest": pin.generation_digest,
            "evaluated_at": _utc_now(),
        }
        proposal["evaluation"] = evaluation

        if security["status"] == "deny" or target_changed:
            proposal["state"] = "quarantined"
            reason = "security-deny" if security["status"] == "deny" else "target-changed"
            proposal["quarantine_reason"] = reason
        else:
            create_owner = proposal.get("source_ownership")
            create_owner_auto = (
                create_owner == "agent_learned"
                or (create_owner == "workspace_local" and config.get("auto_workspace_local") is True)
            )
            ownership_eligible = (
                create_owner_auto
                if proposal.get("kind") == "create"
                else proposal.get("target_ownership") in AUTO_OWNERS
            )
            create_confidence_ok = (
                proposal.get("kind") != "create"
                or float(proposal.get("confidence", 0.0)) >= 0.9
            )
            auto_eligible = (
                config["mode"] == "auto"
                and proposal.get("kind") in {"create", "repair", "update", "archive-review"}
                and ownership_eligible
                and not proposal.get("protected_target")
                and proposal.get("risk") == "low"
                and create_confidence_ok
                and not permission_expansion
                and not connection_expansion
                and not dedup.get("duplicate")
                and security["status"] == "pass"
                and evaluation["provenance_complete"]
                and evaluation["scope_valid"]
                and not base_generation_changed
            )
            proposal["state"] = "auto_eligible" if auto_eligible else "pending_approval"

        proposal["updated_at"] = _utc_now()
        proposal["history"].append({"state": proposal["state"], "at": _utc_now(), "by": "skills-evaluator"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.proposal.evaluated", {
            "proposal_id": proposal_id,
            "state": proposal["state"],
            "security": security["status"],
            "permission_expansion": permission_expansion,
            "connection_expansion": connection_expansion,
            "target_changed": target_changed,
            "base_generation_changed": base_generation_changed,
        })

    if auto_apply and proposal.get("state") == "auto_eligible":
        return apply_proposal(impl, root, proposal_id, approved_by=None)
    return proposal


def reject_proposal(impl: Any, root: Path, proposal_id: str, reason: str = "") -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        proposal = _load_proposal(root, proposal_id)
        if proposal.get("state") in FINAL_STATES:
            raise RuntimeError("Proposal is already final")
        proposal["state"] = "rejected"
        proposal["rejection_reason"] = reason[:1000]
        proposal["updated_at"] = _utc_now()
        proposal["history"].append({"state": "rejected", "at": _utc_now(), "by": "operator"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.proposal.rejected", {"proposal_id": proposal_id, "reason": reason[:1000]})
        return proposal


def quarantine_proposal(impl: Any, root: Path, proposal_id: str, reason: str = "") -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        proposal = _load_proposal(root, proposal_id)
        if proposal.get("state") == "applied":
            raise RuntimeError("Applied proposals cannot be quarantined retroactively")
        proposal["state"] = "quarantined"
        proposal["quarantine_reason"] = reason[:1000]
        proposal["updated_at"] = _utc_now()
        proposal["history"].append({"state": "quarantined", "at": _utc_now(), "by": "operator"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.proposal.quarantined", {"proposal_id": proposal_id, "reason": reason[:1000]})
        return proposal


def _raw_packages(manifest: Mapping[str, Any]) -> List[Dict[str, Any]]:
    keep = {
        "kind", "id", "path", "source_repo", "source_commit", "operators",
        "dependencies", "digest_sha256", "ownership",
    }
    return [{k: v for k, v in dict(p).items() if k in keep} for p in manifest.get("packages", []) if isinstance(p, dict)]


def _stage_from_active(impl: Any, root: Path, pin: Any) -> Path:
    stage_parent = root / ".aiverse"
    stage_parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".learning-stage-", dir=str(stage_parent)))
    shutil.copytree(pin.generation_path, stage, dirs_exist_ok=True, symlinks=True)
    shutil.rmtree(stage / ".aiverse", ignore_errors=True)
    return stage


def _finalize_generation(impl: Any, root: Path, pin: Any, stage: Path, packages: List[Dict[str, Any]]) -> str:
    generation_id = impl.new_generation_id()
    profile = str(pin.manifest.get("profile", "full"))
    write_provider_metadata(impl, profile, packages, generation_id, stage)
    write_admission_metadata(impl, stage)
    errors = verify_provider_generation(stage, generation_id)
    errors.extend(verify_admission_generation(impl, stage, generation_id))
    if errors:
        raise RuntimeError("Learned generation failed verification:\n" + "\n".join(errors))
    impl.commit_stage(root, stage, generation_id)
    impl.activate_generation(root, generation_id)
    return generation_id


def _record_skill_state(impl: Any, root: Path, skill_id: str, status: str, **extra: Any) -> None:
    path = _paths(root)["skill_state"]
    state = _read_json(path, {})
    item = dict(state.get(skill_id, {}))
    item.update({
        "status": status,
        "updated_at": _utc_now(),
        **extra,
    })
    state[skill_id] = item
    impl._atomic_json_write(path, state)


def apply_proposal(
    impl: Any,
    root: Path,
    proposal_id: str,
    *,
    approved_by: Optional[str],
) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        ensure_learning_state(impl, root)
        proposal = _load_proposal(root, proposal_id)
        state = proposal.get("state")
        if state == "pending_approval" and not approved_by:
            raise RuntimeError("Explicit approval is required for this proposal")
        if state not in {"pending_approval", "auto_eligible"}:
            raise RuntimeError(f"Proposal cannot be applied from state {state}")
        if proposal.get("kind") == "archive-review":
            return _archive_skill_locked(
                impl, root, str(proposal.get("target_skill_id")), proposal_id=proposal_id,
                approved_by=approved_by or "policy:auto"
            )

        target_ownership = proposal.get("target_ownership")
        if proposal.get("kind") in {"repair", "update"} and target_ownership in PROTECTED_OWNERS:
            raise RuntimeError(
                "Self-learning never overwrites protected/upstream/user Skills in public beta; "
                "create a derived agent_learned Skill instead"
            )

        pin = impl.pin_active_generation(root, impl.digest)
        evaluation = proposal.get("evaluation") if isinstance(proposal.get("evaluation"), dict) else {}
        if state == "auto_eligible" and (
            pin.generation_id != evaluation.get("evaluated_generation_id")
            or pin.generation_digest != evaluation.get("evaluated_generation_digest")
        ):
            raise RuntimeError("Active generation changed after evaluation; re-evaluate before auto promotion")
        if proposal.get("target_skill_id"):
            current = _find_package(pin.manifest, str(proposal["target_skill_id"]))
            if (
                pin.generation_id != proposal.get("target_generation_id")
                or not current
                or current.get("digest_sha256") != proposal.get("target_package_digest")
            ):
                raise RuntimeError("Proposal target changed after evaluation; re-evaluate from current generation")

        skill_id = str(proposal.get("skill_id") or proposal.get("target_skill_id") or "")
        if not skill_id:
            raise RuntimeError("Proposal has no Skill id")
        candidate = _proposal_path(root, proposal_id) / "candidate"
        security = scan_package(candidate)
        if security["status"] == "deny":
            raise RuntimeError("Candidate failed security scan at apply time")

        stage = _stage_from_active(impl, root, pin)
        try:
            packages = _raw_packages(pin.manifest)
            if proposal.get("kind") == "create":
                if _find_package(pin.manifest, skill_id):
                    raise RuntimeError(f"Skill already exists: {skill_id}")
                target_rel = f"learned/{skill_id}"
                shutil.copytree(candidate, stage / target_rel)
                packages.append({
                    "kind": "learned",
                    "id": skill_id,
                    "path": target_rel,
                    "source_repo": "aiverse-local/learning",
                    "source_commit": None,
                    "operators": [],
                    "dependencies": [],
                    "ownership": (
                        proposal.get("source_ownership")
                        if proposal.get("source_ownership") in AUTO_OWNERS
                        else "agent_learned"
                    ),
                    "digest_sha256": impl.digest(stage / target_rel),
                })
            else:
                target_id = str(proposal["target_skill_id"])
                found = False
                for item in packages:
                    if item.get("id") == target_id:
                        target_rel = str(item["path"])
                        shutil.rmtree(stage / target_rel)
                        shutil.copytree(candidate, stage / target_rel)
                        item["kind"] = "learned"
                        item["source_repo"] = "aiverse-local/learning"
                        item["source_commit"] = None
                        item["ownership"] = "agent_learned"
                        item["digest_sha256"] = impl.digest(stage / target_rel)
                        found = True
                        break
                if not found:
                    raise RuntimeError("Target Skill vanished before promotion")

            append_audit(root, "learning.promotion.intent", {
                "proposal_id": proposal_id,
                "backup_generation": pin.generation_id,
                "approved_by": approved_by or "policy:auto",
            })
            generation_id = _finalize_generation(impl, root, pin, stage, packages)
            stage = None
        finally:
            if stage is not None and Path(stage).exists():
                shutil.rmtree(stage, ignore_errors=True)

        proposal["state"] = "applied"
        proposal["applied_generation_id"] = generation_id
        proposal["backup_generation_id"] = pin.generation_id
        proposal["approved_by"] = approved_by or "policy:auto"
        proposal["applied_at"] = _utc_now()
        proposal["updated_at"] = _utc_now()
        proposal["history"].append({"state": "applied", "at": _utc_now(), "by": proposal["approved_by"]})
        _save_proposal(impl, root, proposal)
        learned_ownership = (
            proposal.get("source_ownership")
            if proposal.get("source_ownership") in AUTO_OWNERS
            else "agent_learned"
        )
        _record_skill_state(
            impl, root, skill_id, "active", ownership=learned_ownership,
            protected=False, generation_id=generation_id, source_proposal_id=proposal_id,
        )
        append_audit(root, "learning.promotion.applied", {
            "proposal_id": proposal_id,
            "generation_id": generation_id,
            "backup_generation": pin.generation_id,
        })
        return proposal


def rollback_learning_change(impl: Any, root: Path, proposal_id: str) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        proposal = _load_proposal(root, proposal_id)
        if proposal.get("state") != "applied":
            raise RuntimeError("Only applied proposals can be rolled back")
        pointer = impl.read_active_pointer(root)
        if pointer.get("generation_id") != proposal.get("applied_generation_id"):
            raise RuntimeError("Refusing rollback because a newer generation is active")
        pin = impl.rollback_active_generation(root, impl.digest)
        proposal["rollback_generation_id"] = pin.generation_id
        proposal["rolled_back_at"] = _utc_now()
        proposal["history"].append({"state": "rolled_back", "at": _utc_now(), "by": "operator"})
        _save_proposal(impl, root, proposal)
        append_audit(root, "learning.promotion.rolled_back", {
            "proposal_id": proposal_id,
            "restored_generation": pin.generation_id,
        })
        return proposal


def record_usage(impl: Any, root: Path, skill_id: str, *, success: Optional[bool], selected: bool = True) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        ensure_learning_state(impl, root)
        path = _paths(root)["usage"]
        usage = _read_json(path, {})
        item = dict(usage.get(skill_id, {}))
        if selected:
            item["selected_count"] = int(item.get("selected_count", 0)) + 1
            item["last_selected"] = _utc_now()
        if success is True:
            item["success_count"] = int(item.get("success_count", 0)) + 1
            item["last_success"] = _utc_now()
        elif success is False:
            item["failure_count"] = int(item.get("failure_count", 0)) + 1
            item["last_failure"] = _utc_now()
        item["updated_at"] = _utc_now()
        usage[skill_id] = item
        impl._atomic_json_write(path, usage)
        append_audit(root, "learning.usage.recorded", {
            "skill_id": skill_id, "selected": selected, "success": success,
        })
        return item


def _archive_record_path(root: Path, skill_id: str) -> Path:
    return _paths(root)["archive"] / skill_id / "archive.json"


def _archive_skill_locked(
    impl: Any,
    root: Path,
    skill_id: str,
    *,
    proposal_id: Optional[str],
    approved_by: str,
) -> Dict[str, Any]:
    pin = impl.pin_active_generation(root, impl.digest)
    package = _find_package(pin.manifest, skill_id)
    if not package:
        raise RuntimeError(f"Skill is not active: {skill_id}")
    ownership = _ownership_for(impl, pin, skill_id)
    if ownership not in AUTO_OWNERS or package.get("kind") != "learned":
        raise RuntimeError("Only learned/workspace-local Skills can enter autonomous archive lifecycle")
    stage = _stage_from_active(impl, root, pin)
    try:
        packages = [x for x in _raw_packages(pin.manifest) if x.get("id") != skill_id]
        archived_path = stage / str(package["path"])
        if archived_path.exists():
            shutil.rmtree(archived_path)
        generation_id = _finalize_generation(impl, root, pin, stage, packages)
        stage = None
    finally:
        if stage is not None and Path(stage).exists():
            shutil.rmtree(stage, ignore_errors=True)
    archive = {
        "schema_version": LEARNING_SCHEMA_VERSION,
        "skill_id": skill_id,
        "source_generation_id": pin.generation_id,
        "archived_generation_id": generation_id,
        "package": {k: v for k, v in package.items() if k in {
            "kind", "id", "path", "source_repo", "source_commit", "operators",
            "dependencies", "digest_sha256", "ownership",
        }},
        "proposal_id": proposal_id,
        "approved_by": approved_by,
        "archived_at": _utc_now(),
    }
    path = _archive_record_path(root, skill_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    impl._atomic_json_write(path, archive)
    _record_skill_state(impl, root, skill_id, "archived", ownership=ownership, protected=False)
    append_audit(root, "learning.skill.archived", archive)
    if proposal_id:
        proposal = _load_proposal(root, proposal_id)
        proposal["state"] = "applied"
        proposal["applied_generation_id"] = generation_id
        proposal["backup_generation_id"] = pin.generation_id
        proposal["approved_by"] = approved_by
        proposal["applied_at"] = _utc_now()
        proposal["history"].append({"state": "applied", "at": _utc_now(), "by": approved_by})
        _save_proposal(impl, root, proposal)
        return proposal
    return archive


def archive_skill(impl: Any, root: Path, skill_id: str, *, approved_by: str) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        ensure_learning_state(impl, root)
        return _archive_skill_locked(impl, root, skill_id, proposal_id=None, approved_by=approved_by)


def restore_archived(impl: Any, root: Path, skill_id: str) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        ensure_learning_state(impl, root)
        archive = _read_json(_archive_record_path(root, skill_id), None)
        if not isinstance(archive, dict):
            raise RuntimeError(f"No archived Skill record: {skill_id}")
        pin = impl.pin_active_generation(root, impl.digest)
        if _find_package(pin.manifest, skill_id):
            raise RuntimeError("Skill is already active")
        source_generation = str(archive["source_generation_id"])
        source_manifest = impl.read_generation_manifest(root, source_generation)
        package = _find_package(source_manifest, skill_id)
        if not package:
            raise RuntimeError("Archived source generation no longer contains the Skill")
        source_path = impl.generation_path(root, source_generation) / str(package["path"])
        stage = _stage_from_active(impl, root, pin)
        try:
            target_rel = f"learned/{skill_id}"
            shutil.copytree(source_path, stage / target_rel)
            packages = _raw_packages(pin.manifest)
            raw = {k: v for k, v in package.items() if k in {
                "kind", "id", "path", "source_repo", "source_commit", "operators",
                "dependencies", "digest_sha256", "ownership",
            }}
            raw["path"] = target_rel
            raw["kind"] = "learned"
            raw["ownership"] = "agent_learned"
            raw["digest_sha256"] = impl.digest(stage / target_rel)
            packages.append(raw)
            generation_id = _finalize_generation(impl, root, pin, stage, packages)
            stage = None
        finally:
            if stage is not None and Path(stage).exists():
                shutil.rmtree(stage, ignore_errors=True)
        _record_skill_state(
            impl, root, skill_id, "active", ownership="agent_learned",
            protected=False, generation_id=generation_id, restored_from=source_generation,
        )
        append_audit(root, "learning.skill.restored", {
            "skill_id": skill_id,
            "generation_id": generation_id,
            "source_generation_id": source_generation,
        })
        return {"skill_id": skill_id, "generation_id": generation_id, "source_generation_id": source_generation}


def _proposal_exists(root: Path, kind: str, target_skill_id: Optional[str], source_skill_ids: Optional[List[str]] = None) -> bool:
    p = _paths(root)["proposals"]
    if not p.exists():
        return False
    wanted_sources = sorted(source_skill_ids or [])
    for d in p.iterdir():
        item = _read_json(d / "proposal.json", None)
        if not isinstance(item, dict) or item.get("state") in FINAL_STATES:
            continue
        if item.get("kind") == kind and item.get("target_skill_id") == target_skill_id:
            if kind != "consolidate" or sorted(item.get("source_skill_ids", [])) == wanted_sources:
                return True
    return False


def curator_run(impl: Any, root: Path) -> Dict[str, Any]:
    root = Path(root).expanduser().resolve()
    with impl.lifecycle_lock(root):
        config = ensure_learning_state(impl, root)
        if config["mode"] == "off":
            return {"mode": "off", "stale": [], "archive_proposals": [], "duplicate_proposals": []}
        pin = impl.pin_active_generation(root, impl.digest)
        usage = _read_json(_paths(root)["usage"], {})
        skill_state = _read_json(_paths(root)["skill_state"], {})
        now = dt.datetime.now(dt.timezone.utc)
        stale_ids: List[str] = []
        archive_candidates: List[str] = []
        learned: List[Dict[str, Any]] = []

        for package in pin.manifest.get("packages", []):
            if package.get("kind") != "learned":
                continue
            skill_id = str(package["id"])
            learned.append(dict(package))
            metrics = usage.get(skill_id, {})
            state_item = skill_state.get(skill_id, {})
            basis = _parse_time(metrics.get("last_success") or metrics.get("last_selected") or state_item.get("updated_at"))
            if basis is None:
                basis = now
            age_days = (now - basis).total_seconds() / 86400.0
            if age_days >= float(config["stale_after_days"]):
                stale_ids.append(skill_id)
                state_item = dict(state_item)
                state_item.update({"status": "stale", "updated_at": _utc_now(), "ownership": "agent_learned", "protected": False})
                skill_state[skill_id] = state_item
            if age_days >= float(config["archive_review_after_days"]):
                archive_candidates.append(skill_id)

        impl._atomic_json_write(_paths(root)["skill_state"], skill_state)

        duplicate_pairs: List[Tuple[str, str, float]] = []
        for i, left in enumerate(learned):
            left_text = (pin.generation_path / str(left["path"]) / "SKILL.md").read_text(encoding="utf-8", errors="replace")
            for right in learned[i + 1:]:
                right_text = (pin.generation_path / str(right["path"]) / "SKILL.md").read_text(encoding="utf-8", errors="replace")
                score = _similarity(left_text, right_text)
                if score >= float(config["duplicate_similarity_threshold"]):
                    duplicate_pairs.append((str(left["id"]), str(right["id"]), score))

    archive_proposals = []
    for skill_id in archive_candidates:
        if _proposal_exists(root, "archive-review", skill_id):
            continue
        env = {
            "kind": "archive-review",
            "target_skill_id": skill_id,
            "summary": "Curator archive review for stale learned Skill",
            "evidence_refs": [f"skills-usage:{skill_id}"],
            "risk": "low",
            "confidence": 1.0,
        }
        archive_proposals.append(
            submit_candidate(impl, root, env, None, trigger="curator", explicit=False)["proposal_id"]
        )

    duplicate_proposals = []
    for left, right, score in duplicate_pairs:
        sources = sorted([left, right])
        if _proposal_exists(root, "consolidate", None, sources):
            continue
        env = {
            "kind": "consolidate",
            "skill_id": f"consolidated-{left}-{right}"[:96],
            "source_skill_ids": sources,
            "summary": f"Curator detected overlapping learned Skills ({score:.2f})",
            "evidence_refs": [f"skills-duplicate:{left}:{right}:{score:.4f}"],
            "risk": "medium",
            "confidence": min(1.0, score),
        }
        duplicate_proposals.append(
            submit_candidate(impl, root, env, None, trigger="curator", explicit=False)["proposal_id"]
        )

    append_audit(root, "learning.curator.completed", {
        "stale": stale_ids,
        "archive_proposals": archive_proposals,
        "duplicate_proposals": duplicate_proposals,
    })
    return {
        "mode": config["mode"],
        "stale": stale_ids,
        "archive_proposals": archive_proposals,
        "duplicate_proposals": duplicate_proposals,
    }


def list_proposals(root: Path) -> List[Dict[str, Any]]:
    p = _paths(root)["proposals"]
    out = []
    if not p.exists():
        return out
    for d in sorted(p.iterdir()):
        item = _read_json(d / "proposal.json", None)
        if isinstance(item, dict):
            out.append(item)
    return out
