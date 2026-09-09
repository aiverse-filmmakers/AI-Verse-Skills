---
name: knowledge-writeback
description: "Safely write validated durable knowledge into the host system without turning transient agent thoughts into canonical memory."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Knowledge Writeback

## Procedure
1. Determine whether information is durable, correctly scoped, and worth canonicalizing.
2. Identify the authoritative destination and competing/duplicate knowledge.
3. Prepare a minimal write proposal with source, confidence, scope, timestamp, and update semantics.
4. Use host-approved write APIs only and never create a parallel hidden source of truth.
5. Read back canonical state and report the exact change.

## Constraints
- AI-Verse OS or the host owns memory/workspace authority.
- Do not store transient reasoning, secrets, or unverified claims as durable knowledge.

## Verification
Scope, provenance, duplicate handling, and canonical read-back are confirmed.
