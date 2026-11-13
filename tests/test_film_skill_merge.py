import json
import unittest
from pathlib import Path
from installer import aiverse_skills_v3

ROOT = Path(__file__).resolve().parents[1]


class FilmSkillMergeTests(unittest.TestCase):
    def test_filmmaker_profile_installs_the_combined_owned_packages(self):
        plan = aiverse_skills_v3.install_plan('filmmaker', Path('/unused-install-root'))
        employee = {item[1]: item for item in plan if item[0] == 'employee'}
        self.assertIn('ai-video-director', employee)
        self.assertIn('director-agent', employee)
        self.assertNotIn('ai-storyboard-director', employee)
        self.assertNotIn('produce-ai-video', employee)
        for name in ('ai-video-director', 'director-agent'):
            source = employee[name][2]
            self.assertTrue((source / 'SKILL.md').is_file())
            self.assertTrue((source / 'LICENSE').is_file())
            provenance = json.loads((source / 'SOURCE.json').read_text())
            self.assertEqual('Apache-2.0', provenance['license'])

    def test_shared_film_references_and_handoff_exist(self):
        merged = ROOT / 'skills/imported/film/ai-video-director'
        for name in ('framing-and-axis.md', 'cinematography-design-engine.md',
                     'production-contract.md', 'shot-design-engine.md', 'video-production.md'):
            self.assertTrue((merged / 'references' / name).is_file(), name)
        director = ROOT / 'skills/imported/film/director-agent'
        self.assertIn('ai-video-director', (director / 'SKILL.md').read_text())
        self.assertFalse((director / 'references/production-storyboard-compiler.md').exists())


if __name__ == '__main__':
    unittest.main()
