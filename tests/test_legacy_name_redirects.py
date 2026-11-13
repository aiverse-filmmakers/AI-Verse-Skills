import json
import unittest
from pathlib import Path
from installer import aiverse_skills_v3

ROOT = Path(__file__).resolve().parents[1]
RETIRED = {
    'ai-storyboard-director': 'ai-video-director',
    'produce-ai-video': 'ai-video-director',
    'meeting-action-items': 'action-items',
    'document-to-action-items': 'action-items',
}


class LegacyNameRedirectTests(unittest.TestCase):
    def test_retired_names_resolve_to_their_replacements(self):
        for old, new in RETIRED.items():
            self.assertEqual(new, aiverse_skills_v3.resolve_package_alias(old), old)

    def test_current_and_unknown_names_are_left_alone(self):
        for name in ('ai-video-director', 'action-items', 'no-such-skill', '', None):
            self.assertEqual(name, aiverse_skills_v3.resolve_package_alias(name))

    def test_every_alias_target_is_a_real_catalogue_skill(self):
        aliases = json.loads((ROOT / 'registry/aliases.json').read_text())['legacy_user_aliases']
        registry = (ROOT / 'registry/skills.json').read_text()
        for old, new in aliases.items():
            self.assertIn(f'"id": "{new}"', registry, f'{old} -> {new}')

    def test_retired_names_are_not_in_the_live_catalogue(self):
        plan = aiverse_skills_v3.install_plan('filmmaker', Path('/unused-install-root'))
        live = {item[1] for item in plan}
        for old in RETIRED:
            self.assertNotIn(old, live)


if __name__ == '__main__':
    unittest.main()
