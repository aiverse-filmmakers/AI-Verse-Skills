# Skin Realism System

Status: RUNTIME KNOWLEDGE
Task: 5.2

This reference defines how the skill should generate, diagnose, and repair human skin so it reads as living photographed tissue rather than wax, plastic, over-retouched beauty texture, or a procedural pore overlay.

Use with:

- `schemas/realism-diagnosis.schema.json`
- `references/anti-ai-artifact-taxonomy.md`
- `references/motivated-lighting.md`
- `references/color-science-and-grading.md`
- `references/aperture-focus-and-depth.md`

## 1. Governing Principle

Skin realism comes from the interaction of:

```text
anatomical form
lighting direction and source size
subtle color variation
specular response
surface texture
subsurface appearance
focus / depth
age / context
makeup / grooming
camera distance / resolution
```

Do not solve unrealistic skin by simply adding more pores.

## 2. Region-Specific Skin

Different facial/body regions should not have identical texture.

Typical variation may include:

- forehead: different oil/specular behavior from cheeks;
- nose: stronger pores/sebum response in many people;
- under-eye: thinner, softer, more translucent appearance;
- cheeks: broader tonal transitions and local redness variation;
- lips: distinct material/texture from surrounding skin;
- ears: thin tissue with stronger transmitted warmth under backlight;
- beard area: follicle/shadow/stubble structure where present;
- hands: different crease, vein, knuckle, nail and dryness behavior;
- neck/body: different pore scale and texture from close facial skin.

AUTO should not exaggerate any region unless distance, lighting, age, or user intent supports it.

## 3. Pores

Pores are contextual microstructure.

They should:

- vary in visibility across regions;
- become more visible under raking/specular light;
- soften with distance, focus falloff, diffusion, makeup or lower resolution;
- remain subordinate to larger skin form.

Avoid:

- identical pore stamps across the face;
- pores equally sharp on foreground and out-of-focus skin;
- giant pore texture used as an anti-plastic filter;
- edge-enhanced pores that look embossed.

## 4. Fine Texture

Fine skin texture can include:

- small creases;
- follicle structure;
- faint dryness;
- tiny irregularities;
- subtle scars/marks when actually present or appropriate;
- fine lines appropriate to age;
- microtexture around eyes/lips.

Do not invent conspicuous blemishes when identity/reference preservation matters.

Natural realism is not equivalent to deliberately roughening someone’s face.

## 5. Color Variation

Real skin should not be one uniform hue.

Allow subtle region-to-region variation such as:

- cheeks/nose/ears slightly warmer or redder;
- under-eye hue shifts;
- cooler/less perfused areas;
- beard shadow;
- tanning/freckling where present;
- local environmental color contamination;
- source-colored highlights and shadows.

Preserve natural complexion and identity.

Hard rule:

```text
skin realism != orange skin
```

## 6. Specular Response

Skin is neither perfectly matte nor uniformly glossy.

Specular highlights should depend on:

- source direction;
- apparent source size;
- skin region/oiliness;
- makeup/skincare/wetness;
- viewing angle;
- exposure.

Common AI failure:

```text
identical glossy sheen across forehead, cheeks, nose and body
```

Repair by making specular response spatially plausible, not simply reducing all shine.

## 7. Subsurface / Translucency Cues

The skill should not simulate tissue physics literally, but it can preserve plausible visible cues:

- soft warm transmission in thin tissue under strong back/side light;
- warmth around ears/fingers where appropriate;
- smooth transition between highlight and underlying diffuse skin color;
- living tonal depth rather than flat painted color.

Avoid exaggerated red glow or fake translucent wax.

## 8. Peach Fuzz / Vellus Hair

Peach fuzz may appear under close, directional/back lighting.

Use only when:

- framing is close enough;
- light direction makes it visible;
- realism target supports high detail;
- it does not alter identity/grooming intent.

Do not cover the whole face in equally visible microhair.

## 9. Age-Appropriate Texture

Preserve age rather than beautifying everyone toward the same smooth face.

Consider:

- fine lines;
- deeper folds;
- skin laxity;
- pore visibility;
- pigmentation;
- under-eye structure;
- hand/neck age cues.

Avoid:

- removing age markers without user request;
- exaggerating age to prove realism;
- applying the same `real skin` texture to every age group.

## 10. Makeup vs Skin

Makeup changes surface response but does not erase anatomy.

Possible effects:

- foundation reduces some color variation;
- powder reduces specular sheen;
- highlighter deliberately increases localized specular response;
- blush/bronzer adds intentional color regions;
- lipstick/eye makeup are distinct materials/colors.

Do not confuse polished makeup with plastic AI skin.

When makeup is a preservation target, repair underlying realism without stripping the intended cosmetics.

