# Visual Intent and Story-to-Shot Reasoning

Status: RUNTIME KNOWLEDGE
Task: 3.1

This reference converts narrative, commercial, editorial, documentary, portrait, product, travel, automotive, food, architecture, fashion, storyboard, and reference-study intent into visual priorities before camera or lighting choices are made.

The core rule is simple:

> Story chooses cinematography. Cinematography does not decorate story.

A cinematic result is not created by stacking camera names, shallow depth of field, grain, flare, haze, teal/orange grading, or dramatic rim light. The shot should first communicate the intended information and feeling. Capture, optics, lighting, color, texture, and realism choices follow from that purpose.

## 1. Intent Extraction Order

When receiving a request, reason in this order:

1. **What must the viewer understand?**
2. **What should the viewer feel?**
3. **What must remain visually dominant?**
4. **What must remain believable?**
5. **What contextual information must survive?**
6. **What visual information can be simplified or suppressed?**
7. **What cinematography choices support those answers?**

Do not start by choosing a camera or lens.

## 2. Minimum Intent Model

Represent the shot internally through at least:

```text
purpose
subject
story_action
emotional_target
visual_priority
context_priority
realism_target
viewer_relationship
energy
clarity_requirement
preservation_constraints
```

Map these into `cinematic-shot-spec.schema.json` rather than inventing a separate incompatible structure.

## 3. Beginner AUTO Rule

A beginner may give only one sentence.

Example:

```text
woman waiting for a taxi in London at night
```

Do not ask for camera, lens, aperture, film stock, lighting, grade, or framing unless the task genuinely cannot proceed without them.

Infer a coherent visual strategy from the story:

```text
purpose: narrative/editorial
subject: woman waiting for taxi
story_action: waiting, watching traffic
emotional_target: anticipation, isolation, urban night
context_priority: London street must remain legible
viewer_relationship: observational, close enough to feel present but not intrusive
energy: restrained
clarity_requirement: face readable, environment recognizable
```

Only after this should the skill design camera, composition, lens, lighting, and tone.

## 4. Expert Lock Rule

If the user specifies camera, focal length, aperture, framing, angle, format, stock, lighting, or another technical parameter, treat it according to `references/locks.md`.

Intent reasoning fills missing fields around the locks.

Example:

```text
User:
woman waiting for a taxi in London at night, Alexa 35, 35mm, low angle

Locked:
camera_reference = ARRI ALEXA 35
focal_length = 35mm
camera_angle = low

AUTO:
camera_distance
shot_size
aperture
focus strategy
lighting
exposure
color
grain
texture
```

Do not change the user's locked 35mm to an 85mm merely because a portrait heuristic prefers compression.

## 5. Viewer Relationship

Before composition, determine how the viewer should relate to the subject.

Useful relationship classes:

### Intimate

The viewer should feel physically or emotionally close.

Possible consequences:

- closer camera position;
- face or gesture carries more frame weight;
- environment becomes secondary but does not automatically disappear;
- eye line and micro-expression matter more;
- shallow depth may help, but is not mandatory.

### Observational

The viewer witnesses without feeling directly addressed.

Possible consequences:

- camera may sit outside immediate personal space;
- foreground occlusion or environmental layering may feel natural;
- subject need not face camera;
- composition can preserve more contextual information.

### Participatory

The viewer should feel inside the action or physically present.

Possible consequences:

- POV or over-the-shoulder framing;
- stronger near/far scale relationships;
- foreground body/prop presence;
- less pristine composition may improve realism.

### Detached

The viewer should read systems, scale, isolation, architecture, or environment more than facial emotion.

Possible consequences:

- wider spatial context;
- smaller subject scale;
- stronger geometry or negative space;
- less aggressive subject separation.

### Iconic / Heroic

The subject should feel visually dominant, aspirational, powerful, monumental, or product-hero oriented.

Possible consequences:

- controlled low angle if justified;
- simplified background hierarchy;
- clear silhouette;
- deliberate separation from environment;
- cleaner light and material control.

