---
name: dependency-supply-chain-audit
description: "Assess dependency risk across vulnerabilities, provenance, maintenance, versions, licenses, and upgrade impact."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Dependency Supply Chain Audit

## Procedure
1. Inventory direct and material transitive dependencies and lockfile-resolved versions.
2. Check advisories, provenance, maintenance/release activity, license, integrity, and install behavior.
3. Map risky packages to reachable application paths and actual exposure.
4. Compare safe remediation options and compatibility constraints.
5. Return prioritized findings and the least-disruptive remediation path.

## Constraints
- Distinguish package presence from reachable exposure.
- Record exact package/version evidence.
- Do not automatically upgrade without compatibility validation and granted write scope.

## Verification
Each finding has provenance, exposure reasoning, and a testable remediation path.
