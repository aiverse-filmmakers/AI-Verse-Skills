# Phase 3 Audit - Core Cinematography Knowledge Base

Status: PASSED
Phase: 3
Branch: `feat/cinematic-realism-director`

## Purpose

Verify that the completed Phase 3 runtime knowledge can design a coherent still-image camera setup from minimal subject + context while preserving expert locks, physical plausibility, and the Phase 0/2 architecture contracts.

Files under audit:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`

Supporting contracts:

- `references/locks.md`
- `references/parameter-conflicts.md`
- `references/confidence-and-uncertainty.md`
- `schemas/cinematic-shot-spec.schema.json`

## Gate Requirement

Phase 3 requires that:

> Given only subject + context, the skill can design a coherent camera setup without generic cinematic filler while preserving expert locks and physical plausibility.

## Audit Method

Test five representative classes:

1. beginner narrative AUTO;
2. commercial/product AUTO;
3. architecture/interior AUTO;
4. action still with motion;
5. expert locked camera setup.

For each case verify:

- story/purpose leads camera decisions;
- framing and blocking are spatially coherent;
- capture format/camera character are not prestige tokens;
- lens character is separated from focal length;
- perspective is driven primarily by camera position;
- aperture/depth serve information hierarchy;
- motion/shutter cues are physically coherent;
- no mandatory shallow DOF, flare, haze, teal/orange, grain, rim light, or anamorphic artifacts appear by default;
- explicit locks remain authoritative.

---

# Case A - Beginner Narrative AUTO

Input:

```text
woman waiting for a taxi in London at night
```

Expected reasoning:

### Intent

Narrative/observational urban waiting moment. Environment matters because London/night context carries story information.

### Composition

A medium or medium-wide observational frame can keep the woman primary while retaining curb, street, practical light, wet pavement/traffic context if present.

### Camera position / perspective

Use a believable human-height or slightly lower observational camera position rather than extreme low/high angle without narrative reason.

### Capture

Provider-neutral modern cinema capture is sufficient. No branded camera is required merely for prestige.

### Lens/focal

Moderate wide-to-normal field of view can preserve person + place. The exact focal choice follows format and camera distance rather than a generic `35mm cinematic` token.

### Depth

Moderate separation: subject readable, city context still recognizable. No automatic f/1.2 blur wall.

### Motion

If taxi/traffic/pedestrians move, slight localized motion may be used. The waiting subject can remain comparatively stable. No arbitrary whole-frame smear.

### Cliche check

Not automatically added:

- anamorphic blue flare;
- teal/orange grade;
- heavy rain/haze;
- extreme grain;
- dramatic rim light;
- razor-thin focus.

Result: PASS.

---

# Case B - Commercial Product AUTO

Input:

```text
premium black wristwatch on a dark stone table for a luxury ad
```

Expected reasoning:

### Intent

Commercial/product hierarchy prioritizes product geometry, material response, dial/branding legibility, surface finish, and controlled premium presentation.

### Composition

Product placement and negative space depend on advertising layout need. Avoid arbitrary portrait-style framing.

### Camera position / perspective

Choose angle/distance to show case, crystal, dial, crown/strap geometry without near-field distortion unless intentional.

### Capture/lens

High-quality neutral capture character and controlled lens rendering are appropriate. A named cinema camera/lens is optional, not required.

### Depth

Moderate/selective focus may isolate the watch, but key branding and hero surfaces must remain readable. Macro detail can become shallower only when the shot becomes a true detail frame.

### Motion

Static by default. No motion blur is added because the image is `cinematic`.

### Cliche check

No mandatory bloom, halation, haze, flare, or dramatic shallow DOF.

Result: PASS.

---

# Case C - Architecture / Interior AUTO

Input:

```text
minimalist concrete hotel lobby in soft morning light
```

Expected reasoning:

### Intent

Architecture/environment is the subject. Spatial legibility dominates.

### Composition

Verticals, horizon, room geometry, circulation, foreground/midground/background relationships, and material surfaces are prioritized.

### Camera position / perspective

Choose a physically plausible camera height/location that reveals the space without forcing fisheye or extreme near-field stretching.

### Focal/format

Wide enough to communicate the room, but rectilinear geometry remains controlled. Wide lens does not imply fisheye.

### Depth

Deep/contextual focus is preferred so structure remains readable. Shallow depth is not added as a cinema token.

### Motion

Static unless people, curtains, foliage, or another moving element is explicitly part of the scene.

Result: PASS.

---

# Case D - Action Still

Input:

```text
runner sprinting through a wet city street at dusk
```

Expected reasoning:

### Intent

Energy and direction of travel matter. The frame can choose either decisive frozen action or tracked motion depending on desired register.

### Composition

Lead room should support travel direction. Street/environment contextualizes action.

### Perspective

Camera distance and height create the relationship to the runner; focal length then frames that position.

### Depth

Focus strategy prioritizes runner/face/torso as needed while environment remains coherent.

### Motion options

Valid AUTO possibilities include:

- mostly frozen runner for a crisp commercial/sports frame;
- tracking pan with relatively stable runner and streaked environment;
- moderate localized limb/water blur for narrative energy.

Invalid:

- random whole-frame blur;
- duplicated limbs as fake motion;
- wet-road reflections moving inconsistently with the runner/camera;
- arbitrary speed lines.

Result: PASS.

---

# Case E - Expert Locked Setup

Input:

```text
ARRI Alexa 35, Cooke Panchro Classic, 25mm, f/1.4, low angle. Child sitting in sand with father, top-down over-the-shoulder feel, keep the frozen moment identical.
```

Locked values:

```text
camera_reference = ARRI ALEXA 35
lens_family = Cooke Panchro Classic
focal_length = 25mm
aperture = f/1.4
camera_angle includes explicit low-angle request
scene/pose/timecode preservation = locked
```

Conflict analysis:

`low angle` and `top-down over-the-shoulder` are directionally inconsistent if interpreted as the same camera orientation. This is a C2/C1-style geometry conflict depending on exact wording and context.

Required behavior:

- do not silently discard either instruction;
- use `parameter-conflicts.md`;
- if one phrase describes the prior shot and the other the requested new angle, use context to resolve;
- otherwise surface the smallest necessary clarification or state the conflict;
- all other missing fields remain AUTO;
- no provider may silently replace Alexa/Cooke/25mm/f1.4 locks;
- frozen moment means subject pose/blocking remains fixed while camera changes only where geometrically possible.

Result: PASS because the system detects rather than hides the conflict.

---

# Cross-System Consistency Checks

## 1. Story before hardware

PASS.

`visual-intent.md` defines the decision order:

```text
story -> viewer relationship -> hierarchy -> composition -> camera -> lens -> light -> grade
```

Named equipment remains optional unless locked or useful for provider translation.

## 2. Composition vs perspective

PASS.

Composition selects the desired spatial relationship. `focal-length-and-perspective.md` prevents focal length from substituting for camera position.

## 3. Camera vs lens responsibility

PASS.

`cameras-and-capture-formats.md` and `lens-character.md` separate capture-system response from optical character.

## 4. Focal length vs lens character

PASS.

A 35mm focal length does not imply one optical family or one look.

## 5. Aperture vs cinematic quality

PASS.

`aperture-focus-and-depth.md` explicitly rejects maximum aperture as a default and supports deep contextual focus where story requires it.

## 6. Motion blur vs cinematic quality

PASS.

`motion-and-shutter.md` treats blur as physical motion during exposure rather than a decorative cinema effect.

## 7. Reference uncertainty

PASS.

Exact camera/lens/focal/aperture/shutter values are not asserted from a reference image without metadata/evidence.

## 8. Lock preservation

PASS.

All runtime references defer to `locks.md` and `parameter-conflicts.md` for explicit user values.

## 9. Provider neutrality

PASS.

The runtime knowledge describes observable intent. Provider-native controls remain downstream adapter concerns.

## 10. Still-image scope

PASS.

Motion language describes a single frame only. It does not expand the skill into temporal video direction.

---

# Anti-Cliche Gate

The completed Phase 3 does not require any of these merely because the user says `cinematic`:

```text
shallow DOF
f/1.2
teal/orange
anamorphic streak flare
heavy grain
halation
haze/fog
rim light
Dutch angle
low angle
slow shutter
motion blur
large format
named cinema camera
named vintage lens
```

PASS.

---

# Physical Plausibility Gate

Phase 3 now checks/coherently reasons about:

- camera position;
- field of view;
- format;
- perspective;
- composition/blocking;
- lens rendering;
- focus plane;
- depth transitions;
- subject/background spacing;
- aperture locks;
- moving subject vs moving camera;
- motion direction;
- reflections/shadows during motion;
- static vs moving scene regions.

PASS.

---

# Phase 0 / Phase 2 Regression Check

Violations found:

```text
scope violations: 0
standalone dependency violations: 0
provider-core contamination: 0
explicit-lock violations: 0
reference-certainty violations: 0
confidence/authority violations: 0
hidden conflict resolution: 0
still-vs-video scope violations: 0
```

PASS.

---

# Phase 3 Gate Verdict

**PASSED**

All seven Phase 3 tasks are complete.

The skill now has a coherent provider-neutral cinematography foundation covering:

```text
visual intent
composition and blocking
capture format / camera character
lens character
focal length / distance / perspective
aperture / focus / depth
motion / shutter appearance in stills
```

The next phase may build lighting, exposure, film response, and color on top of this camera foundation without redefining the Phase 3 geometry/optics contracts.
