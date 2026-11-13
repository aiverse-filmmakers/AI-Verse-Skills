---
name: ai-realism
description: Write one finished Seedance 2.5 video prompt from an idea, script beat, storyboard shot or set of saved references. Use whenever the user asks for a Seedance prompt, a cinematic shot or scene for Seedance, help setting up references or elements for it, or a revision of a Seedance prompt. It is the last step in the filmmaking chain. ai-video-director chooses the deliverable, director-agent plans the story and acting, higgsfield-acting writes the performance, and this skill assembles and formats the final prompt. Not for still images (use cinematic-realism-director) and not for editing footage (use video-editor).
version: 1.0.0
license: MIT
metadata:
  ai-verse:
    ownership: first-party
    category: film-media
---

# AI Realism: Seedance 2.5 prompts

Turn a shot, a scene or a script beat into prompts that Seedance 2.5 renders like a film. Block the action, place the light, and pace every cut.

## Where this skill sits

Rank when instructions disagree, highest first:

1. The user's creative brief. A stylised, animated or non human request is never forced into realism.
2. Locked references and saved elements (identity, voice, location).
3. higgsfield-acting decides how characters perform.
4. This skill decides prompt structure, camera, light, physics and format.
5. Platform limits, which change with the model and must be checked.

The chain, in order:

1. director-agent plans the story, dialogue and acting intent, only when the story is not settled yet.
2. ai-video-director decides what is delivered: a storyboard, one prompt, or one prompt per shot.
3. higgsfield-acting writes the PERFORMANCE part for any shot with a character.
4. This skill assembles every Seedance prompt in the structure below.

Do not skip a step that applies. If a shot has a character and higgsfield-acting is installed, use it. If it is not installed, say so and write the performance yourself with intent verbs, not facial instructions.

Each prompt goes in its own code block. How many prompts you write comes from ai-video-director, or from the user if they said.

## Write what can be seen

The model reacts to what it can see and measure, not to mood words. Turn every abstract word into something visible.

- Instead of "tense scene": "the man stops mid step, fingers close slowly, light comes only from the side, half his face in shadow".
- Instead of "cool fast car shot": "low tracking shot beside the car as it powers through a wet curve, headlights glowing, spray off the tyres, firm camera shake".
- Instead of "more natural movement": describe the movement itself, how the body travels and what follows it.

Use plain, instruction style wording. A few exact words beat many vague ones.

Seedance 2.5 handles these well, so write them with confidence: real lens behaviour (a fisheye warps a near hand before the face), mirror and floor reflections, lit crowds where the extras act, one light source holding its rhythm across cuts, the camera as a physical object (a phone set on a rock wobbles, then settles), and single takes up to 30 seconds with a full emotional arc.

Before finishing, watch the prompt in your head as a viewer. Is the first frame busy, is it clear where the subject is and where it looks, where does the light come from, and does anything have two readings?

## Workflow

1. Read the scene as a director. Find where it turns, lands and breathes.
2. Fix the continuity anchors: who is in frame, how they look, what they carry across cuts.
3. Hand the characters to higgsfield-acting for the PERFORMANCE content.
4. Write the prompt with the blocks below.
5. Tag the assets.

If the idea leaves gaps, close them with the user first: blocking, angle, light, timing, behaviour, the first frame, how it ends. The model fills any gap by itself, and usually not the way you wanted.

Read the whole scene while planning. The final prompt holds only what this one generation needs.

## Assets and tags

A reference image sets how someone or something looks. The text sets what happens and pins the details that matter. Use both.

Tag names, in this order: the names the user gave (`@loc_mountain`), then names that match saved elements in the platform, then load order (`@image1`, `@video1`, `@audio1`). Names that match saved elements attach by themselves, so keep them identical.

Per tag, keep the line short: age and build, current state, one or two unique visible features, details the action depends on, and the voice only if the character speaks. Long descriptions fight the image. State small text, logos and colours in words, because the model can drop them.

Character sheets carry studio light, a plain background and a pose. Always add: "Ignore the reference's background, pose and studio lighting." Light the character only by the scene.

A location reference may carry one short note about its hidden side when the camera turns to face away from the reference view.

A voice saved with a character sheet or video element stays consistent when you reuse the same element. Describe the voice once.

