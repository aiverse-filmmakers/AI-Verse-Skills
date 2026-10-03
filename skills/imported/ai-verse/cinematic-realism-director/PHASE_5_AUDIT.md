# Phase 5 Audit - Physical Realism and Anti-AI Intelligence

Status: PASSED

Phase: 5
Scope: Tasks 5.1-5.8

## 1. Gate Requirement

Phase 5 gate from `IMPLEMENTATION_PLAN.md`:

> The skill can explain exactly why an image feels AI-generated and produce a preservation-aware repair plan.

The audit also verifies that the system does not equate realism with dirt, grain, asymmetry, harshness, or vintage artifacts.

## 2. Evidence Under Test

Phase 5 runtime references:

- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`

Supporting contracts:

- `schemas/realism-diagnosis.schema.json`
- `schemas/cinematic-shot-spec.schema.json`
- `references/locks.md`
- `references/parameter-conflicts.md`
- `references/success-contract.md`

Supporting camera/light/color knowledge:

- all Phase 3 references;
- all Phase 4 references.

## 3. Audit Invariants

The Phase 5 system must preserve:

```text
realism target != documentary-only aesthetic
realism != more texture
realism != dirt / damage
realism != grain
realism != vintage defects
beauty / commercial polish != automatically fake
clean product imagery != automatically fake
stylization != failure when internally coherent
repair != uncontrolled regeneration
```

It must also preserve every Phase 0-2 authority rule:

```text
user lock > AUTO
preservation > repair drift
observation != unsupported hardware fact
provider limitation must be disclosed
visual success requires visual verification when claimed
```

## 4. Case A - Waxy AI Portrait

### Input condition

Portrait has:

- smooth waxy skin;
- identical pore pattern across face;
- overbright glassy eyes;
- individually perfect hair strands;
- plausible pose/composition that must remain unchanged.

### Expected diagnosis

Primary domains:

```text
skin
eyes
hair
```

Secondary domain only if evidence supports it:

```text
lighting / specular response
```

### Expected repair

Preserve:

- identity;
- pose;
- expression;
- framing;
- wardrobe;
- lighting direction if physically valid.

Repair:

- region-specific skin texture and tonal variation;
- source-consistent skin speculars;
- natural eye reflectance/catchlights;
- hair mass before strand detail;
- scale-dependent flyaways only where plausible.

Must **not**:

- add heavy pores everywhere;
- roughen skin indiscriminately;
- alter face shape;
- add freckles/scars/age changes without basis;
- add grain as a substitute for skin repair.

Result: PASS

## 5. Case B - Fashion Image With Floating Fabric

### Input condition

Fashion image has attractive lighting and styling, but:

- sleeve hovers from arm;
- folds repeat decoratively;
- hem reacts to wind opposite the hair;
- garment texture is equally sharp at every distance.

### Expected diagnosis

```text
fabric
contact / gravity
environment interaction
sharpness / scale
```

### Expected repair

- preserve garment design/color/identity;
- reconnect cloth to body geometry;
- rebuild folds from tension/compression/gravity;
- harmonize wind direction while respecting fabric mass;
- reduce weave visibility with distance/focus.

Must not redesign the outfit.

Result: PASS

## 6. Case C - Glossy Product With Fake Highlights

### Input condition

A pristine luxury product is correctly modeled and should stay pristine, but has disconnected beauty highlights and impossible reflections.

### Expected diagnosis

```text
materials / roughness
reflections
lighting motivation
contact shadow if affected
```

### Expected repair

- preserve exact product geometry, branding, color and clean condition;
- identify plausible studio source/card geometry;
- make highlight/reflection shapes follow surface curvature;
- match reflection sharpness to roughness;
- preserve legitimate polished commercial cleanliness.

Must not:

- add fingerprints;
- add dust;
- scratch the product;
- darken it into a moody cinematic scene.

Result: PASS

## 7. Case D - Wet Automotive Night Frame

### Input condition

Car on wet road with neon/practical sources. Failures:

- road reflections point toward unrelated sources;
- car panel reflection does not follow curvature;
- tyre appears slightly above road;
- water sheen is uniform on all surfaces.

### Expected diagnosis

```text
reflections
materials / roughness
contact / gravity
moisture / environment interaction
lighting motivation
```

### Expected repair

- restore tyre-ground contact;
- align wet-road reflections with source positions and road plane;
- shape vehicle reflections along panel geometry;
- vary wetness based on orientation/material/exposure;
- keep deliberate neon color design where source-supported.

Result: PASS

## 8. Case E - Clean Bright Commercial Beauty Frame

### Input condition

Bright soft beauty image with:

- smooth but believable skin;
- clean hair styling;
- clean background;
- minimal grain;
- no flare;
- no haze;
- no visible damage/dirt.

### Expected behavior

The system must **not** diagnose cleanliness itself as an AI artifact.

Check instead:

- source-consistent skin response;
- nonuniform natural skin detail where visible;
- plausible catchlights;
- hair mass/strand hierarchy;
- contact and geometry;
- appropriate exposure/color.

If those pass, outcome should be:

```text
PASS
```

without inventing imperfection.

Result: PASS

## 9. Case F - Stylized Filmic Frame

### Input condition

User explicitly requests:

- pronounced grain;
- halation around hot practicals;
- vintage edge softness;
- strong color separation.

### Expected behavior

These are not automatically failures because they are user-authorized style choices.

Reality Gate checks only:

- grain scale/coherence;
- halation location near bright boundaries;
- edge softness vs focus logic;
- light/source coherence;
- preservation of subject/scene.

Result: PASS

## 10. Case G - Preservation Conflict During Repair

### Input condition

User asks:

> Keep the exact pose, face, framing and product; fix the fake hand contact and floating object.

### Expected behavior

The system must:

1. preserve explicit locked regions;
2. identify the minimum geometry/contact region that requires change;
3. change only what is necessary to establish plausible contact;
4. return partial/blocked if the requested repair is impossible without violating a hard preservation lock;
5. never silently modify face/pose/product geometry.

Result: PASS

## 11. Case H - Reference Match With Unknown Hardware

### Input condition

Reference looks photographic with subtle edge softness and veiling flare.

### Expected behavior

The system may record:

```text
observable optical traits
```

but must not claim:

```text
exact lens model
exact filter
exact film stock
exact aperture
```

without supplied evidence.

Result: PASS

## 12. Reality Gate Order Audit

Required dependency order:

```text
locks / preservation
-> geometry / perspective
-> focus / motion
-> light
-> exposure / color
-> shadows / reflections
-> anatomy / skin / hair / eyes
-> fabric / materials
-> contact / environment
-> atmosphere
-> optical effects
-> stylization restraint
-> provider integrity
```

Verified: PASS

This order prevents decorative finishing from hiding structural failures.

## 13. Repair Priority Audit

Priority model:

```text
P0 structural blockers
P1 physical coherence
P2 realism surfaces
P3 finish / cliche effects
```

Verified: PASS

Examples:

- broken hand geometry outranks grain;
- floating car outranks paint microtexture;
- impossible shadow/reflection system outranks flare;
- identity corruption outranks beautification refinement.

## 14. Scope and Architecture Audit

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

## 15. Phase 5 Gate Verdict

PASSED.

The system can now:

```text
observe / receive a realism problem
-> identify concrete evidence
-> classify failure domain and severity
-> establish preservation boundaries
-> prioritize structural before cosmetic repairs
-> produce the smallest viable repair plan
-> verify dependent light/material/contact systems
-> reject unnecessary cinematic/vintage decoration
-> record Reality Gate outcome truthfully
```

Phase 5 is complete.

## 16. Carry Forward to Phase 6

Phase 6 workflows must call this intelligence rather than duplicate it.

In particular:

- AUTO DIRECT should use the Reality Gate before final output;
- CINEMATIZE must not introduce anti-realism clichés while upgrading a prompt;
- REALITY REPAIR must follow diagnose -> preserve -> repair -> verify;
- REFERENCE MATCH must retain uncertainty boundaries;
- MANUAL CAMERA must preserve locks while still running physical-plausibility checks.
