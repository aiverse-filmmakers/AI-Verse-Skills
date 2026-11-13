---
name: transactional-refactor
description: "Restructure existing code across several files without changing what it does: map it first, change it in small checked steps, and keep a way back at every step. Use when the user asks to rename something everywhere, split a large file, move or reorganise code, remove duplication or tidy a module, or wants to understand how a codebase fits together before changing it."
license: MIT
compatibility: "Needs git and a terminal. Works best when the project has tests; without them it says so and offers to add a few first."
metadata:
  tier: foundation
  owner: ai-verse
---

# Transactional Refactor

A refactor changes the shape of code and nothing about what it does. Treat it like moving house one box at a time, checking nothing broke after each box.

Three failure modes, worst first:

1. **The big bang.** Everything changed at once, the checks fail, and nobody can tell which change did it.
2. **A behaviour change smuggled in as tidying.** "While I was there, I also fixed" is how a refactor ships a bug.
3. **The half finished rename.** The code uses the new name; a setting, a text string and the documentation still use the old one.

## Gate

- **Uncommitted changes in the project?** Stop. Ask the user to save them first.
- **No tests and no way to run the code?** Say so before starting. A refactor with no check is a rewrite on faith. Offer to add a few tests that record what the code does today, then refactor.
- **Checks already failing?** Record which ones, so they are not blamed on the refactor.

## Hard rules

1. **Behaviour stays the same.** A bug you find is written down, not fixed here. It gets its own change afterwards.
2. **Work on a branch,** never directly on the main one.
3. **One kind of change per step:** a rename, or a move, or an extraction. Never two.
4. **One commit per step,** after its checks pass. Each commit is a checkpoint you can return to.
5. **A failed check means undo that step.** Go back to the last checkpoint and take a smaller step. Never pile a fix on top of a broken step.
6. **No drive by changes:** no reformatting, no package upgrades, no "while I am here".
7. **Names other things depend on need a plan or a yes:** web addresses, exported functions, database columns, setting names, files that are linked from outside.

## Step 1 — Map (read only)

Read `references/codebase-map.md` and produce the map before touching anything: every place the code is defined, used, tested, configured and mentioned. The map decides the size of the job.

## Step 2 — Plan

List the steps in order. Show the plan first when it has more than five steps or touches a name from rule 7.

| # | Step | Files | Check after |
| --- | --- | --- | --- |

**The order that never breaks anything:** add the new beside the old, move the users across one group at a time, then remove the old. Each stage leaves the code working.

## Step 3 — The loop

For each step: change, run the checks, commit with a message that names the step, move on.

| Move | How |
| --- | --- |
| Rename | Use the language's rename tool when there is one. Then search plain text for leftovers: strings, comments, settings, documentation, test names |
| Move a file | `git mv`, so its history follows. Then fix what imports it |
| Split a file | Move one piece at a time. Keep the old file passing things through until every user is updated |
| Extract a function | Copy the lines out, call the copy, check, then delete the original lines |
| Remove unused code | Prove it is unused, including uses built from text at run time. Its own commit |

## Step 4 — Finish

1. Run every check once more.
2. Read the whole difference from the starting point, top to bottom.
3. Search for the old name one last time.
4. Report.

```
Goal:              what changed in the structure
Unchanged:         the behaviour, and how that was checked
Steps:             1. step (commit abc1234), checks passed
Kept on purpose:   old names still in place, and why
Found, not fixed:  bugs or oddities noticed on the way
Undo:              the commit to return to, or the range to revert
Not verified:
```

## Never

| Never | Instead |
| --- | --- |
| Change twenty files, then run the checks | One step, check, commit |
| Fix a bug in the middle of a refactor | Note it; separate change afterwards |
| Push on after a failed check | Back to the last checkpoint, smaller step |
| Trust the rename tool alone | Also search plain text |
| Reformat files you are moving | Move only; format in its own commit, if asked |
| Rename a public name silently | Keep the old one working, or get a yes |

## Reference files

| File | Load when |
| --- | --- |
| `references/codebase-map.md` | Step 1, and whenever the user only wants to understand how a codebase fits together |

## Project adjustments

If the current project has adjustments for this skill (its check commands, branch naming, names that must never change), apply them. Where they disagree with these instructions, the project's adjustments win.
