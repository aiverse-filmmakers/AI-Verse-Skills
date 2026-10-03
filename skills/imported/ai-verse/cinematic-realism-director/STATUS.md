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
- Phase 5: IN PROGRESS
- Task 5.1: COMPLETE
- Task 5.2: COMPLETE
- Task 5.3: COMPLETE
- Task 5.4: NEXT
- V1 task progress: **38 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

Next batch can complete all five remaining Phase 5 tasks:

```text
5.4 Fabric and material realism system
5.5 Contact, gravity, and environmental interaction
5.6 Reflection and shadow coherence
5.7 Optical imperfection without fake vintage spam
5.8 Build Reality Gate
Phase 5 gate
```

---

# Phase 0 - Architecture, Scope, and Governance

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

---

# Phase 1 - Research Corpus and Provenance

Status: COMPLETE
Gate: PASSED

Evidence includes:

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

---

# Phase 2 - Cinematic Shot Ontology and Structured Contracts

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

---

# Phase 3 - Core Cinematography Knowledge Base

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

Core hard rules include:

```text
story before prestige camera/lens tokens
perspective != focal length alone
wide lens != fisheye
large format != automatically shallow DOF
cinematic != shallow depth
motion blur != defocus
```

---

# Phase 4 - Lighting, Exposure, Film Response, and Color

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

Completed tasks:

```text
4.1 motivated-lighting engine                       COMPLETE
4.2 key/fill/negative-fill/edge/bounce/practicals COMPLETE
4.3 environment-specific lighting recipes          COMPLETE
4.4 exposure and dynamic-range behavior             COMPLETE
4.5 film stock and sensor response mapping          COMPLETE
4.6 color science and grading strategy              COMPLETE
4.7 grain/halation/bloom/flare/texture restraint    COMPLETE
```

## 4.6 Color science and grading strategy

Status: COMPLETE
Evidence: `references/color-science-and-grading.md`

Implemented provider-neutral runtime rules for:

- capture color vs final grade;
- white-balance strategy;
- mixed-source preservation;
- color separation;
- contextual saturation;
- density;
- skin handling;
- highlight and shadow color;
- black levels;
- highlight rolloff;
- neutral vs stylized grades;
- monochrome;
- brand/product color preservation;
- reference-match grade observation;
- Color Reality Gate.

Hard rules:

```text
log != final grade
cinematic != teal-orange
cinematic != desaturated
film != warm faded LUT
skin != one orange hue
density != simply darker
```

## 4.7 Grain, halation, bloom, flare, and texture restraint

Status: COMPLETE
Evidence: `references/texture-effects-restraint.md`

Implemented separate systems for:

- film grain;
- sensor noise;
- halation;
- bloom;
- lens flare;
- veiling glare;
- optical diffusion;
- sharpness;
- microcontrast;
- compression/low-fi artifacts;
- film dirt/dust/scratches/gate weave;
- material-specific texture hierarchy.

Hard rules:

```text
film != grain + warmth
halation != universal red glow
bloom != global blur
flare != mandatory cinema token
realism != dirtiness
vintage != stack every old-media artifact
```

# Phase 4 Gate

Status: PASSED
Evidence: `PHASE_4_AUDIT.md`

Gate cases included:

- natural window portrait;
- hard-noon travel exterior;
- tungsten/daylight mixed interior;
- bright product commercial;
- neon night street;
- locked VISION3 500T;
- locked ALEXA 35 clean digital beauty.

Audit result:

```text
scope violations: 0
standalone dependency violations: 0
provider-core contamination: 0
explicit-lock violations: 0
reference-certainty violations: 0
hidden conflict resolution: 0
capture-vs-grade conflation: 0
film-vs-effect conflation: 0
```

---

# Phase 5 - Physical Realism and Anti-AI Intelligence

Status: IN PROGRESS
Goal: make realism diagnosis and preservation-aware repair a first-class capability.

## 5.1 Build anti-AI artifact taxonomy

Status: COMPLETE
Evidence: `references/anti-ai-artifact-taxonomy.md`

Implemented structured diagnostic domains for:

- skin;
- symmetry/beautification;
- hair;
- eyes;
- anatomy/geometry;
- fabric;
- materials/roughness;
- reflections/refractions;
- shadows;
- lighting;
- exposure/tone;
- color;
- perspective;
- focus/depth;
- motion;
- contact/gravity;
- environment;
- atmosphere;
- grain/texture;
- optical effects;
- repetition/patterns;
- text/logos/symbols;
- overdone cinematic effects.

Also implemented S0-S4 severity, evidence requirements, minimal-repair ordering, and preserve/repair/allow-change boundaries.

Hard rule:

```text
AI-looking != regenerate everything
```

## 5.2 Skin realism system

Status: COMPLETE
Evidence: `references/skin-realism.md`

Implemented:

- region-specific skin texture;
- pores and fine texture;
- subtle color variation;
- source-consistent specular response;
- restrained subsurface/translucency cues;
- peach fuzz only when framing/light supports it;
- age-appropriate texture;
- makeup vs skin distinction;
- beauty/commercial vs documentary skin handling;
- sweat/moisture;
- anatomy-before-texture rule;
- focus/resolution coherence;
- identity-preserving repair sequence;
- Skin Reality Gate.

Hard rules:

```text
real skin != pore overlay
beauty != plastic
realism != aging the subject
skin != uniform orange
identity preservation outranks cosmetic AUTO changes
```

## 5.3 Hair and eye realism system

Status: COMPLETE
Evidence: `references/hair-and-eye-realism.md`

Hair system covers:

- mass/silhouette before strands;
- root direction;
- gravity/weight;
- clump hierarchy;
- restrained flyaways;
- curl/wave variation;
- directional specular behavior;
- color variation;
- backlight;
- focus/motion/contact;
- facial hair.

Eye system covers:

- binocular gaze coherence;
- eyelid/globe geometry;
- non-white sclera behavior;
- iris/pupil realism;
- corneal reflection and source-consistent catchlights;
- moisture/tear line;
- lashes/brows;
- focus/depth;
- expression integration.

Hard rules:

```text
real hair != thousands of perfect strands
flyaways != mandatory realism
real eyes != glass marbles
sclera != pure white
catchlights != decorative dots
hair/eye repair must preserve identity and expression
```

## 5.4 Fabric and material realism system

Status: NEXT

## 5.5 Contact, gravity, and environmental interaction

Status: NOT STARTED

## 5.6 Reflection and shadow coherence

Status: NOT STARTED

## 5.7 Optical imperfection without fake vintage spam

Status: NOT STARTED

## 5.8 Build Reality Gate

Status: NOT STARTED

# Phase 5 Gate

Status: NOT YET RUN

Gate requirement:

> The skill can explain exactly why an image feels AI-generated and produce a preservation-aware repair plan.

---

# Next

Complete Phase 5 in one five-task batch:

```text
5.4 Fabric and material realism system
5.5 Contact, gravity, and environmental interaction
5.6 Reflection and shadow coherence
5.7 Optical imperfection without fake vintage spam
5.8 Build Reality Gate
Phase 5 gate
```

---

# Change Discipline

Phase 0 remains the governing architecture contract.

Later phases may not silently:

- expand into temporal video authority;
- introduce required external runtime dependencies;
- turn one provider into the core brain;
- override explicit user locks;
- treat inferred reference hardware as known fact;
- convert marketing language into physical truth;
- turn secondary public skills into authoritative cinematography sources;
- use focal length as a false substitute for camera position;
- use cinematic artifacts as mandatory realism tokens;
- beautify or redesign preserved human identity during Reality Repair.
