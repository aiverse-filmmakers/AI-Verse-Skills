"""Member skills imported before the stricter scan (FL-26) must keep working.

The member library re-scans stored revisions when it verifies them and when
learning deduplicates. FL-26 made the scan read .jsx, .mjs and other files it
used to skip, so an unchanged skill can now show new review findings. That must
not break the member's library; only a new deny finding blocks a stored skill.
New imports stay fully strict.
"""
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from installer import member_library as library

PORTABLE = {"reusable": True, "contains_workspace_data": False,
            "contains_credentials": False, "has_workspace_dependencies": False}


def old_scanner(source, max_text_bytes=0):
    # What the pre FL-26 scanner reported for this package: it never read app.mjs.
    return {"status": "pass", "files_scanned": 2, "text_bytes_scanned": 10, "findings": []}


class StoredMemberSkillsSurviveStricterScan(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.root = base / "personal"
        self.package = base / "workspace-a" / "fetcher"
        self.package.mkdir(parents=True)
        (self.package / "SKILL.md").write_text(
            '---\nname: fetcher\ndescription: "Fetch data with an API key."\n---\n\nRun app.mjs.\n', encoding="utf-8")

    def import_with_old_scanner(self):
        with mock.patch.object(library, "scan_package", old_scanner):
            plan = library.plan_import(self.root, self.package, admission=PORTABLE, source_scope="workspace:alpha")
            return library.apply_import(self.root, self.package, plan=plan, admission=PORTABLE,
                                        source_scope="workspace:alpha")

    def test_new_review_finding_does_not_break_a_stored_skill(self):
        (self.package / "app.mjs").write_text("const key = process.env.API_KEY;\n", encoding="utf-8")
        self.import_with_old_scanner()
        self.assertEqual(library.verify(self.root)["errors"], [])

    def test_new_deny_finding_still_blocks_a_stored_skill(self):
        (self.package / "app.mjs").write_text('const key = "ghp_' + "A" * 36 + '";\n', encoding="utf-8")
        self.import_with_old_scanner()
        self.assertNotEqual(library.verify(self.root)["errors"], [])

    def test_new_import_is_still_strict(self):
        (self.package / "app.mjs").write_text("const key = process.env.API_KEY;\n", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "requires review"):
            library.plan_import(self.root, self.package, admission=PORTABLE, source_scope="workspace:alpha")


if __name__ == "__main__":
    unittest.main()
