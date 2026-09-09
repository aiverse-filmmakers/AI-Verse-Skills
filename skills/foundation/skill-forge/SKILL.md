---
name: skill-forge
description: "Create, validate, test, and package new AI-Verse skills without granting them trust or runtime authority."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Skill Forge

## Procedure
1. Start from a reusable job and define triggers, non-triggers, inputs, success contract, effects, and dependencies.
2. Search the catalog for duplicates or composable existing skills.
3. Generate the smallest complete portable package in workshop/quarantine; deterministic mechanics belong in scripts/tools.
4. Run schema validation, security/injection scanning, trigger/non-trigger evals, and sandboxed task evals.
5. Produce a promotion proposal with evidence.

## Constraints
- Creation and promotion are separate permissions.
- New/generated skills begin untrusted.
- Do not embed raw secrets or private workspace content.
- Do not autonomously mutate protected core, human, vendor, or imported originals.

## Verification
Promotion evidence includes deduplication, security results, and task evaluation results.