Never tag an object in a shot where it is absent. The model will try to push it into frame.

Each generation starts empty. Do not carry in scene numbers, headings, summaries of earlier scenes, unused tags, or phrases like "as before".

## Prompt blocks, in this order

Use only the blocks the shot needs. Context and references come first, space and timing next, action and physics after that, then the descriptive style blocks where they belong, and the technical style lines at the end.

```
SCENE CONTEXT
1 or 2 sentences: what happens, where, when. Where each person stands.

ACTIVE REFERENCES
@tag, short anchor of key details, "100% matches the reference", plus the ignore line above.

LOCATION MAP
Foreground, midground, background. Where the camera is, where the light comes from, movement paths.

FIRST FRAME AND BLOCKING
Who is where in the first frame: position, facing, gaze. The framing rule for this scene.

FORMAT MODE
One continuous shot, or cuts in order, or timed hard cuts.

OPTICS
Shot size and field of view per segment, lens character. For several shots add "no drift inside a segment".

CAMERA
Operator behaviour: height, distance, movement, focus. Tonal character of the camera as a look, never a model name.

ACTION
Events at the precision the shot needs. Camera motion and subject motion written separately.

PERFORMANCE
From higgsfield-acting: what each character is doing to the other, in the order of the dialogue. Acting only.

SKIN AND DETAIL
Pore level skin, breath, texture, wear. Kept apart from acting.

PHYSICS
Mass, inertia, contact, fluids, particles.

LIGHTING
Source, direction, exposure. The priority block.

COLOR GRADE
Only when the grade is strong. Palette through material, light and role.

WARDROBE
Only when costume matters. Material and condition.

AUDIO
Only the sound or line that is needed. Say plainly what is absent, for example "sound effects only, no music".

STYLE
Overall look in words, photoreal, format, grain.

OUTPUT SETTINGS
Aspect, real time or slow motion per segment, when it must be pinned.

POSITIVE LOCKS
Short fixers placed next to what they protect. Continuity lives here.
```

Where each style aspect lives: light in LIGHTING, colour in COLOR GRADE or LOCATION MAP, lens in OPTICS, camera look in CAMERA, skin in SKIN AND DETAIL, acting in PERFORMANCE, gravity and fluids in PHYSICS, costume in WARDROBE, format and grain in STYLE and OUTPUT SETTINGS. Nothing style related goes at the very top. Adapt every line to the actual scene. If the user supplies their own block text, use it as given.

A repeated rule for a whole sequence (for example how every insert in a montage is cut) goes in FORMAT MODE, not before the references.

## Cuts and timing

One generation runs up to 30 seconds on Seedance 2.5 (check the platform, this changes). Plan to use it. State total length, and land every hard cut on a stated second when timing matters.

Choose the precision the shot needs:

- One continuous shot: "one continuous shot, the camera does not cut on its own".
- Cuts in order, no clock: `CUT 1`, `CUT 2`, `CUT 3`.
- Timed: `0.0s to 1.0s`, then `1.0s HARD CUT`, and so on.
- Free b roll: leave the cuts open.

When you give cuts, add: "cuts only at the stated points, the camera does not cut on its own". Cut types: HARD CUT, SMASH CUT, MATCH CUT, INSERT CUT, REVERSE CUT, WHIP CUT. Use fades only when asked. Across cuts hold the same people, geometry, screen direction, gaze, light, wardrobe and prop state.

## Directing

- Blocking: say where each person stands, sits and moves, what the hands do, what sits between them.
- Pace: a confession needs air and held shots; action needs short cuts; a reveal lands on one held close up.
- Camera: be concrete about field of view, height, movement and motive. Every move has a reason.
- Continuity to keep in mind: wet or dry, clean or dirty, one time of day, one weather, emotional carry from the last scene.

## Rules for the words

- Positive wording is the default: say what should happen. A negative is allowed when a shot needs one that a positive cannot do, and it works well for absence ("no music, sound effects only", "no other people in frame"). Keep negatives short and few.
- Speeds in km/h, density in percent, distance in metres.
- Atmosphere that grows across shots grows in steps (fog 20 percent, then 40, then 60).
- Giant scale compared to a human: "as tall as four people stacked".
- Left and right are from the camera. Say "screen left" when it could be confused.
- Environment acts on people physically: snow melts on skin, rain runs down hair, wind moves cloth.
- Colour is tied to material, light and role, never a bare list.
- Write the background in layers. Put the camera on the shadow side and say which way the operator faces.
- White balance in Kelvin, fixed inside a scene (3200, 4000, 5600, 8500).
- Describe equipment as a look. Do not use camera, film or lens model names, or director names, in Seedance prompts.
- English only.

