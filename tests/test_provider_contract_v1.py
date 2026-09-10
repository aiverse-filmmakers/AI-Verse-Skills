import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from installer import aiverse_skills as public_impl
from installer import aiverse_skills_v3 as impl
from installer.provider_contract_v1 import (
    CONTRACT_ID,
    DIGEST_ALGORITHM,
    INDEX_FILENAME,
    MANIFEST_SCHEMA_VERSION,
    PROVIDER_ID,
    package_digest_v1,
    qualified_segment,
    verify_provider_generation,
)


class ProviderFixture:
    @staticmethod
    def package(stage: Path, rel: str, *, name: str, version: str = "1.2.3", description: str = "Test capability.") -> Path:
        package = stage / rel
        package.mkdir(parents=True)
        (package / "SKILL.md").write_text(
            "---\n"
            f"name: {name}\n"
            f"version: {version}\n"
            f'description: "{description}"\n'
            "---\n\n"
            f"# {name}\n",
            encoding="utf-8",
        )
        (package / "resource.txt").write_text(f"resource-{name}\n", encoding="utf-8")
        return package

    @classmethod
    def stage(cls, base: Path, generation_id: str = "gen-provider-test"):
        stage = base / "stage"
        employee = cls.package(stage, "imported/test/Council", name="Council")
        support = cls.package(stage, "dependencies/test/helper", name="helper")
        installed = [
            {
                "kind": "employee",
                "id": "Council",
                "path": "imported/test/Council",
                "source_repo": "example/council",
                "source_commit": "a" * 40,
                "operators": ["test-operator"],
                "digest_sha256": impl.digest(employee),
            },
            {
                "kind": "support",
                "id": "helper",
                "path": "dependencies/test/helper",
                "source_repo": "example/helper",
                "source_commit": "b" * 40,
                "operators": [],
                "digest_sha256": impl.digest(support),
            },
        ]
        public_impl._write_stage_manifest("test", installed, generation_id, stage)
        return stage, installed


