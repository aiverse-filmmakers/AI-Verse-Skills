# Fabric and Material Realism

Status: RUNTIME KNOWLEDGE
Task: 5.4

This reference defines how cloth and non-skin materials should behave in a believable still image. It is used by AUTO generation, Reality Repair, Reference Match, and the Reality Gate.

Use with:

- `references/anti-ai-artifact-taxonomy.md`
- `references/motivated-lighting.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `schemas/realism-diagnosis.schema.json`

## 1. Governing Principle

Material identity is not primarily a texture label.

A material reads as believable through the combined behavior of:

```text
shape
surface roughness
microstructure
specular response
reflection / refraction
transmission / translucency
fold / deformation behavior
weight
wear
contact
lighting
view angle
```

Do not fix material realism by adding procedural texture everywhere.

## 2. Scale Coherence

Detail must change with viewing distance.

### Near / macro
May reveal:

- weave;
- pores in leather;
- brushed metal direction;
- fine scratches;
- dust;
- fingerprints;
- fiber fuzz;
- micro-abrasion.

### Medium distance
Prefer:

- material-level roughness;
- fold structure;
- broad specular shape;
- seams;
- wear zones;
- larger grain pattern.

### Far distance
Microtexture should collapse into tonal/material behavior rather than remain equally sharp.

Hard rule:

```text
microdetail visibility must respect image scale and focus
```

## 3. Fabric System

Fabric realism depends on:

```text
fiber / weave family
thickness
weight
stiffness
stretch
surface sheen
compression
fold wavelength
seams / construction
body interaction
wind / gravity
```

### Lightweight fabric
Examples: chiffon, thin cotton, silk-like cloth.

Possible behavior:

- finer folds;
- faster response to airflow;
- lower apparent mass;
- more translucency where appropriate;
- soft edge layering.

### Medium-weight fabric
Examples: jersey, shirt cotton, standard wool blends.

Possible behavior:

- folds organized around joints, tension and gravity;
- visible compression at seated/contact areas;
- moderate drape.

### Heavy/stiff fabric
Examples: denim, canvas, thick wool, structured outerwear.

Possible behavior:

- broader folds;
- slower curvature changes;
- visible crease memory;
- stronger structure away from the body;
- greater resistance to wind.

Do not assign exact textile physics when the material is unknown. Use observed behavior and confidence semantics.

## 4. Fold Logic

Folds should have causes.

Common causes:

- gravity;
- compression;
- body articulation;
- tension between anchor points;
- garment construction;
- wind;
- bunching;
- object contact.

Repair rule:

> Trace each major fold family back to a plausible force or construction point.

Avoid:

- repeated decorative wrinkles;
- isolated folds that start/end without force;
- equal fold density across every garment region;
- cloth hovering above the body;
- folds ignoring elbows, knees, waist, shoulders or seat contact.

## 5. Weave and Fiber Visibility

Weave/fiber is optional, not mandatory.

Use only when supported by:

- distance;
- resolution;
- material family;
- focus;
- lighting angle;
- user intent.

Do not make every garment look coarse merely to signal realism.

## 6. Anisotropy

Some surfaces reflect light directionally because their microstructure has orientation.

Useful examples:

- brushed metal;
- satin/silk-like fabric;
- hair-like fibers;
- some machined surfaces.

Generative translation should describe the visible consequence:

```text
directional elongated highlight following the brushed grain
```

rather than requiring a renderer-specific anisotropy parameter.

## 7. Leather

Believable leather may include:

- nonuniform grain;
- crease concentration near flex/compression zones;
- moderate specular response varying with finish;
- edge wear at handles/corners/seams;
- compression and bending consistent with thickness.

Avoid:

- uniform orange-peel procedural texture;
- perfectly glossy leather regardless of type;
- random scratches over protected areas.

## 8. Metal

Metal realism requires environment-dependent reflection.

### Polished metal
- sharp/structured reflections depending on roughness;
- bright speculars can approach source intensity;
- reflection shape follows environment and curvature.

### Brushed metal
- directional highlight spread;
- visible grain only at suitable scale;
- softer/refined reflection structure.

### Oxidized / aged metal
- roughness variation;
- oxidation/color changes tied to exposure/contact/history;
- not random rust noise everywhere.

Hard rule:

```text
metal should not read as gray plastic
```

## 9. Glass

Glass may require:

- reflection;
- transmission;
- refraction;
- thickness cues;
- edge highlights;
- occlusion by frames/seals;
- environment-consistent reflections.

Avoid:

- perfectly invisible glass with arbitrary highlights;
- reflections unrelated to the scene;
- impossible doubling/refraction;
- same sharpness for transmitted and reflected layers when geometry suggests otherwise.

## 10. Plastic

Plastic spans matte to highly glossy.

Useful cues:

- molded seams / manufacturing logic where relevant;
- roughness appropriate to finish;
- colored diffuse body response;
- specular highlights distinct from metal;
- scratches/wear concentrated on contact areas.

Do not make all plastic glossy toy material.

## 11. Wood

Wood realism requires:

- grain direction following object construction;
- end grain where geometry exposes it;
- scale-appropriate pattern;
- finish-dependent roughness;
- wear concentrated on handled/exposed zones.

Avoid procedural grain that changes direction arbitrarily across connected surfaces.

## 12. Stone / Concrete / Plaster

These materials usually benefit from:

- nonuniform but low-frequency variation;
- pores/aggregate only at appropriate scale;
- edge wear/chipping where plausible;
- rough diffuse response;
- moisture-driven darkening where wet.

Avoid equal high-frequency noise everywhere.

## 13. Painted Surfaces

Separate:

```text
base substrate
paint layer
surface finish
wear / chips
```

A painted car body is not bare metal. Painted wood is not raw wood.

## 14. Wetness and Moisture

Wet surfaces generally change:

- apparent roughness;
- reflection strength/clarity;
- local darkness/saturation;
- contact behavior;
- drip/flow patterns.

Water effects must obey gravity and local geometry.

Do not add random glossy patches that have no moisture source.

## 15. Dust, Dirt, Fingerprints and Wear

Imperfection should tell a history.

Place wear where contact or exposure makes sense:

- handles;
- edges;
- soles;
- knees/elbows;
- high-touch controls;
- road-facing surfaces;
- horizontal dust-catching surfaces;
- exposed leading edges.

Avoid equal dirt over every part of an object.

## 16. Product Imagery

Commercial product realism may be extremely clean.

Do not force dirt, fingerprints, scratches or wear when:

- the product is new;
- brand presentation requires pristine finish;
- the user asks for clean studio imagery.

Realism still requires:

- coherent reflections;
- plausible contact;
- material separation;
- correct edge highlights;
- realistic roughness transitions.

## 17. Material Separation

Adjacent materials should respond differently to the same light.

Example:

```text
matte fabric -> broad low-intensity response
skin -> diffuse + soft specular variation
polished metal -> strong environment reflection
rubber -> dark diffuse with restrained specular
clear glass -> reflected + transmitted structure
```

If every surface shares the same highlight width/intensity, the image will often read synthetic.

## 18. Reference Match

From a reference, infer only observable material traits such as:

- glossy vs matte;
- soft vs stiff fabric;
- coarse vs fine texture;
- worn vs pristine;
- transparent vs translucent vs opaque;
- broad vs tight specular response.

Do not invent exact material formulation, weave count, coating chemistry, or manufacturing process unless supplied.

## 19. Reality Repair Order

For fabric/material failures:

```text
1. preserve identity / product geometry / wardrobe design
2. correct gross geometry and contact
3. correct light-material response
4. correct roughness / reflection
5. correct folds / deformation
6. add only scale-appropriate microtexture
7. add wear/imperfection only if context supports it
8. verify against lighting and contact systems
```

## 20. Fabric and Material Reality Gate

Ask:

1. Does material identity come from light response as well as texture?
2. Are folds caused by gravity, tension, compression or construction?
3. Does microdetail respect distance and focus?
4. Do adjacent materials respond differently to the same light?
5. Are reflective surfaces consistent with the environment?
6. Does roughness fit the stated material and condition?
7. Does wear occur in plausible locations?
8. Does wetness/dirt have a cause?
9. Are clean products allowed to remain clean?
10. Is any texture being used merely to make the image look less AI-generated?

Hard rules:

```text
realism != more texture
fabric folds require forces
material roughness must affect highlights/reflections
microdetail must respect scale
imperfection must be contextual
clean commercial imagery can still be realistic
```

Acceptance: PASSED
