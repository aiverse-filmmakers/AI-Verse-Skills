"""A pin taken from a short lived shell must keep its generation alive (FL-25).

Agents usually run `aiverse-skills pin` through a one shot shell. The lease used to
be tied only to that shell's pid, so as soon as the shell exited the next purge
treated the lease as dead and could delete the generation the agent was reading.
"""
import contextlib
import datetime as dt
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from installer import aiverse_skills as skills
from installer.generation_lifecycle import (
    acquire_generation_lease,
    generation_leases_dir,
    generation_path,
)
from tests.test_generation_lifecycle import GenerationFixture


class PinLeaseOutlivesShell(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "skills"
        self.root.mkdir()
        GenerationFixture.commit(self.root, self.base, "gen-v1", "v1")

    def tearDown(self):
        self.tmp.cleanup()

    def pin_from_short_shell(self, **extra):
        # Stand in for the agent's shell: a real process that is alive while pin runs
        # and has exited before the purge, exactly like `bash -c "aiverse-skills pin"`.
        shell = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
        try:
            out = io.StringIO()
            with mock.patch.object(skills._impl.os, "getppid", return_value=shell.pid), contextlib.redirect_stdout(out):
                skills.cmd_pin(SimpleNamespace(root=str(self.root), lease_owner_pid=None, package=None, json=True, **extra))
        finally:
            shell.terminate()
            shell.wait(timeout=10)
        return json.loads(out.getvalue())

    def test_lease_survives_the_shell_exiting(self):
        pinned = self.pin_from_short_shell()
        self.assertIn("lease_hold_until", pinned)
        GenerationFixture.commit(self.root, self.base, "gen-v2", "v2")
        report = skills.purge_generations(self.root, keep=0, confirmed=True)
        self.assertTrue(generation_path(self.root, "gen-v1").is_dir())
        self.assertIn("gen-v1", report["protected"])
        self.assertEqual(report["stale_execution_leases_reaped"], [])

    def test_unpin_still_releases_it_early(self):
        pinned = self.pin_from_short_shell()
        self.assertTrue(skills.release_generation_lease(
            self.root, pinned["generation_id"], pinned["lease_id"], pinned["lease_token"]))
        GenerationFixture.commit(self.root, self.base, "gen-v2", "v2")
        skills.purge_generations(self.root, keep=0, confirmed=True)
        self.assertFalse(generation_path(self.root, "gen-v1").exists())

    def test_expired_hold_with_dead_shell_is_reaped(self):
        pinned = self.pin_from_short_shell()
        lease_file = generation_leases_dir(self.root) / "gen-v1" / (pinned["lease_id"] + ".json")
        data = json.loads(lease_file.read_text(encoding="utf-8"))
        data["hold_until"] = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=1)).isoformat()
        lease_file.write_text(json.dumps(data), encoding="utf-8")
        GenerationFixture.commit(self.root, self.base, "gen-v2", "v2")
        report = skills.purge_generations(self.root, keep=0, confirmed=True)
        self.assertEqual(len(report["stale_execution_leases_reaped"]), 1)
        self.assertFalse(generation_path(self.root, "gen-v1").exists())

    def test_malformed_hold_time_fails_closed(self):
        pinned = self.pin_from_short_shell()
        lease_file = generation_leases_dir(self.root) / "gen-v1" / (pinned["lease_id"] + ".json")
        data = json.loads(lease_file.read_text(encoding="utf-8"))
        data["hold_until"] = "not a time"
        lease_file.write_text(json.dumps(data), encoding="utf-8")
        GenerationFixture.commit(self.root, self.base, "gen-v2", "v2")
        report = skills.purge_generations(self.root, keep=0, confirmed=True)
        self.assertTrue(generation_path(self.root, "gen-v1").is_dir())
        self.assertEqual(len(report["unverifiable_execution_leases"]), 1)

    def test_explicit_owner_pid_keeps_the_old_pid_only_rule(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            skills.cmd_pin(SimpleNamespace(root=str(self.root), lease_owner_pid=os.getpid(), package=None, json=True))
        self.assertNotIn("lease_hold_until", json.loads(out.getvalue()))

    def test_zero_hours_is_refused(self):
        with self.assertRaisesRegex(RuntimeError, "lease-hours"):
            self.pin_from_short_shell(lease_hours=0)

    def test_huge_or_infinite_hours_are_refused_cleanly(self):
        # These used to crash with OverflowError or hold a generation for a century.
        for hours in (float("inf"), float("nan"), 1e12, 24 * 30 + 1):
            with self.subTest(hours=hours):
                with self.assertRaisesRegex(RuntimeError, "lease-hours"):
                    self.pin_from_short_shell(lease_hours=hours)

    def test_far_future_hold_in_the_file_is_capped_at_30_days(self):
        pinned = self.pin_from_short_shell()
        lease_file = generation_leases_dir(self.root) / "gen-v1" / (pinned["lease_id"] + ".json")
        data = json.loads(lease_file.read_text(encoding="utf-8"))
        old = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=31)
        data["created_at"] = old.isoformat()
        data["hold_until"] = (old + dt.timedelta(days=36500)).isoformat()
        lease_file.write_text(json.dumps(data), encoding="utf-8")
        GenerationFixture.commit(self.root, self.base, "gen-v2", "v2")
        report = skills.purge_generations(self.root, keep=0, confirmed=True)
        self.assertEqual(len(report["stale_execution_leases_reaped"]), 1)

    def test_past_hold_time_is_refused_by_the_library(self):
        with self.assertRaisesRegex(RuntimeError, "hold_until"):
            acquire_generation_lease(self.root, skills.digest,
                                     hold_until=dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=1))


if __name__ == "__main__":
    unittest.main()
