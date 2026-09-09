---
name: git-change-lifecycle
description: "Manage a source change from repository inspection through commits, review, conflicts, and merge readiness."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Git Change Lifecycle

## Procedure
1. Inspect status, branch, remotes, contribution rules, and existing uncommitted work.
2. Define the change boundary and protect unrelated user work.
3. Use the appropriate branch/worktree and make bounded changes.
4. Review the diff, run required checks, and create clear commit/PR context.
5. Assess conflicts, feedback, CI, and merge readiness without overwriting concurrent work.

## Constraints
- Do not discard unrelated local changes.
- History-changing or remote writes follow host approval policy.
- Commit scope should match stated intent.

## Verification
The final diff, checks, conflicts, and merge readiness are explicitly accounted for.
