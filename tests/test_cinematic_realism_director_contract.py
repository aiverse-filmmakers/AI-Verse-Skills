import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from installer.aiverse_skills_v3 import digest, materialize_adapter, verify_adapter_target
from installer.generation_lifecycle import (
    GENERATION_SCHEMA_VERSION,
    activate_generation,
    commit_stage,
    generation_content_digest,
    verify_generation,
)


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "imported" / "ai-verse" / "cinematic-realism-director"


class CinematicRealismDirectorContractTests(unittest.TestCase):
    def test_first_party_package_contract_is_complete(self):
        self.assertTrue(PACKAGE.is_dir())

        required = (
            "SKILL.md",
            "README.md",
            "aiverse.skill.yaml",
            "REPOSITORY_INTEGRATION.md",
            "references/INDEX.md",
            "references/reality-gate.md",
            "references/routing.md",
            "references/locks.md",
            "references/host-action-policy.md",
            "adapters/generic.md",
            "adapters/openai.md",
            "adapters/gemini.md",
            "adapters/seedream.md",
            "adapters/flux.md",
            "adapters/magnific.md",
            "adapters/higgsfield-soul-cinema.md",
            "schemas/cinematic-shot-spec.schema.json",
            "schemas/realism-diagnosis.schema.json",
            "schemas/reference-dna.schema.json",
            "evals/routing.json",
            "evals/shot-design.json",
            "evals/expert-locks.json",
            "evals/realism-repair.json",
            "evals/reference-match.json",
            "evals/adapter-behavior.json",
            "evals/anti-cliche.json",
            "evals/physical-plausibility.json",
            "evals/adversarial.json",
            "evals/regression.json",
            "evals/benchmark-matrix.md",
        )
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((PACKAGE / relative).is_file(), relative)

        skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: cinematic-realism-director\n"))
        for heading in (
            "## When to Use",
            "## Inputs",
            "## Success Contract",
            "## Constraints",
            "## Procedure",
            "## References",
            "## Pitfalls",
            "## Verification",
            "## Output",
        ):
            self.assertIn(heading, skill)

        manifest = (PACKAGE / "aiverse.skill.yaml").read_text(encoding="utf-8")
        for marker in (
            "contract: aiverse-skill-v1",
            "name: cinematic-realism-director",
            "category: film-media",
            "risk: low",
            "- workspace.read",
            "network: conditional",
            "secrets: []",
            "required: true",
            "class: human",
            "autonomous_mutation: false",
        ):
            self.assertIn(marker, manifest)

        # The sidecar describes possible host effects; it does not grant a provider,
        # secret, image service, or executable dependency.
        self.assertIn("toolpacks: []", manifest)
        self.assertNotIn("process.exec", manifest)

        for schema in (PACKAGE / "schemas").glob("*.json"):
            with self.subTest(schema=schema.name):
                parsed = json.loads(schema.read_text(encoding="utf-8"))
                self.assertIsInstance(parsed, dict)

        for eval_file in (PACKAGE / "evals").glob("*.json"):
            with self.subTest(eval=eval_file.name):
                parsed = json.loads(eval_file.read_text(encoding="utf-8"))
                self.assertIsInstance(parsed, dict)

    def test_ranked_registry_is_deliberately_not_mutated_by_v1_package_integration(self):
        skills = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry" / "packages.json").read_text(encoding="utf-8"))
        profiles = json.loads((ROOT / "registry" / "profiles.json").read_text(encoding="utf-8"))

        self.assertEqual(skills["counts"], {"foundation": 20, "employee": 100, "total": 120})
        self.assertEqual(packages["counts"]["foundation"], 20)
        self.assertEqual(packages["counts"]["employee"], 100)
        self.assertEqual(packages["counts"]["canonical_total"], 120)

        employee_ids = {item["id"] for item in skills["employee"]}
        package_ids = {
            item["id"]
            for source in packages["sources"].values()
            for item in source.get("packages", [])
        }
        self.assertNotIn("cinematic-realism-director", employee_ids)
        self.assertNotIn("cinematic-realism-director", package_ids)
        self.assertNotIn("cinematic-realism-director", profiles["profiles"]["full"]["employee_skills"])

        integration = (PACKAGE / "REPOSITORY_INTEGRATION.md").read_text(encoding="utf-8")
        self.assertIn("first-party-native", integration)
        self.assertIn("Ranked-catalog promotion", integration)
        self.assertIn("full-profile automatic installation  NO", integration)

        trust = json.loads((ROOT / "registry" / "trust-policy.json").read_text(encoding="utf-8"))
        first_party = trust["sources"]["aiverse-filmmakers/AI-Verse-Skills"]
        self.assertEqual(first_party["trust"], "first-party")
        self.assertEqual(first_party["ownership"], "first_party")
        self.assertTrue(first_party["vendoring_allowed"])
        self.assertFalse(first_party["auto_mutation"])

    def test_package_survives_isolated_standalone_copy(self):
        with tempfile.TemporaryDirectory() as temp:
            isolated = Path(temp) / "cinematic-realism-director"
            shutil.copytree(PACKAGE, isolated, symlinks=True)

            # Standalone package must not depend on symlinked repo state.
            symlinks = [path for path in isolated.rglob("*") if path.is_symlink()]
            self.assertEqual(symlinks, [])

            skill = (isolated / "SKILL.md").read_text(encoding="utf-8")
            index = (isolated / "references" / "INDEX.md").read_text(encoding="utf-8")

            # Every package-local runtime path named by SKILL.md must resolve after
            # copying only this directory out of the repository.
            refs = set(
                re.findall(
                    r"(?:(?:references|adapters|schemas|examples)/[A-Za-z0-9._/-]+)",
                    skill,
                )
            )
            self.assertGreater(len(refs), 10)
            for relative in refs:
                relative = relative.rstrip(".,;:)")
                with self.subTest(relative=relative):
                    self.assertTrue((isolated / relative).exists(), relative)

            self.assertNotIn("../", skill)
            self.assertNotIn("../", index)

            # Core structured artifacts remain readable without importing any
            # repository module, AI-Verse OS, MCP, or provider SDK.
            for relative in (
                "schemas/cinematic-shot-spec.schema.json",
                "schemas/realism-diagnosis.schema.json",
                "schemas/reference-dna.schema.json",
                "evals/routing.json",
                "evals/regression.json",
            ):
                parsed = json.loads((isolated / relative).read_text(encoding="utf-8"))
                self.assertIsInstance(parsed, dict)

            self.assertTrue((isolated / "adapters" / "generic.md").is_file())
            self.assertTrue((isolated / "references" / "workflows" / "auto-direct.md").is_file())
            self.assertTrue((isolated / "references" / "reality-gate.md").is_file())

    def test_complete_package_survives_supported_runtime_adapter_materialization(self):
        runtimes = ("agent-skills", "claude", "codex", "hermes", "openclaw", "gemini")

        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skills-install"
            root.mkdir()
            generation_id = "cinematic-v1-test"
            stage = base / "stage"
            staged_package = stage / "imported" / "ai-verse" / "cinematic-realism-director"
            staged_package.parent.mkdir(parents=True)
            shutil.copytree(PACKAGE, staged_package)

            package_digest = digest(staged_package)
            meta = stage / ".aiverse"
            meta.mkdir(parents=True)
            manifest = {
                "schema_version": 2,
                "generation_schema_version": GENERATION_SCHEMA_VERSION,
                "distribution": "AI-Verse-Skills",
                "profile": "cinematic-test",
                "generation_id": generation_id,
                "generation_digest_sha256": generation_content_digest(stage),
                "packages": [
                    {
                        "kind": "employee",
                        "id": "cinematic-realism-director",
                        "path": "imported/ai-verse/cinematic-realism-director",
                        "source_repo": "aiverse-filmmakers/AI-Verse-Skills",
                        "source_commit": None,
                        "operators": [],
                        "digest_sha256": package_digest,
                    }
                ],
            }
            (meta / "installed.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

            commit_stage(root, stage, generation_id)
            self.assertEqual(verify_generation(root, generation_id, digest), [])
            activate_generation(root, generation_id)

            for runtime in runtimes:
                with self.subTest(runtime=runtime):
                    target = base / f"{runtime}-skills"
                    exposed = materialize_adapter(
                        root,
                        target,
                        runtime,
                        prefer_copy=True,
                    )
                    package_record = next(
                        item
                        for item in exposed["packages"]
                        if item["id"] == "cinematic-realism-director"
                    )
                    self.assertEqual(package_record["mode"], "copy")
                    self.assertEqual(exposed["generation_id"], generation_id)
                    self.assertEqual(verify_adapter_target(root, target), [])

                    copied = target / "cinematic-realism-director"
                    self.assertEqual(digest(copied), package_digest)
                    self.assertEqual(
                        (copied / "SKILL.md").read_text(encoding="utf-8"),
                        (PACKAGE / "SKILL.md").read_text(encoding="utf-8"),
                    )
                    for relative in (
                        "references/reality-gate.md",
                        "references/INDEX.md",
                        "adapters/generic.md",
                        "schemas/cinematic-shot-spec.schema.json",
                        "examples/beginner-auto.md",
                        "evals/regression.json",
                    ):
                        self.assertTrue((copied / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
