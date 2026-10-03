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
- Task 7.2: COMPLETE
- Task 7.3: COMPLETE
- Task 7.4: COMPLETE
- Task 7.5: COMPLETE
- Task 7.6: COMPLETE
- Task 7.7: NEXT
- Phase 7 progress: **6 / 9 tasks complete**
- V1 task progress: **58 / 93 tasks complete**

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
actual host capability != assumed capability
explicit user values and preservation requirements remain locks
successful tool execution != visual-quality verification
```

## Phase 1 - Research Corpus and Provenance

Status: COMPLETE
Gate: PASSED

Evidence:

- `references/source-ledger.md`
- `references/source-ledger-addendum.md`
- `references/research/magnific.md`
- `references/research/higgsfield.md`
- `references/research/cameras.md`
- `references/research/lenses.md`
- `references/research/lenses-supplement.md`
- `references/research/film-stocks.md`
- `references/research/lighting.md`
- `references/research/color-and-tone.md`
- `references/research/provider-prompting.md`
- `references/research/secondary-public-workflows.md`
- `references/research/research-gap-audit.md`

Completed: Tasks 1.1-1.11.

## Phase 2 - Cinematic Shot Ontology and Structured Contracts

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

Completed: Tasks 2.1-2.5.

Core distinctions:

```text
provider-neutral truth != provider syntax
observation != exact hardware fact
confidence != authority
AUTO != unknown
user lock != inference
preservation lock != creative preference
```

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
wide lens != fisheye
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

Phase 6 gate verified beginner AUTO, expert locks, cinematization without concept drift, targeted repair, reference matching without hardware hallucination, prompt-only override, multi-reference roles, and frozen-moment camera changes.

---

# Phase 7 - Provider and Host Adapters

Status: IN PROGRESS
Goal: translate one provider-neutral cinematic brain into strong instructions across major image-generation environments.

Core rule:

```text
Cinematic Shot Spec = creative truth
adapter = translation layer
provider capability = current execution constraint
```

Provider behavior was rechecked against current first-party/current live surfaces on **2026-10-03** before Tasks 7.2-7.6 were frozen.

## 7.1 Generic adapter

Status: COMPLETE
Evidence: `adapters/generic.md`

Implemented mandatory fallback for unknown/changed providers, natural-language serialization, edit/preservation structures, reference roles, positive realism translation, unsupported-control semantic fallback, truthful host degradation, and no fabricated parameters.

## 7.2 OpenAI image adapter

Status: COMPLETE
Evidence: `adapters/openai.md`

Current first-party OpenAI image documentation was rechecked on 2026-10-03.

Implemented:

- text-to-image and edit routing;
- current Responses/Image API capability awareness without making API fields core requirements;
- multi-turn targeted edits where image state is actually available;
- preservation/change separation;
- multiple-reference role language;
- positive realism translation;
- output-control capability checks;
- current-model drift fallback to generic adapter;
- V0/V2 Reality Gate integration.

Hard rule:

```text
current GPT Image model name / API surface != universal cinematic logic
```

## 7.3 Gemini image adapter

Status: COMPLETE
Evidence: `adapters/gemini.md`

Current Google AI image-generation/editing documentation was rechecked on 2026-10-03.

Implemented:

- conversational text-to-image and image-edit translation;
- explicit spatial relationships;
- targeted multi-turn refinement only when image state exists;
- reference-role preservation;
- Reference Match without hardware certainty;
- Reality Repair integration;
- capability-checked aspect/output controls;
- model-drift fallback.

Hard rule:

```text
Gemini model/version churn cannot redesign the Cinematic Shot Spec
```

## 7.4 Seedream adapter

Status: COMPLETE
Evidence: `adapters/seedream.md`

Current BytePlus Seedream 5.0 Pro / Flash documentation was rechecked on 2026-10-03.

Implemented:

- generation and reference-conditioned translation;
- multi-reference role handling;
- optional point/bounding-box interactive editing when actually exposed;
- unchanged-region preservation;
- local Reality Repair targeting;
- optional layer-decomposition awareness without runtime dependency;
- fallback to natural language when spatial controls are unavailable;
- version/reference-limit drift protection.

Hard rule:

```text
coordinate editing = provider mechanic
not cinematic reasoning
```

## 7.5 FLUX adapter

Status: COMPLETE
Evidence: `adapters/flux.md`

Current official Black Forest Labs public `flux-image-best-practices` material was rechecked on 2026-10-03.

Implemented:

- BFL-style subject/action/context/lighting/technical serialization;
- positive desired-state prompting rather than negative-prompt dependence;
- explicit lighting translation;
- current FLUX.2 / FLUX.1 family capability awareness;
- image editing only when active model/host verifies it;
- multi-reference roles;
- optional structured prompting without unsupported schema invention;
- model-family drift fallback.

Hard rule:

```text
universal avoidance -> positive visible target
```

## 7.6 Magnific Cinematic adapter

Status: COMPLETE
Evidence:

- `adapters/magnific.md`
- `references/research/magnific.md`

Magnific's connected live `Cinematic` model/settings schema was rechecked on 2026-10-03.

Implemented current native mapping for:

```text
camera
lensBrand
focalLength
aperture
shotType
filmStock
movieLook
lighting
motionBlur
grain
halation
tonalLook
```

Also implemented:

- native control only when exact/compatible;
- prompt-language fallback for unsupported nuance;
- no silent focal/aperture/lens rounding/substitution;
- compound shotType conflict protection;
- motivated-lighting prompt logic preserved behind provider lighting presets;
- optional movie-look use only when explicitly justified/requested;
- dedicated edit-operation preference for preservation-sensitive repairs;
- live-schema-over-cached-schema drift rule;
- provider controls never override user locks.

Hard rule:

```text
live verified provider schema
> cached provider adapter
> generic adapter

but always:
user locks + universal shot spec
> provider defaults
```

## Remaining Phase 7 Tasks

```text
7.7 Higgsfield Soul Cinema adapter
7.8 Adapter fallback hierarchy
7.9 Host action policy
Phase 7 gate
```

---

# Next Batch

Only three numbered Phase 7 tasks remain. Under the five-task minimum rule, the next batch is:

```text
7.7 Higgsfield Soul Cinema adapter
7.8 Adapter fallback hierarchy
7.9 Host action policy
Phase 7 gate
8.1 Write final SKILL.md
8.2 Write aiverse.skill.yaml
```

This will complete and gate Phase 7, then begin Phase 8 with two numbered packaging tasks.

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
- claim image generation/editing/visual verification when the host did not actually perform it;
- allow provider syntax, presets, or control enums to redesign the universal shot;
- freeze volatile model names/limits into core cinematography knowledge.
