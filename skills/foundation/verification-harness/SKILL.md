---
name: verification-harness
description: "Turn 'looks done' into evidence using the right tests, builds, lint checks, assertions, smoke checks, and provider read-backs."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Verification Harness

## Procedure
1. Translate the requested outcome into observable success conditions.
2. Select the cheapest checks covering correctness, integration, regressions, and side effects.
3. Run deterministic checks before subjective inspection where possible.
4. Distinguish product failure from test or harness failure.
5. Return a receipt showing what passed, failed, was skipped, and why.

## Constraints
- A green command is not enough when it does not test the requested outcome.
- Never fabricate test execution or results.
- Consequential writes require provider/state read-back when available.

## Verification
Every material success claim maps to evidence and every coverage gap is explicit.
