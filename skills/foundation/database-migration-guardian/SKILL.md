---
name: database-migration-guardian
description: "Plan and verify schema/data migrations with compatibility, backfill, rollback, locking, and data-safety controls."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Database Migration Guardian

## Procedure
1. Capture current schema, data volume, application compatibility window, and availability requirements.
2. Classify operations by locking, rewrite, data-loss, and compatibility risk.
3. Use expand/migrate/contract phases when compatibility across deployments is required.
4. Define backfill batching, observability, checkpoints, rollback/roll-forward, and validation queries.
5. Test on representative data before production execution.

## Constraints
- Data-loss risk must be explicit.
- Production mutation requires host-granted authority.
- Avoid irreversible one-step migrations when a staged path is available.

## Verification
Application compatibility, data invariants, backfill, and recovery behavior are tested.
