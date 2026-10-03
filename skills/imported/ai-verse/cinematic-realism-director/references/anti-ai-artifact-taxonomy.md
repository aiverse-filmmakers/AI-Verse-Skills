# Anti-AI Artifact Taxonomy

Status: RUNTIME KNOWLEDGE
Task: 5.1

This taxonomy gives Reality Repair a structured vocabulary for diagnosing why a still image feels synthetic, overprocessed, physically inconsistent, or generically AI-generated.

Use with:

- `schemas/realism-diagnosis.schema.json`
- `references/motivated-lighting.md`
- `references/exposure-and-dynamic-range.md`
- `references/aperture-focus-and-depth.md`
- `references/focal-length-and-perspective.md`
- `references/texture-effects-restraint.md`

## 1. Governing Principle

Do not repair an image merely because it looks polished, stylized, symmetrical, clean, or unusual.

Diagnose only against the user's requested realism/stylization target.

The system should ask:

```text
What is visually implausible?
What evidence supports that diagnosis?
What must be preserved?
What is the smallest repair that fixes the failure?
```

Avoid:

```text
AI-looking -> regenerate everything
```

## 2. Severity Scale

Use qualitative severity:

### S0 - none
No meaningful realism failure.

### S1 - subtle
Noticeable under inspection but not immediately synthetic.

### S2 - moderate
Clearly harms photographic plausibility.

### S3 - strong
Immediately reads artificial or physically inconsistent.

### S4 - structural
Core geometry/identity/scene logic is broken enough that local repair may not be sufficient.

Severity is not permission to alter preservation locks.

## 3. Diagnostic Domains

Every finding should belong to one or more domains:

```text
anatomy / geometry
skin
hair
eyes
fabric
materials / roughness
reflections / refractions
lighting
shadows
exposure / tone
color
perspective
focus / depth
motion
contact / gravity
atmosphere
environment
texture / grain
optical effects
repetition / pattern
text / symbols
composition / scene logic
```

## 4. Skin Artifacts

Common failures:

- waxy/plastic surface;
- globally airbrushed texture;
- identical pore texture across regions;
- pores pasted over flat lighting;
- over-sharpened pores;
- uniform orange/peach hue;
- beauty smoothing inconsistent with age/context;
- synthetic wet sheen;
- specular highlights disconnected from source direction;
- no local redness/cool variation;
- face and body skin rendered as different materials;
- makeup melted into skin texture;
- extreme microtexture used to compensate for smoothness.

Repair priority:

```text
light-material coherence
-> tonal/color variation
-> region-specific texture
-> age/context appropriate detail
```

Not:

```text
add more pores everywhere
```

## 5. Symmetry and Beautification Artifacts

Potential symptoms:

- unnaturally mirrored facial features;
- identical eye highlights when source geometry would differ;
- perfectly matched hair on both sides;
- over-idealized jaw/cheek/nose proportions that conflict with identity reference;
- all facial irregularity removed;
- excessively centered or posed body geometry in a supposedly candid scene.

Caution:

Symmetry itself is not an error. Diagnose only when it conflicts with identity, pose, source geometry, or intended candid realism.

## 6. Hair Artifacts

Common failures:

- every strand individually rendered with equal clarity;
- spaghetti-like separated strands;
- impossible strand intersections;
- floating wisps disconnected from hair mass;
- hair fused into clothing/skin;
- hair volume inconsistent with gravity;
- wind direction inconsistent across hair/wardrobe/environment;
- glossy plastic hair;
- identical repeated curls;
- hairline too perfect or painted;
- flyaways that unnaturally extend/break apparent hair length.

## 7. Eye Artifacts

Common failures:

- glass-marble eyes;
- overbright sclera;
- identical catchlights despite different eye angles;
- catchlights from non-existent sources;
- iris texture too radial/perfect;
- excessive sharpness compared with surrounding face;
- pupils inconsistent in size/lighting;
- reflections not conforming to corneal curvature;
- both eyes independently optimized to camera rather than sharing gaze direction;
- eyelids/lashes not wrapping eye geometry.

## 8. Anatomy and Geometry Artifacts

Examples:

- malformed fingers/hands;
- fused or duplicated limbs;
- impossible joint bends;
- inconsistent shoulder/hip geometry;
- asymmetric limb lengths without perspective explanation;
- duplicated teeth;
- impossible ear attachment;
- glasses/jewelry intersecting anatomy;
- clothing passing through body;
- object geometry changing across its surface;
- impossible perspective junctions;
- background architecture with broken vanishing logic.

