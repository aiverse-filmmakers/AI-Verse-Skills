---
name: transactional-refactor
description: "Execute multi-file refactors through bounded checkpoints with validation and a clear rollback path."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Transactional Refactor

## Procedure
1. State behavior that must remain invariant and the structural change intended.
2. Partition the refactor into independently verifiable checkpoints.
3. Before each checkpoint, identify callers, tests, data contracts, and generated artifacts affected.
4. Apply one bounded change and validate it before continuing.
5. Finish with full diff review, compatibility verification, and rollback notes.

## Constraints
- Preserve unrelated user work.
- Do not mix opportunistic cleanup into the transaction.
- Stop when a checkpoint fails instead of stacking more changes on uncertainty.

## Verification
- Every checkpoint has health evidence.
- Behavioral invariants are tested or otherwise verified.
- Rollback is possible from known checkpoints.
