# Reflection and Shadow Coherence

Status: RUNTIME KNOWLEDGE
Task: 5.6

This reference enforces scene-wide consistency between light sources, shadows, reflections, refractions, surface roughness, camera viewpoint, motion, and environment geometry.

Use with:

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/anti-ai-artifact-taxonomy.md`
- `schemas/realism-diagnosis.schema.json`

## 1. Governing Principle

Shadows and reflections are not independent decoration.

They are consequences of the same scene geometry and lighting system.

The skill should therefore reason as one system:

```text
source position
source size
subject/object geometry
surface orientation
surface roughness
camera position
occlusion
motion
environment
=> shadows + speculars + reflections + refractions
```

## 2. Shadow Direction

A dominant source should create a coherent family of shadow directions unless additional sources explain differences.

Check:

- cast-shadow direction;
- self-shadow orientation;
- nose/chin/body shadows;
- object shadows;
- background shadows;
- contact shadows.

Multiple sources may legitimately produce multiple shadow families, but their strength/color/softness should correspond to the sources.

## 3. Shadow Softness

Shadow edge softness should be consistent with the apparent source size and geometry.

Broad/close source:

- softer transitions;
- wider penumbra;
- more wrap.

Small/distant source:

- harder edges;
- stronger geometric definition.

Distance from occluder to receiver can also change apparent shadow softness.

Avoid a scene where facial shadows imply a huge soft source while the same source creates razor-sharp nearby cast shadows with no explanation.

## 4. Contact Shadows

Contact shadows should be:

- strongest/tightest at true contact;
- integrated with ambient fill;
- shaped by surrounding occlusion;
- not used to hide floating geometry.

Avoid uniform black halos under every object.

## 5. Shadow Density and Color

Shadows are not automatically black.

Their appearance depends on:

- ambient/sky fill;
- secondary sources;
- bounce;
- exposure;
- local material;
- white balance/grade.

Example:

- sunlit exterior shadows may carry blue-sky/environment fill;
- tungsten interior shadows may be lifted by cooler window ambient;
- negative fill may deepen a side without eliminating all chroma/detail.

## 6. Reflection Fundamentals

Reflections should follow:

```text
viewpoint
surface normal / curvature
roughness
environment brightness/color
source placement
occlusion
```

A polished surface reflects the environment; it does not invent arbitrary beauty highlights.

## 7. Roughness and Reflection Structure

Lower roughness generally produces:

- tighter/sharper reflection structure;
- more distinct source shapes.

Higher roughness generally produces:

- broader/softer specular response;
- less distinct reflections.

Do not treat `glossy` as simply `brighter`.

## 8. Curved Surfaces

Curved surfaces transform reflection geometry.

Important examples:

- eyes/cornea;
- car bodywork;
- chrome;
- bottles/glassware;
- spherical/cylindrical products.

Highlights/reflections should travel and distort according to curvature rather than appear pasted flat.

## 9. Eyes and Catchlights

Catchlights must correspond to plausible sources.

Check:

- relative position in both eyes;
- eye orientation;
- corneal curvature;
- number of visible sources;
- source shape where readable.

The two eyes need not show pixel-identical catchlights because their surface orientation differs.

## 10. Glass and Transparent Surfaces

Transparent objects may combine:

- reflection;
- refraction;
- transmitted background;
- internal edges/thickness;
- highlights;
- partial opacity/color.

Do not generate impossible background shifts or reflections that ignore geometry.

## 11. Mirrors

A mirror should reflect scene content consistent with the camera/viewpoint relationship.

Common failures:

- reflected person with different pose/clothing;
- missing objects that should appear;
- impossible camera visibility;
- reflection perspective inconsistent with mirror plane.

If exact mirror geometry cannot be reliably resolved, reduce complexity rather than invent contradictory reflection content.

## 12. Vehicles

Automotive realism depends heavily on reflection coherence.

Check:

- long reflection gradients following panel curvature;
- windows reflecting sky/environment according to angle;
- headlights/trim reflecting sources appropriately;
- wheel/ground shadows and reflections agreeing with contact;
- wet-road reflections aligned with lights and road plane.

Avoid disconnected studio streaks on an otherwise natural exterior unless off-camera sources intentionally motivate them.

## 13. Product Imagery

Controlled product lighting may intentionally create designed reflection cards/strips.

That remains physically plausible when:

- reflection shape follows product geometry;
- source placement is coherent;
- material roughness modifies edge definition;
- product silhouette remains accurate.

Clean studio reflections are not an anti-realism failure.

## 14. Wet Surfaces

Wetness changes reflection behavior.

Check:

- reflections strengthen/clarify in plausible wet areas;
- puddles follow surface plane/depressions;
- reflected light direction matches sources;
- rough wet asphalt may still blur reflections;
- reflections should not float above the ground.

## 15. Atmospheric Effects

Fog/haze affects both shadows and reflected contrast:

- distant shadows lose contrast;
- beams can become visible when scattering supports them;
- reflections may soften with distance/atmosphere;
- background contrast reduces progressively.

Do not add visible light beams in clean air without particulate explanation.

## 16. Motion Coherence

Motion can affect reflected and shadowed content.

If a moving subject is motion-blurred:

- its strong reflection may show compatible directional blur;
- its cast shadow may soften/smear depending on exposure and source;
- static environment reflections should not inherit subject blur arbitrarily.

## 17. Multi-Source Lighting

For scenes with multiple sources, map each major visible effect back to a source.

Example:

```text
warm practical -> local warm face/specular + nearby shadow family
cool window -> broad cool fill + window reflection
signage -> colored reflection on glossy surfaces facing sign
```

Avoid unrelated colored highlights that do not correspond to any source/environment.

## 18. Reflection/Shadow Repair Order

```text
1. preserve geometry / identity / product shape
2. identify dominant and secondary sources
3. correct cast-shadow direction
4. correct contact and self-shadow behavior
5. correct roughness/material response
6. correct major reflections/refractions
7. correct eye/glass/mirror special cases
8. align motion and atmospheric behavior
9. verify color/exposure coherence
```

## 19. Reference Match

From a reference, safely infer:

- broad source direction;
- shadow hardness/softness;
- reflection sharpness;
- source shapes visible in reflections;
- wet/dry impression;
- roughness tendencies.

Do not infer exact fixture dimensions, wattage, polarizer angle, reflection-card size, or full unseen environment without evidence.

## 20. Reflection and Shadow Reality Gate

Ask:

1. Do shadows point away from plausible sources?
2. Is shadow softness consistent with source size and geometry?
3. Are contact shadows tied to actual contact?
4. Do shadow density/color agree with ambient fill and exposure?
5. Do reflections correspond to camera angle, curvature and environment?
6. Does roughness change reflection sharpness appropriately?
7. Do eye catchlights correspond to real sources?
8. Do mirrors/glass preserve scene geometry?
9. Do wet surfaces reflect the correct sources and plane?
10. Do moving reflections/shadows agree with motion?
11. Are any highlights/reflections present only because they look attractive?

Hard rules:

```text
shadow and reflection logic share one scene geometry
contact shadow cannot rescue floating geometry
roughness changes reflection structure
catchlights require sources
mirror content must obey viewpoint
beauty highlights still need physical motivation
```

Acceptance: PASSED
