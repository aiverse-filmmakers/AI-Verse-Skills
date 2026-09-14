import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = (
    ROOT
    / "skills"
    / "imported"
    / "ai-verse"
    / "video-editor"
    / "specialists"
    / "nate"
    / "website-to-hyperframes"
)
REFS = BASE / "references"

EXPECTED_UNCHANGED_BLOBS = {
    REFS / "step-1-capture.md": "770326203c224e65ffb3785c38cd845940ca4b4a",
    REFS / "step-2-design.md": "f4fc65511273f30bb28760151501f2fb7cdccb19",
    REFS / "step-3-script.md": "2eca87a2e79d8fd35d76def228e5366ae33cfc3d",
}


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


class VideoEditorWebsiteWorkflowTests(unittest.TestCase):
    def test_all_seven_workflow_references_exist(self):
        expected = {
            "step-1-capture.md",
            "step-2-design.md",
            "step-3-script.md",
            "step-4-storyboard.md",
            "step-5-vo.md",
            "step-6-build.md",
            "step-7-validate.md",
            "techniques.md",
        }
        self.assertEqual(expected, {p.name for p in REFS.iterdir() if p.is_file()})

    def test_untouched_capture_design_and_script_methods_are_byte_identical_to_nate(self):
        for path, expected in EXPECTED_UNCHANGED_BLOBS.items():
            with self.subTest(path=path.name):
                self.assertEqual(expected, git_blob_sha(path))

    def test_orchestrator_preserves_the_seven_step_artifact_gates(self):
        skill = (BASE / "SKILL.md").read_text(encoding="utf-8")
        for heading in (
            "Step 1: Capture & Understand",
            "Step 2: Write DESIGN.md",
            "Step 3: Write SCRIPT",
            "Step 4: Write STORYBOARD",
            "Step 5: Generate VO + Map Timing",
            "Step 6: Build Compositions",
            "Step 7: Validate & Deliver",
        ):
            self.assertIn(heading, skill)
        self.assertIn("DESIGN.md", skill)
        self.assertIn("SCRIPT.md", skill)
        self.assertIn("STORYBOARD.md", skill)
        self.assertIn("transcript.json", skill)

    def test_storyboard_preserves_experience_first_and_asset_audit_method(self):
        text = (REFS / "step-4-storyboard.md").read_text(encoding="utf-8")
        self.assertIn("Each beat is a WORLD, not a layout.", text)
        self.assertIn("## Asset Audit", text)
        self.assertIn("### Animation choreography", text)
        self.assertIn("### Depth layers", text)
        self.assertIn("### SFX cues", text)

    def test_storyboard_does_not_depend_on_nates_old_bundled_hyperframes_tree(self):
        text = (REFS / "step-4-storyboard.md").read_text(encoding="utf-8")
        self.assertNotIn("skills/hyperframes/references/transitions/", text)
        self.assertIn("current canonical HyperFrames provider", text)

    def test_voice_timing_uses_current_provider_surfaces_and_real_audio_as_truth(self):
        text = (REFS / "step-5-vo.md").read_text(encoding="utf-8")
        self.assertIn("npx hyperframes tts", text)
        self.assertIn("npx hyperframes transcribe", text)
        self.assertIn(
            "actual generated narration and its normalized word timestamps are the source",
            text,
        )
        self.assertNotIn("mcp__elevenlabs__", text)
        self.assertNotIn("mcp__claude_ai_HeyGen__", text)

    def test_build_reference_uses_project_root_assets_and_current_runtime_contract(self):
        text = (REFS / "step-6-build.md").read_text(encoding="utf-8")
        self.assertNotIn("../assets/", text)
        self.assertNotIn("skills/hyperframes/references/transitions/", text)
        self.assertIn("assets/", text)
        self.assertIn("npx hyperframes lint", text)
        self.assertIn("npx hyperframes check", text)
        self.assertIn("Timeline readiness before registration", text)

    def test_delivery_reference_rejects_deprecated_validate_and_private_cli_fallback(self):
        text = (REFS / "step-7-validate.md").read_text(encoding="utf-8")
        self.assertNotIn("npx hyperframes validate", text)
        self.assertNotIn("packages/cli/src/cli.ts", text)
        self.assertIn("npx hyperframes lint", text)
        self.assertIn("npx hyperframes check", text)
        self.assertIn("npx hyperframes preview", text)
        self.assertIn("actual rendered", text.lower())

    def test_techniques_are_advisory_to_current_provider_contract(self):
        text = (REFS / "techniques.md").read_text(encoding="utf-8")
        self.assertNotIn("../assets/", text)
        self.assertIn("canonical HyperFrames 0.8.40 provider contract wins", text)
        self.assertIn("hyperframes lint", text)
        self.assertIn("hyperframes check", text)

    def test_provenance_records_website_specialist_and_no_ais_asset_reuse(self):
        source = json.loads(
            (
                ROOT
                / "skills"
                / "imported"
                / "ai-verse"
                / "video-editor"
                / "specialists"
                / "nate"
                / "SOURCE.json"
            ).read_text(encoding="utf-8")
        )
        self.assertIn("website-to-hyperframes", source["imported_specialists"])
        joined = "\n".join(source.get("excluded_assets", []))
        self.assertIn("AIS", joined)
        self.assertEqual(
            "b1afdb1dcbcad39dd27638ea699f132fe44ce6df",
            source["upstream"]["commit"],
        )


if __name__ == "__main__":
    unittest.main()
