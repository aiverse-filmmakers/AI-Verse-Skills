# Grain, Halation, Bloom, Flare, and Texture Restraint

Status: RUNTIME KNOWLEDGE
Task: 4.7

This reference governs texture/effect behavior so cinematic realism is not reduced to a bundle of fashionable artifacts.

Use with:

- `references/film-and-sensor-response.md`
- `references/lens-character.md`
- `references/color-science-and-grading.md`
- `references/exposure-and-dynamic-range.md`

## 1. Governing Principle

Grain, halation, bloom, flare, diffusion, sharpening, noise, and compression artifacts are separate phenomena.

Do not collapse them into one `film look` switch.

Reason in this order:

```text
capture intent
-> optical system
-> exposure / bright-source behavior
-> medium response
-> texture requirement
-> effect restraint
```

Every effect needs a cause and a purpose.

## 2. Grain

Grain should be treated as structured image texture, not uniform digital noise.

Consider:

- capture medium;
- format size;
- stock/sensitivity role;
- exposure level;
- enlargement/scan impression;
- luminance region;
- final output size;
- story intent.

### AUTO behavior

Default to little or no visible grain unless:

- film/analog medium is selected;
- a specific stock reference supports it;
- the story benefits from tactile texture;
- a reference image visibly contains it;
- provider benchmarking shows subtle grain improves realism.

### Avoid

- equal noise everywhere;
- giant coarse grain on clean large-format digital capture;
- grain pasted over specular highlights and shadows with identical strength;
- grain as proof that an image is cinematic.

## 3. Sensor Noise

Digital noise and film grain are not interchangeable.

Digital low-light response may include:

- chroma noise;
- luminance noise;
- pattern/fixed noise;
- denoising artifacts;
- detail loss in deep shadows.

Only introduce these when the chosen capture/story intent benefits from imperfect low-light digital response.

Do not contaminate premium clean digital-cinema AUTO shots with obvious noise merely for authenticity.

## 4. Halation

Halation is not a universal red outline around highlights.

Use only when:

- the film/medium reference plausibly supports it;
- bright sources/edges are intense enough to motivate it;
- the provider can express it without turning every highlight into a glow effect;
- the user/reference explicitly asks for visible halation.

Keep it localized and exposure-dependent.

Avoid:

- red/orange halos on every white edge;
- halation on matte midtones;
- treating halation as lens flare;
- adding it to all film-stock references.

## 5. Bloom

Bloom is soft light spread around sufficiently bright areas.

It may come from:

- optical diffusion;
- sensor/film response approximation;
- mist/filter behavior;
- bright-source scatter;
- provider-specific post effects.

Bloom should increase with genuinely bright values and source context.

Avoid globally softening the whole image under the label `bloom`.

## 6. Lens Flare

Flare requires light-source geometry relative to the lens.

Possible forms:

- veiling glare;
- ghosts;
- streaks;
- reduced local contrast;
- anamorphic streak behavior;
- colored internal reflections.

AUTO flare should generally be absent unless a strong source is in-frame or near the optical axis and the selected lens character supports visible flare.

Hard rule:

```text
cinematic != flare
anamorphic != mandatory blue streak
vintage lens != flare everywhere
```

## 7. Veiling Glare

Veiling glare can lower local/global contrast near a strong source.

Use it as a spatial optical response, not a gray haze overlay over the entire frame.

It should agree with:

- source position;
- lens/coating character;
- exposure;
- atmosphere;
- framing.

## 8. Optical Diffusion

If the user requests diffusion, distinguish it from defocus and bloom.

Possible visible consequences:

- gentler high-frequency facial detail;
- highlight spread;
- softened microcontrast;
- less brittle edges;
- preserved underlying focus plane.

Do not turn diffusion into smeared focus.

## 9. Sharpness

Avoid both extremes:

- brittle digital oversharpening;
- indiscriminate cinematic softness.

Sharpness should follow:

- focus plane;
- lens character;
- motion state;
- depth strategy;
- material texture;
- capture medium;
- output use.

