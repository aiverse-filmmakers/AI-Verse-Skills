# Phase 1 Research - Color Science, Grading, and Tonal Design

Status: RESEARCH EVIDENCE

Primary classification: `CONFIRMED` for manufacturer/software color-pipeline concepts, `CORROBORATED` for practitioner grading methods, and `INFERRED` only where explicitly identified.

This file defines what the later skill should understand by `color`. Color is not a single LUT, saturation slider, or teal-orange preset.

## Governing Principle

A cinematic color system should distinguish at least:

- capture white balance / source color relationship;
- exposure and luminance distribution;
- contrast curve / tonal density;
- global saturation;
- hue-specific saturation;
- subject/background color separation;
- skin-tone handling;
- highlight hue and saturation behavior;
- shadow hue and density;
- material-local color;
- final display/look intent.

Named camera logs, film stocks and movie looks should not replace these decisions.

## Capture Color vs Finished Look

ARRI REVEAL, Canon Log, Sony log workflows and Blackmagic RAW/color science are acquisition/post-production systems. They are not final grades.

Hard rule for later runtime behavior:

- `ARRI`, `VENICE`, `Canon Log`, `BRAW`, etc. must not automatically produce a flat gray log image;
- a named capture system may inform highlight/color response, but the final grade still follows story and user intent;
- only generate an intentionally flat/log-looking image when the user explicitly asks for an ungraded/log frame.

## ARRI REVEAL / Scene-Referred Color

Source: `CAM-ARRI-002` / `COLOR-ARRI-001`.

ARRI documents a modern scene-referred color pipeline around ARRI Wide Gamut 4 and LogC4, with emphasis on improved reproduction of bright/saturated colors and consistent downstream display rendering.

### Generative lesson

Useful visible consequences include:

- bright colors retaining hue instead of collapsing immediately to white;
- smoother transitions through highlights;
- natural skin separation;
- a gradeable, non-baked response before the final creative look.

Do not claim an AI-generated image is literally encoded in LogC4 unless it actually is.

## Resolve as a Useful Color Taxonomy

Sources: `COLOR-BMD-001`, `COLOR-BMD-002` and the current DaVinci Resolve Colorist Guide.

Resolve separates operations such as:

- lift / gamma / gain;
- log or HDR tonal zones;
- global offset;
- temperature and tint;
- contrast and pivot;
- saturation;
- hue-vs-hue;
- hue-vs-saturation;
- hue-vs-luminance;
- selective isolation/qualifiers;
- scopes and color management.

The skill does not need to imitate Resolve UI, but this supports a structured color model rather than a single `grade` label.

## Skin Tone Is Not One Numeric Target

Current Blackmagic colorist training explicitly warns against one universal `correct` skin-tone standard because lighting, undertone, exposure and creative intent vary.

Later rules should therefore avoid:

- forcing all people onto one hue line;
- making all skin equally warm;
- removing natural undertone variation;
- neutralizing intentional colored lighting;
- beauty-smoothing texture until skin becomes plastic.

Instead evaluate:

- whether skin belongs to the scene's light;
- whether hue/saturation remain plausible for that individual under that illumination;
- whether highlight/shadow skin retains believable color variation;
- whether local corrections preserve natural texture.

## Skin Texture and Color Are Coupled

Blackmagic training warns that excessive smoothing can make skin look plastic.

This matters directly to AI realism.

Later Reality Repair should not solve skin by only changing color or only adding pores. It should coordinate:

- microtexture;
- specular response;
- tonal transitions;
- local hue variation;
- shadow-side chroma;
- highlight saturation;
- subsurface-looking warmth where light supports it.

## White Balance Is Relational

White balance determines which illumination is treated as neutral and therefore how other sources separate.

Useful design questions:

- Is daylight neutral while tungsten practicals remain warm?
- Is a tungsten interior neutral while exterior daylight shifts cool?
- Is blue-hour ambient intentionally cool against warm practicals?
- Is mixed lighting part of the story or an error to neutralize?

A cinematic grade often preserves useful source separation instead of neutralizing every surface.

## Color Separation

Color separation means important elements remain distinguishable through hue, saturation and/or luminance relationships.

Examples:

- warm face against cooler ambient environment;
- neutral product against a saturated set;
- skin protected from green contamination in foliage-heavy scenes;
- dark wardrobe separated from dark background through hue/value/specular differences rather than artificial rim light.

Separation is a design tool, not a requirement for complementary-color cliches.

## Saturation Discipline

Cinematic saturation is contextual.

Possible valid strategies include:

- muted global palette with selective local color;
- restrained saturation with strong luminance contrast;
- rich saturated reversal-film-like color;
- vivid commercial/product color;
- nearly monochromatic low-saturation drama;
- true monochrome.

