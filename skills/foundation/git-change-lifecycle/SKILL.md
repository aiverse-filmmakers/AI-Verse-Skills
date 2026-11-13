---
name: git-change-lifecycle
description: "Save, share and ship code changes with git without losing anyone's work: check the state, branch, commit, open a pull request, resolve conflicts, undo safely, and confirm a release is ready. Use when the user says 'save my work', 'commit this', 'open a pull request', 'I have a merge conflict', 'undo my last change', 'is this ready to release' or 'ship it'."
license: MIT
compatibility: "Needs git. Pull requests need the GitHub CLI (gh) or the host's website, signed in by the user."
metadata:
  tier: foundation
  owner: ai-verse
---

# Git Change Lifecycle

Git records versions of a project's files. Used carelessly, it is also the fastest way to destroy an afternoon's work.

Three failure modes, worst first:

1. **Destroying work that was never saved.** `reset --hard`, `checkout .`, `clean` and `stash drop` delete it with no way back.
2. **Pushing, or rewriting shared history, without asking.** Other people see it at once, and a forced push can erase their work.
3. **Committing everything in sight.** `git add .` sweeps in passwords, build output and huge media files.

## Hard rules

1. **Look before you act.** `git status` and the current branch, first, every time.
2. **Never discard work you did not create in this session.** Unsaved changes you do not recognise: ask. No `reset --hard`, `checkout -- .`, `clean -fd` or `stash drop` without an explicit yes.
3. **Ask before anything others can see or that cannot be undone:** push, pull request, merge, tag, release, deleting a branch.
4. **Never commit straight onto the main branch.** Make a branch first.
5. **Stage files by name,** and read `git diff --staged` before every commit. No secrets, no build output, no large media.
6. **Never force push a shared branch.** On your own branch only, with `--force-with-lease`, after a yes.
7. **Never skip the project's checks** (`--no-verify`) and never change git's settings.
8. **Never rewrite history that has been pushed.** Undo with a new commit.

## Step 1 — Read the state

```bash
git status --short --branch
git log --oneline -5
git remote -v
git stash list
```

Also look for the project's own rules: `CONTRIBUTING.md`, a pull request template, the names of existing branches.

| What you find | Do |
| --- | --- |
| Clean, on the main branch | Make a branch, then work |
| Unsaved changes that are this task | Make a branch, commit them there |
| Unsaved changes you do not recognise | Ask whose they are. Do not touch them |
| "Merging" or "rebasing" in progress | Finish it or abort it with the user. Nothing else first |
| "HEAD detached" | Make a branch before committing, or the work is easy to lose |
| Behind the remote | Bring in the remote changes before pushing |

## Step 2 — Save

1. `git switch -c short-topic-name`
2. `git add <each file>`
3. `git diff --staged`: read all of it. This is the last look.
4. Commit. First line: what changed, as an instruction, under about 70 characters ("Fix contact form email address"). Then a blank line and the why, if it is not obvious.

One purpose per commit. Two unrelated changes are two commits.

## Step 3 — Share, after a yes

1. `git push -u origin <branch>`
2. Open the pull request. The description says what changed, why, how it was checked, and what is not done.
3. Give the user the link. Do not merge your own pull request unless asked.

## Step 4 — Conflicts

A conflict means two changes touched the same lines. Git marks each one:

```
<<<<<<< yours
=======
>>>>>>> theirs
```

1. `git status` lists the conflicted files.
2. In each, work out what **both** sides were trying to do, and keep both intentions. Picking "mine" wholesale throws someone's work away.
3. Unsure what the other side meant? Ask. Do not guess.
4. Remove the markers, run the project's checks, `git add` the files, then `git merge --continue` or `git rebase --continue`.

The way out at any point: `git merge --abort` or `git rebase --abort` returns everything to how it was before.

## Step 5 — Undo

| You want to | Command | Safe? |
| --- | --- | --- |
| Take a file out of the next commit | `git restore --staged <file>` | Yes |
| Reword the last commit, not yet pushed | `git commit --amend` | Yes, only if not pushed |
| Undo a commit that was pushed | `git revert <commit>` | Yes. It adds a new commit |
| Look at an earlier version | `git switch --detach <commit>`, then `git switch -` to return | Yes |
| Find a commit that seems lost | `git reflog` | Yes |
| Throw away unsaved changes to a file | `git restore <file>` | **No. Gone for good. Ask first** |

## Step 6 — Release

When asked "is this ready to release" or "ship it", read `references/release-checklist.md`. Missing evidence means no. A deadline is not evidence.

## Output

```
Branch:      name, made from main at abc1234
Commits:     1. message
Checks:      what ran, and the result
Shared:      pushed and link, or "not pushed, waiting for your yes"
Left alone:  unsaved or unrelated work that was not touched
Next:
```

## Never

| Never | Instead |
| --- | --- |
| `git add .` or `git add -A` without reading | Add by name, read the staged difference |
| `git reset --hard` to "clean up" | Ask; commit or stash first |
| Commit on main | Branch first |
| Push without asking | Ask, then push |
| Force push to fix a mistake on a shared branch | `git revert` |
| Resolve a conflict by keeping one side | Keep both intentions |
| `--no-verify` to get past a failing check | Fix the cause, or report it |

## Reference files

| File | Load when |
| --- | --- |
| `references/release-checklist.md` | Deciding whether something is ready to release, and checking it after release |

## Project adjustments

If the current project has adjustments for this skill (branch naming, commit message style, who approves, release steps), apply them. Where they disagree with these instructions, the project's adjustments win.
