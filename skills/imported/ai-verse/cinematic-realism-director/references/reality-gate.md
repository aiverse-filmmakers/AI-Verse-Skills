# Reality Gate

Status: RUNTIME KNOWLEDGE
Task: 5.8

This is the reusable physical-plausibility and anti-AI verification policy for the Cinematic Realism Director.

It is used:

- before final prompt/spec delivery when reasoning-only;
- after image generation when the host allows visual inspection;
- before and after Reality Repair;
- during Reference Match transfer;
- during provider adaptation whenever controls may distort the original intent.

Use with:

- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `references/anti-ai-artifact-taxonomy.md`
- all Phase 3 camera references;
- all Phase 4 lighting/exposure/color references;
- all Phase 5 physical-realism references.

## 1. Purpose

The Reality Gate asks one core question:

> Could a real camera plausibly record this scene under the stated visual conditions, while still respecting the user's chosen stylization level?

It is not a demand for documentary realism.

Stylized, surreal, commercial, fashion, fantasy, and heightened images may pass when their internal physics and chosen visual language are coherent.

## 2. Gate Outcomes

Use four outcomes:

```text
PASS
PASS_WITH_NOTES
REPAIR_REQUIRED
BLOCKED_BY_CONSTRAINT
```

### PASS
No material realism issue remains for the requested target.

### PASS_WITH_NOTES
Minor uncertainty or stylized departure exists but does not materially harm the result.

### REPAIR_REQUIRED
One or more material failures should be corrected before claiming visual success.

### BLOCKED_BY_CONSTRAINT
A hard lock, unavailable image, provider limitation, or contradictory requirement prevents a valid repair/verification path.

These map into the broader success vocabulary from `references/success-contract.md`.

## 3. Verification Levels

Reuse the existing verification levels:

```text
V0 reasoning only
V1 execution confirmed
V2 visual inspection completed
V3 comparative / iterative acceptance
```

The gate must never imply V2 visual verification when no image was actually inspected.

## 4. Evaluation Order

Always evaluate in this order because later visual systems depend on earlier geometry:

```text
1. intent / preservation / locks
2. scene geometry and perspective
3. composition / camera position
4. focus / depth / motion
5. lighting motivation and direction
6. exposure / tone / color
7. shadows / reflections / refractions
8. anatomy / skin / hair / eyes
9. fabric / materials / roughness
10. contact / gravity / environmental interaction
11. atmosphere / particles
12. optical effects / texture
13. stylization restraint
14. provider-translation integrity
```

Do not try to solve a structural geometry failure by adding texture, grain, blur, or flare.

## 5. Gate A - Intent and Preservation

Check:

- Does the result still satisfy the user's actual request?
- Are explicit camera/lens/shot/lighting locks preserved?
- Are identity, pose, product geometry, wardrobe, composition, text, or scene elements preserved where required?
- Did AUTO fill only unspecified values?
- Did provider translation silently substitute a different creative decision?

Fail if:

- a hard lock was silently changed;
- Reality Repair drifted the scene unnecessarily;
- a provider limitation was hidden.

## 6. Gate B - Perspective and Geometry

Check:

- Does camera position plausibly explain near/far scale?
- Is focal-length behavior consistent with framing and format?
- Are straight lines/vanishing relationships plausible for the projection?
- Is wide-angle proximity being mistaken for fisheye?
- Are body/object proportions coherent with viewpoint?
- Does architecture retain consistent geometry?

Common failure:

```text
close wide-angle subject proportions + telephoto-looking background relationship
```

without a coherent camera position.

## 7. Gate C - Focus, Depth, and Motion

Check:

- Is there a coherent focus plane?
- Does depth transition continuously with distance?
- Is shallow/deep focus justified by story and geometry?
- Is motion blur distinguished from defocus?
- Do blur direction and amount match subject/camera motion?
- Are reflections/shadows compatible with motion state?

Fail if blur looks like segmentation, pasted bokeh, or random smear.

