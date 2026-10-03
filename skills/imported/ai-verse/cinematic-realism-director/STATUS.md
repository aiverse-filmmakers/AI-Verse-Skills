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
- Phase 8: COMPLETE, gate PASSED
- Phase 9: IN PROGRESS
- Tasks 9.1-9.6: COMPLETE
- Task 9.7: NEXT
- Phase 9 progress: **6 / 11 tasks complete**
- V1 task progress: **73 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

---

# Completed Phase Evidence

## Phase 0 - Architecture, Scope, Governance

Status: COMPLETE
Gate: PASSED
Post-research audit: PASSED

Evidence:
- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

Frozen invariants:
```text
still-image direction/realism is primary scope
standalone-folder operation mandatory
no required AI-Verse OS / MCP / sibling skill / API key for prompt-only reasoning
capable hosts execute, weaker hosts degrade truthfully
explicit user values and preservation requirements remain locks
success != tool execution alone
```

## Phase 1 - Research Corpus and Provenance

Status: COMPLETE
Gate: PASSED

Evidence:
- `references/source-ledger.md`
- `references/source-ledger-addendum.md`
- `references/research/`

Completed: Tasks 1.1-1.11.

## Phase 2 - Cinematic Shot Ontology and Contracts

Status: COMPLETE
Gate: PASSED

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
preservation lock != creative preference
```

Completed: Tasks 2.1-2.5.

## Phase 3 - Core Cinematography Knowledge Base

Status: COMPLETE
Gate: PASSED

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

Hard rules include:
```text
story before prestige camera/lens tokens
perspective != focal length alone
wide rectilinear != fisheye
large format != automatically shallow DOF
cinematic != shallow depth
motion blur != defocus
```

## Phase 4 - Lighting, Exposure, Film Response, Color

Status: COMPLETE
Gate: PASSED

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

## Phase 5 - Physical Realism and Anti-AI Intelligence

Status: COMPLETE
Gate: PASSED

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

## Phase 6 - Decision Engine and Workflows

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

Completed: Tasks 6.1-6.9.

## Phase 7 - Provider and Host Adapters

Status: COMPLETE
Gate: PASSED

Evidence:
- `adapters/generic.md`
- `adapters/openai.md`
- `adapters/gemini.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`
- `references/adapter-fallback-hierarchy.md`
- `references/host-action-policy.md`
- `PHASE_7_AUDIT.md`

Completed: Tasks 7.1-7.9.

Phase 7 invariants:
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

## Phase 8 - Portable Skill, Manifest, and UX

Status: COMPLETE
Gate: PASSED

Evidence:
- `SKILL.md`
- `aiverse.skill.yaml`
- `README.md`
- `references/INDEX.md`
- `references/verified-pitfalls.md`
- `examples/beginner-auto.md`
- `examples/expert-locks.md`
- `examples/reality-repair.md`
- `examples/reference-match.md`
- `examples/prompt-only.md`
- `PHASE_8_AUDIT.md`

Completed: Tasks 8.1-8.6.

Phase 8 gate result:

> A capable agent receiving only `cinematic-realism-director/` can understand how and when to use it, route the correct workflow, load knowledge progressively, preserve locks, use the Reality Gate, adapt to providers, and degrade truthfully when execution tools are unavailable.

---

# Phase 9 - Evaluation, Benchmarking, and Regression System

Status: IN PROGRESS
Progress: **6 / 11**

## 9.1 Routing evals
Status: COMPLETE
Evidence: `evals/routing.json`

Covers 28 positive, negative, and boundary cases across AUTO, CINEMATIZE, REALITY REPAIR, REFERENCE MATCH, MANUAL CAMERA, PROMPT ONLY, shot recipes, and negative/non-scope tasks.

## 9.2 Beginner AUTO evals
Status: COMPLETE
Evidence: `evals/shot-design.json`

Coverage:
- portrait
- narrative drama
- documentary
- travel
- product
- automotive
- food
- architecture
- fashion
- night exterior
- daylight exterior
- interiors

Key assertions:
- no unnecessary beginner camera questions;
- concept preserved;
- story/geometry before prestige tokens;
- motivated light and physical realism required;
- cinematic cliches forbidden as defaults.

## 9.3 Expert-lock evals
Status: COMPLETE
Evidence: `evals/expert-locks.json`

Coverage includes:
- multi-parameter manual locks;
- 14mm rectilinear foreground exaggeration without fisheye;
- f/1.2 + deep-focus tension;
- 65/70mm capture intent + VHS finish;
- provider enum gaps;
- true 90-degree top-down preservation;
- frozen-moment camera-only movement;
- stock/grain/halation separation;
- hard-noon preservation.

## 9.4 Reality Repair evals
Status: COMPLETE
Evidence: `evals/realism-repair.json`

Taxonomy-driven cases cover:
- skin;
- hair;
- eyes;
- fabric;
- product materials;
- contact/gravity;
- reflections;
- shadows;
- lighting motivation;
- fake HDR/exposure;
- DOF segmentation;
- oversharpening;
- repeated background patterns.

Critical rule:
```text
preserve first
fix dependency causes before surface symptoms
prefer smallest justified repair
```

## 9.5 Reference Match evals
Status: COMPLETE
Evidence: `evals/reference-match.json`

Verifies:
- observation vs exact hardware fact;
- known metadata vs visual inference;
- hardware hypotheses remain hypotheses;
- explicit multi-reference roles;
- target locks outrank reference tendencies;
- transferable DNA vs incidental content;
- frozen-moment camera changes;
- true top-down formation preservation;
- product identity priority;
- provider reference-count fallback.

## 9.6 Adapter consistency evals
Status: COMPLETE
Evidence: `evals/adapter-behavior.json`

Cross-provider matrix covers:
- Generic;
- OpenAI;
- Gemini;
- Seedream;
- FLUX;
- Magnific;
- Higgsfield Soul Cinema.

Verified properties:
- same universal shot survives provider translation;
- locks/preservation/reference roles survive;
- provider-specific controls stay downstream;
- unsupported native enums use semantic translation/fallback;
- PROMPT ONLY remains absolute;
- unknown/new model versions degrade to provider-family/generic behavior rather than fabricated parameters;
- adapter existence does not imply provider connection;
- execution success is not V2 visual verification.

## Remaining Phase 9 tasks

```text
9.7 Anti-cliche evals
9.8 Physical plausibility evals
9.9 Adversarial and instruction-boundary evals
9.10 Magnific/Higgsfield comparison protocol
9.11 Regression corpus
Phase 9 gate
```

## Next Batch

Complete the five remaining Phase 9 numbered tasks, then run the Phase 9 gate:

```text
9.7 Anti-cliche evals
9.8 Physical plausibility evals
9.9 Adversarial and instruction-boundary evals
9.10 Magnific/Higgsfield comparison protocol
9.11 Regression corpus
Phase 9 gate
```

Next task: **9.7 - Anti-cliche evals**

---

# Core Invariants Still Governing All Later Work

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

# Change Discipline

Phase 0 remains the governing architecture contract.

Later phases may not silently:
- expand into temporal video authority;
- introduce required external runtime dependencies;
- turn a provider into the core cinematic brain;
- override explicit user or preservation locks;
- treat inferred reference hardware as known fact;
- convert marketing language into physical truth;
- use cinematic artifacts as mandatory realism tokens;
- beautify/redesign preserved identity during repair;
- claim image generation/editing/visual verification when the host did not actually perform it;
- allow provider syntax or controls to redesign the universal shot.
