# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state and restart point for future chats/agents.

## Current State

- Phase 0: COMPLETE
- Phase 0 gate: PASSED
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE
- Phase 1 gate: PASSED
- Phase 2: COMPLETE
- Phase 2 gate: PASSED
- Phase 3: IN PROGRESS
- Task 3.1: COMPLETE
- Task 3.2: COMPLETE
- Task 3.3: COMPLETE
- Task 3.4: COMPLETE
- Task 3.5: COMPLETE
- Task 3.6: NEXT
- Task 3.7: NOT STARTED
- Phase 3 progress: **5 / 7 tasks complete**

Next chunk under the agreed phase-splitting rule: **Tasks 3.6 and 3.7, then run the Phase 3 gate.**

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

Core structured distinctions:

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

Status: IN PROGRESS

Agreed split:

```text
Chunk 1: 3.1 - 3.3                         COMPLETE
Chunk 2: 3.4 - 3.5                         COMPLETE
Chunk 3: 3.6 - 3.7 + Phase 3 gate          NEXT
```

## 3.1 Visual intent and story-to-shot reasoning

Status: COMPLETE
Evidence: `references/visual-intent.md`

Key rule:

```text
story -> viewer relationship -> hierarchy -> composition -> camera -> lens -> light -> grade
```

Implemented beginner AUTO behavior, expert-lock coexistence, viewer relationship, visual hierarchy, purpose-specific reasoning, realism targets, question minimization and anti-cliche behavior.

## 3.2 Composition and blocking

Status: COMPLETE
Evidence: `references/composition-and-blocking.md`

Implemented shot sizes, subject placement, headroom, gaze room, hierarchy, foreground/midground/background layers, negative space, symmetry/asymmetry, camera height, POV/OTS/profile/rear/top-down logic, three-dimensional blocking, multi-subject relationships, cropping discipline, frozen-moment multi-camera consistency and rectilinear wide-angle foreground exaggeration without fisheye.

## 3.3 Capture formats and camera-character reference

Status: COMPLETE
Evidence: `references/cameras-and-capture-formats.md`

Implemented capture medium vs format vs named camera vs camera character, AUTO selection, named-camera locks, dynamic-range/color-science translation, ARRI/Sony/RED/Canon/Blackmagic references, film gauges, 65/70mm caution, medium format, VHS/analog video and low-fi digital.

Hard rules:

```text
camera name != complete look
log/gamut != final grade
format != perspective
large format != automatically shallow DOF
manufacturer stop count != literal AI-image dynamic range
```

## 3.4 Lens-character reference

Status: COMPLETE
Evidence: `references/lens-character.md`

Implemented:

- observable lens-character axes: contrast, microcontrast, edge behavior, focus falloff, bokeh, flare, chromatic behavior, distortion, anamorphic behavior and breathing relevance;
- story-led AUTO lens-character selection;
- strict preservation of user lens locks;
- provider translation without claiming literal simulation;
- runtime mappings for ARRI Signature, ARRI/ZEISS Master Prime, Leitz SUMMILUX-C, ZEISS Supreme/Radiance, Cooke Panchro Classic, restrained Cooke S4-type character, Panavision G-Series, Hawk V-Lite and Angenieux Optimo;
- conservative Canon K35 handling due weaker evidence;
- hard separation of lens family, focal length and aperture;
- source-motivated flare policy;
- bokeh/depth coherence;
- character-lens restraint;
- anamorphic anti-caricature rules;
- reference-match hardware uncertainty;
- lens Reality Gate.

Hard rules:

```text
anamorphic != blue horizontal flare preset
vintage lens != blurry everything
modern lens != oversharpened everything
fast lens != always wide open
lens family != focal length
```

Acceptance: PASSED

## 3.5 Focal length, distance, and perspective

Status: COMPLETE
Evidence: `references/focal-length-and-perspective.md`

Implemented:

- hard rule that perspective comes primarily from camera position relative to the scene;
- joint reasoning across capture format, camera distance, focal length and framing;
- field-of-view vs perspective distinction;
- equivalent framing across formats;
- wide-angle and long-lens strategies without mythology;
- extreme foreground scale using close rectilinear perspective rather than global fisheye distortion;
- rectilinear vs fisheye separation;
- portrait, product, automotive, architecture/interior, OTS, top-down and macro perspective logic;
- reference-match perspective inference without unsupported exact focal claims;
- perspective vs lens-character separation;
- perspective vs depth-of-field separation;
- canonical conflict handling for 14mm/no-fisheye and frozen-scene camera changes;
- provider-neutral prompt translation;
- perspective Reality Gate.

Hard rules:

```text
perspective != focal length alone
wide lens != fisheye
telephoto != compression by itself
large format != epic perspective
macro != high detail token
```

Acceptance: PASSED

## 3.6 Aperture, focus, and depth behavior

Status: NEXT

Must cover aperture choice, focus plane, subject/background distance, shallow/deep focus, rack-focus-like still cues only where meaningful, and avoidance of default maximum blur.

## 3.7 Motion and shutter language for still frames

Status: NOT STARTED

Must cover believable frozen motion, subject motion blur, camera motion blur, shutter-language cues and physical consistency in still imagery.

# Phase 3 Gate

Status: NOT YET RUN

Run after 3.6 and 3.7.

Gate requirement:

> Given only subject + context, the skill can design a coherent camera setup without generic cinematic filler while preserving expert locks and physical plausibility.

---

# Next

**Final Phase 3 chunk: Tasks 3.6 and 3.7, then Phase 3 gate.**

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
- use lens names as decorative prestige tokens;
- turn cinematic aesthetics into mandatory clichés.

Any later change that threatens these invariants triggers another architecture audit.