class ProviderContractV1Tests(unittest.TestCase):
    def test_public_entrypoint_enables_provider_v1_producer(self):
        with tempfile.TemporaryDirectory() as temp:
            stage, _ = ProviderFixture.stage(Path(temp))
            manifest_path = stage / ".aiverse" / "installed.json"
            index_path = stage / ".aiverse" / INDEX_FILENAME
            manifest_bytes = manifest_path.read_bytes()
            manifest = json.loads(manifest_bytes)
            index = json.loads(index_path.read_text(encoding="utf-8"))

            self.assertEqual(manifest["schema_version"], MANIFEST_SCHEMA_VERSION)
            self.assertEqual(manifest["provider_contract"], CONTRACT_ID)
            self.assertEqual(manifest["provider_id"], PROVIDER_ID)
            self.assertEqual(index["contract"], CONTRACT_ID)
            self.assertEqual(index["provider_id"], PROVIDER_ID)
            self.assertEqual(index["generation_id"], manifest["generation_id"])
            self.assertEqual(index["manifest_sha256"], hashlib.sha256(manifest_bytes).hexdigest())
            self.assertEqual(verify_provider_generation(stage, "gen-provider-test"), [])

    def test_capability_record_is_qualified_and_support_is_not_selectable(self):
        with tempfile.TemporaryDirectory() as temp:
            stage, _ = ProviderFixture.stage(Path(temp))
            manifest = json.loads((stage / ".aiverse" / "installed.json").read_text(encoding="utf-8"))
            index = json.loads((stage / ".aiverse" / INDEX_FILENAME).read_text(encoding="utf-8"))

            council = next(p for p in manifest["packages"] if p["id"] == "Council")
            helper = next(p for p in manifest["packages"] if p["id"] == "helper")
            self.assertEqual(council["qualified_id"], "aiverse-skills:council")
            self.assertEqual(council["legacy_id"], "Council")
            self.assertEqual(council["name"], "Council")
            self.assertEqual(council["version"], "1.2.3")
            self.assertEqual(council["description"], "Test capability.")
            self.assertEqual(council["digest"]["algorithm"], DIGEST_ALGORITHM)
            self.assertNotIn("qualified_id", helper)
            self.assertEqual([r["id"] for r in index["capabilities"]], ["aiverse-skills:council"])
            record = index["capabilities"][0]
            self.assertEqual(record["visibility"], "shared")
            self.assertEqual(record["package_state"], "valid")
            self.assertNotIn("readiness", record)
            self.assertNotIn("permission", record)
            self.assertNotIn("approval", record)

    def test_portable_digest_uses_path_nul_bytes_nul_and_detects_tampering(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "package"
            package.mkdir()
            (package / "b.txt").write_bytes(b"B")
            (package / "a.txt").write_bytes(b"A")
            expected = hashlib.sha256(b"a.txt\0A\0b.txt\0B\0").hexdigest()
            self.assertEqual(package_digest_v1(package), expected)

            stage, _ = ProviderFixture.stage(Path(temp) / "fixture")
            target = stage / "imported" / "test" / "Council" / "resource.txt"
            target.write_text("tampered\n", encoding="utf-8")
            errors = verify_provider_generation(stage, "gen-provider-test")
            self.assertTrue(any("portable package digest changed" in error for error in errors), errors)

    def test_exact_manifest_bytes_bind_index(self):
        with tempfile.TemporaryDirectory() as temp:
            stage, _ = ProviderFixture.stage(Path(temp))
            manifest_path = stage / ".aiverse" / "installed.json"
            manifest_path.write_bytes(manifest_path.read_bytes() + b"\n")
            errors = verify_provider_generation(stage, "gen-provider-test")
            self.assertTrue(any("manifest_sha256" in error for error in errors), errors)

    def test_generation_mismatch_and_injected_capability_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            stage, _ = ProviderFixture.stage(Path(temp))
            index_path = stage / ".aiverse" / INDEX_FILENAME
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["generation_id"] = "gen-wrong"
            injected = dict(index["capabilities"][0])
            injected["id"] = "aiverse-skills:injected"
            index["capabilities"].append(injected)
            index_path.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            errors = verify_provider_generation(stage, "gen-provider-test")
            self.assertTrue(any("generation does not match" in error for error in errors), errors)
            self.assertTrue(any("uninstalled packages" in error for error in errors), errors)

    def test_stale_index_record_is_rejected_even_with_valid_manifest_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            stage, _ = ProviderFixture.stage(Path(temp))
            index_path = stage / ".aiverse" / INDEX_FILENAME
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["capabilities"][0]["version"] = "9.9.9"
            index_path.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            errors = verify_provider_generation(stage, "gen-provider-test")
            self.assertTrue(any("does not exactly match manifest metadata" in error for error in errors), errors)

    def test_path_escape_and_escaping_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            stage, _ = ProviderFixture.stage(base)
            manifest_path = stage / ".aiverse" / "installed.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["packages"][0]["path"] = "../escape"
            manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            errors = verify_provider_generation(stage, "gen-provider-test")
            self.assertTrue(any("Invalid provider package path" in error for error in errors), errors)

            stage2, _ = ProviderFixture.stage(base / "symlink-fixture", "gen-symlink")
            outside = base / "outside.txt"
            outside.write_text("outside\n", encoding="utf-8")
            link = stage2 / "imported" / "test" / "Council" / "escape-link"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable on this platform")
            with self.assertRaises(RuntimeError):
                package_digest_v1(stage2 / "imported" / "test" / "Council")

    def test_qualified_id_normalization_is_deterministic(self):
        self.assertEqual(qualified_segment("Council"), "council")
        self.assertEqual(qualified_segment("ExtractWisdom"), "extractwisdom")
        self.assertEqual(qualified_segment("some_name"), "some-name")
        with self.assertRaises(RuntimeError):
            qualified_segment("___")

    def test_schema2_immutable_generation_without_index_remains_legacy_valid(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills"
            root.mkdir()
            generation_id = "gen-legacy-schema2"
            stage = base / "stage-legacy"
            package = ProviderFixture.package(stage, "imported/test/sample", name="sample")
            meta = stage / ".aiverse"
            meta.mkdir(parents=True)
            manifest = {
                "schema_version": 2,
                "generation_schema_version": impl.GENERATION_SCHEMA_VERSION,
                "distribution": "AI-Verse-Skills",
                "profile": "test",
                "generation_id": generation_id,
                "generation_digest_sha256": public_impl.generation_content_digest(stage),
                "packages": [{
                    "kind": "employee",
                    "id": "sample",
                    "path": "imported/test/sample",
                    "operators": [],
                    "digest_sha256": impl.digest(package),
                }],
            }
            (meta / "installed.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            impl.commit_stage(root, stage, generation_id)
            impl.activate_generation(root, generation_id)
            self.assertEqual(public_impl.verify_root(root), [])
            pin = public_impl.pin_active_generation(root, impl.digest)
            self.assertEqual(pin.generation_id, generation_id)
            self.assertFalse((pin.generation_path / ".aiverse" / INDEX_FILENAME).exists())


if __name__ == "__main__":
    unittest.main()
