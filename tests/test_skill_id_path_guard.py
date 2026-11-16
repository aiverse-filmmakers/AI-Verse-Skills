"""FL-02: a skill id must never be able to point outside the folder it is meant to live in."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "installer"))
import aiverse_skills_v3 as core  # noqa: E402
import learning  # noqa: E402

BAD_IDS = ["", ".", "..", "../x", "a/b", "a\\b", "/etc", "/tmp/x", "a\x00b", "../..", " ", "-x"]
GOOD_IDS = ["action-items", "ExtractWisdom", "ai-video-director", "a", "x.y_z-1"]


class SafeIdTests(unittest.TestCase):
    def test_bad_ids_refused(self):
        for bad in BAD_IDS:
            with self.subTest(bad=bad), self.assertRaises(RuntimeError):
                core.safe_skill_id(bad)
        with self.assertRaises(RuntimeError):
            core.safe_skill_id(None)

    def test_real_ids_accepted(self):
        for good in GOOD_IDS:
            self.assertEqual(core.safe_skill_id(good), good)

    def test_every_registry_id_accepted(self):
        reg = Path(__file__).resolve().parents[1] / "registry" / "packages.json"
        if not reg.is_file():
            self.skipTest("no registry")
        ids = []

        def walk(o):
            if isinstance(o, dict):
                if isinstance(o.get("id"), str):
                    ids.append(o["id"])
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(json.loads(reg.read_text()))
        self.assertTrue(ids)
        for i in ids:
            core.safe_skill_id(i)

    def test_confined_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "chat"
            folder.mkdir()
            for bad in BAD_IDS:
                with self.subTest(bad=bad), self.assertRaises(RuntimeError):
                    core.confined_entry(folder, bad)
            self.assertEqual(core.confined_entry(folder, "action-items"), folder / "action-items")


class UninstallTraversalTests(unittest.TestCase):
    def _setup(self, tmp, ids):
        outside = Path(tmp) / "above"
        chat = outside / "skills"
        chat.mkdir(parents=True)
        (outside / "precious.txt").write_text("keep")
        (chat / "mine").mkdir()
        (chat / "mine" / "SKILL.md").write_text("mine")
        (chat / ".aiverse-adapter.json").write_text(json.dumps({"packages": [{"id": i} for i in ids], "redirects": ids}))
        (chat / ".aiverse-adapter-pending.json").write_text(json.dumps({"ids": ids}))
        return outside, chat

    def test_unexpose_never_deletes_above_the_chat_folder(self):
        for bad in ["..", "../x", "a/b", "/", ""]:
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as tmp:
                outside, chat = self._setup(tmp, [bad, "real-skill"])
                (chat / "real-skill").mkdir()
                root = Path(tmp) / "root"
                root.mkdir()
                orig = core.load_chat_folders
                core.load_chat_folders = lambda r, c=chat: {"claude": str(c)}
                try:
                    core.unexpose_chat_folders(root)
                finally:
                    core.load_chat_folders = orig
                self.assertTrue((outside / "precious.txt").is_file())
                self.assertTrue((chat / "mine" / "SKILL.md").is_file())
                self.assertFalse((chat / "real-skill").exists(), "a real listed skill is still removed")

    def test_previous_adapter_ids_drops_unsafe(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, chat = self._setup(tmp, ["..", "a/b", "ok-id"])
            self.assertEqual(core._previous_adapter_ids(chat), {"ok-id"})

    def test_write_redirect_refuses_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "t"
            target.mkdir()
            with self.assertRaises(RuntimeError):
                core._write_redirect(target, "..", "new")
            with self.assertRaises(RuntimeError):
                core._write_redirect(target, "../x", "new")
            self.assertFalse((Path(tmp) / "x").exists())


class LearningPathTests(unittest.TestCase):
    def test_archive_record_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            for bad in ["..", "../..", "../x", "a/b", "/etc", ""]:
                with self.subTest(bad=bad), self.assertRaises(RuntimeError):
                    learning._archive_record_path(root, bad)
            p = learning._archive_record_path(root, "action-items")
            self.assertEqual(p.name, "archive.json")
            self.assertEqual(p.parent.name, "action-items")

    def test_restore_archive_record_usage_refuse_bad_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            for bad in ["..", "../x", "a/b", "/etc/passwd"]:
                with self.subTest(bad=bad):
                    with self.assertRaises(RuntimeError):
                        learning.restore_archived(object(), root, bad)
                    with self.assertRaises(RuntimeError):
                        learning.archive_skill(object(), root, bad, approved_by="t")
                    with self.assertRaises(RuntimeError):
                        learning.record_usage(object(), root, bad, success=True)


if __name__ == "__main__":
    unittest.main()
