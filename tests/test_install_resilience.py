"""One broken third party repo must not abort the whole install (FL-73)."""
import contextlib
import io
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from installer import aiverse_skills_v3 as v3


def git(*args, cwd):
    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args],
        cwd=cwd, check=True, capture_output=True, text=True, encoding="utf-8",
    )


def make_repo(base, name, body="demo"):
    repo = base / "owner" / (name + ".git")
    repo.mkdir(parents=True)
    (repo / "SKILL.md").write_text(f"---\nname: {name}\n---\n{body}\n", encoding="utf-8")
    git("init", "-q", cwd=repo)
    git("add", ".", cwd=repo)
    git("commit", "-q", "-m", "x", cwd=repo)
    sha = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True, encoding="utf-8"
    ).stdout.strip()
    return sha


class GitGuardTests(unittest.TestCase):
    def test_git_never_prompts_and_has_a_timeout(self):
        seen = {}

        def fake_run(cmd, **kw):
            seen.update(kw)
            return subprocess.CompletedProcess(cmd, 0, "", "")

        with mock.patch.object(v3.subprocess, "run", fake_run):
            v3.run(["git", "status"], timeout=7)
        self.assertEqual(seen["timeout"], 7)
        self.assertEqual(seen["env"]["GIT_TERMINAL_PROMPT"], "0")
        self.assertEqual(seen["env"]["GIT_ASKPASS"], "true")
        self.assertEqual(seen["stdin"], subprocess.DEVNULL)

    def test_timeout_comes_from_environment(self):
        with mock.patch.dict(os.environ, {v3.GIT_TIMEOUT_ENV: "5"}):
            self.assertEqual(v3.git_timeout(), 5)
        with mock.patch.dict(os.environ, {v3.GIT_TIMEOUT_ENV: "nonsense"}):
            self.assertEqual(v3.git_timeout(), v3.DEFAULT_GIT_TIMEOUT)
        with mock.patch.dict(os.environ):
            os.environ.pop(v3.GIT_TIMEOUT_ENV, None)
            self.assertEqual(v3.git_timeout(), 120)

    def test_a_hung_git_is_stopped_and_reported_in_plain_words(self):
        def hang(cmd, **kw):
            raise subprocess.TimeoutExpired(cmd, kw["timeout"])

        with tempfile.TemporaryDirectory() as td, mock.patch.object(v3.subprocess, "run", hang), \
                mock.patch.dict(os.environ, {v3.GIT_TIMEOUT_ENV: "2"}):
            with self.assertRaises(v3.UpstreamFetchError) as ctx:
                v3.checkout("owner/slow", "a" * 40, Path(td))
        self.assertIn("timed out after 2 seconds", str(ctx.exception))
        self.assertIn("owner/slow", str(ctx.exception))

    def test_working_local_repo_still_installs(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td) / "up"
            sha = make_repo(base, "good")
            with mock.patch.dict(os.environ, {"AIVERSE_UPSTREAM_BASE": base.as_uri()}):
                dst = v3.checkout("owner/good", sha, Path(td) / "cache")
            self.assertTrue((dst / "SKILL.md").exists())

    def test_missing_local_repo_raises_fetch_error_and_leaves_no_partial_folder(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td) / "up"
            base.mkdir()
            with mock.patch.dict(os.environ, {"AIVERSE_UPSTREAM_BASE": base.as_uri()}):
                with self.assertRaises(v3.UpstreamFetchError):
                    v3.checkout("owner/gone", "b" * 40, Path(td) / "cache")
            self.assertEqual([p for p in (Path(td) / "cache").iterdir()], [])


class PartialInstallTests(unittest.TestCase):
    def _jobs(self, base, stage, shas):
        jobs = []
        for name in ("alpha", "broken", "gamma", "broken_two"):
            p = {
                "repo": f"owner/{name}", "commit": shas.get(name, "c" * 40),
                "selector": {"type": "repo_root"}, "operators": [],
            }
            jobs.append(("support", name, None, stage / "support" / name, p))
        return jobs

    def _run_stage(self, td):
        base = Path(td) / "up"
        shas = {"alpha": make_repo(base, "alpha"), "gamma": make_repo(base, "gamma")}
        stage = Path(td) / "stage"
        stage.mkdir()
        with mock.patch.object(v3, "install_plan", lambda profile, root: self._jobs(base, stage, shas)), \
                mock.patch.dict(os.environ, {"AIVERSE_UPSTREAM_BASE": base.as_uri()}), \
                contextlib.redirect_stdout(io.StringIO()):
            return v3.build_stage("full", stage, Path(td) / "cache", "gen-test")

    def test_one_dead_repo_does_not_stop_the_others(self):
        with tempfile.TemporaryDirectory() as td:
            installed = self._run_stage(td)
            self.assertEqual([x["id"] for x in installed], ["alpha", "gamma"])
            self.assertEqual(sorted(k[0] for k in v3.LAST_FETCH_FAILURES), ["owner/broken", "owner/broken_two"])
            self.assertEqual(sorted(v3.LAST_SKIPPED_PACKAGES), ["broken", "broken_two"])

    def test_report_names_winners_and_losers_and_exit_code_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            installed = self._run_stage(td)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = v3.report_upstream_failures(installed)
            text = out.getvalue()
            self.assertEqual(code, v3.EXIT_PARTIAL_INSTALL)
            self.assertIn("partial", text)
            self.assertIn("owner/alpha", text)
            self.assertIn("owner/broken", text)
            self.assertNotIn("Traceback", text)

    def test_everything_working_reports_nothing_and_exits_zero(self):
        v3.LAST_FETCH_FAILURES.clear()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(v3.report_upstream_failures([]), 0)
        self.assertEqual(out.getvalue(), "")

    def test_offline_cache_miss_is_still_an_error(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(RuntimeError) as ctx:
                v3.checkout("owner/x", "d" * 40, Path(td), offline=True)
            self.assertNotIsInstance(ctx.exception, v3.UpstreamFetchError)


if __name__ == "__main__":
    unittest.main()
