"""Every catalogue skill is stored in the repo, described well, and exposed to chats.

Chats only trigger a skill they can see in their skill list (name and description).
These tests make sure no skill can be added, or left behind, unlisted or badly described.
"""
import json
import tempfile
import unittest
from pathlib import Path

from installer.aiverse_skills_v3 import (
    digest,
    expose_to_chat_folders,
    load_chat_folders,
    parse_expose,
    listing_problems,
    materialize_adapter,
    read_skill_listing,
    verify_adapter_target,
)
from installer.generation_lifecycle import (
    GENERATION_SCHEMA_VERSION,
    activate_generation,
    commit_stage,
    generation_content_digest,
    verify_generation,
)

ROOT = Path(__file__).resolve().parents[1]


def _catalogue():
    skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
    return skills["foundation"] + skills["employee"]


def _skill_md_for(skill_id):
    found = sorted((ROOT / "skills").glob(f"**/{skill_id}/SKILL.md"))
    return found


class CatalogueIsCompleteAndListable(unittest.TestCase):
    def test_every_catalogue_skill_is_stored_in_the_repo(self):
        for item in _catalogue():
            with self.subTest(skill=item["id"]):
                self.assertIn(item["state"], {"vendored", "specified"}, "skill would be fetched from outside at install")
                self.assertEqual(len(_skill_md_for(item["id"])), 1, "exactly one SKILL.md must exist")

    def test_every_catalogue_skill_has_a_listable_description(self):
        problems = []
        for item in _catalogue():
            found = _skill_md_for(item["id"])
            if len(found) == 1:
                problems.extend(listing_problems(found[0], item["id"]))
        self.assertEqual(problems, [])

    def test_header_reader_handles_folded_and_plain_descriptions(self):
        with tempfile.TemporaryDirectory() as temp:
            plain = Path(temp) / "a.md"
            plain.write_text('---\nname: a\ndescription: "Use when you need X."\n---\nbody\n', encoding="utf-8")
            folded = Path(temp) / "b.md"
            folded.write_text("---\nname: b\ndescription: >\n  First line.\n  Second line.\nlicense: MIT\n---\nbody\n", encoding="utf-8")
            self.assertEqual(read_skill_listing(plain), ("a", "Use when you need X."))
            self.assertEqual(read_skill_listing(folded), ("b", "First line. Second line."))

    def test_badly_described_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            md = Path(temp) / "SKILL.md"
            md.write_text("---\nname: thing\ndescription: A tool.\n---\n", encoding="utf-8")
            self.assertTrue(listing_problems(md, "thing"))
            md.write_text("---\nname: other\ndescription: Use when the user asks to turn rough notes into a clear written plan.\n---\n", encoding="utf-8")
            self.assertTrue(any("expected" in p for p in listing_problems(md, "thing")))
            md.write_text("---\nname: thing\ndescription: Use when the user asks to turn rough notes into a clear written plan.\n---\n", encoding="utf-8")
            self.assertEqual(listing_problems(md, "thing"), [])


