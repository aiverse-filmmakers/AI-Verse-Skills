"""FL-11: the one line installer must install the accepted release, not the newest main."""
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOT = ROOT / "bootstrap.sh"


def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], check=True, capture_output=True, text=True,
                          env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}, encoding="utf-8").stdout.strip()


class BootstrapAcceptedReleaseTests(unittest.TestCase):
    def test_script_reads_release_file_and_not_a_bare_main_checkout(self):
        text = BOOT.read_text(encoding="utf-8")
        self.assertIn("release/component-release.json", text)
        self.assertNotIn("checkout --quiet main", text)
        self.assertNotIn("pull --quiet --ff-only", text)
        self.assertIn("AI_VERSE_SKILLS_REF", text)

    def test_real_release_descriptor_is_accepted_and_well_formed(self):
        rel = json.loads((ROOT / "release" / "component-release.json").read_text(encoding="utf-8"))
        self.assertEqual(rel["release_status"], "accepted")
        self.assertRegex(rel["revision"], r"^[a-f0-9]{40}$")

    def _run(self, repo, home, **env):
        e = {**os.environ, "HOME": str(home), "AI_VERSE_SKILLS_REPO": str(repo),
             "AI_VERSE_SKILLS_HOME": str(home / "dest"), "AI_VERSE_BIN_DIR": str(home / "bin")}
        e.pop("AI_VERSE_SKILLS_REF", None)
        e.update(env)
        # Stop right after checkout: the fake repo has no installer, so the run ends there.
        return subprocess.run(["sh", str(BOOT)], capture_output=True, text=True, env=e, encoding="utf-8")

    def _fake_repo(self, tmp, acceptance_only_tip=False):
        repo = Path(tmp) / "origin"
        repo.mkdir()
        git(repo, "init", "-q", "-b", "main")
        (repo / "code.txt").write_text("accepted code", encoding="utf-8")
        (repo / "release").mkdir()
        (repo / "release" / "component-release.json").write_text("{}", encoding="utf-8")
        git(repo, "add", "-A")
        git(repo, "commit", "-q", "-m", "accepted code")
        accepted = git(repo, "rev-parse", "HEAD")
        (repo / "release" / "component-release.json").write_text(
            json.dumps({"release_status": "accepted", "revision": accepted}), encoding="utf-8")
        if acceptance_only_tip:
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "accept")
        else:
            (repo / "code.txt").write_text("newer unaccepted code", encoding="utf-8")
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "newer main")
        return repo, accepted

    def test_installs_accepted_commit_not_newer_main(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, accepted = self._fake_repo(tmp)
            home = Path(tmp) / "h"
            home.mkdir()
            self._run(repo, home)
            self.assertEqual(git(home / "dest", "rev-parse", "HEAD"), accepted)
            self.assertEqual((home / "dest" / "code.txt").read_text(encoding="utf-8"), "accepted code")
            # Running again (existing checkout) still lands on the accepted commit.
            self._run(repo, home)
            self.assertEqual(git(home / "dest", "rev-parse", "HEAD"), accepted)

    def test_acceptance_only_tip_is_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, accepted = self._fake_repo(tmp, acceptance_only_tip=True)
            home = Path(tmp) / "h"
            home.mkdir()
            self._run(repo, home)
            self.assertEqual(git(home / "dest", "rev-parse", "HEAD"), git(repo, "rev-parse", "HEAD"))

    def test_developer_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, accepted = self._fake_repo(tmp)
            home = Path(tmp) / "h"
            home.mkdir()
            self._run(repo, home, AI_VERSE_SKILLS_REF="main")
            self.assertEqual(git(home / "dest", "rev-parse", "HEAD"), git(repo, "rev-parse", "main"))

    def test_bogus_revision_stops_and_installs_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, _ = self._fake_repo(tmp)
            (repo / "release" / "component-release.json").write_text(
                json.dumps({"release_status": "accepted", "revision": "a" * 40}), encoding="utf-8")
            git(repo, "commit", "-qam", "bogus")
            home = Path(tmp) / "h"
            home.mkdir()
            r = self._run(repo, home)
            self.assertEqual(r.returncode, 2)
            self.assertIn("Nothing was changed", r.stderr)
            self.assertFalse((home / "dest").exists())

    def test_not_accepted_status_stops(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, accepted = self._fake_repo(tmp)
            (repo / "release" / "component-release.json").write_text(
                json.dumps({"release_status": "candidate", "revision": accepted}), encoding="utf-8")
            git(repo, "commit", "-qam", "candidate")
            home = Path(tmp) / "h"
            home.mkdir()
            r = self._run(repo, home)
            self.assertEqual(r.returncode, 2)
            self.assertFalse((home / "dest").exists())

    def test_dirty_rerun_stops_with_friendly_message(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, accepted = self._fake_repo(tmp)
            home = Path(tmp) / "h"
            home.mkdir()
            self._run(repo, home)
            (home / "dest" / "code.txt").write_text("local edit", encoding="utf-8")
            r = self._run(repo, home)
            self.assertEqual(r.returncode, 2)
            self.assertIn("local changes", r.stderr)
            self.assertIn("Nothing was changed", r.stderr)
            self.assertEqual((home / "dest" / "code.txt").read_text(encoding="utf-8"), "local edit")

    def test_rename_into_release_is_not_release_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "origin"
            repo.mkdir()
            git(repo, "init", "-q", "-b", "main")
            (repo / "release").mkdir()
            (repo / "release" / "component-release.json").write_text("{}", encoding="utf-8")
            (repo / "code.txt").write_text("accepted code\n" * 20, encoding="utf-8")
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "accepted")
            accepted = git(repo, "rev-parse", "HEAD")
            git(repo, "mv", "code.txt", "release/code.txt")
            (repo / "release" / "component-release.json").write_text(
                json.dumps({"release_status": "accepted", "revision": accepted}), encoding="utf-8")
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "move code under release")
            home = Path(tmp) / "h"
            home.mkdir()
            self._run(repo, home)
            self.assertEqual(git(home / "dest", "rev-parse", "HEAD"), accepted)

    def test_missing_release_file_stops(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "origin"
            repo.mkdir()
            git(repo, "init", "-q", "-b", "main")
            (repo / "a").write_text("x", encoding="utf-8")
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "x")
            home = Path(tmp) / "h"
            home.mkdir()
            r = self._run(repo, home)
            self.assertEqual(r.returncode, 2)
            self.assertIn("no valid accepted release", r.stderr)


if __name__ == "__main__":
    unittest.main()
