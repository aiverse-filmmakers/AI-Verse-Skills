---
name: release-deploy-guard
description: "Gate releases and deployments using explicit readiness, compatibility, rollback, security, and observability checks."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Release Deploy Guard

## Procedure
1. Identify artifact/version, target environment, changes, dependencies, migrations, flags, and user impact.
2. Evaluate tests, security findings, configuration, secrets, migration safety, capacity, and compatibility.
3. Confirm rollout strategy, health signals, rollback/roll-forward, and ownership.
4. Block release when required evidence is missing or contradictory.
5. After deployment, verify runtime health and key user journeys.

## Constraints
- Pressure or deadlines do not count as evidence.
- Deployment authority belongs to the host runtime/user policy.

## Verification
All required gates, rollback path, and post-deployment health evidence are explicit.