## 8. Gate D - Lighting Motivation

Check:

- What are the dominant and secondary sources?
- Do their direction, apparent size, softness, color, and falloff make sense?
- Does the face/product receive light that could plausibly exist in the scene?
- Is any rim/edge light actually motivated?
- Are practicals behaving locally rather than lighting the whole room magically?
- Does atmosphere reveal beams only when scattering supports it?

Fail if attractive highlights cannot be traced to a source.

## 9. Gate E - Exposure and Tone

Check:

- Is there a clear exposure hierarchy?
- Are important highlights preserved where needed?
- Are some highlights allowed to clip naturally?
- Are blacks intentionally dense rather than accidentally crushed?
- Is the frame avoiding fake HDR/local-tone-mapping halos?
- Are subject and environment exposures mutually plausible?

Hard rule:

```text
realistic dynamic range != every region perfectly visible
```

## 10. Gate F - Color

Check:

- Is white balance coherent with dominant/mixed sources?
- Do skin/product colors remain plausible under those sources?
- Are bright saturated colors retaining hue/texture rather than clipping into digital patches?
- Are shadow colors consistent with ambient illumination?
- Does the grade preserve the original light logic?
- Is teal/orange or other split-toning actually intentional?

Fail if the grade paints over the physics of the light.

## 11. Gate G - Shadows, Reflections, and Refractions

Check:

- Do cast shadows point consistently from plausible sources?
- Does softness match apparent source size and geometry?
- Are contact shadows tied to real contact?
- Do reflections agree with camera viewpoint, curvature, roughness, and environment?
- Do eye catchlights correspond to sources?
- Are mirrors/glass geometrically coherent?
- Do wet surfaces reflect the correct lights and plane?

## 12. Gate H - Anatomy, Skin, Hair, and Eyes

Check anatomy first, then surface realism.

### Anatomy
- hands/fingers/joints plausible;
- limbs connect correctly;
- facial/ear/teeth geometry coherent;
- accessories do not intersect anatomy.

### Skin
- texture varies by region and age/context;
- pores are not uniform overlays;
- speculars follow the light;
- color has subtle local variation;
- makeup remains distinct from skin material;
- no plastic/wax sheen unless intentionally cosmetic.

### Hair
- mass and silhouette are primary;
- strand detail is secondary and scale-dependent;
- gravity/wind are coherent;
- no floating spaghetti strands or fused intersections.

### Eyes
- shared gaze direction;
- plausible sclera/iris/pupil balance;
- catchlights tied to sources;
- corneal reflection curvature plausible;
- eyes are not sharper/brighter than the capture logic supports.

## 13. Gate I - Fabric and Materials

Check:

- folds have causes;
- cloth weight/stiffness matches deformation;
- weave/detail respects scale and focus;
- metal reflects environment rather than reading as gray plastic;
- glass combines reflection/transmission/refraction plausibly;
- wood/stone grain follows object geometry;
- roughness affects highlight/reflection structure;
- wear/dirt is contextually placed;
- pristine commercial products remain allowed to be pristine.

Hard rule:

```text
more microtexture is not automatically more realistic
```

## 14. Gate J - Contact, Gravity, and Environment

Check:

- feet/tyres/objects sit on their support plane;
- hands actually contact/grip objects;
- soft surfaces compress under load;
- clothing responds to posture/contact;
- tracks/footprints connect with motion;
- wind affects relevant elements coherently but material-dependently;
- moisture/dust/sand/snow follow environmental cause and gravity;
- object placement is stable.

Fail if subjects look composited into the scene.

## 15. Gate K - Atmosphere and Particles

Check:

- haze/fog density changes with depth;
- visible beams correspond to light + scattering;
- rain/snow/dust follow gravity/wind/motion;
- particle scale and contrast change with distance;
- atmosphere does not erase all depth structure.

## 16. Gate L - Optical Effects and Texture

Check each independently:

