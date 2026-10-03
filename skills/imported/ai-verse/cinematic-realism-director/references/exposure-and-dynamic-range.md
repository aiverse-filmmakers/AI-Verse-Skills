# Exposure and Dynamic-Range Behavior

Status: RUNTIME KNOWLEDGE
Task: 4.4

This reference defines how the Cinematic Realism Director reasons about exposure, highlight protection, shadow density, clipping, and scene contrast without turning dynamic range into HDR-style equal visibility.

Evidence basis:

- `references/research/lighting.md`
- `references/research/color-and-tone.md`
- `references/cameras-and-capture-formats.md`

## 1. Core Principle

A believable image has an exposure hierarchy.

The goal is not:

```text
everything visible
everything recovered
no clipping anywhere
all shadows lifted
```

The goal is:

```text
important information is prioritized
bright sources are allowed to be bright
dark regions are allowed to be dark
transitions remain natural
materials retain plausible response
```

## 2. Exposure Design Order

AUTO resolves exposure in this order:

```text
story / commercial priority
-> subject priority
-> dominant source
-> brightest meaningful region
-> shadow-information requirement
-> highlight-clipping tolerance
-> black-density target
-> midtone placement
-> capture-character intent
-> grade / display intent
```

## 3. Subject Priority

Identify what must be exposed intentionally.

Examples:

### Portrait

Usually face/eyes/skin are priority, unless silhouette or environmental mood overrides.

### Product

Brand-critical surfaces, label, shape, and material response are priority.

### Architecture

Spatial relationships and material surfaces may matter more than a single local subject.

### Documentary

Preserve authentic compromise. Do not relight every face into studio perfection.

### Automotive

Body reflections and form may matter more than uniformly bright cabin/interior details.

## 4. Highlight Protection

Highlight protection does not mean suppressing all bright values.

Prefer:

- gradual transition toward clipping;
- retained hue around bright saturated sources;
- visible shape around windows/practicals when plausible;
- small hot cores allowed to clip;
- no abrupt digital white plateau unless intentional.

Examples of acceptable clipping:

- lamp filament;
- direct sun disc;
- specular sparkle;
- tiny chrome highlight;
- hottest neon core;
- blown exterior patch in a dark interior.

## 5. Shadow Density

Shadows may be:

```text
open
moderately dense
dense but differentiated
near-black selective
crushed intentionally
```

Do not equate `cinematic` with crushed blacks.

Do not equate `dynamic range` with lifted gray shadows.

Good dense shadows retain enough structure/chroma to feel photographic while preserving contrast.

## 6. Midtone Placement

Midtones carry much of the perceived image density.

AUTO should avoid:

- overbright skin that feels thin/digital;
- globally lifted mids that erase lighting shape;
- underexposed mids where subject intent disappears;
- excessive local contrast that fragments surfaces.

## 7. Scene Contrast vs Local Contrast

### Scene contrast

Difference created by source/environment exposure.

### Local contrast

Small-scale tonal separation inside surfaces/details.

These are separate.

A low-key scene may still have restrained local sharpening. A high-key image may still preserve subtle local texture.

Do not simulate `cinema` by adding aggressive clarity/microcontrast.

## 8. Dynamic Range Translation

Manufacturer stop numbers are not literal generative controls.

Translate broad-latitude intent into visible consequences:

```text
bright windows retain a gradual shoulder
practical lights preserve surrounding color before clipping
shadow regions retain shape without HDR lifting
highlight and shadow regions belong to one exposure
```

Never claim an AI image literally has a measured number of stops.

## 9. Camera Character and Exposure

Named camera locks can influence the exposure target through documented response tendencies, but never override story.

Examples:

### ALEXA-like intent

- controlled highlight rolloff;
- retained highlight color;
- natural skin separation;
- restrained digital clipping.

### Modern high-end digital

- broad usable tonal range;
- clean low-light capability where appropriate;
- no requirement to make blacks gray.

### Analog video / low-fi

- narrower-feeling highlight handling may be intentional;
- harder clipping/blooming can be part of the requested medium.

## 10. Film Negative vs Reversal Exposure Intent

