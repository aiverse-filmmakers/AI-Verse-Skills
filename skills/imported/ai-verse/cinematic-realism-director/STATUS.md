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
- Phase 6: IN PROGRESS
- Task 6.1: COMPLETE
- Task 6.2: COMPLETE
- Task 6.3: COMPLETE
- Task 6.4: COMPLETE
- Task 6.5: COMPLETE
- Task 6.6: NEXT
- V1 task progress: **48 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

## Completed foundations

### Phase 0 - Architecture / Governance
Status: COMPLETE, gate PASSED

Evidence:
- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

### Phase 1 - Research / Provenance
Status: COMPLETE, gate PASSED

Evidence includes source ledger plus Magnific, Higgsfield, camera, lens, film, lighting, color, provider-prompting, secondary-workflow and research-gap files under `references/research/`.

### Phase 2 - Structured Contracts
Status: COMPLETE, gate PASSED

Evidence:
- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `PHASE_2_AUDIT.md`

Core distinctions:
```text
provider-neutral truth != provider syntax
observation != exact hardware fact
confidence != authority
AUTO != unknown
user lock != inference
```

### Phase 3 - Core Cinematography
Status: COMPLETE, gate PASSED

Evidence:
- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`
- `PHASE_3_AUDIT.md`

### Phase 4 - Lighting / Exposure / Film / Color
Status: COMPLETE, gate PASSED

Evidence:
- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`
- `PHASE_4_AUDIT.md`

### Phase 5 - Physical Realism / Anti-AI
Status: COMPLETE, gate PASSED

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

The reusable Reality Gate evaluates intent/locks, geometry, focus/depth/motion, lighting, exposure/color, shadows/reflections, anatomy/human surfaces, materials, contact/gravity/environment, atmosphere, optical effects, stylization restraint, and provider integrity.

---

# Phase 6 - Decision Engine and Workflows

Status: IN PROGRESS
Progress: **5 / 9 tasks complete**

## 6.1 AUTO DIRECT
Status: COMPLETE
Evidence: `references/workflows/auto-direct.md`

One-sentence input is sufficient. The workflow resolves intent -> hierarchy -> composition -> capture -> optics -> lighting -> exposure/color -> realism -> provider adaptation -> Reality Gate. It asks no unnecessary camera questions and does not add cinematic cliches by default.

## 6.2 CINEMATIZE
Status: COMPLETE
Evidence: `references/workflows/cinematize.md`

Preserves the original concept and explicit locks while upgrading only underspecified/weak layers. Cinematization is defined as stronger visual causality and physical plausibility, not effect stacking or prompt inflation.

## 6.3 REALITY REPAIR
Status: COMPLETE
Evidence: `references/workflows/reality-repair.md`

Mandatory sequence:
```text
preserve targets
-> diagnose artificiality
-> prioritize repairs
-> avoid scene drift
-> adapt edit instructions
-> Reality Gate
```

The workflow requires a real target image for visual inspection/editing, uses minimal targeted repair, and never pretends an unavailable previous image is attached.

## 6.4 REFERENCE MATCH
Status: COMPLETE
Evidence: `references/workflows/reference-match.md`

Transfers observable visual DNA while separating observations from hardware hypotheses. Multiple references receive explicit roles/priorities; target locks outrank reference tendencies.

Hard rule:
```text
observed visual trait != known camera/lens/stock fact
```

## 6.5 MANUAL CAMERA
Status: COMPLETE
Evidence: `references/workflows/manual-camera.md`

Every explicit technical choice becomes a lock; AUTO fills only missing values. C0-C3 conflict handling is integrated. Unsupported provider controls are semantically translated and disclosed rather than silently changed.

Hard rule:
```text
explicit user value = LOCK
unspecified compatible value = AUTO
```

## Remaining Phase 6 tasks

```text
6.6 Implement PROMPT ONLY workflow
6.7 Build progressive disclosure router
6.8 Define question-minimization policy
6.9 Define multi-image/reference behavior
Phase 6 gate
```

Phase 6 gate requirement:

> The same skill behaves naturally for a novice sentence, expert camera specification, bad AI image, or reference frame.

## Next batch

Because only four numbered Phase 6 tasks remain, the next minimum-five batch is:

```text
6.6 PROMPT ONLY workflow
6.7 progressive disclosure router
6.8 question-minimization policy
6.9 multi-image/reference behavior
Phase 6 gate
7.1 Generic provider adapter
```

---

# Change Discipline

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
- claim image generation/editing/visual verification when the host did not actually perform it.