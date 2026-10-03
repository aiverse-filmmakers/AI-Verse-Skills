# Motion and Shutter Language for Still Frames

Status: RUNTIME KNOWLEDGE
Task: 3.7

This reference defines how the Cinematic Realism Director represents motion, frozen action, subject blur, camera blur, and shutter-language cues in a single still image.

The skill remains a still-image system. It may describe the photographic consequences of motion inside one frame, but it does not become a temporal video-directing engine.

Use after:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`

## 1. Core Principle

Motion blur is not a decorative cinema effect.

A still frame should imply a believable relationship between:

```text
subject motion
camera motion
exposure duration / shutter behavior
camera-to-subject distance
focal length / field of view
motion direction
focus strategy
scene brightness
```

The correct question is:

> What was moving relative to the camera during the exposure, and how should that motion appear in the frame?

## 2. Motion State Classes

Use one of these conceptual states:

### Frozen motion

Use when:

- action must read crisply;
- sports/stunt/product splash detail matters;
- a decisive instant is the storytelling goal;
- user explicitly wants no blur.

Behavior:

- moving subject edges remain defined;
- clothing/hair/liquid may retain shape complexity without smearing;
- do not add arbitrary motion trails;
- camera geometry remains stable unless a different effect is requested.

### Subtle natural motion

Use when:

- a still should feel alive rather than frozen like a mannequin;
- walking, gestures, wind, water, hair, fabric, traffic, or handheld capture benefits from slight movement cues.

Behavior:

- blur remains localized to actually moving components;
- the static environment stays comparatively stable;
- motion direction matches anatomy/physics;
- the primary subject may remain mostly readable.

### Moderate subject motion blur

Use when:

- movement energy matters more than perfect detail;
- the frame should communicate running, dancing, cycling, traffic, crowds, or fast gestures;
- the user asks for a slower-shutter feel.

Behavior:

- moving regions elongate in the direction of motion;
- static geometry remains stable if camera is locked;
- multiple body parts may show different blur amounts because velocities differ;
- blur should not become a uniform halo around the whole person.

### Camera-motion blur

Use when:

- intentional pan/drag/handheld smear is part of the photographic strategy;
- the camera itself moves during the exposure.

Behavior depends on the motion type:

- pan: background streaks roughly opposite apparent subject travel while tracked subject may remain more stable;
- vertical/diagonal drag: scene streak direction follows camera movement;
- handheld: small irregular blur may affect much of the frame;
- rotational camera movement: blur direction varies spatially around a center rather than becoming one flat linear smear.

### Long-exposure / accumulated motion

Use when:

- light trails, water smoothing, moving crowds, vehicle paths, or intentional temporal accumulation are the actual concept.

This is a specialty state, not a cinematic default.

## 3. Subject Motion vs Camera Motion

Always distinguish:

```text
subject moves, camera stable
camera moves, subject stable
camera tracks moving subject
both move independently
```

These produce different photographic results.

### Subject moves, camera stable

- background remains stable;
- moving subject parts blur according to speed/direction;
- contact points may remain sharper during phases of slower motion.

### Camera moves, subject stable

- subject and background may both blur according to camera displacement;
- blur should have spatially coherent direction/rotation.

### Camera tracks moving subject

- tracked subject can remain relatively sharp;
- background exhibits directional streaking;
- extremities may still blur because they move relative to the tracked torso/object.

### Both move independently

Use only when the scene calls for a deliberately unstable/kinetic result. Keep the physics coherent rather than layering random blur styles.

## 4. Shutter Language

AI image generation often cannot literally simulate a measured shutter speed or shutter angle. Treat numerical shutter settings as user locks or photographic references, then translate them into observable behavior.

Examples:

```text
fast shutter intent
-> crisp moving edges, minimal travel during exposure

moderate shutter intent
-> small physically directional movement on faster body parts

