# Film Stock and Sensor Response Mapping

Status: RUNTIME KNOWLEDGE

Purpose: translate named film stocks, digital cinema references, and analog/low-fi capture intent into observable image behavior without pretending an AI image model performs literal emulsion chemistry or sensor simulation.

Use with:

- `references/professional-quality-floor.md`
- `references/texture-effects-restraint.md`
- `references/exposure-and-dynamic-range.md`
- `references/color-science-and-grading.md`

## Core Separation

Keep these independent:

```text
capture medium
capture format
named stock / camera reference
exposure / tonal response
color response
base professional texture
stock-specific visible grain / digital noise
halation / bloom / flare
sharpness / acutance
final grade
```

Do not collapse them into one `film look` token.

## Base Texture vs Stock Grain

The Professional Quality Floor normally permits a **subtle organic filmic finishing texture** on photographic work.

That base texture is not the same thing as saying the image was shot on film or adding visibly strong stock grain.

```text
subtle base texture = normal finishing choice for most photographic/cinematic output
visible stock-specific grain = capture/style decision whose strength follows stock/format/exposure intent
```

Therefore:

- a premium digital-cinema image may have extremely fine organic texture without pretending to be film;
- a clean mobile image may have barely perceptible texture while retaining phone character;
- a pristine product/clinical image may reduce/remove the base texture;
- a 16mm/Double-X/Super-8 request may justify substantially more visible stock-specific grain.

## Named Reference States

A named camera/stock may be:

```text
USER LOCKED
AUTO SELECTED
PROVIDER-NATIVE PRESET
REFERENCE HYPOTHESIS
```

Always preserve observable intent even if the active provider cannot represent the literal name.

## Modern High-End Digital Cinema

Useful observable targets:

- controlled highlight rolloff;
- retained saturated-highlight differentiation;
- rich/open shadows according to exposure intent;
- restrained digital sharpening;
- natural skin separation;
- stable color relationships;
- professional grade rather than flat log unless requested;
- fine organic finishing texture when compatible.

Never claim the AI output literally contains LogC4, S-Log3, BRAW, X-OCN, REDCODE, physical photosite behavior, or measured dynamic range.

## ARRI / ALEXA-Like Tonal Target

When ALEXA/ARRI is explicitly locked—or when cinematic AUTO uses an ARRI-like observable tonal target—translate toward:

```text
smooth controlled highlights
gentle highlight-to-mid transition
natural skin tonal separation
rich readable shadows according to exposure
high detail without brittle edge enhancement
restrained color density
fine non-sterile texture when appropriate
```

Do not automatically add:

- strong film grain;
- halation;
- vintage softness;
- warmth;
- anamorphic behavior.

`ARRI-like` is an observable tonal target, not literal sensor simulation.

## Other Modern Cinema References

### Sony VENICE / VENICE 2

- polished contemporary cinema response;
- broad highlight/shadow intent;
- low-light flexibility where relevant;
- natural color foundation;
- controlled high-resolution detail.

Do not force a stereotyped cool `Sony color`.

### RED V-RAPTOR

- contemporary high-resolution cinema capture;
- clean geometry/detail;
- broad exposure intent;
- do not invent a visible `global-shutter look` in a still.

### Canon C500 Mark II

- modern cinema response;
- natural color/skin;
- broad tonal retention;
- controlled sharpness.

### Blackmagic URSA Mini Pro

- professional post-friendly cinema response;
- natural controllable color;
- model-specific claims only when evidence/user specificity supports them.

## 35mm Motion Negative - General

May justify:

- organic visible grain at an appropriate strength;
- gradual highlight transition;
- dense midtones;
- non-brittle sharpness;
- slight texture irregularity;
- stock/grade-specific color rather than universal warmth.

Do not automatically add orange halation, faded blacks, scratches, dust, gate weave, or extreme grain.

## Kodak VISION3 500T

Observable target:

```text
tungsten-origin negative logic
low-light/night usefulness
gradual highlight handling
information-rich shadows with controlled grain
color determined by sources/WB/grade rather than automatic orange
grain more apparent in darker values when appropriate
```

Avoid mandatory orange/teal, heavy coarse grain, or mandatory halation.

## Kodak VISION3 250D

Observable target:

```text
daylight-origin negative logic
controlled broad highlights
finer/moderate grain intent
natural daylight color foundation
```

Useful for exterior narrative, daylight travel, lifestyle/commercial film texture.

## EASTMAN DOUBLE-X

- true monochrome tonal design;
- assertive black-and-white character where desired;
- visible organic grain;
- careful face/specular separation;
- luminance hierarchy rather than desaturated color pretending to be B&W.

## EKTACHROME 100D

- daylight reversal-film intent;
- crisp color separation;
- moderately stronger saturation;
- fine grain/high apparent definition;
- more direct contrast/density than a soft-negative interpretation.

