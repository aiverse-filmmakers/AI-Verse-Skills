from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_release_record.py"
spec = importlib.util.spec_from_file_location("check_release_record", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)

DISPLAY = "1.4.0"
OLD = "1.1.0-beta.2.dev0"
GOOD_PY = 'version = (impl.REPO_ROOT / "VERSION").read_text()\n    return {"version": version}\n'


def git(repo, *args):
    out = subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.com", *args],
        check=True, capture_output=True, text=True,
        encoding="utf-8",
    )
    return out.stdout.strip()


def write(repo, rel, text):
    path = Path(repo) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def record(revision, version=DISPLAY, ci="1", acceptance="2"):
    return {
        "schema_version": guard.SCHEMA,
        "version": version,
        "revision": revision,
        "release_status": "accepted",
        "evidence": {"ci": [{"run_id": ci}], "acceptance": [{"run_id": acceptance}]},
    }


class ReleaseRecordGuardTests(unittest.TestCase):
    def write_code(self, repo, code_version, py=GOOD_PY):
        write(repo, "VERSION", code_version + "\n")
        write(repo, "docs/PUBLIC_BETA.md", f"# Contract\n\n**Version:** {code_version} (note)\n")
        write(repo, "installer/public_beta.py", py)

    def make_repo(self, code_version=DISPLAY, py=GOOD_PY):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        repo = Path(tmp.name)
        git(repo, "init", "-q")
        self.write_code(repo, code_version, py)
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "code")
        return repo, git(repo, "rev-parse", "HEAD")

    def put_record(self, repo, data):
        write(repo, guard.RECORD_PATH, json.dumps(data))

    def test_matching_record_passes(self):
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        self.assertEqual(guard.check(repo), ([], []))

    def test_version_mismatch_at_accepted_commit_fails(self):
        repo, sha = self.make_repo(code_version=OLD)
        self.put_record(repo, record(sha))
        problems, _ = guard.check(repo)
        self.assertTrue(any(p.startswith("VERSION ") for p in problems))
        self.assertTrue(any("PUBLIC_BETA.md" in p for p in problems))

    def test_hard_coded_descriptor_version_fails(self):
        repo, sha = self.make_repo(py='return {"version": "1.4.0"}\n')
        self.put_record(repo, record(sha))
        problems, _ = guard.check(repo)
        self.assertTrue(any("public_beta.py" in p for p in problems))

    def test_reads_code_at_accepted_commit_not_head(self):
        repo, sha = self.make_repo(code_version=OLD)
        self.write_code(repo, DISPLAY)
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "later fix")
        self.put_record(repo, record(sha))
        problems, _ = guard.check(repo)
        self.assertTrue(problems)

    def test_missing_commit_fails(self):
        repo, _ = self.make_repo()
        self.put_record(repo, record("a" * 40))
        problems, _ = guard.check(repo)
        self.assertTrue(any("does not exist" in p for p in problems))

    def test_duplicate_run_id_fails(self):
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha, ci="7", acceptance="7"))
        problems, _ = guard.check(repo)
        self.assertTrue(any("listed twice" in p for p in problems))

    def test_malformed_record_fails(self):
        repo, _ = self.make_repo()
        write(repo, guard.RECORD_PATH, "{not json")
        problems, _ = guard.check(repo)
        self.assertTrue(any("cannot be read" in p for p in problems))

    def test_missing_record_fails(self):
        repo, _ = self.make_repo()
        problems, _ = guard.check(repo)
        self.assertTrue(problems)

    def test_stale_warns_but_does_not_fail(self):
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        git(repo, "add", "-A")
        for i in range(guard.STALE_AFTER_COMMITS + 1):
            git(repo, "commit", "-q", "--allow-empty", "-m", f"c{i}")
        problems, warnings = guard.check(repo)
        self.assertEqual(problems, [])
        self.assertEqual(len(warnings), 1)

    def test_not_stale_at_limit(self):
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        for i in range(guard.STALE_AFTER_COMMITS):
            git(repo, "commit", "-q", "--allow-empty", "-m", f"c{i}")
        self.assertEqual(guard.check(repo)[1], [])

    def run_mode(self, repo, strict):
        import contextlib
        import io
        buf = io.StringIO()
        summary = Path(repo) / "summary.md"
        with contextlib.redirect_stdout(buf):
            code = guard.run(repo, strict, env={"GITHUB_STEP_SUMMARY": str(summary)})
        return code, buf.getvalue(), summary.read_text(encoding="utf-8")

    def test_warn_mode_exits_zero_but_is_loud(self):
        repo, sha = self.make_repo(code_version=OLD)
        self.put_record(repo, record(sha, ci="7", acceptance="7"))
        code, out, summary = self.run_mode(repo, False)
        self.assertEqual(code, 0)
        self.assertIn("::warning title=Release record mismatch::", out)
        self.assertIn("listed twice", summary)
        self.assertIn("PUBLIC_BETA.md", summary)

    def test_strict_mode_exits_one(self):
        repo, sha = self.make_repo(code_version=OLD)
        self.put_record(repo, record(sha))
        self.assertEqual(self.run_mode(repo, True)[0], 1)

    def test_strict_mode_passes_when_clean(self):
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        self.assertEqual(self.run_mode(repo, True)[0], 0)

    def test_malformed_json_only_warns_by_default(self):
        repo, _ = self.make_repo()
        write(repo, guard.RECORD_PATH, "{nope")
        self.assertEqual(self.run_mode(repo, False)[0], 0)
        self.assertEqual(self.run_mode(repo, True)[0], 1)

    def test_strict_flag_and_env(self):
        self.assertTrue(guard.strict_requested(True, {}))
        self.assertTrue(guard.strict_requested(False, {"RELEASE_GUARD_STRICT": "1"}))
        self.assertFalse(guard.strict_requested(False, {}))
        self.assertFalse(guard.strict_requested(False, {"RELEASE_GUARD_STRICT": "0"}))

    def test_git_missing_is_reported_not_raised(self):
        import os
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        old = os.environ["PATH"]
        os.environ["PATH"] = str(repo / "nowhere")
        try:
            problems, _ = guard.check(repo)
        finally:
            os.environ["PATH"] = old
        self.assertTrue(any("git could not be run" in p for p in problems))
        self.assertFalse(any("does not exist" in p for p in problems))

    def test_main_swallows_crash_unless_strict(self):
        import contextlib
        import io
        import os
        from unittest import mock
        repo, _ = self.make_repo()
        with mock.patch.object(guard, "check", side_effect=RuntimeError("boom")):
            for env, want in (({}, 0), ({"RELEASE_GUARD_STRICT": "1"}, 1)):
                with mock.patch.dict(os.environ, env), contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(guard.main([str(repo)]), want)
                self.assertIn("::", out.getvalue())

    def test_binary_file_does_not_hide_other_findings(self):
        repo, _ = self.make_repo(code_version=OLD)
        (repo / "VERSION").write_bytes(b"\xff\xfe\x00\x80")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "binary")
        sha = git(repo, "rev-parse", "HEAD")
        self.put_record(repo, record(sha, ci="7", acceptance="7"))
        problems, _ = guard.check(repo)
        self.assertTrue(any("listed twice" in p for p in problems))
        self.assertTrue(any("PUBLIC_BETA.md" in p for p in problems))
        self.assertFalse(any("crashed" in p for p in problems))

    def test_git_missing_in_default_mode_exits_zero(self):
        import contextlib
        import io
        import os
        from unittest import mock
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        with mock.patch.dict(os.environ, {"PATH": str(repo / "nowhere")}), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(guard.main([str(repo)]), 0)
        self.assertIn("::warning", out.getvalue())

    def test_git_missing_in_strict_mode_exits_one(self):
        import contextlib
        import io
        import os
        from unittest import mock
        repo, sha = self.make_repo()
        self.put_record(repo, record(sha))
        with mock.patch.dict(os.environ, {"PATH": str(repo / "nowhere")}), \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(guard.main([str(repo), "--strict"]), 1)


if __name__ == "__main__":
    unittest.main()
