import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'skills/imported/adobe/after-effects-assistant/scripts/runner.sh'


class AfterEffectsVersionDetectionTests(unittest.TestCase):
    def detect(self, directory):
        source = RUNNER.read_text(encoding='utf-8')
        function = source[source.index('detect_ae_versions() {'):source.index('\nAE_APP=$(get_cached_version)')]
        result = subprocess.run(
            ['/bin/bash', '-c', function + '\ndetect_ae_versions "$1"\nprintf "%s\\n" "${#VERSIONS[@]}" "${VERSIONS[@]}"', 'test', str(directory)],
            check=True, capture_output=True, text=True,
        )
        return result.stdout.splitlines()

    def test_empty_single_and_multiple_versions_preserve_names(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertEqual(['0'], self.detect(root))
            (root / 'Adobe After Effects 2025').mkdir()
            self.assertEqual(['1', 'Adobe After Effects 2025'], self.detect(root))
            (root / 'Adobe After Effects 2026').mkdir()
            self.assertEqual(['2', 'Adobe After Effects 2025', 'Adobe After Effects 2026'], self.detect(root))


if __name__ == '__main__':
    unittest.main()
