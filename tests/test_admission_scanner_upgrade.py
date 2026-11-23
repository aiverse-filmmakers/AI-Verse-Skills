"""A stricter safety scanner must not break installs admitted by the older one (FL-26).

Installed generations store their safety scan result, and pin, doctor and
rollback compare it with a fresh scan. FL-26 made the scanner read more files,
so an unchanged package can now get new review findings. That must not stop a
member's existing install from working; only a new deny finding blocks it.
"""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from installer import admission

OLD_PASS = {"status": "pass", "files_scanned": 3, "text_bytes_scanned": 10, "findings": []}  # no scanner_version


def _package(security):
    return {"id": "pkg", "protected": True, "admission": "admitted",
            "integrity": {"status": "verified"}, "security": security, "authorized": False}


class ScannerUpgradeKeepsOldInstallsUsable(unittest.TestCase):
    def verify(self, stored_security, fresh_security):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".aiverse").mkdir()
            (root / ".aiverse" / "installed.json").write_text(json.dumps({"generation_id": "g1"}), encoding="utf-8")
            (root / ".aiverse" / admission.ADMISSION_FILENAME).write_text(json.dumps({
                "schema_version": admission.ADMISSION_SCHEMA_VERSION, "generation_id": "g1",
                "packages": [_package(stored_security)]}), encoding="utf-8")
            fresh = {"packages": [_package(fresh_security)]}
            with mock.patch.object(admission, "build_admission_report", lambda impl, r, m: fresh):
                return admission.verify_admission_generation(None, root, "g1")

    def fresh(self, status, findings=()):
        return {"status": status, "scanner_version": admission.SCANNER_VERSION,
                "files_scanned": 3, "text_bytes_scanned": 10, "findings": list(findings)}

    def test_old_pass_with_new_review_findings_stays_usable(self):
        review = self.fresh("review-required", [{"severity": "review", "code": "environment-harvest", "path": "x.mjs"}])
        self.assertEqual(self.verify(OLD_PASS, review), [])

    def test_old_pass_with_new_deny_finding_is_blocked(self):
        deny = self.fresh("deny", [{"severity": "deny", "code": "github-token", "path": "x.mjs"}])
        self.assertTrue(any("now denies" in e for e in self.verify(OLD_PASS, deny)))

    def test_same_scanner_version_is_still_strict(self):
        stored = self.fresh("pass")
        changed = self.fresh("review-required", [{"severity": "review", "code": "bidi-control", "path": "a.md"}])
        self.assertTrue(any("security scan result changed" in e for e in self.verify(stored, changed)))
        self.assertEqual(self.verify(stored, self.fresh("pass")), [])


if __name__ == "__main__":
    unittest.main()
