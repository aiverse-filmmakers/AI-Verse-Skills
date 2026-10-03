# Phase 1 Research - Color, Tone, and Display-Independent Visual Principles

Status: RESEARCH EVIDENCE

Primary classification: `CONFIRMED` for first-party/standards behavior, `CORROBORATED` for established grading practice, `INFERRED` only where explicitly labeled.

This file captures color and tonal principles that should survive across providers and display pipelines. It is not a LUT library and does not prescribe one cinematic grade.

## Core Principle

Color decisions should be described first in terms of visible relationships, not provider-specific sliders.

The universal brain should reason about:

- white balance and source neutrality;
- relative hue separation;
- saturation discipline;
- skin versus environment separation;
- highlight color behavior;
- shadow color behavior;
- black density;
- midtone placement;
- highlight rolloff;
- gamut compression rather than clipping;
- exposure-dependent color stability;
- scene contrast and local contrast;
- output intent.

## Scene-Referred Versus Display-Referred Thinking

ACES and ARRI color-science documentation reinforce an important separation:

```text
CAPTURE / SCENE DATA
        ↓
COLOR MANAGEMENT / RENDERING
        ↓
DISPLAY OUTPUT
```

The skill should not equate a log capture encoding with a finished visual look.

Examples:

- `LogC4` is not itself a cinematic grade;
- a wide-gamut working space is not a final palette;
- a camera's color science and a creative grade are distinct stages;
- a film-stock reference may imply capture response, but the final display rendering still determines perceived contrast and saturation.

## Tone Mapping and Highlight Rolloff

ACES 2 documentation explicitly describes a rendering transform with a tone scale and chroma/gamut compression. Its design goals include a gentler highlight rolloff than ACES 1, hue preservation across exposure levels, and reduction of harsh clipping artifacts.

### Generative implication

When the target is natural cinematic realism:

- protect bright highlights from abrupt hard clipping unless the story calls for clipping;
- preserve some colorfulness in highlights instead of turning every bright source pure white immediately;
- transition from midtones into highlights smoothly;
- avoid excessive HDR-style local contrast that makes every tone equally emphasized;
- avoid crushed shadows unless intentionally motivated;
- allow blacks to feel dense without destroying all shadow information.

Do not treat `filmic` as simply `low contrast`. Filmic tone can still have strong contrast while using controlled shoulder/toe behavior.

## Hue Preservation and Gamut Discipline

ACES 2 separates lightness/colorfulness operations in a perceptual model partly to preserve hue and manage saturation more predictably through tone mapping and gamut limits.

### Generative implication

Avoid synthetic color behavior such as:

- saturated reds shifting unpredictably toward orange/magenta in highlights;
- neon colors clipping into flat digital patches;
- skin becoming oversaturated as exposure increases;
- cyan/blue shadows turning uniformly electric;
- every saturated object appearing equally intense.

Prefer:

- stable hue relationships;
- saturation that decreases or compresses plausibly near exposure extremes;
- strong colors retaining texture and tonal variation;
- controlled gamut rather than hard clipping.

## ARRI REVEAL Evidence

ARRI's REVEAL Color Science describes:

- more accurate and subtle color reproduction;
- naturalistic rendering of diverse skin tones;
- improved color tracking and differentiation across exposure levels;
- improved handling of bright saturated colors;
- AWG4 + LogC4 as a wide-gamut/log capture pipeline.

### Generative implication

An `ARRI natural` style reference should not be reduced to a LUT token. Observable goals include:

- natural skin hue and saturation;
- subtle separation between nearby colors;
- bright saturated objects remaining differentiated;
- restrained digital clipping;
- smooth highlight transitions;
- a grade that can remain clean without looking flat.

## Skin Tone Handling

Skin tone is not one fixed hue. The skill should preserve:

- ethnicity and natural variation;
- local redness and cooler areas;
- subsurface warmth;
- shadow chroma;
- specular highlights that reflect the light source rather than becoming painted skin color;
- makeup only when present/requested.

### Avoid

- forcing every complexion toward orange;
- uniform peach color across the entire face;
- whitening highlights by removing all skin chroma;
- skin isolated from environmental light color;
- using a vectorscope `skin-tone line` as a rule that all skin must literally sit on one hue.

## White Balance and Mixed Light

White balance changes the interpretation of the whole scene. It should be chosen in relation to the dominant source and creative intent.

Mixed-source environments may legitimately retain color differences, for example:

- warm tungsten practicals against cooler exterior daylight;
- greenish fluorescent spill against neutral skin correction;
- sodium-vapor streetlight against cool ambient sky;
- candlelight with warm highlights and cooler unlit surroundings.