- focus falloff;
- edge behavior;
- chromatic aberration;
- geometric distortion;
- flare;
- veiling glare;
- bloom;
- halation;
- grain/noise;
- analog/compression artifacts.

Ask:

> Is this effect caused by the chosen capture/lens/reference, or was it added because it sounds cinematic?

Remove unsupported effects.

## 17. Gate M - Stylization Restraint

Explicitly test against recurring AI/cinematic clichés:

```text
mandatory shallow DOF
mandatory teal/orange
mandatory haze
mandatory rim light
mandatory anamorphic streak
mandatory heavy grain
mandatory halation
mandatory bloom
mandatory crushed blacks
mandatory desaturation
mandatory wet pavement
mandatory perfect symmetry
mandatory beauty retouching
```

Any of these may be valid when justified. None is a default requirement.

## 18. Gate N - Provider Translation

Check:

- Did the adapter preserve the universal shot intent?
- Did unsupported controls get translated semantically instead of fabricated?
- Did a provider preset introduce unwanted artifacts/effects?
- Did the model's output drift identity/product/composition locks?
- Are provider-specific negative/avoidance mechanisms used only where supported?

## 19. Severity and Repair Priority

Prioritize failures by downstream impact:

### P0 - structural blockers
- identity/product corruption;
- major anatomy;
- impossible geometry;
- broken perspective;
- missing required subject/object;
- hard-lock violation.

### P1 - physical coherence failures
- impossible lighting;
- contradictory shadows/reflections;
- floating/contact;
- material category failure;
- severe depth/motion inconsistency.

### P2 - realism surface failures
- skin/hair/eye artificiality;
- fabric roughness/folds;
- over-HDR;
- oversharpening;
- fake bokeh.

### P3 - finish/cliche failures
- excessive grain;
- unnecessary bloom/halation/flare;
- overdone grade;
- decorative imperfections.

Repair P0 before P1, P1 before P2, P2 before P3 unless preservation constraints force a different order.

## 20. Minimal-Change Repair Policy

For Reality Repair:

```text
preserve what works
identify the highest-impact failure
change the smallest region/system that can solve it
re-check dependent systems
repeat only as necessary
```

Do not regenerate the whole image when a targeted repair can solve the problem.

## 21. Structured Gate Record

When an internal structured result is useful, record:

```text
reality_gate:
  status: PASS | PASS_WITH_NOTES | REPAIR_REQUIRED | BLOCKED_BY_CONSTRAINT
  verification_level: V0 | V1 | V2 | V3
  checks:
    - domain
    - result
    - severity
    - evidence
    - repair_needed
  preserved_locks_verified: true | false
  provider_translation_verified: true | false | unknown
  unresolved_issues: []
```

This structure may be serialized into `cinematic-shot-spec.schema.json` / `realism-diagnosis.schema.json` carriers without making the user read the full internal checklist.

## 22. Beginner Behavior

Do not expose a giant checklist to normal users.

Run the Reality Gate silently and return:

- the corrected result;
- a concise note only if a material limitation/conflict remains.

## 23. Expert / Explain Behavior

When the user asks why a shot looks fake or requests a technical breakdown, expose the relevant failed gates and evidence.

Do not dump unrelated gate sections.

## 24. Final Pass Criteria

A still-image result may be considered Reality-Gate-passed when:

- explicit locks/preservation are intact;
- no material P0/P1 physical contradiction remains;
- surface realism matches the requested stylization level;
- lighting, exposure, materials, contact, shadows and reflections belong to one coherent scene;
- optional cinematic effects are justified rather than automatic;
- provider translation has not silently changed the shot.

## 25. Hard Reality Gate Rules

```text
physical coherence before decorative finish
locks before AUTO
preservation before repair drift
geometry before texture
light/material/contact must agree
reflection/shadow logic shares one scene
imperfection is optional
stylization may bend realism but must remain internally coherent
no visual-success claim without actual visual inspection when V2 is required
```

Acceptance: PASSED
