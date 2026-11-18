"""usage list shows every active skill with how often and when it was last used, most used first."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "installer" / "aiverse_skills.py"


def cli(root, *args):
    return subprocess.run([sys.executable, str(CLI), "--root", str(root), *args],
                          capture_output=True, text=True, check=True, encoding="utf-8").stdout


class UsageReportTests(unittest.TestCase):
    def test_counts_order_and_never_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "skills"
            cli(root, "--cache", str(Path(tmp) / "cache"), "install", "--profile", "universal", "--offline")
            cli(root, "setup", "--json")
            cli(root, "usage", "record", "weekly-review-planning", "--json")
            cli(root, "usage", "record", "action-items", "--json")
            cli(root, "usage", "record", "action-items", "--json")
            report = json.loads(cli(root, "usage", "list", "--json"))
            first, second = report["skills"][0], report["skills"][1]
            self.assertEqual((first["skill_id"], first["used"]), ("action-items", 2))
            self.assertEqual((second["skill_id"], second["used"]), ("weekly-review-planning", 1))
            self.assertTrue(first["last_used"])
            self.assertIn("change-review", report["never_used"])
            self.assertNotIn("action-items", report["never_used"])
            text = cli(root, "usage", "list")
            self.assertIn("action-items: used 2 times, last ", text)
            self.assertIn("change-review: never used", text)


if __name__ == "__main__":
    unittest.main()
