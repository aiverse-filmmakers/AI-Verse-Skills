---
name: incident-forensics
description: "Reconstruct incidents from logs, traces, commits, configuration, timestamps, and state changes."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Incident Forensics

## Procedure
1. Preserve evidence and define the incident time window and impacted systems.
2. Normalize timestamps and build a factual event timeline from independent sources.
3. Correlate errors, deploys, configuration changes, user actions, dependencies, and resource signals.
4. Separate trigger, root cause, contributing factors, detection gaps, and recovery actions.
5. Produce a reconstruction with confidence levels and missing evidence.

## Constraints
- Correlation is not causation without support.
- Do not alter original evidence to simplify analysis.
- Clock and timezone uncertainty must be explicit.

## Verification
Timeline claims reference evidence and root cause is separated from contributing factors.