The skill should not equate `cinematic` with low saturation, teal/orange, or faded blacks.

## Tonal Density

`Density` is useful shorthand for how substantial or thin the image feels through black level, midtone placement, color concentration and highlight distribution.

A dense image can have:

- substantial blacks;
- rich midtones;
- controlled highlights;
- saturated-but-not-neon color.

But density must not become crushed shadows or indiscriminate underexposure.

## Highlight Color Behavior

A realistic highlight system should distinguish:

- diffuse bright surfaces;
- specular reflections;
- emissive sources;
- clipped source cores;
- surrounding rolloff.

Common synthetic failure:

- every highlight becomes desaturated pure white with a hard digital boundary;
- or HDR processing forces texture into every hot source and destroys exposure hierarchy.

Later rules should allow a lamp, sun reflection or practical bulb to clip naturally while preserving plausible transition and nearby color.

## Shadow Color Behavior

Shadows are rarely `black paint`.

Depending on scene lighting they may contain:

- skylight blue/cyan;
- warm bounce;
- colored practical contamination;
- neutral low-saturation values;
- film/sensor noise/grain;
- retained material color.

The skill should not add colored shadows decoratively. Shadow hue must follow ambient/bounce/light logic.

## Black Level

Three common failure modes:

### Lifted digital gray

Everything in shadow remains visible, making the frame feel HDR/computational.

### Crushed artificial black

Large regions lose all structure regardless of actual exposure/material.

### Corrective target

Use deliberate black density with selective retained information. Some areas may legitimately disappear while important forms remain readable.

## Local Contrast vs Oversharpening

Cinematic clarity often comes from lighting, tonal separation, texture and controlled local contrast, not aggressive edge sharpening.

Over-sharpened skin, hair and fabric are common AI tells.

Later color/detail rules should separate:

- global contrast;
- local/midtone contrast;
- optical sharpness;
- digital edge enhancement;
- texture detail.

## Look Creation vs Technical Correction

Later architecture should distinguish:

### Technical normalization

- exposure balance;
- white balance;
- obvious color cast correction when unintended;
- display transform / usable tonal mapping.

### Creative look

- palette;
- contrast personality;
- density;
- saturation strategy;
- highlight/shadow color relationship;
- stock/camera-inspired response;
- era/genre choices.

This distinction helps prevent accidental `look stacking`.

## Scope / Display Independence

The skill cannot know the user's exact calibrated display unless the host provides that information.

Therefore universal outputs should describe relative visual intent rather than rely on a specific monitor transform.

Examples:

- `deep but not crushed blacks`;
- `soft highlight shoulder`;
- `restrained cyan ambient against warm practicals`;
- `natural skin saturation`.

Avoid pretending the skill can guarantee exact display-referred values across every host.

## Named Movie Looks

Magnific exposes named-film and filmmaker look presets. Those are provider convenience controls.

The universal skill should primarily decompose look into observable attributes:

- palette;
- contrast;
- exposure;
- density;
- light color;
- production design;
- texture;
- optics.

If the user names a film/director, the skill may analyze/request high-level characteristics subject to style/copyright rules, but named looks must not replace physical image reasoning.

## Reality Repair Color Diagnostics

Future Reality Repair should check for:

- over-saturation;
- uniform skin hue;
- fake cyan/magenta split lighting;
- HDR/local-tone-mapping halos;
- lifted gray blacks;
- dead/crushed shadows;
- hard clipped highlights;
- inconsistent source color;
- material color not responding to light;
- reflections with impossible color sources;
- excessive digital sharpening/microcontrast;
- LUT-like grade overpowering scene logic.

## Phase 1 Color Knowledge Strength

Strong:

- capture-log vs final-look distinction;
- white balance as a relational decision;
- separation of luminance/hue/saturation operations;
- no universal skin-tone target;
- skin smoothing restraint;
- scopes/objective measurement as a production principle;
- highlight/shadow hierarchy;
- technical normalization vs creative look.

Moderate:

- qualitative `density` vocabulary, which is useful but not a standardized numerical measurement.

Weak / unresolved:

- exact model-by-model response to advanced colorist language;
- exact transfer of LUT/ACES/film-print-transform names into current image generators;
- display-calibrated color guarantees in generic LLM/image-tool environments.

## Requirements Carried Forward

Phase 4 should:

- model white balance, palette, color separation, saturation, density and highlight/shadow chroma separately;
- avoid one-size-fits-all skin hue;
- prevent over-smoothing/over-sharpening from being mistaken for beauty/quality;
- keep technical capture transforms distinct from finished creative grade;
- make color follow lighting/material physics;
- include HDR halos, lifted blacks, crushed shadows and generic teal-orange treatment in the Reality Gate.