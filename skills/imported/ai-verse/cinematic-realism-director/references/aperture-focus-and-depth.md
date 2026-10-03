# Aperture, Focus, and Depth Behavior

Status: RUNTIME KNOWLEDGE
Task: 3.6

This reference defines how the Cinematic Realism Director chooses aperture, focus strategy, focus plane, subject/background distance, and depth behavior for a still image.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`

## 1. Core Principle

Depth of field is not a cinema effect to maximize.

The skill must select depth behavior according to:

```text
story information
subject hierarchy
camera position
capture format
focal length
aperture
focus distance
subject distance
background distance
foreground distance
lens character
```

The correct question is not:

> How blurry can the background be?

It is:

> What must remain visually legible, and what depth behavior best supports the shot?

## 2. Separate the Variables

Do not collapse these into one concept:

```text
aperture
focus target
focus plane
focus distance
depth of field
background blur
foreground blur
focus falloff
bokeh character
```

A wide aperture may contribute to shallow depth, but the visible result also depends on framing, format, subject distance, focal length, and background distance.

A lens family may influence the aesthetic quality of defocus and focus falloff, but it does not replace the physical depth decision.

## 3. AUTO Depth Decision Order

When no aperture/focus values are locked, decide in this order:

1. Identify what the viewer must read.
2. Decide whether environment/context must remain legible.
3. Determine whether multiple subjects need simultaneous focus.
4. Determine camera distance and framing.
5. Determine format/focal relationship.
6. Choose a depth strategy.
7. Choose aperture consistent with that strategy.
8. Define focus target and transition behavior.
9. Check that foreground/background blur is spatially plausible.

Do not begin AUTO by selecting `f/1.2`.

## 4. Depth Strategy Classes

### Deep contextual focus

Use when:

- environment is narratively important;
- architecture/interiors must read clearly;
- multiple depth planes carry information;
- documentary realism favors observational legibility;
- product context matters;
- blocking across a group matters more than portrait isolation.

Behavior:

- retain meaningful detail across foreground, subject, and environment;
- stop down or choose geometry/distance that supports broader focus;
- avoid artificial global sharpness: depth can still taper naturally;
- keep distant detail believable rather than hyper-acutance-everywhere.

### Moderate cinematic separation

Use as the default for many narrative/commercial shots when one subject should lead while environment still matters.

Behavior:

- primary subject clearly resolved;
- environment remains identifiable;
- background softens progressively rather than becoming an abstract blur wall;
- foreground elements may be slightly out of focus if physically closer than the focus plane;
- preserve spatial depth cues.

### Shallow selective focus

Use when:

- attention must be tightly isolated;
- emotional intimacy benefits from visual separation;
- distracting environment should recede;
- product/detail emphasis benefits from selective focus;
- the user explicitly asks for shallow depth.

Behavior:

- define exactly what plane is sharp;
- allow plausible falloff around that plane;
- preserve enough facial/product geometry to avoid cutout-looking sharpness;
- do not make ears, hair, clothing, and both eyes arbitrarily sharp when geometry says otherwise;
- avoid synthetic circular blur masks.

### Razor-thin / specialty focus

Use sparingly for:

- macro/detail imagery;
- intentionally extreme fast-lens close-ups;
- specific experimental or fashion/editorial intent;
- explicit expert locks.

This is not the normal cinematic default.

## 5. Aperture Selection

Aperture should serve depth and exposure intent, not prestige.

### Wide apertures

Potential uses:

- low-light capture intent;
- subject isolation;
- close emotional portraiture;
- low-depth stylization;
- specific lens-character use.

Risks:

- too little facial/product depth;
- implausible group focus;
- background erased despite contextual importance;
- AI-style cutout subject against uniform blur;
- conflict with architecture/interior legibility.

### Mid apertures

Often useful for:

- balanced subject/environment separation;
- commercial/product work needing shape and detail;
- medium narrative shots;
- documentary/naturalistic framing;
- multi-subject scenes where some depth is needed.

### Smaller apertures

Useful for:

- architecture and interiors;
- environmental wides;
- layered blocking;
- landscape/travel context;
- multiple subjects across depth;
- deep-focus narrative intent.

Do not equate smaller aperture with `uncinematic`.

## 6. Focus Target

The focus target should be explicit when it matters.

Examples:

```text
near eye
both eyes as much as physically plausible
product logo plane
front edge of object
hands interacting with object
mid-subject plane
distant architecture
foreground prop
```

For portraits, the near eye is often a useful default when the head is angled and depth is shallow, but do not force this if the story points elsewhere.

For products, focus should prioritize the intended hero surface or functional detail, not blindly the geometric center.

For multi-subject scenes, define whether one person leads or whether focus must carry the group.

## 7. Focus Plane Coherence

A convincing frame has a believable plane/region of sharpest focus.

Check:

- objects at similar camera distance should not have radically inconsistent sharpness without optical reason;
- the sharpest region should not jump arbitrarily between non-coplanar surfaces;
- near/far objects should transition progressively according to their distance from the focus plane;
- subject edges should not remain uniformly cutout-sharp while the interior shows different focus behavior;
- hair strands crossing into defocus should transition naturally rather than retaining selection-mask sharpness.

## 8. Subject and Background Distance

Background blur depends heavily on how far the background lies behind the subject.

Do not request strong bokeh when:

- the subject is pressed against a wall;
- the environment is nearly coplanar with the subject;
- the camera is far away and geometry does not support the requested separation;
- deep-focus intent is locked.

If AUTO wants stronger separation without violating other locks, prefer changing unlocked geometry such as subject-background spacing before forcing an extreme aperture.

## 9. Foreground Blur

Foreground defocus should be physically motivated.

Use when:

- shooting through an object/window/doorway/foliage;
- a close shoulder creates OTS depth;
- a near prop is deliberately used for layered composition;
- visual obstruction increases intimacy or observational feel.

Avoid random foreground blur patches with no corresponding object or depth plane.

## 10. Over-the-Shoulder Depth

For OTS shots:

- the near shoulder/head may be partially soft if the focus is on the farther subject;
- the amount of blur depends on camera-to-foreground distance and focus distance;
- do not turn the foreground person into an abstract smear unless deliberately very close and shallow;
- if both foreground and far subject must read, use a deeper-focus strategy rather than pretending both are on one focus plane.

For a top-down OTS, preserve the geometric relation between shoulder, hands, subject, and ground plane before deciding blur.

## 11. Portrait Depth

Portrait depth should be chosen by emotional purpose.

### Intimate close portrait

Moderate-to-shallow depth may support intimacy, but preserve enough facial volume to avoid a pasted-eye effect.

### Environmental portrait

Keep surroundings readable enough to explain person + place.

### Editorial/fashion portrait

Depth can be stylized more aggressively, but wardrobe, silhouette, and intended production design must remain legible.

### Documentary portrait

Prefer plausible available-light/focus behavior over exaggerated creamy-background aesthetics unless the actual setup justifies it.

## 12. Product Depth

For products:

- important branding and geometry should remain legible;
- shallow depth must not obscure required product features;
- reflective surfaces need coherent focus and reflection behavior;
- macro product details may use very shallow focus, but the focus target must be explicit;
- avoid synthetic tilt-shift-style selective blur unless deliberately requested.

## 13. Food Depth

Food often benefits from selective depth, but:

- the hero ingredient/texture should be in the focus plane;
- nearby ingredients should transition naturally;
- plate/table context should not become meaningless mush unless the shot is a true detail/macro;
- steam, droplets, garnish, and utensils should follow physical distance cues.

## 14. Architecture and Interiors

Default bias: preserve spatial legibility.

- do not use shallow DOF as a generic cinema token;
- maintain wall/furniture depth relationships;
- allow natural distance falloff, but key structural elements should remain readable;
- if a foreground detail is the explicit subject, shallow focus may be appropriate, but it becomes a detail shot rather than a general architectural view.

## 15. Automotive Depth

For full-vehicle hero shots:

- preserve enough depth that vehicle body shape and key design surfaces remain coherent;
- do not render grille sharp while the adjacent hood plane is implausibly blurred if geometry is similar;
- use shallow depth more readily for detail shots such as emblem, wheel, light, cockpit control, stitching, etc.;
- background separation should reflect actual vehicle-background distance.

## 16. Macro and Close Detail

Macro/near-macro framing naturally makes depth management critical.

Use:

- precise focus target;
- strong but plausible falloff;
- microtexture on the sharp plane;
- depth cues from adjacent soft planes.

Avoid:

- entire macro subject perfectly sharp despite extreme proximity unless focus stacking is explicitly intended;
- using `macro` merely as a synonym for `high detail`.

## 17. Deep Focus

Deep focus is a valid cinematic strategy.

Use when:

- foreground and background actions both matter;
- spatial relationships tell the story;
- tension comes from allowing the viewer to inspect the whole frame;
- architecture/environment is important;
- staging carries meaning across depth.

Deep focus does not mean:

```text
HDR-sharp everything with no optical hierarchy
```

It means multiple important planes remain acceptably legible while the image still behaves like one optical capture.

## 18. f/1.2 + Deep Focus Conflict

If the user locks both:

```text
f/1.2
and
deep focus across a large scene
```

classify according to `references/parameter-conflicts.md`.

Possible reconciliation if other values remain AUTO:

- increase camera distance;
- choose a wider field of view/format relationship;
- arrange subjects nearer one focus plane;
- use environmental composition where critical information falls within the available focus region.

Do not silently change f/1.2 if it is locked.

If the requested geometry still makes the combination materially incompatible, surface the conflict rather than inventing impossible depth.

## 19. Reference Matching

From a reference image, infer only observable depth behavior such as:

- shallow / moderate / deep;
- focus target;
- foreground softness;
- background separation;
- transition character;
- apparent bokeh shape/quality;
- relative focus distances.

Do not infer exact aperture from blur alone unless trustworthy metadata is available.

Example:

```text
OBSERVED:
moderately shallow focus with the subject's face sharp and background recognizable but softened

