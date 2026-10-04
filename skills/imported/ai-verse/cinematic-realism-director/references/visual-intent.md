# Visual Intent and Story-to-Shot Reasoning

Status: RUNTIME KNOWLEDGE

Purpose: convert narrative, commercial, editorial, documentary, portrait, product, travel, automotive, food, architecture, mobile, and other photographic intent into professional visual priorities before camera/provider decisions are made.

Use with `references/professional-quality-floor.md`.

## Core Rule

> Story chooses cinematography. The Professional Quality Floor determines how expertly that story is executed.

Do not begin with prestige equipment names or a fixed effect bundle. Also do not interpret restraint as permission to deliver merely ordinary photography.

AUTO must answer two questions first:

1. What kind of image is the user actually asking for?
2. What would an elite professional in that exact photographic/cinematic specialty do with it?

## Intent Extraction Order

Reason in this order:

1. What must the viewer understand?
2. What should the viewer feel?
3. What photographic/cinematic medium is requested or implied?
4. Which professional specialty best matches it?
5. What must remain visually dominant?
6. What context must remain readable?
7. What must remain physically believable?
8. What visual information can be simplified?
9. What shot, light, color, texture, and finish choices best support those answers?

## Minimum Intent Model

Track at least:

```text
purpose
subject
story_action
requested_or_implied_medium
professional_specialty
emotional_target
visual_priority
context_priority
realism_target
viewer_relationship
energy
clarity_requirement
preservation_constraints
```

## Beginner AUTO

One sentence is enough.

Example:

```text
woman waiting for a taxi in London at night
```

Do not ask the user to choose camera, lens, aperture, stock, lighting, color grade, grain, or provider when safe professional choices can be inferred.

Infer:

```text
purpose: narrative/editorial
medium: cinematic photographic still
professional_specialty: feature-film cinematography
story_action: waiting / watching traffic
viewer_relationship: observational but emotionally near
visual_priority: face + waiting posture
context_priority: London street remains legible
realism_target: cinematic photographic
finish: premium tonal response + subtle organic filmic texture
```

The user does not need to say `Hollywood`, `ARRI`, or `cinematic` to unlock this standard.

## Medium Preservation

Professionalization must respect the requested medium.

### Mobile / selfie

If the user asks for an iPhone/mobile/selfie image, do not convert it into generic cinema-camera capture.

Preserve:

- phone-like proximity/perspective;
- casual/social plausibility;
- appropriate depth behavior;
- believable phone processing.

Elevate through elite framing, timing, exposure, skin, color, local contrast, highlight control, and finishing.

### Candid / documentary / street

Prioritize believable access, non-performative gesture, decisive timing, context, layering, available/motivated light, and top editorial/documentary finishing.

The image may feel discovered rather than staged while still being exceptionally composed.

### Narrative / cinematic

Prioritize story beat, viewer relationship, production context, motivated light, premium tonal response, professional color separation, intentional depth, and polished movie-grade finishing.

### Commercial / product / fashion / automotive / food / architecture / travel

Use the professional specialty rules in `professional-quality-floor.md` instead of forcing one generic cinema aesthetic onto every field.

## Viewer Relationship

Choose the viewer relationship before composition.

### Intimate
Closer physical/emotional relationship; face/gesture can dominate; environment may remain secondary but readable when important.

### Observational
Viewer witnesses without direct address; environmental layering and non-performative behavior may improve authenticity.

### Participatory
Viewer feels inside the action; POV/OTS/foreground body or prop presence may be appropriate.

### Detached
Environment/system/scale dominates; subject can be smaller; geometry and negative space may carry meaning.

### Iconic / heroic
Subject/product is dominant and aspirational; silhouette/separation/composition become disciplined. Do not automatically add extreme low angle, rim light, or distortion.

## Information Hierarchy

Every professional shot needs an explicit hierarchy.

Internally answer:

```text
what should the eye see first?
what second?
what context must stay readable?
what can fall away?
```

Possible priorities include face, eyes, gesture, hands, product, vehicle, environment, architecture, food texture, costume, prop, light source, text/signage, or atmospheric scale.

Professional composition does not always mean isolating one subject with blur.

## Emotional Target to Visual Strategy

Translate emotion into observable choices rather than adjectives alone.

### Vulnerability
May favor environmental exposure, negative space, observational distance, restrained dominance, and natural contrast.

### Intimacy
May favor closer spatial relationship, gentle perspective, clear expression priority, motivated soft light, and quieter background hierarchy.

### Tension
May favor withheld information, asymmetry, selective darkness, layered foreground/background, or tighter spatial relationships. Do not automatically use Dutch angle.

### Isolation
May favor smaller subject scale, negative space, environmental dominance, or physical separation.

### Energy
May favor diagonals, closer camera relationship, near/far layering, decisive motion evidence, or less static balance. Do not automatically add motion blur.

