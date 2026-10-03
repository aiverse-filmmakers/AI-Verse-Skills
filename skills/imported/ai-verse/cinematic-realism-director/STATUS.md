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
- Phase 7: IN PROGRESS
- Task 7.1: COMPLETE
- Task 7.2: NEXT
- V1 task progress: **53 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

## Completed Phase Evidence

### Phase 0 - Architecture, Scope, Governance
Evidence:
- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

### Phase 1 - Research Corpus and Provenance
Evidence:
- `references/source-ledger.md`
- `references/source-ledger-addendum.md`
- `references/research/`

Completed: Tasks 1.1-1.11.

### Phase 2 - Cinematic Shot Ontology and Contracts
Evidence:
- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `PHASE_2_AUDIT.md`

Completed: Tasks 2.1-2.5.

Core distinctions:
```text
provider-neutral truth != provider syntax
observation != exact hardware fact
confidence != authority
AUTO != unknown
user lock != inference
```

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

Core hard rules include:
```text
story before prestige camera/lens tokens
perspective != focal length alone
wide lens != fisheye
large format != automatically shallow DOF
cinematic != shallow depth
motion blur != defocus
```

### Phase 4 - Lighting, Exposure, Film Response, Color
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

Core hard rules include:
```text
cinematic lighting starts from motivated sources
dynamic range != everything visible
film != warm + grain + faded
log != final grade
cinematic != teal-orange
grain / halation / bloom / flare are separate optional systems
```

### Phase 5 - Physical Realism and Anti-AI Intelligence
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

Reality Gate order:
```text
locks / preservation
-> geometry / perspective
-> focus / depth / motion
-> lighting
-> exposure / color
-> shadows / reflections
-> anatomy / skin / hair / eyes
-> fabric / materials
-> contact / gravity / environment
-> atmosphere
-> optical effects
-> stylization restraint
-> provider integrity
```

### Phase 6 - Decision Engine and Workflows
Status: COMPLETE
Gate: PASSED
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

Completed tasks:
```text
6.1 AUTO DIRECT                         COMPLETE
6.2 CINEMATIZE                          COMPLETE
6.3 REALITY REPAIR                      COMPLETE
6.4 REFERENCE MATCH                     COMPLETE
6.5 MANUAL CAMERA                       COMPLETE
6.6 PROMPT ONLY                         COMPLETE
6.7 progressive disclosure router       COMPLETE
6.8 question-minimization policy        COMPLETE
6.9 multi-image/reference behavior      COMPLETE
```

Phase 6 gate verified:
- one-sentence beginner AUTO;
- expert technical locks;
- CINEMATIZE without concept drift;
- targeted Reality Repair;
- Reference Match without hardware hallucination;
- prompt-only override;
- multi-reference role separation;
- frozen-moment camera changes.

Audit result:
```text
scope violations: 0
standalone violations: 0
provider-core contamination: 0
explicit-lock violations: 0
preservation violations: 0
false hardware-certainty violations: 0
false visual-verification violations: 0
question-bloat violations: 0
reference-role violations: 0
prompt-only override violations: 0
```

## Phase 7 - Provider and Host Adapters

Status: IN PROGRESS
Goal: translate one provider-neutral cinematic brain into strong instructions across major image-generation environments.

### 7.1 Generic adapter
Status: COMPLETE
Evidence: `adapters/generic.md`

Implemented:
- mandatory fallback for unknown/changed providers;
- provider-neutral natural-language serialization;
- generation, edit, repair and reference-conditioned prompt structures;
- positive physical-realism translation;
- camera/lens names preserved as references while observable traits remain authoritative;
- explicit camera-position/perspective translation;
- motivated-lighting serialization;
- no assumed negative-prompt support;
- semantic fallback for unsupported controls;
- truthful host degradation;
- no fabricated provider parameters.

Hard rule:
```text
Cinematic Shot Spec = creative truth
adapter = translation layer
```

### Remaining Phase 7 tasks

```text
7.2 OpenAI image adapter
7.3 Gemini image adapter
7.4 Seedream adapter
7.5 FLUX adapter
7.6 Magnific adapter
7.7 Higgsfield Soul Cinema adapter
7.8 Adapter fallback hierarchy
7.9 Host action policy
Phase 7 gate
```

## Next Batch

Complete the next five numbered tasks:

```text
7.2 OpenAI image adapter
7.3 Gemini image adapter
7.4 Seedream adapter
7.5 FLUX adapter
7.6 Magnific adapter
```

Then the following batch will finish Phase 7 and continue into Phase 8 as needed to satisfy the five-task minimum.

## Change Discipline

Phase 0 remains the governing architecture contract.

Later phases may not silently:
- expand into temporal video authority;
- introduce required external runtime dependencies;
- turn one provider into the core brain;
- override explicit user or preservation locks;
- treat inferred reference hardware as known fact;
- convert marketing language into physical truth;
- use cinematic artifacts as mandatory realism tokens;
- beautify/redesign preserved identity during repair;
- claim image generation/editing/visual verification when the host did not actually perform it;
- allow provider syntax or controls to redesign the universal shot.