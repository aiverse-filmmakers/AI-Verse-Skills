# Phase 1 Research - Lens Character and Optical Behavior

Status: RESEARCH EVIDENCE

Primary classification: `CONFIRMED` for first-party optical/manufacturer claims, `CORROBORATED` for consistent cinematographer testimony, `INFERRED` only when explicitly identified.

This file exists to prevent a major failure mode in AI image prompting: treating a lens name as a magical style token without understanding what observable optical behavior the name is supposed to evoke.

## Governing Principle

A lens reference should be translated through **observable traits** such as:

- global contrast;
- local/microcontrast;
- center-to-edge sharpness/falloff;
- bokeh geometry and transition quality;
- flare and veiling glare;
- ghosting;
- chromatic aberration/fringing;
- distortion;
- anamorphic squeeze and out-of-focus geometry;
- breathing;
- close-focus behavior;
- transmission/aperture behavior;
- color/warmth tendencies where evidence supports them.

A generated image cannot prove that it was optically captured by a named lens. The skill may only request the observable visual behavior associated with the reference.

## ARRI Signature Primes

Source: `LEN-ARRI-001`.

ARRI's first-party material emphasizes:

- smooth rendering of skin;
- open shadows alongside crisp blacks;
- soft/smooth bokeh;
- controlled, delicate flare behavior;
- low distortion and controlled chromatic aberration;
- a modern high-performance image intended to remain natural rather than clinically harsh.

### Safe generative translation

When `ARRI Signature` is explicitly locked or selected:

- maintain high resolving ability without brittle digital oversharpening;
- render faces with smooth tonal transitions and believable skin texture;
- allow clean, soft defocus transitions;
- use restrained flare unless a bright source actually intersects the optical path;
- keep geometry clean unless perspective itself creates wide-angle exaggeration;
- avoid adding vintage aberrations that contradict the family.

## Panavision G-Series Anamorphic

Source: `LEN-PAN-001`.

Panavision documents characteristics including:

- high contrast and high resolution;
- balanced aberrations;
- glare resistance;
- tightly controlled anamorphic squeeze;
- minimal breathing;
- anamorphic optical behavior without requiring uncontrolled distortion everywhere.

### Safe generative translation

A G-Series reference may justify:

- anamorphic geometry/bokeh cues appropriate to the squeeze;
- controlled rather than extreme edge distortion;
- high-performance contrast/resolution;
- restrained breathing relevance in stills;
- flares only when motivated by light placement.

Do not automatically add a bright horizontal blue flare merely because `anamorphic` appears.

## Cooke Panchro Classic

Sources: `LEN-COOKE-001`, `LEN-COOKE-002`.

First-party Cooke material connects the Panchro heritage with:

- classic Speed Panchro visual character;
- controlled flare/distortion/spherical-aberration design choices;
- older/simple coating behavior contributing to more internal reflection and lower contrast than highly modern multi-coated optics;
- characteristic focus/definition falloff toward the image edges.

### Safe generative translation

A Panchro-style treatment may include:

- gentler global contrast;
- softer edge definition/falloff while retaining an intentional focal plane;
- warmer/less clinical facial rendering only when corroborated by the actual source/grade intent;
- more permissive veiling flare around strong sources;
- subtle vintage optical irregularity without turning the entire image soft.

The skill should prefer these concrete traits over generic phrases such as `vintage cinematic lens`.

## Cooke S4 / S4-Type Character

Source: `LEN-COOKE-003`, official Cooke publication containing working-cinematographer testimony.

The evidence here is practitioner description rather than laboratory specification. Reported visual qualities include:

- natural skin reproduction;
- gentle focus falloff;
- slight imperfection that avoids sterile rendering;
- gentle flare;
- some edge softness;
- warm/lived-in character.

Classification: `CORROBORATED`, not hard physics.

### Safe generative translation

Use restrained language around:

- smooth facial tonal transitions;
- gentle rather than abrupt focus falloff;
- a clean center with less clinical edge behavior;
- controlled warm/organic impression when it supports the story;
- subtle flare, not automatic flare.

## ZEISS Supreme Prime

Source: `LEN-ZEISS-001`.

ZEISS first-party material emphasizes:

- smooth focus falloff;
- elegant bokeh;
- high performance with a gentle/organic rendering goal;
- detailed but flattering reproduction of skin and subjects.

### Safe generative translation

- crisp subject detail without hard artificial edge enhancement;
- smooth depth transition;
- clean modern optical geometry;
- elegant rather than nervous background blur;
- neutral contemporary rendering unless the grade specifies otherwise.

## ZEISS Supreme Prime Radiance

Source: `LEN-ZEISS-002`.

ZEISS positions Radiance as maintaining Supreme performance while providing:

- controlled, repeatable flare character;
- slightly warmer character;
- maintained contrast relative to uncontrolled vintage veiling flare.

### Safe generative translation

Use flare as a deliberately motivated optical response from strong in-frame/near-frame light, not a decorative overlay.

## Hawk V-Lite / V-Lite 1.3x

