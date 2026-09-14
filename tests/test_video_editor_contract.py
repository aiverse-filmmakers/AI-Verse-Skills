import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO_EDITOR = ROOT / "skills" / "imported" / "ai-verse" / "video-editor"

HF_COMMIT = "cfe5dcfad310ced2a5844998628daa2b8a0f53d7"
NATE_COMMIT = "b1afdb1dcbcad39dd27638ea699f132fe44ce6df"
HF_SUPPORT = {
    "hyperframes",
    "hyperframes-core",
    "hyperframes-cli",
    "hyperframes-animation",
    "hyperframes-keyframes",
    "hyperframes-creative",
    "hyperframes-audio",
    "hyperframes-registry",
    "media-use",
    "general-video",
    "embedded-captions",
}


class VideoEditorContractTests(unittest.TestCase):
    def load_json(self, name):
        return json.loads((VIDEO_EDITOR / "references" / name).read_text(encoding="utf-8"))

    def registry(self, name):
        return json.loads((ROOT / "registry" / name).read_text(encoding="utf-8"))

    def test_package_is_accepted_release(self):
        skill = (VIDEO_EDITOR / "SKILL.md").read_text(encoding="utf-8")
        manifest = (VIDEO_EDITOR / "aiverse.skill.yaml").read_text(encoding="utf-8")
        registry = self.registry("skills.json")
        employee = {x["id"]: x for x in registry["employee"]}

        self.assertIn("name: video-editor", skill)
        self.assertIn("version: 1.0.0", skill)\n        self.assertNotIn("registered-release-candidate", skill)
        self.assertIn("name: video-editor", manifest)
        self.assertIn("video-editor", employee)
        self.assertEqual(100, employee["video-editor"]["rank"])
        self.assertEqual("ai-verse-native", employee["video-editor"]["implementation"])
        self.assertEqual("vendored", employee["video-editor"]["state"])

    def test_video_editor_package_resolves_exact_internal_hyperframes_dependencies(self):
        packages = self.registry("packages.json")
        source = packages["sources"]["hyperframes-v0840"]
        self.assertEqual("heygen-com/hyperframes", source["repo"])
        self.assertEqual(HF_COMMIT, source["commit"])
        self.assertEqual("Apache-2.0", source["license"])
        self.assertEqual("fetch-only", source["redistribution"])
        self.assertEqual("hyperframes", source["namespace"])

        ai_package = next(
            p for p in packages["sources"]["ai-verse"]["packages"] if p["id"] == "video-editor"
        )
        self.assertEqual(HF_SUPPORT, set(ai_package["deps"]))

        support = {p["id"]: p for p in packages["support"]}
        self.assertTrue(HF_SUPPORT.issubset(support))
        for sid in HF_SUPPORT:
            with self.subTest(support=sid):
                self.assertEqual("hyperframes-v0840", support[sid]["source"])
                self.assertEqual(f"skills/{sid}", support[sid]["path"])

    def test_hyperframes_support_packages_are_not_member_capabilities(self):
        skills = self.registry("skills.json")
        public_ids = {x["id"] for x in skills["foundation"] + skills["employee"]}
        self.assertTrue(HF_SUPPORT.isdisjoint(public_ids))
        self.assertIn("video-editor", public_ids)

        provider = self.load_json("hyperframes-provider.json")
        self.assertEqual([], provider["member_visible_provider_capabilities"])
        self.assertEqual("video-editor", provider["member_visible_editor_capability"])
        self.assertEqual(HF_SUPPORT, set(provider["support_packages"]))

    def test_hyperframes_trust_is_pinned_fetch_only(self):
        trust = self.registry("trust-policy.json")["sources"]["heygen-com/hyperframes"]
        self.assertEqual("Apache-2.0", trust["license"])
        self.assertEqual("fetch-only", trust["redistribution"])
        self.assertEqual("reviewed-upstream", trust["trust"])
        self.assertFalse(trust["vendoring_allowed"])
        self.assertFalse(trust["auto_mutation"])

    def test_video_editor_is_in_full_creator_and_filmmaker_profiles(self):
        profiles = self.registry("profiles.json")["profiles"]
        for name in ("full", "creator", "filmmaker"):
            with self.subTest(profile=name):
                self.assertIn("video-editor", profiles[name]["employee_skills"])
        for name in ("universal", "business", "sales", "finance"):
            with self.subTest(profile=name):
                self.assertNotIn("video-editor", profiles[name]["employee_skills"])

    def test_semantic_capability_map_contains_required_editorial_runtime_and_qa_surfaces(self):
        data = self.load_json("capabilities.json")
        ids = {x["id"] for x in data["semantic_capabilities"]}
        required = {
            "video.edit.orchestrate",
            "video.transcribe",
            "video.cut.silence",
            "video.cut.mistakes",
            "video.edl",
            "video.shortform.edit",
            "video.longform.storytelling",
            "video.hook_payoff",
            "video.reference_analysis",
            "video.caption",
            "video.broll.plan",
            "video.motion_beats",
            "video.style_select",
            "video.website_to_video",
            "video.hyperframes.compose",
            "video.gsap.motion",
            "video.ffmpeg.media",
            "video.qa.structural",
            "video.qa.visual",
            "video.qa.audio_sync",
            "video.render.final",
        }
        self.assertEqual(required, ids)

    def test_exact_accepted_provider_pins_are_frozen(self):
        providers = self.load_json("capabilities.json")["provider_decisions"]
        self.assertEqual("0.8.40", providers["hyperframes"]["version"])
        self.assertEqual(HF_COMMIT, providers["hyperframes"]["commit"])
        self.assertEqual("accepted-canonical", providers["hyperframes"]["state"])
        self.assertEqual(NATE_COMMIT, providers["nate_editorial"]["commit"])
        self.assertEqual("integrated-package-local", providers["nate_editorial"]["state"])

        provider = self.load_json("hyperframes-provider.json")
        self.assertEqual("0.8.40", provider["source"]["version"])
        self.assertEqual(HF_COMMIT, provider["source"]["commit"])
        self.assertEqual(34888930903, provider["acceptance"]["run_id"])
        self.assertEqual("pass", provider["acceptance"]["result"])

    def test_every_scope_pipeline_starts_with_source_intake(self):
        data = self.load_json("orchestration.json")
        for scope, stages in data["scope_pipelines"].items():
            with self.subTest(scope=scope):
                self.assertEqual("source_intake", stages[0])

    def test_full_edit_preserves_editorial_truth_before_visual_handoff(self):
        stages = self.load_json("orchestration.json")["scope_pipelines"]["FULL_EDIT"]
        self.assertLess(stages.index("edl_truth"), stages.index("visual_plan"))
        self.assertLess(stages.index("edl_truth"), stages.index("interface_design_handoff"))
        self.assertLess(stages.index("shortform_editorial"), stages.index("hyperframes_compose"))
        self.assertLess(stages.index("longform_storytelling"), stages.index("hyperframes_compose"))
        self.assertLess(stages.index("structural_qa"), stages.index("final_render"))
        self.assertLess(stages.index("audio_sync_qa"), stages.index("final_render"))

    def test_narrow_silence_route_does_not_invoke_visual_or_renderer_stages(self):
        stages = set(self.load_json("orchestration.json")["scope_pipelines"]["SILENCE_ONLY"])
        forbidden = {
            "visual_plan",
            "style_direction",
            "interface_design_handoff",
            "hyperframes_compose",
            "final_render",
        }
        self.assertTrue(forbidden.isdisjoint(stages))

    def test_interface_designer_is_presentation_only(self):
        data = self.load_json("orchestration.json")
        handoff = next(x for x in data["stages"] if x["id"] == "interface_design_handoff")
        self.assertEqual(["interface-designer"], handoff["capabilities"])
        self.assertEqual("presentation-only", handoff["boundary"])

        ownership = (VIDEO_EDITOR / "references" / "ownership.md").read_text(encoding="utf-8")
        for forbidden_owner in (
            "transcript truth",
            "EDLs",
            "editorial cuts",
            "source-time mapping",
            "audio sync",
            "HyperFrames correctness",
        ):
            self.assertIn(forbidden_owner, ownership)

    def test_release_fail_closed_rules_protect_provider_and_verification(self):
        data = self.load_json("orchestration.json")
        self.assertEqual("accepted", data["release_gate_state"])
        joined = "\n".join(data["fail_closed"])
        self.assertIn("Nate-derived editorial provenance", joined)
        self.assertIn("HyperFrames 0.8.40", joined)
        self.assertIn("support dependencies install", joined)
        self.assertIn("Do not expose HyperFrames provider support packages", joined)
        self.assertIn("Do not use Interface Designer as an editorial fallback", joined)
        self.assertIn("Do not claim final media verification from composition source alone", joined)


if __name__ == "__main__":
    unittest.main()
