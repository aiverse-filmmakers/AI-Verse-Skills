# Cameras and Capture Formats

Status: RUNTIME KNOWLEDGE
Task: 3.3

This reference translates capture-system intent into observable image behavior without treating camera names, sensor formats, film gauges, or acquisition pipelines as magical style presets.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`

Use source evidence from:

- `references/research/cameras.md`
- `references/research/film-stocks.md`
- `references/source-ledger.md`

## 1. Core Principle

A camera body does not create the final look by itself.

The visible result depends on a chain including:

```text
capture medium
capture format
camera position
lens
focal length
aperture
focus distance
exposure
lighting
white balance
sensor/emulsion response
filtration
color transform
grade
texture / grain / sharpening
```

Therefore:

> Named camera references are constraints or priors. They are not complete visual recipes.

## 2. Separate the Axes

Do not collapse all capture choices into a single `camera` label.

Reason through:

```text
capture_medium
capture_format
camera_reference
camera_character
sensor_or_emulsion_behavior
```

### capture_medium

Examples:

```text
digital cinema
negative film
reversal film
analog video
consumer digital
low-fi digital
```

### capture_format

Examples:

```text
Super 35
full frame / large format
VistaVision-class
65mm / 70mm reference
16mm
8mm
medium format stills
1-inch / smaller video formats where relevant
```

### camera_reference

Optional named acquisition system supplied by the user or selected deliberately.

Examples:

```text
ARRI ALEXA 35
Sony VENICE 2
RED V-RAPTOR
Canon C500 Mark II
Blackmagic URSA Mini Pro
```

### camera_character

Observable finished-image intent such as:

```text
controlled highlight rolloff
clean large-format digital capture
open shadows with retained density
restrained digital sharpness
natural skin separation
high-resolution contemporary response
low-light clean capture
```

Do not confuse `camera_character` with a guaranteed measured simulation.

## 3. AUTO Selection Rule

When the user does not name a camera, do not choose a branded camera merely to make the prompt sound professional.

Prefer a provider-neutral character description first.

Example:

```text
capture_format: Super 35
camera_reference: null
camera_character: modern cinema capture with controlled highlights, natural skin, restrained digital sharpness
```

A named camera should be selected in AUTO only when:

- the provider exposes a meaningful native control for it;
- the user asks for a recognizable camera family;
- the chosen reference materially improves translation to the provider;
- a benchmark later proves the name improves consistency.

Otherwise observable behavior is safer and more portable.

## 4. User Camera Locks

If the user specifies a camera, preserve it as a lock.

Example:

```text
ARRI Alexa 35, 35mm, f/2.8
```

Record:

```text
camera_reference = ARRI ALEXA 35 [LOCKED]
focal_length = 35mm [LOCKED]
aperture = f/2.8 [LOCKED]
```

Then infer only missing behavior.

Do not silently replace the camera because another model supports a different named preset.

If the provider cannot represent the exact camera, translate the documented observable intent semantically and record the limitation in `provider_adaptation`.

## 5. Camera Reference vs Camera Fact

When generating an AI image, a camera name means:

> render toward visual traits associated with that reference

It does not mean:

> this output was actually captured by that camera

Never claim generated images literally possess:

- a measured stop count;
- a specific raw codec;
- a real sensor readout mode;
- actual LogC4/S-Log3/C-Log data;
- real photosite behavior;
- true manufacturer color science.

Translate those systems into visible consequences only where justified.

## 6. Dynamic Range Translation

Do not use numeric manufacturer stop claims as prompt decoration.

Translate broad dynamic-range intent into visible behavior:

```text
bright practicals/windows retain color and shape
highlight transition is gradual rather than abruptly white-clipped
shadow detail survives without lifting blacks into gray HDR
bright and dark regions belong to one coherent exposure
no local-tone-mapping halo around high-contrast edges
```

If the story calls for clipping, crushed blacks, harsh video response, or low latitude, do not force broad-latitude behavior.

## 7. Color Science Translation

Acquisition log and gamut are not final looks.

Do not interpret:

```text
LogC4
S-Log3
Canon Log 2
Blackmagic Film
```

as instructions to return a flat gray ungraded image unless the user explicitly requests an ungraded/log frame.

Default output should be a finished image whose tonal/color behavior is compatible with the capture intent and the story-appropriate grade.

## 8. Capture Format and Field of View

Format affects field-of-view relationships with focal length.

The skill must reason jointly about:

```text
format
camera distance
focal length
framing
```

Do not assume a focal length means the same framing across all formats.

Example:

```text
50mm on Super 35
!=
50mm on full frame
```

for the same camera position and output framing.

Perspective itself still comes primarily from camera position relative to the scene.

## 9. Format Does Not Automatically Mean Shallow Depth

Larger formats can produce shallower depth relationships when framing, aperture, distance, and focal choices change accordingly, but `large format` must not automatically become:

```text
f/1.2 + razor-thin focus
```

Depth is handled explicitly in Task 3.6.

## 10. ARRI ALEXA 35

Source basis: `references/research/cameras.md`.

Safe visual translation when explicitly selected:

- controlled highlight rolloff;
- highlight color retained around bright sources when exposure permits;
- natural skin color separation;
- open but information-rich shadows;
- cinematic digital image without brittle oversharpening;
- flexible finished grade rather than a fixed baked palette.

Avoid:

- automatically making the image warm;
- automatically adding film grain;
- stating the image has 17 stops;
- outputting a flat log image by default;
- treating Alexa as a lens look.

## 11. Sony VENICE 2

Safe visual translation:

- polished high-end large-format digital capture;
- strong low-light cleanliness when required;
- broad highlight/shadow retention;
- natural color designed for grading;
- controlled contemporary detail.

Avoid:

- generic `Sony video look` stereotypes;
- blue/cool grading simply because Sony is named;
- literal dual-base-ISO claims in generated pixels.

## 12. RED V-RAPTOR / V-RAPTOR [X]

Safe visual translation:

- VistaVision-class / large-format field-of-view behavior when that format is part of the request;
- high-resolution contemporary digital capture;
- strong detail while avoiding artificial oversharpening;
- broad tonal range if the scene calls for it.

Global shutter on V-RAPTOR [X] is primarily relevant to motion geometry. Do not invent a visible global-shutter signature in a static frame.

Avoid turning `RED` into exaggerated crispness, saturation, or contrast without a story reason.

## 13. Canon C500 Mark II

Safe visual translation:

- modern cinema capture;
- broad tonal retention;
- natural, gradeable color;
- restrained finished contrast until the intended grade is applied.

Avoid unsupported stereotypes such as universally warm skin.

## 14. Blackmagic URSA Mini Pro

If exact model is unspecified:

- treat it as a professional digital cinema capture reference;
- do not invent exact sensor dimensions, resolution, or dynamic-range number;
- keep color/tonal response flexible and grade-dependent.

Avoid treating Blackmagic Film/BRAW as a final aesthetic preset.

## 15. 35mm Motion-Picture Film

`35mm film` is not a single look.

Separate:

```text
format / gauge
stock
exposure
processing
scan
print/display transform
grade
```

If the user only says `35mm film`, infer a restrained generic photochemical response rather than inventing a particular stock.

Possible generic translation:

- organic grain appropriate to image scale;
- smoother high-frequency detail than aggressively sharpened digital imagery;
- natural tonal density;
- highlight response informed by negative-film behavior when a negative-film assumption is reasonable;
- slight frame-to-frame/process imperfections are irrelevant to a single still unless intentionally simulated.

Do not automatically add heavy grain, orange halation, faded blacks, dust, scratches, or vintage color casts.

## 16. 16mm

Potential visible tendencies when intentionally requested:

- smaller image area relative to 35mm;
- more apparent grain for comparable enlargement/output;
- lower-resolution/rougher texture depending on stock/process;
- documentary, period, music-video, or intimate associations may influence creative choice but are not physical laws.

Do not make every 16mm image dirty, green, underexposed, or handheld.

## 17. 8mm

Use only when the aesthetic is intentionally low-resolution/consumer/archival/nostalgic or otherwise story-appropriate.

Possible traits:

- much coarser apparent grain;
- lower detail;
- stronger format texture;
- less controlled exposure/color depending on the intended historical/consumer process.

Do not inject 8mm artifacts into normal cinematic work simply for authenticity.

## 18. 65mm / 70mm Reference

Treat cautiously because detailed IMAX/proprietary translation remains research debt.

Safe general behavior:

- very large capture area relative to 35mm cinema;
- potential for exceptional spatial/detail presentation;
- focal/field-of-view relationships appropriate to the larger format;
- can support immersive scale, large environments, or intimate large-format faces.

Do not automatically apply:

- shallow DOF;
- extreme clarity;
- cool color;
- IMAX-specific contrast;
- zero grain;
- epic lighting.

A large format can photograph mundane, intimate, soft, dark, or restrained scenes too.

## 19. Medium Format Still Photography

When intentionally used as a visual reference:

- treat it as a large still-photo capture format;
- reason about field of view and depth in relation to framing and distance;
- preserve high-quality tonal/detail rendering when appropriate;
- do not automatically turn it into luxury advertising.

## 20. Analog Video / VHS

VHS and analog-video character belongs to a different capture-medium axis from cinema film.

Possible visible traits:

- lower effective detail;
- chroma softness/bleed;
- video noise;
- scan/field/interlace artifacts where intentionally reproduced;
- limited highlight response;
- tape-generation artifacts if the brief implies recorded/copied media.

If the user combines a large-format capture reference with VHS, use `references/parameter-conflicts.md` to determine whether they want:

```text
large-format scene characteristics followed by VHS recording/output artifacts
```

rather than treating them as physically impossible by default.

## 21. Low-Fi Digital / Pixelvision-Type References

When a provider exposes a named low-fi camera/preset, separate:

- low spatial resolution;
- sensor noise;
- limited dynamic response;
- unusual color/contrast;
- compression or signal artifacts;

from unrelated vintage-film traits.

Do not add film grain when the intended medium is low-fi digital unless the user requests a hybrid treatment.

## 22. Camera Selection by Purpose

AUTO should select a **capture behavior**, not chase brands.

### Narrative drama

Often benefits from:

- controlled highlight response;
- natural skin;
- intentional shadow density;
- restrained detail;
- flexible grading.

### Documentary

Often benefits from:

- believable available-light response;
- context retention;
- natural detail;
- less processed finish.

### Commercial / beauty

May benefit from:

- high material/skin readability;
- clean highlights;
- controlled surface response;
- precise color separation.

### Product

Prioritize geometry/material truth over camera mystique.

### Travel / architecture

Prioritize environmental scale, detail, tonal range, and believable perspective.

### Low-fi / period / archival

Select format/media artifacts intentionally from story need.

## 23. Camera Character Strength

Do not over-amplify a named camera's identity.

Recommended internal principle:

```text
camera reference = subtle capture prior
lens + lighting + exposure + grade = major visible determinants
```

If a provider requires stronger semantic cues to make the difference visible, amplification may be adapter-specific and should be benchmarked later, not hard-coded universally.

This follows the broader lesson from the Higgsfield research: model-visible lens/camera character may require deliberate amplification, but amplification must remain controlled and evidence-driven.

## 24. Camera vs Lens Responsibility

Camera/capture system primarily influences intended behavior around:

- capture format;
- tonal latitude intent;
- color handling intent;
- noise/texture basis;
- detail/sharpening character;
- sensor/emulsion response.

Lens primarily influences:

- field of view with format;
- optical contrast/microcontrast;
- flare;
- bokeh;
- edge behavior;
- aberrations;
- distortion;
- focus falloff.

Do not assign lens traits to the camera body.

## 25. Camera vs Grade Responsibility

Do not bake grade clichés into camera references.

Examples:

```text
ARRI != warm beige grade
Sony != cool cyan grade
RED != saturated sharp grade
Canon != orange skin
film != faded warm grade
```

Grade is handled in Phase 4.

## 26. Camera vs Texture Responsibility

Do not assume:

```text
cinema camera = grain
film = heavy grain
large format = no grain
old camera = dust/scratches
```

Texture choices are controlled separately according to medium, stock/process, exposure, provider behavior, and story.

## 27. Capture Format Selection Rules

AUTO may use these broad heuristics, subject to later focal/depth rules:

### Super 35

Useful default for traditional cinema spatial relationships, flexible lensing, narrative work, documentary, and broad compatibility.

### Full frame / large format

Useful when broader field of view at a given focal length, large-format spatial feel, low-light strategy, or contemporary premium capture intent supports the scene.

### 35mm film

Use when photochemical response materially supports the brief.

### 16mm

Use when smaller-format texture/energy is justified.

### 65mm / 70mm reference

Use for intentionally large-format spatial presentation, not automatically for spectacle.

### Analog/low-fi

Use only for explicit medium/story intent.

## 28. Provider Translation

If a provider exposes native camera controls:

1. preserve explicit user locks;
2. map exact supported values when available;
3. translate unsupported named cameras semantically;
4. never invent provider control values;
5. keep provider-specific mappings inside adapter files.

The universal reference should not depend on any provider enum.

## 29. Reference Matching Rule

When analyzing a reference frame, do not infer exact camera hardware as fact.

You may infer observable characteristics such as:

```text
large-format-like field of view relationship
clean modern digital response
gentle highlight transition
low-fi analog-video texture
small-format film-like grain scale
```

Exact camera names belong only in hypotheses unless supplied by metadata/user/source.

Use `schemas/reference-dna.schema.json`.

## 30. Validation Checklist

Before accepting capture choices, check:

- is the capture medium appropriate to the story?
- is the format compatible with the intended framing/focal strategy?
- is perspective being attributed correctly to camera position?
- is the named camera user-supplied, deliberately chosen, or unnecessary branding?
- were manufacturer marketing phrases translated into observable traits?
- were log/gamut concepts kept separate from final grade?
- was dynamic range translated into plausible tonal behavior rather than numeric prompt spam?
- were camera traits kept separate from lens traits?
- were camera traits kept separate from grade and texture?
- were explicit camera locks preserved?
- did the provider adapter avoid fabricating unsupported controls?

## 31. Output to Shot Spec

Populate primarily:

```text
capture.capture_format
capture.camera_reference
capture.camera_character
capture.sensor_or_emulsion_behavior
texture_and_finish.film_stock_or_tonal_reference
texture_and_finish.tonal_response
parameter_states[]
provider_adaptation
provenance
```

Later Tasks 3.4, 3.5, and 3.6 fill lens, focal/perspective, aperture/focus/depth independently.

## 32. Requirements Carried Forward

Task 3.4 must not let lens-family stereotypes overwrite capture-system intent.

Task 3.5 must model camera distance and focal length together with format.

Task 3.6 must not infer depth of field directly from format size.

Phase 4 must keep exposure, film-stock response, color science, grade, grain, halation, bloom, and flare as separate controllable systems.