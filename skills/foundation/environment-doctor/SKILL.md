---
name: environment-doctor
description: "Diagnose runtime, path, package, permission, service, and configuration mismatches that prevent software from working."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Environment Doctor

## Procedure
1. Capture the expected environment contract: OS, runtimes, binaries, paths, services, ports, permissions, and configuration.
2. Collect actual values without exposing secrets.
3. Compare expected vs actual and rank mismatches by explanatory power.
4. Test the smallest safe correction or provide a reversible remediation sequence.
5. Re-run the failing operation and environment checks.

## Constraints
- Secret values remain redacted.
- Diagnosis is based on measured state, not assumptions.
- Prefer reversible corrections.

## Verification
The original failure is re-tested and the corrected effective environment is confirmed.