Faces may retain pores without every pore having an edge-enhancement halo.

## 10. Microcontrast

Microcontrast affects perceived texture and dimensionality.

Too much can produce:

- crunchy skin;
- exaggerated pores;
- fake fabric detail;
- excessive local HDR;
- over-separated texture.

Too little can produce waxy surfaces.

Keep microcontrast material-specific and lighting-dependent.

## 11. Compression and Low-Fi Media Artifacts

VHS, consumer digital, Pixelvision-type references, phone compression, or archival media may justify:

- chroma bleed;
- reduced resolution;
- edge ringing;
- scanline/interlace cues;
- block/compression artifacts;
- color instability;
- tape noise/dropout where appropriate.

These are medium-specific, not generic vintage decoration.

Do not add all artifacts simultaneously unless the reference supports them.

## 12. Film Dirt, Dust, Scratches, Gate Weave

These are projection/scan/physical-medium artifacts, not mandatory film-stock characteristics.

AUTO should omit them unless:

- archival/damaged print is the intent;
- user explicitly requests them;
- reference match requires them.

Clean film capture can be filmic without visible scratches or dust.

## 13. Texture Hierarchy

The image should not have equal texture strength everywhere.

Prioritize material-appropriate variation:

- skin texture responds to light and focus;
- fabric weave depends on distance/focus;
- brushed metal has directional texture;
- glass is mostly seen through reflections, refraction, dust/smudges where appropriate;
- walls/stone may retain fine irregularity;
- background texture should soften with depth/motion as appropriate.

Global texture overlays are a common AI-look amplifier.

## 14. Bright Commercial Work

Do not assume clean commercial = sterile plastic.

A clean commercial result may have:

- little/no visible grain;
- no halation;
- no flare;
- precise material microtexture;
- clean highlights;
- controlled sharpening;
- subtle natural imperfections.

Realism comes from physical consistency, not dirtiness.

## 15. Naturalistic Drama

May use:

- subtle grain;
- restrained lens softness;
- occasional motivated flare;
- slight highlight bloom;
- natural material/skin variation.

But none is mandatory.

## 16. Vintage / Period Intent

First decide which period/medium is intended.

Then choose only relevant traits.

Do not combine:

```text
1970s 35mm grain
+ VHS chroma bleed
+ modern anamorphic flare
+ heavy digital sharpening
+ Polaroid color shift
```

unless the user explicitly wants hybrid media.

## 17. Reference Match

Observe texture effects separately:

```text
grain
noise
sharpness
diffusion
bloom
halation
flare
compression
physical media damage
```

Do not infer one from another.

A soft reference may be caused by lens falloff, focus, motion, diffusion, low resolution, compression, or enlargement. Mark uncertainty instead of inventing the cause.

## 18. Provider Behavior

Some providers expose explicit sliders/toggles for grain, halation, flare, sharpen, skin detail, or film looks.

Adapters may use those controls, but the universal brain must decide first whether each effect is actually needed.

Provider availability does not imply creative necessity.

## 19. Texture Reality Gate

Check:

1. Is the texture/effect motivated by medium, optics, exposure, or user intent?
2. Is grain spatially and tonally plausible rather than uniform noise?
3. Is halation localized to sufficiently bright boundaries?
4. Is bloom tied to bright values?
5. Does flare geometry correspond to a plausible source?
6. Does sharpness follow focus/depth/motion?
7. Is microcontrast appropriate to the material?
8. Are media artifacts internally consistent with one medium?
9. Has an AUTO effect been added simply because `cinematic` was requested?
10. Would removing the effect improve realism? If yes, remove it.

## 20. Hard Rules

```text
film != grain + warmth
halation != universal red glow
bloom != global blur
flare != mandatory cinema token
anamorphic != blue-streak preset
diffusion != missed focus
sharpness != edge halos
realism != dirtiness
vintage != stack every old-media artifact
provider effect control != reason to use it
```
