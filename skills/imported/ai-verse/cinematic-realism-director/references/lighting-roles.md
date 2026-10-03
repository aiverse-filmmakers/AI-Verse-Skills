# Key, Fill, Negative Fill, Edge, Bounce, and Practical Logic

Status: RUNTIME KNOWLEDGE
Task: 4.2

This reference defines the distinct jobs of common lighting roles and when each should or should not be used.

Evidence basis:

- `references/motivated-lighting.md`
- `references/research/lighting.md`

## 1. Core Rule

Do not treat lighting roles as ingredients that every cinematic image must contain.

A shot may need:

```text
key only
key + ambient
key + negative fill
available light only
practicals only
soft commercial key + fill
sun + sky
window + room bounce
```

and still be fully cinematic.

## 2. Key Light

The key is the primary directional modeling source.

It should define:

- subject shape;
- dominant shadow direction;
- principal specular direction;
- facial/object modeling;
- primary exposure relationship.

The key may be:

- sun;
- window;
- lamp;
- softbox;
- bounced source;
- overhead fixture;
- sign;
- candle;
- another motivated source.

Do not add a separate `cinematic key` if the actual environment already provides one.

## 3. Fill

Fill raises shadow-side exposure without replacing the key.

Possible sources:

- sky;
- wall bounce;
- floor bounce;
- white card;
- ceiling;
- soft frontal source;
- ambient environment.

Fill should be described by effect:

```text
very gentle frontal lift preserving key direction
cool sky fill retaining detail in sun shadows
white-wall bounce opening the eye sockets slightly
```

Avoid flat omnidirectional fill that erases modeling unless a deliberate high-key look requires it.

## 4. Negative Fill

Negative fill removes ambient/bounce contribution.

Use it when:

- a bright environment is flattening the subject;
- the shadow side needs stronger dimensional separation;
- a face/product needs controlled contrast;
- surrounding white surfaces create too much accidental fill.

Visible result:

- deeper shadow-side values;
- stronger shape;
- reduced stray bounce;
- preserved directional hierarchy.

Do not equate negative fill with crushed blacks.

## 5. Edge / Back Light

Back or edge light is optional.

Use only when source geometry supports it or when deliberate production lighting is justified.

Useful purposes:

- contour separation against similar-value background;
- hair/shoulder separation;
- atmospheric backscatter;
- translucent material illumination;
- reflective edge definition.

Do not use when:

- no plausible source exists;
- the subject already separates clearly;
- it creates a generic halo;
- it contradicts environmental direction.

A perfect symmetric rim on every subject is a failure condition.

## 6. Bounce

Bounce redirects another source into a larger indirect source.

Reason about:

```text
originating source
bounce surface size
bounce surface color
surface reflectance
subject distance
resulting direction
```

Examples:

- warm wood floor bounce under face;
- white wall returning window light softly;
- pale sand lifting lower-body shadows;
- negative dark wall providing almost no return.

Do not invent bounce light without a plausible surface or production setup.

## 7. Practicals

Practicals are visible or scene-integrated lights.

They can function as:

- motivation;
- exposure anchor;
- background depth cue;
- local color source;
- reflection source;
- composition element.

A practical should not magically illuminate the whole environment.

Its influence should respect:

- distance;
- occlusion;
- source size;
- surrounding reflectance;
- exposure.

## 8. Ambient Light

Ambient is not `fill light` in the studio-only sense. It is the cumulative low-directionality contribution of the environment.

Examples:

- blue sky dome;
- bright white room;
- city glow;
- overcast sky;
- fluorescent office base level;
- moonlit landscape ambience.

Ambient establishes shadow color and baseline visibility.

## 9. Light Role Precedence

AUTO should resolve roles in this order:

```text
1. identify environmental/visible sources
2. choose dominant key
3. estimate ambient contribution
4. decide whether natural fill is sufficient
5. add or remove fill only if needed
6. add back/edge only if justified
7. use practicals according to location logic
8. add bounce only if a real/environmental or production surface explains it
```

## 10. Portrait Examples

