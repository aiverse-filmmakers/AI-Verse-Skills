# Phase 1 Research - Film Stocks and Photochemical Response

Status: RESEARCH EVIDENCE

Primary classification: `CONFIRMED` for manufacturer-documented stock behavior, `CORROBORATED` for cinematographer testimony, and `INFERRED` only when explicitly stated.

This file records film-stock characteristics that can later be translated into visible generative cues. It does not claim that an AI image model performs literal photochemical emulsion simulation when prompted with a film-stock name.

## Governing Principle

A named film stock is useful only when the skill understands the **observable consequences** associated with it.

Relevant dimensions include:

- color or B&W;
- daylight/tungsten balance;
- sensitivity / intended lighting conditions;
- highlight latitude;
- shadow detail/noise/grain behavior;
- saturation;
- color bias/neutrality where documented;
- grain scale and visibility;
- sharpness/acutance;
- contrast/tonal scale;
- reversal versus negative behavior.

The skill should never reduce all film simulation to `add grain and warm colors`.

## Kodak VISION3 500T 5219/7219

Source: `FILM-KODAK-001`.

Kodak first-party material documents:

- tungsten-balanced motion-picture negative stock;
- high sensitivity suited to low-light/tungsten/night work;
- design emphasis on increased highlight latitude;
- improved signal-to-noise/shadow detail;
- Kodak's DLT technology intended to reduce grain in shadows.

### Safe generative translation

A 500T reference may justify:

- night/interior capability without crushing all shadow information;
- gradual bright-practical/highlight handling;
- visible but controlled organic grain, especially in darker values when aesthetically appropriate;
- tungsten-origin color logic while allowing the final grade/white balance to vary;
- dense blacks with retained low-end information rather than lifted HDR gray.

Do not automatically make the entire image orange. Tungsten-balanced stock can be corrected, mixed, pushed, pulled and graded in many ways.

## Kodak VISION3 250D 5207/7207

Source: `FILM-KODAK-002`.

Kodak documents:

- daylight-balanced motion-picture negative stock;
- extended highlight latitude;
- reduced shadow grain relative to earlier generations;
- medium-speed role suitable for daylight and controlled lighting.

### Safe generative translation

- clean natural-daylight color foundation;
- controlled highlights in bright exterior conditions;
- moderate/fine grain rather than coarse high-speed texture;
- balanced shadow detail without artificial HDR lifting.

## EASTMAN DOUBLE-X 5222/7222

Sources: `FILM-KODAK-003`, `FILM-KODAK-004`.

Kodak documents DOUBLE-X as a black-and-white negative stock with a broad useful tonal scale and long production history.

A Kodak production article for *Malcolm & Marie* includes cinematographer testimony describing DOUBLE-X as having a more assertive contrast/grain character than the color 500T path used in other contexts.

Classification:

- stock identity/spec role: `CONFIRMED`;
- comparative aesthetic testimony: `CORROBORATED`.

### Safe generative translation

- true monochrome tonal design, not simply desaturating a color image;
- intentional B&W contrast structure;
- visible organic grain appropriate to exposure/print intent;
- protect facial tonal modeling and specular separation;
- avoid fake monochrome HDR where every surface remains equally readable.

## KODAK EKTACHROME 100D 5294/7294

Source: `FILM-KODAK-005`.

Kodak technical information supports:

- daylight balance around 5500K;
- color reversal film rather than negative;
- moderately enhanced saturation;
- neutral gray reproduction;
- accurate/natural flesh-tone intent;
- high sharpness and fine grain for its format/use.

### Safe generative translation

- more direct, crisp color separation than a muted negative-stock look;
- clean daylight rendering;
- moderately increased saturation without neon clipping;
- fine-grain/high-definition appearance;
- reversal-like density/contrast should remain controlled rather than exaggerated into posterized color.

## Kodak Portra 400 / Portra Family

Source: `FILM-KODAK-007`, historical Kodak professional-film brochure.

Documented stable family traits include:

- fine grain for its speed;
- emphasis on natural/pleasing skin reproduction;
- broad utility across varied lighting;
- moderate/controlled color intended for portrait/general professional use.

### Safe generative translation

Portra-style language can be useful for portrait/editorial stills, but it should not be treated as motion-picture VISION3 behavior.

Avoid collapsing photo negative stocks and cinema negative stocks into one `film look` category.

## Kodak Ektar 100

Source: `FILM-KODAK-007`.

Kodak's documented positioning emphasizes:

- vivid color/saturation;
- high sharpness/fine grain;
- strong suitability for landscape/product/travel-type color when accurate yet vivid rendering is desired.

