import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "skills" / "imported" / "ai-verse" / "video-editor" / "specialists" / "nate"
SHORT = BASE / "short-form-edit"
STORY = BASE / "video-storytelling"
FIXTURE = ROOT / "tests" / "fixtures" / "video-editor" / "short-form"

VALIDATE_PLAN = SHORT / "scripts" / "validate-plan.mjs"
VALIDATE_FOOTAGE = SHORT / "scripts" / "validate-footage.mjs"
GEOM = STORY / "reference" / "patterns" / "wall-of-slots" / "geom.py"
WALL = STORY / "reference" / "patterns" / "wall-of-slots" / "wall.py"

EXPECTED_GIT_BLOBS = {
    VALIDATE_PLAN: "0860bdab829b363f5f5df1678756e9b63dc9a7ef",
    VALIDATE_FOOTAGE: "4d4be237d1dd7313ea9cc4c8daa57b64f82bfadf",
    GEOM: "d10e80765d1750e7709973695cd29cd1871fce8a",
    WALL: "ed7d28702a536e113b47210808e8e43d171300f8",
}


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


class VideoEditorShortFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which("node")
        if cls.node is None:
            raise unittest.SkipTest("Node.js is required for short-form validator tests")

    def workspace(self):
        temp = tempfile.TemporaryDirectory(prefix="aiverse-video-short-form-")
        root = Path(temp.name)
        assets = root / "assets"
        assets.mkdir(parents=True)
        for name in ("plan.json", "transcript.json", "edit-decisions.json"):
            shutil.copy2(FIXTURE / name, assets / name)
        return temp, root

    def run_validator(self, script: Path, workspace: Path):
        return subprocess.run(
            [self.node, str(script), str(workspace)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    @staticmethod
    def read_json(path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def write_json(path: Path, value):
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_upstream_validator_and_story_pattern_blobs_remain_byte_identical(self):
        for path, expected in EXPECTED_GIT_BLOBS.items():
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())
                self.assertEqual(expected, git_blob_sha(path))

    def test_pristine_nate_short_form_fixture_passes_plan_and_footage_validation(self):
        temp, root = self.workspace()
        with temp:
            plan = self.run_validator(VALIDATE_PLAN, root)
            footage = self.run_validator(VALIDATE_FOOTAGE, root)
            self.assertEqual(0, plan.returncode, plan.stderr or plan.stdout)
            self.assertEqual(0, footage.returncode, footage.stderr or footage.stdout)

    def test_caption_timing_drift_is_rejected(self):
        temp, root = self.workspace()
        with temp:
            plan_path = root / "assets" / "plan.json"
            plan = self.read_json(plan_path)
            plan["captions"][0]["words"][0]["start"] += 0.1
            self.write_json(plan_path, plan)

            result = self.run_validator(VALIDATE_PLAN, root)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("timing differs", (result.stdout + result.stderr).lower())

    def test_wrong_source_word_mapping_is_rejected(self):
        temp, root = self.workspace()
        with temp:
            transcript_path = root / "assets" / "transcript.json"
            transcript = self.read_json(transcript_path)
            transcript["words"][0]["sourceStart"] += 0.1
            self.write_json(transcript_path, transcript)

            result = self.run_validator(VALIDATE_PLAN, root)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("source mapping", (result.stdout + result.stderr).lower())

    def test_scene_gap_and_duplicate_scene_id_are_rejected(self):
        temp, root = self.workspace()
        with temp:
            plan_path = root / "assets" / "plan.json"
            plan = self.read_json(plan_path)
            plan["scenes"][1]["start"] += 0.1
            plan["scenes"][1]["id"] = plan["scenes"][0]["id"]
            self.write_json(plan_path, plan)

            result = self.run_validator(VALIDATE_PLAN, root)
            combined = result.stdout + result.stderr
            self.assertNotEqual(0, result.returncode)
            self.assertIn("gap or overlap", combined.lower())
            self.assertIn("duplicate scene", combined.lower())

    def test_broll_scene_without_footage_ledger_fails_closed(self):
        temp, root = self.workspace()
        with temp:
            plan_path = root / "assets" / "plan.json"
            plan = self.read_json(plan_path)
            plan["scenes"][1]["layout"] = "broll"
            plan["scenes"][1]["kind"] = "garden"
            self.write_json(plan_path, plan)

            result = self.run_validator(VALIDATE_FOOTAGE, root)
            self.assertNotEqual(0, result.returncode)

    def test_footage_ledger_hash_passes_then_detects_changed_asset(self):
        temp, root = self.workspace()
        with temp:
            assets = root / "assets"
            plan_path = assets / "plan.json"
            plan = self.read_json(plan_path)
            plan["scenes"][1]["layout"] = "broll"
            plan["scenes"][1]["kind"] = "garden"
            self.write_json(plan_path, plan)

            payload = b"synthetic footage hash fixture"
            media = assets / "garden.mp4"
            media.write_bytes(payload)
            ledger = [{
                "scene": "s01",
                "sourceSceneId": "garden-one",
                "asset": "assets/garden.mp4",
                "sha256": hashlib.sha256(payload).hexdigest(),
                "sourceStart": 0,
                "sourceEnd": 2,
            }]
            self.write_json(assets / "footage-ledger.json", ledger)

            accepted = self.run_validator(VALIDATE_FOOTAGE, root)
            self.assertEqual(0, accepted.returncode, accepted.stderr or accepted.stdout)

            media.write_bytes(b"changed")
            changed = self.run_validator(VALIDATE_FOOTAGE, root)
            self.assertNotEqual(0, changed.returncode)

    def test_storytelling_adaptation_uses_current_provider_gates(self):
        skill = (STORY / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("npx hyperframes lint", skill)
        self.assertIn("npx hyperframes check", skill)
        self.assertNotIn("Parallel workers make the video layer paint black", skill)
        self.assertIn("rendered nested video successfully with two workers", skill)


if __name__ == "__main__":
    unittest.main()