def _commit(root, base, generation_id, skills):
    """Commit a generation holding the given {id: description} skills."""
    stage = base / f"stage-{generation_id}"
    packages = []
    for skill_id, description in skills.items():
        package = stage / "imported" / "test" / skill_id
        package.mkdir(parents=True)
        (package / "SKILL.md").write_text(
            f"---\nname: {skill_id}\ndescription: {description}\n---\nbody-{skill_id}\n", encoding="utf-8"
        )
        packages.append({
            "kind": "employee", "id": skill_id, "path": f"imported/test/{skill_id}",
            "operators": [], "digest_sha256": digest(package),
        })
    meta = stage / ".aiverse"
    meta.mkdir(parents=True)
    manifest = {
        "schema_version": 2, "generation_schema_version": GENERATION_SCHEMA_VERSION,
        "distribution": "AI-Verse-Skills", "profile": "test", "generation_id": generation_id,
        "generation_digest_sha256": generation_content_digest(stage), "packages": packages,
    }
    (meta / "installed.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    commit_stage(root, stage, generation_id)
    assert not verify_generation(root, generation_id, digest)
    activate_generation(root, generation_id)


GOOD = "Use when the user asks for {x}. It does {x} step by step and explains each choice."


class ExposeEveryNewSkill(unittest.TestCase):
    def _setup(self, temp):
        base = Path(temp)
        root, target = base / "skills", base / "chat-skills"
        root.mkdir()
        return base, root, target

    def test_sync_lists_every_skill_and_a_new_skill_appears_on_the_next_update(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha"), "beta": GOOD.format(x="beta")})
            m1 = materialize_adapter(root, target, "claude", sync=True)
            self.assertEqual({p["id"] for p in m1["packages"]}, {"alpha", "beta"})
            self.assertEqual(verify_adapter_target(root, target, require_complete=True), [])

            _commit(root, base, "gen-2", {"alpha": GOOD.format(x="alpha"), "beta": GOOD.format(x="beta"),
                                          "gamma": GOOD.format(x="gamma")})
            self.assertTrue(any("stale" in e for e in verify_adapter_target(root, target, require_complete=True)))
            m2 = materialize_adapter(root, target, "claude", sync=True)
            self.assertEqual({p["id"] for p in m2["packages"]}, {"alpha", "beta", "gamma"})
            self.assertTrue((target / "gamma" / "SKILL.md").is_file())
            self.assertEqual(verify_adapter_target(root, target, require_complete=True), [])

    def test_sync_removes_retired_skills_but_never_a_folder_it_did_not_create(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            mine = target / "my-own-skill"
            mine.mkdir(parents=True)
            (mine / "SKILL.md").write_text("mine", encoding="utf-8")
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha"), "beta": GOOD.format(x="beta")})
            materialize_adapter(root, target, "claude", sync=True)
            _commit(root, base, "gen-2", {"alpha": GOOD.format(x="alpha")})
            m = materialize_adapter(root, target, "claude", sync=True)
            self.assertEqual(m["pruned"], ["beta"])
            self.assertFalse((target / "beta").exists())
            self.assertEqual((mine / "SKILL.md").read_text(encoding="utf-8"), "mine")

    def test_sync_does_not_overwrite_a_same_name_skill_it_did_not_create(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            foreign = target / "alpha"
            foreign.mkdir(parents=True)
            (foreign / "SKILL.md").write_text("somebody else's alpha", encoding="utf-8")
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha"), "beta": GOOD.format(x="beta")})
            m = materialize_adapter(root, target, "claude", sync=True)
            self.assertEqual([c["id"] for c in m["skipped_collisions"]], ["alpha"])
            self.assertEqual((foreign / "SKILL.md").read_text(encoding="utf-8"), "somebody else's alpha")
            errors = verify_adapter_target(root, target, require_complete=True)
            self.assertTrue(any("alpha" in e and "same name" in e for e in errors))

    def test_doctor_style_check_flags_a_skill_with_no_usable_description(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha"), "beta": "A tool."})
            materialize_adapter(root, target, "claude", sync=True)
            errors = verify_adapter_target(root, target, require_complete=True)
            self.assertTrue(any(e.startswith("beta:") for e in errors))
            self.assertFalse(any(e.startswith("alpha:") for e in errors))


class UpdateKeepsChatFoldersListed(ExposeEveryNewSkill):
    def test_parse_expose_reads_pairs_and_defaults(self):
        self.assertEqual(parse_expose(["claude=/a", "codex=/b"], False), {"claude": "/a", "codex": "/b"})
        defaults = parse_expose([], True)
        self.assertEqual(set(defaults), {"claude", "codex"})
        self.assertEqual(parse_expose(["claude=/mine"], True)["claude"], "/mine")
        with self.assertRaises(SystemExit):
            parse_expose(["no-equals-sign"], False)

    def test_folders_are_remembered_and_a_later_update_relists_new_skills(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha")})
            self.assertEqual(expose_to_chat_folders(root, {"claude": str(target)}), [])
            self.assertEqual(load_chat_folders(root), {"claude": str(target)})
            _commit(root, base, "gen-2", {"alpha": GOOD.format(x="alpha"), "beta": GOOD.format(x="beta")})
            self.assertEqual(expose_to_chat_folders(root, load_chat_folders(root)), [])
            self.assertTrue((target / "beta" / "SKILL.md").is_file())

    def test_a_badly_described_skill_is_reported_as_a_problem(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            _commit(root, base, "gen-1", {"alpha": GOOD.format(x="alpha"), "beta": "A tool."})
            problems = expose_to_chat_folders(root, {"claude": str(target)})
            self.assertTrue(any("beta" in p for p in problems))

    def test_no_folders_means_nothing_happens(self):
        with tempfile.TemporaryDirectory() as temp:
            base, root, target = self._setup(temp)
            self.assertEqual(expose_to_chat_folders(root, {}), [])
            self.assertEqual(load_chat_folders(root), {})


if __name__ == "__main__":
    unittest.main()
