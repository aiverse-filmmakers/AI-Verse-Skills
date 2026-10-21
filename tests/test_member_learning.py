import unittest
from installer import aiverse_skills as skills, learning, member_library as library
from tests import test_public_beta_learning as Fixtures

class MemberLearningTests(unittest.TestCase):
    setUp = Fixtures.PublicBetaLearningTests.setUp
    tearDown = Fixtures.PublicBetaLearningTests.tearDown
    _install_one_foundation = Fixtures.PublicBetaLearningTests._install_one_foundation
    _candidate = Fixtures.PublicBetaLearningTests._candidate

    def configured(self):
        self.personal = self.base / "personal"
        library.configure_learning(skills, self.root, self.personal, apply=True)

    def proposal(self, **extra):
        env = {"kind": "create", "scope": {"aiverse_scope": "workspace:alpha"}, "source_ownership": "agent_learned",
               "skill_id": "shared-method", "summary": "Reusable verified method", "evidence_refs": ["run:verified"], "risk": "low", "confidence": .95, **extra}
        item = learning.submit_candidate(skills, self.root, env, self._candidate("shared-method"), trigger="explicit-learn", explicit=True)
        return learning.evaluate_proposal(skills, self.root, item["proposal_id"])

    def test_default_proposal_does_not_activate_and_approved_create_uses_member_owner(self):
        self.configured()
        before = skills.pin_active_generation(self.root, skills.digest).generation_id
        item = self.proposal(portability=library.PORTABILITY)
        self.assertEqual(item["state"], "pending_approval")
        self.assertFalse(self.personal.exists())
        applied = learning.apply_proposal(skills, self.root, item["proposal_id"], approved_by="fixture-user")
        self.assertIn("member_import", applied)
        self.assertEqual(skills.pin_active_generation(self.root, skills.digest).generation_id, before)
        record = library.read_index(self.personal)["skills"][applied["member_import"]["id"]]
        self.assertEqual(record["visibility"], "shared")
        self.assertEqual(library.verify(self.personal)["ok"], True)
        learning.rollback_learning_change(skills, self.root, item["proposal_id"])
        self.assertFalse(library.read_index(self.personal)["skills"][record["id"]]["enabled"])
        self.assertTrue(library.revision_path(self.personal, record["id"], record["active_revision"]).exists())

    def test_unknown_portability_stays_workspace_restricted(self):
        self.configured()
        item = self.proposal()
        applied = learning.apply_proposal(skills, self.root, item["proposal_id"], approved_by="fixture-user")
        record = library.read_index(self.personal)["skills"][applied["member_import"]["id"]]
        self.assertEqual(record["visibility"], "workspace:alpha")

    def test_explicit_workspace_only_is_not_broadened_by_portability(self):
        self.configured()
        item = self.proposal(source_ownership="workspace_local", scope={"workspace_id": "alpha"}, portability=library.PORTABILITY)
        applied = learning.apply_proposal(skills, self.root, item["proposal_id"], approved_by="fixture-user")
        self.assertEqual(library.read_index(self.personal)["skills"][applied["member_import"]["id"]]["visibility"], "workspace:alpha")

    def test_uncertain_candidate_does_not_bypass_private_auto_policy(self):
        self.configured()
        learning.set_learning_mode(skills, self.root, "auto")
        item = self.proposal()
        self.assertEqual(item["state"], "pending_approval")
        self.assertFalse(self.personal.exists())

    def test_component_doctor_checks_configured_member_integrity(self):
        self.configured()
        item = self.proposal(portability=library.PORTABILITY)
        result = learning.apply_proposal(skills, self.root, item["proposal_id"], approved_by="fixture-user")
        self.assertTrue(skills.doctor_report(self.root)["ok"])
        target = library.revision_path(self.personal, result["member_import"]["id"], result["member_import"]["revision"])
        (target / "SKILL.md").write_text("damaged")
        self.assertFalse(skills.doctor_report(self.root)["checks"]["member_library"]["ok"])

    def test_member_library_participates_in_learning_deduplication(self):
        self.configured()
        first = self.proposal(portability=library.PORTABILITY)
        learning.apply_proposal(skills, self.root, first["proposal_id"], approved_by="fixture-user")
        learning.set_learning_mode(skills, self.root, "auto")
        another = self.proposal(portability=library.PORTABILITY)
        self.assertEqual(another["state"], "pending_approval")
        self.assertTrue(another["evaluation"]["dedup"]["duplicate"])
        self.assertEqual(len(library.read_index(self.personal)["skills"]), 1)

    def test_route_rebinding_refuses_without_moving_skills(self):
        self.configured()
        with self.assertRaisesRegex(RuntimeError, "another library"):
            library.configure_learning(skills, self.root, self.base / "elsewhere", apply=True)
        self.assertFalse(self.personal.exists())

    def test_unknown_operator_candidate_remains_unapplied(self):
        self.configured()
        item = self.proposal(scope={"aiverse_scope": "operator"})
        with self.assertRaisesRegex(RuntimeError, "portability review"):
            learning.apply_proposal(skills, self.root, item["proposal_id"], approved_by="fixture-user")
        self.assertFalse(self.personal.exists())
