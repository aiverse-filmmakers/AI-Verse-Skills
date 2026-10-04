# Reality Gate

Status: RUNTIME KNOWLEDGE

Purpose: verify both physical plausibility **and** the Professional Quality Floor before a still-image result is considered complete.

Use with:

- `references/professional-quality-floor.md`
- `references/execution-priority.md`
- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- physical-realism references in this package.

## Core Question

The gate asks:

> Could an elite professional plausibly create this requested image in the stated medium and conditions, with coherent geometry, optics, lighting, exposure, color, materials and finishing?

A result can be physically possible yet still fail if it is merely generic, under-directed, sterile, or below the professional standard safely inferable from the request.

The gate is not a demand for one house style. Mobile, candid, documentary, product, architecture, fashion, food, travel and cinematic work each have different professional standards.

## Outcomes

```text
PASS
PASS_WITH_NOTES
REPAIR_REQUIRED
BLOCKED_BY_CONSTRAINT
```

### PASS
No material professional-quality, realism, lock, preservation or execution-integrity issue remains at the verification level available.

### PASS_WITH_NOTES
Minor uncertainty/stylized departure exists but does not materially harm the requested result.

### REPAIR_REQUIRED
One or more material failures should be corrected before claiming visual success.

### BLOCKED_BY_CONSTRAINT
A hard lock, missing target, provider limitation, contradictory requirement or unavailable capability prevents valid repair/verification.

## Verification Levels

```text
V0 reasoning only
V1 execution confirmed
V2 actual image inspected
V3 inspected + corrected / comparative acceptance
```

Never imply V2 when no returned image was actually inspected.

## Evaluation Order

Evaluate in dependency order:

```text
1. literal user intent / requested medium / locks / preservation
2. Professional Quality Floor / professional specialty
3. scene geometry / perspective
4. composition / camera position / timing
5. focus / depth / motion
6. lighting motivation / direction / falloff
7. exposure / tonal response / highlight rolloff / shadows
8. color / white balance / grade
9. shadows / reflections / refractions
10. anatomy / skin / hair / eyes
11. fabric / materials / roughness
12. contact / gravity / environment
13. atmosphere / particles
14. optical effects / base texture / visible grain
15. stylization / anti-cliche restraint
16. execution-priority / provider-translation integrity
```

Do not solve structural problems with grain, blur, flare, texture or color grading.

## Gate A - Intent, Medium, Locks and Preservation

Check:

- Is the literal subject/action/environment still correct?
- Is the requested or clearly implied photographic medium preserved?
- Are explicit camera/lens/shot/light/style/cleanliness/provider locks intact?
- Are identity, pose, product geometry, wardrobe, composition, text or scene elements preserved where required?
- Did AUTO fill only genuinely unspecified fields?

Fail if an iPhone/selfie became generic cinema-camera imagery, a candid became staged fashion, architecture lost geometry discipline, or a hard lock was silently changed.

## Gate B - Professional Quality Floor

Check:

- Was the correct professional specialty inferred?
- Would the image look intentionally made by a top practitioner of that specialty rather than merely generated literally?
- Is composition/timing/viewer relationship professionally judged?
- Are lighting, exposure, tonal response, color and finishing at a professional standard appropriate to the medium?
- Does the image avoid sterile AI cleanliness where subtle organic texture would improve it?
- Did the user have to supply words such as `professional`, `cinematic`, `Hollywood`, `ARRI`, `high quality`, `good lighting` or `good composition` to obtain that standard? If yes, the default failed.

For narrative/cinematic/general photographic work without a stronger specialty signal, check for a feature-film-level finish: premium digital-cinema tonal behavior, smooth controlled highlights, rich readable shadows, professional color separation, realistic optical falloff, natural skin/material response and restrained organic texture.

`ARRI-like` tonal behavior may be used as an observable target, not as a literal sensor claim.

A physically coherent but generic/flat/under-finished image is `REPAIR_REQUIRED` under this gate.

## Gate C - Geometry and Perspective

Check:

- Does camera position explain near/far scale?
- Are field of view and format coherent with framing?
- Are straight lines/vanishing relationships plausible for the projection?
- Is rectilinear wide-angle proximity being mistaken for fisheye?
- Are body/object/architecture proportions coherent with viewpoint?

