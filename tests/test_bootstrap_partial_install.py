"""bootstrap.sh treats install exit code 3 (partial) as success when readiness passes."""
import json
import os
import stat
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


@unittest.skipIf(os.name == "nt", "bootstrap.sh is a POSIX shell script")
class BootstrapPartialInstallTests(unittest.TestCase):
    def _run(self, install_code, doctor_code):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "origin"
            repo.mkdir()
            git(repo, "init", "-q", "-b", "main")
            (repo / "release").mkdir()
            (repo / "release" / "component-release.json").write_text("{}", encoding="utf-8")
            script = repo / "aiverse-skills"
            script.write_text(
                "#!/bin/sh\n"
                f'case "$1" in install) exit {install_code};; doctor) echo READINESS-RAN; exit {doctor_code};; esac\n',
                encoding="utf-8",
            )
            script.chmod(script.stat().st_mode | stat.S_IXUSR)
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "code")
            accepted = git(repo, "rev-parse", "HEAD")
            (repo / "release" / "component-release.json").write_text(
                json.dumps({"release_status": "accepted", "revision": accepted}), encoding="utf-8")
            git(repo, "add", "-A")
            git(repo, "commit", "-q", "-m", "accept")
            home = Path(tmp) / "home"
            home.mkdir()
            env = {**os.environ, "HOME": str(home), "AI_VERSE_SKILLS_REPO": str(repo),
                   "AI_VERSE_SKILLS_HOME": str(home / "dest"), "AI_VERSE_BIN_DIR": str(home / "bin")}
            env.pop("AI_VERSE_SKILLS_REF", None)
            return subprocess.run(["sh", str(BOOT)], capture_output=True, text=True, env=env, encoding="utf-8")

    def test_partial_install_still_runs_readiness_and_succeeds(self):
        r = self._run(3, 0)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("READINESS-RAN", r.stdout)
        self.assertIn("some third party skills were skipped", r.stdout)

    def test_partial_install_fails_when_readiness_fails(self):
        r = self._run(3, 1)
        self.assertEqual(r.returncode, 1)

    def test_other_install_failures_still_stop_early(self):
        r = self._run(2, 0)
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("READINESS-RAN", r.stdout)

    def test_blocked_install_exit_4_is_not_treated_as_partial_success(self):
        r = self._run(4, 0)
        self.assertEqual(r.returncode, 4)
        self.assertNotIn("READINESS-RAN", r.stdout)
        self.assertNotIn("installed and ready", r.stdout)
        self.assertIn("not installed or changed", r.stderr)

    def test_clean_install_prints_no_partial_note(self):
        r = self._run(0, 0)
        self.assertEqual(r.returncode, 0)
        self.assertNotIn("skipped", r.stdout)


if __name__ == "__main__":
    unittest.main()
