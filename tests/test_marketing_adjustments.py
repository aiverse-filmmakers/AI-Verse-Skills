import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKETING = ['copywriting', 'ad-creative', 'content-strategy', 'customer-research',
             'email-sequence', 'seo-audit', 'community-marketing', 'social-content']
BASE = ROOT / 'skills/imported/corey-haines'


class MarketingAdjustmentTests(unittest.TestCase):
    def test_marketing_skills_read_the_project_notes_not_the_shared_file(self):
        for name in MARKETING:
            text = (BASE / name / 'SKILL.md').read_text()
            self.assertNotIn('.agents/product-marketing.md', text, name)
            self.assertIn("this project's marketing notes", text, name)
            self.assertIn('marketing', text.lower())
        ref = (BASE / 'ad-creative/references/motion-video-ads.md').read_text()
        self.assertNotIn('.agents/product-marketing.md', ref)

    def test_setup_interview_lives_in_copywriting(self):
        ref = BASE / 'copywriting/references/marketing-project-setup.md'
        self.assertTrue(ref.is_file())
        text = ref.read_text()
        for section in ('Audience', 'Voice', 'Proof', 'Goals'):
            self.assertIn(section, text)
        self.assertIn('Saved for this project only', text)

    def test_product_marketing_context_is_gone_and_redirects(self):
        for name in ('skills.json', 'packages.json', 'profiles.json', 'roles.json'):
            self.assertNotIn('product-marketing-context', (ROOT / 'registry' / name).read_text(), name)
        aliases = json.loads((ROOT / 'registry/aliases.json').read_text())['legacy_user_aliases']
        self.assertEqual('copywriting', aliases['product-marketing-context'])
        self.assertEqual('copywriting', aliases['product-marketing'])


if __name__ == '__main__':
    unittest.main()
