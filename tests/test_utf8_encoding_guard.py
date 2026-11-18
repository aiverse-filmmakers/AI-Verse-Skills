"""Guard: text mode file and subprocess calls must name their encoding.

Without an explicit encoding, Python uses the machine's own code page. On
Windows that turns Romanian and other accented letters into garbage or a
crash. This test reads every Python file in the repository and fails when a
text mode open(), read_text(), write_text() or text mode subprocess call does
not say encoding="utf-8" (or another explicit encoding).
"""
import ast
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBPROCESS_FUNCS = {"run", "Popen", "check_output", "check_call", "call"}


def _kw(call, name):
    for k in call.keywords:
        if k.arg == name:
            return k
    return None


def _const_true(node):
    return isinstance(node, ast.Constant) and bool(node.value) is True


def _is_bare_text_call(call):
    """True when this call opens text without an explicit encoding."""
    if _kw(call, "encoding") is not None or any(k.arg is None for k in call.keywords):
        return False
    f = call.func
    if isinstance(f, ast.Name) and f.id == "open" or (
        isinstance(f, ast.Attribute) and f.attr == "open"
        and isinstance(f.value, ast.Name) and f.value.id in {"io", "codecs"}
    ):
        mode = call.args[1] if len(call.args) > 1 else None
        if mode is None:
            kw = _kw(call, "mode")
            mode = kw.value if kw else None
        if mode is None:
            return True
        if isinstance(mode, ast.Constant) and isinstance(mode.value, str):
            return "b" not in mode.value
        return False
    if isinstance(f, ast.Attribute):
        if f.attr == "read_text":
            return not call.args
        if f.attr == "write_text":
            return len(call.args) < 2
        if (
            f.attr in SUBPROCESS_FUNCS
            and isinstance(f.value, ast.Name)
            and f.value.id == "subprocess"
        ):
            for name in ("text", "universal_newlines"):
                kw = _kw(call, name)
                if kw is not None and _const_true(kw.value):
                    return True
    return False


def bare_text_calls(source):
    """Return (line, end_line, end_col, call) for each offending call."""
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call) and _is_bare_text_call(node):
            found.append((node.lineno, node.end_lineno, node.end_col_offset))
    return sorted(found)


def tracked_python_files():
    out = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.py"],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout.split("\n")
    return [ROOT / p for p in out if p]


class Utf8EncodingGuard(unittest.TestCase):
    def test_scanner_flags_bare_calls(self):
        bad = (
            'open("a")\n'
            'p.read_text()\n'
            'p.write_text("x")\n'
            'subprocess.run(["x"], text=True)\n'
        )
        self.assertEqual(len(bare_text_calls(bad)), 4)

    def test_scanner_accepts_explicit_or_binary(self):
        good = (
            'open("a", encoding="utf-8")\n'
            'open("a", "rb")\n'
            'p.read_text(encoding="utf-8")\n'
            'p.write_text("x", encoding="utf-8")\n'
            'subprocess.run(["x"], capture_output=True)\n'
            'subprocess.run(["x"], text=True, encoding="utf-8")\n'
            'os.open("a", 0)\n'
        )
        self.assertEqual(bare_text_calls(good), [])

    def test_no_bare_text_mode_calls_in_repository(self):
        problems = []
        for path in tracked_python_files():
            try:
                source = path.read_text(encoding="utf-8")
                hits = bare_text_calls(source)
            except (SyntaxError, UnicodeDecodeError):
                continue
            for line, _, _ in hits:
                problems.append(f"{path.relative_to(ROOT)}:{line}")
        self.assertEqual(
            problems, [],
            'Add encoding="utf-8" to these calls:\n' + "\n".join(problems),
        )


if __name__ == "__main__":
    unittest.main()