### Negative-film reference

Generally supports more flexible highlight/shadow shaping in the generative interpretation.

### Reversal-film reference

May justify tighter exposure discipline, stronger density, and more direct color/contrast relationship.

Do not invent exact latitude numbers unless sourced and relevant.

## 11. Interior Window Exposure

Three common strategies:

### Interior priority

Face/room reads correctly; exterior may run bright or partially clip.

### Balanced interior/exterior

Requires plausible fill, ND, time-of-day, or production-lighting logic.

### Exterior priority

Interior may become silhouette/selective.

Do not force all three into simultaneous perfect visibility.

## 12. Night Exposure

Night should still contain a hierarchy.

Possible targets:

```text
practicals brightest
face one step below practicals
ambient environment lower
deep background selectively near-black
```

Avoid:

- every shadow lifted;
- sky and face at identical brightness;
- all neon signage perfectly retained while dark subject is independently beauty-lit.

## 13. Snow / Beach / Bright Environments

High-reflectance environments naturally create high ambient levels.

Expect:

- brighter shadow fill;
- strong specular risk;
- reduced subject/background contrast unless shaped;
- need for exposure priority.

Do not force deep black shadows where environment would fill them strongly without a reason.

## 14. Dark Environments

Low-key does not require zero information.

Preserve:

- edge relationships;
- subject silhouette;
- small local speculars;
- meaningful shadow color;
- texture where the light actually reaches.

## 15. Underexposure as Intent

Underexposure may be correct for:

- suspense;
- documentary night;
- silhouette;
- dense editorial work;
- protecting bright practicals;
- preserving atmosphere.

But underexposure must still preserve the requested subject information.

## 16. Overexposure as Intent

Overexposure may be correct for:

- dreamlike high key;
- backlit summer;
- flash photography;
- bright fashion/editorial;
- deliberate blown windows;
- analog/consumer-media references.

Do not automatically repair deliberate exposure choice.

## 17. HDR Failure Modes

Reject synthetic HDR behavior such as:

- equal visibility in every tonal zone;
- halos around edges;
- shadow microcontrast brighter than the light warrants;
- bright windows darkened unnaturally while room remains bright;
- metallic highlights flattened to gray texture;
- skin carrying separate local exposure from environment;
- skies with extreme texture while foreground remains independently perfect.

## 18. Clipping Failure Modes

Reject accidental-looking:

- featureless large white skin patches;
- abrupt color-to-white transition on neon;
- blown product label needed for legibility;
- hard digital clipping across broad clouds when not intentional;
- specular clipping inconsistent with nearby source brightness.

## 19. Exposure Locks

If user specifies:

```text
one stop under
protect highlights
crushed blacks
blown windows
high-key
low-key
silhouette
ETTR-like technical intent
```

preserve the requested direction as a lock.

If another lock conflicts, use `references/parameter-conflicts.md`.

## 20. Reference Match

From a reference, describe observable exposure relationships:

```text
face is approximately one visual step below window
highlights roll smoothly before small clipped cores
shadows remain dense but chromatic
background drops substantially below subject
```

Do not infer exact ISO, shutter, aperture, EI, or stop count from appearance alone.

## 21. Exposure Reality Gate

Check:

1. What is the exposure priority?
2. What is the brightest meaningful region?
3. Which highlights may clip?
4. Are highlight transitions gradual where intended?
5. Are shadows dense/open by design?
6. Is shadow visibility plausible for ambient fill?
7. Are midtones placed intentionally?
8. Does skin/product exposure agree with environment?
9. Is there local HDR or halo behavior?
10. Is any clipping destroying required information?
11. Does the chosen capture/film reference support the visual behavior without pretending literal measured DR?
12. Does the exposure still serve the story?

## 22. Runtime Output Language

Prefer visible behavior:

```text
protect highlight color around the windows while allowing the brightest exterior patches to clip; keep the subject's face in a natural midtone range; let the far room fall into dense but differentiated shadow without lifting the blacks
```

Avoid:

```text
17 stops dynamic range, HDR, perfect exposure everywhere
```

The first describes an image. The second is unsupported specification theater.