### Calm
May favor stable geometry, simple hierarchy, controlled negative space, restrained competition, and smooth tonal transitions.

### Luxury
Favor disciplined composition, controlled surfaces/reflections, rich tonal density, precise highlights, purposeful materials, and brand-appropriate polish—not automatic black/gold, smoke, or rim light.

### Documentary honesty
Favor plausible camera access, truthful environmental context, available/motivated light, natural imperfection, and restrained staging.

## Purpose-Specific Direction

### Narrative
Prioritize the current story beat, emotional information, context, and what should remain unresolved. Do not make every frame a poster.

### Commercial
Balance brand/product clarity, aspirational context, physical material realism, and human emotion. Apply top-tier campaign polish without flattening the world into catalog light.

### Editorial / Fashion
Prioritize silhouette, styling, garment physics, attitude, environment, and image identity. Bold formal choices are allowed when conceptually justified.

### Documentary / Candid
Prioritize believable access, moment, gesture, context, available-light logic, and truthful imperfection. The professional quality comes from timing/judgment/finishing, not artificial staging.

### Portrait
Prioritize identity, expression, gaze, posture, skin, dimensionality, and background relationship. Do not assume 85mm + f/1.4.

### Product
Prioritize exact geometry, logo/text where required, materials, surfaces, scale, contact, controlled reflections, and appropriate specialist lighting.

### Automotive
Prioritize vehicle proportions, wheel geometry, paint/surface response, road contact, reflections, location, and motion state.

### Food
Prioritize edible cues, moisture/crust/translucency, physically justified steam/condensation, plate geometry, action, and tactile realism.

### Architecture / Interiors
Prioritize spatial clarity, vertical/horizon logic, material scale, human scale, source balance, and believable camera position.

### Travel / Hospitality
Balance destination identity, human experience, atmosphere, environment scale, material appeal, and aspirational polish.

### Mobile / Social
Preserve the capture language of a phone/selfie/social image while applying elite mobile-photography composition, light, exposure, color, and editing.

## Realism Target

### strict_photographic
Physically conservative capture logic; minimal stylization; still professionally executed.

### cinematic_photographic
Feature-film-level choices while remaining plausible as a photographed frame. Default general photographic AUTO target when no stronger specialty/medium signal exists.

### heightened_but_plausible
Stronger contrast/palette/atmosphere/lens/production design while maintaining physical coherence.

### stylized_photographic
Overt art direction allowed while retaining photographic capture logic where possible.

### user_defined
Follow the user's explicit target.

## Default Professional Finish

For normal photography, AUTO should usually resolve unspecified finishing toward:

```text
intentional composition
professional exposure hierarchy
controlled highlight rolloff
natural shadow density
clean color separation
credible skin/material response
realistic optical/focus transition
subtle organic texture
high-end restrained grading
```

For cinematic/narrative work, premium digital-cinema tonal behavior and ARRI-like highlight rolloff/skin response may be used as observable targets without claiming literal ARRI capture.

## Texture Default

Subtle organic filmic texture is normally part of professional photographic finishing unless:

- the user says no grain/pristine/clinical/noise-free;
- the medium clearly requires sterile technical cleanliness;
- texture would damage critical product/material readability.

Strong grain, halation, bloom, scratches, dust, heavy flare, and other visible film artifacts still require stronger justification.

## Anti-Cliche Guard

These are **not** automatic consequences of professional/cinematic quality:

- maximum background blur;
- anamorphic lens;
- horizontal blue flare;
- teal/orange grade;
- haze;
- dramatic rim light;
- Dutch angle;
- underexposure;
- orange practicals + blue moonlight;
- strong halation;
- lifted blacks;
- heavy vignette;
- exaggerated film damage.

Important distinction:

```text
professional finish != cinematic cliché stack
subtle organic texture != heavy film-effect preset
premium tonal response != prestige camera-name spam
```

## Context Preservation

Before choosing tight framing or shallow depth, decide whether context carries identity, social relationship, scale, product use, architecture, weather, time, culture, location, or danger.

Do not erase useful story information merely to increase subject separation.

## Ambiguity Policy

Ask only when:

- two interpretations materially change content rather than just professional shot choices;
- hard locks directly conflict and cannot be reconciled;
- a missing reference/asset is essential to preservation;
- the user explicitly wants to choose among directions.

Otherwise choose the strongest professional AUTO solution.

## Reality Gate Questions for Intent

Before accepting the design:

- does the frame communicate the literal request?
- is the professional specialty appropriate to the requested medium?
- did AUTO elevate the image without erasing its medium?
- is viewer relationship coherent?
- is important context preserved?
- are light/color/depth choices motivated?
- is the finish premium rather than merely ordinary?
- did any cliché get added without reason?
- did the quality floor override any user lock? If yes, fix it.

A shot that is merely competent because the user gave a simple prompt fails the intent layer.
