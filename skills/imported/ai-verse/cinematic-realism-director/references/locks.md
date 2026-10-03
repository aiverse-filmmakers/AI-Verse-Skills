# Cinematic Realism Director - Explicit Lock Semantics

Status: FROZEN FOR V1

This contract defines how explicit user choices interact with AUTO cinematography.

The governing rule is simple:

> What the user explicitly specifies is locked. What the user leaves unspecified remains eligible for AUTO completion.

The skill must not silently replace a locked value merely because another choice would be more conventional, more cinematic, or easier for a provider.

## Lock Sources

A value becomes locked when the user explicitly supplies it in the active request or clearly preserves it from an existing target/reference.

Examples:

- `25mm`
- `f/1.2`
- `low angle`
- `ARRI Alexa 35`
- `Cooke Panchro`
- `70mm format`
- `deep focus`
- `hard noon sunlight`
- `black-and-white`
- `keep the exact composition`
- `do not change the product`

Locks may apply to technical, visual, compositional, preservation, or output parameters.

## Lock Precedence

Apply this order:

1. current explicit user instructions;
2. current explicit preservation constraints;
3. previously established user locks that remain clearly active in the same task;
4. package rules required for physical/logical consistency;
5. AUTO inference;
6. provider defaults.

A provider default is never allowed to silently supersede an explicit user lock.

## Lock Types

### Hard lock

The user has explicitly required the value.

Examples:

```text
focal_length = 25mm
aperture = f/1.2
angle = low
preserve_pose = true
```

Hard locks must be preserved unless:

- the user later changes them;
- the request is internally impossible and requires clarification/reconciliation;
- execution is blocked by tool/provider capability;
- safety/policy requires refusal or modification.

### Preservation lock

The user requires existing visual content to remain unchanged or materially consistent.

Examples:

```text
identity
pose
composition
product design
wardrobe
location layout
camera angle
logo placement
```

Preservation locks are especially important in Reality Repair and reference-conditioned editing.

### Soft preference

The user expresses a preference rather than a strict requirement.

Examples:

- "maybe around 50mm"
- "I'd prefer something like Kodak"
- "keep it fairly wide"

Soft preferences should usually be honored, but may be adjusted when needed for coherence. If adjustment materially changes the user's intent, explain it.

### AUTO field

The user did not specify the value.

AUTO fields should be inferred from story, subject, environment, physical plausibility, visual hierarchy, and the other locked values.

## Partial Specification Rule

Never force the user to fill every parameter.

Example:

```text
User: 70mm format, 25mm, f/1.2, low angle.
```

Represent internally as:

```text
LOCKED
capture_format = 70mm
focal_length = 25mm
aperture = f/1.2
camera_angle = low

AUTO
camera_character
lens_family
camera_distance
shot_size
lighting
exposure
film_response
color
texture
material treatment
atmosphere
```

AUTO completion must support the locks rather than fighting them.

## Contradiction Classes

Not every unusual combination is a contradiction. Creative combinations are allowed.

Classify conflicts before changing anything.

### C0 - No contradiction

The combination is unusual but visually/physically plausible.

Action: honor all locks and continue.

### C1 - Tension, but reconcilable

Two choices pull in different directions but can coexist with tradeoffs.

Example:

```text
f/1.2 + desire for more environmental readability
```

Possible reconciliation:

- increase camera-subject distance;
- adjust blocking;
- choose a wider focal length/format relationship if not locked;
- place important elements near the focus plane;
- accept shallower depth where unavoidable.

Action: preserve locks, solve through AUTO fields.

### C2 - Direct visual/physical contradiction

The user explicitly requests mutually incompatible outcomes.

Examples:

```text
14mm ultra-wide field of view + no wide-angle perspective at close camera distance
f/1.2 + entire deep scene tack-sharp while keeping close focus and format fixed
single hard point light + completely shadowless illumination
```

Action:

1. do not silently override either lock;
2. identify the minimum contradiction;
3. offer the smallest reconciliation when interaction is possible;
4. if the host/task should proceed without interruption, preserve the higher-priority/current explicit instruction and flag the other as an unresolved constraint in the output.

### C3 - Provider execution conflict