## Optics

Shot sizes: ECU detail, CU full face, MCU head and shoulders, MS to the waist, WS full figure with surroundings, EWS scale and place.

Field of view in degrees is the default in prompt text. A millimetre figure is fine when the user or the shot needs it.

| Degrees | Looks like | Use for |
|---|---|---|
| 180 | fisheye | point of view, dream |
| 107 | 14 to 16 mm | huge interiors, epic opening |
| 84 | 20 to 24 mm | establishing, groups |
| 63 | 28 to 35 mm | observation, reportage, dialogue |
| 47 | 40 to 50 mm | neutral, human eye |
| 29 | 75 to 85 mm | portrait, dialogue bust |
| 18 | 100 to 135 mm | tight portrait, identity |
| 12 | 180 to 200 mm | hands, objects |
| 8 | 300 to 400 mm | extreme compression, distance |

Use only these steps (not 23 degrees). In a multi shot sequence set the angle per segment and add "no drift inside a segment". Put CAMERA after OPTICS and before ACTION. At the very front it fights identity, and at the very end the field of view gets ignored.

Techniques that work:

- Hidden camera feel needs all three: something soft and out of focus over 20 to 30 percent of the frame, haze between camera and subject, and a far vantage at 8 to 12 degrees. Change the foreground object between beats, keep one vantage.
- Sports broadcast: 8 degrees, small handheld tremor, "anchored at distance, finding the action".
- Detail on a wide: 84 degrees, low, right against a small object, so the background falls away.
- Intimate wide: 63 to 84 degrees on a close face.
- Long lens air: "dust hanging in the long compressed air between camera and subject".

## Video to video and image to video

Video to video (swap a character, add a creature, keep the plate):

- The source clip must be at least 4 seconds. If shorter, freeze its last frame to pad it.
- Set the generation length to match the source, usually 4 seconds. Longer and the model invents beyond the source.
- Tag it `@video1` and name it master for camera, framing, focus, motion, expression timing, background, light, grain and length. State the one change and lock everything else.
- If the same defect appears in all four tries, change the prompt or the source. Usual cause: the wanted action has nothing to hold onto in the source. Switch to image to video: take a frame of the location as the start frame and write the action fresh. Plan a 1 to 2 second empty pause where you will join takes.

## Special cases

Extreme angles (8 or 107 degrees) over several beats need all four of these, or they drift after two or three beats: one location reference across all beats; the angle written at the start of each beat; the angle confirmed at the end of each beat; colour told through material and light.

Whip pan: settle subject A at 0.3s, whip at 0.8s, settle subject B at 1.4s. A whip shorter than 0.8s becomes a plain hard cut.

Mixed speed: hard cuts only between speeds, and each shot keeps one speed from start to finish.

Cracks and breaks with no hit: "pressure builds along the edge and a crack spreads from the edge toward the center, edge to center in sequence".

## Platform notes (Seedance 2.5, verify before relying on them)

- Up to 30 seconds per generation.
- Native output may be lower than the delivery size; words such as "8K" change detail, not resolution. For true 4K, check which model and tier the platform offers.
- Cheap low resolution drafts first, then regenerate the best take at full quality with the same references and settings.
- Run several versions of a shot and pick the best moments. A generation does not have to be used whole.

## Check before sending

- Context and references first, style where it belongs, technical style last?
- Tags follow the naming order, and the ignore line is present for character sheets?
- No tag for anything absent from the shot?
- PERFORMANCE comes from higgsfield-acting, not from facial instructions?
- Speeds, density and distances are numbers?
- Emotion is carried by what the character does, not by a label?
- Left and right from the camera?
- Field of view from the table, CAMERA after OPTICS?
- Kelvin set, colour tied to material and light?
- Several shots: angle per segment, "no drift", hard cuts stated?
- Does it still respect the user's brief and any locked element?
