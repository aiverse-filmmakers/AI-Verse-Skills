# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state and restart point for future chats/agents.

## Current State

- Phase 0: COMPLETE, gate PASSED
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE, gate PASSED
- Phase 2: COMPLETE, gate PASSED
- Phase 3: COMPLETE, gate PASSED
- Phase 4: COMPLETE, gate PASSED
- Phase 5: COMPLETE, gate PASSED
- Phase 6: COMPLETE, gate PASSED
- Phase 7: COMPLETE, gate PASSED
- Phase 8: IN PROGRESS
- Task 8.1: COMPLETE
- Task 8.2: COMPLETE
- Task 8.3: NEXT
- Phase 8 progress: **2 / 6 tasks complete**
- V1 task progress: **63 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

## Phase Evidence

### Phase 0 - Architecture / Governance
Evidence:
- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

### Phase 1 - Research / Provenance
Evidence:
- `references/source-ledger.md`
- `references/source-ledger-addendum.md`
- `references/research/`

Completed: Tasks 1.1-1.11.

### Phase 2 - Structured Contracts
Evidence:
- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `PHASE_2_AUDIT.md`

Completed: Tasks 2.1-2.5.

### Phase 3 - Core Cinematography
Evidence:
- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`
- `PHASE_3_AUDIT.md`

Completed: Tasks 3.1-3.7.

### Phase 4 - Lighting / Exposure / Film / Color
Evidence:
- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`
- `PHASE_4_AUDIT.md`

Completed: Tasks 4.1-4.7.

### Phase 5 - Physical Realism / Anti-AI
Evidence:
- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`
- `PHASE_5_AUDIT.md`

Completed: Tasks 5.1-5.8.

### Phase 6 - Decision Engine / Workflows
Evidence:
- `references/workflows/auto-direct.md`
- `references/workflows/cinematize.md`
- `references/workflows/reality-repair.md`
- `references/workflows/reference-match.md`
- `references/workflows/manual-camera.md`
- `references/workflows/prompt-only.md`
- `references/progressive-disclosure-router.md`
- `references/question-minimization.md`
- `references/multi-reference-behavior.md`
- `PHASE_6_AUDIT.md`

Completed: Tasks 6.1-6.9.

### Phase 7 - Provider / Host Adapters
Status: COMPLETE
Gate: PASSED

Evidence:
- `adapters/generic.md`
- `adapters/openai-image.md`
- `adapters/gemini-image.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`
- `references/adapter-fallback-hierarchy.md`
- `references/host-action-policy.md`
- `PHASE_7_AUDIT.md`

Completed tasks:
```text
7.1 Generic adapter                    COMPLETE
7.2 OpenAI image adapter               COMPLETE
7.3 Gemini image adapter               COMPLETE
7.4 Seedream adapter                   COMPLETE
7.5 FLUX adapter                       COMPLETE
7.6 Magnific adapter                   COMPLETE
7.7 Higgsfield Soul Cinema adapter     COMPLETE
7.8 Adapter fallback hierarchy         COMPLETE
7.9 Host action policy                 COMPLETE
```

Phase 7 gate invariants:
```text
one universal cinematic brain
provider syntax stays downstream
locks survive translation
preservation survives translation
reference roles survive translation
unknown/stale provider controls fall back rather than being invented
adapter existence != provider access
V1 execution != V2 visual verification
```

### Phase 8 - Portable Skill / Manifest / UX
Status: IN PROGRESS

Completed:

#### 8.1 Final `SKILL.md`
Status: COMPLETE
Evidence: `SKILL.md`

Implements:
- portable frontmatter and routing description;
- positive/negative activation guidance;
- beginner and expert inputs;
- success contract;
- lock/AUTO/physical-realism/host constraints;
- workflow routing;
- progressive local reference loading;
- provider adaptation downstream of shot design;
- Reality Gate integration;
- execution vs prompt-only host behavior;
- pitfalls, verification and output contracts.

#### 8.2 `aiverse.skill.yaml`
Status: COMPLETE
Evidence: `aiverse.skill.yaml`

Manifest properties:
- low risk;
- required read-only workspace effect only;
- optional write/network/browser effects;
- no raw secret requirement;
- no provider/tool access implied by the manifest;
- explicit postcondition verification;
- first-party human ownership with autonomous mutation disabled.

## Core Invariants Still Governing All Later Work

```text
story before prestige tokens
explicit user value = lock
AUTO fills only missing choices
perspective != focal length alone
cinematic != shallow DOF / grain / flare / teal-orange
reference observation != exact hardware fact
preserve before transforming
Reality Gate before visual-success claims
provider adapter != cinematic brain
adapter file != provider access
prompt-only override is absolute
successful tool call != visual quality verified
standalone package operation remains mandatory
```

## Next Batch

Complete five numbered tasks by finishing Phase 8 and entering Phase 9:

```text
8.3 Write standalone README
8.4 Create reference index
8.5 Create examples
8.6 Write pitfalls from verified test failures
Phase 8 gate
9.1 Routing evals
```

Next task: **8.3 - Write standalone README**

## Change Discipline

Phase 0 remains the governing architecture contract. Later phases may not silently expand temporal video scope, introduce hidden runtime dependencies, override locks, invent provider controls, infer exact hardware from pixels, or weaken standalone operation.
