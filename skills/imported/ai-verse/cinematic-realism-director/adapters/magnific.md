# Magnific Cinematic Adapter

Status: RUNTIME ADAPTER
Task: 7.6
Verified against Magnific's live connected model/settings surface: 2026-10-03

Purpose: translate the provider-neutral Cinematic Shot Spec into Magnific's current Cinematic image model controls plus prompt language, without treating Magnific's UI ontology as the universal cinematic brain.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
Magnific Cinematic controls = provider-specific execution layer
```

The adapter maps only verified current controls. Unsupported or more precise intent remains in prompt language.

If the current Magnific schema differs from this file, use live verified settings when available; otherwise fall back to `adapters/generic.md`.

## Current Verified Surface

Magnific's live current image catalog exposes a model named `Cinematic` with:

- 1K, 2K, and 4K output options;
- common photographic/cinematic aspect ratios;
- image, character, and product references;
- an optional `cinematicControls` settings layer.

The current `cinematicControls` groups are:

```text
camera
lensBrand
focalLength
aperture
shotType
filmStock
movieLook
lighting
motionBlur
grain
halation
tonalLook
```

These are provider-specific controls, not proof of literal physical camera/lens/film simulation.

## Mapping Rule

For each resolved universal field:

1. check whether an exact compatible Magnific enum exists;
2. if yes, map it into the native control;
3. keep any nuance not represented by the enum in prompt language;
4. if no exact compatible control exists, leave the native field on Auto/unused and describe the visible intent in the prompt;
5. never force the closest-looking control if it changes a user lock.

## Camera Mapping

Current live camera choices include:

```text
Auto
ARRI ALEXA 35
ARRI ALEXA Mini LF
Sony VENICE
Sony VENICE 2
RED V-RAPTOR
Blackmagic URSA Mini Pro
Canon C500 Mark II
Sony FX9
IMAX 70mm
35mm film
8mm film
medium format
VHS camcorder
Pixelvision
```

Note: this provider category mixes camera bodies, capture formats, film media, and legacy acquisition references. Keep the universal schema's `capture_medium`, `capture_format`, and `camera_reference` separate internally even when mapping them into this single provider field.

If the universal request is more precise than the available enum, preserve the precision in prompt language.

## Lens Mapping

Current live choices include families and exact references such as:

```text
Panavision G-Series
ZEISS Master / Master Prime
Cooke S4
Cooke Panchro
ARRI Signature
Canon K35
Leica / Leitz Summilux / Summilux-C
Cooke Anamorphic/i
Hawk V-Lite anamorphic
Angenieux Optimo
selected still-photo lens families
Auto
```

Native lens choice does not replace focal length, aperture, camera distance, or explicit perspective instructions.

If a user locks a lens not present in the live enum, do not substitute a different lens family. Leave native lens control neutral/Auto and express the locked observable lens character in the prompt.

## Focal Length Mapping

Current verified values:

```text
14mm
24mm
35mm
50mm
85mm
135mm
200mm
Auto
```

If the user locks an unsupported focal length, preserve the requested field of view/perspective behavior in prompt language and do not round silently.

Perspective still comes primarily from camera position, not focal length alone.

## Aperture Mapping

Current verified values:

```text
f/1.2
f/1.4
f/2
f/2.8
f/4
f/5.6
f/8
f/11
f/16
Auto
```

Do not choose maximum aperture merely for cinematic effect.

If the universal shot calls for a depth result that conflicts with an exact locked aperture, preserve the lock and resolve through distance/geometry where possible.

## Shot Type Mapping

Current `shotType` combines framing, subject orientation, and camera angle.

It includes:

- extreme close / close / medium / three-quarter / long / wide variants;
- front / 45-degree / profile variants;
- over-shoulder;
- back;
- POV;
- high angle;
- low angle;
- Dutch angle;
- bird's-eye;
- worm's-eye.

Mapping rule:

- use a native shotType only when it agrees with all locked geometry;
- if one compound preset conflicts with the universal camera height/orientation/framing, do not let the compound preset override the shot;
- use prompt language for the unresolved dimensions.

## Film Stock Mapping

Current Magnific controls include Kodak, Fuji, Ilford, CineStill, Lomography, Agfa, and Polaroid presets, including documented universal references such as:

```text
Kodak VISION3 500T
Kodak VISION3 250D
Kodak Portra 400/800
Kodak Ektar 100
Kodak Tri-X 400
Kodak T-MAX 400
Ektachrome E100
```

When a stock exists natively:

- map the literal stock when user-locked;
- keep universal observable response rules active;
- do not assume the provider preset is a literal emulsion simulation.

For stocks with weaker universal evidence, native provider use may still be allowed when explicitly requested, but do not invent physical claims about them.

## Lighting Mapping

Current live lighting presets include environmental, portrait-pattern, contrast, studio, practical, and directional concepts such as:

```text
golden hour
blue hour
overcast
hard sunlight
natural window
Rembrandt
butterfly
loop
split
broad
short
high-key
low-key
rim
backlight
three-point
neon
chiaroscuro
candle
moonlight
volumetric
dappled
studio soft
beauty dish
parabolic
practical
silhouette
contre-jour
bounce
overhead
```

Because these presets collapse multiple lighting dimensions, never let a preset replace the universal motivated-lighting design.

Use a native preset when it is compatible; retain source direction, motivation, fill, ambient, exposure, and material-response nuance in the prompt.

Do not automatically select rim, volumetric, neon, or chiaroscuro merely because the requested image is cinematic.

## Motion Blur Mapping

Current verified choices include:

```text
none
subtle cinematic
moderate cinematic
heavy cinematic
subject-only motion blur
camera-only motion blur
rack-focus/pull blur
zoom blur
long-exposure light trails
```

Map only when the universal motion/shutter system calls for that behavior.

`cinematic` in a provider label is not sufficient reason to add blur.

## Grain Mapping

Current verified choices:

```text
35mm silver-halide
16mm coarse
fine organic sensor noise
barely visible shadow grain
```

Use only when capture intent justifies texture.

Do not combine grain with film stock automatically if the desired result is clean.

## Halation Mapping

Current verified choices:

```text
none
warm orange-red halo
strong warm bloom
green-yellow fringe
```

Treat these as provider approximations. Halation, bloom, and flare remain separate concepts in the universal brain.

Do not enable visible halation automatically for film stocks.

## Tonal Look Mapping

Current live values include provider presets referencing:

```text
Kodak VISION3 500T
Fujifilm ETERNA 500
Kodak Portra 400
Kodak Double-X
ARRI ALEXA natural
Sony VENICE natural
```

Use `tonalLook` only when it supports the resolved color/tone system.

Do not stack camera + stock + tonalLook redundantly if the combined controls begin to fight the user's requested grade.

## Movie Look Policy

Magnific exposes named movie/filmmaker convenience looks plus a documentary-natural option.

These are not universal ontology fields.

Rules:

- do not choose a named movie/filmmaker preset in AUTO merely to make a shot cinematic;
- if the user explicitly requests a named provider look and current product policy permits it, use the provider control;
- otherwise decompose the desired look into observable palette, contrast, lighting, composition, texture, and production-design traits.

## Prompt + Controls Cooperation

Native controls should reduce ambiguity, not duplicate or contradict the prompt.

Good pattern:

```text
native camera = ARRI ALEXA 35
native focal = 35mm
native aperture = f/2.8
prompt = camera at chest height, close observational distance, motivated soft window key from camera-left, restrained fill, dense natural shadows, neutral skin, moderate depth with continuous falloff
```

Bad pattern:

```text
native camera/lens/focal/aperture all set
prompt contains several contradictory camera/lens/focal/aperture choices
```

## References

Current Magnific Cinematic supports image, character, and product references.

Preserve universal reference roles:

- identity/character;
- product geometry/material;
- image/style/composition where supported by host semantics.

If the provider does not expose a role needed by the universal shot, explain the role in prompt language and do not assume reference type alone communicates all constraints.

## Editing / Reality Repair

Magnific exposes multiple dedicated image operations beyond full regeneration. Reality Repair should choose the smallest appropriate operation when the active host exposes it.

Examples include:

- regional retouching;
- relighting;
- structure-preserving reimagination;
- restyling;
- expansion;
- quality/upscale operations.

Do not use general `images_generate` re-rendering for a pixel-preserving/local edit when a dedicated preservation-aware tool is available.

The universal preserve/change/reality-diagnosis contract remains authoritative.

## Output Settings

Current Cinematic model supports 1K, 2K, and 4K plus common ratios.

Use exact provider settings only when verified live. Otherwise preserve requested output framing in the generic prompt/spec.

## Live-Schema Drift Rule

Before execution through a connected Magnific environment, prefer the current model catalog/settings over this cached adapter.

If drift is detected:

```text
live verified schema
> cached provider adapter
> generic adapter
```

But at every level:

```text
user locks + universal shot spec
> provider defaults
```

## Sources

Provider-specific evidence:

- live Magnific `Cinematic` model catalog and `cinematicControls` settings rechecked 2026-10-03;
- local `references/research/magnific.md`.

The live connected provider is optional. The standalone skill can still use this cached mapping and degrade to generic prompt output.

## Acceptance

Task 7.6 passes when Magnific's current native cinematic controls are used where exact, prompt language carries unsupported nuance, compound provider presets never override universal geometry/lighting locks, and current live schema can safely supersede cached enums without redesigning the shot.