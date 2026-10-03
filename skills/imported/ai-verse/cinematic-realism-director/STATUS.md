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
- Phase 4: IN PROGRESS
- Task 4.1: COMPLETE
- Task 4.2: COMPLETE
- Task 4.3: COMPLETE
- Task 4.4: COMPLETE
- Task 4.5: COMPLETE
- Task 4.6: NEXT
- Task 4.7: NOT STARTED
- V1 task progress: **33 / 93 tasks complete**

Agreed execution rule from this point forward:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

Next batch:

```text
4.6 Color science and grading strategy
4.7 Grain, halation, bloom, flare, and texture restraint
Phase 4 gate
5.1 Build anti-AI artifact taxonomy
5.2 Skin realism system
5.3 Hair and eye realism system
```

This produces five numbered tasks while also completing and gating Phase 4 before continuing into Phase 5.

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
first-party package identity
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

Research debt remains registered rather than guessed.

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

Completed tasks:

```text
3.1 visual intent / story-to-shot                   COMPLETE
3.2 composition and blocking                       COMPLETE
3.3 capture formats / camera character             COMPLETE
3.4 lens character                                 COMPLETE
3.5 focal length / distance / perspective          COMPLETE
3.6 aperture / focus / depth                       COMPLETE
3.7 motion / shutter for stills                    COMPLETE
```

Phase 3 established one coherent camera foundation covering visual intent, composition, capture format, lens behavior, geometry, depth, and still-frame motion without generic cinematic filler.

---

# Phase 4 - Lighting, Exposure, Film Response, and Color

Status: IN PROGRESS
Goal: build physically motivated lighting, exposure, capture-response, color, and texture systems.

## 4.1 Motivated-lighting engine

Status: COMPLETE
Evidence: `references/motivated-lighting.md`

Implemented:

- source-first lighting design;
- M0 available-light, M1 enhanced-naturalism, M2 stylized-motivation, M3 expressionistic motivation levels;
- dominant source selection;
- direction, apparent source size, falloff and ambient logic;
- light/material interaction;
- atmosphere/light-path logic;
- lighting/exposure coupling;
- geometric portrait-pattern handling;
- AUTO behavior by purpose;
- user lighting locks;
- reference-match observation without fixture/wattage hallucination;
- motivated-lighting Reality Gate.

Hard rule:

```text
cinematic lighting starts from why/where/how the light exists
not from a list of fashionable lighting labels
```

Acceptance: PASSED

## 4.2 Key, fill, negative fill, edge, bounce, and practical logic

Status: COMPLETE
Evidence: `references/lighting-roles.md`

Implemented distinct roles and omission rules for:

- key;
- fill;
- negative fill;
- edge/back light;
- bounce;
- practicals;
- ambient light.

Also implemented portrait, product, automotive, exterior, night and mixed-source examples plus role-specific failure checks.

Hard rules:

```text
not every shot needs every lighting role
negative fill removes light; it does not add black
rim light is optional and must be source-motivated
practicals have local influence, not magical room-wide reach
bounce must have a plausible surface and color
```

Acceptance: PASSED

## 4.3 Environment-specific lighting recipes

Status: COMPLETE
Evidence: `references/environment-lighting-recipes.md`

Implemented adaptive decision recipes for:

- overcast exterior;
- hard noon sun;
- golden hour;
- blue hour;
- window daylight interior;
- tungsten practical interior;
- fluorescent/office;
- neon city night;
- moonlit exterior;
- candle/firelight;
- commercial soft source;
- documentary available light;
- glossy and matte product studio;
- automotive day/night;
- food/tabletop;
- architecture interior/exterior;
- forest/dappled light;
- snow;
- desert;
- rain/wet night.

Recipes are decision patterns, not fixed prompt templates.

Acceptance: PASSED

## 4.4 Exposure and dynamic-range behavior

Status: COMPLETE
Evidence: `references/exposure-and-dynamic-range.md`

Implemented:

- exposure hierarchy;
- subject-priority logic by purpose;
- highlight protection without universal recovery;
- intentional clipping rules;
- shadow-density classes;
- midtone placement;
- scene vs local contrast distinction;
- dynamic-range translation without fake stop-count simulation;
- camera/film exposure-response integration;
- interior/window strategies;
- night exposure hierarchy;
- bright- and dark-environment behavior;
- intentional under/overexposure;
- HDR and clipping failure taxonomy;
- exposure-lock and reference-match rules;
- Exposure Reality Gate.

Hard rules:

```text
dynamic range != everything visible
good highlights != no clipping anywhere
dense shadows != crushed blacks
cinematic exposure != HDR recovery
manufacturer stop count != literal generated-image capability
```

Acceptance: PASSED

## 4.5 Film stock and sensor response mapping

Status: COMPLETE
Evidence: `references/film-and-sensor-response.md`

Implemented runtime mappings for:

- high-end digital cinema response;
- ARRI ALEXA 35;
- Sony VENICE 2;
- RED V-RAPTOR;
- Canon C500 Mark II;
- Blackmagic URSA Mini Pro;
- generic 35mm motion negative;
- Kodak VISION3 500T;
- Kodak VISION3 250D;
- EASTMAN DOUBLE-X;
- EKTACHROME 100D;
- Portra;
- Ektar 100;
- T-MAX;
- 16mm;
- 8mm/Super-8-like intent;
- cautious 65/70mm intent;
- analog video/VHS;
- low-fi digital.

Also separated:

```text
stock/camera response
grain or sensor noise
halation
bloom
flare
white-balance relationship
final grade
```

Hard rules:

```text
film != warm + grain + faded
500T != orange
250D != blue
camera reference != literal sensor simulation
provider stock preset != universal stock truth
halation / bloom / flare are separate systems
```

Acceptance: PASSED

## 4.6 Color science and grading strategy

Status: NEXT

Must convert the Phase 1 color research into runtime rules for white balance, color separation, saturation, density, skin, black levels, highlight/shadow color and neutral vs stylized grades.

## 4.7 Grain, halation, bloom, flare, and texture restraint

Status: NOT STARTED

Must define these as optional, physically contextual effects rather than mandatory cinema tokens.

# Phase 4 Gate

Status: NOT YET RUN

Run after 4.6 and 4.7.

Gate requirement:

> The skill can construct lighting, exposure, film/sensor response, color and texture logic that feels physically motivated rather than procedurally decorated.

---

# Next

Complete 4.6 and 4.7, run the Phase 4 gate, then continue directly into Phase 5 Tasks 5.1-5.3 to satisfy the five-task minimum batch rule.

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
- use lens/camera/stock names as decorative prestige tokens;
- default cinematic images to shallow depth, grain, flare, halation, haze, rim light, teal/orange, or motion blur;
- force every tonal region into HDR-style equal visibility.

Any later change that threatens these invariants triggers another architecture audit.
