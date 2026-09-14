import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO_EDITOR = ROOT / "skills" / "imported" / "ai-verse" / "video-editor"


class VideoEditorContractTests(unittest.TestCase):
    def load_json(self, name):
        return json.loads((VIDEO_EDITOR / "references" / name).read_text(encoding="utf-8"))

    def test_package_is_present_but_fail_closed_before_registration(self):
        skill = (VIDEO_EDITOR / "SKILL.md").read_text(encoding="utf-8")
        manifest = (VIDEO_EDITOR / "aiverse.skill.yaml").read_text(encoding="utf-8")
        registry = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))

        self.assertIn("name: video-editor", skill)
        self.assertIn("registration: fail-closed-until-provider-integration", skill)
        self.assertIn("name: video-editor", manifest)
        self.assertNotIn("video-editor", {x["id"] for x in registry["employee"]})

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
        self.assertEqual(
            "cfe5dcfad310ced2a5844998628daa2b8a0f53d7",
            providers["hyperframes"]["commit"],
        )
        self.assertEqual(
            "b1afdb1dcbcad39dd27638ea699f132fe44ce6df",
            providers["nate_editorial"]["commit"],
        )

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

    def test_fail_closed_rules_block_premature_selectability_and_fake_verification(self):
        rules = self.load_json("orchestration.json")["fail_closed"]
        joined = "\n".join(rules)
        self.assertIn("Do not mark the Video Editor selectable", joined)
        self.assertIn("HyperFrames 0.8.40 provider", joined)
        self.assertIn("Do not use Interface Designer as an editorial fallback", joined)
        self.assertIn("Do not claim final media verification from composition source alone", joined)


if __name__ == "__main__":
    unittest.main()
