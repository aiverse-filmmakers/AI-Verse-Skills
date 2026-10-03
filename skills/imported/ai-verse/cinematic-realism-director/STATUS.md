# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state and restart point for future chats/agents.

## Current State

- Phase 0: COMPLETE
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE
- Phase 1 gate: PASSED
- Phase 2: COMPLETE
- Phase 2 gate: PASSED
- Phase 3: IN PROGRESS
- Task 3.1: COMPLETE
- Task 3.2: COMPLETE
- Task 3.3: COMPLETE
- Task 3.4: NEXT
- Phase 3 progress: **3 / 7 tasks complete**

Next chunk under the agreed phase-splitting rule: **Tasks 3.4 and 3.5**.

---

# Phase 0 - Architecture, Scope, and Governance

Status: COMPLETE
Gate: PASSED

Evidence:

- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

Core invariants:

- first-party package identity: `cinematic-realism-director`;
- still-image direction/realism is primary scope;
- standalone-folder operation is mandatory;
- no required AI-Verse OS, MCP, sibling skill or API key for prompt-only reasoning;
- image-capable hosts execute, weaker hosts degrade truthfully;
- explicit user values and preservation requirements remain locks;
- success/partial/blocked/failed remain distinct;
- tool execution is not automatically visual-quality verification.

Post-research architecture re-audit passed with zero contract violations.

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

Completed tasks:

```text
1.1 source ledger framework                         COMPLETE
1.2 Magnific public evidence                       COMPLETE
1.3 Higgsfield public evidence                     COMPLETE
1.4 camera manufacturer knowledge                  COMPLETE
1.5 lens manufacturer knowledge                    COMPLETE
1.6 film stock / photochemical knowledge           COMPLETE
1.7 lighting / cinematography fundamentals         COMPLETE
1.8 color / display-independent principles         COMPLETE
1.9 provider prompting guidance                    COMPLETE
1.10 secondary public workflow review              COMPLETE
1.11 research gap audit                            COMPLETE
```

Research debt remains explicitly registered rather than guessed.

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

Completed tasks:

```text
2.1 cinematic shot spec                            COMPLETE
2.2 realism diagnosis schema                       COMPLETE
2.3 reference DNA schema                           COMPLETE
2.4 confidence / uncertainty semantics             COMPLETE
2.5 parameter conflict resolution                  COMPLETE
```

Core structured distinctions preserved:

```text
provider-neutral truth != provider syntax
observation != exact hardware fact
confidence != authority
AUTO != unknown
user lock != inference
preservation lock != creative preference
```

The Phase 2 gate verified beginner AUTO, expert locked shots, Reality Repair, and Reference Match.

---

# Phase 3 - Core Cinematography Knowledge Base

Status: IN PROGRESS
Goal: build the foundational camera, composition, lens, perspective, focus, and still-motion intelligence.

Agreed execution split for this 7-task phase:

```text
Chunk 1: 3.1 - 3.3
Chunk 2: 3.4 - 3.5
Chunk 3: 3.6 - 3.7 + Phase 3 gate
```

## 3.1 Visual intent and story-to-shot reasoning

Status: COMPLETE

Evidence: `references/visual-intent.md`

Implemented:

- story-first cinematography decision order;
- beginner AUTO behavior from minimal input;
- expert-lock coexistence;
- viewer relationship classes: intimate, observational, participatory, detached, iconic/heroic;
- information hierarchy;
- emotional-target to visual-strategy mapping;
- purpose-specific reasoning for narrative, commercial, editorial/fashion, documentary, portrait, product, automotive, food, architecture, travel and storyboard work;
- context-preservation logic;
- realism-target levels;
- ambiguity/question-minimization rules;
- anti-cliche guard against automatic shallow DOF, anamorphic flare, teal/orange, haze, grain, halation, rim light, etc.;
- intent-level Reality Gate questions.

Key rule:

```text
story -> viewer relationship -> hierarchy -> composition -> camera -> lens -> light -> grade
```

not:

```text
camera/lens preset -> force story into it
```

