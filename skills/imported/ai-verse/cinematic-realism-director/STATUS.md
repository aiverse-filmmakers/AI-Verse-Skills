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
- Phase 6: NOT STARTED
- V1 task progress: **43 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

Next batch:

```text
6.1 Implement AUTO DIRECT workflow
6.2 Implement CINEMATIZE workflow
6.3 Implement REALITY REPAIR workflow
6.4 Implement REFERENCE MATCH workflow
6.5 Implement MANUAL CAMERA workflow
```

Next task: **6.1 - Implement AUTO DIRECT workflow**

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

Completed: Tasks 4.1-4.7.

Core hard rules include:

```text
cinematic lighting starts from motivated sources
not every shot needs every lighting role
dynamic range != everything visible
good highlights != no clipping anywhere
film != warm + grain + faded
log != final grade
cinematic != teal-orange
grain / halation / bloom / flare are separate optional systems
```

---

# Phase 5 - Physical Realism and Anti-AI Intelligence

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

Completed tasks:

```text
5.1 anti-AI artifact taxonomy                       COMPLETE
5.2 skin realism system                             COMPLETE
5.3 hair and eye realism system                     COMPLETE
5.4 fabric and material realism system              COMPLETE
5.5 contact / gravity / environmental interaction  COMPLETE
5.6 reflection and shadow coherence                 COMPLETE
5.7 optical imperfection restraint                  COMPLETE
5.8 reusable Reality Gate                           COMPLETE
```

## 5.1 Anti-AI artifact taxonomy

Implemented structured diagnostic domains covering anatomy, skin, hair, eyes, fabric, materials, reflections, shadows, lighting, exposure, color, perspective, depth, motion, contact, atmosphere, patterns, text, optical effects and cinematic overprocessing.

Hard rule:

```text
AI-looking != regenerate everything
```

## 5.2 Skin realism

Implemented region-specific texture, subtle color variation, source-consistent specular response, age/context-appropriate detail, makeup distinction, focus coherence and identity-preserving repair.

Hard rules:

```text
real skin != pore overlay
beauty != plastic
realism != aging the subject
identity preservation outranks cosmetic AUTO changes
```

## 5.3 Hair and eye realism

Implemented hair mass/silhouette, gravity, clump hierarchy, restrained flyaways, directional specular response, gaze coherence, eyelid/globe geometry, sclera/iris/pupil realism and source-consistent catchlights.

Hard rules:

```text
real hair != thousands of perfect strands
flyaways != mandatory realism
real eyes != glass marbles
catchlights != decorative dots
```

## 5.4 Fabric and material realism

Status: COMPLETE
Evidence: `references/fabric-and-material-realism.md`

Implemented:

- scale-aware microdetail;
- fabric weight/stiffness/stretch/drape;
- force-driven fold logic;
- weave/fiber restraint;
- anisotropic reflection language;
- leather, metal, glass, plastic, wood, stone/concrete/plaster and painted-surface behavior;
- wetness/moisture;
- context-driven dust/dirt/fingerprints/wear;
- clean commercial product exception;
- material separation under common lighting;
- preservation-aware repair order.

Hard rules:

```text
realism != more texture
fabric folds require forces
material roughness must affect highlights/reflections
microdetail must respect scale
imperfection must be contextual
clean commercial imagery can still be realistic
```

## 5.5 Contact, gravity, and environmental interaction

Status: COMPLETE
Evidence: `references/contact-gravity-environment.md`

Implemented:

- support/load-bearing contact;
- weight/posture;
- ground contact across sand/snow/mud/hard floors;
- body/clothing interaction;
- hand/object contact;
- wind as a shared environmental field;
- water/moisture behavior;
- dust/sand/snow/smoke/particle interaction;
- object stability;
- soft-surface compression;
- footprints/tracks/disturbance;
- environment-to-subject continuity;
- clean-commercial contact rules;
- minimal repair order.

Hard rules:

```text
contact shadow != contact geometry
weight must have support
wind is shared but material-dependent
environment interaction must have a cause
clean imagery can remain pristine
```

