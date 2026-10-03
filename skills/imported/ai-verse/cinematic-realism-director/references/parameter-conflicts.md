# Cinematic Realism Director - Parameter Conflict Resolution

Status: FROZEN FOR V1

This contract defines how the skill resolves contradictory or tension-filled cinematic parameters without silently violating user locks.

It extends `references/locks.md` into a deterministic resolution system for the universal Cinematic Shot Spec.

The governing rule is:

> Preserve the user's explicit intent first. Resolve tension through unlocked variables. Change a hard lock only when the user changes it, execution is impossible, or policy/capability makes it unavailable.

## 1. Conflict Resolution Order

When two or more parameters appear incompatible, process them in this order:

1. identify which values are explicit hard locks;
2. identify preservation locks;
3. separate factual constraints from creative preferences;
4. determine whether the combination is genuinely contradictory or merely unconventional;
5. search unlocked/AUTO variables for a reconciliation;
6. preserve the observable intent when a provider cannot express a literal control;
7. ask for a user choice only when no meaningful result can proceed without choosing between mutually exclusive hard locks;
8. never claim all constraints were satisfied if one materially was not.

## 2. Conflict Classes

Use the same conceptual classes introduced by `locks.md`, with stronger execution rules here.

### C0 - Compatible

No meaningful contradiction exists.

The combination may be unusual, but it can be represented coherently.

Examples:

```text
14mm + close portrait
65/70mm reference + modern clean digital finish
hard noon sun + soft bounce fill
f/1.4 + wide shot where only one spatial plane needs focus
```

Action:

- preserve all locks;
- do not warn merely because the choice is unconventional;
- complete the remaining shot through AUTO fields.

### C1 - Tension but reconcilable

The locked choices pull against each other, but unlocked variables can make the result coherent.

Action:

1. preserve all hard locks;
2. identify the physical/visual tradeoff;
3. solve with AUTO parameters;
4. expose the tradeoff only if it materially affects what the user expects.

### C2 - Direct contradiction

Two or more hard requirements cannot all be literally true in the same physical/visual interpretation.

Action:

1. preserve the fact that both were requested;
2. identify the exact contradiction;
3. test whether semantic reinterpretation can preserve the user's likely intent without falsifying the literal settings;
4. if not, require a choice only when execution cannot reasonably continue;
5. if the host/task should continue without interruption, choose the interpretation that preserves the most recent or highest-priority explicit instruction and mark the unresolved lock as not fully satisfied;
6. result cannot be `success` if a material hard lock was knowingly violated.

### C3 - Provider execution conflict

The cinematic request is coherent, but the active provider/tool cannot literally express one or more controls.

Action:

- preserve the universal shot spec;
- translate the control into observable visual language;
- use a supported approximation only if it preserves intent;
- never invent a nonexistent provider parameter;
- if exact execution is mandatory and unavailable, degrade to `partial` or `blocked` per `success-contract.md`.

## 3. Authority Order

Use this order when constraints conflict:

```text
1. current explicit user instruction
2. current explicit preservation constraint
3. newer explicit revision of an older lock
4. trusted factual metadata when the task concerns an existing source
5. previously active locks that remain clearly in scope
6. physical/logical consistency requirements
7. strong observable evidence
8. AUTO creative inference
9. provider defaults
```

Provider defaults are never allowed to beat explicit creative intent.

## 4. Solve Through AUTO First

Before touching any hard lock, search these unlocked dimensions for solutions:

- camera distance;
- camera height;
- subject blocking;
- focus target;
- focus distance;
- spatial arrangement;
- lighting ratio;
- source size;
- fill level;
- exposure strategy;
- foreground/background placement;
- composition;
- crop/aspect ratio;
- atmosphere;
- color separation;
- texture strength;
- provider translation wording.

This is one of the main advantages of the skill over a static prompt suffix.

## 5. Canonical Conflict Example: 14mm + No Wide-Angle Perspective

User request:

```text
14mm lens, but no wide-angle perspective distortion.
```

### Analysis

A 14mm focal-length lock does not by itself force a close-camera caricature. Strong near/far scale exaggeration comes primarily from camera position relative to the subject.

Possible interpretations:

#### C1 if the user's real goal is clean geometry

Keep 14mm locked and solve through:

- greater camera-subject distance;
- central subject placement;
- rectilinear lens behavior;
- controlled edge placement;
- level camera when architecture/verticals matter;
- crop/reframe from the wider captured field if necessary.