Do not equate heroic with extreme low angle, wide lens distortion, or rim light by default.

## 6. Information Hierarchy

Every shot should have an explicit visual hierarchy.

Ask internally:

```text
What should the eye see first?
What should it see second?
What context must remain readable?
What can fall away?
```

Priority can be distributed across:

- face;
- eyes;
- gesture;
- hands;
- product;
- vehicle;
- environment;
- architectural geometry;
- food surface/texture;
- costume;
- prop;
- light source;
- text/signage;
- atmospheric scale.

A cinematic shot is not necessarily one with one isolated subject. Sometimes the story depends on multiple readable layers.

## 7. Emotional Target to Visual Strategy

Emotion should influence cinematography through observable decisions, not adjectives alone.

### Vulnerability

Possible strategies:

- more environmental exposure around the subject;
- slight negative space;
- observational camera position;
- restrained contrast;
- reduced visual dominance;
- subject placement that feels less protected.

### Intimacy

Possible strategies:

- closer spatial relationship;
- gentle perspective;
- clear eye/face priority;
- soft but motivated light;
- quieter background hierarchy.

### Tension

Possible strategies:

- withheld visual information;
- asymmetric balance;
- stronger foreground/background separation;
- selective darkness;
- tighter spatial relationships;
- off-axis camera placement when justified.

Do not automatically use dutch angle.

### Isolation

Possible strategies:

- subject smaller relative to frame;
- negative space;
- environment allowed to dominate;
- physical distance from other people/objects;
- reduced visual clutter around the subject.

### Energy

Possible strategies:

- active diagonals;
- closer camera relationship;
- stronger near/far layering;
- motion evidence if present;
- less static balance.

Do not automatically add motion blur.

### Calm

Possible strategies:

- stable geometry;
- simple hierarchy;
- controlled negative space;
- lower visual competition;
- restrained texture/effects.

### Luxury

Possible strategies:

- disciplined composition;
- controlled surfaces/reflections;
- precise visual hierarchy;
- tonal density;
- clean highlight behavior;
- intentional texture rather than maximal gloss.

Luxury is not synonymous with black backgrounds, gold light, or shallow depth.

### Documentary honesty

Possible strategies:

- plausible camera access;
- available/motivated light;
- natural imperfection;
- truthful environmental context;
- restrained beautification;
- practical depth rather than artificial subject cutout.

## 8. Purpose-Specific Reasoning

### Narrative

Prioritize story beat and viewer relationship.

Ask:

- what just happened?
- what is happening now?
- what matters emotionally?
- what information should remain unresolved?

Do not make every narrative frame a poster.

### Commercial

Prioritize product/service clarity while preserving believable world-building.

Balance:

```text
brand clarity
product readability
aspirational context
material realism
human emotion
```

Commercial does not mean flat catalog lighting unless that is the brief.

### Editorial / Fashion

Prioritize silhouette, styling, attitude, environment, texture, and image identity.

Allow bolder formal choices when they support the concept, but maintain believable anatomy, fabric, light, and spatial logic.

### Documentary

Prioritize plausibility, context, available-light logic, truthful imperfection, and non-performative framing.

Avoid over-directed visual polish unless the brief explicitly asks for stylized documentary.

### Portrait

Prioritize face, expression, skin, gaze, posture, and background relationship.

Do not assume 85mm + f/1.4.

The environment may carry essential identity or story.

### Product

Prioritize exact product form, logo/text where required, materials, surface response, scale, and purposeful environment.

Do not sacrifice product geometry for lens spectacle.

### Automotive

Prioritize vehicle proportions, body surfaces, reflections, wheel geometry, road contact, environment, and speed/state.

Avoid wide-angle deformation that changes recognizable body proportions unless intentionally requested.

### Food

Prioritize edible material cues, moisture, crust, translucency, steam/condensation when justified, plate geometry, and tactile realism.

Do not over-sharpen every crumb.

### Architecture

Prioritize spatial clarity, vertical/horizon logic, materials, human scale, light direction, and believable camera position.

Do not use cinematic distortion as a substitute for architecture photography logic.

