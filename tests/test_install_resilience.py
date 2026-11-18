"""One broken third party repo must not abort the whole install (FL-73)."""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
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

        class FakeProc:
            returncode = 0
            pid = 1

            def __init__(self, cmd, **kw):
                seen.update(kw)

            def communicate(self, timeout=None):
                seen["timeout"] = timeout
                return "", ""

        with mock.patch.object(v3.subprocess, "Popen", FakeProc):
            v3.run(["git", "status"], timeout=7)
        self.assertEqual(seen["timeout"], 7)
        self.assertEqual(seen["env"]["GIT_TERMINAL_PROMPT"], "0")
        self.assertEqual(seen["env"]["GIT_ASKPASS"], "true")
        self.assertEqual(seen["stdin"], subprocess.DEVNULL)
        if os.name != "nt":
            self.assertTrue(seen["start_new_session"])

    @unittest.skipIf(os.name == "nt", "process groups are POSIX here; Windows uses taskkill")
    def test_a_hung_git_and_its_child_are_both_killed(self):
        with tempfile.TemporaryDirectory() as td:
            bindir = Path(td) / "bin"
            bindir.mkdir()
            marker = Path(td) / "child.pid"
            fake = bindir / "git"
            fake.write_text(
                f"#!/bin/sh\nsleep 300 &\necho $! > '{marker}'\nsleep 300\n", encoding="utf-8"
            )
            fake.chmod(0o755)
            env = {**os.environ, "PATH": f"{bindir}{os.pathsep}{os.environ['PATH']}"}
            started = time.time()
            with mock.patch.dict(os.environ, env):
                with self.assertRaises(RuntimeError) as ctx:
                    v3.run(["git", "fetch"], timeout=1)
            self.assertLess(time.time() - started, 20)
            self.assertIn("timed out", str(ctx.exception))
            child = int(marker.read_text(encoding="utf-8").strip())
            time.sleep(0.3)
            with self.assertRaises(ProcessLookupError):
                os.kill(child, 0)

    def test_timeout_comes_from_environment(self):
        with mock.patch.dict(os.environ, {v3.GIT_TIMEOUT_ENV: "5"}):
            self.assertEqual(v3.git_timeout(), 5)
        with mock.patch.dict(os.environ, {v3.GIT_TIMEOUT_ENV: "nonsense"}):
            self.assertEqual(v3.git_timeout(), v3.DEFAULT_GIT_TIMEOUT)
        with mock.patch.dict(os.environ):
            os.environ.pop(v3.GIT_TIMEOUT_ENV, None)
            self.assertEqual(v3.git_timeout(), 120)

    def test_a_hung_git_is_stopped_and_reported_in_plain_words(self):
        def hang(cmd, cwd=None, timeout=None):
            raise RuntimeError(f"Command timed out after {timeout:g} seconds: {' '.join(cmd)}")

        with tempfile.TemporaryDirectory() as td, mock.patch.object(v3, "run", hang), \
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


REPO_ROOT = Path(__file__).resolve().parent.parent


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