slow shutter intent
-> visible accumulated motion while static elements remain stable if camera is fixed
```

Do not claim that a generated image was literally exposed at `1/48 s`, `1/1000 s`, or a specific shutter angle unless the value is simply part of the user's requested simulation/specification.

## 5. Still-Frame Use of Motion-Cinema Vocabulary

Terms such as `180-degree shutter` come from motion-picture capture. In this still-image skill they may be used only as an intended motion-rendering reference.

Do not turn the skill into a video timing system.

Safe translation:

```text
natural cinematic movement rendering
moderate realistic motion smear on moving extremities
not hyper-crisp sports freeze
```

If the user asks for a single image from an imagined film sequence, represent only the appearance of that frozen frame.

## 6. Directionality

Motion blur must have a direction justified by motion.

Check:

- hand swing direction;
- leg/foot direction;
- wheel rotation/tangential movement;
- vehicle travel;
- hair movement from wind/body movement;
- fabric trailing direction;
- water/particle travel;
- pan direction.

Avoid blur that radiates equally around an object unless the intended motion actually causes radial/zoom-like behavior.

## 7. Differential Motion

Real moving subjects rarely blur uniformly.

Examples:

### Walking person

- torso/head may remain relatively stable;
- hands and feet can move faster and blur more;
- coat hem/hair may lag or flutter.

### Running person

- extremities may show stronger directional blur;
- torso can remain more readable if camera tracks;
- feet near impact may momentarily appear sharper than mid-swing feet.

### Dancer

- hands, fabric, hair and limbs can trace different arcs;
- face may remain relatively stable if movement is choreographed around it.

### Vehicle

- body may remain sharp during a tracking pan;
- environment streaks;
- wheels need rotational cues consistent with vehicle motion;
- do not create unrelated radial blur around the entire car.

## 8. Wind Motion

Wind should affect physically exposed elements:

```text
hair
loose clothing
foliage
dust
fabric banners
steam/smoke
```

Do not use generic blur to communicate wind if the actual objects should primarily change shape/orientation rather than smear.

For portraits, individual flyaway hairs may move differently while the core hairstyle remains coherent.

## 9. Water and Particles

### Frozen droplets

Use for crisp splash/product/sports imagery when each droplet matters.

### Moderate water motion

Allow short directional streaks consistent with gravity/throw direction.

### Long exposure water

Use continuous/silky accumulation only if long-exposure intent is explicit.

Dust, sparks, rain, snow and debris should likewise match exposure intent and gravity/wind.

Do not mix crisp suspended particles with strong long-exposure smears without a reason.

## 10. Human Faces and Motion

Avoid motion blur that destroys identity unintentionally.

If the frame's goal is a recognizable portrait within action:

- preserve the face sufficiently;
- place stronger blur on faster limbs/hair/clothing;
- use tracking-camera logic if appropriate.

If the user wants deliberate face smear or anonymous motion, that can be an explicit creative choice.

## 11. Camera Shake

Handheld photography does not automatically mean blurred photography.

If slight camera shake is desired:

- use restrained directional/irregular edge movement;
- keep it compatible with focal length and exposure intent;
- do not add heavy whole-frame smear merely because the shot is `handheld`.

A crisp handheld frame is completely plausible.

## 12. Panning

For a panning still:

- tracked subject stays relatively more stable than environment;
- background streak direction should be coherent;
- streak strength can vary with distance and angular velocity;
- wheels/limbs may retain their own relative motion blur;
- the blur should reinforce travel direction.

This is useful for automotive, cycling, running, and action imagery.

## 13. Zoom Blur

Zoom blur is a specialty optical/camera effect.

Use only if explicitly requested or strongly justified by experimental intent.

Behavior:

- streaks radiate around an optical center;
- stationary geometry appears stretched radially;
- it should not be confused with subject movement or a normal pan.

Never add zoom blur merely because the image should feel energetic.

## 14. Long-Exposure Light Trails

Use only when:

- bright moving lights traverse the scene during a long exposure;
- the camera is sufficiently stable, unless a deliberate camera movement is part of the concept.

Static buildings/road surfaces should remain stable in a tripod-style long exposure.

Do not create free-floating neon trails unrelated to moving luminous sources.

## 15. Motion and Focus

Motion blur and defocus are different phenomena.

An object can be:

```text
in focus + motion blurred
out of focus + stationary
out of focus + motion blurred
in focus + frozen
```

Do not use soft focus to substitute for movement.

Do not use directional motion blur to substitute for depth-of-field falloff.

The two systems must remain independently coherent.

## 16. Motion and Lens/Focal Relationship

At longer focal lengths, small angular camera movement can become visually more consequential for framing/shake. At wider fields of view, the same physical camera displacement may appear less dominant.

Do not turn this into a universal blur formula. Use it qualitatively when selecting believable camera-motion strength.

Camera distance also matters for apparent subject travel across the frame.

## 17. Motion and Environment

Static scene elements should normally remain static when the camera is static.

Reject:

- smeared building edges while only a runner moves;
- blurred floor/walls with a stable camera and localized subject motion;
- direction changes across a single moving limb with no rotation/arc explanation;
- static shadows displaced independently from their moving objects.

If camera motion is present, whole-scene blur must remain geometrically consistent.

## 18. Shadows During Motion

Shadows are part of motion coherence.

For short exposure/frozen motion:

- shadow geometry should correspond closely to the subject's captured position.

For longer exposure:

- a moving subject and its shadow may both accumulate/soften along their respective geometric paths;
- the shadow must still follow light direction and surface geometry.

Do not render a crisp person with a randomly smeared shadow unless the lighting/exposure explains it.

## 19. Reflections During Motion

Reflections must track the moving subject according to reflective geometry.

Examples:

- moving car reflected in wet road/window should show compatible motion direction;
- panned subject reflection should not remain frozen if the reflected image also moves across the sensor;
- long-exposure light trails may appear in wet reflections with geometrically plausible displacement.

## 20. Motion for Different Purposes

### Narrative drama

Use blur only when it supports urgency, disorientation, memory, violence, or natural movement.

### Documentary

Prefer plausible incidental movement rather than stylized streaks unless the actual capture concept calls for them.

### Commercial/product

Default toward controlled clarity; introduce motion cues deliberately around liquids, particles, fabric, hands, vehicles, or dynamic usage.

### Automotive

Tracking pans, wheel motion, road/environment streaking and crisp-car/blurred-background relationships are strong options when justified.

### Fashion/editorial

Can use controlled body/fabric blur for gesture and energy, but keep silhouette/anatomy intentional.

### Travel/street

Moderate pedestrian/traffic blur can express lived movement while preserving place.

### Architecture/interiors

Default to static unless people/traffic/weather are intentionally part of the story.

## 21. Reference Matching

From a still reference, infer observable motion signatures only:

- frozen action;
- localized hand/limb blur;
- panning background;
- camera shake;
- long-exposure accumulation;
- light trails;
- wind-driven movement;
- water/particle rendering.

Do not claim exact shutter speed from appearance alone unless metadata supports it.

## 22. Provider Translation

If a provider exposes motion-blur controls, map the universal intent into them.

Possible categories include:

```text
none
subtle subject motion
moderate subject motion
camera motion
panning feel
long exposure
light trails
zoom blur
```

If the provider has no native control, encode observable effects in prose.

Never fabricate unsupported shutter controls.

## 23. Anti-AI Motion Failures

Reject or repair:

- blur equally surrounding all sides of a moving subject;
- body parts streaking in impossible directions;
- static environment blur with a stable camera;
- wheel blur inconsistent with travel direction;
- sharp reflection of a strongly blurred moving subject without geometric reason;
- motion-smear shadow disconnected from the object;
- random duplicated limbs presented as motion;
- multi-exposure ghost copies when only normal motion blur was requested;
- arbitrary speed lines;
- inconsistent motion directions across rain/snow/dust;
- subject blur and background blur that imply incompatible camera states.

## 24. Runtime Decision Template

Reason internally as:

```text
ACTION
what is moving?
which parts move fastest?
what direction?

