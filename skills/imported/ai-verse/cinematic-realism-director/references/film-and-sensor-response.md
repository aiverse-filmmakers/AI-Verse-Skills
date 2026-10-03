# Film Stock and Sensor Response Mapping

Status: RUNTIME KNOWLEDGE
Task: 4.5

This reference translates named film stocks, digital cinema references, and analog/low-fi capture intent into observable image behavior without pretending an AI image model performs literal emulsion chemistry or sensor simulation.

Evidence basis:

- `references/research/film-stocks.md`
- `references/research/cameras.md`
- `references/cameras-and-capture-formats.md`
- `references/exposure-and-dynamic-range.md`

## 1. Core Rule

Separate:

```text
capture medium
capture format
named stock / camera reference
exposure behavior
color response
grain / noise
halation / bloom
sharpness / acutance
final grade
```

Do not collapse them into one `film look` token.

## 2. Named Reference Behavior

A named camera or stock may be:

```text
USER LOCKED
AUTO SELECTED
PROVIDER-NATIVE PRESET
REFERENCE HYPOTHESIS
```

The runtime brain should always preserve the observable intent even if the active provider cannot represent the exact name.

## 3. Digital Cinema Response

For modern high-end digital cinema references, describe visible consequences rather than acquisition jargon.

Possible observable traits:

- controlled highlight rolloff;
- retained saturated highlight color;
- clean shadow information when exposure supports it;
- restrained digital sharpening;
- natural skin separation;
- stable color across exposure;
- low-light cleanliness where appropriate;
- finished grade rather than flat log unless explicitly requested.

Never claim the AI output literally contains:

- LogC4;
- S-Log3;
- BRAW;
- X-OCN;
- REDCODE;
- real sensor photosite behavior;
- measured dynamic range.

## 4. ALEXA 35 Reference

When explicitly locked or meaningfully selected:

```text
highlight behavior: smooth and controlled
bright saturated color: retain differentiation where plausible
skin: natural tonal separation
shadow behavior: open or dense according to exposure, not artificially lifted
sharpness: high detail without brittle digital edge enhancement
texture: restrained, capture-character dependent
```

Do not auto-add grain, halation, or vintage softness merely because the user says ARRI.

## 5. Sony VENICE 2 Reference

Useful runtime translation:

- polished contemporary digital cinema;
- broad highlight/shadow retention;
- strong low-light flexibility when story requires;
- natural color foundation;
- controlled high-resolution detail.

Do not force a stereotyped `Sony color` or cool cast.

## 6. RED V-RAPTOR Reference

Useful translation:

- contemporary large-format high-resolution capture;
- clean geometry and detail;
- broad exposure intent;
- strong motion cleanliness if [X]/global-shutter context is explicitly relevant, without inventing a visible `global shutter look` in a still.

## 7. Canon C500 Mark II Reference

Useful translation:

- modern cinema response;
- natural color and skin;
- broad tonal retention;
- controlled sharpness.

Do not force `warm Canon skin` unless the requested grade/light supports it.

## 8. Blackmagic URSA Mini Pro Reference

Useful translation:

- professional cinema capture;
- post-friendly tonal response;
- natural, controllable color;
- model-specific exact claims avoided unless user names the variant.

## 9. 35mm Motion Negative - General

A generic 35mm negative-film intent may justify:

- organic but restrained grain;
- gradual highlight transition;
- dense midtones;
- non-brittle sharpness;
- slight texture irregularity;
- color response chosen by stock/grade rather than universal warmth.

Do not auto-add:

- orange halation;
- faded blacks;
- scratches;
- dust;
- heavy gate weave;
- extreme grain.

Those are separate conditions/effects.

## 10. Kodak VISION3 500T

Evidence-backed runtime translation:

```text
balance: tungsten-origin negative stock
use case: low light / night / tungsten / mixed practicals
highlights: broad, gradual handling
shadows: retained information with controlled grain
color: not automatically orange; grade and source determine visible balance
grain: present but controlled, especially in darker values when appropriate
```

Good AUTO contexts:

- night narrative;
- tungsten practical interiors;
- mixed-light city work;
- low-light portrait.

Avoid:

- making every 500T image orange/teal;
- heavy coarse grain by default;
- mandatory halation.

## 11. Kodak VISION3 250D

Runtime translation:

```text
balance: daylight-origin negative stock
use case: daylight / controlled exterior / brighter interiors
highlights: controlled and broad
shadows: moderate/fine grain intent
color: natural daylight foundation
grain: finer/moderate relative to high-speed stock intent
```

Good for:

- exterior narrative;
- daylight travel;
- commercial/lifestyle with film texture.

## 12. EASTMAN DOUBLE-X

Runtime translation:

- true monochrome tonal design;
- assertive black-and-white contrast character where desired;
- visible organic grain;
- careful face/specular separation;
- luminance hierarchy rather than desaturated color masquerading as B&W.

Avoid:

- color fringing;
- fake sepia unless separately requested;
- HDR monochrome with equal detail everywhere.

## 13. EKTACHROME 100D

Runtime translation:

- daylight reversal-film intent;
- crisp color separation;
- moderately stronger saturation;
- fine grain/high apparent definition;
- more direct density/contrast relationship than a soft negative interpretation.

Avoid:

- neon oversaturation;
- posterization;
- generic `retro warm film` treatment.

## 14. Portra Family

Use primarily for still-photo/editorial/portrait references.

Observable target:

- fine grain for speed class;
- natural skin emphasis;
- controlled/moderate color;
- broad practical utility.