Perspective is not focal length alone.

## Gate D - Composition, Camera Relationship and Timing

Check:

- Is visual hierarchy intentional?
- Does camera height/distance/angle match viewer relationship?
- Is important environmental context preserved when it carries story or product/location identity?
- For candid/documentary work, does the frame feel believably observed rather than staged?
- For mobile/selfie, is framing/proximity plausible for the device/gesture?
- For product/architecture/automotive/food, are specialist composition priorities respected?

## Gate E - Focus, Depth and Motion

Check:

- coherent focus plane;
- continuous depth transition;
- depth strategy supports information hierarchy;
- motion blur distinguished from defocus;
- blur direction/amount matches camera/subject motion;
- no segmentation-like bokeh or pasted blur.

Do not require shallow depth merely because the image is cinematic.

## Gate F - Lighting Motivation

Check:

- dominant/secondary sources are identifiable;
- source direction, size, softness, color and falloff make sense;
- faces/products/materials receive light that could plausibly exist;
- practicals behave locally;
- rim/edge light is motivated if present;
- atmosphere reveals beams only when light + scattering justify them.

Attractive highlights without a plausible source fail.

## Gate G - Exposure and Tonal Response

Check:

- clear exposure hierarchy;
- important highlights protected where appropriate;
- natural clipping allowed where plausible;
- shadows intentionally dense/open rather than accidentally crushed/lifted;
- subject/environment exposure relationship is plausible;
- no fake HDR/local-tone halos;
- professional highlight rolloff appropriate to the medium.

For premium cinematic work, harsh digital clipping or flat equalized visibility is normally a defect unless explicitly desired.

## Gate H - Color and Grade

Check:

- white balance agrees with sources;
- skin/product colors remain plausible;
- saturated highlights retain believable hue/texture;
- shadow color agrees with ambient illumination;
- grade preserves source logic;
- color separation is professional rather than muddy or oversaturated;
- stylization is deliberate, not a generic preset.

Teal/orange is never a default requirement.

## Gate I - Shadows, Reflections and Refractions

Check:

- cast-shadow direction/softness agrees with sources;
- contact shadows match real contact;
- reflections agree with viewpoint, curvature, roughness and environment;
- eye catchlights correspond to sources;
- mirrors/glass/wet surfaces are geometrically coherent.

## Gate J - Anatomy, Skin, Hair and Eyes

Anatomy first, surface detail second.

### Anatomy

- hands/fingers/joints plausible;
- limbs/facial features connect coherently;
- accessories do not intersect anatomy impossibly.

### Skin

- region-specific texture and subtle tonal variation;
- source-consistent specular response;
- age/context/makeup preserved;
- no wax/plastic smoothing;
- no universal pore overlay.

### Hair

- mass/silhouette/root direction/gravity first;
- strand/flyaway detail scale-appropriate;
- no floating/fused strands.

### Eyes

- coherent gaze/alignment;
- plausible iris/pupil/sclera;
- source-consistent catchlights;
- no decorative glass-marble look.

## Gate K - Fabric and Materials

Check:

- folds have tension/compression/gravity causes;
- fabric weight/stiffness matches deformation;
- weave/detail respects distance/focus;
- metal/glass/wood/stone/leather/plastic/rubber respond according to material category;
- roughness shapes highlights/reflections;
- product surfaces may remain pristine when intended.

More microtexture is not automatically more realistic.

## Gate L - Contact, Gravity and Environment

Check:

- bodies/objects/vehicles sit on support planes;
- grip/contact is real;
- soft surfaces compress under load;
- clothing responds to posture/contact/wind;
- footprints/tracks/moisture/sand/snow/dust follow cause and gravity;
- nothing floats without intent.

## Gate M - Atmosphere and Particles

Check:

- haze/fog varies with depth;
- beams require source + scattering;
- rain/snow/dust follow scale, gravity, wind and depth;
- atmosphere does not flatten all scene structure.

Atmosphere is optional, not a cinema token.

## Gate N - Optical Effects and Texture

Evaluate separately:

- focus falloff;
- lens edge behavior;
- distortion;
- flare / veiling glare;
- bloom;
- halation;
- subtle base texture;
- visible stock-specific grain / digital noise;
- compression/analog artifacts.