CAMERA
static | tracking | panning | handheld | deliberate drag | long-exposure stable

MOTION INTENT
frozen | subtle natural | moderate subject blur | camera blur | long exposure

FOCUS
what remains in focus?

ENVIRONMENT
what must remain stable?

VERIFY
do motion, shadows, reflections, particles, and camera state agree?
```

## 25. Hard Rules

```text
cinematic != motion blur
handheld != blurry
motion blur != defocus
slow shutter != random smear
fast action != mandatory blur
pan != whole-frame uniform blur
long exposure != neon trails without moving lights
motion effect != speed-line graphic design
still-frame shutter language != temporal video direction
reference blur != exact shutter metadata
```

## 26. Motion Reality Gate

Before finalizing:

1. What is moving relative to the camera?
2. Is blur direction physically consistent with that motion?
3. Are faster and slower body/object regions differentiated plausibly?
4. Is the camera static, tracking, panning, or moving, and does the whole frame agree?
5. Do focus and motion blur remain separate coherent systems?
6. Do shadows agree with moving geometry and light direction?
7. Do reflections agree with motion?
8. Do particles/water/hair/fabric follow plausible direction and exposure behavior?
9. Are static elements preserved when they should be?
10. Has the skill avoided decorative motion blur where crisp capture better serves the shot?

If not, revise before output.
