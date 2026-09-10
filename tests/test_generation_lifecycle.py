import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

from installer.aiverse_skills_v3 import digest, materialize_adapter, verify_adapter_target
from installer.generation_lifecycle import (
    GENERATION_SCHEMA_VERSION,
    active_pointer_path,
    activate_generation,
    commit_stage,
    generation_content_digest,
    lifecycle_lock,
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
            pointer = active_pointer_path(root)

            def fail_pointer_swap(src, dst):
                if Path(dst) == pointer:
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


if __name__ == "__main__":
    unittest.main()
