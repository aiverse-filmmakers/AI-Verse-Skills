---
name: api-integration-engineer
description: "Integrate unfamiliar APIs or SDKs safely, including auth, pagination, retries, rate limits, schemas, errors, and verification."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# API Integration Engineer

## Procedure
1. Read current official documentation and identify the operation and version.
2. Model authentication as secret/connection handles and enumerate required scopes.
3. Define schemas, pagination, idempotency, retry policy, rate limits, and failure semantics.
4. Implement the smallest end-to-end path and test a safe/read-only operation first where possible.
5. Add contract checks for success, expected errors, and edge cases.

## Constraints
- Never embed credentials in skill content.
- Retries must not duplicate non-idempotent operations.
- Validate responses before downstream use.

## Verification
Endpoint/version behavior, error handling, and read-back of consequential writes are demonstrated.
