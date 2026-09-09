---
name: configuration-contract-doctor
description: "Find contradictions among configuration files, environment variables, defaults, schemas, secrets, deployment settings, and runtime expectations."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Configuration Contract Doctor

## Procedure
1. Enumerate configuration sources and precedence for the affected component.
2. Build the expected contract for each key: type, requiredness, default, scope, secrecy, and consumers.
3. Resolve effective values without exposing secrets and compare environments.
4. Identify stale keys, shadowed values, incompatible defaults, schema drift, and undocumented requirements.
5. Apply/propose the smallest normalization and verify effective runtime configuration.

## Constraints
- Never print raw secret values.
- Precedence must be explicit rather than assumed.

## Verification
Each mismatch names the conflicting sources and runtime behavior is rechecked after correction.