Structural anatomy failures often require a different repair strategy than surface-texture failures.

## 9. Fabric Artifacts

Common failures:

- cloth too smooth/plastic;
- weave equally visible at all distances;
- arbitrary folds unrelated to gravity/compression;
- folds that terminate unnaturally;
- fabric penetrating body;
- clothing hovering above body;
- identical repeated wrinkles;
- material type and roughness inconsistent with garment;
- embroidered/printed details melting or repeating;
- wind response inconsistent with hair/environment.

## 10. Material / Roughness Artifacts

Symptoms:

- every object shares the same glossy finish;
- metal looks like gray plastic;
- plastic looks like polished metal;
- wood grain ignores geometry;
- stone has uniform procedural noise;
- leather lacks compression/crease behavior;
- glass reflections do not match environment;
- wet surfaces lack coherent roughness/reflection changes;
- skin, fabric, and hard surfaces share identical specular size.

Material identity is largely visible through light response, not texture labels alone.

## 11. Reflection Artifacts

Common failures:

- reflected content absent from the scene;
- reflection direction inconsistent with camera/viewpoint;
- mirror image geometry impossible;
- car/body reflections painted for beauty rather than environment;
- glass reflecting light from the wrong side;
- puddles reflecting unrelated sky/buildings;
- reflected subject pose different from actual subject;
- rough surfaces acting like perfect mirrors.

## 12. Refraction / Transparency Artifacts

Examples:

- glass has no distortion/refraction where thickness/shape implies it;
- liquid boundary geometry inconsistent;
- transparent materials render like opacity masks;
- background through glass does not align spatially;
- bottle contents ignore container curvature;
- lenses/windows alter objects inconsistently.

## 13. Shadow Artifacts

Common failures:

- multiple incompatible shadow directions;
- shadow softness inconsistent with source size;
- missing contact shadow;
- floating shadow detached from subject;
- cast shadow shape unrelated to object;
- face lighting direction conflicts with body/environment shadow;
- ambient occlusion painted excessively into every crease;
- shadows too uniformly black despite environment fill.

## 14. Lighting Artifacts

Examples:

- arbitrary perfect rim light;
- unexplained frontal beauty light in a dark scene;
- every object separately lit for visibility;
- colored edge light without source;
- impossible source direction changes across surfaces;
- visible volumetric beam without atmosphere;
- candle illuminating a huge room evenly;
- hard-sun environment with soft undefined cast shadows.

## 15. Exposure and Tonal Artifacts

Common failures:

- excessive HDR/local tone mapping;
- halos around high-contrast edges;
- every region perfectly exposed;
- bright practical core artificially recovered;
- gray lifted blacks with no density;
- crushed shadows inconsistent with broad ambient illumination;
- highlight clipping occurring as flat digital patches;
- local contrast exaggerated independently across surfaces.

## 16. Color Artifacts

Examples:

- universal teal/orange regardless of sources;
- skin uniformly orange;
- equal cyan/magenta bilateral lighting with no set sources;
- neon colors clipped into flat patches;
- shadows all cyan regardless of ambient environment;
- inconsistent white balance across objects under same light;
- locked product color shifted for style.

## 17. Perspective Artifacts

Common failures:

- face/hand/object scale relationships impossible for camera position;
- local fisheye warp in only one object without optical logic;
- architecture verticals bending inconsistently;
- foreground scale exaggerated but background does not follow same projection;
- multiple incompatible vanishing systems;
- OTS geometry where shoulder/subject placement cannot coexist physically;
- top-down image that is not actually 90-degree down despite request.

## 18. Focus / Depth Artifacts

Examples:

- fake segmentation blur around hair/ears;
- foreground and background equally blurred despite different distances;
- razor-sharp eyes with blurred nose/ears inconsistent with the stated aperture/distance;
- multiple separated focus planes without tilt/specialty explanation;
- background bokeh shape unrelated to lens/depth logic;
- uniform Gaussian blur rather than optical defocus;
- whole scene shallow merely because it is labeled cinematic.

## 19. Motion Artifacts

Common failures:

- random directional smear;
- face blurred but hair/clothes frozen inconsistently;
- panning where subject and background blur relationships are reversed;
- moving object reflection/shadow frozen inconsistently;
- motion blur on static architecture with a supposedly fixed camera;
- every moving body part blurred identically despite different velocities.

## 20. Contact / Gravity Artifacts

