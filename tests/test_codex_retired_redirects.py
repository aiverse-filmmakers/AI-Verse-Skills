"""Codex only matches exact skill names, so retired names get a tiny redirect skill in Codex folders."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CLI = Path(__file__).resolve().parents[1] / "installer" / "aiverse_skills.py"


def cli(root, *args, check=True):
    return subprocess.run([sys.executable, str(CLI), "--root", str(root), *args], capture_output=True, text=True, check=check)


class RetiredRedirectTests(unittest.TestCase):
    def test_codex_gets_redirects_claude_does_not_and_they_stay_tidy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, codex, claude = Path(tmp) / "skills", Path(tmp) / "codex", Path(tmp) / "claude"
            cli(root, "--cache", str(Path(tmp) / "cache"), "install", "--profile", "universal", "--offline")
            cli(root, "adapt", "--runtime", "codex", "--target", str(codex), "--sync")
            cli(root, "adapt", "--runtime", "claude", "--target", str(claude), "--sync")
            stub = (codex / "meeting-action-items" / "SKILL.md").read_text()
            self.assertIn("Use the action-items skill instead", stub)
            self.assertTrue((codex / "document-to-action-items" / "SKILL.md").is_file())
            self.assertFalse((codex / "produce-ai-video").exists(), "no redirect when the replacement is not installed")
            self.assertFalse((claude / "meeting-action-items").exists(), "Claude follows old names by itself")
            manifest = json.loads((codex / ".aiverse-adapter.json").read_text())
            self.assertEqual(sorted(manifest["redirects"]), ["document-to-action-items", "meeting-action-items"])
            self.assertEqual(cli(root, "adapter-verify", "--target", str(codex), "--complete", check=False).returncode, 0)
            cli(root, "adapt", "--runtime", "codex", "--target", str(codex), "--sync")
            self.assertTrue((codex / "meeting-action-items" / "SKILL.md").is_file(), "a second run keeps its own redirects")

    def test_a_folder_the_member_made_with_a_retired_name_is_left_alone(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, codex = Path(tmp) / "skills", Path(tmp) / "codex"
            cli(root, "--cache", str(Path(tmp) / "cache"), "install", "--profile", "universal", "--offline")
            mine = codex / "meeting-action-items"
            mine.mkdir(parents=True)
            (mine / "SKILL.md").write_text("my own skill")
            cli(root, "adapt", "--runtime", "codex", "--target", str(codex), "--sync")
            self.assertEqual((mine / "SKILL.md").read_text(), "my own skill")


if __name__ == "__main__":
    unittest.main()
