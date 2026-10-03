# Phase 2 Audit - Cinematic Shot Ontology and Structured Contracts

Status: PASSED

Branch: `feat/cinematic-realism-director`

Phase 2 goal:

> One structured representation must be able to describe beginner AUTO shots, expert locked shots, edit repairs, and reference matches without confusing fact, inference, creative choice, provider translation, or preservation constraints.

## Files Audited

- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/parameter-conflicts.md`
- `references/locks.md`
- `references/host-capabilities.md`
- `references/success-contract.md`

## Gate A - Beginner AUTO Shot

Test intent:

```text
woman waiting for a taxi in London at night
```

Required representation:

- simple user intent remains intact;
- no camera knowledge required from user;
- shot spec may AUTO-select framing, camera position, focal behavior, focus, light, exposure, color, texture and physical realism;
- AUTO values remain distinguishable from user locks;
- provider adaptation remains downstream;
- no unnecessary exact hardware claim is required.

Result: PASS

The Cinematic Shot Spec can represent the request with:

```text
operation = auto_direct
user-supplied intent/scene
AUTO composition/capture/lighting/color/finish
parameter_states = auto_selected or auto_open
provider_adaptation = optional downstream layer
```

No contradiction with Phase 0 portability or beginner-first behavior.

## Gate B - Expert Locked Shot

Test intent:

```text
70mm format, 25mm, f/1.2, low angle. Keep those exact choices.
```

Required representation:

- exact supplied values are preserved;
- unspecified parameters remain AUTO;
- confidence does not weaken user authority;
- unusual combinations are not rejected merely for being unusual;
- provider limitations cannot erase universal locks.

Result: PASS

Conceptual representation:

```text
capture.capture_format = 65/70mm reference
capture.focal_length = 25mm
capture.aperture = f/1.2
composition.camera_angle = low_angle

parameter_states:
- user_supplied + locked for each explicit value
- auto_selected / auto_open for unspecified values
```

`references/confidence-and-uncertainty.md` makes `user_supplied` provenance certain while keeping physical conflict analysis separate.

`references/parameter-conflicts.md` requires reconciliation through unlocked fields before any hard lock is touched.

## Gate C - Reality Repair

Test intent:

```text
Make this AI-looking portrait feel photographed. Keep identity, pose, composition and wardrobe unchanged. Fix waxy skin, fake hair, odd reflections and floating contact.
```

Required representation:

- source image availability/basis;
- observed artificiality and evidence;
- severity;
- preservation list;
- repair list;
- allowed-change list;
- repair strategy;
- uncertainty around suspected causes;
- verification of preservation after edit.

Result: PASS

`realism-diagnosis.schema.json` explicitly separates:

```text
findings
preserve
repair
allow_change
repair_strategy
verification
```

The universal shot spec can carry the repaired target shot, while the diagnosis schema carries why and what must change.

Conflict semantics correctly treat `preserve exact pose` + `repair malformed fingers` as potentially reconcilable at a narrower anatomical boundary rather than permission to regenerate the entire frame.

## Gate D - Reference Match

Test intent:

```text
Match this frame's cinematic look on a different subject, but do not pretend to know what exact camera or lens shot the reference.
```

Required representation:

- observable composition/perspective/depth/light/exposure/color/texture/atmosphere/material DNA;
- transferable vs content-specific properties;
- supplied metadata separated from visual hypotheses;
- exact hardware remains unknown unless actually supplied;
- target locks override conflicting reference properties.

Result: PASS

`reference-dna.schema.json` separates:

```text
observed_dna
transferable_dna
content_specific_features
metadata_and_hypotheses
uncertainty
target_transfer
```

`confidence-and-uncertainty.md` prevents a high-confidence visual observation from being escalated into a certain exact-hardware claim.

`parameter-conflicts.md` ensures reference DNA never silently overrides target locks.

## Gate E - Confidence and Provenance

Required distinctions:

```text
user_supplied
user_preserved
directly_observed
metadata_confirmed
strong_inference
weak_inference
auto_selected
auto_open
provider_translated
unknown
not_applicable
```

Result: PASS

Confidence vocabulary:

```text
certain
high
medium
low
unknown
not_applicable
```

Key invariant verified:

> Confidence describes evidentiary certainty, not authority over the user.

A low-confidence inference cannot override a hard lock.

AUTO creative selection is not mislabeled as uncertainty.

## Gate F - Conflict Resolution

Required canonical cases:

### 14mm + no wide-angle perspective distortion

Result: PASS

- can be C1 when the actual intent is cleaner geometry;
- solve through distance, placement, rectilinear behavior and framing first;
- becomes C2 only if the user literally demands wide FOV plus telephoto-like spatial compression under fixed geometry.

### f/1.2 + deep focus across a large scene

Result: PASS

- preserve f/1.2;
- first use distance, blocking, focal/format fields if unlocked, and perceived environmental readability;
- if all relevant factors are hard locked into physical incompatibility, classify C2 rather than silently changing aperture.

### 65/70mm + VHS artifacts

Result: PASS

- normally C0 because capture character and presentation/degradation layer are separate stages;
- does not falsely claim an actual photochemical original and VHS transfer are the same process.

## Gate G - Provider Independence

Result: PASS

The schemas model photographic intent before provider translation.

Provider adaptation is downstream and may not:

- fabricate unsupported controls;
- erase locks;
- redefine physical truth;
- turn provider marketing vocabulary into the universal ontology.

## Gate H - Standalone Integrity

Result: PASS AT CONTRACT LEVEL

All Phase 2 files live inside:

```text
cinematic-realism-director/
```

No Phase 2 semantic contract requires:

- a sibling skill;
- repository-root knowledge;
- AI-Verse OS;
- MCP;
- external provider access;
- an API key for reasoning/prompt-only operation.

Full isolated-folder executable validation remains a later V1 release gate once `SKILL.md` and all runtime references exist.

## Gate I - No Phase 0 Regression

Result: PASS

Phase 2 does not alter:

- first-party skill identity;
- still-image scope;
- standalone invariant;
- H1-H6 host degradation behavior;
- user-lock authority;
- truthful success/partial/blocked/failed semantics.

## Known Deferred Work

Phase 2 intentionally does not yet implement:

- story-to-shot decision rules, Phase 3;
- full camera/lens knowledge runtime references, Phase 3;
- lighting/color runtime engine, Phase 4;
- physical-realism taxonomy and Reality Gate implementation, Phase 5;
- user workflows, Phase 6;
- provider adapters, Phase 7;
- final `SKILL.md`, Phase 8;
- empirical provider calibration, Phase 9.

Those are not Phase 2 failures.

# Phase 2 Verdict

```text
Task 2.1  PASS
Task 2.2  PASS
Task 2.3  PASS
Task 2.4  PASS
Task 2.5  PASS

Phase 2 Gate  PASSED
```

The structured system can now represent:

```text
BEGINNER AUTO
EXPERT LOCKED SHOT
REALITY REPAIR
REFERENCE MATCH
```

while preserving the distinctions between:

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

Phase 3 may begin.