class UpdateKeepsWhatYouHaveTests(unittest.TestCase):
    """An update with a dead repo must never remove skills the member already has."""

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.addCleanup(self.td.cleanup)
        self.base = Path(self.td.name) / "up"
        self.root = Path(self.td.name) / "root"
        self.shas = {n: make_repo(self.base, n) for n in ("alpha", "held")}

    def _plan(self, names):
        def plan(profile, root):
            return [
                ("support", n, None, root / "support" / n, {
                    "repo": f"owner/{n}", "commit": self.shas.get(n, "e" * 40),
                    "selector": {"type": "repo_root"}, "operators": [],
                })
                for n in names
            ]
        return plan

    def _install(self, names, cache):
        with mock.patch.object(v3, "install_plan", self._plan(names)), \
                mock.patch.dict(os.environ, {"AIVERSE_UPSTREAM_BASE": self.base.as_uri()}), \
                contextlib.redirect_stdout(io.StringIO()):
            return v3.transactional_install("full", self.root, Path(self.td.name) / cache)

    def _ids(self):
        return sorted(x["id"] for x in v3.load_manifest(self.root)["packages"])

    def test_dead_repo_keeps_the_installed_copy_and_skips_the_never_installed(self):
        self._install(["alpha", "held"], "cache1")
        shutil_rmtree = __import__("shutil").rmtree
        shutil_rmtree(self.base / "owner" / "held.git")
        installed, *_ = self._install(["alpha", "held", "newbie"], "cache2")
        self.assertEqual(sorted(x["id"] for x in installed), ["alpha", "held"])
        self.assertEqual(self._ids(), ["alpha", "held"])
        self.assertEqual([c for c, _ in v3.LAST_KEPT_PACKAGES], ["held"])
        self.assertEqual(v3.LAST_SKIPPED_PACKAGES, ["newbie"])
        kept = next(x for x in installed if x["id"] == "held")
        self.assertEqual(kept["source_commit"], self.shas["held"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = v3.report_upstream_failures(installed)
        self.assertEqual(code, v3.EXIT_PARTIAL_INSTALL)
        self.assertIn("Kept at the version you already had (1): held", out.getvalue())
        self.assertIn("never installed before (1): newbie", out.getvalue())

    def test_missing_old_copy_blocks_activation_and_leaves_install_untouched(self):
        self._install(["alpha", "held"], "cache1")
        before = v3.read_active_pointer(self.root)["generation_id"]
        pkg = v3.generation_path(self.root, before) / "support" / "held"
        __import__("shutil").rmtree(pkg)
        __import__("shutil").rmtree(self.base / "owner" / "held.git")
        with self.assertRaises(v3.PartialInstallBlocked):
            self._install(["alpha", "held"], "cache2")
        self.assertEqual(v3.read_active_pointer(self.root)["generation_id"], before)

    def test_corrupt_install_record_blocks_instead_of_dropping_skills(self):
        self._install(["alpha", "held"], "cache1")
        gid = v3.read_active_pointer(self.root)["generation_id"]
        (v3.generation_path(self.root, gid) / ".aiverse" / "installed.json").write_text("{not json", encoding="utf-8")
        with self.assertRaises(v3.PartialInstallBlocked) as ctx:
            self._install(["alpha", "held"], "cache2")
        self.assertIn("nothing was changed", str(ctx.exception))
        self.assertEqual(v3.read_active_pointer(self.root)["generation_id"], gid)

    def test_nothing_installed_yet_is_not_an_error(self):
        self.assertIsNone(v3.previous_install(self.root))

    def test_blocked_update_json_says_blocked_and_records_nothing(self):
        from installer import aiverse_skills as cli

        self._install(["alpha", "held"], "cache1")
        gid = v3.read_active_pointer(self.root)["generation_id"]
        pkg = v3.generation_path(self.root, gid) / "support" / "held"
        __import__("shutil").rmtree(pkg)
        __import__("shutil").rmtree(self.base / "owner" / "held.git")
        # Keep the manifest valid so the update starts, then block on the missing old copy.
        recorded = []
        out = io.StringIO()
        argv = ["--root", str(self.root), "--cache", str(Path(self.td.name) / "c3"), "update", "--json"]
        with mock.patch.object(v3, "install_plan", self._plan(["alpha", "held"])), \
                mock.patch.object(v3, "load_manifest", lambda root: {"profile": "full"}), \
                mock.patch.dict(os.environ, {"AIVERSE_UPSTREAM_BASE": self.base.as_uri()}), \
                mock.patch("installer.public_beta._write_integration", lambda *a, **k: recorded.append(a)), \
                contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as ctx:
                with mock.patch.object(sys, "argv", ["aiverse-skills", *argv]):
                    cli.main()
        self.assertEqual(ctx.exception.code, 3)
        self.assertEqual(recorded, [])
        payload = json.loads(out.getvalue())
        self.assertTrue(payload["blocked"])
        self.assertFalse(payload["partial"])
        self.assertEqual(payload["ok_packages"], [])
        self.assertEqual(v3.read_active_pointer(self.root)["generation_id"], gid)

    def test_cli_exit_code_json_and_lifecycle_for_a_fully_dead_upstream(self):
        empty = Path(self.td.name) / "empty"
        empty.mkdir()
        env = {**os.environ, "AIVERSE_UPSTREAM_BASE": empty.as_uri(), "HOME": self.td.name,
               v3.GIT_TIMEOUT_ENV: "20"}
        root = Path(self.td.name) / "cli-root"
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "installer" / "aiverse_skills.py"), "--root", str(root),
             "--cache", str(Path(self.td.name) / "cli-cache"), "install", "--profile", "full", "--json"],
            capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(REPO_ROOT),
        )
        self.assertEqual(proc.returncode, 3, proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload["partial"])
        self.assertTrue(payload["partial_report"]["failed_repos"])
        self.assertFalse(payload["blocked"])
        self.assertEqual(payload["ok_packages"], payload["partial_report"]["ok_packages"])
        self.assertEqual(payload["failed_packages"], payload["partial_report"]["failed_packages"])
        self.assertTrue(payload["partial_report"]["ok_packages"])
        self.assertTrue(payload["partial_report"]["failed_packages"])
        self.assertTrue((root / ".aiverse").exists())


if __name__ == "__main__":
    unittest.main()