### Subtle base texture

For most photographic/cinematic output, confirm a fine organic non-uniform texture is present or represented in the prompt/spec unless:

- the user explicitly requests no grain/pristine/noise-free/clinical output;
- the professional specialty materially benefits from near-perfect cleanliness;
- visible texture would damage required product/beauty/technical detail.

### Visible grain/effects

Strong/coarse grain, halation, bloom, flare, scratches, haze and other overt effects still need a medium/story/optical reason.

Do not confuse the normal subtle professional base texture with heavy `film-look` effect stacking.

## Gate O - Stylization / Anti-Cliche Restraint

Test against automatic clichés:

```text
maximum shallow DOF
teal/orange preset
haze/fog
rim light
anamorphic blue streak
strong/coarse grain
heavy halation
heavy bloom
crushed blacks
forced desaturation
wet pavement everywhere
perfect symmetry
beauty-filter retouching
```

Any may be valid when justified. None defines professional cinematic quality by itself.

Anti-cliche restraint must not remove professional composition, premium tonal response, color separation, natural material response, restrained grade or subtle organic texture.

## Gate P - Execution Priority and Provider Integrity

Check:

- Was execution path selected before provider adapter?
- If no provider was explicitly locked, was an adequate native/local image capability used first?
- Was an external MCP/plugin/connector chosen only because native lacked a material required capability?
- Were Magnific/Higgsfield kept inactive for ordinary requests?
- Were they used only for explicit target/export or controlled benchmark cases?
- Did adapter translation preserve the Professional Quality Floor and all locks?
- Were unsupported controls translated semantically rather than fabricated?
- Did provider presets introduce unwanted effects or redesign the shot?

Using an external provider because it appears more cinematic or specialized is a gate failure.

## Severity / Repair Priority

### P0 - contract/structural blockers

- missing/incorrect subject;
- identity/product corruption;
- hard-lock/provider-lock violation;
- requested medium erased;
- impossible anatomy/geometry/perspective;
- ordinary request wrongly routed to external competitor.

### P1 - professional/physical coherence failures

- Professional Quality Floor materially absent;
- impossible/unmotivated lighting;
- contradictory shadows/reflections;
- floating/contact failures;
- severe material/depth/motion inconsistency;
- harsh/flat tonal response incompatible with requested premium cinematic work.

### P2 - realism/finish failures

- plastic skin/hair/eyes;
- fabric/material roughness/fold errors;
- over-HDR/oversharpening/fake bokeh;
- weak color separation;
- sterile AI-clean texture where subtle organic finishing is appropriate.

### P3 - over-effect/cliche failures

- excessive grain;
- unnecessary bloom/halation/flare/haze;
- generic preset grade;
- decorative imperfections.

Repair higher-impact failures first.

## Minimal-Change Repair

```text
preserve what works
-> identify highest-impact failed gate
-> change smallest region/system that can solve it
-> re-check dependencies
-> repeat only as necessary
```

If native/local execution created the first result, prefer focused native/local correction where practical before external fallback.

## Structured Gate Record

When useful internally:

```text
reality_gate:
  status: PASS | PASS_WITH_NOTES | REPAIR_REQUIRED | BLOCKED_BY_CONSTRAINT
  verification_level: V0 | V1 | V2 | V3
  professional_quality_floor: pass | fail | unknown
  medium_fidelity: pass | fail | unknown
  physical_coherence: pass | fail | unknown
  execution_priority: pass | fail | not_applicable
  preserved_locks_verified: true | false | unknown
  provider_translation_verified: true | false | unknown
  unresolved_issues: []
```

Do not expose the full internal checklist to normal users unless requested.

## Final Pass Criteria

A still-image result passes when, at the strongest verification level available:

- literal request/medium and explicit locks are intact;
- Professional Quality Floor is met for the correct specialty;
- no material geometry/light/exposure/material/contact contradiction remains;
- skin/material/detail treatment matches requested realism;
- professional finishing is present without unjustified cliché stacking;
- subtle texture vs clean-output choice is appropriate;
- execution-priority policy was obeyed;
- provider translation did not silently weaken or redesign the image;
- no visual-quality claim exceeds actual inspection evidence.