### Natural window portrait

```text
key: window camera-left
ambient: room bounce
fill: none or slight white-wall return
negative fill: optional camera-right if room is too bright
edge: none unless another source exists
practical: background lamp only if naturally present
```

### Beauty commercial

```text
key: large frontal-side source
fill: controlled near-axis lift
negative fill: optional for jaw/cheek shape
edge: only if required by hair/background separation
bounce: may open under-chin shadows
practicals: usually irrelevant unless set design calls for them
```

### Low-key drama

```text
key: selective motivated source
ambient: restrained
negative fill: often useful
fill: minimal
edge: source-dependent, not automatic
practicals: can provide motivation/depth
```

## 11. Product Examples

### Glossy bottle

Use sources primarily to create readable reflection gradients.

Key/fill terminology is secondary to:

- strip reflection placement;
- label readability;
- edge definition;
- base contact;
- cap/shoulder specular hierarchy.

### Matte package

Use broad directional light to reveal geometry without flattening printed graphics.

### Metal object

Control reflected environment. A `key` may appear mainly as a reflected source shape rather than diffuse brightness.

## 12. Automotive Examples

Car lighting is often reflection design.

Use:

- long broad source gradients;
- sky/environment reflections;
- edge highlights from geometry;
- controlled negative spaces in reflection.

Avoid fake white streaks painted onto body panels without environmental cause.

## 13. Exterior Daylight

### Clear sun

```text
key: direct sun
fill: sky + environment
negative fill: only production-controlled close work
edge: may occur naturally depending sun position
bounce: ground/environment
```

### Overcast

```text
key: broad sky hemisphere / dominant sky direction
fill: environment
negative fill: useful for portraits if needed
edge: generally weak unless another source exists
```

Do not create hard cast shadows in flat overcast without another source.

## 14. Night Exterior

Possible hierarchy:

```text
streetlight / storefront / neon / vehicle / moon / ambient city glow
```

Choose one dominant idea rather than lighting every surface independently.

## 15. Mixed Color Sources

Each light role can have different color.

Examples:

- warm practical key + cool window ambient;
- sodium street key + blue-hour sky fill;
- red neon edge + neutral storefront key.

Color should follow source location, not be globally painted onto image sides.

## 16. Fill Ratio Language

Exact numerical ratios are optional and usually unnecessary.

Prefer qualitative levels:

```text
flat
very gentle modeling
gentle modeling
moderate contrast
strong contrast
selective / near-silhouette
```

If the user supplies an exact ratio, preserve it as a lock.

## 17. Common Failure Modes

Reject:

- key from left but cast shadows imply right;
- fill as bright as key unintentionally;
- rim with no source;
- `negative fill` that becomes total black clipping;
- practical lamp lighting distant room uniformly;
- bounce whose color ignores bounce surface;
- every face receiving independent beauty lighting in one scene;
- eye catchlights that do not correspond to sources;
- duplicate catchlights from nonexistent fixtures;
- product reflections that do not match source geometry.

## 18. Lighting Role Reality Gate

Check:

1. Is there a dominant source?
2. Is the key consistent across subject and environment?
3. Is fill level intentional?
4. Is negative fill reducing bounce rather than inventing darkness?
5. Is edge light physically/source motivated?
6. Do practicals have local, plausible influence?
7. Does bounce have a plausible surface and color?
8. Do eye/specular reflections correspond to real sources?
9. Do multiple subjects share the same lighting world?
10. Does the role structure support the story rather than a lighting recipe cliché?

## 19. Runtime Translation Template

```text
MOTIVATION
[dominant source and why it exists]

KEY
[direction, apparent size, quality, color, falloff]

AMBIENT
[environmental base and shadow color]

FILL / NEGATIVE FILL
[what is added or removed and why]

EDGE / BACK
[only if source-motivated]

PRACTICALS
[visible sources and local contribution]

BOUNCE
[environmental/production return]

MATERIAL CONSEQUENCE
[skin, glass, metal, fabric, car paint, etc.]
```

Omit unused roles rather than filling every field decoratively.