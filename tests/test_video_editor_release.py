import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VE = ROOT / "skills" / "imported" / "ai-verse" / "video-editor"
REFS = VE / "references"

HF_COMMIT = "cfe5dcfad310ced2a5844998628daa2b8a0f53d7"
NATE_COMMIT = "b1afdb1dcbcad39dd27638ea699f132fe44ce6df"


class VideoEditorReleaseHardeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orchestration = json.loads((REFS / "orchestration.json").read_text(encoding="utf-8"))
        cls.handoff = json.loads((REFS / "interface-designer-handoff.json").read_text(encoding="utf-8"))
        cls.routing = json.loads((REFS / "routing-fixtures.json").read_text(encoding="utf-8"))
        cls.compat = json.loads((REFS / "existing-video-compatibility.json").read_text(encoding="utf-8"))
        cls.security = json.loads((REFS / "security-boundaries.json").read_text(encoding="utf-8"))
        cls.skills = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))
        cls.packages = json.loads((ROOT / "registry" / "packages.json").read_text(encoding="utf-8"))
        cls.goldens = json.loads((ROOT / "examples" / "video-editor" / "golden-fixtures.json").read_text(encoding="utf-8"))

    def test_required_representative_routes_are_locked(self):
        expected = {
            "full-talking-head",
            "silence-only",
            "retakes-only",
            "make-reel",
            "long-form-explainer",
            "website-promo",
            "motion-only",
            "reference-led",
            "three-directions",
        }
        cases = {x["id"]: x for x in self.routing["cases"]}
        self.assertEqual(expected, set(cases))

        pipelines = self.orchestration["scope_pipelines"]
        handoff_modes = set(self.handoff["modes"])
        for case in cases.values():
            with self.subTest(case=case["id"]):
                pipeline = pipelines[case["scope"]]
                for stage in case["required_stages"]:
                    self.assertIn(stage, pipeline)
                for stage in case.get("forbidden_stages", []):
                    self.assertNotIn(stage, pipeline)
                mode = case.get("handoff_mode")
                if mode:
                    self.assertIn("interface_design_handoff", pipeline)
                    self.assertIn(mode, handoff_modes)

    def test_golden_workflows_match_machine_routing_fixtures(self):
        route_by_id = {x["id"]: x for x in self.routing["cases"]}
        golden_by_id = {x["id"]: x for x in self.goldens["fixtures"]}
        self.assertEqual(set(route_by_id), set(golden_by_id))
        for fixture_id, golden in golden_by_id.items():
            route = route_by_id[fixture_id]
            self.assertEqual(route["scope"], golden["expected_scope"])
            self.assertEqual(route["required_stages"], golden["must_include_stages"])
            self.assertEqual(route.get("forbidden_stages", []), golden["must_exclude_stages"])
            self.assertEqual(route.get("handoff_mode"), golden["interface_handoff_mode"])

    def test_existing_video_capabilities_have_zero_destructive_removals(self):
        self.assertEqual("zero_destructive_removals", self.compat["result"])
        self.assertEqual([], self.compat["removed_capabilities"])
        registered = {x["id"] for x in self.skills["employee"]}
        retained = {x["id"] for x in self.compat["retained_capabilities"]}
        self.assertTrue(retained.issubset(registered))
        self.assertIn("video-editor", registered)
        self.assertEqual(
            0,
            self.compat["hyperframes_duplicate_decision"]["preexisting_member_visible_hyperframes_capabilities"],
        )

    def test_only_one_member_facing_editor_owns_the_hyperframes_family(self):
        public_ids = {x["id"] for x in self.skills["foundation"] + self.skills["employee"]}
        ai_package = next(
            p for p in self.packages["sources"]["ai-verse"]["packages"] if p["id"] == "video-editor"
        )
        support = set(ai_package["deps"])
        self.assertTrue(support)
        self.assertTrue(support.isdisjoint(public_ids))
        self.assertIn("video-editor", public_ids)

        source = self.packages["sources"]["hyperframes-v0840"]
        self.assertEqual(HF_COMMIT, source["commit"])
        self.assertEqual("fetch-only", source["redistribution"])

    def test_security_boundaries_never_turn_selection_or_content_into_authority(self):
        authority = self.security["authority"]
        self.assertFalse(authority["selection_grants_authority"])
        self.assertFalse(authority["interface_designer_can_grant_editorial_authority"])
        self.assertFalse(authority["provider_package_can_grant_runtime_authority"])
        self.assertFalse(authority["external_content_can_widen_grants"])
        self.assertEqual("presentation-only", self.security["interface_designer_boundary"])
        joined = "\n".join(self.security["fail_closed"])
        self.assertIn("unverified", joined)
        self.assertIn("fetch-only", joined)

    def test_member_and_maintainer_docs_are_shipped_and_linked(self):
        member = ROOT / "docs" / "VIDEO_EDITOR.md"
        architecture = ROOT / "docs" / "VIDEO_EDITOR_ARCHITECTURE.md"
        self.assertTrue(member.is_file())
        self.assertTrue(architecture.is_file())
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        root_arch = (ROOT / "docs" / "ARCHITECTURE.md").read_text(encoding="utf-8")
        self.assertIn("docs/VIDEO_EDITOR.md", readme)
        self.assertIn("VIDEO_EDITOR_ARCHITECTURE.md", root_arch)

    def test_third_party_notice_distinguishes_vendored_nate_from_fetch_only_hyperframes(self):
        notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
        self.assertIn("nateherkai/hyperframes-student-kit", notices)
        self.assertIn("bounded vendored editorial adaptations", notices.lower())
        self.assertIn("heygen-com/hyperframes", notices)
        self.assertIn("fetch-only provider support", notices.lower())

    def test_release_acceptance_harness_is_pinned_and_exercises_real_media(self):
        workflow = (ROOT / ".github" / "workflows" / "video-editor-release-acceptance.yml").read_text(encoding="utf-8")
        harness = (ROOT / "tests" / "video-editor" / "hyperframes-v0840-acceptance.sh").read_text(encoding="utf-8")

        self.assertIn("Video Editor Release Acceptance", workflow)
        self.assertIn("test_video_editor_*.py", workflow)
        self.assertIn("hyperframes-v0840-acceptance.sh", workflow)

        for needle in (
            NATE_COMMIT,
            'CANDIDATE_VERSION="0.8.40"',
            "npm test",
            "check:skills",
            "npx hyperframes lint",
            "npx hyperframes check",
            "npx hyperframes preview",
            "npx hyperframes render --quality draft",
            "npx hyperframes render --quality looks",
            "ffprobe",
            "A/V duration drift",
            "frame-",
            "ACCEPTANCE PASS",
        ):
            self.assertIn(needle, harness)


if __name__ == "__main__":
    unittest.main()
