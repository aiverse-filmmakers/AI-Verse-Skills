# Example - REFERENCE MATCH

This example demonstrates observable visual-DNA transfer without hardware hallucination. It is not a hidden mandatory template.

## User

```text
Use this reference only for the visual look. Keep my subject and location, but match the reference's camera feeling, lighting, color, texture and depth.
```

## Routing

```text
workflow = REFERENCE MATCH
reference role = visual-language reference
subject/location = target locks
```

## Correct Observation Layer

From the supplied reference, the skill may observe traits such as:

- eye-level medium framing with slight off-axis composition;
- moderate wide-normal field of view;
- natural perspective with no fisheye curvature;
- moderate depth with readable environment and smooth focus falloff;
- soft directional key from camera-left, likely a large nearby source or window-like source;
- gentle negative fill on the opposite side;
- controlled highlights, dense but open shadows;
- restrained saturation with warm skin and slightly cooler environment;
- fine, subtle texture rather than coarse grain;
- low flare and restrained bloom.

These are observable traits.

Do **not** convert them into unsupported factual claims such as:

```text
Shot on ARRI ALEXA 35 + Cooke S4 32mm at T2.8 on Kodak 5219
```

unless metadata or documented evidence actually supports those values.

## Transferable DNA

```text
TRANSFER
- camera relationship / framing feel
- perspective behavior
- depth behavior
- lighting direction and softness
- contrast hierarchy
- warm/cool relationship
- saturation/density
- restrained texture / optical behavior

DO NOT TRANSFER
- reference identity
- reference wardrobe
- reference location
- reference props
- exact hardware claims
```

## Example Target Prompt

```text
Keep the target subject, wardrobe, and location unchanged. Match only the reference's observable photographic language: eye-level medium framing with a slight off-axis observational feel, moderate wide-normal rectilinear perspective, and moderate depth that keeps the environment readable with smooth natural focus falloff.

Use a soft directional key from camera-left with gentle negative fill opposite, preserving the same dimensional but natural contrast hierarchy. Keep highlights controlled and shadows dense but open. Reproduce the reference's restrained saturation, warm skin-to-cooler-environment separation, and subtle fine capture texture without adding heavy grain, flare, haze, or bloom.

Do not copy the reference subject, location, wardrobe, or props. Do not claim or force an exact camera, lens, aperture, stock, or LUT unless independently known.
```

## Multiple References

If more references are supplied, assign roles explicitly, for example:

```text
Reference 1 = identity only
Reference 2 = lighting/color only
Reference 3 = lens/depth/composition language
Target image = scene continuity / edit base
```

Target locks outrank reference tendencies.

## Why This Passes

- observable visual traits are separated from hidden metadata;
- content-specific features are not accidentally copied;
- multiple references can remain role-separated;
- the target subject/location stay authoritative;
- the final provider adapter receives the same visual DNA rather than inventing new creative decisions.
