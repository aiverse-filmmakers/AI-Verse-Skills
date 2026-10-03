# Phase 1 Research - Lighting, Exposure, and Atmospheric Behavior

Status: RESEARCH EVIDENCE

Primary classification: physical principles and well-established cinematography practice, with source-backed practitioner examples marked `CORROBORATED` where appropriate.

This file establishes the lighting concepts the later cinematic brain must understand. It is not a menu of fashionable lighting labels.

## Governing Principle

Cinematic lighting should answer four questions before it chooses a named pattern:

1. **Why does this light exist in the scene?**
2. **Where is it coming from?**
3. **How large/hard/soft is it relative to the subject?**
4. **What exposure and contrast relationship does it create?**

A believable image may use stylized light, but the light should still have spatial logic.

## Motivated Lighting

`Motivated` lighting means the image's light design is plausibly tied to visible or implied sources in the world, for example:

- window daylight;
- practical lamp;
- streetlight;
- neon sign;
- fire/candle;
- overhead fluorescent;
- vehicle headlight;
- bounced sky/sun;
- stage fixture.

The production may enhance or cheat those sources off-camera, but the resulting direction, color and shadow logic should remain coherent with the apparent motivation.

### Generative relevance

AI images often look artificial when they contain:

- a bright rim with no plausible back source;
- a face key coming from one direction while shadows indicate another;
- random multicolor highlights not supported by the environment;
- perfectly lit eyes/face despite scene exposure suggesting darkness;
- every surface separately optimized for visibility.

Later Reality Gate checks should explicitly test lighting motivation and directional consistency.

## Apparent Source Size and Softness

Source: `LIGHT-001`, corroborating standard photographic practice.

The apparent size of a light source relative to the subject strongly affects shadow transition:

- larger/closer apparent source -> softer shadow edges and broader wrap;
- smaller/farther apparent source -> harder, more defined shadow edges.

Distance also changes intensity and coverage, so `soft` is not merely a stylistic adjective.

### Generative translation

Instead of:

```text
soft cinematic lighting
```

prefer a physically meaningful design such as:

```text
large diffused window source close to camera-left, broad wrap across the face, gentle shadow transition, minimal frontal fill
```

## Inverse-Square Behavior

For a point-like source in free space, illuminance approximately falls with the square of distance.

Practical cinematography modifiers are not perfect point sources, and walls/bounce/ambient light alter the scene. Still, the principle explains why moving a light much closer can create stronger near/far falloff.

### Generative relevance

This helps distinguish:

- intimate close-source falloff, where the near side/background can darken quickly;
- distant/sun-like illumination with much more uniform intensity across a human-scale scene.

Do not prompt the formula itself. Prompt the visible consequence when useful.

## Negative Fill

Sources: `LIGHT-002` plus established lighting practice.

Negative fill does not add light. It reduces unwanted bounce/ambient fill, usually with dark material or environment control, increasing shape and contrast on the shadow side.

### Generative translation

Useful descriptions include:

- controlled shadow side;
- reduced environmental bounce;
- deeper cheek/body-side separation;
- retained shadow detail without flat frontal fill.

Avoid making `negative fill` synonymous with crushed black shadows.

## Bounce

Bounce turns another surface into a larger indirect source.

Observable consequences depend on:

- bounce surface size;
- distance;
- color/reflectance;
- original source direction;
- environment.

Generative prompts should identify the bounce's role, for example:

```text
warm pavement bounce lifting the underside of the face
```

rather than simply writing `cinematic bounce lighting`.

## Practicals

Practicals are visible or scene-integrated light sources such as lamps, bulbs, signs or fixtures.

They can provide:

- visible motivation;
- exposure anchors;
- local pools of color/contrast;
- depth separation;
- specular reflections.

### Reality caution

A practical does not automatically illuminate an entire room evenly. Its spill should respect distance, obstruction and source size.

## Window Light

Window light is valuable because it naturally implies:

- one primary side/direction;
- potentially large apparent source size;
- environment-dependent bounce and negative fill;
- depth gradient away from the window;
- possible exterior overexposure if interior exposure is prioritized.

For realism, the skill should allow bright windows to remain brighter than the room instead of forcing every exterior highlight to be fully recovered.

## Sunlight and Sky Fill

Direct sun is effectively a small hard source at human scale, producing relatively defined shadows under clear conditions.

The sky acts as a broad ambient source. Clouds can become a very large diffuser.

### Generative consequences

Hard-sun scenes should usually show:

- coherent shadow direction;
- strong geometric light/shadow structure;
- sky/environment fill in the shadows rather than zero information;
- specular responses consistent with surface orientation.

Overcast scenes should usually avoid fake directional hard shadows unless another source explains them.

## Backlight and Rim Light

Backlight is valid when a source exists behind or behind-side the subject.

A visible rim/edge highlight depends on:

- source position;
- subject contour/material;
- exposure;
- atmosphere;
- lens orientation.

### Anti-cliche rule

Do not add a perfect rim to every `cinematic` portrait.

A rim should be absent when the lighting geometry would not produce one.

## Chiaroscuro / Low-Key / High-Key

These are broad contrast/exposure strategies, not specific light fixtures.

### Low-key

- larger proportion of darker values;
- selective illumination;
- controlled fill;
- may still preserve information in shadows.

### High-key

- brighter overall value distribution;
- lower shadow contrast in many applications;
- does not necessarily mean overexposed white clipping.

### Chiaroscuro

- pronounced light/dark modeling with deliberate shape;
- should still have source logic.

