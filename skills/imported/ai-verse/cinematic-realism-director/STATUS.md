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
- Next task: **3.1 - Visual intent and story-to-shot reasoning**

---

# Phase 0 - Architecture, Scope, and Governance

Status: COMPLETE

Evidence:

- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

Core invariants remain frozen:

- first-party package identity: `cinematic-realism-director`;
- still-image direction/realism is the primary scope;
- standalone-folder operation is mandatory;
- no required AI-Verse OS, MCP, sibling skill or API key for prompt-only reasoning;
- image-capable hosts execute, weaker hosts degrade truthfully;
- explicit user values and preservation requirements remain locks;
- success/partial/blocked/failed are distinct;
- tool execution is not automatically visual-quality verification.

Post-research architecture re-audit: PASSED with zero contract violations.

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

Research debt remains explicitly registered rather than guessed, including IMAX/65-70mm deeper translation, Canon K35 character depth, selected non-Kodak stocks, Phase 5 material-realism taxonomy, Phase 9 provider calibration, and ongoing provider-version drift.

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

## 2.1 Cinematic Shot Spec

Status: COMPLETE

`schemas/cinematic-shot-spec.schema.json` provides the provider-neutral universal representation for:

- operation/mode;
- intent and purpose;
- scene/action/environment;
- subject hierarchy;
- composition, camera height/angle/distance and perspective;
- capture format/camera character;
- lens family and observable lens character;
- focal length, aperture, focus and depth;
- motivated lighting and exposure;
- color/tone;
- film/texture/finish;
- physical realism;
- preserve/repair/allow-change constraints;
- parameter states and locks;
- reference bindings;
- provider adaptation as a downstream layer;
- Reality Gate carrier;
- output and provenance.

Key invariant:

```text
provider-neutral cinematic truth
!=
provider-specific syntax
```

## 2.2 Realism Diagnosis Schema

Status: COMPLETE

`schemas/realism-diagnosis.schema.json` formalizes:

```text
diagnose
-> preserve
-> repair
-> allow change
-> verify
```

It carries findings, severity, evidence, repair priorities, preservation boundaries, provider handoff and post-edit verification.

## 2.3 Reference DNA Schema

Status: COMPLETE

`schemas/reference-dna.schema.json` separates:

```text
observable visual DNA
transferable DNA
content-specific details
supplied metadata
hardware hypotheses
uncertainty
```

Exact hardware may only be represented as fact when supported by user input, metadata or another authoritative source.

## 2.4 Confidence and Uncertainty Semantics

Status: COMPLETE

Evidence:

- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`

Semantic states distinguish:

- explicit user value;
- preservation requirement;
- direct observation;
- metadata-confirmed fact;
- strong inference;
- medium inference;
- weak inference;
- AUTO-selected value;
- intentionally open AUTO value;
- provider translation;
- unknown;
- not applicable.

Core rule:

```text
confidence describes evidence
lock state describes authority
```

A low-confidence inference can never override a hard user lock.

The shot schema's numeric confidence carrier is explicitly ordinal, not a calibrated probability. Canonical V1 serialization maps semantic confidence to compact state/ordinal values without exposing fake percentages to users.

## 2.5 Parameter Conflict Resolution

Status: COMPLETE

Evidence: `references/parameter-conflicts.md`

Conflict classes:

```text
C0 compatible
C1 tension but reconcilable
C2 direct contradiction
C3 provider execution conflict
```

Rules:

- preserve explicit locks first;
- solve C1 tension through unlocked/AUTO fields before touching locks;
- never hide a C2 contradiction;
- provider limitations translate observable intent rather than fabricate controls;
- reference DNA cannot silently override target locks;
- preservation-vs-repair conflicts use the narrowest necessary change boundary;
- unresolved hard-lock violations cannot produce full `success`.

Canonical cases verified:

- 14mm + request for reduced wide-angle distortion;
- f/1.2 + deep-focus request;
- 65/70mm capture reference + VHS finish;
- lighting, color, preservation, reference-transfer and provider conflicts.

# Phase 2 Gate

Status: PASSED

Evidence: `PHASE_2_AUDIT.md`

The structured system successfully represents all four required classes:

```text
BEGINNER AUTO
EXPERT LOCKED SHOT
REALITY REPAIR
REFERENCE MATCH
```

while preserving the distinction between:

```text
fact
observation
inference
AUTO creative choice
user lock
preservation lock
provider translation
unknown
```

No Phase 0 invariant was broken.

---

# Next

**Task 3.1 - Visual intent and story-to-shot reasoning**

Phase 3 will build the core cinematography knowledge engine on top of the completed structured contracts. It should convert narrative/commercial intent into visual decisions rather than applying generic cinematic presets.

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
- turn secondary public skills into authoritative cinematography sources.

Any later change that threatens these invariants triggers another architecture audit.
