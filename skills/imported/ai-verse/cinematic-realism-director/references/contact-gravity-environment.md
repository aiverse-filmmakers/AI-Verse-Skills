# Contact, Gravity, and Environmental Interaction

Status: RUNTIME KNOWLEDGE
Task: 5.5

This reference defines how people, objects, clothing, surfaces, dust, moisture, wind, and terrain should visibly interact so subjects feel physically present in the scene rather than composited or floating.

Use with:

- `references/anti-ai-artifact-taxonomy.md`
- `references/fabric-and-material-realism.md`
- `references/motion-and-shutter.md`
- `references/reflection-shadow-coherence.md`
- `schemas/realism-diagnosis.schema.json`

## 1. Governing Principle

Physical presence requires evidence of force exchange.

The scene should answer:

```text
What supports the subject?
Where is weight transferred?
What compresses, bends, deforms, scatters, displaces, or gets wet?
What moves with the wind or motion?
What remains rigid?
```

A subject that has correct anatomy but no believable contact often still reads as synthetic.

## 2. Contact Hierarchy

Evaluate contact from largest to smallest effect:

```text
support / load-bearing contact
body-object or object-object contact
soft-material compression
ground interaction
contact shadow / ambient occlusion cue
surface contamination / transfer
secondary particles / deformation
```

Do not use contact shadow as a substitute for real geometry.

## 3. Weight and Support

Weight should be visible through posture and support geometry.

Examples:

- feet spread/load differently during stance or motion;
- seated body mass compresses cushions/clothing;
- hands resting on a table alter finger shape/pressure;
- a heavy bag pulls shoulder/strap geometry;
- a tire deforms subtly at its contact patch;
- heavy props rest with convincing orientation instead of floating.

Avoid exaggerated deformation unless the material and load support it.

## 4. Ground Contact

Check:

- foot/shoe/tyre/object alignment with the surface plane;
- no daylight gap where weight-bearing contact should exist;
- contact shadow or soft occlusion where appropriate;
- terrain-specific deformation;
- matching dirt/wetness transfer where relevant.

### Sand
Possible cues:

- footprint/tire depression;
- displaced ridges;
- soft edge collapse;
- sand accumulation near contact.

### Snow
Possible cues:

- compression depth based on load and snow condition;
- disturbed powder;
- darker/denser compressed zones;
- footprints/tracks matching movement direction.

### Mud / wet soil
Possible cues:

- sinking/compression;
- wet transfer;
- splash pattern tied to motion;
- darker moisture near contact.

### Hard floor
Possible cues:

- geometry/contact shadow/reflection rather than visible deformation.

## 5. Body and Clothing Interaction

Clothing should react to:

- body volume;
- joint articulation;
- gravity;
- compression;
- stretch;
- seams;
- straps;
- sitting/leaning/contact.

Examples:

- elbow bend creates compression on the inside and tension outside;
- seated trousers/skirts compress at seat/hips;
- backpack straps indent clothing/shoulders slightly;
- sleeves and hems respond to arm position and wind.

Avoid clothing that floats a uniform distance off the body.

## 6. Hand/Object Interaction

Hands touching objects must show:

- contact point agreement;
- finger wrap matching object geometry;
- pressure/compression where plausible;
- object weight consistent with wrist/arm posture;
- no interpenetration;
- no hovering fingertips unless intentionally barely touching.

For product imagery, preserve exact product geometry before adding hand contact.

## 7. Wind

Wind is a shared environmental field.

If wind affects one element, check whether it should affect others:

```text
hair
loose clothing
flags
foliage
dust
rain
smoke
sand
lightweight props
```

Wind effects need not be identical, because mass/shape/anchoring differ.

Hard rule:

```text
shared direction does not mean identical deformation
```

## 8. Water and Moisture Interaction

Water should obey:

- gravity;
- surface slope;
- capillary/absorption differences conceptually;
- splash direction;
- pooling geometry;
- material-specific wetness.

Examples:

- wet fabric darkens/clings differently from dry fabric;
- skin can show localized moisture/specular changes;
- pavement gains stronger reflections;
- water trails downward unless motion changes them.

Avoid random droplets distributed uniformly regardless of orientation.

## 9. Dust, Sand, Snow, Smoke, and Particles

Particle behavior should depend on:

- gravity;
- airflow;
- motion source;
- density;
- particle size;
- lighting direction;
- depth.

Examples:

- wheel spin throws dust/sand from the contact zone;
- footsteps disturb loose surface material;
- backlight can reveal dust without requiring volumetric beams everywhere;
- distant particles lose contrast/definition.

## 10. Object Placement and Stability

Objects should have plausible support and center-of-mass logic.

Check:

- chair legs on floor;
- cups/plates stable on tabletop;
- stacked objects not balancing impossibly;
- vehicles aligned with terrain;
- hanging objects follow gravity unless wind/motion explains deviation.

## 11. Compression and Soft Surfaces

Soft surfaces may deform where loaded:

- cushions;
- mattresses;
- upholstered furniture;
- soft ground;
- foam;
- clothing layers.

Do not apply the same deformation amount to all materials.

## 12. Footprints, Tracks, and Disturbance

Secondary evidence should match:

- direction of travel;
- number of feet/wheels;
- scale;
- surface type;
- freshness;
- subject position.

Avoid decorative tracks that fail to connect with the visible action.

## 13. Environmental Continuity

The environment should affect the subject and vice versa.

Examples:

- desert dust on lower vehicle/body zones;
- snow accumulation on upward-facing surfaces;
- rain wetting exposed regions;
- warm firelight strongest on source-facing areas;
- foliage occlusion/cast shadows matching placement.

## 14. Contact in Commercial / Clean Imagery

Pristine imagery may intentionally suppress dirt and wear, but must retain:

- support geometry;
- plausible contact shadow;
- weight;
- reflection/contact consistency;
- realistic hand/product interaction if present.

Do not add grime solely to make a clean commercial frame look real.

## 15. Contact in Reality Repair

Repair order:

```text
1. preserve identity/product/pose/composition locks
2. locate support and contact points
3. correct interpenetration / floating geometry
4. restore weight / compression / posture
5. restore contact shadows and reflections
6. restore terrain/material displacement
7. add transfer/particles only when justified
8. verify shared environmental forces
```

## 16. Reference Match

From a still reference, infer observable interaction only:

- pressed vs hovering;
- wind direction;
- wet/dry;
- soft/hard terrain;
- approximate weight impression;
- displaced particles.

Do not claim measured wind speed, object mass, moisture percentage, or force unless supplied.

## 17. Contact / Gravity Reality Gate

Ask:

1. What supports each major subject/object?
2. Is weight transferred visibly and plausibly?
3. Are feet, tyres, hands and props actually touching where intended?
4. Do soft materials compress where loaded?
5. Do clothing folds follow posture and contact?
6. Do particles/disturbance originate from plausible interactions?
7. Is wind direction coherent across affected elements?
8. Does moisture follow gravity and material behavior?
9. Are contact shadows/reflections consistent with geometry?
10. Is any dirt/deformation being added merely as realism decoration?

Hard rules:

```text
contact shadow != contact geometry
weight must have support
wind is shared but material-dependent
environment interaction must have a cause
clean imagery can remain pristine
```

Acceptance: PASSED
