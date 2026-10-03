# Example - Expert Locks / MANUAL CAMERA

This example demonstrates lock behavior. It is not a hidden mandatory template.

## User

```text
Desert portrait at sunrise. ARRI ALEXA 35 character, Cooke S4 look, 35mm, f/4, low angle, three-quarter framing. Keep the background readable. No flare, no haze. Warm side light from the rising sun.
```

## Routing

```text
workflow = MANUAL CAMERA
```

## Locked Values

```text
camera_character = ARRI ALEXA 35
lens_character = Cooke S4
focal_length = 35mm
aperture = f/4
camera_angle = low
shot_size = three-quarter
background_readability = preserve
flare = none
haze = none
key_motivation = sunrise side light
```

AUTO may still choose compatible values such as:

- exact camera distance and height within the low-angle requirement;
- subject placement and lead room;
- fill strategy;
- exposure hierarchy;
- white-balance handling;
- shadow density;
- material/skin realism;
- final provider syntax.

## Correct Conflict Behavior

The request for `f/4` plus a readable background is compatible and should not be silently changed to `f/1.4` for a more fashionable shallow-depth look.

`35mm` does not itself define the perspective. The skill must choose camera distance/position consistent with the requested three-quarter framing and low angle.

`No flare` and `no haze` remain hard constraints even though sunrise photography often contains both.

## Example Final Direction

```text
Three-quarter desert portrait at sunrise from a low camera position, using a 35mm rectilinear field of view and camera distance chosen to preserve natural body proportions while giving the foreground and landscape a strong but believable sense of scale. Keep the background recognizably readable rather than dissolving it into shallow bokeh. Aperture behavior consistent with f/4.

ARRI ALEXA 35-inspired capture character: controlled highlight transition, natural skin separation and dense but open shadows. Cooke S4-inspired lens character expressed through gentle contrast, natural skin rendering and smooth focus transition without exaggerated vintage softness or anamorphic artifacts.

The rising sun is the motivated warm side key. Use restrained ambient sky fill from the opposite side so the face remains dimensional without losing the sunrise direction. Preserve texture in skin, fabric and sand, with contact shadows and footprints/ground interaction matching the low sun. No lens flare. No atmospheric haze. No teal-orange split grade.
```

## Why This Passes

- every explicit technical choice remained locked;
- AUTO changed only unspecified fields;
- named equipment was translated into observable behavior without claiming literal physical simulation;
- focal length did not replace camera-position reasoning;
- cinematic clichés did not override explicit constraints.
