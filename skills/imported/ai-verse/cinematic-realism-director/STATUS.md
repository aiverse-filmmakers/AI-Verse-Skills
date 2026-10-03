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
- Task 9.1: COMPLETE
- Task 9.2: NEXT
- Phase 9 progress: **1 / 11 tasks complete**
- V1 task progress: **68 / 93 tasks complete**

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

Research debt remains explicitly tracked in `references/research/research-gap-audit.md` and does not block current runtime architecture.

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

Hard rules include:

```text
cinematic lighting starts from motivated sources
dynamic range != everything visible
film != warm + grain + faded
log != final grade
cinematic != teal-orange
grain / halation / bloom / flare are separate optional systems
```

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

Reality Gate dependency order:

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

Workflow split:

```text
AUTO DIRECT       minimal idea -> complete directed shot
CINEMATIZE        existing concept -> stronger cinematography without concept drift
REALITY REPAIR    preserve -> diagnose -> minimal repair -> verify
REFERENCE MATCH   observable DNA -> target transfer without hardware hallucination
MANUAL CAMERA     explicit values = locks; AUTO fills missing fields
PROMPT ONLY       adapted prompt/spec only; never generate
```

## Phase 7 - Provider and Host Adapters

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

Standalone core requires no parent/sibling skill, AI-Verse OS, MCP, API key, private machine path, or provider account for prompt/spec operation.

---

# Phase 9 - Evaluation, Benchmarking, and Regression System

Status: IN PROGRESS

## 9.1 Routing evals

Status: COMPLETE
Evidence: `evals/routing.json`

Corpus currently covers 28 positive, negative, and boundary cases, including:

- beginner cinematic still generation;
- CINEMATIZE;
- Reality Repair;
- Reference Match;
- expert MANUAL CAMERA locks;
- PROMPT ONLY;
- shot-recipe explanation;
- commercial product photography;
- frozen-moment camera changes;
- true top-down reference transformations;
- negative video-editing/UI/logo/equipment-fact/chart/crop/script/general-education cases;
- hero-frame and still-frame motion boundary cases.

Critical routing failures include activating for video editorial/UI work, ignoring PROMPT ONLY, missing Reality Repair activation, or turning pure equipment questions into shot-design tasks.

## Remaining Phase 9 tasks

```text
9.2 Beginner AUTO evals
9.3 Expert-lock evals
9.4 Reality Repair evals
9.5 Reference Match evals
9.6 Adapter consistency evals
9.7 Anti-cliche evals
9.8 Physical plausibility evals
9.9 Adversarial and instruction-boundary evals
9.10 Magnific/Higgsfield comparison protocol
9.11 Regression corpus
Phase 9 gate
```

## Next Batch

Complete the next five numbered tasks:

```text
9.2 Beginner AUTO evals
9.3 Expert-lock evals
9.4 Reality Repair evals
9.5 Reference Match evals
9.6 Adapter consistency evals
```

Next task: **9.2 - Beginner AUTO evals**

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