NOT ALLOWED AS FACT:
shot at T1.5
```

## 20. Provider Translation

Some providers expose aperture/focal controls; others only accept prose.

Core truth remains:

```text
depth intent
focus target
focus/falloff behavior
subject-background geometry
```

Adapter translation may use:

- native aperture control when supported;
- natural-language depth instructions;
- reference-image guidance;
- edit/preservation instructions.

Never claim a native aperture control exists when it does not.

## 21. Anti-AI Depth Failures

Reject or repair:

- uniform Gaussian background blur;
- cutout-sharp subject contours;
- different blur directions on similar-depth objects;
- both eyes equally razor sharp at geometry where one should fall off noticeably;
- random sharp background patches;
- bokeh objects that ignore scene depth;
- foreground blur with no foreground object;
- every portrait using maximum separation;
- impossible product/architecture depth;
- focus behavior inconsistent with reflection/refraction geometry.

## 22. Runtime Decision Template

For AUTO, reason internally as:

```text
INFORMATION THAT MUST READ
primary subject
secondary subject/context
environment importance

GEOMETRY
camera distance
subject distance
background distance
foreground distance
format/focal relationship

DEPTH STRATEGY
deep contextual | moderate separation | shallow selective | specialty

APERTURE
selected or locked

FOCUS
focus target
focus plane / region
transition behavior

VERIFY
is blur spatially plausible?
is context preserved?
is the sharpest region narratively correct?
```

## 23. Hard Rules

```text
cinematic != shallow depth
fast lens != always wide open
f/1.2 != automatically better
background blur != subject isolation by itself
bokeh != depth of field
lens character != focus geometry
large format != automatically shallow depth
deep focus != video-looking
macro != everything sharp
reference blur != exact aperture metadata
```

## 24. Depth Reality Gate

Before finalizing:

1. Is the intended focus target clear?
2. Does the depth strategy serve the story/purpose?
3. Are subject and background distances consistent with the blur amount?
4. Is foreground softness physically motivated?
5. Does sharpness transition through space rather than by object-selection masks?
6. Are multi-subject focus relationships plausible?
7. Does aperture respect explicit locks?
8. Is environment legibility preserved when needed?
9. Are bokeh/falloff cues compatible with the lens-character reference?
10. Has the skill avoided automatic maximum blur?

If not, revise unlocked variables before output.
