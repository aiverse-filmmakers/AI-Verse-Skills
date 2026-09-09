---
name: delegation-orchestrator
description: "Decompose work into isolated subproblems, delegate with explicit contracts, and recombine results without losing provenance."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Delegation Orchestrator

## Procedure
1. Identify independent subproblems and the dependencies that must remain sequential.
2. Give each delegate an objective, inputs, scope, allowed effects, deliverable, evidence, and stop conditions.
3. Avoid sharing unnecessary secrets or mutable state.
4. Validate returned work independently and resolve contradictions rather than averaging them.
5. Integrate accepted results with provenance.

## Constraints
- Delegation never expands host permissions.
- Parallel delegates must not race on the same mutable state.
- Returned claims are not trusted merely because another agent produced them.

## Verification
Every accepted sub-result meets its handoff contract and conflicts/uncertainty remain visible.
