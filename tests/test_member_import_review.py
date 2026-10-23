import json
import tempfile
import unittest
from pathlib import Path
from installer import member_library as library

PORTABLE = dict(library.PORTABILITY)

class MemberImportReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.root=self.base/'library';self.package=self.base/'package';self.package.mkdir()
        (self.package/'SKILL.md').write_text('---\nname: method\ndescription: >-\n  A portable method\n  with a folded description.\n---\nUse explicit inputs.\n',encoding='utf-8')
        (self.package/'mocking.md').write_text('Example: const client = new StripeClient(process.env.STRIPE_KEY);\n',encoding='utf-8')

    def review(self):
        inspected=library._package(self.package,inspect_only=True)
        return {'source_revision':inspected['source_revision'],'findings':[{'path':f['path'],'code':f['code']} for f in inspected['scan']['findings']], 'reviewer':'maintainer-test','reason':'Reviewed inert documentation example; no credentials or execution permission granted.'}

    def test_review_is_explicit_exact_and_preserved(self):
        with self.assertRaisesRegex(RuntimeError,'admission requires review'):library.plan_import(self.root,self.package,admission=PORTABLE)
        review=self.review();plan=library.plan_import(self.root,self.package,admission=PORTABLE,security_review=review)
        self.assertFalse(self.root.exists());self.assertEqual(plan['metadata']['description'],'A portable method with a folded description.')
        first=library.apply_import(self.root,self.package,plan=plan,admission=PORTABLE,security_review=review)
        again=library.apply_import(self.root,self.package,plan=plan,admission=PORTABLE,security_review=review)
        self.assertEqual(first['id'],again['id']);self.assertTrue(library.verify(self.root)['ok'])
        record=library.read_index(self.root)['skills'][first['id']]['revisions'][first['revision']]
        self.assertEqual(record['security_review'],review)
        self.assertTrue(library.select_revision(self.root,first['id'],first['revision'],expected_index=library.index_digest(self.root)))

    def test_missing_or_changed_finding_refuses(self):
        review=self.review();review['findings']=[]
        with self.assertRaisesRegex(RuntimeError,'every exact finding'):library.plan_import(self.root,self.package,admission=PORTABLE,security_review=review)

    def test_source_change_invalidates_review(self):
        review=self.review();(self.package/'mocking.md').write_text('changed process.env.STRIPE_KEY',encoding='utf-8')
        with self.assertRaisesRegex(RuntimeError,'exact package revision'):library.plan_import(self.root,self.package,admission=PORTABLE,security_review=review)

    def test_denied_material_cannot_be_waived(self):
        review=self.review();(self.package/'key.txt').write_text('-----BEGIN PRIVATE KEY-----\n',encoding='utf-8')
        review['source_revision']=library._package(self.package,inspect_only=True)['source_revision']
        with self.assertRaisesRegex(RuntimeError,'cannot waive'):library.plan_import(self.root,self.package,admission=PORTABLE,security_review=review)

    def test_review_cannot_be_removed_at_apply(self):
        review=self.review();plan=library.plan_import(self.root,self.package,admission=PORTABLE,security_review=review)
        with self.assertRaises(RuntimeError):library.apply_import(self.root,self.package,plan=plan,admission=PORTABLE)

    def test_literal_description_has_bounded_block_semantics(self):
        (self.package/'SKILL.md').write_text('---\nname: method\ndescription: |-\n  First line.\n  Second line.\nversion: 1\n---\nBody.\n',encoding='utf-8')
        self.assertEqual(library.skill_metadata(self.package/'SKILL.md')['description'],'First line.\nSecond line.')

    def test_incomplete_scan_cannot_be_waived(self):
        review=self.review();review['findings']=[{'path':'large.md','code':'text-scan-budget'}]
        scan={'status':'review-required','findings':[{'severity':'review','path':'large.md','code':'text-scan-budget'}]}
        with self.assertRaisesRegex(RuntimeError,'cannot waive'):library._review_receipt(review,review['source_revision'],scan)

    def test_scan_covers_the_full_bounded_member_package(self):
        # Each text file is below the existing1MiB per-file bound. A credential
        # beyond the scanner's old2MB default still has to be denied.
        (self.package/'a.md').write_text('a'*900_000,encoding='utf-8')
        (self.package/'b.md').write_text('b'*900_000,encoding='utf-8')
        (self.package/'c.md').write_text('c'*900_000+'\n-----BEGIN PRIVATE KEY-----',encoding='utf-8')
        inspected=library._package(self.package,inspect_only=True)
        self.assertEqual(inspected['scan']['status'],'deny')
        self.assertNotIn('text-scan-budget',{x['code'] for x in inspected['scan']['findings']})
