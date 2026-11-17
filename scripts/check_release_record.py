"""Release record guard.

Warns when release/component-release.json and the code it points at drift apart
(fails only in strict mode).
The record names an accepted commit ("revision") and a version. This script reads
the version files AT THAT COMMIT with git show and compares them to the record.

Default (warn only): problems print as GitHub warnings and the exit code is 0.
Strict (--strict or RELEASE_GUARD_STRICT=1): exit code 1 when a problem is found.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

RECORD_PATH = "release/component-release.json"
STALE_AFTER_COMMITS = 50
SHA = re.compile(r"^[0-9a-f]{40}$")
SCHEMA = "ai-verse.component-release/v1"


def git(repo, *args):
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8"
        )
    except OSError as exc:
        return 127, "", f"git could not be run ({exc})"
    return proc.returncode, proc.stdout, proc.stderr


def load_record(repo, problems):
    path = Path(repo) / RECORD_PATH
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        problems.append(f"The release record {RECORD_PATH} cannot be read as JSON ({exc}).")
        return None
    if not isinstance(data, dict):
        problems.append("The release record is not a JSON object.")
        return None
    if data.get("schema_version") != SCHEMA:
        problems.append(f"The release record schema_version is not {SCHEMA}.")
    for key in ("version", "revision", "release_status"):
        if not isinstance(data.get(key), str) or not data.get(key):
            problems.append(f"The release record is missing a text field named {key}.")
    if isinstance(data.get("revision"), str) and not SHA.match(data["revision"]):
        problems.append("The release record revision is not a full 40 character commit id.")
    return data


def check_evidence(data, problems):
    evidence = data.get("evidence")
    if not isinstance(evidence, dict):
        problems.append("The release record has no evidence section.")
        return
    seen = {}
    for group in ("ci", "acceptance"):
        entries = evidence.get(group)
        if not isinstance(entries, list):
            problems.append(f"The release record evidence.{group} is not a list.")
            continue
        for entry in entries:
            run_id = entry.get("run_id") if isinstance(entry, dict) else None
            if run_id is None:
                problems.append(f"An evidence.{group} entry has no run_id.")
                continue
            run_id = str(run_id)
            if run_id in seen:
                problems.append(
                    f"CI run {run_id} is listed twice as separate evidence "
                    f"(evidence.{seen[run_id]} and evidence.{group}). "
                    "One run is one proof, not two."
                )
            else:
                seen[run_id] = group


def check_versions_at_commit(repo, revision, version, problems):
    short = revision[:12]

    def show(path):
        code, out, _ = git(repo, "show", f"{revision}:{path}")
        if code != 0:
            problems.append(f"{path} does not exist at the accepted commit {short}.")
            return None
        return out

    text = show("VERSION")
    if text is not None:
        have = text.strip()
        if have != version:
            problems.append(
                f"VERSION at the accepted commit {short} says {have}, "
                f"but the record says {version}."
            )
    text = show("docs/PUBLIC_BETA.md")
    if text is not None:
        m = re.search(r"^\*\*Version:\*\*\s*(\S+)", text, re.M)
        have = m.group(1) if m else None
        if have != version:
            problems.append(
                f"docs/PUBLIC_BETA.md at the accepted commit {short} says version {have}, "
                f"but the record says {version}."
            )
    # The machine readable descriptor takes its version from the VERSION file at run time.
    # If someone hard codes a number there instead, it can drift again.
    text = show("installer/public_beta.py")
    if text is not None:
        reads_file = re.search(r'REPO_ROOT\s*/\s*"VERSION"', text)
        uses_it = re.search(r'"version":\s*version\b', text)
        if not (reads_file and uses_it):
            problems.append(
                f"installer/public_beta.py at the accepted commit {short} no longer builds the "
                "component descriptor version from the VERSION file, so the descriptor may "
                "report a different version than the record."
            )


def check(repo):
    problems, warnings = [], []
    data = load_record(repo, problems)
    if data is None:
        return problems, warnings
    check_evidence(data, problems)
    revision, version = data.get("revision"), data.get("version")
    if not (isinstance(revision, str) and SHA.match(revision) and isinstance(version, str)):
        return problems, warnings
    code, _, _ = git(repo, "cat-file", "-e", f"{revision}^{{commit}}")
    if code != 0:
        problems.append(
            f"The accepted commit {revision} does not exist in this repository "
            "(if this is a CI run, the checkout needs full history)."
        )
        return problems, warnings
    check_versions_at_commit(repo, revision, version, problems)
    code, out, _ = git(repo, "rev-list", "--count", f"{revision}..HEAD")
    if code == 0 and out.strip().isdigit() and int(out) > STALE_AFTER_COMMITS:
        warnings.append(
            f"Heads up: the code is {int(out)} commits ahead of the accepted commit "
            f"{revision[:12]} (limit {STALE_AFTER_COMMITS}). The release record is getting stale "
            "and should be refreshed. This is a warning only."
        )
    return problems, warnings


def strict_requested(args_strict, env):
    return bool(args_strict) or env.get("RELEASE_GUARD_STRICT", "") not in ("", "0", "false")


def run(repo, strict, env=None):
    """Print results. Returns the exit code: nonzero only in strict mode with problems."""
    env = os.environ if env is None else env
    problems, warnings = check(repo)
    for w in warnings:
        print("::warning title=Release record is getting stale::" + w)
    for p in problems:
        print(("::error title=Release record mismatch::" if strict else
               "::warning title=Release record mismatch::") + p)
    lines = ["## Release record guard", ""]
    if problems:
        mode = "strict (blocks CI)" if strict else "warn only (does not block CI)"
        lines.append(f"Mode: {mode}. {len(problems)} problem(s) found:")
        lines += [f"- {p}" for p in problems]
    else:
        lines.append("The release record and the code at its accepted commit agree.")
    lines += [f"- Warning: {w}" for w in warnings]
    summary = env.get("GITHUB_STEP_SUMMARY")
    if summary:
        try:
            with open(summary, "a", encoding="utf-8") as fh:
                fh.write("\n".join(lines) + "\n")
        except OSError:
            pass
    print("\n".join(lines))
    return 1 if (problems and strict) else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when problems are found (also RELEASE_GUARD_STRICT=1)")
    args = parser.parse_args(argv)
    strict = strict_requested(args.strict, os.environ)
    try:
        return run(args.repo, strict, os.environ)
    except Exception as exc:  # the guard must never crash a build in warn mode
        kind = "error" if strict else "warning"
        print(f"::{kind} title=Release record guard crashed::The guard could not finish ({exc!r}).")
        return 1 if strict else 0


if __name__ == "__main__":
    sys.exit(main())
