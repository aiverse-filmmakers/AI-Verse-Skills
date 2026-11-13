import hashlib
import json
import re
import unittest
from pathlib import Path
from installer import aiverse_skills_v3

ROOT = Path(__file__).resolve().parents[1]
FILM = ROOT / 'skills/imported/film'
AIV = ROOT / 'skills/imported/ai-verse'


# SHA-256 of private words (a private film title and a teacher's name) that must never
# appear in public skill text. Only the hashes are stored so the words stay out of the repo.
PRIVATE_WORD_HASHES = {
    '3ed51f95cb57323b9cb868117d99bea65eef3ca2b4eafb46468ddf59c3c89c53',
    'ec187a17a1a662a451a5d08f5bcb670f3be7f9fef211cb768d6a4e202b80ec80',
}


def private_words(text):
    words = set(re.findall(r'[a-z]+', text.lower()))
    return {w for w in words if hashlib.sha256(w.encode()).hexdigest() in PRIVATE_WORD_HASHES}


def body(path):
    return (path / 'SKILL.md').read_text()


class FilmmakingChainTests(unittest.TestCase):
    def test_each_skill_names_the_neighbours_it_hands_to(self):
        self.assertIn('higgsfield-acting', body(FILM / 'director-agent'))
        self.assertIn('ai-realism', body(FILM / 'director-agent'))
        director = body(FILM / 'ai-video-director')
        for name in ('director-agent', 'higgsfield-acting', 'ai-realism', 'video-editor'):
            self.assertIn(name, director)
        acting = body(AIV / 'higgsfield-acting')
        for name in ('director-agent', 'ai-video-director', 'ai-realism'):
            self.assertIn(name, acting)
        realism = body(AIV / 'ai-realism')
        for name in ('director-agent', 'ai-video-director', 'higgsfield-acting', 'cinematic-realism-director', 'video-editor'):
            self.assertIn(name, realism)

    def test_contradictions_that_were_decided_stay_fixed(self):
        realism = body(AIV / 'ai-realism')
        acting = body(AIV / 'higgsfield-acting')
        self.assertIn('Ignore the reference', realism)
        self.assertIn('PERFORMANCE', realism)
        self.assertNotIn('catch-light', realism.lower())
        self.assertNotIn('3rd position', realism)
        self.assertIn('Gaze stays engaged', acting)
        self.assertEqual(set(), private_words(acting))

    def test_new_skills_are_registered_and_installed_for_filmmakers(self):
        plan = aiverse_skills_v3.install_plan('filmmaker', Path('/unused-install-root'))
        employee = {item[1]: item for item in plan if item[0] == 'employee'}
        for name in ('ai-realism', 'higgsfield-acting'):
            self.assertIn(name, employee)
            self.assertTrue((employee[name][2] / 'SKILL.md').is_file())
        roles = json.loads((ROOT / 'registry/roles.json').read_text())['roles']
        filmmaker = next(r for r in roles if r['id'] == 'ai-filmmaker')
        self.assertIn('ai-realism', filmmaker['skills'])
        self.assertIn('higgsfield-acting', filmmaker['skills'])

    def test_higgsfield_adapter_accepts_a_user_who_works_in_higgsfield(self):
        text = (AIV / 'cinematic-realism-director/SKILL.md').read_text()
        self.assertIn('working in Higgsfield', text)


if __name__ == '__main__':
    unittest.main()