Avoid generic `retro warm film` treatment.

## Portra Family

Primarily still-photo/editorial/portrait reference:

- fine stock-appropriate grain;
- natural skin emphasis;
- controlled/moderate color;
- broad practical utility.

Do not confuse Portra with VISION3 motion-negative behavior.

## Ektar 100

- vivid but controlled color;
- high sharpness/fine grain;
- strong landscape/product/travel color separation.

Avoid synthetic neon saturation.

## T-MAX Family

- fine B&W grain;
- high acutance;
- clean monochrome tonal separation;
- not automatically coarse/vintage.

## 16mm

May justify:

- more visible grain than comparable 35mm treatment;
- slightly less pristine fine-detail rendering;
- stronger mids/shadow texture.

Do not automatically make it scratched, dirty, unstable, green, orange, or underexposed.

## 8mm / Super 8-Like

May justify more obvious grain/texture, lower fine-detail fidelity, consumer-film character, and exposure/color irregularity when requested.

Dust, scratches, jitter and light leaks remain separate choices.

## 65/70mm

Safe generic translation:

- very large capture-area intent;
- fine-grained/high-detail impression when stock/process supports it;
- theatrical clarity;
- depth/perspective still controlled by geometry/lens choices.

Do not invent one IMAX palette, mandatory shallow DOF, or unsupported proprietary behavior.

## Analog Video / VHS

Not film.

Possible traits:

- lower resolution;
- chroma/luma softness;
- analog noise;
- limited highlight behavior;
- color bleed;
- interlace/scan cues;
- tape instability when requested.

Do not add film grain/photochemical halation by default.

## Low-Fi Digital / Pixelvision-Like

Possible traits:

- low resolution;
- electronic edges;
- constrained tonal range;
- digital noise/artifacts;
- unconventional color response.

Do not turn it into aged film unless intentionally hybridized.

## Visible Grain Rules

Visible stock-specific grain should consider:

```text
format size
stock speed
exposure
scan/enlargement impression
tonal region
grain scale
grain strength
```

Use the **least visible stock-grain strength that communicates the chosen capture character**, while retaining the separate subtle base finishing texture defined by the Professional Quality Floor.

Do not make every cinematic frame obviously grainy.

## Digital Noise

Digital sensor noise is distinct from both film grain and subtle organic finishing texture.

If low-light digital noise is appropriate:

- keep it exposure-dependent;
- avoid uniform overlays;
- preserve underlying material detail;
- do not use ugly noise merely as an authenticity token.

## Halation, Bloom, Flare

These remain separate systems.

A stock/camera name never automatically enables them.

- **halation**: localized film-layer/light interaction approximation around sufficiently bright boundaries;
- **bloom**: broader bright-value spread from optics/sensor/filtration/atmosphere/post;
- **flare**: source/lens-geometry-dependent internal reflection/scatter.

## Tungsten vs Daylight Balance

Do not translate stock balance into a final color cast.

```text
capture balance + actual source spectrum + WB/filtration + grade = visible color
```

So `500T != orange` and `250D != blue`.

## Weak-Evidence Stock / Camera Lock

If the user names a weakly documented reference:

1. preserve the literal name as a lock;
2. pass it to a provider that explicitly supports it when appropriate;
3. do not fabricate detailed physics;
4. use only broad defensible observable traits;
5. state uncertainty only when explanation is relevant.

## Provider-Native Presets

Provider presets are provider-specific behavior, not universal film/camera truth.

A provider may map a named stock/camera when explicitly selected, but the core keeps the observable professional target. Another provider may interpret the same token differently.

Magnific/Higgsfield presets are used only under explicit-target/benchmark execution rules.

## Capture Response vs Grade vs Lighting

Capture response, lighting and final grade remain separate.

A stock/camera may influence how highlights/shadows/color are interpreted, but source direction/size/falloff, material response, and final creative grade remain independent systems.

## Reality Gate

Check:

1. Is the medium correctly classified?
2. Is a named camera/stock actually locked or deliberately selected?
3. Are documented traits translated into observable behavior rather than fake specs?
4. Is subtle base texture appropriate to the professional finish?
5. Is visible grain appropriate to format/stock/exposure intent?
6. Are halation/bloom/flare separate?
7. Is balance being confused with final color?
8. Is provider-native behavior being mistaken for universal truth?
9. Are weak-evidence references handled conservatively?
10. Does capture response support the image purpose rather than act as prestige decoration?

## Runtime Example

Weak:

```text
shot on Kodak 500T, cinematic grain, halation, film look
```

Stronger:

```text
VISION3 500T-inspired night response: gradual rolloff around warm practicals, dense but information-rich shadows, restrained stock-specific grain more visible in darker midtones, tungsten-origin color logic without forcing an orange cast; retain the image's fine organic professional base texture, with no added halation or flare unless bright-source/optical geometry justifies it
```
