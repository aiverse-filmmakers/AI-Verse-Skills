# Phase 1 Research Supplement - SUMMILUX-C and Master Prime

Status: RESEARCH EVIDENCE

This supplement closes two evidence gaps identified in `lenses.md` during Task 1.5. It is additive Phase 1 evidence and does not change the Phase 0 architecture contract.

## Leitz SUMMILUX-C

Primary source: Leitz Cine, official SUMMILUX-C product page.

Classification: `CONFIRMED` for manufacturer-stated optical behavior, with normal caution around qualitative marketing language.

First-party material supports the following observable tendencies:

- high clarity and resolution;
- accurate color rendition;
- strong contrast without requiring a harsh clinical appearance;
- correction of chromatic aberration and breathing;
- nearly distortion-free, telecentric design;
- consistent illumination and resolution from center toward the edges;
- warm, natural skin reproduction;
- gentle focus rolloff;
- sharp detail combined with a softer, creamy facial impression rather than brittle digital sharpness;
- edge character can become more noticeable when the image circle is pushed toward coverage limits.

### Safe generative translation

When `Leitz SUMMILUX-C` is locked or selected:

- render high resolving detail without digital oversharpening;
- preserve natural, warm skin and smooth facial tonal transitions;
- use gentle focus falloff rather than abrupt cutout-style blur;
- keep geometric distortion restrained;
- avoid exaggerated chromatic fringing;
- keep color clean and natural rather than forcing a heavy vintage cast;
- allow modest edge character only when framing/format use plausibly pushes toward the lens image-circle limits.

### Avoid

Do not translate SUMMILUX-C into generic `vintage Leica haze`, extreme softness, heavy flare, or low contrast. The first-party description is fundamentally a high-performance natural-image design.

## ARRI / ZEISS Master Prime

Primary sources: ARRI official Master Prime product page and ZEISS official ARRI/ZEISS Master Prime material.

Classification: `CONFIRMED` for documented optical behavior.

First-party documentation supports:

- T1.3 high-speed operation across the prime family;
- high resolution and contrast;
- extremely low geometric distortion;
- strongly reduced flare;
- virtually no focus breathing;
- consistent optical performance across the T-stop range;
- clean, neutral image character in practitioner testimony published by the manufacturer;
- anti-reflection coating designed to reduce veiling glare/internal reflections and maintain deeper blacks and contrast.

### Safe generative translation

When `ARRI/ZEISS Master Prime` is locked or selected:

- favor a clean, high-resolution, high-contrast image without brittle edge sharpening;
- keep geometry controlled, especially compared with deliberately vintage or character-heavy optics;
- keep flare restrained unless strongly motivated by source placement;
- avoid focus-breathing implications in any still-frame simulation;
- allow shallow depth at wide aperture when it supports the shot, but do not make maximum blur mandatory;
- preserve a comparatively neutral, precise optical impression rather than inventing warmth, haze, swirls, or strong aberrations.

### Avoid

Do not translate `Master Prime` into a generic `cinema lens` preset containing anamorphic streaks, vintage bloom, warm veiling haze, or heavy edge softness.

## Updated Task 1.5 Strength

With these sources added, first-party evidence is now strong for:

- ARRI Signature;
- ARRI/ZEISS Master Prime;
- Leitz SUMMILUX-C;
- Panavision G-Series;
- Cooke Panchro Classic;
- ZEISS Supreme / Supreme Radiance;
- Hawk V-Lite;
- Angenieux Optimo technical behavior.

Remaining weaker areas include:

- detailed Canon K35 optical character beyond first-party historical package information;
- some still-photography lens families exposed as provider presets, where manufacturer evidence may not map cleanly to cinema use;
- exact generative-model interpretation strength for any named lens family, which must be established empirically in later evals.

## Source Notes

- Leitz Cine SUMMILUX-C: https://www.leitz-cine.com/product/summilux-c
- ARRI Master Prime: https://www.arri.com/en/cine-lenses/arri-zeiss-fujinon-lenses/master-primes/master-primes
- ZEISS ARRI/ZEISS lenses: https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/arrizeiss.html

These URLs are provenance references, not runtime dependencies.