import json
import unittest
from pathlib import Path

from installer.admission import scan_package


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "imported" / "ai-verse" / "cinematic-realism-director"


class CinematicRealismDirectorSecurityTests(unittest.TestCase):
    def test_first_party_package_passes_deterministic_admission_scan(self):
        report = scan_package(PACKAGE)
        self.assertEqual(
            report["status"],
            "pass",
            json.dumps(report.get("findings", []), indent=2, sort_keys=True),
        )
        self.assertGreater(report["files_scanned"], 20)
        self.assertEqual(report["findings"], [])


if __name__ == "__main__":
    unittest.main()
