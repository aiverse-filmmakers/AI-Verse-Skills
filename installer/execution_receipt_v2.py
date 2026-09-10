#!/usr/bin/env python3
"""Strict semantic validation for AI-Verse execution receipt v2.

Receipt v2 is a transport/evidence contract, not an authority grant. In
particular, ``trace_id`` is correlation metadata only and may never stand in for
a stable execution receipt or criterion evidence.
"""
from __future__ import annotations

import copy
import re
from typing import Any, Dict, Mapping, Optional

CONTRACT_ID = "aiverse-execution-receipt-v2"
PROVIDER_ID = "aiverse-skills"
PACKAGE_DIGEST_ALGORITHM = "aiverse-package-sha256-v1"

ACTION_CLASSES = {
    "read_local", "read_connected", "write_local_reversible", "modify_canonical_state",
    "external_write_reversible", "send_message", "publish_publicly", "spend_money",
    "create_commit_or_pr", "merge_or_deploy", "delete_data", "change_permissions",
    "security_sensitive", "high_stakes_domain_action",
}
READ_ONLY_ACTIONS = {"read_local", "read_connected"}
STATUSES = {"success", "partial", "blocked", "failed", "aborted"}
EFFECT_STATES = {"occurred", "not_occurred", "uncertain"}
VERDICT_STATUSES = {"unverified", "passed", "failed", "insufficient_evidence", "not_applicable"}
EVIDENCE_KINDS = {
    "observation", "measurement", "canonical_state", "user_confirmation",
    "authoritative_external", "independent_evaluation",
}
SOURCE_KINDS = {"skill_runtime", "ai_verse_os", "user", "external_authority", "independent_evaluator"}
INDEPENDENCE = {"same_context", "fresh_context", "independent_model", "external_authoritative"}
_ALLOWED_SOURCE_INDEPENDENCE = {
    "skill_runtime": {"same_context"},
    "ai_verse_os": {"same_context", "fresh_context"},
    "user": {"same_context"},
    "external_authority": {"external_authoritative"},
    "independent_evaluator": {"fresh_context", "independent_model"},
}
_STRONG_KIND_SOURCE = {
    "measurement": {"ai_verse_os"},
    "canonical_state": {"ai_verse_os"},
    "user_confirmation": {"user"},
    "authoritative_external": {"external_authority"},
    "independent_evaluation": {"independent_evaluator"},
}
_HEX64 = re.compile(r"^[a-f0-9]{64}$")
_SCOPE = re.compile(r"^(operator|workspace:[a-z0-9][a-z0-9._-]{0,127})$")
_CAPABILITY = re.compile(r"^aiverse-skills:[a-z0-9][a-z0-9-]*$")
_GENERATION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,191}$")

_TOP_FIELDS = {
    "contract", "receipt_id", "status", "summary", "binding", "effect",
    "verification_context", "verification", "artifacts", "warnings",
    "remaining_uncertainty", "trace_id",
}
_REQUIRED_TOP = _TOP_FIELDS - {"artifacts"}
_BINDING_FIELDS = {
    "request_fingerprint", "scope", "action_class", "operation", "provider_id",
    "capability_id", "generation_id", "package_digest",
}
_EFFECT_FIELDS = {"state", "source_kind", "source_ref", "independence", "observed_at", "details"}
_REQUIRED_EFFECT = {"state", "source_kind", "source_ref", "independence"}
_CONTEXT_FIELDS = {"evaluator_id", "independence", "builder_context_id", "evaluator_context_id"}
_REQUIRED_CONTEXT = {"evaluator_id", "independence"}
_VERDICT_FIELDS = {"criterion_id", "status", "evidence", "rationale"}
_EVIDENCE_FIELDS = {
    "ref", "kind", "source_kind", "source_ref", "independence", "claim",
    "observed_at", "expires_at", "scope", "integrity",
}
_REQUIRED_EVIDENCE = {"ref", "kind", "source_kind", "source_ref", "independence"}


