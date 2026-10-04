# Cinematic Realism Director - Routing and Scope Contract

Status: RUNTIME ROUTING CONTRACT

Purpose: define package identity and activation boundaries.

## Package Identity

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
primary_role: professional photographic/cinematic still-image direction and realism intelligence
```

The package ID `cinematic-realism-director` is stable. Do not rename it casually because Agent Skills retrieval, tests, examples, adapters and integrations may depend on it.

## Primary Scope

Activate this skill when the user's goal is primarily a **photographic or cinematic still image** and professional visual direction would improve the result.

The user does not need to say `cinematic`.

Use it for:

- ordinary photo/image generation that should be professionally directed;
- iPhone/mobile/selfie photography;
- candid/documentary/street photography;
- narrative/movie-like stills;
- portraits/beauty;
- fashion/editorial;
- product/commercial;
- automotive;
- food;
- architecture/interiors;
- travel/hospitality;
- hero/key/storyboard frames;
- prompt cinematization/professionalization;
- AI-look repair;
- reference visual-DNA matching;
- expert camera/lighting locks;
- professional shot recipes;
- provider-specific prompt export when explicitly requested.

## Default Routing Principle

**Still-frame visual authority belongs here whenever photographic/cinematic quality is the task.**

A basic request such as:

```text
iPhone mirror selfie in a hotel room
```

is valid because the skill can supply elite mobile-photography direction while preserving the phone medium.

A request such as:

```text
candid photo of two friends laughing outside a restaurant
```

is valid because the skill can apply top candid/editorial judgment without making it staged.

The user should not need to pre-supply professional terminology.

## Positive Activation Classes

### STILL_GENERATION

Any photographic/cinematic still where professional composition, camera relationship, light, exposure, color, texture, material realism or finishing matters.

### CINEMATIZE / PROFESSIONALIZE

A concept or prompt needs stronger professional image direction while preserving its subject/purpose/medium.

### REALITY_REPAIR

An existing image must become more photographically plausible while preserving identity, pose, product, wardrobe, scene, composition, or other locked content.

### REFERENCE_MATCH

One or more still references must be analyzed for observable composition, perspective, depth, light, contrast, palette, texture, atmosphere, material response, or other reusable visual characteristics.

### MANUAL_CAMERA

The user supplies one or more capture decisions. Explicit choices are locks; missing values remain AUTO.

### PROMPT_ONLY

The user wants a final image-generation/editing prompt/spec rather than direct generation.

### SHOT_RECIPE

The user asks to explain the technical/professional still-frame decisions.

## Negative Activation Boundaries

Do not use as primary authority for:

- timeline editing, cuts, captions, B-roll placement, EDLs, render/delivery;
- temporal motion choreography, duration, lip-sync, frame-to-frame continuity;
- website/app/dashboard/product UI design;
- diagrams/charts/logos/icons/infographics where photographic realism is irrelevant;
- pure camera/lens factual shopping questions unrelated to an image-design task.

This skill may contribute a still-image asset/spec to those workflows without taking their primary authority.

## Medium Fidelity

Professionalization must respect the user's requested medium.

Examples:

- `iPhone selfie` -> elite mobile photography/editing, not generic cinema-camera capture;
- `candid photo` -> elite candid/editorial photography, not staged fashion blocking;
- `architectural photo` -> architectural-photography geometry discipline;
- `movie frame` -> feature-film cinematography;
- `product packshot` -> specialist product photography.

## Authority Priority

For still-image work:

```text
1. current explicit user instruction
2. preservation requirements
3. active explicit technical/aesthetic/provider locks
4. package physical/logical rules
5. Professional Quality Floor for unspecified fields
6. AUTO inference
7. provider defaults
```

Provider quirks must not silently override locks or the professional quality floor.

## Execution Boundary

Routing to this skill does not decide the external provider.

Execution follows `references/execution-priority.md`:

```text
explicit provider lock
> native/local image capability
> permitted external fallback only for missing material capability
> prompt/spec
```

Magnific/Higgsfield are explicit-target/benchmark only.

## Still-Image Boundary

The skill is centered on still images.

Video concepts may be considered only when they affect a frozen frame, such as visible shutter/motion behavior or designing a hero frame that will later be animated.

Temporal filmmaking/editing remains outside primary scope.

## Routing Acceptance Examples

### Should activate

- `iPhone mirror selfie in a hotel room`
- `candid photo of my friends laughing outside a restaurant`
- `woman waiting for a taxi in London at night`
- `premium product photo of a watch on stone`
- `make this AI-looking image feel photographed but keep everything the same`
- `Alexa 35, 35mm, T2, low angle. Choose the rest`
- `analyze this frame and give me a reusable visual recipe`
- `give me only the Gemini image prompt for this shot`

### Should not activate as primary authority

- `cut this 30-second video and add captions`
- `design a responsive dashboard`
- `make a pie chart`
- `what does an Alexa 35 weigh?`

## Routing Acceptance

Correct routing means photographic still requests can receive the Professional Quality Floor even when the user uses basic language, while non-photographic/temporal/UI tasks remain outside this skill's primary authority.
