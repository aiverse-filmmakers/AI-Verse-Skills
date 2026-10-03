# Lens Character

Status: RUNTIME KNOWLEDGE
Task: 3.4

This reference translates named lens families and optical intent into observable image behavior. It prevents the skill from using lens names as decorative style tokens or reducing every cinema lens to the same package of shallow focus, flare, edge softness, and anamorphic streaks.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`

Evidence basis:

- `references/research/lenses.md`
- `references/research/lenses-supplement.md`
- `references/source-ledger.md`

## 1. Core Principle

A lens reference is useful only when it changes one or more observable optical traits.

Reason through separate axes:

```text
lens_family / lens_reference
focal_length
aperture
focus_distance
anamorphic_squeeze
optical_character
```

Do not collapse those into one label.

A generated image cannot prove that it was physically captured through a named lens. The skill may request the documented or corroborated visual behavior associated with the lens, but must not present the rendered output as optical proof.

## 2. Observable Lens Character Axes

When a lens family matters, describe only relevant axes:

```text
global contrast
microcontrast / local definition
center-to-edge resolution or falloff
focus transition
bokeh geometry and smoothness
flare / ghosting / veiling glare
chromatic behavior
distortion
anamorphic squeeze and geometry
breathing relevance
close-focus behavior
transmission / wide-open behavior
color tendency only when supported
```

Not every shot requires every axis.

## 3. Story Before Character

Lens character serves the shot.

Examples:

- restrained modern optics may suit clean commercial/product work;
- gentler edge definition may help a period portrait;
- controlled anamorphic behavior may support widescreen scale;
- strong flare is useful only when a source and story motivate it;
- high optical precision may be preferable when architecture or product geometry must stay clean.

Do not choose an exotic lens family simply because the user said `cinematic`.

## 4. AUTO Lens Selection

When the user does not name a lens family:

1. choose field of view and camera distance from composition/perspective needs;
2. choose aperture/focus from narrative depth needs;
3. decide whether a distinct optical character is useful;
4. if not, use a neutral cinema-lens behavior rather than inventing a brand;
5. select a named family only when the provider exposes a useful native control, the user asks for it, or benchmark evidence later shows meaningful benefit.

Default AUTO character should usually be restrained:

```text
clean geometry
believable focus transition
natural contrast
no gratuitous flare
no artificial edge sharpening
no exaggerated aberrations
```

## 5. User Lens Locks

If the user names a lens or family, treat it as locked.

Do not silently substitute a supposedly `better` lens.

If the provider lacks a literal control:

- preserve the named reference in the shot spec;
- translate supported observable traits into prompt language;
- record unsupported literal controls in provider adaptation;
- never claim exact simulation.

## 6. Modern / Clean Families

### ARRI Signature Prime

Evidence strength: strong first-party.

Useful observable tendencies:

- high resolving ability without requiring brittle sharpening;
- smooth facial tonal transitions;
- soft, controlled bokeh transitions;
- low geometric distortion and controlled chromatic aberration;
- restrained, delicate flare behavior;
- open shadows and clean blacks when exposure/grade support them.

Generation translation:

```text
high-resolution natural rendering
smooth focus transition
controlled geometry
restrained flare
clean but non-clinical skin detail
```

Avoid:

- fake vintage haze;
- heavy chromatic fringing;
- exaggerated swirl;
- mandatory bloom.

### ARRI / ZEISS Master Prime

Evidence strength: strong first-party.

Useful traits:

- high resolution and contrast;
- very low geometric distortion;
- strongly reduced flare;
- virtually no breathing;
- precise, neutral, controlled rendering;
- consistent high-speed optical performance.

Generation translation:

```text
clean high-resolution optics
controlled geometry
neutral precise image
restrained flare and veiling glare
strong contrast without artificial edge enhancement
```

Avoid inventing warmth, anamorphic streaking, heavy edge softness, or vintage bloom.

### Leitz SUMMILUX-C

Evidence strength: strong first-party.

Useful traits:

- high clarity and resolution;
- restrained distortion and chromatic aberration;
- natural, warm skin reproduction;
- gentle focus rolloff;
- high detail without brittle digital sharpness;
- comparatively consistent center-to-edge performance.

Generation translation:

```text
high-detail natural image
warm but not heavily tinted skin
smooth facial rendering
gentle focus falloff
clean geometry
```

Avoid generic `Leica vintage haze`, extreme softness, or forced low contrast.

### ZEISS Supreme Prime

Evidence strength: strong first-party.

Useful traits:

- smooth focus falloff;
- elegant bokeh;
- modern optical precision;
- detailed but flattering subject rendering;
- clean geometry.

Generation translation:

```text
crisp focal plane without hard sharpening
smooth depth transition
clean modern geometry
elegant non-nervous defocus
neutral contemporary rendering
```

### ZEISS Supreme Prime Radiance

Evidence strength: strong first-party.

Use Supreme behavior plus deliberately controlled flare character and a modest warmer tendency where appropriate.

Important:

- flare requires a plausible bright source;
- do not add flare to every shot;
- do not let flare erase subject hierarchy.

## 7. Character / Vintage-Leaning Families

### Cooke Panchro Classic

Evidence strength: strong first-party.

Useful traits:

- gentler global contrast than highly modern multi-coated optics;
- characteristic center-to-edge definition falloff;
- more permissive internal reflection / veiling behavior around strong sources;
- controlled vintage irregularity;
- focal plane remains intentional even when edges are gentler.

Generation translation:

```text
gentler global contrast
clean focal subject with softer edge definition
subtle vintage optical irregularity
motivated veiling flare near strong sources
less clinical transition than modern precision optics
```

Avoid making the entire image blurry, sepia, low-resolution, or heavily flared.

### Cooke S4 / S4-Type

Evidence strength: corroborated practitioner description, not hard lab characterization.

Useful tendencies may include:

- natural skin reproduction;
- gentle focus falloff;
- mild optical imperfection rather than sterile precision;
- restrained warmth/organic impression;
- gentle flare and edge softness.

Because this evidence is less authoritative than the first-party technical families above, keep translation restrained.

### Canon K35

Evidence strength for detailed character: limited.

V1 rule:

- preserve an explicit K35 lock;
- do not fabricate a detailed universal K35 signature;
- use only traits supported by future corroborated evidence or provider-native behavior;
- if needed, describe the intended vintage/fast-prime role separately from unverified brand mythology.

## 8. Anamorphic Families

### Panavision G-Series

Evidence strength: strong first-party.

Useful traits:

- high contrast and resolution;
- balanced aberrations;
- controlled squeeze;
- restrained breathing;
- anamorphic behavior without requiring uncontrolled distortion.

Generation translation may include:

```text
controlled anamorphic geometry
appropriate anamorphic out-of-focus shape
high-performance contrast and detail
restrained edge distortion
flare only when source placement motivates it
```

### Hawk V-Lite / V-Lite 1.3x

Evidence strength: strong first-party for family/squeeze behavior.

Reason explicitly about:

- squeeze ratio;
- horizontal/vertical geometry;
- out-of-focus shape;
- edge/focus behavior;
- field-of-view relationship;
- flare only when justified.

A 1.3x anamorphic reference must not be rendered as an exaggerated 2x anamorphic caricature.

## 9. Anamorphic Is Not a Blue-Flare Preset

Hard rule:

```text
anamorphic != blue horizontal streak + extreme oval bokeh + warped edges
```

Possible anamorphic cues include:

- squeeze-dependent geometry;
- altered bokeh geometry;
- astigmatic/focus effects;
- edge behavior;
- streak or ghost flare;
- breathing characteristics.

Each is lens-family dependent and should be used only when justified.

If the user requests clean anamorphic imagery with no flare, preserve that request.

## 10. Cinema Zooms

### Angenieux Optimo Style 25-250

Evidence strength: strong first-party technical behavior.

Useful translation:

- professional cinema zoom response;
- controlled distortion;
- minimized breathing;
- consistent transmission/color intent;
- framing flexibility without assuming an exotic vintage look.

Do not invent a pronounced signature if evidence does not support one.

## 11. Focal Length Is Separate

Never infer lens character from focal length alone.

Example:

```text
35mm ARRI Signature
35mm Cooke Panchro
35mm anamorphic
```

share a nominal focal length but may render very differently.

`references/focal-length-and-perspective.md` owns focal length, camera distance, field of view, and perspective logic.

## 12. Aperture Is Separate

Lens family does not determine the aperture choice.

Even if a family is fast:

- do not default to maximum aperture;
- choose aperture from desired depth, focus reliability, optical behavior, light, and story;
- an f/1.4-capable lens may legitimately be used at f/4 or f/8.

Task 3.6 owns depth-of-field logic.

## 13. Flare Policy

Flare must be physically motivated.

Before adding it, verify:

```text
Is there a bright source in or near the optical path?
Would this lens family plausibly flare this way?
Does the flare support the shot rather than decorate it?
Does it obscure required subject/product detail?
```

If any answer fails, omit or reduce flare.

## 14. Bokeh Policy

Bokeh is a consequence of:

```text
lens design
aperture
focus distance
subject distance
background distance
highlight structure
anamorphic geometry if relevant
```

Do not prompt `creamy bokeh` by default.

Background blur should retain spatial logic and depth progression rather than become a uniform synthetic smear.

## 15. Edge Behavior and Imperfection

Optical imperfection is useful only when it remains coherent.

Possible controlled traits:

- edge resolution falloff;
- modest veiling glare;
- slight chromatic fringe;
- mild distortion;
- non-uniform sharpness;
- subtle bokeh irregularity.

Do not stack every imperfection at once.

A character lens is not a damaged lens.

## 16. Distortion Policy

Distinguish:

```text
perspective exaggeration from camera proximity
geometric lens distortion
anamorphic deformation
fisheye projection
```

They are not interchangeable.

A wide rectilinear lens can produce dramatic near/far scale relationships while keeping straight lines largely rectilinear.

This is particularly important when a huge foreground hand, shoe, prop, vehicle nose, or product is desired without a circular/fisheye background.

## 17. Reference Matching

When analyzing a reference image:

Allowed observations:

```text
low contrast
soft edge falloff
oval out-of-focus highlights
restrained veiling flare
clean rectilinear geometry
high microcontrast
```

Not allowed without metadata/evidence:

```text
definitely Cooke Panchro 40mm
definitely ARRI Signature 35mm
definitely Panavision G-Series
```

Named hardware must remain a hypothesis unless supplied or externally verified.

## 18. Provider Translation

If the active provider exposes native lens controls:

- map the shot spec to those controls;
- preserve the universal observable intent in case provider behavior differs;
- do not duplicate incompatible provider control and text instructions unnecessarily.

If only free-text prompting exists:

- describe observable traits;
- include a named lens reference only when helpful;
- keep prompts concise enough that lens cues do not overwhelm subject/story requirements.

## 19. Lens Reality Gate

Before accepting a lens design, check:

```text
[ ] lens family serves story/purpose
[ ] user lens lock preserved
[ ] focal length treated separately
[ ] aperture treated separately
[ ] camera distance/perspective not falsely attributed to lens alone
[ ] flare is source-motivated
[ ] anamorphic cues match squeeze/family rather than stereotype
[ ] geometry is coherent
[ ] bokeh follows depth/highlight logic
[ ] character is restrained rather than artifact-stacked
[ ] reference analysis does not hallucinate exact hardware
```

## 20. Failure Patterns

Reject these patterns:

```text
cinematic = anamorphic flare
vintage lens = blurry everything
modern lens = oversharpened everything
Leica = warm haze
Cooke = orange skin
Master Prime = sterile digital look
wide lens = fisheye
anamorphic = warped edges everywhere
fast lens = always shoot wide open
```

The runtime objective is not to imitate lens mythology. It is to create a coherent, observable optical response that supports the shot.