Sources: `LEN-HAWK-001`, `LEN-HAWK-002`.

First-party Hawk/Vantage material confirms:

- compact/lightweight anamorphic lens families;
- characteristic anamorphic rendering;
- 1.3x V-Lite systems intended to use more of a 16:9 sensor area for widescreen framing.

### Safe generative translation

The important variables are not the brand label alone but:

- anamorphic squeeze amount;
- bokeh shape/geometry;
- horizontal versus vertical rendering relationship;
- edge/focus behavior;
- flare behavior when justified;
- field-of-view/framing relationship.

A 1.3x reference should not be treated like an exaggerated 2x anamorphic caricature.

## Angenieux Optimo Style 25-250

Source: `LEN-ANG-001`.

First-party documentation supports:

- long-range cinema zoom architecture;
- constant T3.5 across the zoom range;
- internal focusing;
- minimized breathing;
- controlled distortion;
- color matching intended for cinema use.

### Safe generative translation

If selected, the main value may be a professional cinema-zoom response and framing flexibility rather than a strong exotic `look`.

Do not fabricate a pronounced vintage signature without additional evidence.

## Canon K35

Source: `LEN-CANON-001`.

Phase 1 has good first-party historical evidence for the K35 set and its fast T-stop/focal-length package, but not enough strong first-party material to encode a detailed authoritative optical-character profile.

Safe V1 behavior:

- honor `Canon K35` as a user-supplied historical lens reference;
- allow only lower-confidence/corroborated character translation if later evidence supports it;
- do not state a detailed K35 look as confirmed manufacturer fact based on community mythology alone.

This remains a gap.

## Leica / Leitz Summilux-C

Magnific exposes Leica Summilux/Summilux-C options, but Phase 1 did not surface a sufficiently strong current first-party Leitz/Leica page with detailed optical-character statements suitable for the knowledge base.

Safe behavior:

- preserve explicit user lock;
- later adapter may pass the literal name when the provider supports it;
- universal brain should not invent detailed traits until evidence is added.

## ZEISS / ARRI Master Prime

Magnific exposes ZEISS Master/Master Prime references, but Phase 1 does not yet contain a sufficiently strong first-party current optical-character source.

Safe behavior mirrors Summilux-C:

- preserve user lock;
- use only independently verified characteristics;
- do not fill the gap with remembered forum descriptions.

## Anamorphic Is Not a Flare Preset

Hard research synthesis:

Anamorphic lens behavior may involve multiple optical consequences depending on design:

- squeeze;
- horizontal/vertical field relationship;
- oval or otherwise altered out-of-focus shapes;
- astigmatism/focus behavior;
- edge distortion;
- breathing;
- streak/ghost flare character.

The skill must not reduce `anamorphic` to:

```text
blue horizontal flare + extreme oval bokeh + warped edges
```

Those cues are optional and lens-family dependent.

## Focal Length Is Not Lens Character

A 35mm Cooke, 35mm ARRI Signature and 35mm anamorphic lens may share nominal focal length while rendering differently.

Later schema should separate:

```text
lens_family / lens_reference
focal_length
anamorphic_squeeze
aperture
focus_distance
optical_character
```

This also allows expert users to lock only the variables they care about.

## Perspective Caution

Lens focal length by itself does not create `facial distortion` in isolation.

Perspective depends primarily on camera position/distance. A very wide lens often leads the camera to move closer for equivalent framing, which creates stronger near/far scale relationships.

Later runtime prompts should avoid false statements such as:

```text
14mm automatically distorts the face
```

and instead reason about camera distance, field of view and framing together.

## Lens Character Translation Strategy

For every supported lens family, later Phase 3 entries should use this structure:

```text
REFERENCE
name / family

EVIDENCE
first-party facts
practitioner corroboration
confidence

OBSERVABLE TRAITS
contrast
falloff
bokeh
flare
edge behavior
distortion
chromatic behavior
anamorphic traits

GENERATION TRANSLATION
restrained prompt language

AVOID
common caricatures / unsupported claims
```

## Phase 1 Lens Knowledge Strength

Strong:

- ARRI Signature;
- Panavision G-Series;
- Cooke Panchro Classic;
- ZEISS Supreme/Supreme Radiance;
- Hawk V-Lite family;
- Angenieux Optimo technical behavior.

Moderate:

- Cooke S4 aesthetic description, because current evidence is practitioner testimony published by Cooke rather than controlled optical measurement.

Weak / unresolved:

- Canon K35 detailed look;
- Leica/Leitz Summilux-C detailed first-party look;
- Master Prime detailed current first-party look;
- exact behavior of some still-photo lens families exposed by Magnific.

## Requirements Carried Forward

Phase 3 must:

- model lens name and observable lens behavior separately;
- prevent lens-name hallucination when analyzing references;
- translate named lens locks into visual traits where evidence exists;
- preserve literal user lock even when detailed traits are unknown;
- use restrained, motivated flare;
- keep perspective reasoning separate from focal length mythology;
- calibrate generative lens-character strength through evals rather than maxing every artifact.