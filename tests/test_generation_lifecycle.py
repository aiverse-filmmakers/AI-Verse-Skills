import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest import mock

from installer import aiverse_skills as skills
from installer import learning
from installer.aiverse_skills_v3 import digest, materialize_adapter, verify_adapter_target
from installer.generation_lifecycle import (
    GENERATION_SCHEMA_VERSION,
    LOCK_STALE_SECONDS,
    active_pointer_path,
    activate_generation,
    commit_stage,
    controller_path,
    generation_content_digest,
    generation_path,
    generation_leases_dir,
    generations_dir,
    acquire_generation_lease,
    active_generation_leases,
    release_generation_lease,
    lifecycle_lock,
    lifecycle_lock_path,
    mark_uninstalled,
    pin_active_generation,
    read_active_pointer,
    rollback_active_generation,
    verify_generation,
)


class GenerationFixture:
    @staticmethod
    def stage(base: Path, generation_id: str, label: str) -> Path:
        stage = base / f"stage-{generation_id}"
        package = stage / "imported" / "test" / "sample"
        scripts = package / "scripts"
        scripts.mkdir(parents=True)
        (package / "SKILL.md").write_text(
            f"---\nname: sample\n---\ninstructions-{label}\n",
            encoding="utf-8",
        )
        (scripts / "run.py").write_text(f"print('script-{label}')\n", encoding="utf-8")
        package_digest = digest(package)
        meta = stage / ".aiverse"
        meta.mkdir(parents=True)
        manifest = {
            "schema_version": 2,
            "generation_schema_version": GENERATION_SCHEMA_VERSION,
            "distribution": "AI-Verse-Skills",
            "profile": "test",
            "generation_id": generation_id,
            "generation_digest_sha256": generation_content_digest(stage),
            "packages": [
                {
                    "kind": "employee",
                    "id": "sample",
                    "path": "imported/test/sample",
                    "operators": [],
                    "digest_sha256": package_digest,
                }
            ],
        }
        (meta / "installed.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return stage

    @classmethod
    def commit(cls, root: Path, base: Path, generation_id: str, label: str, *, activate=True):
        stage = cls.stage(base, generation_id, label)
        commit_stage(root, stage, generation_id)
        errors = verify_generation(root, generation_id, digest)
        if errors:
            raise AssertionError(errors)
        if activate:
            activate_generation(root, generation_id)


class ImmutableGenerationLifecycleTests(unittest.TestCase):
    def _make_dir_link(self, link: Path, destination: Path) -> None:
        if os.name == "nt":
            subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(link), str(destination)],
                check=True,
                capture_output=True,
                text=True,
            )
        else:
            link.symlink_to(destination, target_is_directory=True)

    def _replace_with_dir_link(self, path: Path, destination: Path) -> None:
        if path.exists() or os.path.lexists(path):
            if path.is_dir() and not path.is_symlink():
                shutil.rmtree(path)
            else:
                path.unlink()
        path.parent.mkdir(parents=True, exist_ok=True)
        self._make_dir_link(path, destination)

    def test_pinned_execution_survives_update_rollback_and_uninstall(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")

            execution = pin_active_generation(root, digest)
            package = execution.package_path("sample")
            self.assertIn("instructions-v1", (package / "SKILL.md").read_text(encoding="utf-8"))

            # Update: activate a complete new generation. The execution keeps v1.
            GenerationFixture.commit(root, base, "gen-v2", "v2")
            self.assertEqual(read_active_pointer(root)["generation_id"], "gen-v2")
            self.assertIn("instructions-v1", (package / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("script-v1", (package / "scripts" / "run.py").read_text(encoding="utf-8"))

            # Rollback changes only the pointer; the already pinned execution is untouched.
            rolled = rollback_active_generation(root, digest)
            self.assertEqual(rolled.generation_id, "gen-v1")
            self.assertIn("instructions-v1", (package / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("script-v1", (package / "scripts" / "run.py").read_text(encoding="utf-8"))

            # Re-activate v2 and uninstall. Generations remain available to in-flight work.
            activate_generation(root, "gen-v2")
            mark_uninstalled(root)
            self.assertEqual(read_active_pointer(root, allow_uninstalled=True)["state"], "uninstalled")
            self.assertIn("instructions-v1", (package / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("script-v1", (package / "scripts" / "run.py").read_text(encoding="utf-8"))

    def test_interrupted_activation_keeps_previous_generation_active(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            GenerationFixture.commit(root, base, "gen-v2", "v2", activate=False)

            real_replace = __import__("os").replace
            pointer = active_pointer_path(root).resolve()

            def fail_pointer_swap(src, dst):
                if Path(dst).resolve() == pointer:
                    raise OSError("simulated activation interruption")
                return real_replace(src, dst)

            with mock.patch("installer.generation_lifecycle.os.replace", side_effect=fail_pointer_swap):
                with self.assertRaises(OSError):
                    activate_generation(root, "gen-v2")

            active = pin_active_generation(root, digest)
            self.assertEqual(active.generation_id, "gen-v1")
            package = active.package_path("sample")
            self.assertIn("instructions-v1", (package / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("script-v1", (package / "scripts" / "run.py").read_text(encoding="utf-8"))

    def test_lifecycle_mutations_are_serialized(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skills"
            errors = []

            def contender():
                try:
                    with lifecycle_lock(root, timeout_seconds=0.10):
                        pass
                except RuntimeError as exc:
                    errors.append(str(exc))

            with lifecycle_lock(root):
                thread = threading.Thread(target=contender)
                thread.start()
                thread.join(timeout=2)

            self.assertEqual(len(errors), 1)
            self.assertIn("lifecycle is busy", errors[0])

    def test_stale_lifecycle_lock_is_not_reclaimed_while_holder_is_live(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skills"
            errors = []

            def contender():
                try:
                    with lifecycle_lock(root, timeout_seconds=0.10):
                        pass
                except RuntimeError as exc:
                    errors.append(str(exc))

            with lifecycle_lock(root):
                path = lifecycle_lock_path(root)
                stale_time = time.time() - LOCK_STALE_SECONDS - 10
                os.utime(path, (stale_time, stale_time))
                thread = threading.Thread(target=contender)
                thread.start()
                thread.join(timeout=2)
                self.assertFalse(thread.is_alive())
                self.assertTrue(path.exists())

            self.assertEqual(len(errors), 1)
            self.assertIn("lifecycle is busy", errors[0])
            self.assertFalse(lifecycle_lock_path(root).exists())

    def test_stale_lifecycle_lock_is_recovered_after_holder_crash(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skills"
            code = (
                "import os, sys\n"
                "from pathlib import Path\n"
                "from installer.generation_lifecycle import lifecycle_lock\n"
                "with lifecycle_lock(Path(sys.argv[1])):\n"
                "    os._exit(0)\n"
            )
            completed = subprocess.run(
                [sys.executable, "-c", code, str(root)],
                cwd=Path(__file__).resolve().parents[1],
                check=False,
            )
            self.assertEqual(completed.returncode, 0)

            path = lifecycle_lock_path(root)
            self.assertTrue(path.exists())
            crashed_holder = json.loads(path.read_text(encoding="utf-8"))
            self.assertNotEqual(crashed_holder["pid"], os.getpid())
            stale_time = time.time() - LOCK_STALE_SECONDS - 10
            os.utime(path, (stale_time, stale_time))

            with lifecycle_lock(root, timeout_seconds=1.0):
                recovered = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(recovered["pid"], os.getpid())
                self.assertNotEqual(recovered["token"], crashed_holder["token"])

            self.assertFalse(path.exists())

    def test_generation_tampering_is_detected_before_pin(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            pin = pin_active_generation(root, digest)
            (pin.package_path("sample") / "scripts" / "run.py").write_text(
                "print('tampered')\n", encoding="utf-8"
            )
            errors = verify_generation(root, "gen-v1", digest)
            self.assertTrue(any("content digest changed" in error for error in errors))
            with self.assertRaises(RuntimeError):
                pin_active_generation(root, digest)

    def test_copied_adapter_is_generation_bound_and_rejects_stale_active_state(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            target = base / "codex-skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")

            manifest = materialize_adapter(root, target, "codex", prefer_copy=True)
            self.assertEqual(manifest["generation_id"], "gen-v1")
            self.assertEqual(manifest["packages"][0]["mode"], "copy")
            self.assertEqual(verify_adapter_target(root, target), [])

            GenerationFixture.commit(root, base, "gen-v2", "v2")
            stale_errors = verify_adapter_target(root, target)
            self.assertTrue(any("stale adapter generation" in error for error in stale_errors))

            # The stale copy is rejected as current, but it remains internally consistent
            # with the generation it was created from and can never mix v1/v2 files.
            self.assertEqual(verify_adapter_target(root, target, require_active=False), [])
            copied = target / "sample"
            self.assertIn("instructions-v1", (copied / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("script-v1", (copied / "scripts" / "run.py").read_text(encoding="utf-8"))

    def test_public_pin_command_returns_lease_and_unpin_releases_it(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                skills.cmd_pin(SimpleNamespace(
                    root=str(root), lease_owner_pid=os.getpid(), package="sample", json=True
                ))
            pinned = json.loads(output.getvalue())
            self.assertEqual(pinned["generation_id"], "gen-v1")
            self.assertTrue(pinned["lease_release_required"])
            self.assertEqual(pinned["package_id"], "sample")
            self.assertTrue((Path(pinned["package_path"]) / "SKILL.md").is_file())
            leases = active_generation_leases(root)
            self.assertEqual(leases["protected_generation_ids"], ["gen-v1"])

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                skills.cmd_unpin(SimpleNamespace(
                    root=str(root),
                    generation_id=pinned["generation_id"],
                    lease_id=pinned["lease_id"],
                    lease_token=pinned["lease_token"],
                    json=True,
                ))
            self.assertTrue(json.loads(output.getvalue())["released"])
            self.assertEqual(active_generation_leases(root)["protected_generation_ids"], [])


    def test_exact_generation_lease_can_pin_previously_selected_generation(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            GenerationFixture.commit(root, base, "gen-v2", "v2")
            lease = acquire_generation_lease(root, digest, generation_id="gen-v1", package_id="sample")
            self.assertEqual(lease.generation_id, "gen-v1")
            self.assertIn("instructions-v1", (lease.package_path("sample") / "SKILL.md").read_text(encoding="utf-8"))
            report = skills.purge_generations(root, keep=0, confirmed=True)
            self.assertTrue(generation_path(root, "gen-v1").is_dir())
            self.assertIn("gen-v1", report["protected"])
            self.assertTrue(release_generation_lease(root, lease.generation_id, lease.lease_id, lease.lease_token))

    def test_invalid_package_does_not_publish_execution_lease(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            with self.assertRaisesRegex(RuntimeError, "Package not installed"):
                acquire_generation_lease(root, digest, package_id="missing")
            self.assertFalse(generation_leases_dir(root).exists())

    def test_purge_protects_live_execution_lease_until_explicit_release(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            lease = acquire_generation_lease(root, digest)

            GenerationFixture.commit(root, base, "gen-v2", "v2")
            report = skills.purge_generations(root, keep=0, confirmed=True)
            self.assertTrue(generation_path(root, "gen-v1").is_dir())
            self.assertIn("gen-v1", report["protected"])
            self.assertEqual(len(report["live_execution_leases"]), 1)
            self.assertEqual(report["unverifiable_execution_leases"], [])

            with self.assertRaisesRegex(RuntimeError, "token mismatch"):
                release_generation_lease(root, lease.generation_id, lease.lease_id, "wrong-token")
            self.assertTrue(generation_path(root, "gen-v1").is_dir())

            self.assertTrue(release_generation_lease(
                root, lease.generation_id, lease.lease_id, lease.lease_token
            ))
            second = skills.purge_generations(root, keep=0, confirmed=True)
            self.assertFalse(generation_path(root, "gen-v1").exists())
            self.assertIn("gen-v1", second["removed"])
            self.assertEqual(second["live_execution_leases"], [])
            self.assertEqual(active_generation_leases(root)["protected_generation_ids"], [])

    def test_live_old_execution_lease_is_not_reclaimed_by_age_and_dead_holder_recovers(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            holder = subprocess.Popen(
                [sys.executable, "-c", "import time; time.sleep(60)"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            try:
                time.sleep(0.1)
                lease = acquire_generation_lease(root, digest, owner_pid=holder.pid)
                lease_file = generation_leases_dir(root) / "gen-v1" / (lease.lease_id + ".json")
                os.utime(lease_file, (1, 1))
                GenerationFixture.commit(root, base, "gen-v2", "v2")

                live = skills.purge_generations(root, keep=0, confirmed=True)
                self.assertTrue(generation_path(root, "gen-v1").is_dir())
                self.assertEqual(len(live["live_execution_leases"]), 1)
                self.assertEqual(live["stale_execution_leases_reaped"], [])

                holder.terminate()
                holder.wait(timeout=10)
                recovered = skills.purge_generations(root, keep=0, confirmed=True)
                self.assertFalse(generation_path(root, "gen-v1").exists())
                self.assertEqual(recovered["live_execution_leases"], [])
                self.assertEqual(len(recovered["stale_execution_leases_reaped"]), 1)
            finally:
                if holder.poll() is None:
                    holder.terminate()
                    holder.wait(timeout=10)

    def test_foreign_or_unverifiable_execution_lease_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            lease = acquire_generation_lease(root, digest)
            lease_file = generation_leases_dir(root) / "gen-v1" / (lease.lease_id + ".json")
            record = json.loads(lease_file.read_text(encoding="utf-8"))
            record["hostname"] = "unreachable-remote-host"
            lease_file.write_text(json.dumps(record), encoding="utf-8")

            GenerationFixture.commit(root, base, "gen-v2", "v2")
            report = skills.purge_generations(root, keep=0, confirmed=True)
            self.assertTrue(generation_path(root, "gen-v1").is_dir())
            self.assertIn("gen-v1", report["protected"])
            self.assertEqual(report["live_execution_leases"], [])
            self.assertEqual(report["unverifiable_execution_leases"][0]["reason"], "foreign-host holder")

            self.assertTrue(release_generation_lease(
                root, lease.generation_id, lease.lease_id, lease.lease_token
            ))
            final = skills.purge_generations(root, keep=0, confirmed=True)
            self.assertFalse(generation_path(root, "gen-v1").exists())
            self.assertIn("gen-v1", final["removed"])

    def test_generation_lease_controller_indirection_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")
            lease = acquire_generation_lease(root, digest)
            leases = generation_leases_dir(root)
            shutil.rmtree(leases)
            outside = base / "outside-leases"
            outside.mkdir()
            sentinel = outside / "sentinel.json"
            sentinel.write_text('{"must":"remain"}', encoding="utf-8")
            self._make_dir_link(leases, outside)

            with self.assertRaises(RuntimeError):
                skills.purge_generations(root, keep=0, confirmed=True)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), '{"must":"remain"}')
            self.assertTrue(generation_path(root, lease.generation_id).is_dir())


    def test_controller_rejects_metadata_and_generation_indirection(self):
        cases = (".aiverse", ".aiverse/generations")
        for relative in cases:
            with self.subTest(relative=relative):
                with tempfile.TemporaryDirectory() as temp:
                    base = Path(temp)
                    root = base / "skills"
                    root.mkdir()
                    outside = base / "outside"
                    outside.mkdir()
                    sentinel = outside / "sentinel.txt"
                    sentinel.write_text("must remain outside", encoding="utf-8")

                    if relative != ".aiverse":
                        (root / ".aiverse").mkdir()
                    self._make_dir_link(root / relative, outside)

                    with self.assertRaises(RuntimeError):
                        if relative == ".aiverse":
                            controller_path(root, "active.json")
                        else:
                            generation_path(root, "gen-outside")

                    self.assertEqual(sentinel.read_text(encoding="utf-8"), "must remain outside")

    def test_commit_stage_cannot_write_through_redirected_controller(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            outside = base / "outside"
            outside.mkdir()
            sentinel = outside / "sentinel.txt"
            sentinel.write_text("external controller data", encoding="utf-8")
            self._make_dir_link(root / ".aiverse", outside)
            stage = GenerationFixture.stage(base, "gen-escape", "escape")

            with self.assertRaises(RuntimeError):
                commit_stage(root, stage, "gen-escape")

            self.assertTrue(stage.exists())
            self.assertFalse((outside / "generations" / "gen-escape").exists())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "external controller data")

    def test_public_purge_refuses_redirected_generation_store_without_external_deletion(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")

            generation_root = generations_dir(root)
            shutil.rmtree(generation_root)
            outside = base / "outside-generations"
            orphan = outside / "gen-orphan"
            orphan.mkdir(parents=True)
            sentinel = orphan / "sentinel.txt"
            sentinel.write_text("do not delete", encoding="utf-8")
            self._make_dir_link(generation_root, outside)

            pointer_before = active_pointer_path(root).read_bytes()
            with self.assertRaises(RuntimeError):
                skills.purge_generations(root, keep=0, confirmed=True)

            self.assertEqual(sentinel.read_text(encoding="utf-8"), "do not delete")
            self.assertEqual(active_pointer_path(root).read_bytes(), pointer_before)

    def test_learning_state_refuses_redirected_controller_storage(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            GenerationFixture.commit(root, base, "gen-v1", "v1")

            outside = base / "outside-learning"
            outside.mkdir()
            sentinel = outside / "sentinel.txt"
            sentinel.write_text("no learning writes", encoding="utf-8")
            self._make_dir_link(controller_path(root) / "learning", outside)

            with self.assertRaises(RuntimeError):
                learning.ensure_learning_state(skills, root)

            self.assertEqual(sentinel.read_text(encoding="utf-8"), "no learning writes")
            self.assertEqual(list(outside.iterdir()), [sentinel])

    def test_status_refuses_external_controller_state(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            outside = base / "outside-state"
            outside.mkdir()
            (outside / "active.json").write_text(
                json.dumps({
                    "schema_version": 1,
                    "state": "uninstalled",
                    "generation_id": None,
                    "generation_digest_sha256": None,
                    "history": ["gen-outside"],
                }) + "\n",
                encoding="utf-8",
            )
            self._make_dir_link(root / ".aiverse", outside)

            with self.assertRaises(RuntimeError):
                skills.status_report(root)


if __name__ == "__main__":
    unittest.main()
