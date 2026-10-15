# AUTO DIRECT Workflow

Status: RUNTIME WORKFLOW

Purpose: turn a minimal still-image idea into the strongest professional image appropriate to the requested medium without interrogating the user for technical camera knowledge.

Use with:

- `references/professional-quality-floor.md`
- `references/execution-priority.md`
- `references/visual-intent.md`
- `references/reality-gate.md`

## Entry

Use when the user supplies a subject, situation, or simple visual idea and has not requested strict manual camera control, reference matching, or repair of an existing image.

One sentence is sufficient.

## Governing Rule

```text
user intent
-> requested/implicit photographic medium
-> professional quality floor
-> story priority
-> shot design
-> capture/optics
-> light
-> exposure/color/finish
-> physical realism
-> Reality Gate
-> native-first execution
```

AUTO is not a neutral completion engine. It is a world-class visual-director default.

The user should not need to add words such as:

```text
professional
cinematic
Hollywood
ARRI
high quality
good lighting
good composition
realistic
```

for AUTO to deliver professional-quality direction.

## Procedure

1. Extract the literal subject, action, environment, requested medium, mood/purpose, and explicit constraints.
2. Convert every explicit technical, aesthetic, provider, and preservation choice into a lock.
3. Infer the intended image class: mobile/selfie, candid/documentary, narrative/cinematic, portrait, fashion, product, automotive, food, architecture, travel/hospitality, or another photographic specialty.
4. Apply `professional-quality-floor.md` for that image class.
5. Infer viewer relationship and visual hierarchy from story/purpose.
6. Design composition, timing/blocking, camera position, and spatial relationship before focal length.
7. Choose capture character and optics that support the medium. Do not force cinema-camera semantics onto explicit mobile/phone capture.
8. Choose aperture/focus/depth from information hierarchy and medium rather than maximum blur.
9. Build lighting from plausible source motivation, then fill/negative-fill/bounce/practicals only as needed.
10. Choose professional exposure hierarchy, highlight behavior, shadow density, white balance, color separation, and grade.
11. Add subtle organic filmic texture by default for most photographic/cinematic work unless the requested medium or explicit user lock calls for pristine/no-grain output.
12. Add physical-realism requirements appropriate to subject, skin, material, environment, contact, shadows, and reflections.
13. Populate the Cinematic Shot Spec. Mark inferred choices as AUTO/inferred, not user-supplied.
14. Run the Reality Gate at V0.
15. Choose execution under `execution-priority.md`: explicit provider lock first, otherwise native/local image model first, external fallback only for missing material capability.
16. Adapt only to the execution path already chosen.
17. Generate/edit if requested and possible; otherwise return the strongest prompt/spec.
18. If the output can be inspected, run V2 Reality Gate and correct only material failures while preserving successful regions/locks.

## Beginner Behavior

Do not ask about camera, lens, aperture, film stock, lighting ratio, white balance, grain, grade, or provider when AUTO can infer them safely.

A beginner asking:

```text
A girl drinking coffee by the window.
```

should receive a professionally directed image, not a generic literal rendering waiting for the user to add cinematography keywords.

## Medium Examples

### `iPhone mirror selfie in a hotel room`

AUTO should preserve phone/selfie plausibility while applying elite mobile-photography judgment:

- believable phone distance/perspective;
- excellent available-light positioning;
- controlled exposure and white balance;
- flattering but real skin;
- clean framing and background hierarchy;
- professional mobile edit;
- no fake cinema-camera depth merely to look expensive.

### `candid photo of friends laughing outside a restaurant`

AUTO should behave like a top candid/editorial photographer:

- decisive authentic moment;
- non-performative gesture;
- believable camera access;
- layered composition/context;
- professional exposure/color;
- subtle organic texture;
- no obvious staged beauty setup unless implied.

### `woman waiting for a taxi in London at night`

AUTO should behave like feature-film cinematography:

- intentional narrative hierarchy;
- motivated street/practical light;
- premium highlight rolloff and shadow density;
- high-end skin/color separation;
- realistic optical depth;
- subtle filmic texture;
- polished movie-grade finish;
- no need for the user to ask for `cinematic`.

## Default Cinema DNA

When cinematic/narrative work is requested—or when a general photographic scene has no stronger specialty signal—AUTO should normally aim for:

```text
feature-film visual hierarchy
premium digital-cinema tonal response
ARRI-like highlight rolloff / gentle highlight-to-mid transition as an observable target
rich but readable shadows
motivated source falloff
professional color separation
natural skin/material response
realistic optical depth
subtle organic filmic texture
high-end restrained grade
```

This is not a claim of literal ARRI capture or simulation.

## Anti-Cliche Rules

Professional quality is mandatory; cliché stacking is not.

AUTO should **not** automatically add:

- anamorphic blue streaks;
- teal/orange grading;
- haze/fog;
- dramatic rim light;
- f/1.2 or maximum background blur;
- Dutch angle;
- heavy bloom;
- obvious halation;
- strong vignette;
- crushed blacks;
- arbitrary motion blur;
- named prestige camera/lens tokens with no observable purpose.

Subtle organic grain/texture is different from heavy `film-look` effect stacking and is normally part of the professional photographic finish unless the medium/user calls for clean digital output.

## Output

Minimum useful result:

- resolved professional shot concept;
- provider-neutral shot decisions;
- quality-floor decisions appropriate to the medium;
- adapted prompt/instructions if execution is unavailable or prompt-only is required;
- truthful verification state.

AUTO fails when the image is merely competent/ordinary because the user did not know which professional cinematography or photography terms to request.
