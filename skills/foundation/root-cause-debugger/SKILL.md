---
name: root-cause-debugger
description: "Diagnose the underlying cause of a failure before proposing or applying a fix."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Root Cause Debugger

## When to Use
Use for failures, regressions, incorrect behavior, flaky systems, or unexplained errors where symptom-patching would be risky.

## Procedure
1. Reproduce or precisely characterize the failure and boundary conditions.
2. Collect the smallest useful evidence set: errors, logs, inputs, state, environment, and recent changes.
3. Form competing hypotheses and test the highest-information hypotheses first.
4. Identify the causal chain, not only the visible failing line.
5. Propose the minimum safe correction and a regression check.

## Constraints
- Do not claim causation from correlation alone.
- Do not change unrelated code while diagnosing.
- Preserve original evidence where possible.

## Verification
- Root cause explains the symptoms and boundary conditions.
- Plausible alternatives were ruled out with evidence.
- The fix addresses the cause and has a regression check.