The skill should not neutralize every source to white. Cinematic realism often depends on believable source-to-source color contrast.

## Color Contrast and Separation

Useful separation can come from:

- complementary hue relationships;
- warm/cool source contrast;
- saturation contrast;
- luminance contrast;
- production-design color blocking;
- subject/environment separation;
- selective neutrality around a saturated focal subject.

Color separation should serve visual hierarchy rather than becoming a mandatory orange/teal formula.

## Saturation Discipline

Saturation should be contextual.

High saturation can be correct for:

- pop commercial imagery;
- stylized fashion;
- certain reversal-film references;
- neon environments;
- saturated production design.

Low/moderate saturation can be correct for:

- documentary realism;
- overcast exteriors;
- restrained drama;
- aged/bleached references;
- dense low-key work.

Hard rule:

```text
cinematic != desaturated
cinematic != teal-orange
cinematic != warm highlights + cyan shadows by default
```

## Density

`Density` is useful as a perceptual description for images that feel rich, substantial, and not digitally thin.

It may involve a combination of:

- controlled midtone placement;
- stable saturation in midtones;
- deep but differentiated shadows;
- non-clipped highlights;
- production-design color mass;
- limited excessive lift in blacks;
- avoiding overly bright, thin skin exposure.

Density is not a single slider and should not be represented as `make everything darker`.

## Black Level and Shadow Color

Shadows may be:

- neutral;
- warm;
- cool;
- contaminated by ambient/environmental sources.

The skill should preserve believable color in shadows where the scene supports it rather than crushing them to chroma-free black.

Dense blacks are compatible with shadow detail. The visual target should determine how much low-end information remains visible.

## Highlight Color

Highlights inherit source color and material behavior.

Examples:

- warm practicals can create warm specular highlights;
- blue sky reflection can cool metal/glass highlights;
- skin specular highlights may be less saturated than underlying diffuse skin but should still follow the light source;
- bright emissive signage may retain hue before approaching display white.

Do not paint highlight color independently of lighting motivation.

## Filmic Versus Video-Like Tonality

For this skill, `video-like` should not be used as an insult or a precise technical classification. It is a shorthand for visible artifacts often associated with less-controlled rendering, such as:

- harsh highlight clipping;
- brittle edge sharpening;
- excessive local contrast;
- very clean/noiseless surfaces combined with unnatural texture;
- oversaturated bright colors;
- crushed shadows with no tonal transition;
- global contrast added without protecting skin/material detail.

A more cinematic/photographic result often uses:

- gradual highlight transitions;
- intentional midtone contrast;
- controlled black density;
- stable hue through exposure changes;
- restrained saturation;
- texture appropriate to capture medium;
- local contrast that follows materials and light.

These are visual goals, not claims that all video cameras behave one way and all film behaves another.

## Display Independence

The skill should describe the intended visual relationships rather than hardcode output-device assumptions.

Preferred language:

- `gentle highlight rolloff`
- `dense but open shadows`
- `restrained saturation in highlights`
- `natural skin separation from cool background`
- `soft warm practicals with neutral midtones`

Avoid runtime dependence on:

- a specific monitor calibration;
- one HDR nit level;
- one LUT file;
- one color-management implementation.

Provider adapters may translate the same visual intent differently.

## Color Reality Gate Checks

Later Reality Gate implementation should ask:

1. Are skin hues plausible under the stated sources?
2. Do highlights retain believable source/material color?
3. Are saturated colors clipping or flattening unnaturally?
4. Are shadows consistent with ambient light?
5. Is white balance coherent with the scene?
6. Does the grade preserve visual hierarchy?
7. Is saturation justified by story/product intent?
8. Are black levels intentionally dense or accidentally crushed?
9. Is highlight rolloff smooth enough for the intended capture character?
10. Does any stylized split-tone treatment overpower physical light logic?

## Sources

Primary/strong sources recorded in `source-ledger.md` include:

- ARRI REVEAL Color Science;
- ACES 2 official documentation on rendering transforms, tone mapping, chroma compression and gamut mapping;
- Blackmagic Design / DaVinci Resolve color documentation and official training;
- FilmLight colorist material as practitioner corroboration.

External URLs are provenance only, not runtime dependencies.

## Requirements Carried Forward

Phase 4 should convert this evidence into concise runtime rules for:

- white balance;
- palette;
- color separation;
- saturation;
- density;
- skin treatment;
- shadow/highlight color;
- highlight rolloff;
- black-level strategy;
- display-independent output language.

Provider adapters must not replace these visual goals with arbitrary provider presets.