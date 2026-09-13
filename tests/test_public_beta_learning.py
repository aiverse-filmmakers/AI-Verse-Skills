import json
import shutil
import tempfile
import unittest
from pathlib import Path

from installer import aiverse_skills as skills
from installer import execution_receipt_v2
from installer import learning


class PublicBetaLearningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "skills-root"
        self.root.mkdir()
        self._install_one_foundation()
        skills.setup_component(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def _install_one_foundation(self):
        gid = skills.new_generation_id()
        stage = self.base / "stage"
        src = skills.REPO_ROOT / "skills" / "foundation" / "verification-harness"
        dst = stage / "foundation" / "verification-harness"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)
        installed = [{
            "kind": "foundation",
            "id": "verification-harness",
            "path": "foundation/verification-harness",
            "source_repo": "aiverse-filmmakers/AI-Verse-Skills",
            "source_commit": None,
            "operators": [],
            "digest_sha256": skills.digest(dst),
        }]
        skills._write_stage_manifest("test", installed, gid, stage)
        self.assertEqual(skills.verify_stage(stage, gid), [])
        skills.commit_stage(self.root, stage, gid)
        skills.activate_generation(self.root, gid)

    def _candidate(self, name, body="Perform the procedure and verify the outcome."):
        d = self.base / ("candidate-" + name + "-" + str(len(list(self.base.glob("candidate-*")))))
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\n"
            f"name: {name}\n"
            f"description: Learned test Skill {name}\n"
            "version: 1.0.0\n"
            "---\n\n"
            f"{body}\n",
            encoding="utf-8",
        )
        return d

    def test_setup_status_and_lifecycle_separation(self):
        status = skills.status_report(self.root)
        self.assertEqual(status["state"], "ready")
        pin = skills.pin_active_generation(self.root, skills.digest)
        admission = json.loads((pin.generation_path / ".aiverse" / "admission.json").read_text())
        package = admission["packages"][0]
        self.assertEqual(package["integrity"]["status"], "verified")
        self.assertEqual(package["admission"], "admitted")
        self.assertTrue(package["trusted"])
        self.assertEqual(package["readiness"], "not-evaluated")
        self.assertIs(package["authorized"], False)

        disabled = skills.disable_component(self.root)
        self.assertEqual(disabled["state"], "disabled")
        enabled = skills.enable_component(self.root)
        self.assertEqual(enabled["state"], "ready")

    def test_create_requires_approval_even_in_auto_then_promotes_immutably(self):
        learning.set_learning_mode(skills, self.root, "auto")
        proposal = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "learned-test",
                "summary": "Reusable verified procedure",
                "evidence_refs": ["memory:example-success"],
                "risk": "low",
                "confidence": 0.95,
            },
            self._candidate("learned-test"),
            trigger="explicit-learn",
            explicit=True,
        )
        evaluated = learning.evaluate_proposal(skills, self.root, proposal["proposal_id"])
        self.assertEqual(evaluated["state"], "pending_approval")
        before = skills.pin_active_generation(self.root, skills.digest).generation_id
        applied = learning.apply_proposal(
            skills, self.root, proposal["proposal_id"], approved_by="test-user"
        )
        self.assertEqual(applied["state"], "applied")
        self.assertNotEqual(applied["applied_generation_id"], before)
        pin = skills.pin_active_generation(self.root, skills.digest)
        learned = [p for p in pin.manifest["packages"] if p["id"] == "learned-test"][0]
        self.assertEqual(learned["kind"], "learned")
        self.assertEqual(learned["ownership"], "agent_learned")

        # Later-task acceptance: a fresh consumer pins the promoted generation,
        # loads the learned Skill from that exact generation, and submits a
        # generation/digest-bound successful receipt before usage is recorded.
        skill_md = pin.package_path("learned-test") / "SKILL.md"
        self.assertIn("Perform the procedure", skill_md.read_text(encoding="utf-8"))
        binding = {
            "request_fingerprint": "a" * 64,
            "scope": "workspace:learning-acceptance",
            "action_class": "read_local",
            "operation": "learned.acceptance",
            "provider_id": "aiverse-skills",
            "capability_id": learned["qualified_id"],
            "generation_id": pin.generation_id,
            "package_digest": learned["digest"],
        }
        receipt = {
            "contract": "aiverse-execution-receipt-v2",
            "receipt_id": "receipt-learned-acceptance",
            "status": "success",
            "summary": "Promoted learned Skill was selected and loaded successfully.",
            "binding": binding,
            "effect": {
                "state": "not_occurred",
                "source_kind": "skill_runtime",
                "source_ref": "learned-use:1",
                "independence": "same_context",
            },
            "verification_context": {
                "evaluator_id": "ai-verse-os",
                "independence": "same_context",
            },
            "verification": [{
                "criterion_id": "skill-loaded",
                "status": "passed",
                "evidence": [{
                    "ref": f"generation:{pin.generation_id}:learned-test",
                    "kind": "measurement",
                    "source_kind": "ai_verse_os",
                    "source_ref": "provider-load-check:1",
                    "independence": "same_context",
                }],
            }],
            "warnings": [],
            "remaining_uncertainty": [],
            "trace_id": "trace-learned-acceptance",
        }
        validated = execution_receipt_v2.validate_receipt(receipt, expected_binding=binding)
        self.assertEqual(validated["status"], "success")
        usage = learning.record_usage(skills, self.root, "learned-test", success=True)
        self.assertEqual(usage["success_count"], 1)

    def test_auto_repair_only_for_agent_learned_and_compare_and_set_bound(self):
        create = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "learned-repair",
                "evidence_refs": ["memory:seed"],
                "risk": "low",
                "confidence": 1.0,
            },
            self._candidate("learned-repair"),
            trigger="explicit-learn",
            explicit=True,
        )
        learning.evaluate_proposal(skills, self.root, create["proposal_id"])
        learning.apply_proposal(skills, self.root, create["proposal_id"], approved_by="test-user")
        learning.set_learning_mode(skills, self.root, "auto")

        repair = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "repair",
                "target_skill_id": "learned-repair",
                "evidence_refs": ["gateway:failed-use"],
                "risk": "low",
                "confidence": 0.99,
            },
            self._candidate("learned-repair", "Use the corrected procedure and verify twice."),
            trigger="foreground-correction",
            explicit=False,
        )
        result = learning.evaluate_proposal(
            skills, self.root, repair["proposal_id"], auto_apply=True
        )
        self.assertEqual(result["state"], "applied")
        self.assertEqual(result["approved_by"], "policy:auto")

        protected = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "repair",
                "target_skill_id": "verification-harness",
                "evidence_refs": ["gateway:correction"],
                "risk": "low",
                "confidence": 0.9,
            },
            self._candidate("verification-harness", "Modified protected content."),
            trigger="foreground-correction",
            explicit=False,
        )
        evaluated = learning.evaluate_proposal(skills, self.root, protected["proposal_id"])
        self.assertEqual(evaluated["state"], "pending_approval")
        with self.assertRaisesRegex(RuntimeError, "never overwrites protected"):
            learning.apply_proposal(
                skills, self.root, protected["proposal_id"], approved_by="test-user"
            )

    def test_off_blocks_background_but_explicit_learn_remains(self):
        learning.set_learning_mode(skills, self.root, "off")
        with self.assertRaisesRegex(RuntimeError, "learning is off"):
            learning.submit_candidate(
                skills,
                self.root,
                {
                    "kind": "create",
                    "skill_id": "background-blocked",
                    "evidence_refs": ["gateway:post-run"],
                    "risk": "low",
                    "confidence": 0.8,
                },
                self._candidate("background-blocked"),
                trigger="post-run",
                explicit=False,
            )

        explicit = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "explicit-allowed",
                "evidence_refs": ["user:learn"],
                "risk": "low",
                "confidence": 1.0,
            },
            self._candidate("explicit-allowed"),
            trigger="explicit-learn",
            explicit=True,
        )
        self.assertEqual(explicit["state"], "proposal")

    def test_secret_candidate_is_quarantined(self):
        bad = self._candidate(
            "secret-bad",
            "-----BEGIN PRIVATE KEY-----\nnot-a-real-key\n-----END PRIVATE KEY-----",
        )
        proposal = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "secret-bad",
                "evidence_refs": ["user:learn"],
                "risk": "low",
                "confidence": 1.0,
            },
            bad,
            trigger="explicit-learn",
            explicit=True,
        )
        evaluated = learning.evaluate_proposal(skills, self.root, proposal["proposal_id"])
        self.assertEqual(evaluated["state"], "quarantined")
        self.assertEqual(evaluated["quarantine_reason"], "security-deny")

    def test_archive_restore_and_learning_rollback(self):
        proposal = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "archive-me",
                "evidence_refs": ["user:learn"],
                "risk": "low",
                "confidence": 1.0,
            },
            self._candidate("archive-me"),
            trigger="explicit-learn",
            explicit=True,
        )
        learning.evaluate_proposal(skills, self.root, proposal["proposal_id"])
        applied = learning.apply_proposal(
            skills, self.root, proposal["proposal_id"], approved_by="test-user"
        )
        archived = learning.archive_skill(
            skills, self.root, "archive-me", approved_by="test-user"
        )
        self.assertEqual(archived["skill_id"], "archive-me")
        pin = skills.pin_active_generation(self.root, skills.digest)
        self.assertIsNone(learning._find_package(pin.manifest, "archive-me"))
        self.assertFalse((pin.generation_path / "learned" / "archive-me").exists())

        restored = learning.restore_archived(skills, self.root, "archive-me")
        self.assertEqual(restored["skill_id"], "archive-me")
        pin = skills.pin_active_generation(self.root, skills.digest)
        self.assertIsNotNone(learning._find_package(pin.manifest, "archive-me"))

        # Rollback is compare-and-set: a proposal can only roll back while its own
        # applied generation is still active. The earlier create is no longer current.
        with self.assertRaisesRegex(RuntimeError, "newer generation"):
            learning.rollback_learning_change(skills, self.root, proposal["proposal_id"])

    def test_curator_creates_evaluable_archive_review(self):
        proposal = learning.submit_candidate(
            skills,
            self.root,
            {
                "kind": "create",
                "skill_id": "curator-stale",
                "evidence_refs": ["user:learn"],
                "risk": "low",
                "confidence": 1.0,
            },
            self._candidate("curator-stale"),
            trigger="explicit-learn",
            explicit=True,
        )
        learning.evaluate_proposal(skills, self.root, proposal["proposal_id"])
        learning.apply_proposal(skills, self.root, proposal["proposal_id"], approved_by="test-user")

        config = learning.ensure_learning_state(skills, self.root)
        config["stale_after_days"] = 0
        config["archive_review_after_days"] = 0
        skills._atomic_json_write(learning._paths(self.root)["config"], config)

        result = learning.curator_run(skills, self.root)
        self.assertIn("curator-stale", result["stale"])
        self.assertEqual(len(result["archive_proposals"]), 1)
        archive_proposal = learning._load_proposal(self.root, result["archive_proposals"][0])
        self.assertEqual(archive_proposal["state"], "proposal")
        evaluated = learning.evaluate_proposal(skills, self.root, archive_proposal["proposal_id"])
        self.assertEqual(evaluated["state"], "pending_approval")

    def test_cli_parser_exposes_public_beta_commands(self):
        parser = skills.parser()
        for argv in (
            ["status", "--json"],
            ["setup", "--json"],
            ["learning", "status", "--json"],
            ["proposals", "list", "--json"],
            ["curator", "status", "--json"],
        ):
            args = parser.parse_args(argv)
            self.assertTrue(callable(args.fn))


if __name__ == "__main__":
    unittest.main()