Later runtime rules should not confuse these with specific portrait patterns such as Rembrandt or butterfly lighting.

## Portrait Lighting Patterns

Magnific exposes Rembrandt, butterfly, loop, split, broad and short as direct controls.

These are useful composition/light-position patterns but should not be applied blindly.

Later reference material should define them geometrically:

- relation of key to face/camera;
- resulting nose/cheek shadow behavior;
- broad vs short side orientation;
- suitability to pose and narrative.

The beginner AUTO system should choose them only when portrait structure calls for them.

## Key-to-Fill Relationship

The skill does not need to hallucinate exact numeric ratios for every shot.

What matters visually is the relationship:

- flat/even;
- gentle modeling;
- moderate contrast;
- strong contrast;
- near-silhouette/selective illumination.

Later schema may store a qualitative contrast strategy and optional numeric ratio only when the user explicitly provides one.

## Exposure Hierarchy

A believable image has an exposure hierarchy.

Questions later Reality Gate should ask:

- What is the visual subject?
- What is the brightest meaningful object/source?
- Which highlights may naturally clip?
- How dark can shadows become before important information disappears?
- Are the face/product/materials exposed consistently with the environment?

Artificial images often reveal themselves because everything is independently `perfectly exposed`.

## Specular vs Diffuse Response

Lighting realism depends on materials.

The same light should create different responses on:

- skin;
- matte fabric;
- glossy plastic;
- polished metal;
- glass;
- wet pavement;
- painted car body;
- rough concrete.

A later material system must therefore interact with lighting rather than being a separate decorative description.

## Reflections

Reflections should be consistent with:

- light/source position;
- environment geometry;
- surface normal/roughness;
- camera viewpoint.

Common AI failure:

- highlights/reflections placed for beauty but disconnected from any source/environment.

Reality Repair should correct the light-material system together.

## Atmosphere and Volumetric Light

Fog, haze, dust or moisture can reveal light paths through scattering.

Important restraint:

- no atmosphere -> beams generally should not appear visibly suspended in clean air;
- more atmosphere reduces contrast with distance;
- back/side light often makes particles/haze more visible;
- volumetric effects should respect light geometry.

Do not add `god rays` merely because the shot is cinematic.

## Candle / Firelight

Small flame sources are warm and local, often with rapid spatial falloff and variable intensity.

For plausible candle/fire scenes:

- illumination should be strongest close to the source;
- surrounding ambient/moon/window/bounce may still exist;
- skin highlights and eye reflections should agree with flame placement;
- do not illuminate an enormous room evenly from one candle unless intentionally stylized.

## Neon / Colored Practicals

Colored sources should create spatially plausible contamination:

- color strongest near source-facing surfaces;
- mixed-light zones can produce separation;
- shadows may carry different ambient hues;
- skin can reflect colored sources without becoming uniformly painted.

Avoid the generic AI trope of equal cyan on one side and magenta on the other unless the actual set contains those sources.

## White Balance and Mixed Sources

White balance changes the relative appearance of light sources.

Example principle:

- a tungsten practical may appear neutral/warm/cooler depending on capture white balance and grade;
- daylight and tungsten mixed together can create useful warm/cool separation;
- the skill should decide which source, if any, is treated as neutral.

White balance belongs to both capture and color design and should not be applied as a final Instagram-style temperature slider only.

## Lighting and Skin

Skin realism requires:

- directional modeling consistent with facial geometry;
- plausible specular intensity;
- retained subsurface/tonal variation;
- no uniform wax sheen;
- pores/microtexture should respond to light rather than look pasted over it;
- shadow-side skin should retain chroma/tonal nuance when exposure permits.

This will be expanded in Phase 5.

## Lighting and Product Imagery

Product shots often require more deliberate highlight shaping than narrative scenes.

AUTO should infer when the goal is:

- form-revealing softbox reflections;
- crisp controlled specular edges;
- gradient reflections on glass/metal;
- brand-legible product geometry;
- clean but not impossible contact shadows.

Cinematic realism does not mean making every commercial product shot dark and moody.

## Named Lighting Labels vs Structured Light

A user may lock `Rembrandt`, `golden hour`, `hard noon sun`, `natural window`, etc.

The internal system should decompose the label into:

```text
source motivation
source direction
apparent size / softness
color
intensity/exposure
fill strategy
ambient contribution
back/edge contribution
atmosphere
```

This makes the result provider-independent.

## Phase 1 Lighting Knowledge Strength

Strong:

- source-size/softness relationship;
- inverse-square qualitative behavior;
- negative fill/bounce concepts;
- motivated source logic;
- practical/window/sun/sky spatial reasoning;
- material-light interaction;
- exposure hierarchy;
- atmosphere/scattering principles.

Moderate:

- generic portrait-lighting pattern definitions, which need a dedicated Phase 4 reference and examples.

Weak / unresolved:

- one standardized cross-provider prompt vocabulary for exact lighting ratios;
- whether named lighting terms are interpreted consistently by every image generator;
- precise numeric photometry for arbitrary generated scenes, which is unnecessary for V1.

## Requirements Carried Forward

Phase 4 and Phase 5 should:

- model light motivation before lighting style;
- separate key, fill/negative fill, ambient, back/edge and practicals;
- model source direction, size/softness, color and exposure consequence;
- avoid automatic rim light, haze and neon split lighting;
- make reflections/material response consistent with the lighting design;
- use exposure hierarchy instead of flattening every tonal region;
- include light-direction/shadow/material checks in the Reality Gate.