Acceptance: PASSED

## 3.2 Composition and blocking

Status: COMPLETE

Evidence: `references/composition-and-blocking.md`

Implemented:

- shot-size reasoning;
- subject placement;
- headroom;
- lead/gaze room;
- visual hierarchy beyond blur;
- foreground/midground/background layering;
- negative space;
- symmetry/asymmetry;
- camera-height logic;
- frontal, profile, three-quarter, rear, OTS, POV and dutch-angle logic;
- true 90-degree top-down rules;
- three-dimensional blocking;
- multi-subject relationships;
- high-angle and standard OTS behavior;
- environmental, product, automotive and architecture composition;
- cropping/anatomy discipline;
- frozen-moment multi-camera consistency;
- reference-frame camera-change logic where the scene stays fixed and only the camera moves;
- anti-filler rules for generic composition clichés.

Special rectilinear-wide rule:

A deliberately huge foreground hand/shoe/prop may be produced through physical proximity and wide rectilinear perspective without turning the whole frame into fisheye/circular distortion.

Acceptance: PASSED

## 3.3 Capture formats and camera-character reference

Status: COMPLETE

Evidence: `references/cameras-and-capture-formats.md`

Implemented runtime translation for:

- capture medium vs format vs named camera vs camera character;
- provider-neutral AUTO capture behavior;
- named-camera locks;
- camera reference vs literal camera fact;
- dynamic-range translation into visible tonal behavior;
- acquisition color-science vs final-grade separation;
- format/focal/field-of-view relationships;
- explicit rule that format does not automatically mean shallow DOF;
- ARRI ALEXA 35;
- Sony VENICE 2;
- RED V-RAPTOR / [X];
- Canon C500 Mark II;
- Blackmagic URSA Mini Pro;
- 35mm film;
- 16mm;
- 8mm;
- cautious 65/70mm reference;
- medium format;
- analog video/VHS;
- low-fi digital / Pixelvision-type response;
- purpose-led capture selection;
- camera vs lens responsibility;
- camera vs grade responsibility;
- camera vs texture responsibility;
- reference-match hardware uncertainty;
- provider translation boundaries.

Hard rules:

```text
camera name != complete look
log/gamut != final grade
format != perspective
large format != automatically shallow DOF
manufacturer stop count != literal AI-image dynamic range
```

Acceptance: PASSED

## 3.4 Lens-character reference

Status: NEXT

Will turn the verified Phase 1 lens evidence into runtime mappings for contrast, microcontrast, flare, veiling glare, focus falloff, bokeh, edge behavior, chromatic artifacts, anamorphic behavior and lens-family restraint.

## 3.5 Focal length, distance, and perspective

Status: NOT STARTED

Hard rule already carried forward:

> Perspective comes primarily from camera position/distance. Focal length and format determine field of view for that position.

## 3.6 Aperture, focus, and depth behavior

Status: NOT STARTED

## 3.7 Motion and shutter language for still frames

Status: NOT STARTED

# Phase 3 Gate

Status: NOT YET RUN

Run after 3.6 and 3.7 are complete.

The gate must prove that a subject + context alone is enough for the skill to design a coherent camera setup without generic cinematic filler while still preserving expert locks.

---

# Next

**Chunk 2 of Phase 3: Tasks 3.4 and 3.5**

1. `3.4 Lens-character reference`
2. `3.5 Focal length, distance, and perspective`

Then Chunk 3 will complete 3.6, 3.7 and the Phase 3 gate.

---

# Change Discipline

Phase 0 remains the governing architecture contract.

Later phases may not silently:

- expand the skill into temporal video authority;
- introduce required external runtime dependencies;
- turn one provider into the core brain;
- override explicit user locks;
- treat inferred reference hardware as known fact;
- convert marketing language into physical truth;
- turn secondary public skills into authoritative cinematography sources;
- use focal length as a false substitute for camera position;
- turn cinematic aesthetics into mandatory clichés.

Any later change that threatens these invariants triggers another architecture audit.