# Optical Imperfection Without Fake Vintage Spam

Status: RUNTIME KNOWLEDGE
Task: 5.7

This reference defines when optical imperfection improves photographic plausibility and when it merely adds generic retro decoration.

Use with:

- `references/lens-character.md`
- `references/aperture-focus-and-depth.md`
- `references/texture-effects-restraint.md`
- `references/film-and-sensor-response.md`
- `references/anti-ai-artifact-taxonomy.md`

## 1. Governing Principle

Imperfection is not a realism toggle.

The correct target is:

```text
context-appropriate optical behavior
```

not:

```text
add grain + bloom + halation + flare + softness + chromatic aberration
```

A modern clean commercial frame can be realistic with very little visible optical imperfection. A vintage or low-fi reference may require substantially more.

## 2. Separate the Imperfection Systems

Treat these independently:

```text
focus falloff
edge softness
field curvature impression
spherical-aberration softness
chromatic aberration
geometric distortion
anamorphic behavior
veiling glare
flare / ghosting
bloom
halation
grain / sensor noise
motion blur
compression / analog artifacts
```

Do not bundle them into one `vintage` control.

## 3. Source Hierarchy

Optical imperfection may be justified by:

1. explicit user lock;
2. reference DNA observation;
3. named lens/capture evidence;
4. capture medium/era intent;
5. scene-specific physical condition;
6. AUTO choice only when it materially supports the visual goal.

If none applies, restraint is the default.

## 4. Focus Falloff

Believable focus transition should:

- follow the focus plane;
- change continuously with depth;
- respect aperture/distance/format strategy;
- differ from motion blur;
- not cut subjects out like a segmentation mask.

A character lens may soften transition or edges without making the entire image unfocused.

## 5. Edge Softness

Edge softness can be plausible for:

- older optics;
- wide-open character lenses;
- certain image-circle/format combinations;
- intentionally imperfect low-fi systems.

It should not automatically affect the center equally.

Avoid uniform Gaussian softness over the whole frame.

## 6. Chromatic Aberration

Use only when:

- a lens/reference supports it;
- high-contrast edges make it plausible;
- the amount is restrained and spatially coherent.

Avoid RGB splitting on every object edge.

Modern corrected lens references may call for almost none.

## 7. Distortion

Distinguish:

- perspective exaggeration from camera position;
- rectilinear geometric distortion;
- barrel/pincushion lens distortion;
- fisheye projection;
- anamorphic geometric behavior.

Never add global fisheye distortion merely because the focal length is wide.

## 8. Flare and Ghosting

Flare requires source geometry.

Plausible triggers:

- bright source in frame;
- bright source just outside frame;
- lens orientation allowing internal reflection.

Flare should vary with lens family and source position.

Avoid decorative flare placed over dark areas with no source.

## 9. Veiling Glare

Veiling glare can locally reduce contrast around strong light interaction.

It may be appropriate for:

- vintage/older coatings;
- bright backlight;
- atmosphere + lens interaction;
- strong practicals near frame edge.

Do not lower global contrast indiscriminately and call it vintage.

## 10. Bloom

Bloom is a soft spread around bright values.

Use when bright sources/highlights justify it and the capture/reference supports it.

Bloom should not:

- erase all highlight geometry;
- affect dark objects equally;
- turn skin into glowing plastic.

## 11. Halation

Halation is distinct from bloom and flare.

In generative workflows it is often an approximation of film-layer behavior near intense highlights.

Rules:

- use only for film-like/reference intent where justified;
- strongest near genuinely bright high-contrast boundaries;
- keep subtle unless reference explicitly shows strong halation;
- do not put orange/red outlines around every edge.

## 12. Grain and Noise

Grain/noise should respect:

- capture medium;
- format;
- exposure;
- scale;
- luminance region;
- output resolution.

Avoid identical noise amplitude across sky, skin, shadows, and bright highlights.

Do not use noise to hide geometry/material failures.

## 13. Anamorphic Behavior

Anamorphic may involve:

- squeeze-related framing;
- bokeh geometry;
- astigmatic/focus behavior;
- edge behavior;
- flare/ghost character;
- breathing/distortion differences.

Do not force all cues simultaneously.

Hard rule:

```text
anamorphic != blue streak + giant oval bokeh + warped edges
```

## 14. Vintage Lens Strategy

A convincing vintage treatment usually uses a **small coherent subset** of traits.

Example:

```text
slightly reduced global contrast
subtle edge falloff
gentler focus transition
modest veiling flare around strong backlight
```

not:

```text
heavy softness + extreme grain + red halation + blue anamorphic flare + chromatic split + vignette + scratches
```

unless the reference actually demands that extreme combination.

## 15. Modern Lens Strategy

Modern optics can still look photographic.

Prefer:

- high resolving detail without digital oversharpening;
- controlled flare;
- clean geometry;
- smooth focus transition;
- material/light texture providing organic variation.

Do not add vintage defects simply to avoid a digital look.

## 16. Low-Fi Capture

VHS, 8mm, toy/consumer cameras, Pixelvision-like systems, or degraded media may justify stronger artifact stacks.

Still decompose them:

```text
resolution/detail response
noise/grain
chroma behavior
highlight response
edge artifacts
compression / tape artifacts
optical softness
```

Do not assume one universal low-fi preset.

## 17. Reality Repair

If an image looks too perfect/CG-like, first diagnose whether the cause is actually optical.

Possible non-optical causes:

- plastic materials;
- impossible light;
- uniform texture;
- bad contact;
- synthetic depth;
- over-clean environment;
- geometry errors.

Adding lens defects to those failures often makes the image worse.

Repair order:

```text
1. fix geometry / light / material / contact problems
2. preserve intended camera/lens character
3. add only the minimum optical imperfection needed
4. verify that imperfection follows source geometry and capture intent
```

## 18. Reference Match

From a reference, describe observable optical traits:

- soft/hard focus transition;
- edge falloff;
- flare type;
- bloom amount;
- halation visibility;
- chromatic behavior;
- distortion pattern;
- grain/noise character.

Do not claim exact lens model/filter/film process unless metadata or source evidence supports it.

## 19. Optical Imperfection Reality Gate

Ask:

1. Is each imperfection justified by a source/reference/capture choice?
2. Are focus and softness spatially coherent?
3. Is chromatic aberration restrained and edge-dependent?
4. Is distortion correctly distinguished from perspective?
5. Does flare correspond to a bright source?
6. Is bloom limited to bright values?
7. Is halation distinct from bloom and physically located near highlights?
8. Does grain/noise respect medium, scale and exposure?
9. Are anamorphic cues lens-specific rather than caricatured?
10. Would the image become more realistic by removing an effect rather than adding one?

Hard rules:

```text
imperfection != realism
vintage != every defect at once
modern != sterile
flare requires source geometry
halation != bloom != flare
distortion != perspective
```

Acceptance: PASSED
