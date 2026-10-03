# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state and restart point for future chats/agents.

## Current State

- Phase 0: COMPLETE
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE
- Phase 1 gate: PASSED
- Phase 2: IN PROGRESS
- Task 2.1: COMPLETE
- Task 2.2: COMPLETE
- Task 2.3: COMPLETE
- Task 2.4: NEXT
- Task 2.5: NOT STARTED
- Phase 2 progress: **3 / 5 tasks complete**

Next task: **2.4 - Define confidence and uncertainty semantics**

---

# Phase 0 - Architecture, Scope, and Governance

Status: COMPLETE

## 0.1 Package identity and routing

Status: COMPLETE

Evidence: `references/routing.md`

Frozen identity:

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
```

## 0.2 Standalone portability

Status: COMPLETE

Evidence: `references/portability.md`

Core guarantees:

- no required parent-repo knowledge;
- no sibling-skill dependency;
- no AI-Verse OS requirement for reasoning/prompt-only operation;
- no MCP requirement;
- no API key required for prompt-only use;
- package-local references/adapters/schemas;
- isolated-folder V1 release test required.

## 0.3 Host capability degradation

Status: COMPLETE

Evidence: `references/host-capabilities.md`

H1-H6 host classes cover native generation/editing through text-only operation. Every class has a useful truthful result path.

## 0.4 Explicit locks

Status: COMPLETE

Evidence: `references/locks.md`

User-supplied values and preservation requirements are locks. Unspecified values remain AUTO. Provider defaults cannot silently override locks.

## 0.5 Success/failure contract

Status: COMPLETE

Evidence: `references/success-contract.md`

Top-level states:

```text
success
partial
blocked
failed
```

Verification levels:

```text
V0 reasoning only
V1 execution confirmed
V2 visual inspection completed
V3 comparative/iterative acceptance
```

## Phase 0 Post-Research Re-Audit

Status: PASSED

Evidence: `PHASE_0_AUDIT.md`

After Phase 1 research began landing:

```text
Architecture violations: 0
Standalone violations: 0
Scope violations: 0
Lock violations: 0
Host-capability violations: 0
Success-contract violations: 0
Research-isolation violations: 0
```

---

# Phase 1 - Research Corpus and Provenance

Status: COMPLETE

Gate: PASSED

## 1.1 Source ledger framework

Status: COMPLETE

Evidence:

- `references/source-ledger.md`
- `references/source-ledger-addendum.md`

Evidence classes:

- CONFIRMED
- CORROBORATED
- MODEL-BEHAVIOR
- PROVIDER-SPECIFIC
- INFERRED

## 1.2 Magnific public evidence

Status: COMPLETE

Evidence: `references/research/magnific.md`

Captured live Cinematic model controls, camera/lens/focal/aperture/shot ontology, film stocks/movie looks, lighting, blur, grain, halation, tonal controls, structure-preservation/repair concepts, and the boundary around unknowable private internals.

## 1.3 Higgsfield public evidence

Status: COMPLETE

Evidence: `references/research/higgsfield.md`

Captured Soul Cinema role, Cinema Studio philosophy, cinematography vocabulary as model visual priors, DP/operator testing, lens-character amplification, prompt enhancement/AUTO principles, Soul ID/color continuity concepts, hero-frame workflow, and version drift.

## 1.4 Camera manufacturer knowledge

Status: COMPLETE

Evidence: `references/research/cameras.md`

First-party evidence for ARRI, Sony, RED, Canon and Blackmagic. IMAX/65-70mm deeper translation remains registered research debt.

## 1.5 Lens manufacturer knowledge

Status: COMPLETE

Evidence:

- `references/research/lenses.md`
- `references/research/lenses-supplement.md`

Strong/usable evidence covers ARRI Signature, ARRI/ZEISS Master Prime, Leitz SUMMILUX-C, Panavision G-Series, Cooke Panchro Classic, ZEISS Supreme/Radiance, Hawk V-Lite and Angenieux Optimo. Canon K35 detailed character remains conservative.

## 1.6 Film stock / photochemical knowledge

Status: COMPLETE

Evidence: `references/research/film-stocks.md`

Strong Kodak motion-stock evidence plus negative/reversal, white-balance, grain, halation and tonal-response distinctions.

## 1.7 Lighting / cinematography fundamentals

Status: COMPLETE

Evidence: `references/research/lighting.md`

Captured motivated lighting, source-size/softness, falloff, negative fill, bounce, practicals, sun/sky/window logic, exposure hierarchy, specular/diffuse response, atmosphere and mixed-source logic.

## 1.8 Color and display-independent visual principles

Status: COMPLETE

Evidence: `references/research/color-and-tone.md`

Captured scene-referred vs display-referred distinction, highlight rolloff, hue preservation, gamut/saturation discipline, skin/environment separation, white balance, density, black levels, display-independent language and color Reality Gate questions.

## 1.9 Current model-provider prompting guidance

Status: COMPLETE

Evidence: `references/research/provider-prompting.md`

Official/current guidance captured for OpenAI GPT Image, Gemini native image generation, Seedream, FLUX, Magnific and Higgsfield while preserving a model-independent core.

## 1.10 Secondary public skills/workflows

Status: COMPLETE

Evidence: `references/research/secondary-public-workflows.md`

Secondary public material is restricted to architecture/test hypotheses and cannot outrank first-party evidence.

## 1.11 Research gap audit

Status: COMPLETE

Evidence: `references/research/research-gap-audit.md`

Registered research debt:

- RG-001 IMAX / 65-70mm translation;
- RG-002 Canon K35 detailed character;
- RG-003 selected non-Kodak stock depth;
- RG-004 physical-realism/material taxonomy for Phase 5;
- RG-005 cross-provider empirical calibration for Phase 9;
- RG-006 continuous provider-version drift.

None blocks Phase 2.

---

# Phase 2 - Cinematic Shot Ontology and Structured Contracts

Status: IN PROGRESS

Goal: create one provider-neutral internal language capable of representing beginner AUTO shots, expert locked shots, image repairs, and reference matches.

## 2.1 Define `cinematic-shot-spec.schema.json`

Status: COMPLETE

Evidence: `schemas/cinematic-shot-spec.schema.json`

Implemented a Draft 2020-12 provider-neutral schema covering:

- operation/mode;
- creative intent and purpose;
- scene/environment/action;
- subjects and hierarchy;
- framing, shot size, camera height/angle/distance and perspective;
- capture format and camera character;
- lens family plus observable lens behavior;
- focal length, aperture, focus and depth;
- lighting motivation, key/fill/practicals/ambient/bounce/negative fill;
- exposure, highlights, shadows and specular strategy;
- white balance, palette, separation, saturation, density and tone;
- film/tonal response, grain, halation, bloom, flare and sharpness;
- physical realism fields;
- preserve / repair / allow-change / avoid constraints;
- field-level parameter states and locks;
- reference bindings;
- provider adaptation isolated from core truth;
- Reality Gate carrier;
- output status and provenance.

Key invariants:

- explicit locks can be represented without being overwritten by AUTO;
- perspective is represented separately from focal-length mythology;
- lens name is separated from observable lens character;
- provider parameters live only in an adapter-owned block;
- prompt/output execution fields do not become the core cinematic model.

Acceptance: PASSED

## 2.2 Define `realism-diagnosis.schema.json`

Status: COMPLETE

Evidence: `schemas/realism-diagnosis.schema.json`

Implemented structured representation for:

- whether the image was actually available for inspection;
- overall artificiality level and severity;
- domain-specific findings;
- visual evidence and confidence;
- likely cause and visual impact;
- preservation conflicts;
- explicit preserve boundaries;
- repair targets and priorities;
- allowed changes;
- minimal-change repair strategy;
- single-edit, multi-region, multi-pass, regeneration and diagnosis-only paths;
- provider handoff without assuming a provider exists;
- post-edit preservation/realism verification;
- provenance.

The domain taxonomy includes perspective, focus/DOF, light, shadows, exposure, color, skin, hair, anatomy, fabric, materials, roughness, reflections/refractions, contact, gravity/weight, atmospheric depth, grain, bloom/halation, flare, sharpness, motion blur, composition, repetition and geometry.

Key invariant: Reality Repair is represented as **diagnose -> preserve -> repair -> allow change -> verify**, not uncontrolled regeneration.

Acceptance: PASSED

## 2.3 Define `reference-dna.schema.json`

Status: COMPLETE

Evidence: `schemas/reference-dna.schema.json`

Implemented structured representation for:

- one or multiple reference sources and their roles;
- observed composition;
- perspective;
- focus/depth;
- lighting;
- exposure/tone;
- color;
- texture;
- atmosphere;
- materials;
- production design;
- imperfections;
- optional motion signature visible in a still;
- transferable visual DNA;
- content-specific/non-transferable features;
- supplied metadata;
- uncertain hardware hypotheses;
- known unknowns and prohibited claims;
- target-transfer instructions;
- provenance.

Critical separation:

```text
OBSERVABLE VISUAL TRAIT
!=
EXACT HARDWARE FACT
```

Exact camera/lens/stock information may be stored as fact only when supplied by the user, embedded metadata, or another documented external source. Visually inferred hardware is forced into `hardware_hypotheses` with `assertion_level: hypothesis_only`.

This prevents the reference matcher from claiming exact unavailable metadata while still allowing useful focal/camera/lens-family hypotheses when needed.

Acceptance: PASSED

## 2.4 Define confidence and uncertainty semantics

Status: NEXT

Must formalize how numeric confidence and state labels map to:

- directly supplied user values;
- strongly inferred values;
- weakly inferred values;
- reference-observed values;
- known metadata;
- intentionally AUTO values;
- provider translations.

The first three Phase 2 schemas intentionally provide confidence/state carrier fields, but Task 2.4 remains authoritative for their interpretation.

## 2.5 Define parameter conflict resolution

Status: NOT STARTED

Must formalize structured reconciliation of technically tense or contradictory locks without silently changing the user's request.

# Phase 2 Gate

Status: NOT YET RUN

Run only after Tasks 2.4 and 2.5 are complete.

---

# Next

**Task 2.4 - Define confidence and uncertainty semantics**

After 2.4, Task 2.5 will complete conflict resolution and allow the Phase 2 gate to test whether one structured representation can cover beginner AUTO, expert locks, Reality Repair and Reference Match.

# Change Discipline

Phase 0 remains the governing architecture contract.

Research and structured contracts may not silently:

- expand the skill into temporal video authority;
- introduce required external runtime dependencies;
- turn one image provider into the core brain;
- override explicit user locks;
- convert marketing language into physical truth;
- turn secondary public skills into authoritative cinematography sources;
- treat inferred reference metadata as confirmed hardware fact.

Any later change that threatens these invariants triggers another architecture audit.
