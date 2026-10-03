# Cinematic Realism Director - Routing and Scope Contract

Status: FROZEN FOR V1

This document defines package identity and activation boundaries only. It does not define the cinematic knowledge base.

## Package Identity

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
primary_role: cinematic still-image direction and photorealism intelligence
```

The package name `cinematic-realism-director` is the stable V1 capability ID. Do not rename it casually because Agent Skills retrieval, AI-Verse registry identity, adapters, tests, examples, release packaging, and future plugin/MCP surfaces may depend on it.

## Primary Scope

Activate this skill when the user's goal is primarily about a **single still image or a set of still images** and one or more of the following is required:

- create a photorealistic or cinematic still image;
- turn a simple image idea into a fully directed cinematic shot;
- improve an ordinary image prompt so it behaves like a coherent real-camera capture rather than generic AI art;
- edit or repair an existing still image so it looks less synthetic, CG-like, overprocessed, or visually inconsistent;
- diagnose why a still image looks artificial and specify what should be preserved, repaired, and allowed to change;
- reverse-engineer the observable visual DNA of a reference frame for reuse in another still image;
- design a still-image shot recipe using camera, format, lens, focal length, aperture, framing, lighting, exposure, film/sensor response, color, texture, atmosphere, materials, or realism constraints;
- honor user-specified camera or capture parameters as locked values while intelligently filling unspecified values;
- translate one cinematic still-image intent into a prompt or edit specification for a supported image-generation provider;
- prepare a hero frame, keyframe, storyboard frame, campaign frame, product frame, portrait, environment frame, or other frozen image that may later be animated elsewhere;
- explain the cinematic decisions behind a still image when the user explicitly asks for the shot recipe.

The skill is especially appropriate for requests such as:

- "woman waiting for a taxi in London at night" when the user wants a realistic cinematic image;
- "make this AI-looking image feel like a real movie frame";
- "keep everything the same but make the lighting, skin, materials and lens behavior believable";
- "use 25mm at f/1.2 and a low angle, choose everything else for me";
- "match the visual language of this reference without guessing unobservable camera metadata";
- "give me the Seedream / GPT Image / Gemini prompt for this shot".

## Default Routing Principle

**Still-frame visual authority belongs here.**

When a request spans multiple domains, this skill owns decisions that determine what a frozen frame should look like. Other capabilities may own what happens before or after that frame.

Examples:

- hero frame for a future video: Cinematic Realism Director owns the hero-frame visual design; a video-generation or video-editing capability owns temporal motion and editorial assembly;
- website hero artwork: Cinematic Realism Director may create or repair the still artwork; Interface Designer owns layout, interaction, responsive behavior, and product UI;
- commercial edit requiring a generated insert: Cinematic Realism Director may design the insert frame; Video Editor owns edit timing, sequence structure, captions, audio, EDLs, and final media delivery.

## Positive Activation Boundaries

Use this skill when the dominant user intent is any of these classes:

### STILL_GENERATION

A new realistic/cinematic image, film frame, photograph-like frame, key art frame, campaign still, hero frame, portrait, product shot, environment, vehicle shot, food shot, architecture shot, fashion shot, travel shot, documentary-style still, or narrative still.

### CINEMATIZE

A supplied concept or prompt needs to become a coherent cinematic still without changing its core subject or purpose unnecessarily.

### REALITY_REPAIR

An existing image must become more photographically plausible while preserving user-important identity, pose, product, wardrobe, scene, composition, or other locked content.

### REFERENCE_MATCH

One or more still references must be analyzed for observable composition, perspective, depth, lighting, contrast, palette, texture, atmosphere, material response, or other reusable visual characteristics.

### MANUAL_CAMERA

The user supplies one or more capture decisions such as format, camera, lens family, focal length, aperture, camera height, angle, shot size, lighting, stock/look, or texture. Explicit choices are treated as locks. Missing values remain eligible for AUTO completion.

### PROMPT_ONLY

The user wants a final image-generation or image-editing prompt/specification rather than direct generation.

### SHOT_RECIPE

The user asks to reveal or explain the technical still-frame decisions.

## Negative Activation Boundaries

Do **not** activate this skill as the primary authority for the following tasks.

### Video editing and temporal editorial work

Route to Video Editor or another appropriate temporal/video capability when the task is primarily about:

- cutting footage;
- silence or mistake removal;
- timeline editing;
- scene order;
- pacing;
- transitions;
- captions;
- B-roll placement in an edit;
- audio sync;
- EDLs;
- long-form or short-form edit structure;
- final video render or encoded-media QA.

This skill may contribute a still-frame visual specification to such a workflow, but it must not take editorial authority.

### Video motion design and temporal generation

Do not treat this skill as the primary authority for:

- camera movement over time;
- character movement choreography over time;
- clip duration;
- temporal continuity across generated frames;
- frame-rate decisions for motion delivery;
- scene-to-scene video prompting;
- lip-sync or performance timing;
- temporal artifact repair.

Exception: still-image concepts with a visible motion signature, such as shutter/motion blur, may be reasoned about because they affect the frozen frame itself.

### Interface and product design

Route to Interface Designer when the task is primarily about:

- websites;
- dashboards;
- application UI;
- screen flows;
- responsive layout;
- interaction design;
- design systems;
- HTML/CSS/JS interfaces;
- Figma/product-interface implementation.

This skill may produce still artwork used inside an interface, but it does not own the interface.

### General image work with no cinematic/realism need

Do not force this skill onto tasks that are primarily:

- diagrams;
- charts;
- logos;
- icons;
- flat illustrations;
- infographics;
- UI mockups;
- technical schematics;
- intentionally non-photographic artwork where cinematic realism is irrelevant.

If the user explicitly asks for a cinematic photographic treatment of such subject matter, the skill may become relevant again.

### Pure equipment facts or shopping

A factual question such as "what does an Alexa 35 weigh?" or "which lens should I buy?" is not, by itself, a Cinematic Realism Director task. Use normal research/shopping capabilities unless the equipment question is part of designing a generated or edited still image.

## Borderline Routing Rules

### "Cinematic" does not automatically mean video

If the requested deliverable is a still image, film frame, photograph, hero frame, keyframe, poster frame without typography, or reference image, this skill remains primary even if the user describes it as a film shot.

### A still intended for later animation remains a still task

If the current request is to establish the frozen hero frame before animation, this skill owns the current task. Do not prematurely convert it into a temporal video workflow.

### Storyboards

Use this skill for the **visual design and realism of individual storyboard frames**. A separate storytelling/video capability may own sequence logic, shot order, timing, or complete storyboard orchestration.

### Product campaigns

Use this skill for photographic/cinematic product imagery. Do not redesign the product unless the user explicitly requests product redesign.

### Reference recreation

Use this skill when matching the photographic language of a still reference. Do not claim exact camera/lens metadata unless it is supplied or otherwise known. Observable visual behavior is more important than pretending to identify hardware.

## Authority Priority

For still-image work, apply this order:

1. current explicit user instructions;
2. user-specified locked visual/camera parameters;
3. preservation requirements from supplied images/references;
4. task-specific cinematic/realism rules in this package;
5. AUTO inference for everything genuinely unspecified;
6. provider-specific adaptation only after the visual intent is established.

Provider quirks must not silently override user locks or rewrite the creative intent.

## V1 Medium Boundary

V1 is intentionally centered on **still images**.

Video knowledge may appear only when it directly changes a frozen-frame decision, for example:

- shutter-induced motion blur visible in the still;
- choosing a hero frame that will later be animated;
- avoiding a still-image choice that would make later image-to-video work obviously unstable, when the user explicitly says animation is the next step.

Full temporal filmmaking, video generation choreography, editing, sound, pacing, and delivery remain outside V1's primary scope.

## Routing Acceptance Examples

### Should activate

- "Create a realistic cinematic image of a father and child playing in desert sand."
- "This looks AI. Keep the composition and person identical, but make it look photographed."
- "Alexa 35, 35mm, T2, low angle. Choose the rest."
- "Analyze this film frame and give me a reusable visual recipe."
- "Turn this ordinary prompt into a grounded feature-film still."
- "Give me only the Gemini image prompt for this shot."

### Should not activate as primary authority

- "Remove pauses and mistakes from this talking-head video."
- "Make a 30-second sequence with three camera moves and timed action."
- "Build me a responsive landing page."
- "Create a bar chart from this CSV."
- "Design a flat vector logo."
- "What is the current retail price of an ARRI camera?"

## Scope Change Rule

Any future expansion that makes the skill primarily responsible for temporal video generation, video editing, UI/interface design, or unrelated image-design categories is a scope change and must be explicitly approved rather than silently added during implementation.
