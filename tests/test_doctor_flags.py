"""doctor --readiness and doctor --target must really check something (FL-22).

The installer (bootstrap.sh) and CI run `doctor --readiness` and trust a zero exit.
Before this fix the public doctor command accepted both flags and then ignored
them, so a missing or badly described chat skill listing still said "healthy".
These tests drive the real command line parser, the same path members use.
"""
import contextlib
import io
import unittest
import unittest.mock

from installer import aiverse_skills as skills
from tests import test_public_beta_learning as Fixtures


class DoctorFlagsAreChecked(unittest.TestCase):
    setUp = Fixtures.PublicBetaLearningTests.setUp
    tearDown = Fixtures.PublicBetaLearningTests.tearDown
    _install_one_foundation = Fixtures.PublicBetaLearningTests._install_one_foundation

    def run_doctor(self, *extra):
        args = skills.parser().parse_args(["--root", str(self.root), "doctor", *extra])
        out = io.StringIO()
        code = 0
        with contextlib.redirect_stdout(out):
            try:
                args.fn(args)
            except SystemExit as stop:
                code = stop.code or 0
        return code, out.getvalue()

    def test_target_folder_without_the_skills_fails(self):
        # An empty chat skills folder lists none of the installed skills, so doctor must fail.
        empty = self.base / "empty-chat-skills"
        empty.mkdir()
        code, out = self.run_doctor("--target", str(empty))
        self.assertNotEqual(code, 0, out)
        self.assertIn("ERROR", out)

    def test_target_folder_with_every_skill_listed_passes(self):
        target = self.base / "chat-skills"
        skills.materialize_adapter(self.root, target, "claude", sync=True)
        code, out = self.run_doctor("--target", str(target))
        self.assertEqual(code, 0, out)
        self.assertIn("Every catalogue skill is listed", out)

    def test_readiness_prints_the_readiness_counts(self):
        code, out = self.run_doctor("--readiness")
        self.assertEqual(code, 0, out)
        self.assertIn("Skills immediately ready:", out)

    def test_readiness_fails_when_readiness_cannot_be_worked_out(self):
        # If the readiness check itself breaks, doctor must say so instead of "healthy".
        # The live implementation module is skills._impl; doctor calls readiness from there.
        def broken(root):
            raise RuntimeError("operator registry unreadable")
        with unittest.mock.patch.object(skills._impl, "readiness", broken):
            code, out = self.run_doctor("--readiness")
        self.assertNotEqual(code, 0, out)
        self.assertIn("readiness", out)


if __name__ == "__main__":
    unittest.main()
