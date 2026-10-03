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
question required = no
```

## Internal Shot Direction

The skill may infer a coherent shot such as:

- lonely-but-natural late-night street moment rather than a posed fashion portrait;
- medium-wide environmental framing so London context remains readable;
- camera near eye/chest height with a slight observational offset rather than perfect frontal symmetry;
- moderate wide-normal rectilinear perspective, not fisheye;
- enough depth to retain wet street, taxi lights, architecture, and atmospheric context;
- practical street/shop/taxi sources as the lighting motivation;
- mixed warm practicals and cooler ambient night light with believable local color contamination;
- controlled highlights on wet pavement without fake HDR recovery;
- natural skin and fabric response, coherent reflections, contact shadows, and rain/wet-surface behavior;
- grain, bloom, flare, haze, and shallow depth only if the resolved shot actually benefits from them.

## Example Final Generic Prompt

```text
A woman waits alone for a taxi on a London street at night, caught in a natural unposed moment. Medium-wide environmental framing from an observational eye-to-chest-height camera position, slightly off-axis, with a rectilinear wide-normal field of view that keeps the street architecture and approaching traffic readable without fisheye curvature. The woman is the visual priority but the city remains part of the story.

Lighting is motivated by real street and storefront practicals, vehicle headlights and cooler ambient night sky/city spill. Warm practical light shapes one side of her face and coat while cooler ambient fill remains in the shadows. Wet pavement carries viewpoint-consistent reflections from signs and headlights. Preserve a realistic exposure hierarchy: bright practicals may approach or exceed clipping while the face remains readable; do not flatten the whole scene into HDR.

Natural skin texture and source-consistent specular response, believable coat fabric weight and moisture, grounded feet/contact shadows, coherent rain and wet-surface behavior, subtle atmospheric depth. Clean cinematic color separation with restrained saturation and dense night blacks. No automatic teal-orange grade, decorative rim light, fisheye distortion, excessive bokeh, or mandatory grain/flare.
```

## Why This Passes

- the user was not asked to choose a camera;
- AUTO filled only missing decisions;
- story/context drove framing and light;
- physical realism was specified through causes and relationships rather than quality adjectives;
- no cinematic cliché was added by default.
