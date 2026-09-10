from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("execution_receipt_v2", ROOT / "installer" / "execution_receipt_v2.py")
assert SPEC and SPEC.loader
receipt_v2 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(receipt_v2)


FINGERPRINT = "a" * 64
PACKAGE_DIGEST = "b" * 64


def base_receipt(*, action_class: str = "send_message", status: str = "success"):
    side_effect = action_class not in receipt_v2.READ_ONLY_ACTIONS
    return {
        "contract": "aiverse-execution-receipt-v2",
        "receipt_id": "receipt-123",
        "status": status,
        "summary": "Execution finished.",
        "binding": {
            "request_fingerprint": FINGERPRINT,
            "scope": "workspace:demo",
            "action_class": action_class,
            "operation": "demo.operation",
            "provider_id": "aiverse-skills",
            "capability_id": "aiverse-skills:demo-skill",
            "generation_id": "gen-20260910T120000000000Z-deadbeef",
            "package_digest": {
                "algorithm": "aiverse-package-sha256-v1",
                "value": PACKAGE_DIGEST,
            },
        },
        "effect": {
            "state": "occurred" if side_effect else "not_occurred",
            "source_kind": "ai_verse_os" if side_effect else "skill_runtime",
            "source_ref": "os-effect-check:123" if side_effect else "skill-run:123",
            "independence": "same_context",
        },
        "verification_context": {
            "evaluator_id": "ai-verse-os" if side_effect else "aiverse-skills-runtime",
            "independence": "same_context",
        },
        "verification": [],
        "warnings": [],
        "remaining_uncertainty": [],
        "trace_id": "trace-123",
    }


class ReceiptV2Tests(unittest.TestCase):
    def test_v2_schema_exists_without_changing_v1(self):
        v1 = json.loads((ROOT / "schemas" / "execution-receipt-v1.schema.json").read_text(encoding="utf-8"))
        v2 = json.loads((ROOT / "schemas" / "execution-receipt-v2.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(v1["properties"]["contract"]["const"], "aiverse-execution-receipt-v1")
        self.assertEqual(v1["properties"]["status"]["enum"], ["success", "partial", "blocked", "failed", "aborted"])
        self.assertEqual(v2["properties"]["contract"]["const"], "aiverse-execution-receipt-v2")
        for field in ("receipt_id", "binding", "effect", "verification_context"):
            self.assertIn(field, v2["required"])

    def test_valid_side_effect_success_is_os_verified_and_generation_bound(self):
        receipt = base_receipt()
        validated = receipt_v2.validate_receipt(receipt, expected_binding={
            "request_fingerprint": FINGERPRINT,
            "scope": "workspace:demo",
            "action_class": "send_message",
            "operation": "demo.operation",
            "provider_id": "aiverse-skills",
            "capability_id": "aiverse-skills:demo-skill",
            "generation_id": "gen-20260910T120000000000Z-deadbeef",
            "package_digest": {
                "algorithm": "aiverse-package-sha256-v1",
                "value": PACKAGE_DIGEST,
            },
        })
        self.assertEqual(validated["effect"]["source_kind"], "ai_verse_os")

    def test_successful_side_effect_cannot_self_assert_effect(self):
        receipt = base_receipt()
        receipt["effect"].update({"source_kind": "skill_runtime", "source_ref": "self", "independence": "same_context"})
        with self.assertRaisesRegex(ValueError, "requires AI-Verse OS effect verification"):
            receipt_v2.validate_receipt(receipt)

    def test_read_success_has_no_side_effect(self):
        receipt = base_receipt(action_class="read_connected")
        validated = receipt_v2.validate_receipt(receipt)
        self.assertEqual(validated["effect"]["state"], "not_occurred")

    def test_trace_id_is_not_receipt_or_evidence(self):
        receipt = base_receipt()
        receipt["receipt_id"] = receipt["trace_id"]
        with self.assertRaisesRegex(ValueError, "trace_id is not proof"):
            receipt_v2.validate_receipt(receipt)

        receipt = base_receipt()
        receipt["verification"] = [{
            "criterion_id": "delivered",
            "status": "passed",
            "evidence": [{
                "ref": receipt["trace_id"],
                "kind": "measurement",
                "source_kind": "ai_verse_os",
                "source_ref": "os-check:1",
                "independence": "same_context",
            }],
        }]
        with self.assertRaisesRegex(ValueError, "cannot be criterion evidence"):
            receipt_v2.validate_receipt(receipt)

    def test_strong_evidence_cannot_be_self_labeled(self):
        receipt = base_receipt()
        receipt["verification"] = [{
            "criterion_id": "delivered",
            "status": "passed",
            "evidence": [{
                "ref": "proof:1",
                "kind": "measurement",
                "source_kind": "skill_runtime",
                "source_ref": "self",
                "independence": "same_context",
            }],
        }]
        with self.assertRaisesRegex(ValueError, "cannot be self-asserted"):
            receipt_v2.validate_receipt(receipt)

    def test_passed_criterion_requires_evidence(self):
        receipt = base_receipt()
        receipt["verification"] = [{"criterion_id": "delivered", "status": "passed", "evidence": []}]
        with self.assertRaisesRegex(ValueError, "requires evidence"):
            receipt_v2.validate_receipt(receipt)

    def test_fresh_context_requires_distinct_context_ids(self):
        receipt = base_receipt(action_class="read_local")
        receipt["verification_context"] = {
            "evaluator_id": "fresh-verifier",
            "independence": "fresh_context",
            "builder_context_id": "same",
            "evaluator_context_id": "same",
        }
        with self.assertRaisesRegex(ValueError, "distinct builder and evaluator"):
            receipt_v2.validate_receipt(receipt)

    def test_binding_mismatch_rejects_stale_generation(self):
        receipt = base_receipt()
        with self.assertRaisesRegex(ValueError, "binding mismatch for generation_id"):
            receipt_v2.validate_receipt(receipt, expected_binding={"generation_id": "gen-new"})

    def test_binding_mismatch_rejects_wrong_action(self):
        receipt = base_receipt()
        with self.assertRaisesRegex(ValueError, "binding mismatch for request_fingerprint"):
            receipt_v2.validate_receipt(receipt, expected_binding={"request_fingerprint": "c" * 64})

    def test_partial_effect_can_be_reported_without_being_upgraded_to_success(self):
        receipt = base_receipt(status="partial")
        receipt["effect"].update({
            "state": "uncertain",
            "source_kind": "skill_runtime",
            "source_ref": "skill-run:partial",
            "independence": "same_context",
        })
        validated = receipt_v2.validate_receipt(receipt)
        self.assertEqual(validated["status"], "partial")
        self.assertEqual(validated["effect"]["state"], "uncertain")

    def test_source_cannot_overclaim_independence(self):
        receipt = base_receipt()
        receipt["effect"]["independence"] = "external_authoritative"
        with self.assertRaisesRegex(ValueError, "cannot claim independence"):
            receipt_v2.validate_receipt(receipt)


if __name__ == "__main__":
    unittest.main()
