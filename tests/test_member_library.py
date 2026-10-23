"""Public owner behavior for private shared member procedures."""
import json
import os
import subprocess
import sys
import time
from unittest import mock
import tempfile
import unittest
from pathlib import Path

from installer import member_library as library


PORTABLE = {"reusable": True, "contains_workspace_data": False,
            "contains_credentials": False, "has_workspace_dependencies": False}


class MemberLibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "personal"
        self.package = self.base / "workspace-a" / "scraper"
        self.package.mkdir(parents=True)
        (self.package / "SKILL.md").write_text(
            '---\nname: youtube-scraper\ndescription: "Retrieve public video information."\n---\n\nUse explicit channel inputs.\n', encoding="utf-8")
        (self.package / "helper.txt").write_text("portable helper\n", encoding="utf-8")

    def plan(self, **kwargs):
        return library.plan_import(self.root, self.package, admission=PORTABLE,
                                   source_scope="workspace:alpha", **kwargs)

    def test_preview_is_read_only_and_apply_preserves_source(self):
        plan = self.plan()
        self.assertFalse(self.root.exists())
        result = library.apply_import(self.root, self.package, plan=plan,
                                      admission=PORTABLE, source_scope="workspace:alpha")
        self.assertEqual(result["state"], "imported")
        record = library.read_index(self.root)["skills"][result["id"]]
        self.assertEqual(record["visibility"], "shared")
        self.assertTrue((self.package / "SKILL.md").is_file())
        self.assertEqual(library.verify(self.root)["errors"], [])

    def test_two_same_names_have_different_stable_ids(self):
        first = library.apply_import(self.root, self.package, plan=self.plan(),
                                    admission=PORTABLE, source_scope="workspace:alpha")
        second = library.apply_import(self.root, self.package, plan=self.plan(),
                                     admission=PORTABLE, source_scope="workspace:alpha")
        self.assertNotEqual(first["id"], second["id"])
        records = library.read_index(self.root)["skills"]
        self.assertEqual(len(records), 2)
        self.assertEqual({x["name"] for x in records.values()}, {"youtube-scraper"})

    def test_retry_same_plan_is_idempotent(self):
        plan = self.plan()
        first = library.apply_import(self.root, self.package, plan=plan,
                                    admission=PORTABLE, source_scope="workspace:alpha")
        again = library.apply_import(self.root, self.package, plan=plan,
                                    admission=PORTABLE, source_scope="workspace:alpha")
        self.assertEqual(first["id"], again["id"])
        self.assertEqual(again["state"], "already-imported")

    def test_changed_source_or_index_refuses_stale_plan(self):
        plan = self.plan()
        (self.package / "helper.txt").write_text("changed\n", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "source changed"):
            library.apply_import(self.root, self.package, plan=plan,
                                 admission=PORTABLE, source_scope="workspace:alpha")
        plan = self.plan()
        another = self.plan()
        library.apply_import(self.root, self.package, plan=another,
                             admission=PORTABLE, source_scope="workspace:alpha")
        with self.assertRaisesRegex(RuntimeError, "library changed"):
            library.apply_import(self.root, self.package, plan=plan,
                                 admission=PORTABLE, source_scope="workspace:alpha")

    def test_private_package_is_not_silently_shared(self):
        with self.assertRaisesRegex(RuntimeError, "portability"):
            library.plan_import(self.root, self.package, admission={}, source_scope="workspace:alpha")
        plan = library.plan_import(self.root, self.package, admission={},
                                   source_scope="workspace:alpha", visibility="workspace:alpha")
        result = library.apply_import(self.root, self.package, plan=plan, admission={},
                                      source_scope="workspace:alpha", visibility="workspace:alpha")
        self.assertEqual(library.read_index(self.root)["skills"][result["id"]]["visibility"], "workspace:alpha")

    def test_security_findings_and_symlinks_refuse(self):
        (self.package / "helper.txt").write_text("-----BEGIN PRIVATE KEY-----\n", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "admission"):
            self.plan()
        (self.package / "helper.txt").write_text("okay\n", encoding="utf-8")
        try:
            (self.package / "linked").symlink_to(self.base / "elsewhere")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            self.plan()

    def test_immutable_versions_and_revision_selection(self):
        first = library.apply_import(self.root, self.package, plan=self.plan(),
                                    admission=PORTABLE, source_scope="workspace:alpha")
        old_revision = first["revision"]
        (self.package / "helper.txt").write_text("version two\n", encoding="utf-8")
        plan = self.plan(skill_id=first["id"])
        second = library.apply_import(self.root, self.package, plan=plan,
                                     admission=PORTABLE, source_scope="workspace:alpha")
        self.assertEqual(first["id"], second["id"])
        self.assertNotEqual(old_revision, second["revision"])
        restored = library.select_revision(self.root, first["id"], old_revision,
                                            expected_index=library.index_digest(self.root))
        self.assertEqual(restored["revision"], old_revision)
        self.assertEqual(library.verify(self.root)["errors"], [])

    def test_redirected_package_parent_receives_no_writes(self):
        plan = self.plan()
        metadata = self.root / library.RELATIVE
        metadata.mkdir(parents=True)
        outside = self.base / "outside"
        outside.mkdir()
        try:
            (metadata / "packages").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        with self.assertRaisesRegex(RuntimeError, "redirected"):
            library.apply_import(self.root, self.package, plan=plan,
                                 admission=PORTABLE, source_scope="workspace:alpha")
        self.assertEqual(list(outside.iterdir()), [])

    def test_invalid_index_fails_closed(self):
        metadata = self.root / library.RELATIVE
        metadata.mkdir(parents=True)
        (metadata / "index.json").write_text('{"contract": "unknown"}', encoding="utf-8")
        self.assertFalse(library.verify(self.root)["ok"])
        with self.assertRaisesRegex(RuntimeError, "index"):
            self.plan()

    def apply(self, plan=None, **kwargs):
        return library.apply_import(self.root, self.package, plan=plan or self.plan(),
                                    admission=PORTABLE, source_scope="workspace:alpha", **kwargs)

    def test_interrupted_index_commit_leaves_no_active_package_and_retry_recovers(self):
        plan = self.plan()
        with mock.patch.object(library, "_write", side_effect=OSError("interrupted commit")):
            with self.assertRaises(OSError):
                self.apply(plan)
        self.assertEqual(library.read_index(self.root)["skills"], {})
        self.assertTrue(library.revision_path(self.root, plan["id"], plan["source_revision"]).is_dir())
        result = self.apply(plan)
        self.assertEqual(result["state"], "imported")
        self.assertEqual(library.read_index(self.root)["sequence"], 1)

    def test_retry_does_not_hide_corruption(self):
        plan = self.plan()
        result = self.apply(plan)
        target = library.revision_path(self.root, result["id"], result["revision"])
        (target / "helper.txt").write_text("damaged", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "integrity"):
            self.apply(plan)
        self.assertFalse(library.verify(self.root)["ok"])

    def test_live_lock_blocks_without_changes_and_owner_dead_stale_lock_recovers(self):
        from installer import generation_lifecycle as lifecycle
        plan = self.plan()
        metadata = self.root / library.RELATIVE
        metadata.mkdir(parents=True)
        with lifecycle.lifecycle_lock(metadata / "writer"):
            with self.assertRaisesRegex(RuntimeError, "busy"):
                self.apply(plan)
        lock = metadata / ".writer.lifecycle.lock"
        lock.write_text(json.dumps({"token": "stale-fixture", "pid": 987654321}), encoding="utf-8")
        old = time.time() - lifecycle.LOCK_STALE_SECONDS - 10
        os.utime(lock, (old, old))
        with mock.patch.object(lifecycle, "_process_is_alive", return_value=False):
            self.assertEqual(self.apply(plan)["state"], "imported")

    def test_unknown_lock_never_reclaimed(self):
        plan = self.plan()
        metadata = self.root / library.RELATIVE
        metadata.mkdir(parents=True)
        (metadata / ".writer.lifecycle.lock").write_text("not a lock record", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "busy"):
            self.apply(plan)
        self.assertEqual(library.read_index(self.root)["sequence"], 0)

    def test_provenance_is_bound_preserved_and_does_not_execute(self):
        marker = self.base / "must-not-exist"
        (self.package / "run.py").write_text("raise RuntimeError('never execute imports')", encoding="utf-8")
        (self.package / "LICENSE").write_text("Fixture license", encoding="utf-8")
        provenance = {"origin": "external fixture", "license": "see LICENSE",
                      "dependencies": ["not-installed-fixture"],
                      "requested_capabilities": ["network-read"],
                      "requires_connection": True, "requires_credential": False}
        plan = self.plan(provenance=provenance)
        with self.assertRaisesRegex(RuntimeError, "differ"):
            self.apply(plan)
        result = self.apply(plan, provenance=provenance)
        record = library.read_index(self.root)["skills"][result["id"]]
        self.assertEqual(record["revisions"][result["revision"]]["provenance"], provenance)
        self.assertTrue((self.package / "LICENSE").exists())
        self.assertFalse(marker.exists())
        self.assertTrue((self.package / "run.py").exists())

    def test_partial_copy_failure_preserves_source_and_allows_retry(self):
        plan = self.plan()
        before = {p.relative_to(self.package).as_posix(): p.read_bytes()
                  for p in self.package.rglob("*") if p.is_file()}
        def interrupted_copy(source, stage, **kwargs):
            (stage / "partial.txt").write_text("partial", encoding="utf-8")
            raise OSError("copy interrupted")
        with mock.patch.object(library.shutil, "copytree", side_effect=interrupted_copy):
            with self.assertRaises(OSError):
                self.apply(plan)
        self.assertEqual(library.read_index(self.root)["skills"], {})
        self.assertEqual(before, {p.relative_to(self.package).as_posix(): p.read_bytes()
                                 for p in self.package.rglob("*") if p.is_file()})
        self.assertEqual(list((self.root / library.RELATIVE).rglob(".stage-*")), [])
        self.assertEqual(self.apply(plan)["state"], "imported")

    def test_resource_limits_refuse_before_library_creation(self):
        (self.package / "oversize.dat").write_bytes(b"x" * 1_048_577)
        with self.assertRaisesRegex(RuntimeError, "resource limits"):
            self.plan()
        self.assertFalse(self.root.exists())

    def test_invalid_admission_and_forged_preview_refuse(self):
        with self.assertRaises(RuntimeError):
            library.plan_import(self.root, self.package, admission={**PORTABLE, "reusable": 1})
        plan = self.plan()
        plan["unrecognized"] = True
        with self.assertRaisesRegex(RuntimeError, "fields"):
            self.apply(plan)
        with self.assertRaisesRegex(RuntimeError, "credentials"):
            library.plan_import(self.root, self.package, admission={"contains_credentials": True},
                                source_scope="workspace:alpha", visibility="workspace:alpha")

    def test_managed_root_is_not_writable_member_library(self):
        metadata = self.root / ".aiverse"
        metadata.mkdir(parents=True)
        (metadata / "active.json").write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "managed Skills"):
            self.plan()
        self.assertFalse((metadata / "member-library").exists())

    def test_dangling_index_symlink_and_duplicate_json_refuse(self):
        metadata = self.root / library.RELATIVE
        metadata.mkdir(parents=True)
        file = metadata / "index.json"
        try:
            file.symlink_to(self.base / "missing")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        self.assertFalse(library.verify(self.root)["ok"])
        file.unlink()
        file.write_text('{"contract":"a","contract":"b"}', encoding="utf-8")
        self.assertFalse(library.verify(self.root)["ok"])

    def test_same_revision_selection_is_noop_and_stale_selection_refuses(self):
        result = self.apply()
        before = library.index_digest(self.root)
        selected = library.select_revision(self.root, result["id"], result["revision"], expected_index=before)
        self.assertEqual(selected["state"], "already-selected")
        self.assertEqual(before, library.index_digest(self.root))
        with self.assertRaisesRegex(RuntimeError, "changed"):
            library.select_revision(self.root, result["id"], result["revision"], expected_index="0" * 64)

    def cli(self, *args):
        environment = dict(os.environ)
        for key in ("AI_VERSE_SKILLS_ROOT", "AI_VERSE_LOCAL_SKILLS_ROOT", "PYTHONPATH"):
            environment.pop(key, None)
        return subprocess.run([sys.executable, "installer/aiverse_skills.py", "library", *args],
                              cwd=Path(__file__).resolve().parents[1], env=environment,
                              capture_output=True, text=True, timeout=30)

    def test_public_cli_preview_apply_list_doctor_and_explicit_root(self):
        args = ["--library-root", str(self.root)]
        admission = self.base / "admission.json"
        admission.write_text(json.dumps(PORTABLE), encoding="utf-8")
        request = ["import", "--source", str(self.package), "--admission-json", str(admission)]
        preview = self.cli(*args, *request)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse(self.root.exists())
        plan_file = self.base / "plan.json"
        plan_file.write_text(preview.stdout, encoding="utf-8")
        result = self.cli(*args, *request, "--apply-plan", str(plan_file))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["state"], "imported")
        listed = self.cli(*args, "list")
        self.assertEqual(len(json.loads(listed.stdout)["skills"]), 1)
        self.assertEqual(self.cli(*args, "doctor").returncode, 0)
        self.assertNotEqual(self.cli("list").returncode, 0)
        record = next(iter(library.read_index(self.root)["skills"].values()))
        (library.revision_path(self.root, record["id"], record["active_revision"]) / "helper.txt").write_text("damaged")
        failed = self.cli(*args, "doctor")
        self.assertEqual(failed.returncode, 2)
        self.assertFalse(json.loads(failed.stdout)["ok"])



if __name__ == "__main__":
    unittest.main()
