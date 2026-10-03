# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical plan: `IMPLEMENTATION_PLAN.md`

## Current State

- Phase 0: COMPLETE
- Task 0.1: COMPLETE
- Task 0.2: COMPLETE
- Task 0.3: COMPLETE
- Task 0.4: COMPLETE
- Task 0.5: COMPLETE
- Next task: 1.1 - Build source ledger framework

## Task 0.1 - Freeze package identity and routing scope

Status: COMPLETE

### Frozen identity

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
primary_role: cinematic still-image direction and photorealism intelligence
```

### Evidence

Created `references/routing.md` with:

- stable package identity;
- primary still-image scope;
- positive activation boundaries;
- negative activation boundaries;
- Video Editor ownership boundary;
- Interface Designer ownership boundary;
- video/temporal boundary;
- borderline routing rules;
- routing authority order;
- positive and negative activation fixtures;
- explicit scope-change rule.

### Acceptance check

- [x] name is stable
- [x] scope does not overlap unnecessarily with Video Editor
- [x] scope does not overlap unnecessarily with Interface Designer
- [x] still-image creation/editing is primary
- [x] video is discussed only where it changes a still-frame decision or belongs to future/adjacent workflow ownership

## Task 0.2 - Define standalone portability contract

Status: COMPLETE

### Evidence

Created `references/portability.md` with:

- package folder as the canonical portable runtime unit;
- package-local required references only;
- no required repository-root files/scripts;
- no required sibling skills;
- no AI-Verse OS requirement for prompt-only/reasoning operation;
- no MCP requirement for V1 core operation;
- no API-key requirement for prompt-only operation;
- host-independent/provider-neutral core logic;
- local adapter and schema requirements;
- generic adapter fallback;
- isolated-folder V1 acceptance requirements.

### Acceptance check

- [x] no required parent-directory references
- [x] no required sibling skills
- [x] no required AI-Verse OS
- [x] no required MCP
- [x] no required API key for prompt-only operation

## Task 0.3 - Define host capability degradation rules

Status: COMPLETE

### Evidence

Created `references/host-capabilities.md`.

Defined six capability classes:

- H1 native generation + editing;
- H2 generation without true editing;
- H3 editing without general text-to-image generation;
- H4 vision + external/granted image tools;
- H5 vision without image execution;
- H6 text-only.

The contract also defines:

- operation matrix by host class;
- action-priority hierarchy;
- explicit prompt-only override;
- image-target availability rule;
- execution-confirmed versus visual-quality-verified distinction;
- unknown-provider generic fallback;
- degradation without reduction of cinematic reasoning quality;
- failure conditions for false capability claims.

### Acceptance check

- [x] native image-generation hosts produce a direct execution path
- [x] image-editing hosts produce a direct repair/edit path
- [x] external image-tool hosts route through granted capabilities only
- [x] vision-only hosts produce diagnosis + prompt/spec outputs
- [x] text-only hosts produce useful AUTO/manual/prompt outputs
- [x] every host class produces a useful result
- [x] no host class requires false claims of generation/editing/inspection

## Task 0.4 - Define explicit-lock semantics

Status: COMPLETE

### Evidence

Created `references/locks.md`.

The lock contract defines:

- hard locks;
- preservation locks;
- soft preferences;
- AUTO fields;
- lock precedence;
- partial specification behavior;
- contradiction classes C0-C3;
- reconciliation through AUTO fields before touching locks;
- semantic translation when providers do not expose literal hardware controls;
- preservation-first Reality Repair behavior;
- lock persistence and revision rules;
- uncertainty rules for reference-derived values;
- mandatory lock verification before full success.

### Acceptance check

- [x] explicit values become locks by default
- [x] locks cannot be silently changed
- [x] contradictions are handled predictably
- [x] reconcilable tension is solved through AUTO fields first
- [x] unspecified parameters remain inferable
- [x] provider limitations do not silently erase user intent
- [x] preservation locks are enforced in image-editing workflows

## Task 0.5 - Define success contract and failure vocabulary

Status: COMPLETE

### Evidence

Created `references/success-contract.md`.

Defined top-level states:

```text
success
partial
blocked
failed
```

Defined verification levels:

```text
V0 reasoning only
V1 execution confirmed
V2 visual inspection completed
V3 comparative/iterative acceptance
```

Defined task-specific postconditions for:

- AUTO DIRECT / new generation;
- CINEMATIZE;
- REALITY REPAIR;
- REFERENCE MATCH;
- MANUAL CAMERA;
- PROMPT ONLY;
- SHOT RECIPE / EXPLAIN.

Also froze:

- Reality Gate participation in success;
- execution confirmation versus visual verification;
- uncertainty handling;
- retry/iteration principle;
- lightweight beginner reporting versus structured agent/test reporting.

### Acceptance check

- [x] success has explicit postconditions
- [x] partial is distinct from success and blocked
- [x] blocked represents missing prerequisites/capabilities rather than internal failure
- [x] failed represents execution/logic/postcondition failure
- [x] generation/edit/analysis/prompt-only workflows have distinct success semantics
- [x] tool-call success is not treated as visual-quality proof
- [x] Reality Gate participates in final acceptance
- [x] user-facing status remains concise by default

# Phase 0 Gate

Status: PASSED

Architecture, scope, portability, host degradation, user-lock semantics, and truthful success/failure reporting are frozen before adding the cinematic research corpus.

Phase 1 may now begin.

## Change Discipline

Implement numbered tasks from `IMPLEMENTATION_PLAN.md` deliberately and record acceptance evidence here.

For research tasks, preserve provenance and do not allow weaker internal skills to become authoritative cinematic sources without independent verification.