The requested concept is valid, but the current provider does not expose or reliably support a parameter.

Action:

- preserve the cinematic intent semantically;
- express the effect in observable visual language;
- do not pretend the provider exposes the named control;
- if necessary, return a prompt/spec rather than changing the user's desired result.

Example:

If a provider has no literal "ARRI Alexa 35" setting, retain the lock as a visual/capture reference and translate its intended observable behavior rather than inventing a hidden camera selector.

## Semantic Lock Translation

Some locks are names for desired visual behavior rather than guaranteed physical simulation.

Examples:

- camera body names;
- lens families;
- film stocks;
- named movie looks.

When the active provider does not simulate the hardware directly:

1. preserve the named lock in the structured shot spec;
2. translate it into supported observable traits using the knowledge base;
3. never claim the generated output is physically identical to the real hardware.

## No Silent "Improvement"

The skill must not decide that the user's specified choice is inferior and replace it.

Forbidden behavior:

```text
User asks for 25mm.
Skill silently changes to 50mm because portraits are "better" on 50mm.
```

Correct behavior:

```text
Keep 25mm locked.
Adjust camera distance, framing, blocking, lighting, or focus strategy around it.
```

## Preserve-vs-Repair Rule

In image editing, preservation locks outrank generic realism improvements.

If the user says:

```text
keep the exact pose and composition, only make the image look real
```

then the skill must not "improve" realism by changing:

- pose;
- camera angle;
- framing;
- subject count;
- product geometry;
- wardrobe;
- scene layout.

Reality Repair should target only unlocked systems such as skin texture, materials, light consistency, shadow behavior, reflections, tonal response, depth behavior, and other diagnosed artifacts.

## Lock Persistence

Locks persist only while clearly relevant to the active task.

Do not carry a 25mm lock from one unrelated image request into a later independent request unless the user clearly establishes a continuing visual package or asks for continuity.

Within a deliberate sequence, campaign, character set, or reference-matching workflow, continuity locks may persist until the user changes them.

## User Revision Rule

A newer explicit instruction replaces an older conflicting lock.

Example:

```text
Earlier: 35mm
Later: actually make it 50mm
```

Result:

```text
focal_length = 50mm
```

Do not preserve both as if they are simultaneously active.

## Unknown-value Rule

Do not invent exact technical locks from a reference image.

If analyzing a reference, the skill may infer:

```text
wide-normal perspective
shallow-to-moderate depth
soft highlight rolloff
low camera height
```

but should not lock:

```text
ARRI Alexa 35 + Cooke S4 32mm T2.0
```

unless that metadata is supplied or otherwise known.

Reference-derived values must carry uncertainty in the future structured schema.

## Lock Reporting

By default, keep lock bookkeeping internal.

Expose locks when:

- the user asks for settings/shot recipe;
- a contradiction needs explanation;
- a provider limitation materially changes execution;
- a structured/JSON output is requested;
- verification requires proving that user constraints were preserved.

## Lock Verification

Before final output, compare the planned/executed shot against all active hard and preservation locks.

A task cannot claim full success if a meaningful explicit lock was violated without user authorization.

When output inspection is possible, verify observable locks against the generated/edited image where practical.

When inspection is impossible, verify at least that the final prompt/spec preserves every active lock.

## Failure Conditions

Lock handling fails if the skill:

- silently changes an explicit value;
- treats an AUTO inference as if the user requested it;
- invents exact camera/lens metadata from an image;
- lets provider defaults override the user;
- changes preservation-locked content during Reality Repair without permission;
- repeatedly asks the user to specify values that AUTO can infer;
- refuses an unusual but coherent combination merely because it is unconventional;
- hides a direct contradiction and claims all constraints were satisfied.

## Task 0.4 Acceptance

Task 0.4 is satisfied when:

- explicit values are hard locks by default;
- locks cannot be silently changed;
- unspecified parameters remain AUTO;
- contradictory locks have deterministic conflict classes;
- reconcilable conflicts are solved through AUTO fields first;
- provider limitations translate intent rather than fabricate controls;
- preservation locks are enforced during editing;
- newer explicit instructions replace older conflicting locks;
- lock verification is mandatory before claiming full success.
