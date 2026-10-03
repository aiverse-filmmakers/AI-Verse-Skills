# Phase 4 Audit - Lighting, Exposure, Film Response, and Color

Status: PASSED

Phase 4 gate requirement:

> The skill can construct lighting/exposure/color logic that feels physically motivated rather than procedurally decorated.

This audit checks Tasks 4.1-4.7 as one integrated visual system.

## Files Audited

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`

## Gate Invariants

Phase 4 must preserve:

```text
source motivation before lighting style
lighting geometry before decorative effects
exposure hierarchy before HDR recovery
capture response != final grade
film stock != generic grain preset
color grade != source-light replacement
texture effects are optional
provider controls do not define creative truth
explicit locks remain authoritative
```

## Test Case A - Natural Window Portrait

Input intent:

```text
quiet portrait in a modest room near a window
natural, intimate, not glamorous
```

Expected system behavior:

- key motivation: window daylight;
- broad side source with soft transition;
- environmental bounce rather than mandatory frontal fill;
- no automatic rim light;
- exposure prioritizes face while allowing window to remain brighter;
- moderate natural saturation;
- skin remains integrated with room color;
- grain/halation/flare omitted unless separately motivated.

Result: PASS

No generic `cinematic portrait` bundle is required.

## Test Case B - Hard Noon Travel Exterior

Input intent:

```text
bright desert travel frame at noon, realistic heat and harsh sun
```

Expected behavior:

- small hard sun source;
- coherent hard shadow direction;
- sky/ground bounce in shadow areas;
- highlight clipping allowed where physically natural;
- no fake softbox facial light;
- warm/cool balance derives from sun, sky and ground rather than teal/orange grading;
- no unnecessary haze unless atmosphere/dust is present;
- clean texture may be correct.

Result: PASS

## Test Case C - Tungsten Interior + Daylight Window

Input intent:

```text
warm practical interior with cool daylight still visible outside
```

Expected behavior:

- preserve two source families;
- decide which source is near-neutral rather than neutralizing both;
- practicals motivate local warm pools;
- window/daylight contributes cooler ambient/fill;
- shadow color follows the mixed environment;
- grade preserves warm/cool separation without turning into equal orange/cyan split lighting.

Result: PASS

## Test Case D - Product Commercial

Input intent:

```text
premium reflective bottle, bright clean commercial image
```

Expected behavior:

- lighting shaped around readable form/reflections;
- controlled specular gradients;
- product color/brand constraints outrank an AUTO grade;
- high-key or bright exposure can remain cinematic;
- no forced film grain, flare, bloom, halation, lifted blacks or moody underexposure;
- material realism preserved through reflection/roughness logic.

Result: PASS

## Test Case E - Night Neon Street

Input intent:

```text
night street with actual red signage and cool ambient sky spill
```

Expected behavior:

- red light strongest on surfaces facing/near the sign;
- cool ambient appears where physically exposed to sky/environment;
- dark areas remain dark where justified;
- emissive color retains hue before clipping;
- no automatic cyan-magenta bilateral portrait setup;
- wet-surface reflections only if wetness is actually present;
- bloom/flare only around sufficiently bright sources and compatible optics.

Result: PASS

## Test Case F - Film Stock Lock

Input:

```text
Kodak VISION3 500T locked, night interior
```

Expected behavior:

- preserve stock lock;
- translate documented tungsten/high-speed/highlight/shadow/grain tendencies;
- do not force orange image;
- grade remains a downstream decision;
- grain remains controlled and contextual;
- halation not mandatory.

Result: PASS

## Test Case G - Clean Digital Camera Lock

Input:

```text
ARRI ALEXA 35 locked, clean commercial beauty frame
```

Expected behavior:

- preserve camera lock;
- translate highlight/color/detail intent without claiming literal LogC4 or measured dynamic range in the generated image;
- allow clean low-grain finish;
- no forced vintage artifacts;
- skin handling remains natural rather than orange/airbrushed.

Result: PASS

## Cross-System Checks

### Lighting vs exposure

PASS: lighting roles determine where brightness and contrast originate; exposure does not independently optimize every region.

### Lighting vs color

PASS: source colors constrain highlight/shadow color; grade does not replace source geometry.

### Capture response vs grade

PASS: camera/log/stock references remain separate from creative grade.

### Film vs texture

PASS: stock response, grain, halation, bloom and flare remain separate controls.

### Texture vs optics

PASS: flare/diffusion/sharpness must agree with lens/light/focus behavior.

### Provider independence

PASS: no Phase 4 file requires one provider-specific control surface.

### Explicit locks

PASS: camera, stock, lighting, color, grade and preservation locks remain authoritative.

## Anti-Cliche Audit

The system does not require any of the following for a cinematic result:

```text
shallow DOF
teal-orange grade
haze
god rays
rim light
anamorphic flare
grain
halation
bloom
lifted blacks
underexposure
warm skin
cool shadows
```

Result: PASS

## Architecture Audit

```text
scope violations: 0
standalone dependency violations: 0
provider-core contamination: 0
explicit-lock violations: 0
reference-certainty violations: 0
hidden conflict resolution: 0
capture-vs-grade conflation: 0
film-vs-effect conflation: 0
```

## Phase 4 Gate Verdict

**PASSED**

Phase 4 provides a coherent provider-neutral system for:

```text
motivated lighting
key/fill/negative-fill/edge/bounce/practicals
scene-specific lighting patterns
exposure hierarchy and dynamic-range appearance
film/sensor response
white balance and grading
color separation and density
grain/halation/bloom/flare/texture restraint
```

Phase 5 may now build physical-realism diagnosis and repair on top of this lighting/color foundation.