Result:

```text
14mm preserved
perspective exaggeration reduced
field of view remains wide
```

#### C2 if user literally requires 14mm field of view and telephoto-like spatial compression

Those are incompatible under ordinary pinhole-camera geometry at the same framing and scene arrangement.

Do not promise both.

State the minimum tradeoff only when necessary.

## 6. Canonical Conflict Example: f/1.2 + Deep Focus Across Large Scene

User request:

```text
f/1.2, but everything from foreground to distant background tack sharp.
```

### C1 possibilities

Some degree of increased depth may be achieved by:

- increasing focus distance;
- using a wider focal length if not locked;
- using a smaller capture format if not locked;
- reducing near-camera foreground elements;
- arranging important subjects closer to the same focus plane;
- accepting perceived rather than mathematically total sharpness.

### C2 condition

If the user simultaneously locks:

```text
large format
long focal length
very close focus
f/1.2
deep foreground-to-infinity sharpness
single exposure / natural optical DOF
```

then literal physical compatibility fails.

Possible semantic alternatives, only when allowed:

- focus-stacked photographic look;
- computational/deep-focus composite;
- reduce the depth requirement to "environment readable" rather than tack sharp.

Do not silently change f/1.2 to f/11.

## 7. Canonical Conflict Example: IMAX 70mm + VHS Artifacts

User request:

```text
IMAX 70mm with vintage VHS artifacts.
```

This is usually **C0**, not a contradiction.

Why:

The request may describe two different stages:

```text
capture aesthetic: large-format 65/70mm cinematic image
presentation/degradation layer: VHS transfer artifacts
```

The skill should model them separately.

Possible spec:

```text
capture_format: 65/70mm reference
capture_character: large-format photographic clarity / scale
finish: VHS transfer degradation
```

Do not reject creative cross-era combinations merely because the technologies are historically different.

The only contradiction would arise if the user simultaneously requires:

```text
pristine untouched photochemical original
and
visible VHS transfer artifacts in that same final representation
```

Then the desired final artifact must clarify which state is being represented.

## 8. Lens Character vs Focal Length

Do not treat lens family and focal length as the same parameter.

Example:

```text
Cooke Panchro character + 24mm
```

is coherent if that focal length exists conceptually or the user is asking for the visual combination.

If a provider offers only a fixed branded lens preset that internally implies another focal length, this becomes C3 provider conflict, not a reason to alter the universal spec.

## 9. Camera Body vs Film Stock

A digital camera reference plus a film-stock look is normally C0.

Example:

```text
ARRI Alexa 35 + Kodak Vision3 500T tonal response
```

Interpretation:

- digital capture/camera character;
- film-emulation or grading target.

Do not falsely claim actual 500T negative was exposed.

Schema/runtime language should separate:

```text
capture system
from
finish / tonal response
```

## 10. Lighting Conflicts

### Hard source + soft shadows

Not automatically contradictory.

A hard key can coexist with softer secondary shadows from:

- ambient sky;
- bounce;
- fill;
- multiple sources;
- atmospheric scattering.

### Single hard point source + completely shadowless illumination

Likely C2 if both are intended as literal lighting conditions.

Possible semantic reconciliation:

- keep the hard point source visually present;
- add strong ambient/fill only if not prohibited;
- otherwise admit the shadowless requirement cannot coexist physically.

### Low key + bright subject readability

Usually C1.

Low key describes tonal distribution/contrast, not "everything dark."

Keep subject readable while allowing most of the frame to remain dark.

## 11. Color and White-Balance Conflicts

Example:

```text
neutral white balance + preserve strong tungsten warmth
```

Usually C1.

Possible solution:

- neutralize the reference neutral surface while allowing tungsten practicals to remain warm relative to it;
- preserve mixed-light separation.

Do not globally orange the frame.

Example:

```text
strict monochrome + vivid red product
```

C2 if "strict monochrome" literally applies to the entire image.

Could become C0 if the user's intended meaning is selective color, but do not assume that without enough context.

## 12. Preservation vs Repair Conflicts

Reality Repair often contains the most important conflict class.

Example:

```text
keep exact composition and pose, but fix hand anatomy
```

Usually C1.

Repair may alter finger topology/shape while preserving:

- wrist position;
- gesture intent;
- hand placement;
- composition;
- body pose.

Example:

```text
keep every pixel of the hand identical, but fix malformed fingers
```

C2.

The same pixels cannot remain identical while their anatomy changes.

The skill must identify the narrowest preservation boundary that can be relaxed, rather than regenerating the entire frame.

## 13. Reference Match Conflicts

If the reference contains properties that conflict with user locks for the target, user locks win.

Example:

```text
Reference: telephoto compressed portrait
User target lock: 24mm close camera
```

Do not secretly preserve the reference perspective by changing the user's focal/camera choices.

Instead transfer the non-conflicting DNA:

- color;
- lighting;
- texture;
- production design;
- contrast;
- atmosphere;
- perhaps composition rhythm.

Report that perspective DNA was intentionally not copied only if the user asks for exact matching or the difference is material.

## 14. Temporal-Looking Still Effects

Motion blur in a still image is allowed and does not move the skill into video authority.

Potential conflict:

```text
frozen razor-sharp subject
heavy subject-motion blur
```

C2 if both apply to the same subject/body region at the same exposure.

Can become C1 if:

- only limbs blur while face remains relatively sharp;
- flash/flicker or composite effect is explicitly intended;
- camera motion and subject motion affect different elements.

## 15. Provider Conflict Translation

When the provider lacks a literal control:

### Example: no camera selector

Universal lock:

```text
camera_reference = ARRI Alexa 35
```

Adapter translation may express:

- high-latitude digital cinema response;
- restrained highlight rolloff;
- natural skin color separation;
- controlled shadow detail;
- non-brittle detail.

The universal lock remains intact in the shot spec.

The provider execution is an approximation of observable behavior, not proof of camera simulation.

### Example: no negative-prompt support

Do not force a `negative_prompt` parameter.

Translate avoidance guidance positively or into provider-supported edit constraints.

This is C3, not a core-spec conflict.

## 16. Conflict Record

When structured output is useful, a conflict record should conceptually include:

```text
id
class: C0 | C1 | C2 | C3
parameters_involved
locked_parameters
summary
physical_or_logical_reason
resolution_strategy
resolved_through_auto_fields
user_choice_required
provider_limitation
remaining_unsatisfied_constraint
status
```

The V1 shot schema may carry conflicts through provenance/notes or a future dedicated field. The semantic contract is authoritative even when a host uses a compact representation.

## 17. Ask vs Proceed Rule

Do not ask a clarifying question merely because a combination is uncommon.

Proceed automatically when:

- C0;
- C1 can be solved through AUTO fields;
- C3 has a faithful semantic/provider fallback;
- the user's likely intent is sufficiently clear.

Ask only when:

- C2 contains mutually exclusive hard locks;
- choosing either interpretation materially changes the requested result;
- no reasonable best-effort result can preserve the central intent.

If the host/task context requires continuing without interaction, preserve the most recent/highest-priority explicit instruction and mark the other constraint unresolved rather than pretending success.

## 18. Conflict Verification

Before final output:

1. enumerate active hard and preservation locks;
2. verify each against the final shot spec;
3. verify provider translation did not silently remove one;
4. verify any C1 reconciliation uses only unlocked fields unless authorized;
5. verify any C2 unresolved constraint is disclosed when material;
6. verify status follows `success-contract.md`.

A result with an unresolved material hard-lock violation cannot be full `success`.

## 19. Failure Conditions

Conflict handling fails if the skill:

- changes 14mm to 50mm because it prefers portraits on 50mm;
- changes f/1.2 to f/8 without permission to gain depth;
- calls an unusual creative combination impossible without analysis;
- confuses capture format with finishing texture;
- confuses lens focal length with perspective in isolation;
- lets reference DNA override target locks;
- fabricates provider controls to satisfy the spec;
- resolves preservation/repair tension by unnecessarily regenerating the entire frame;
- claims all locks were satisfied when one was knowingly broken.

## Task 2.5 Acceptance

Task 2.5 is complete when:

- C0-C3 conflicts have deterministic meanings;
- user locks remain authoritative;
- C1 conflicts are solved through AUTO fields first;
- C2 conflicts cannot be silently hidden;
- C3 provider limitations preserve universal intent without fabricated controls;
- the canonical 14mm, f/1.2/deep-focus, and 65/70mm+VHS examples are handled correctly;
- preservation, reference-match, lighting, color, and provider conflicts are covered;
- final verification checks all hard locks before success.
