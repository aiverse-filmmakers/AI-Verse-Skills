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
- V1 task progress: **28 / 93 tasks complete**
- Next phase: **Phase 4 - Lighting, Exposure, Film Response, and Color**
- Phase 4 contains 7 tasks and follows the agreed thirds split:
  - Chunk 1: **4.1 - 4.3**
  - Chunk 2: **4.4 - 4.5**
  - Chunk 3: **4.6 - 4.7 + Phase 4 gate**

Next task: **4.1 - Motivated-lighting engine**

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

Execution split:

```text
Chunk 1: 3.1 - 3.3                         COMPLETE
Chunk 2: 3.4 - 3.5                         COMPLETE
Chunk 3: 3.6 - 3.7 + Phase 3 gate          COMPLETE
```

## 3.1 Visual intent and story-to-shot reasoning

Status: COMPLETE

Key decision order:

```text
story -> viewer relationship -> hierarchy -> composition -> camera -> lens -> light -> grade
```

The system does not begin from prestige camera/lens tokens.

## 3.2 Composition and blocking

Status: COMPLETE

Covers shot size, subject placement, headroom, gaze room, hierarchy, negative space, layers, symmetry/asymmetry, camera height, POV/OTS/profile/rear/top-down logic, 3D blocking, multi-subject relationships, crop discipline, frozen-moment camera changes and rectilinear wide-angle foreground exaggeration.

## 3.3 Capture formats and camera character

Status: COMPLETE

Hard rules:

```text
camera name != complete look
log/gamut != final grade
format != perspective
large format != automatically shallow DOF
manufacturer stop count != literal AI-image dynamic range
```

## 3.4 Lens character

Status: COMPLETE

Covers optical contrast, microcontrast, edge behavior, focus falloff, bokeh, flare, chromatic behavior, distortion, anamorphic behavior and evidence-based named lens mappings.

Hard rules:

```text
anamorphic != blue horizontal flare preset
vintage lens != blurry everything
modern lens != oversharpened everything
fast lens != always wide open
lens family != focal length
```

## 3.5 Focal length, distance, and perspective

Status: COMPLETE

Hard rules:

```text
perspective != focal length alone
wide lens != fisheye
telephoto != compression by itself
large format != epic perspective
macro != high detail token
```

## 3.6 Aperture, focus, and depth behavior

Status: COMPLETE
Evidence: `references/aperture-focus-and-depth.md`

Implemented:

- depth strategy classes: deep contextual, moderate separation, shallow selective, specialty razor-thin;
- AUTO decision order based on story information before aperture;
- aperture selection by purpose rather than prestige;
- explicit focus target and focus-plane coherence;
- subject/background/foreground distance logic;
- OTS, portrait, product, food, architecture, automotive and macro depth behavior;
- deep focus as a valid cinematic strategy;
- f/1.2 + deep-focus conflict handling through unlocked geometry first;
- reference-match depth inference without exact aperture hallucination;
- provider translation without invented native controls;
- anti-AI depth failures and Depth Reality Gate.

Hard rules:

```text
cinematic != shallow depth
fast lens != always wide open
f/1.2 != automatically better
bokeh != depth of field
large format != automatically shallow DOF
deep focus != video-looking
reference blur != exact aperture metadata
```

## 3.7 Motion and shutter language for still frames

Status: COMPLETE
Evidence: `references/motion-and-shutter.md`

Implemented:

- frozen, subtle-natural, subject-blur, camera-blur and long-exposure motion states;
- subject motion vs camera motion vs tracking/panning distinctions;
- qualitative shutter-language translation without false measured simulation;
- directional and differential motion across body/object regions;
- wind, water, particles, hair and fabric behavior;
- face/identity preservation in action imagery;
- camera-shake restraint;
- panning, zoom-blur and light-trail specialty behavior;
- motion vs focus separation;
- shadow/reflection coherence during motion;
- purpose-specific motion logic;
- reference-match motion inference without exact shutter hallucination;
- anti-AI motion failures and Motion Reality Gate.

Hard rules:

```text
cinematic != motion blur
handheld != blurry
motion blur != defocus
slow shutter != random smear
fast action != mandatory blur
pan != whole-frame uniform blur
still shutter language != temporal video direction
```

# Phase 3 Gate

Status: PASSED
Evidence: `PHASE_3_AUDIT.md`

Gate cases tested:

1. beginner narrative AUTO;
2. commercial/product AUTO;
3. architecture/interior AUTO;
4. action still with motion;
5. expert locked camera setup with a deliberate geometry conflict.

Results:

```text
scope violations: 0
standalone dependency violations: 0
provider-core contamination: 0
explicit-lock violations: 0
reference-certainty violations: 0
confidence/authority violations: 0
hidden conflict resolution: 0
still-vs-video scope violations: 0
```

Phase 3 now provides one coherent camera foundation covering:

```text
visual intent
composition / blocking
capture format / camera character
lens character
focal length / distance / perspective
aperture / focus / depth
motion / shutter appearance in stills
```

---

# Phase 4 - Lighting, Exposure, Film Response, and Color

Status: NOT STARTED

Agreed split for this 7-task phase:

```text
Chunk 1: 4.1 - 4.3
Chunk 2: 4.4 - 4.5
Chunk 3: 4.6 - 4.7 + Phase 4 gate
```

Next tasks:

```text
4.1 Motivated-lighting engine
4.2 Key, fill, negative fill, edge, bounce, and practical logic
4.3 Environment-specific lighting recipes
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
- use lens names as decorative prestige tokens;
- default every cinematic image to shallow depth, grain, flare, haze, rim light, teal/orange, or motion blur.

Any later change that threatens these invariants triggers another architecture audit.
