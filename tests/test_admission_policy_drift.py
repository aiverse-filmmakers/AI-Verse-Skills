"""An older immutable generation must stay usable after the catalogue policy changes."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from installer import admission


def package(**changes):
    base = {"id": "business-pulse", "ownership": "upstream", "protected": False,
            "license": "fetched", "redistribution": "fetch-only", "integrity": {"sha256": "a" * 64},
            "security": {"status": "clean"}, "admission": "admitted", "trust": "pinned",
            "trusted": True, "readiness": "not-evaluated", "authorized": False}
    base.update(changes)
    return base


class AdmissionPolicyDriftTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / ".aiverse").mkdir()
        (self.root / ".aiverse" / "installed.json").write_text(json.dumps({"generation_id": "gen-old"}))
        self.stored = {"schema_version": admission.ADMISSION_SCHEMA_VERSION, "generation_id": "gen-old",
                       "packages": [package()]}
        (self.root / ".aiverse" / admission.ADMISSION_FILENAME).write_text(json.dumps(self.stored))

    def verify(self, now):
        current = copy.deepcopy(self.stored); current["packages"] = [now]
        with mock.patch.object(admission, "build_admission_report", return_value=current):
            return admission.verify_admission_generation(object(), self.root, "gen-old")

    def test_newer_licence_classification_keeps_the_old_generation_usable(self):
        self.assertEqual(self.verify(package(ownership="owned", license="Apache-2.0", redistribution="vendored",
                                             trust="owned")), [])

    def test_changed_bytes_or_security_still_fail(self):
        self.assertTrue(self.verify(package(integrity={"sha256": "b" * 64})))
        self.assertTrue(self.verify(package(security={"status": "flagged"})))

    def test_protection_and_block_decisions_stay_bound(self):
        self.assertTrue(self.verify(package(protected=True)))
        self.assertTrue(self.verify(package(admission="blocked")))


if __name__ == "__main__":
    unittest.main()
