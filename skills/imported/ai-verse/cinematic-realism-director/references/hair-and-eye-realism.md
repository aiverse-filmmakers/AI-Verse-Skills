# Hair and Eye Realism System

Status: RUNTIME KNOWLEDGE
Task: 5.3

This reference defines how the skill should generate, diagnose, and repair hair and eyes so they remain physically coherent, identity-preserving, and photographically believable rather than hyper-detailed synthetic ornaments.

Use with:

- `schemas/realism-diagnosis.schema.json`
- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/motivated-lighting.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`

# Part A - Hair

## 1. Governing Principle

Hair should read first as a coherent mass with volume, weight, grooming, gravity, and light response.

Individual strands are secondary detail.

Reason in this order:

```text
silhouette / mass
-> root direction
-> gravity / styling / wind
-> major clumps / waves / curls
-> light / specular behavior
-> flyaways and fine strands
```

Do not begin by rendering thousands of equally sharp isolated strands.

## 2. Hair Mass and Silhouette

The overall silhouette should agree with:

- haircut;
- length;
- density;
- styling;
- head shape;
- gravity;
- wind/motion;
- wardrobe/contact.

Common AI failure:

```text
fine strand detail is convincing locally, but the overall hair volume is impossible
```

Fix mass/shape before microstrands.

## 3. Root Logic

Hair direction should plausibly emerge from the scalp/hairline.

Avoid:

- strands beginning in mid-air;
- roots changing direction arbitrarily;
- hairline painted as a perfect uniform edge;
- clumps crossing the scalp without origin;
- duplicated root patterns.

## 4. Gravity and Weight

Hair behavior depends on:

- length;
- curl pattern;
- styling/product;
- moisture;
- wind/motion;
- contact with shoulders/clothing.

Long hair should not behave like weightless fiber unless strong wind/motion explains it.

Short/styled hair can resist gravity more strongly.

## 5. Clumping and Strand Hierarchy

Realistic rendering should contain multiple scales:

```text
overall mass
large locks / curls / sections
mid-scale clumps
fine strands
occasional flyaways
```

Avoid equal-frequency spaghetti strands everywhere.

## 6. Flyaways

Flyaways are optional realism cues, not a required `real hair` token.

Use them sparingly.

They should:

- originate from the hair mass;
- follow plausible length and direction;
- respond to wind/static/styling;
- not break the apparent haircut length;
- not form duplicated looping filaments.

When the user asks to clean messy hair, preserve the haircut, length, color, parting, pose, and broad wind direction while removing only implausible/excessive flyaways.

## 7. Curl / Wave Behavior

Avoid repeated identical curl shapes.

Curls/waves should vary in:

- radius;
- compression;
- direction;
- occlusion;
- highlight position;
- grouping.

Pattern repetition is a strong synthetic cue.

## 8. Hair Specular Response

Hair often shows directional/anisotropic highlight behavior along fibers.

Generative translation:

- highlights should follow major strand/clump direction;
- intensity depends on source direction and hair material/color;
- dark hair can still preserve shape through specular separation;
- blonde/light hair can transmit/scatter backlight strongly around edges.

Avoid plastic uniform gloss across the whole hair mass.

## 9. Hair Color

Hair color is not one flat swatch.

Variation may come from:

- strand orientation;
- source color;
- shadows;
- dye/highlights;
- translucency/backlight;
- natural root differences.

Do not invent streaks/highlights that change identity unless allowed.

## 10. Backlight and Edge Detail

Backlight can reveal fine edge strands.

But edge detail should depend on:

- source position;
- exposure;
- focus;
- hair color;
- atmospheric/background contrast.

Do not create a perfect luminous halo around the entire head without source geometry.

## 11. Hair and Focus

Hair detail should obey the focus plane.

Avoid:

- every strand sharp while eyes/face fall off;
- flyaways sharper than the focal subject when outside the plane;
- segmentation-like blur boundaries around hair.

Depth falloff should pass naturally through complex hair edges.

## 12. Hair and Motion

Hair movement should agree with:

- body motion;
- camera motion;
- wind;
- gravity;
- clothing/loose environmental elements.

If wind moves hair camera-left, lightweight fabric or foliage should not imply the opposite direction unless turbulence/local shielding explains it.

Motion blur should vary across strands/clumps according to movement.

## 13. Hair Contact

Hair should interact believably with:

- shoulders;
- neck;
- clothing;
- hats;
- glasses;
- hands;
- chairs/surfaces.

Avoid clipping through anatomy/wardrobe or hovering just above contact surfaces.

## 14. Facial Hair

Beards, moustaches, brows, and stubble should:

- emerge from plausible follicles/regions;
- vary in density/direction;
- follow face geometry;
- respond to light/focus;
- preserve grooming and identity.

Avoid beard texture pasted over lips/skin or razor-sharp individual hairs at inappropriate distance.

# Part B - Eyes

## 15. Governing Principle

Eyes should read as wet curved organs integrated into eyelids and facial lighting, not flat iris graphics or glass marbles.

Reason through:

```text
gaze / binocular alignment
-> eyelid geometry
-> sclera / iris / pupil
-> corneal reflection
-> catchlight source
-> moisture / lash detail
```

## 16. Gaze Coherence

Both eyes should share one plausible gaze target unless the subject has a deliberate/asymmetric eye condition represented by the reference.

Avoid:

- each eye aiming independently;
- pupils centered for camera despite a side gaze;
- iris position inconsistent with head/eye direction.

For reference-preserving edits, gaze direction is normally a hard preservation target.

## 17. Eyelid Geometry

The eyeball sits inside and is partially occluded by eyelids.

Check:

- upper/lower lid wrap;
- lid thickness;
- crease behavior;
- inner/outer canthus geometry;
- lash origin;
- contact with globe.

Common AI failure:

```text
iris is convincing but eyelids do not physically wrap the eye
```

## 18. Sclera

The sclera is not pure digital white.

Depending on light/exposure it may show:

- subtle warm/cool variation;
- faint veins at close distance;
- shadow from eyelids;
- environmental color;
- moisture highlights.

Avoid whitening the eye until it becomes brighter than the scene logic permits.

## 19. Iris

Iris structure should be detailed only as framing/focus allows.

Avoid:

- perfectly radial repeated spokes;
- identical iris texture in both eyes;
- oversaturated unnatural color;
- macro detail in a medium-wide portrait;
- iris sharper than every other feature under the same focus conditions.

Preserve reference eye color rather than beautifying it.

## 20. Pupil

Pupil size should broadly agree with:

- scene brightness;
- source intensity;
- artistic/reference constraints.

Do not independently optimize pupil size for attractiveness.

The skill does not need to infer precise physiological response from every image; it should simply avoid obviously contradictory behavior.

## 21. Corneal Reflection

Catchlights/reflections should follow source geometry.

Check:

- number of visible catchlights;
- relative position;
- source size/shape;
- eye orientation;
- differences between left/right eye due to geometry.

Avoid perfectly duplicated catchlights pasted into both eyes.

## 22. Eye Wetness

The eye surface is moist, so small specular cues can appear.

Keep them localized.

Avoid the generic AI `glassy eye` look caused by oversized bright reflections and excessive clarity.

## 23. Tear Line

At close distance, the lower tear line may carry a small moisture highlight.

It should not become a bright white outline around the entire eye.

## 24. Lashes

Eyelashes should:

- emerge from lid margins;
- follow eyelid curvature;
- vary in grouping/length;
- soften with depth/focus;
- respect makeup state.

Avoid individually perfect evenly spaced comb-like lashes.

## 25. Brows

Eyebrows are hair structures with mass, direction, density, and individual variation.

Do not render them as:

- flat painted arcs;
- perfectly mirrored hair maps;
- identical repeated strokes.

Preserve grooming/reference shape.

## 26. Makeup / Contact Lenses

If makeup or colored/contact lenses are present:

- preserve them when locked;
- distinguish eyeliner/mascara/eyeshadow from anatomy;
- do not `repair` deliberate cosmetic stylization away;
- avoid synthetic contact-lens edge artifacts unless actually present.

## 27. Eye Focus / Sharpness

For portraits, eyes are often the focus target, but they should still obey optics.

Avoid:

- hyper-sharp irises with globally soft face caused by local AI sharpening;
- both eyes perfectly sharp at a plane where strong oblique head angle/shallow depth would not allow it;
- sharpened catchlights that exceed the lens/detail character.

When one eye is intentionally closer under shallow depth, differential sharpness may be natural.

## 28. Expression Integration

Eyes must agree with:

- eyelid tension;
- brows;
- cheek movement;
- mouth/expression;
- head orientation.

Do not repair eyes independently in a way that changes expression or identity.

# Part C - Repair and Verification

## 29. Hair Repair Sequence

```text
1. preserve identity / haircut / length / color / parting
2. repair mass/silhouette
3. repair root/gravity/contact logic
4. repair major clumps/curls
5. align highlights with source
6. remove duplicated/impossible strands
7. add restrained fine/flyaway detail only if needed
8. verify focus and motion coherence
```

## 30. Eye Repair Sequence

```text
1. preserve identity / gaze / eye color / expression
2. repair globe/eyelid geometry
3. align gaze/binocular direction
4. repair sclera/iris/pupil proportions
5. align catchlights/reflections with sources
6. restore restrained moisture/lash/brow detail
7. verify focus and grade integration
```

## 31. Generation Guidance

Prefer structural instructions equivalent to:

```text
hair forms coherent natural masses and clumps with restrained fine strands, realistic gravity/contact and source-aligned highlights

