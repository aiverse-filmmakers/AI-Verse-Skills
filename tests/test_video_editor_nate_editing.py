import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "skills" / "imported" / "ai-verse" / "video-editor" / "specialists" / "nate"
FIXTURES = ROOT / "tests" / "fixtures" / "video-editor"

SILENCE = BASE / "cut-silences" / "scripts" / "cut-silences.mjs"
FIND = BASE / "cut-mistakes" / "scripts" / "find-cut-candidates.mjs"
APPLY = BASE / "cut-mistakes" / "scripts" / "apply-cuts.mjs"
REVIEW = BASE / "cut-mistakes" / "scripts" / "build-edl-review.mjs"

EXPECTED_GIT_BLOBS = {
    SILENCE: "fd34ec6a7e808ae038d9f080b8aeece8e206fb37",
    FIND: "ddc124283d901b83909f1bff4431cbab17feadcf",
    APPLY: "62973c4e8603613879ecd0962041b55d2655c18b",
    REVIEW: "ae9892c146c111ee6a93e12f2d4bca4235336abd",
}


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


class NateEditingPreservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which("node")
        if cls.node is None:
            raise unittest.SkipTest("Node.js is required for Nate editing behavior tests")

    def run_node(self, script: Path, *args: str):
        return subprocess.run(
            [self.node, str(script), *map(str, args)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def scratch(self):
        return tempfile.TemporaryDirectory(prefix="aiverse-video-editor-")

    def test_pinned_nate_executable_blobs_remain_byte_identical(self):
        for path, expected in EXPECTED_GIT_BLOBS.items():
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())
                self.assertEqual(expected, git_blob_sha(path))

    def test_silence_edit_preserves_words_and_retimes_monotonically(self):
        with self.scratch() as td:
            result = self.run_node(
                SILENCE,
                FIXTURES / "nate-source.json",
                "--out-dir",
                td,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            doc = json.loads((Path(td) / "nate-source.silence-transcript.json").read_text())
            self.assertEqual(
                "We we build a small garden. Plants need light.",
                " ".join(word["text"] for word in doc["words"]),
            )
            self.assertGreater(doc["audio_duration_secs"], 3)
            self.assertLess(doc["audio_duration_secs"], 6)
            previous_end = None
            for word in doc["words"]:
                self.assertGreater(word["end"], word["start"])
                if previous_end is not None:
                    self.assertGreaterEqual(word["start"], previous_end)
                previous_end = word["end"]

    def test_reviewed_stutter_cut_matches_nate_baseline(self):
        with self.scratch() as td:
            result = self.run_node(
                APPLY,
                FIXTURES / "nate-source.json",
                "--cuts",
                FIXTURES / "nate-approved-cuts.json",
                "--out-dir",
                td,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            doc = json.loads((Path(td) / "nate-source.mistakes-transcript.json").read_text())
            self.assertEqual(7.71, doc["audio_duration_secs"])
            self.assertEqual("we", doc["words"][0]["text"])
            self.assertEqual(0.61, doc["words"][0]["start"])
            self.assertEqual("light.", doc["words"][-1]["text"])

    def test_zero_mistake_review_is_valid_identity_edit(self):
        with self.scratch() as td:
            cuts = Path(td) / "cuts.json"
            cuts.write_text('{"cuts":[]}', encoding="utf-8")
            result = self.run_node(
                APPLY,
                FIXTURES / "nate-source.json",
                "--cuts",
                cuts,
                "--out-dir",
                td,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            doc = json.loads((Path(td) / "nate-source.mistakes-transcript.json").read_text())
            self.assertEqual(8, doc["audio_duration_secs"])
            self.assertEqual(9, len(doc["words"]))
            self.assertEqual(0.6, doc["words"][0]["start"])

    def test_out_of_source_cut_fails_closed(self):
        with self.scratch() as td:
            cuts = Path(td) / "cuts.json"
            cuts.write_text('{"cuts":[{"start":-1,"end":9}]}', encoding="utf-8")
            result = self.run_node(
                APPLY,
                FIXTURES / "nate-source.json",
                "--cuts",
                cuts,
                "--out-dir",
                td,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertRegex(result.stderr.lower(), r"range|duration|bounds")

    def test_candidate_detector_produces_reviewable_output_without_applying_cuts(self):
        with self.scratch() as td:
            result = self.run_node(
                FIND,
                FIXTURES / "nate-source.json",
                "--out-dir",
                td,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            summary = json.loads(result.stdout)
            self.assertIn("candidates", summary)
            self.assertTrue((Path(td) / "nate-source.cut-candidates.json").is_file())
            doc = json.loads((Path(td) / "nate-source.cut-candidates.json").read_text())
            self.assertEqual("cut-mistakes", doc["agent"])
            self.assertIsInstance(doc["candidates"], list)

    def test_review_helper_is_preserved_as_package_local_script(self):
        self.assertTrue(REVIEW.is_file())
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn("Build a self-contained review page", text)
        self.assertIn("delete_ranges", text)


if __name__ == "__main__":
    unittest.main()