def _object(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value


def _exact_fields(value: Mapping[str, Any], allowed: set[str], required: set[str], label: str) -> None:
    unknown = set(value) - allowed
    missing = required - set(value)
    if unknown:
        raise ValueError(f"{label} has unknown fields: {', '.join(sorted(unknown))}")
    if missing:
        raise ValueError(f"{label} is missing fields: {', '.join(sorted(missing))}")


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _string_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")


def _validate_source(source_kind: Any, independence: Any, label: str) -> tuple[str, str]:
    source = _string(source_kind, f"{label}.source_kind")
    level = _string(independence, f"{label}.independence")
    if source not in SOURCE_KINDS:
        raise ValueError(f"unknown {label}.source_kind: {source}")
    if level not in INDEPENDENCE:
        raise ValueError(f"unknown {label}.independence: {level}")
    if level not in _ALLOWED_SOURCE_INDEPENDENCE[source]:
        raise ValueError(f"{label} source {source} cannot claim independence {level}")
    return source, level


def _validate_binding(binding: Mapping[str, Any]) -> None:
    _exact_fields(binding, _BINDING_FIELDS, _BINDING_FIELDS, "binding")
    fingerprint = _string(binding["request_fingerprint"], "binding.request_fingerprint")
    if not _HEX64.fullmatch(fingerprint):
        raise ValueError("binding.request_fingerprint must be 64 lowercase hex characters")
    scope = _string(binding["scope"], "binding.scope")
    if not _SCOPE.fullmatch(scope):
        raise ValueError("binding.scope is invalid")
    action_class = _string(binding["action_class"], "binding.action_class")
    if action_class not in ACTION_CLASSES:
        raise ValueError(f"unknown binding.action_class: {action_class}")
    _string(binding["operation"], "binding.operation")
    if binding["provider_id"] != PROVIDER_ID:
        raise ValueError(f"binding.provider_id must be {PROVIDER_ID}")
    capability_id = _string(binding["capability_id"], "binding.capability_id")
    if not _CAPABILITY.fullmatch(capability_id):
        raise ValueError("binding.capability_id must be a qualified aiverse-skills id")
    generation_id = _string(binding["generation_id"], "binding.generation_id")
    if not _GENERATION.fullmatch(generation_id):
        raise ValueError("binding.generation_id is not path-safe")
    digest = _object(binding["package_digest"], "binding.package_digest")
    _exact_fields(digest, {"algorithm", "value"}, {"algorithm", "value"}, "binding.package_digest")
    if digest["algorithm"] != PACKAGE_DIGEST_ALGORITHM:
        raise ValueError(f"binding.package_digest.algorithm must be {PACKAGE_DIGEST_ALGORITHM}")
    if not _HEX64.fullmatch(_string(digest["value"], "binding.package_digest.value")):
        raise ValueError("binding.package_digest.value must be 64 lowercase hex characters")


def _validate_context(context: Mapping[str, Any]) -> None:
    _exact_fields(context, _CONTEXT_FIELDS, _REQUIRED_CONTEXT, "verification_context")
    _string(context["evaluator_id"], "verification_context.evaluator_id")
    independence = _string(context["independence"], "verification_context.independence")
    if independence not in INDEPENDENCE:
        raise ValueError(f"unknown verification_context.independence: {independence}")
    builder = context.get("builder_context_id")
    evaluator = context.get("evaluator_context_id")
    if independence == "fresh_context":
        builder = _string(builder, "verification_context.builder_context_id")
        evaluator = _string(evaluator, "verification_context.evaluator_context_id")
        if builder == evaluator:
            raise ValueError("fresh-context verification requires distinct builder and evaluator contexts")
    else:
        if builder is not None:
            _string(builder, "verification_context.builder_context_id")
        if evaluator is not None:
            _string(evaluator, "verification_context.evaluator_context_id")


def _validate_verification(receipt: Mapping[str, Any]) -> None:
    verification = receipt["verification"]
    if not isinstance(verification, list):
        raise ValueError("verification must be an array")
    seen = set()
    trace_id = receipt["trace_id"]
    for index, raw in enumerate(verification):
        item = _object(raw, f"verification[{index}]")
        _exact_fields(item, _VERDICT_FIELDS, {"criterion_id", "status", "evidence"}, f"verification[{index}]")
        criterion = _string(item["criterion_id"], f"verification[{index}].criterion_id")
        if criterion in seen:
            raise ValueError(f"duplicate verification criterion_id: {criterion}")
        seen.add(criterion)
        status = _string(item["status"], f"verification[{index}].status")
        if status not in VERDICT_STATUSES:
            raise ValueError(f"unknown verification status: {status}")
        evidence = item["evidence"]
        if not isinstance(evidence, list):
            raise ValueError(f"verification[{index}].evidence must be an array")
        if status == "passed" and not evidence:
            raise ValueError(f"passed criterion {criterion} requires evidence")
        if "rationale" in item and not isinstance(item["rationale"], str):
            raise ValueError(f"verification[{index}].rationale must be a string")
        for evidence_index, raw_evidence in enumerate(evidence):
            label = f"verification[{index}].evidence[{evidence_index}]"
            entry = _object(raw_evidence, label)
            _exact_fields(entry, _EVIDENCE_FIELDS, _REQUIRED_EVIDENCE, label)
            ref = _string(entry["ref"], f"{label}.ref")
            if ref == trace_id:
                raise ValueError("trace_id is correlation metadata and cannot be criterion evidence")
            kind = _string(entry["kind"], f"{label}.kind")
            if kind not in EVIDENCE_KINDS:
                raise ValueError(f"unknown {label}.kind: {kind}")
            source, _ = _validate_source(entry["source_kind"], entry["independence"], label)
            _string(entry["source_ref"], f"{label}.source_ref")
            if kind in _STRONG_KIND_SOURCE and source not in _STRONG_KIND_SOURCE[kind]:
                raise ValueError(f"{kind} evidence cannot be self-asserted by source {source}")
            if kind == "observation" and source not in {"skill_runtime", "ai_verse_os"}:
                raise ValueError(f"observation evidence has unsupported source {source}")
            if "scope" in entry and not _SCOPE.fullmatch(_string(entry["scope"], f"{label}.scope")):
                raise ValueError(f"{label}.scope is invalid")
            for optional in ("claim", "observed_at", "expires_at", "integrity"):
                if optional in entry and not isinstance(entry[optional], str):
                    raise ValueError(f"{label}.{optional} must be a string")


def assert_binding(receipt: Mapping[str, Any], expected: Mapping[str, Any]) -> None:
    """Require every supplied expected binding field to match exactly."""
    binding = _object(receipt.get("binding"), "binding")
    for key, expected_value in expected.items():
        if key not in _BINDING_FIELDS:
            raise ValueError(f"unknown expected binding field: {key}")
        actual = binding.get(key)
        if actual != expected_value:
            raise ValueError(f"receipt binding mismatch for {key}: expected {expected_value!r}, got {actual!r}")


def validate_receipt(receipt: Mapping[str, Any], *, expected_binding: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    """Validate receipt shape, semantic safety rules, and optional exact binding."""
    data = _object(receipt, "receipt")
    _exact_fields(data, _TOP_FIELDS, _REQUIRED_TOP, "receipt")
    if data["contract"] != CONTRACT_ID:
        raise ValueError(f"receipt.contract must be {CONTRACT_ID}")
    receipt_id = _string(data["receipt_id"], "receipt.receipt_id")
    trace_id = _string(data["trace_id"], "receipt.trace_id")
    if receipt_id == trace_id:
        raise ValueError("receipt_id and trace_id must be distinct; trace_id is not proof")
    status = _string(data["status"], "receipt.status")
    if status not in STATUSES:
        raise ValueError(f"unknown receipt.status: {status}")
    _string(data["summary"], "receipt.summary")
    _string_list(data["warnings"], "receipt.warnings")
    _string_list(data["remaining_uncertainty"], "receipt.remaining_uncertainty")
    if "artifacts" in data and not isinstance(data["artifacts"], list):
        raise ValueError("receipt.artifacts must be an array")

    binding = _object(data["binding"], "binding")
    _validate_binding(binding)

    effect = _object(data["effect"], "effect")
    _exact_fields(effect, _EFFECT_FIELDS, _REQUIRED_EFFECT, "effect")
    effect_state = _string(effect["state"], "effect.state")
    if effect_state not in EFFECT_STATES:
        raise ValueError(f"unknown effect.state: {effect_state}")
    effect_source, _ = _validate_source(effect["source_kind"], effect["independence"], "effect")
    _string(effect["source_ref"], "effect.source_ref")
    if "observed_at" in effect and not isinstance(effect["observed_at"], str):
        raise ValueError("effect.observed_at must be a string")
    if "details" in effect and not isinstance(effect["details"], Mapping):
        raise ValueError("effect.details must be an object")

    _validate_context(_object(data["verification_context"], "verification_context"))
    _validate_verification(data)

    action_class = str(binding["action_class"])
    side_effect = action_class not in READ_ONLY_ACTIONS
    if status == "success" and side_effect:
        if effect_state != "occurred":
            raise ValueError("successful side-effect receipt must report effect.state=occurred")
        if effect_source != "ai_verse_os":
            raise ValueError("successful side-effect receipt requires AI-Verse OS effect verification")
    if status == "success" and not side_effect and effect_state != "not_occurred":
        raise ValueError("successful read-only receipt must report effect.state=not_occurred")

    if expected_binding is not None:
        assert_binding(data, expected_binding)
    return copy.deepcopy(dict(data))
