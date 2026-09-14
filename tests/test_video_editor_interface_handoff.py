import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VE = ROOT / "skills" / "imported" / "ai-verse" / "video-editor"
ID = ROOT / "skills" / "imported" / "ai-verse" / "interface-designer"

EXPECTED_MODES = {
    "VISUAL_DIRECTION",
    "REFERENCE_RECREATION",
    "PROTOTYPE_VISUAL_DIRECTIONS",
    "MOTION_TASTE",
}


class VideoEditorInterfaceHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(
            (VE / "references" / "interface-designer-handoff.json").read_text(encoding="utf-8")
        )
        cls.video_graph = json.loads(
            (VE / "references" / "orchestration.json").read_text(encoding="utf-8")
        )
        cls.interface_graph = json.loads(
            (ID / "references" / "orchestration.json").read_text(encoding="utf-8")
        )
        cls.registry = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))

    def test_exactly_four_visual_handoff_modes_exist(self):
        self.assertEqual(EXPECTED_MODES, set(self.contract["modes"]))
        self.assertEqual("presentation-only", self.contract["boundary"])
        self.assertEqual(
            "video-editor -> interface-designer -> video-editor",
            self.contract["direction"],
        )

    def test_orchestration_stage_points_to_the_canonical_handoff_contract(self):
        stage = next(
            s for s in self.video_graph["stages"] if s["id"] == "interface_design_handoff"
        )
        self.assertEqual(["interface-designer"], stage["capabilities"])
        self.assertEqual("presentation-only", stage["boundary"])
        self.assertEqual(
            "references/interface-designer-handoff.json",
            stage["contract"],
        )
        self.assertEqual(EXPECTED_MODES, set(stage["handoff_modes"]))
        self.assertEqual("video-editor", stage["return_authority"])

    def test_interface_designer_and_video_editor_agree_on_registered_boundary(self):
        registered = {x["id"] for x in self.registry["employee"]}
        self.assertIn("video-editor", registered)
        self.assertIn("interface-designer", registered)

        integration = self.interface_graph["registered_integrations"]["video-editor"]
        self.assertEqual("registered", integration["status"])
        self.assertEqual("interface-designer -> video-editor", integration["direction"])
        self.assertEqual("presentation-handoff-only", integration["boundary"])

        does_not_own = set(integration["does_not_own"])
        for boundary in (
            "transcript truth",
            "EDLs",
            "editorial cuts",
            "source-time mapping",
            "HyperFrames runtime correctness",
            "final media acceptance",
        ):
            self.assertIn(boundary, does_not_own)

    def test_global_boundary_keeps_all_editorial_and_runtime_authority_in_video_editor(self):
        forbidden = set(self.contract["always_forbidden"])
        expected = {
            "transcript truth ownership",
            "EDL ownership",
            "silence or mistake-cut authority",
            "hook/open-loop/payoff editorial authority",
            "source-time mapping ownership",
            "audio/video synchronization authority",
            "HyperFrames runtime correctness ownership",
            "final media acceptance",
        }
        self.assertEqual(expected, forbidden)

    def test_visual_direction_cannot_mutate_edit_truth(self):
        mode = self.contract["modes"]["VISUAL_DIRECTION"]
        joined = "\n".join(mode["forbidden"])
        self.assertIn("transcript truth", joined)
        self.assertIn("EDL", joined)
        self.assertIn("source-time mapping", joined)
        self.assertIn("final media acceptance", joined)

    def test_reference_recreation_cannot_invent_audio_or_replace_pacing_analysis(self):
        mode = self.contract["modes"]["REFERENCE_RECREATION"]
        joined = "\n".join(mode["forbidden"])
        self.assertIn("audio-reference facts from silent frames", joined)
        self.assertIn("replace Video Editor pacing/timing analysis", joined)
        self.assertIn("change transcript/EDL/source-time truth", joined)
        self.assertIn("fabricate unavailable brand assets", joined)

    def test_prototype_handoff_is_bounded_and_not_mandatory_ceremony(self):
        mode = self.contract["modes"]["PROTOTYPE_VISUAL_DIRECTIONS"]
        request = "\n".join(mode["request"]["include"])
        forbidden = "\n".join(mode["forbidden"])
        self.assertIn("one bounded beat or representative frame/section", request)
        self.assertIn("prototype every ordinary lower third", forbidden)
        self.assertIn("change spoken meaning or edit order", forbidden)
        self.assertIn("force a framework migration", forbidden)

    def test_motion_taste_cannot_override_editorial_timing_or_hyperframes(self):
        mode = self.contract["modes"]["MOTION_TASTE"]
        request = "\n".join(mode["request"]["include"])
        forbidden = "\n".join(mode["forbidden"])
        self.assertIn("locked beat duration", request)
        self.assertIn("spoken/transcript anchors", request)
        self.assertIn("override HyperFrames timing or adapter rules", forbidden)
        self.assertIn("change EDL/source-time mapping", forbidden)
        self.assertIn("claim encoded A/V verification", forbidden)

    def test_narrow_nonvisual_operations_never_route_to_interface_designer(self):
        for scope in ("SILENCE_ONLY", "MISTAKE_RETAKE_ONLY", "CAPTIONS_ONLY"):
            with self.subTest(scope=scope):
                self.assertNotIn(
                    "interface_design_handoff",
                    self.video_graph["scope_pipelines"][scope],
                )

    def test_visual_video_workflows_may_route_to_interface_designer_before_hyperframes(self):
        for scope in (
            "MOTION_GRAPHICS_ONLY",
            "SHORT_FORM_EDIT",
            "LONG_FORM_TALKING_HEAD",
            "WEBSITE_PROMO",
            "REFERENCE_LED_EDIT",
            "FULL_EDIT",
        ):
            with self.subTest(scope=scope):
                pipeline = self.video_graph["scope_pipelines"][scope]
                self.assertIn("interface_design_handoff", pipeline)
                self.assertLess(
                    pipeline.index("interface_design_handoff"),
                    pipeline.index("hyperframes_compose"),
                )

    def test_conflict_order_places_runtime_and_media_evidence_above_visual_advice(self):
        order = self.contract["conflict_order"]
        self.assertLess(
            order.index("canonical HyperFrames/runtime correctness"),
            order.index("Interface Designer visual recommendation"),
        )
        self.assertLess(
            order.index("encoded media QA evidence"),
            order.index("Interface Designer visual recommendation"),
        )
        self.assertLess(
            order.index("locked editorial decisions"),
            order.index("Interface Designer visual recommendation"),
        )


if __name__ == "__main__":
    unittest.main()