Do not confuse Portra with VISION3 motion negative behavior.

## 15. Ektar 100

Observable target:

- vivid but controlled color;
- high sharpness/fine grain;
- strong landscape/product/travel color separation.

Avoid clipping saturated objects into synthetic neon patches.

## 16. T-MAX Family

B&W target:

- fine grain;
- high acutance/sharpness;
- clean monochrome tonal separation;
- not automatically coarse or vintage.

## 17. 16mm

Generic 16mm intent may justify:

- more visible grain than comparable 35mm treatment;
- slightly less pristine fine-detail rendering;
- texture becoming more perceptible in mids/shadows;
- handheld/documentary associations only if the concept requires them.

Do not make 16mm automatically:

- unstable;
- scratched;
- dirty;
- green;
- orange;
- underexposed.

## 18. 8mm / Super 8-Like Intent

May justify:

- more obvious grain/texture;
- lower fine-detail fidelity;
- stronger home-movie/consumer-film character;
- possible exposure/color irregularity if requested.

But scratches, dust, frame jitter and light leaks remain separate optional effects.

## 19. 65/70mm Film Reference

Safe generic translation only:

- very large capture-area intent;
- fine-grained/high-detail impression when stock/process supports it;
- large-scale theatrical clarity;
- depth/perspective still determined by geometry and lens choices.

Do not invent:

- one fixed IMAX palette;
- mandatory shallow DOF;
- specific grain level without stock/process;
- proprietary camera behavior unsupported by evidence.

## 20. Analog Video / VHS

This is not film.

Possible observable intent:

- lower resolution;
- chroma/luma softness;
- analog noise;
- limited highlight handling;
- color bleed;
- interlaced/scan-like artifacts where appropriate;
- tape instability only when desired.

Do not add film grain or photochemical halation by default.

## 21. Low-Fi Digital / Pixelvision-Like Intent

Possible visible behavior:

- low resolution;
- electronic edge behavior;
- constrained tonal range;
- sensor/noise artifacts;
- unconventional color response.

Do not make it look like aged film unless user requests hybridization.

## 22. Film Grain Rules

Grain is not uniform noise.

Reason about:

```text
format size
stock speed
exposure
scan/enlargement impression
tonal region
grain scale
grain strength
```

Default rule:

> Use the least grain required to communicate the chosen capture character.

Do not make every cinematic frame visibly grainy.

## 23. Digital Noise Rules

Digital sensor noise is distinct from film grain.

If a low-light digital reference calls for noise:

- keep it exposure-dependent;
- avoid uniform monochrome overlay;
- preserve material detail beneath it;
- avoid using noise merely to make AI imagery feel `real`.

## 24. Halation, Bloom, and Flare Are Separate

### Halation

Film-layer/light interaction approximation around strong highlights.

### Bloom

Broader bright-source glow/spread that may come from optics, sensor, filtration, atmosphere, or post interpretation.

### Lens flare

Internal optical reflection/scatter tied to source-lens geometry.

Never turn a stock name into automatic visible halation + bloom + flare.

Task 4.7 handles these effects in depth.

## 25. Tungsten vs Daylight Balance

Do not translate balance into a color filter.

Correct logic:

```text
stock/capture balance
+
actual source spectrum
+
white balance / filtration
+
grade
=
visible color relationship
```

So:

```text
500T != orange
250D != blue
```

## 26. Stock Lock with Weak Evidence

If the user names a stock for which the universal brain lacks strong evidence:

1. preserve the stock name as a lock;
2. pass the literal name to a provider that supports it;
3. do not fabricate detailed physics;
4. use only broad, defensible observable traits if known;
5. record uncertainty when explaining the result.

## 27. Provider-Native Stock Presets

A provider preset is provider-specific behavior.

It does not become universal film truth.

If Magnific or another provider exposes a literal stock preset:

- adapter may map to it;
- core keeps the user intent/observable target;
- do not assume another provider interprets the same token identically.

## 28. Film/Sensor vs Grade

Capture response and final grade are separate.

Examples:

- 500T can be graded cool, warm, neutral, saturated, muted;
- ALEXA footage can be high-key, low-key, colorful, monochrome;
- reversal film can still receive a stylized digital grade.

Do not hard-wire a grade into the capture reference.

## 29. Film/Sensor vs Lighting

Capture medium does not replace lighting design.

A stock/camera may influence how highlights/shadows/color are interpreted, but source direction, size, falloff, and material response remain independent systems.

## 30. Film/Sensor Reality Gate

Check:

1. Is the medium correctly classified as film, digital, analog video, or low-fi digital?
2. Is the named stock/camera actually user-supplied or deliberately selected?
3. Are documented traits translated into visible behavior rather than fake specs?
4. Is grain appropriate to format/speed/exposure intent?
5. Are halation/bloom/flare being kept separate?
6. Is tungsten/daylight balance being confused with final color?
7. Is the final grade independent of the acquisition reference?
8. Is a provider-native preset being mistaken for universal truth?
9. Are weak-evidence references handled conservatively?
10. Does the capture response support the story rather than exist as prestige decoration?

## 31. Runtime Translation Example

Weak:

```text
shot on Kodak 500T, cinematic grain, halation, film look
```

Stronger:

```text
VISION3 500T-inspired night response: gradual rolloff around warm practicals, dense but information-rich shadows, restrained organic grain visible mostly in the darker midtones, tungsten-origin color logic without forcing an orange cast; no added halation or flare unless a bright source and optical setup justify it
```

The named reference becomes useful only after it is decomposed into observable behavior.