### Safe generative translation

Use stronger color separation/saturation when appropriate, but preserve material realism and prevent digital neon oversaturation.

## Kodak T-MAX Family

Source: `FILM-KODAK-007`.

Kodak documents T-MAX around fine grain and high sharpness/acutance within professional B&W film.

### Safe generative translation

If the user requests T-MAX-style B&W:

- prioritize fine grain and crisp tonal separation rather than coarse retro grain;
- design true monochrome luminance relationships;
- avoid adding color fringing or warm `film` tint unless separately requested.

## Other Film Presets Exposed by Magnific

Magnific's current ontology includes several stocks for which this Phase 1 pass does not yet have equally strong first-party current sources, including:

- CineStill 800T;
- Fujifilm Pro 400H;
- Fujifilm Superia 400;
- Fujifilm Velvia 50;
- Fujifilm Provia 100F;
- Ilford Delta 3200;
- Lomography 800;
- Agfa Vista 400;
- Polaroid 600.

These remain provider-supported tokens but should not receive detailed universal behavioral profiles until evidence is added.

The Magnific adapter may pass a supported literal preset when the user selects it. The universal brain must not fabricate authoritative stock physics from the preset name alone.

## Negative Film vs Reversal Film

Later runtime rules should distinguish:

### Negative stocks

Typically intended for a flexible post/print pipeline with more room to reshape contrast/color.

### Reversal stocks

Produce a positive transparency/image and historically have less forgiving exposure behavior and a more direct relationship between capture and final density/color.

The exact latitude/contrast varies by stock and process. Do not convert this conceptual distinction into unsupported numeric claims.

## Tungsten vs Daylight Balance

A stock's nominal balance describes the illumination under which it is designed to reproduce neutral color without corrective filtration.

It does **not** mean:

```text
Tungsten stock = orange image
Daylight stock = blue image
```

Color temperature of the actual light, filters, scan, white-balance intent and grade all influence the visible result.

Later prompts should use stock balance as part of a coherent lighting/color design, not as a color filter.

## Grain Is Not Uniform Noise

Film-grain simulation should eventually consider:

- format size;
- stock speed;
- exposure;
- scan/enlargement amount;
- luminance region;
- grain scale;
- grain strength;
- chroma/luma character depending on the intended simulation.

A simple overlay of equal noise across all tones often reads digitally artificial.

The skill should use grain sparingly and only when justified by the capture/look intent.

## Halation Is Separate from Film Stock

Real halation depends on film-layer/base behavior and bright light interaction. In generation systems it is often an aesthetic approximation.

Do not assume every film-stock reference requires visible red/orange halation.

Treat:

- stock response;
- grain;
- halation;
- bloom;
- lens flare

as related but separate controls.

## Highlight Roll-Off vs Local HDR

A filmic highlight impression is not achieved by making every bright area darker so texture is visible everywhere.

The better target is:

- gradual transition toward clipping;
- bright sources may still clip at their hottest core;
- surrounding highlight color and texture roll away naturally;
- avoid halos/local-tone-mapping boundaries;
- preserve believable exposure hierarchy.

This visual rule will later combine Kodak/ARRI evidence with physical plausibility checks.

## Stock Name vs Observable Recipe

Later stock entries should use:

```text
STOCK
name
medium: negative / reversal / B&W
balance
speed role

DOCUMENTED TRAITS
...

OBSERVABLE GENERATIVE TRAITS
highlight behavior
shadow behavior
grain
color/saturation
contrast/density

AVOID
unsupported stereotypes
```

## Phase 1 Film Knowledge Strength

Strong:

- VISION3 500T;
- VISION3 250D;
- DOUBLE-X;
- EKTACHROME 100D;
- stable Kodak Portra/Ektar/T-MAX family traits.

Moderate:

- practitioner-relative descriptions from individual productions.

Weak / unresolved:

- several Fuji/Ilford/CineStill/Lomography/Agfa/Polaroid presets currently present in Magnific;
- discontinued Fujifilm ETERNA motion-stock detail suitable for a high-confidence profile;
- exact provider behavior when a current image model sees any particular film-stock token.

## Requirements Carried Forward

Phase 4 should:

- distinguish physical film-stock evidence from provider token response;
- separate stock response, grain, halation, bloom and lens flare;
- distinguish daylight/tungsten balance from final color grade;
- avoid `film = warm + grain + faded` stereotypes;
- model highlight/shadow behavior and density explicitly;
- allow user stock names as locks even when detailed evidence is incomplete;
- fall back to observable visual description when a provider does not reliably understand the stock name.