Examples:

- floating feet/objects;
- no compression where body/object meets soft surface;
- hand resting without contact deformation;
- vehicle tires not bearing weight;
- footprints missing from deformable surface when expected;
- cloth hanging against gravity;
- liquid/dust/sand interaction absent around contact;
- props hovering millimeters above support.

## 21. Environment Artifacts

Common failures:

- overclean lived-in environment;
- repeated background people/objects;
- identical leaves/windows/bricks;
- perspective/scale drift across architecture;
- environmental weather does not affect subjects/materials;
- dust/rain/snow appears as uniform overlay;
- distant elements have same contrast/sharpness as foreground;
- scene objects lack wear/contact history where context implies it.

## 22. Atmosphere Artifacts

Examples:

- visible light beams in clean air;
- haze uniformly applied without depth;
- atmospheric perspective not increasing with distance;
- fog occludes foreground/background equally;
- dust particles lit from incompatible directions;
- rain/snow scale/direction inconsistent with scene.

## 23. Grain / Texture Artifacts

Common failures:

- uniform noise overlay;
- grain identical at all depths/scales;
- grain sharper than focused image detail;
- excessive pore/fabric texture hallucination;
- texture copied/repeated across unrelated surfaces;
- oversharpening halos;
- excessive clarity/local contrast;
- artifact stack used to hide poor base realism.

## 24. Optical-Effect Artifacts

Examples:

- mandatory anamorphic blue streak;
- flare with no bright source;
- red halation around non-bright edges;
- bloom around midtones;
- chromatic aberration applied equally across entire frame;
- vintage softness without optical/depth logic;
- strong vignetting unrelated to lens/format intent.

## 25. Repetition / Pattern Artifacts

Common AI clues:

- duplicated faces;
- repeated accessories;
- repeating texture motifs;
- cloned background objects;
- repeated folds/hair curls;
- pseudo-random text-like symbols;
- tiled vegetation/building detail.

Repair should break repetition while preserving scene design.

## 26. Text / Logo / Symbol Artifacts

For real-world commercial/editorial imagery:

- malformed lettering;
- inconsistent logo geometry;
- invented brand marks;
- duplicated labels;
- nonsensical signage;
- typography changing across reflections.

When exact text/product branding is a preservation lock, do not `improve` it creatively.

## 27. Overdone Cinematic Effects

The image may look AI-generated because too many cinematic signifiers are stacked together:

```text
extreme shallow DOF
+ heavy grain
+ halation
+ haze
+ teal-orange
+ rim light
+ anamorphic flare
+ crushed blacks
+ lifted local shadows
+ skin sharpening
```

Repair often means removing effects, not adding realism effects.

## 28. Overclean vs Deliberately Clean

Do not confuse a clean studio/commercial image with an AI artifact.

`Overclean` means contextually implausible absence of natural variation, contact, texture, reflections, wear, micro-shadow, or material response.

A controlled product studio may correctly be pristine.

## 29. Diagnosis Evidence Rule

Every finding should state what is actually visible.

Good:

```text
Both cheek highlights have identical shape/intensity although the key is camera-left; likely synthetic specular response.
```

Weak:

```text
Skin looks AI.
```

The diagnosis schema should record:

- domain;
- severity;
- evidence;
- likely cause when inferable;
- confidence;
- preservation conflict;
- recommended repair.

## 30. Minimal Repair Principle

Repair in this order:

```text
structural impossibility
-> lighting / reflection / shadow inconsistency
-> contact / material response
-> anatomy / identity-local issues
-> depth / motion inconsistency
-> skin / hair / eye surface realism
-> texture / color / effect excess
```

The exact priority may change when the user identifies a more important defect.

Do not redraw the entire scene to fix one flyaway, one reflection, or one plastic-skin region.

## 31. Preservation Boundary

Before any repair identify:

```text
PRESERVE
REPAIR
ALLOW CHANGE
```

Typical preserve targets:

- identity;
- expression;
- pose;
- composition;
- product geometry;
- wardrobe;
- logo/text;
- lighting direction;
- background layout.

If a requested repair conflicts with preservation, use the Task 2.5 conflict system.

## 32. Hard Rules

```text
AI-looking != regenerate everything
realism != add noise
realism != add pores everywhere
clean != fake
symmetry != automatically wrong
stylized != defective
artifact diagnosis requires visible evidence
repair should be narrower than the problem whenever possible
preservation locks outrank aesthetic cleanup
```
