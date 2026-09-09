---
name: skill-miner
description: "Study repeated workflows, corrections, failures, and traces to propose reusable skills without directly changing the trusted catalog."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Skill Miner

## Procedure
1. Analyze approved execution traces/corrections using only the minimum necessary scoped data.
2. Cluster repeated multi-step work, stable procedures, and recurring failure recovery.
3. Filter one-off tasks, transient state, secrets, and behavior already covered by existing skills.
4. Propose trigger, outcome, inputs, effects, dependencies, examples, and expected reuse value.
5. Send proposals to the workshop/forge pipeline only.

## Constraints
- Mining is proposal-only and cannot publish or grant permissions.
- Sensitive/transient content is excluded from durable skill text.
- Candidates must be deduplicated against the catalog.

## Verification
Each candidate has evidence of repeated value and a clear reason it should be a skill rather than a tool, memory, or one-off workflow.
