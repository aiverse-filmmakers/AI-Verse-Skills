# Focal Length, Distance, and Perspective

Status: RUNTIME KNOWLEDGE
Task: 3.5

This reference formalizes field of view, camera distance, capture format, perspective, rectilinear projection, and foreground exaggeration. Its purpose is to prevent a common prompting error: treating focal length itself as the cause of perspective distortion.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`

## 1. Hard Rule

Perspective is determined primarily by **camera position relative to the scene**.

Focal length and capture format determine field of view for that camera position.

Therefore:

```text
perspective != focal length alone
```

and:

```text
wide lens != automatic facial distortion
telephoto lens != perspective compression by itself
```

The visual perspective often associated with wide and long lenses usually appears because the photographer moves the camera to a different distance in order to maintain desired framing.

## 2. The Four Variables Must Be Solved Together

For any shot, reason jointly about:

```text
capture format
camera position / distance
focal length
framing / shot size
```

Changing one may require changing another.

Example:

If a close-up must remain the same size in frame:

- a wider lens usually requires moving the camera closer;
- a longer lens usually requires moving the camera farther away;
- the change in camera position changes near/far scale relationships.

That positional change is what creates the familiar `wide-close` versus `long-far` perspective difference.

## 3. Camera Distance Categories

Use physical or relational distance when exact meters are unnecessary.

Useful categories:

```text
extreme proximity
close proximity
conversational distance
medium observational distance
far observational distance
landscape / remote distance
```

For expert users, preserve actual distance when supplied.

Examples:

```text
camera 40 cm from subject [LOCKED]
camera 2.5 m from subject [LOCKED]
```

## 4. Field of View vs Perspective

At a fixed camera position:

- changing focal length changes how much of the scene fits in frame;
- cropping a wider image to match a longer lens can produce the same geometric perspective if the viewpoint did not move;
- optical rendering, resolution, depth of field, and crop quality may differ, but perspective geometry from the viewpoint remains the same.

The skill should use this distinction whenever the user asks for `same perspective but tighter/wider framing`.

## 5. Equivalent Framing Across Formats

The same focal length does not produce the same field of view on every format.

Example:

```text
50mm on Super 35
50mm on full frame
```

are different fields of view from the same camera position.

When a user locks both format and focal length, respect both.

When format is AUTO, choose format/focal pair from the required field of view and depth strategy rather than from prestige value.

Do not use `medium format`, `large format`, `IMAX`, or `65/70mm` as automatic synonyms for `epic cinematic perspective`.

## 6. Wide-Angle Strategy

Wide lenses are useful for:

- spatial context;
- environmental storytelling;
- foreground/background layering;
- energetic proximity;
- architectural or interior coverage;
- immersive POV;
- dramatic foreground scale;
- close camera-to-subject relationships.

Potential risks arise when camera proximity becomes extreme:

- nose/hands/feet near camera grow relative to farther features;
- face depth can appear exaggerated;
- foreground objects can dominate;
- background appears smaller relative to nearby objects;
- edges may feel stretched depending on projection/framing.

Those effects should be intentional, not treated as defects by default.

## 7. Extreme Foreground Distortion Without Fisheye

A key supported look is:

```text
very large foreground object
+ rectilinear background
+ no circular fisheye look
```

Achieve conceptually through:

1. use a very wide **rectilinear** field of view;
2. place the foreground hand/shoe/prop/vehicle nose physically close to camera;
3. keep the main subject farther away;
4. allow near/far scale exaggeration from camera position;
5. preserve straight-line rectilinear behavior in the background where appropriate;
6. explicitly avoid fisheye projection unless requested.

This is the correct mental model for a Laowa-zero-distortion-type wide perspective request.

Do not fake the effect by applying barrel distortion to the whole frame.

## 8. Rectilinear vs Fisheye

### Rectilinear

Goal:

- straight scene lines generally remain straight;
- extreme field of view stretches edges but does not intentionally curve all geometry into a circular projection;
- near/far scale can still be dramatic if camera position is close.

### Fisheye

Goal:

- deliberately non-rectilinear projection;
- strong line curvature;
- often circular or visibly bowed geometry;
- distinctive central/edge spatial warping.

Never use `fisheye` as a synonym for `very wide`.

If the user says `no fisheye`, preserve a rectilinear projection intent even at very short focal lengths.

## 9. Long-Lens Strategy

Longer focal lengths are useful for:

- distant observational framing;
- isolating a subject from a far camera position;
- flattening apparent spatial relationships when the camera is placed farther away for equivalent framing;
- layering distant background planes;
- minimizing intrusive close-camera perspective;
- elegant portrait framing;
- distant automotive/sports/environment shots.

Important wording:

Do not say the lens itself `compresses perspective` as a standalone physical cause.

For equivalent subject framing, the longer focal length typically moves the camera farther away. That farther viewpoint reduces relative near/far size differences and produces the familiar compressed appearance.

## 10. Portrait Perspective

When realism matters, solve portrait perspective from camera distance first.

### Intimate / energetic portrait

May use:

- closer camera;
- wider-normal field of view;
- stronger environmental relationship;
- more pronounced near/far facial/hand scale if desired.

### Neutral portrait

Use a camera distance that keeps facial proportions plausible and comfortable for the intended framing.

### Detached / elegant portrait

May use:

- farther camera position;
- longer field of view;
- reduced foreground exaggeration;
- cleaner subject/background separation.

Do not automatically assign 85mm to every portrait.

## 11. Product Perspective

Product shape accuracy can be more important than dramatic proximity.

When geometry must remain faithful:

- avoid unnecessarily close camera placement;
- use focal length and distance jointly to control shape relationships;
- maintain verticals/horizontals when required;
- allow controlled wide foreground exaggeration only when it is part of the commercial concept.

For bottles, watches, phones, vehicles, furniture, and architecture, perspective can materially change perceived proportions.

## 12. Automotive Perspective

Automotive shots commonly use two distinct strategies:

### Hero proximity

```text
wide or wide-normal field of view
camera physically close to front/rear quarter
large near wheel / grille / body plane
strong depth into the vehicle
rectilinear geometry unless stylization requested
```

### Distant elegance

```text
farther camera
longer focal length
more even vehicle proportions
background planes appear more layered/compressed
less near/far exaggeration
```

Neither is universally more cinematic.

## 13. Architecture and Interiors

For architecture/interiors:

- field of view may need to be wide because physical space limits camera distance;
- preserve verticals unless a deliberate tilt/keystone effect is intended;
- distinguish perspective convergence from barrel/fisheye distortion;
- do not invent impossible room dimensions to make a wide view fit;
- avoid `ultra wide` prompts that turn straight geometry into a curved CGI room unless requested.

If a top-down or orthographic-like result is requested, camera orientation and projection intent matter more than merely choosing a short focal length.

## 14. Over-the-Shoulder Perspective

For OTS shots, perspective must preserve the physical relationship among:

```text
foreground shoulder/head
camera
primary subject
background
```

A wide-close OTS can make the foreground shoulder very large and immersive.

A longer/farther OTS makes the foreground less dominant and more observational.

When matching a frozen reference moment, changing focal/distance must not move the subjects themselves unless the user permits scene reblocking.

## 15. Top-Down Perspective

True 90-degree top-down means the camera optical axis points straight toward the ground/subject plane.

Do not simulate it merely by using a wide lens from a high oblique angle.

Focal length controls coverage; camera height determines how much area fits and how large objects appear.

## 16. Macro / Close-Up Perspective

Macro or extreme close-up framing can introduce unusual spatial relationships because camera distance is extremely short.

Do not use `macro` simply to mean `high detail`.

Macro intent affects:

- camera distance;
- depth-of-field behavior;
- working distance;
- relative scale;
- material texture visibility.

Task 3.6 handles the depth consequences.

## 17. Perspective Matching from a Reference

When reverse-engineering a reference, infer observable geometry first:

```text
strong near/far scale exaggeration
neutral perspective
far-camera compressed relationships
wide environmental field of view
close camera position
high camera position
```

Exact focal length is usually a hypothesis unless metadata or reliable context exists.

Safe output:

```text
wide-normal field of view from close camera position
```

Less safe without evidence:

```text
exactly 28mm
```

Use confidence semantics from `references/confidence-and-uncertainty.md`.

## 18. Perspective and Lens Character Must Stay Separate

A vintage 35mm lens and a modern 35mm lens can share field of view while rendering contrast, flare, bokeh, chromatic behavior, and edge definition differently.

Therefore:

```text
perspective system -> camera position + format + focal + framing
optical character system -> lens design / family
```

Do not conflate them.

## 19. Perspective and Depth of Field Must Stay Separate

Perspective and DOF interact through camera position/focal/aperture choices, but they are not the same variable.

A wide environmental shot does not have to be deep focus.

A long lens does not guarantee shallow focus.

Task 3.6 solves aperture/focus/depth explicitly.

## 20. Conflict Examples

### 14mm + `no wide-angle distortion`

Interpretation:

- keep the 14mm lock;
- understand whether the user means no fisheye/barrel distortion or no close-camera perspective exaggeration;
- prefer rectilinear projection;
- increase camera distance where framing allows;
- keep important faces away from extreme edge stretch;
- if equivalent framing requires close proximity, explain the unavoidable perspective trade-off rather than silently changing focal length.

### 200mm + immersive near-camera foreground

Potential tension:

- a 200mm field of view normally encourages a farther camera for useful framing;
- if the user also wants an enormous near-camera hand/object, the geometry may require a separate foreground plane, unusual staging, composite logic, or changed distance.

Do not silently turn 200mm into 20mm.

### Same frozen scene, different camera angle

Preserve:

- people;
- poses;
- gaze;
- props;
- environment;
- moment/timecode.

Change only:

- camera position;
- camera height/angle;
- focal length if needed to achieve target framing.

## 21. Prompt Translation

Good provider-neutral language describes the relationship:

```text
camera placed very close to the foreground hand, wide rectilinear field of view, hand becomes dramatically larger than the subject behind it, straight architectural lines remain rectilinear, no fisheye projection
```

Better than:

```text
10mm distorted cinematic lens
```

For a distant portrait:

```text
camera positioned well back from the subject, narrow field of view, restrained near/far scale difference, layered background planes
```

rather than relying only on:

```text
135mm compression
```

## 22. Perspective Reality Gate

Before accepting a shot, verify:

```text
[ ] camera position is physically plausible
[ ] focal length and format can produce requested field of view
[ ] framing follows from distance + field of view
[ ] near/far scale relationships match camera position
[ ] wide perspective is not automatically converted into fisheye
[ ] straight geometry remains coherent when rectilinear is requested
[ ] facial/object proportions are intentional
[ ] top-down angle is truly top-down when requested
[ ] reference-match focal claims do not exceed evidence
[ ] no lock was silently changed
```

## 23. Failure Patterns

Reject these shortcuts:

```text
14mm = fisheye
24mm = distorted face
85mm = perfect portrait
135mm = cinematic compression
large format = epic perspective
IMAX = shallow DOF
telephoto = compressed perspective regardless of camera position
wide lens = curved background
macro = more detail
```

Use camera geometry, not lens mythology.
