---
name: change-review
description: "Review proposed changes for correctness, regressions, security, architecture fit, test quality, and unintended side effects."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Change Review

## Procedure
1. Read stated intent and inspect the complete relevant diff plus surrounding contracts/code.
2. Trace changed behavior through callers, data flows, permissions, error paths, and tests.
3. Prioritize concrete correctness/security/regression issues over stylistic preference.
4. For each finding, show failure mechanism, affected scenario, evidence, and severity.
5. Assess whether tests cover the changed behavior and state residual risk.

## Constraints
- Do not invent findings without a plausible failure path.
- Absence of findings is not proof of correctness.

## Verification
Findings are actionable, severity-ranked, and grounded in the actual change and affected system.
