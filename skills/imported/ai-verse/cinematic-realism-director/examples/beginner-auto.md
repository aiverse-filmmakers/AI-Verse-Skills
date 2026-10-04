# Example - Beginner AUTO DIRECT

This example demonstrates behavior. It is not a hidden mandatory template.

## User

```text
woman waiting for a taxi in London at night
```

## Routing

```text
workflow = AUTO DIRECT
technical locks = none
preservation locks = none
provider lock = none
question required = no
professional specialty = feature-film cinematography
execution = native/local image model first when available
```

The user does **not** need to add `cinematic`, `Hollywood`, `ARRI`, `professional`, or `high quality`.

## Internal Shot Direction

AUTO may infer a professional shot such as:

- natural narrative moment rather than a posed fashion portrait;
- medium-wide environmental framing so London context remains readable;
- observational eye/chest-height camera relationship with slight off-axis asymmetry;
- rectilinear wide-normal perspective, not fisheye;
- enough depth to retain street architecture, taxi lights, and contextual layers;
- practical street/storefront/vehicle sources as the lighting motivation;
- premium digital-cinema tonal behavior with smooth highlight rolloff and rich readable shadows;
- ARRI-like highlight-to-mid transition and natural skin separation as observable tonal targets, without claiming literal ARRI capture;
- controlled mixed-source color with believable warm practicals and cooler ambient night spill;
- wet pavement reflections only where physically motivated;
- realistic skin, coat fabric, contact shadows, glass/metal/wet-surface response;
- subtle organic filmic texture as part of the normal professional finish;
- no automatic teal-orange grade, decorative rim light, haze, anamorphic streak, maximum blur, or strong halation.

## Example Final Generic Prompt

```text
A woman waits for a taxi on a London street at night, captured as a natural narrative moment rather than a posed portrait. Feature-film-quality visual hierarchy: she is the emotional priority while the London street, curb, storefronts and moving traffic remain readable context. Medium-wide environmental framing from an observational eye-to-chest-height position, slightly off-axis, with a rectilinear wide-normal perspective and believable camera distance.

Lighting is motivated by real street lamps, storefront practicals and passing vehicle lights. Shape the face naturally from the available sources, with restrained ambient fill and believable source falloff. Premium digital-cinema tonal response: smooth highlight rolloff, gentle highlight-to-mid transition, rich readable shadows, no fake HDR flattening. Natural skin tone separation within mixed warm practical and cooler ambient night color.

Preserve realistic optical depth and focus falloff without excessive bokeh. Wet pavement and glass/metal reflections must remain viewpoint-consistent. Natural skin texture, physically believable coat fabric and moisture response, grounded feet/contact shadows, coherent environmental atmosphere. Apply a high-end restrained grade and subtle fine organic filmic texture to avoid sterile AI cleanliness while keeping the image contemporary and photographic.

No automatic teal-orange look, anamorphic blue streaks, decorative rim light, cinematic fog, Dutch angle, heavy bloom, strong halation or arbitrary motion blur.
```

## Execution

If the host has both a native/local image generator and optional external MCP/provider tools:

```text
native/local image model first
```

Do not automatically route to Magnific Cinematic or Higgsfield Soul Cinema.

Those providers are used only if the user explicitly requests them or a controlled benchmark names them.

## Why This Passes

- zero technical intake questions;
- professional quality was automatic;
- feature-film standard was inferred from the general narrative photographic request;
- premium tonal/color/texture finish was added without cliché stacking;
- subtle organic texture was treated as finishing, not as a heavy film effect;
- provider selection remained native-first;
- story/context drove camera, light, exposure and color.
