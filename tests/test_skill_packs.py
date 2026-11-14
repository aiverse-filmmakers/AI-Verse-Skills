"""Skill packs combine in one step and each skill is installed once."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CLI = Path(__file__).resolve().parents[1] / "installer" / "aiverse_skills.py"


def cli(root, cache, *args):
    return subprocess.run([sys.executable, str(CLI), "--root", str(root), "--cache", str(cache), *args],
                          capture_output=True, text=True, check=True).stdout


def ids(root):
    active = json.loads((root / ".aiverse" / "active.json").read_text())
    gen = active.get("generation_id") or active.get("generation")
    manifest = json.loads((root / ".aiverse" / "generations" / gen / ".aiverse" / "installed.json").read_text())
    return manifest["profile"], {p["id"] for p in manifest["packages"]}


class SkillPackTests(unittest.TestCase):
    def test_add_a_pack_in_one_step(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, cache = Path(tmp) / "skills", Path(tmp) / "cache"
            cli(root, cache, "install", "--profile", "universal", "--offline")
            profile, before = ids(root)
            self.assertEqual(profile, "universal")
            self.assertNotIn("copywriting", before)
            cli(root, cache, "update", "--add-pack", "marketing", "--offline")
            profile, after = ids(root)
            self.assertEqual(profile, "universal+marketing")
            self.assertIn("copywriting", after)
            self.assertTrue(before <= after, "nothing already installed is removed")
            cli(root, cache, "update", "--add-pack", "marketing", "--offline")
            self.assertEqual(ids(root)[0], "universal+marketing", "adding the same pack twice changes nothing")

    def test_unknown_pack_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(CLI), "--root", str(Path(tmp) / "s"), "--cache", str(Path(tmp) / "c"),
                                     "install", "--profile", "universal+nope", "--offline"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("nope", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
