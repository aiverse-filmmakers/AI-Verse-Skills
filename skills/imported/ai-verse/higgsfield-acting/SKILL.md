---
name: higgsfield-acting
description: Write the performance part of an AI video prompt so characters look alive. Use for almost every AI video generation that has a character who speaks, listens, reacts or does something with intent, including Seedance and Higgsfield work, and whenever a character reads as dead, glassy, flat or over acted. It turns a scene into what each person is trying to do to the other, with the eyes doing real work. It works with director-agent (plans the acting upstream), ai-video-director (decides the deliverable) and ai-realism (assembles the final Seedance prompt). Skip it for stylised, animated or non human requests that do not call for human acting.
version: 1.0.0
license: MIT
metadata:
  ai-verse:
    ownership: first-party
    category: film-media
---

# Higgsfield Acting: performance for AI video

Give every character in a prompt something to do, so the face looks like a mind at work. The model needs a task for each person. A list of facial movements gives it nothing to believe.

## Where this skill sits

Rank when instructions disagree, highest first: the user's creative brief, locked references and saved elements, this skill for performance, ai-realism for structure and camera, platform limits.

The chain:

1. director-agent plans the scene upstream and may already supply each character's objective, action verb and reaction. Use that and do not reinvent it.
2. ai-video-director decides the deliverable.
3. This skill writes the PERFORMANCE content for each shot with a character.
4. ai-realism places it in the final Seedance prompt, in the PERFORMANCE block.

For video that is not Seedance, still use this skill. The content works anywhere, and the block goes where the target prompt format keeps acting.

Do not force acting onto a request that does not want it: animation, abstract motion, creatures, objects, crowds seen from far away. Follow the brief.

## The core idea

A character is invested in a tactic for getting what they want. The tactic is what they are doing to the other person right now, and it can live entirely in the eyes: a different look when the partner is begging than when the partner is mocking; checking both of the partner's eyes for any sign of trust, noticing whether they lean in or drift away, and adjusting.

So:

- Do not describe the result ("he looks sad", "eyebrows lift"). Playing a result gives a dead or mechanical face.
- Do not fix dead eyes with lighting tricks. Give the eyes a job.
- The tactic does not have to be physical. The movement of the eyes is the doing.
- Nobody plays the emotion. Everybody plays the direction of the scene, and the feeling reaches the audience through the pressure against it.

## The ladder, in this order

0. Read the whole scene and all the dialogue first. The task lives across the exchange: where it holds and where it breaks.

1. Scene direction. One shared direction that every character plays, often unspoken: a quiet agreement about how this time will go. It is not the film's theme, and characters never know the theme.

2. Name the event from the ending. The last beat is the key to the whole scene. Watch for a last line that says one thing and means another. The event must include every person in frame, including silent and sleeping ones, as participants or mirrors.

3. The physical channel. The surface activity of the scene stays as what the camera sees (packing, cooking, doing paperwork). Each character pursues the event through it in their own visible way. Give each person their own behaviour, one event, one setting.

4. Motive. Each character pushes the same direction for a different reason. Same direction, different fuel. Their situation limits the motives: someone who already took the compromised job cannot play innocence.

5. Goal. What this person is fighting for inside the scene. Ordinary, personal and playable. Never the theme.

6. Obstacle. What presses against the direction, so that one crack would break the scene. The audience feels this because nobody plays it.

7. Tactic. What the character does to the partner, moment by moment, including the eye work as action: checking, measuring, stealing a look and snapping back, registering whether the point landed. Key the beats to the actual dialogue words, and mark the point where a character's fuel runs out and the line breaks.

## The PERFORMANCE content

Write one entry per character with a want, using this shape. Use the long form when planning and the short form inside the prompt.

```
[NAME] (invested in the task; the work happens in the eyes)
Direction (shared): ...
Motive: ...
Goal: ...
Obstacle: ...
Tactic: what they do to the partner, with the eye work as action
Beat by beat:
  "line" : verb at the partner, what the eyes check
  "line" : verb, eye work
  where the line breaks, if it does
Gaze stays engaged in the task; blink at a natural rate.
```

Rules:

- Use verbs aimed at the partner. No emotion adjectives ("sadly", "nervously").
- No face choreography ("brows lift", "mouth trembles"). Body, hands and props may be described concretely, because those are the visible channel.
- Silent listeners get a real task too ("decide whether he is serious", "wait for the punchline", "protect the mood").
- Keep the gaze line in every prompt. It guards against the frozen, glassy stare.
- Keep it short. In the prompt, each character needs only the tactic, the beats and the gaze line. Direction, motive, goal and obstacle shape your choices and may stay out of the prompt.

## Pairs that contrast

A two person scene is richer when each person carries one plus and one minus, mirrored against the other, with one axis the audience reads.

Example: a bakery owner and a food inspector. The owner is warm and generous (plus) but hides a failed check (minus). The inspector is stiff and procedural (minus) but notices the owner's tired hands and quietly gives time to fix things (plus). The essential axis is care for the person in front of you.

- Both still push the same shared direction (keep the visit routine). The contrast sits under it and leaks through the tactics and the eyes.
- Often the visible trait is a scar over its opposite: someone who seems careless may be someone who stopped hoping. Direct the history, not the surface.

## Worked example

A father and his teenage daughter, parallel parking before her test. Direction: keep it light, do not mention last night's argument. His motive: he wants her to feel trusted. Hers: she does not want him to see she is scared. Goal: his, to teach without taking the wheel; hers, to look unbothered. Obstacle: the argument, one wrong word away.

- He sits calm, hands loose on his knees, checks her face in the mirror and looks away when she catches him.
- She watches the mirror, steals a look at his hands to see whether they tense, and snaps back when he turns.
- When she hits the kerb, he says "good, again" and looks at the street, not at her.

Nobody on screen cries, which is why the scene lands.

## Common mistakes

- Building a task from one line: re-read the whole scene.
- Giving a character the film's theme as their task.
- Mixing up the scene direction (shared) with a character goal (personal).
- A motive that ignores the character's situation.
- Writing eye or face movements instead of eye work as action: rewrite as a verb at the partner.
- Emotion adjectives as direction: replace with the task that produces the feeling.