### Travel

Balance destination identity, human experience, atmosphere, and environmental scale.

Avoid generic postcard perfection when lived experience is part of the brief.

### Storyboard / Shot Design

Prioritize blocking, readable action, spatial continuity, camera intent, and reproducibility over final-beauty polish.

## 9. Context Preservation

Before choosing shallow depth or tight framing, determine whether context carries story information.

Context may include:

- location identity;
- social relationship;
- danger;
- scale;
- product use;
- architecture;
- weather;
- time of day;
- crowd density;
- cultural/environmental cues.

If context matters, preserve it through framing, focus strategy, camera distance, or layering.

Do not erase narrative information merely to increase subject separation.

## 10. Realism Target

Use the `intent.realism_target` field from the shot schema.

### strict_photographic

Favor physically conservative capture logic and minimal stylization.

### cinematic_photographic

Allow deliberate cinema choices while keeping the image plausible as a real photographed frame.

### heightened_but_plausible

Permit stronger contrast, palette, atmosphere, lens character, or production design while preserving coherent physical behavior.

### stylized_photographic

Allow more overt art direction while maintaining photographic capture logic where possible.

### user_defined

Follow the user's explicit target.

## 11. Visual Priority Before Technical Choice

Use this internal sequence:

```text
intent
-> viewer relationship
-> information hierarchy
-> context requirement
-> composition/blocking
-> camera position
-> capture format
-> lens/focal choice
-> aperture/focus
-> lighting
-> exposure
-> color/tone
-> texture
-> realism verification
```

Do not reverse the sequence by selecting a camera/lens first and forcing the story into it.

## 12. Anti-Cliche Guard

The following are never automatic consequences of the word `cinematic`:

- f/1.2;
- maximum background blur;
- anamorphic lens;
- horizontal blue flare;
- 2.39:1 crop;
- teal/orange grade;
- warm highlights/cool shadows;
- haze;
- rim light;
- grain;
- halation;
- bloom;
- dutch angle;
- underexposure;
- handheld imperfection;
- orange practicals;
- blue moonlight.

Every such choice requires a story, realism, location, or aesthetic reason.

## 13. Ambiguity Policy

Do not ask a beginner to choose between technical options the skill can safely infer.

Ask only when:

- two interpretations would produce materially different content, not merely different cinematography;
- a user-supplied lock is directly contradictory and cannot be reconciled;
- a missing reference or asset is essential to the requested preservation task;
- safety or rights constraints require clarification;
- the user explicitly wants to choose among creative directions.

Otherwise choose a coherent AUTO solution.

## 14. Shot Intent Output

Before downstream camera reasoning, the internal intent should be reducible to a compact brief like:

```text
PURPOSE
Narrative urban-night still.

STORY
A woman waits for a taxi while traffic passes behind her.

VIEWER RELATIONSHIP
Observational but emotionally near.

PRIMARY PRIORITY
Face and waiting posture.

SECONDARY PRIORITY
Recognizable wet London street context.

EMOTION
Anticipation, slight isolation, realism.

CONTEXT REQUIREMENT
Keep city lights, curb, road activity, and weather readable.

REALISM TARGET
Cinematic photographic.
```

This brief is not necessarily shown to the user. It is the decision basis for the rest of the shot.

## 15. Reality Gate Questions for Intent

Before accepting the shot design, ask internally:

- does the shot communicate the requested subject and action?
- does the emotional target come from composition/light/camera rather than filler adjectives?
- is the viewer relationship coherent?
- is important context accidentally erased?
- did any cinematic cliche get added without a reason?
- did AUTO choices respect all user locks?
- would a real cinematographer have a plausible reason for the chosen camera relationship?

If not, revise before provider adaptation.

## 16. Requirements Carried Forward

Tasks 3.2 through 3.7 must treat this file as the upstream intent layer.

Composition, capture, lens, focal length, focus, and motion choices should explain themselves through the visual priorities established here.

Later provider adapters may translate the decisions but must not reinterpret the story or replace explicit user intent.