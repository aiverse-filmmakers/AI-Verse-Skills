---
name: dependency-supply-chain-audit
description: "Check a project's third party packages for known security holes, abandoned or suspicious packages and licence problems, then give the least disruptive fix. Use when the user asks 'are my packages safe', 'is it safe to add this package', 'update my dependencies', 'I got a security alert', or before a release."
license: MIT
compatibility: "Needs a terminal in the project folder and network access. Uses the project's own package manager. Some scanners are separate installs and need approval first."
metadata:
  tier: foundation
  owner: ai-verse
---

# Dependency Supply Chain Audit

A dependency is someone else's code your project pulls in. Three failure modes, worst first:

1. **The forced fix.** `audit fix --force` jumps major versions and breaks the app to close a hole it may never have been exposed to.
2. **Panic over unreachable code.** A hole in a part the project never runs is a note, not an emergency.
3. **Judging from memory.** Listing "known vulnerable" packages without running a scanner is guessing.

## Hard rules

1. **Run a real scanner.** Never list vulnerabilities from memory.
2. **Read only by default.** No install, upgrade or lockfile change without a yes. (The lockfile pins the exact version of every package.)
3. **Never `--force`.** One package, or one related group, at a time, with tests and a build after each.
4. **Quote the locked version,** not the range in the manifest.
5. **Present is not the same as exposed.** For every finding say whether the vulnerable part runs in production. If you cannot tell, write "unknown", never "safe".
6. **Check a new package before installing it** (table below).
7. **Do not run a stranger's install scripts** just to look at a package.

## Step 1 — Identify

Find the lockfile; it tells you the package manager. Commands for each are in `references/commands.md`.

## Step 2 — Scan

Run the scanner for production packages first, then everything. Record the tool and its version.

## Step 3 — Triage

| Priority | When |
| --- | --- |
| **Fix now** | Critical or high, runs in production, exposed or unknown, and a fix exists |
| **Fix soon** | High or medium on a production path, or anything being actively exploited |
| **Plan** | Developer only tools, low severity, or no fix yet (note the workaround) |
| **Note and leave** | Not exposed, and you can say exactly why |

For each finding, find out why the package is there at all: asked for directly, or pulled in by another package.

## Step 4 — Fix, least disruptive first

1. A patch or minor version bump of the package you asked for directly.
2. A bump of the parent package that pulls the bad one in.
3. An override that pins the nested package to a fixed version.
4. Replace the package.
5. Accept the risk, in writing, with the reason.

After each change: install, run the tests and the build, run the scanner again. If something breaks, undo that one change and say so.

## Adding a new package

| Check | Bad sign |
| --- | --- |
| The name, letter by letter | One character off a famous name |
| Age and weekly downloads | Days old, or almost nobody uses it |
| Last release | Nothing for 18 months |
| Source repository | Missing, or does not match the package |
| Open security advisories | Any without a fix |
| Install scripts | Runs code at install with no clear reason |
| Licence | None at all. Copyleft licences (GPL, AGPL) need a decision before commercial use |
| What it drags in | Dozens of packages for one small job |
| Is it needed? | The language or framework already does this |

## Output

| Package | Locked version | Issue (id) | Severity | Direct, or via | Runs in production? | Fix | Risk of the fix |
| --- | --- | --- | --- | --- | --- | --- | --- |

```
Scanned with:  tool and version, on <date>
Findings:      fix now 1, fix soon 2, plan 4, noted 3
Changed:       nothing (or exactly what, after approval)
Not checked:
```

## Never

| Never | Instead |
| --- | --- |
| `--force` | One package at a time |
| Upgrade everything to "latest" | The smallest version that fixes it |
| Call it safe because the scanner is quiet | Say what the scanner covers and what it does not |
| Ignore developer only findings completely | Put them under "Plan" |
| Edit the lockfile by hand | Let the package manager write it |