## 5.6 Reflection and shadow coherence

Status: COMPLETE
Evidence: `references/reflection-shadow-coherence.md`

Implemented:

- shadow direction and softness;
- contact shadows;
- shadow density/color;
- reflection viewpoint/roughness/curvature logic;
- eye catchlights;
- glass/refraction;
- mirrors;
- automotive reflections;
- controlled product reflection cards;
- wet surfaces;
- atmosphere;
- motion coherence;
- multi-source mapping;
- preservation-aware repair order.

Hard rules:

```text
shadow and reflection logic share one scene geometry
contact shadow cannot rescue floating geometry
roughness changes reflection structure
catchlights require sources
mirror content must obey viewpoint
beauty highlights still need physical motivation
```

## 5.7 Optical imperfection without fake vintage spam

Status: COMPLETE
Evidence: `references/optical-imperfection.md`

Implemented separate, restrained handling for:

- focus falloff;
- edge softness;
- field/aberration character;
- chromatic aberration;
- distortion;
- flare/ghosting;
- veiling glare;
- bloom;
- halation;
- grain/noise;
- anamorphic behavior;
- vintage and modern lens strategies;
- low-fi capture artifacts.

Hard rules:

```text
imperfection != realism
vintage != every defect at once
modern != sterile
flare requires source geometry
halation != bloom != flare
distortion != perspective
```

## 5.8 Reality Gate

Status: COMPLETE
Evidence: `references/reality-gate.md`

Reusable gate order:

```text
intent / locks / preservation
-> geometry / perspective
-> focus / depth / motion
-> lighting
-> exposure / color
-> shadows / reflections / refractions
-> anatomy / skin / hair / eyes
-> fabric / materials
-> contact / gravity / environment
-> atmosphere / particles
-> optical effects / texture
-> stylization restraint
-> provider translation integrity
```

Gate outcomes:

```text
PASS
PASS_WITH_NOTES
REPAIR_REQUIRED
BLOCKED_BY_CONSTRAINT
```

Repair priority:

```text
P0 structural blockers
P1 physical coherence
P2 realism surfaces
P3 finish / cliche effects
```

Hard rules:

```text
physical coherence before decorative finish
locks before AUTO
preservation before repair drift
geometry before texture
light/material/contact must agree
imperfection is optional
stylization may bend realism but must remain internally coherent
```

# Phase 5 Gate

Status: PASSED
Evidence: `PHASE_5_AUDIT.md`

Gate cases verified:

1. waxy AI portrait;
2. fashion image with floating/repeated fabric;
3. pristine glossy product with fake reflections;
4. wet automotive night frame;
5. clean bright commercial beauty frame;
6. intentionally stylized filmic frame;
7. preservation conflict during repair;
8. reference match with unknown hardware.

Audit result:

```text
scope violations: 0
standalone dependency violations: 0
provider-core contamination: 0
explicit-lock violations: 0
preservation-authority violations: 0
reference-certainty violations: 0
still-vs-video scope violations: 0
mandatory-vintage assumptions: 0
mandatory-dirt assumptions: 0
mandatory-grain assumptions: 0
```

Phase 5 gate requirement is satisfied: the skill can identify concrete reasons an image feels synthetic and produce a preservation-aware minimal repair plan.

---

# Phase 6 - Decision Engine and Workflows

Status: NOT STARTED
Goal: turn the completed cinematography and realism knowledge into reliable user-facing behavior for beginners and experts.

Next batch:

```text
6.1 AUTO DIRECT
6.2 CINEMATIZE
6.3 REALITY REPAIR
6.4 REFERENCE MATCH
6.5 MANUAL CAMERA
```

Remaining after that batch:

```text
6.6 PROMPT ONLY
6.7 progressive disclosure router
6.8 question-minimization policy
6.9 multi-image/reference behavior
Phase 6 gate
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
- beautify or redesign preserved human identity during Reality Repair;
- claim visual verification when no image was inspected.
