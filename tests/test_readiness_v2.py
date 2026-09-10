import json
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

from installer import aiverse_skills as public_impl
from installer import aiverse_skills_v3 as impl
from installer import readiness_v2


class ReadinessV2Tests(unittest.TestCase):
    def _operator(self, oid):
        operators = impl.load("registry/operators.json")["operators"]
        return next(op for op in operators if op["id"] == oid)

    def _write_probe(self, base: Path, oid: str, payload=None, *, exit_code=0, sleep=0.0):
        script = base / f"probe-{oid}.py"
        body = ["import json, time, sys"]
        if sleep:
            body.append(f"time.sleep({sleep!r})")
        if payload is not None:
            body.append(f"print(json.dumps({payload!r}))")
        body.append(f"raise SystemExit({exit_code})")
        script.write_text("\n".join(body) + "\n", encoding="utf-8")
        return [sys.executable, str(script)]

    def _write_registry(self, base: Path, probes):
        registry = base / "probes.json"
        registry.write_text(
            json.dumps({"schema_version": 1, "probes": probes}),
            encoding="utf-8",
        )
        return registry

    def _env_for_registry(self, registry: Path):
        env = dict(os.environ)
        env["AI_VERSE_READINESS_PROBES"] = str(registry)
        return env

    def test_public_entrypoint_applies_readiness_v2(self):
        self.assertTrue(getattr(impl, "_readiness_v2_applied", False))
        result = public_impl.readiness(Path(tempfile.gettempdir()) / "not-an-install")
        self.assertEqual(result["schema_version"], 2)
        self.assertIn("operator_details", result)

    def test_gws_binary_alone_is_not_ready(self):
        op = self._operator("google-workspace")

        def fake_which(name):
            return "/fake/gws" if name == "gws" else None

        with mock.patch.object(readiness_v2.shutil, "which", side_effect=fake_which):
            report = readiness_v2._static_operator_report(impl, op, {})
        self.assertEqual(report["status"], "installed-unverified")
        self.assertFalse(report["ready"])
        self.assertFalse(report["live_verified"])

    def test_legacy_connection_env_hint_is_not_ready(self):
        op = self._operator("google-workspace")
        env = {"AI_VERSE_CONNECTION_GOOGLE_WORKSPACE": "connected"}
        with mock.patch.object(readiness_v2.shutil, "which", return_value=None):
            report = readiness_v2._static_operator_report(impl, op, env)
        self.assertEqual(report["status"], "configured-unverified")
        self.assertFalse(report["ready"])
        self.assertFalse(report["live_verified"])

    def test_live_connector_probe_requires_auth_reachability_and_usability(self):
        op = self._operator("google-workspace")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            good = {
                "schema_version": 1,
                "operator_id": "google-workspace",
                "authenticated": True,
                "reachable": True,
                "usable": True,
            }
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "google-workspace", good)}},
            )
            env = self._env_for_registry(registry)
            probes, error, _ = readiness_v2._load_probe_registry(base / "skills", env)
            self.assertIsNone(error)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "ready")
            self.assertTrue(report["ready"])
            self.assertTrue(report["live_verified"])

            unauthenticated = dict(good, authenticated=False)
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "google-workspace-unauth", unauthenticated)}},
            )
            env = self._env_for_registry(registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "authentication-failed")
            self.assertFalse(report["ready"])
            self.assertTrue(report["live_verified"])

            unreachable = dict(good, reachable=False)
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "google-workspace-down", unreachable)}},
            )
            env = self._env_for_registry(registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "unreachable")
            self.assertFalse(report["ready"])

    def test_probe_identity_and_shape_fail_closed_without_leaking_payload(self):
        op = self._operator("google-workspace")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            payload = {
                "schema_version": 1,
                "operator_id": "google-workspace",
                "authenticated": True,
                "reachable": True,
                "usable": True,
                "token": "super-secret-token",
            }
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "google-workspace", payload)}},
            )
            env = self._env_for_registry(registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "invalid-probe-result")
            self.assertFalse(report["ready"])
            self.assertNotIn("super-secret-token", json.dumps(report))

            wrong_identity = dict(payload)
            wrong_identity.pop("token")
            wrong_identity["operator_id"] = "hubspot"
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "wrong-id", wrong_identity)}},
            )
            env = self._env_for_registry(registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "invalid-probe-result")
            self.assertFalse(report["ready"])

    def test_probe_timeout_and_nonzero_exit_fail_closed(self):
        op = self._operator("google-workspace")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            payload = {
                "schema_version": 1,
                "operator_id": "google-workspace",
                "authenticated": True,
                "reachable": True,
                "usable": True,
            }
            timeout_registry = self._write_registry(
                base,
                {"google-workspace": {
                    "command": self._write_probe(base, "slow", payload, sleep=0.2),
                    "timeout_seconds": 0.05,
                }},
            )
            env = self._env_for_registry(timeout_registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "probe-timeout")
            self.assertFalse(report["ready"])

            failed_registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "failed", payload, exit_code=7)}},
            )
            env = self._env_for_registry(failed_registry)
            probes, _, _ = readiness_v2._load_probe_registry(base / "skills", env)
            report = readiness_v2.operator_report(impl, op, base / "skills", probes, env)
            self.assertEqual(report["status"], "probe-failed")
            self.assertFalse(report["ready"])

    def test_local_apps_are_installed_unverified_without_live_bridge_probe(self):
        op = self._operator("premiere-pro")
        with mock.patch.object(impl, "app_exists", return_value=True):
            report = readiness_v2._static_operator_report(impl, op, {})
        self.assertEqual(report["status"], "installed-unverified")
        self.assertFalse(report["ready"])

    def test_ffmpeg_uses_live_local_self_test(self):
        op = self._operator("ffmpeg")

        def fake_which(name):
            return f"/fake/{name}" if name in {"ffmpeg", "ffprobe"} else None

        completed = mock.Mock(returncode=0)
        with mock.patch.object(readiness_v2.shutil, "which", side_effect=fake_which), mock.patch.object(
            readiness_v2.subprocess, "run", return_value=completed
        ) as run_mock:
            report = readiness_v2._static_operator_report(impl, op, {})
        self.assertEqual(report["status"], "ready")
        self.assertTrue(report["ready"])
        self.assertTrue(report["live_verified"])
        self.assertEqual(run_mock.call_count, 2)

    def test_skill_readiness_requires_all_operator_proofs_and_keeps_generation_identity(self):
        manifest = {
            "generation_id": "gen-readiness-test",
            "packages": [
                {"kind": "employee", "id": "no-operator", "operators": []},
                {"kind": "employee", "id": "google-skill", "operators": ["google-workspace"]},
                {"kind": "support", "id": "support-only", "operators": []},
            ],
        }
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            env = {"AI_VERSE_CONNECTION_GOOGLE_WORKSPACE": "connected"}
            with mock.patch.object(impl, "load_manifest", return_value=manifest), mock.patch.object(
                readiness_v2.shutil, "which", return_value=None
            ):
                result = readiness_v2.evaluate_readiness(impl, base / "skills", env=env)
            self.assertEqual(result["generation_id"], "gen-readiness-test")
            self.assertIn("no-operator", result["skills"]["ready"])
            self.assertNotIn("google-skill", result["skills"]["ready"])
            conditional = {item["id"]: item for item in result["skills"]["conditional"]}
            self.assertEqual(conditional["google-skill"]["operators"]["google-workspace"], "configured-unverified")

            payload = {
                "schema_version": 1,
                "operator_id": "google-workspace",
                "authenticated": True,
                "reachable": True,
                "usable": True,
            }
            registry = self._write_registry(
                base,
                {"google-workspace": {"command": self._write_probe(base, "google-workspace", payload)}},
            )
            env = self._env_for_registry(registry)
            with mock.patch.object(impl, "load_manifest", return_value=manifest):
                result = readiness_v2.evaluate_readiness(impl, base / "skills", env=env)
            self.assertIn("google-skill", result["skills"]["ready"])
            self.assertTrue(result["operator_details"]["google-workspace"]["live_verified"])


if __name__ == "__main__":
    unittest.main()
