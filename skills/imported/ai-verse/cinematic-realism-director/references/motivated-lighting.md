# Motivated Lighting Engine

Status: RUNTIME KNOWLEDGE
Task: 4.1

This reference defines how the Cinematic Realism Director designs lighting from believable scene causes rather than fashionable lighting labels.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`

Evidence basis:

- `references/research/lighting.md`
- `references/research/color-and-tone.md`

## 1. Core Rule

Lighting begins with:

```text
WHY does the light exist?
WHERE is it?
HOW large / hard / soft is it?
WHAT does it illuminate?
WHAT exposure relationship does it create?
```

Do not begin with:

```text
cinematic lighting
rim light
volumetric light
teal and orange
Rembrandt
neon glow
```

unless the scene or user request actually motivates them.

## 2. Lighting Design Order

For AUTO behavior, resolve lighting in this order:

```text
story / commercial purpose
-> location and time
-> visible or implied sources
-> dominant source
-> source direction
-> apparent source size / softness
-> ambient / bounce environment
-> fill or negative fill strategy
-> edge / back contribution if physically justified
-> practicals
-> exposure hierarchy
-> material / reflection consequences
-> atmospheric consequences
-> color / white-balance relationship
```

This order prevents decorative lighting from replacing scene logic.

## 3. Source Inventory

Before designing the image, identify plausible sources.

Examples:

```text
sun
sky
cloud cover
window
doorway
lamp
ceiling fixture
fluorescent tube
neon sign
streetlight
headlight
phone / monitor
fire
candle
stage light
softbox / book light
bounce card
large overhead diffusion
```

Classify each as:

```text
VISIBLE
IMPLIED
OFF-CAMERA PRODUCTION LIGHT
AMBIENT / ENVIRONMENTAL
EMISSIVE PRACTICAL
```

A production light may be invisible in frame, but its result should still make sense relative to the visible or implied world unless the user explicitly requests expressionistic lighting.

## 4. Motivation Strength

Use one of four levels:

### M0 - Available Light

The frame should appear lit only by sources naturally present in the location.

Good for:

- documentary;
- observational travel;
- naturalistic drama;
- candid portraiture.

### M1 - Enhanced Naturalism

Real sources are strengthened, softened, bounced, controlled, or extended without changing the apparent reason for the light.

This is the default cinematic realism mode.

### M2 - Stylized Motivation

The source is still plausible, but color, contrast, direction or intensity is pushed for expressive effect.

Examples:

- stronger moonlight than literal photometry would imply;
- more pronounced neon contamination;
- dramatic window shaft in haze.

### M3 - Expressionistic / Abstract

Lighting may deliberately ignore realistic source motivation.

Use only when the user or concept requests it.

Do not silently move an ordinary realistic request into M3.

## 5. Dominant Source Rule

Most believable scenes benefit from one clearly dominant lighting idea.

That does not mean there is only one source.

It means the viewer can understand the primary illumination relationship.

Examples:

```text
window is dominant; lamp is warm practical accent
sun is dominant; sky is fill
neon sign is dominant; street ambience fills shadows
soft commercial key is dominant; white studio environment supplies fill
```

Avoid giving every visible source equal visual authority.

## 6. Directional Coherence

For each source, reason about:

```text
azimuth / side
height
front / side / rear relationship
shadow direction
specular direction
reflection placement
```

If the key is camera-left, the image should not simultaneously create incompatible nose, object, and cast-shadow directions unless multiple sources explain it.

## 7. Apparent Source Size

Use visible consequences rather than empty adjectives.

### Large apparent source

Usually supports:

- broad wrap;
- gradual shadow transition;
- larger soft specular reflections;
- reduced micro-shadow harshness.

### Small apparent source

Usually supports:

- crisp shadow edges;
- strong shape definition;
- smaller/brighter specular highlights;
- less wrap.

Do not write `soft cinematic light` when a concrete source design is possible.

Prefer:

```text
large diffused window close to subject on camera-left, broad wrap, slow cheek-shadow transition
```

## 8. Distance and Falloff

Closer finite sources often create stronger near/far falloff.

Distant sources such as sun behave much more uniformly across human-scale scenes.

Use the consequence, not the inverse-square formula, in runtime prompts.

Useful language:

```text
rapid intimate falloff from the practical
background falls two visual steps darker away from the lamp
sun exposure remains comparatively uniform across the group
```

## 9. Ambient Environment

No object is lit only by the key.

Account for:

- sky;
- walls;
- floors;
- ceilings;
- nearby colored surfaces;
- large windows;
- atmospheric scattering;
- practical spill.

Ambient light should explain why shadow regions have their particular brightness and color.

## 10. Lighting and Material Response

Every lighting design must predict different responses for different materials.

Examples:

### Skin

- diffuse/subsurface body;
- directional specular sheen;
- local chroma variation;
- no uniform wax highlight.

### Matte fabric

- broad diffuse response;
- weave/fold visibility depends on grazing light;
- restrained specular response.

### Metal

- reflections dominate appearance;
- source/environment shape strongly visible;
- highlight position follows geometry.

### Glass

- transmission + reflection;
- source reflections should match environment;
- edges may catch stronger highlights.

### Car paint

- large source shapes create readable body gradients;
- environment reflections communicate form;
- glossy surfaces cannot have arbitrary painted-on highlights.

Lighting design is incomplete until these relationships are plausible.

## 11. Lighting and Atmosphere

Visible light beams require participating media such as:

- haze;
- smoke;
- dust;
- mist;
- moisture.

No atmosphere means no arbitrary solid `god rays` suspended in clean air.

Atmosphere also affects:

- distant contrast;
- color separation;
- backlight visibility;
- bloom around sources.

## 12. Lighting and Exposure Are Coupled

Lighting design must define what is allowed to be bright or dark.

Do not make every region perfectly readable.

Examples:

```text
window may run brighter than face
lamp filament may clip at its hottest core
shadow-side jacket may retain shape but not every weave detail
bright chrome may contain small specular clipping
```

Phase 4.4 expands exposure behavior, but motivation and exposure cannot be separated conceptually.

## 13. Portrait Pattern Handling

Named portrait patterns are geometric shorthand, not mandatory styles.

### Rembrandt

Use only when pose + key direction create a small cheek-side triangle of light.

### Loop

Short nose shadow angled slightly down/side without joining cheek shadow.

### Split

One side of face strongly lit, the other substantially darker.

### Butterfly

Frontal-high source creating a compact shadow under the nose.

### Broad / Short

Describe which side of the turned face receives the primary illumination relative to camera.

Do not request these by name if the current pose makes them geometrically impossible.

## 14. AUTO Defaults by Purpose

### Narrative drama

Default: M1 enhanced naturalism.

Prefer one dominant motivated source plus controlled ambient.

### Documentary / travel

Default: M0-M1.

Preserve believable available-light irregularity.

### Commercial / product

Default: M1-M2.

Production lighting may be less diegetic, but reflections and material geometry must remain physically coherent.

### Fashion / editorial

Default: M1-M3 depending concept.

Stylization may lead, but source geometry still needs internal consistency unless abstraction is intentional.

### Architecture

Default: M0-M1.

Respect actual window/sun/practical relationships and avoid impossible room-wide fill.

### Automotive

Default: M1-M2.

Use long source gradients/reflections to describe bodywork; do not paint fake highlight stripes disconnected from environment.

## 15. Lighting Lock Behavior

If the user specifies:

```text
golden hour
hard noon sun
single candle
Rembrandt lighting
flat overcast
neon only
```

that becomes a lock or high-authority lighting constraint.

AUTO may fill missing details around it, but must not silently replace the requested source logic.

If the request is contradictory, use `references/parameter-conflicts.md`.

## 16. Reference Match

From a reference image, infer only observable lighting properties such as:

```text
key appears camera-left and high
shadow transition is broad
background is around two visual stops darker
warm practical contamination on right edge
cool ambient fill in shadows
```

Do not claim exact fixture model, wattage, modifier size, measured lux, or exact lighting ratio without external evidence.

## 17. Anti-Cliche Rules

Never add automatically:

- perfect rim light;
- haze;
- volumetric beams;
- cyan/magenta split;
- warm key + cool rim;
- glowing eyes;
- universal eye light;
- symmetrical two-color edge lighting;
- practicals everywhere;
- dark moody exposure for every commercial;
- giant soft source for every portrait.

Each requires a reason.

## 18. Motivated Lighting Reality Gate

Before accepting the lighting design, ask:

1. What is the dominant source?
2. Why does it exist?
3. Where is it relative to camera and subject?
4. Does shadow direction agree?
5. Does specular response agree?
6. Does the source size match the shadow transition?
7. Does falloff make sense?
8. Is ambient fill plausible for the environment?
9. Are visible practicals contributing plausibly?
10. Are back/rim effects actually motivated?
11. Are colored lights spatially localized?
12. Do atmosphere and visible beams agree?
13. Is the exposure hierarchy believable?
14. Do material reflections agree with source geometry?
15. Did any cinematic cliché appear without a reason?

If multiple answers fail, lighting is not ready for full success.

## 19. Output Translation

Convert the design into observable instructions rather than jargon where possible.

Weak:

```text
cinematic Rembrandt lighting, volumetric, moody
```

Stronger:

```text
single large warm window source high on camera-left, broad but directional wrap across the face, reduced room bounce on the shadow side, practical lamp in the deep background only, no artificial rim light, background falling naturally darker away from the window
```

The provider adapter may compress or rephrase this later, but the internal design remains source-driven.