eyes share a coherent gaze, sit naturally inside eyelids, retain subtle scleral tone, realistic iris detail for the camera distance, and catchlights matching the actual light sources
```

Avoid giant negative-prompt lists unless the active provider specifically benefits from them.

## 32. Reference Match

Observe hair:

- cut/length;
- parting;
- color;
- density;
- curl/wave pattern;
- grooming;
- broad strand direction;
- flyaway level;
- sheen.

Observe eyes:

- color;
- shape;
- gaze;
- lid geometry;
- makeup;
- catchlight pattern;
- apparent pupil size;
- retouching level.

Do not infer medical/health conditions from appearance.

## 33. Hair Reality Gate

Check:

1. Does the overall mass make sense before strand detail?
2. Do roots originate plausibly?
3. Do gravity, styling and wind agree?
4. Are curls/strands non-repetitive?
5. Are highlights directional and source-consistent?
6. Do flyaways originate from the hair and remain restrained?
7. Does hair interact physically with clothing/body?
8. Does focus/motion apply correctly to hair detail?
9. Has identity/haircut changed during repair?

## 34. Eye Reality Gate

Check:

1. Do both eyes share a plausible gaze?
2. Do eyelids wrap the globes naturally?
3. Is scleral brightness/color plausible for the scene?
4. Is iris detail appropriate to distance/focus?
5. Do pupils broadly agree with lighting/reference?
6. Do catchlights correspond to real/implied sources?
7. Are left/right reflections appropriately different when geometry requires it?
8. Are lashes/brows irregular and anatomically attached?
9. Do eye sharpness and depth match the shot?
10. Has the repair changed expression or identity?

## 35. Hard Rules

```text
real hair != thousands of perfect strands
flyaways != mandatory realism
hair highlight != plastic gloss
wind != random strand explosion
real eyes != glass marbles
sclera != pure white
catchlights != decorative dots
iris detail != always macro-sharp
both eyes != independently optimized
hair/eye repair must preserve identity and expression
```