## 11. Beauty / Commercial Skin

Beauty imagery can be clean and flattering while still realistic.

Preserve:

- smooth but non-flat tonal gradients;
- controlled microtexture;
- plausible speculars;
- natural anatomy;
- subtle local color variation;
- makeup intent.

Avoid the false choice between:

```text
plastic airbrush
vs
extreme forensic pores
```

A premium commercial face can be refined without becoming synthetic.

## 12. Documentary / Naturalistic Skin

Allow more environmental truth:

- uneven source color;
- sweat/oil when contextually present;
- stronger pores/lines at close distance;
- weather effects;
- minor redness;
- less retouching.

Do not add grime or blemishes merely because the image is documentary.

## 13. Sweat / Moisture

Moist skin changes specular behavior.

If sweat/rain/water is present:

- highlights become more localized/intense;
- droplets follow gravity/anatomy;
- wet hair/clothing/environment should agree;
- skin should not become uniformly lacquered.

## 14. Facial Anatomy Before Texture

A realistic skin shader cannot rescue impossible facial geometry.

Check first:

- eye spacing/alignment;
- eyelids;
- nose structure;
- lips/teeth;
- ears;
- jaw/cheeks;
- expression symmetry/asymmetry;
- neck connection.

If geometry is wrong, repair geometry before polishing pores.

## 15. Lighting Coherence

Skin texture must respond to light.

Under broad soft light:

- microtexture may appear gentle;
- highlight transitions are broad;
- pores are not aggressively embossed.

Under hard/raking light:

- relief and fine texture can become more visible;
- small shadows/specular peaks increase.

If texture ignores lighting direction, it looks pasted on.

## 16. Focus and Resolution Coherence

Do not render skin detail beyond the optical/resolution logic of the shot.

Examples:

- medium-wide face should not show macro-level pores;
- out-of-focus ear should not retain sharper pores than the eyes;
- motion-blurred face should not have frozen microtexture;
- diffusion should soften high-frequency detail while preserving form.

## 17. Color Grade Coherence

Skin should remain integrated with the chosen grade and source colors.

Do not protect skin so aggressively that it appears isolated from:

- colored practicals;
- sunset;
- neon spill;
- cool sky;
- candle/fire;
- underwater/colored environments.

Natural color does not mean globally neutral.

## 18. Identity Preservation

For edits/reference repair:

Preserve unless user allows change:

- face shape;
- age;
- ethnicity;
- freckles/moles/scars that define identity;
- makeup;
- facial hair;
- expression;
- skin tone/complexion.

Reality Repair should not `beautify` identity by default.

## 19. Plastic Skin Diagnosis

Before repair, identify the cause.

Possible causes:

- excessive smoothing;
- missing local color variation;
- uniform specular response;
- over-denoising;
- global blur;
- overly clean beauty lighting;
- synthetic pore overlay;
- excessive sharpening after smoothing;
- anatomy/shape simplification.

Repair the actual cause, not the label `plastic`.

## 20. Repair Strategy

Recommended minimal sequence:

```text
1. preserve identity / expression / makeup
2. correct lighting/specular inconsistency
3. restore broad tonal and color variation
4. restore region-specific microtexture
5. add fine detail only where focus/distance support it
6. verify age/context
7. verify grade integration
```

## 21. Generation Guidance

For photoreal generation, prioritize phrases/intent equivalent to:

```text
natural region-specific skin texture
subtle tonal and chromatic variation
specular response consistent with the key source
fine facial texture appropriate to distance and focus
unretouched anatomy unless beauty treatment requested
```

Do not rely on a giant list of `pores, wrinkles, peach fuzz, blemishes` in every portrait.

## 22. Reference Match

Observe:

- apparent texture strength;
- makeup;
- sheen;
- local hue variation;
- age detail;
- lighting interaction;
- retouching level.

Do not infer dermatological conditions or health information from an image.

## 23. Skin Reality Gate

Check:

1. Does facial anatomy look structurally coherent?
2. Is texture appropriate to camera distance/focus?
3. Does texture vary by region?
4. Are pores/fine lines subordinate to larger form?
5. Do speculars agree with source direction/size?
6. Is complexion naturally varied rather than one flat hue?
7. Does skin pick up environmental light plausibly?
8. Is age preserved?
9. Is makeup distinguished from skin?
10. Are face/neck/hands/body rendered as compatible skin materials?
11. Has the repair changed identity unnecessarily?
12. Has realism been confused with adding excessive defects?

## 24. Hard Rules

```text
real skin != pore overlay
real skin != blemish generator
beauty != plastic
realism != aging the subject
skin != uniform orange
specular != wet lacquer
peach fuzz != mandatory
retouching != erase anatomy
identity preservation outranks cosmetic AUTO changes
```
