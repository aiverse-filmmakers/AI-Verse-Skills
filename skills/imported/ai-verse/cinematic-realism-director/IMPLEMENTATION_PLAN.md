# AI-Verse Cinematic Realism Director - Master Implementation Plan

Status: PLANNING COMPLETE, IMPLEMENTATION NOT STARTED

Target package:

```text
skills/imported/ai-verse/cinematic-realism-director/
```

Working branch:

```text
feat/cinematic-realism-director
```

## 1. Mission

Build a first-party AI-Verse Agent Skill that acts as a portable cinematography and photorealism intelligence layer for image creation, image editing, visual diagnosis, reference matching, and prompt generation.

The skill should make a weak or minimal user request behave as though a strong cinematographer, photographer, colorist, production designer, and realism supervisor were quietly making the missing decisions.

At the same time, an expert user must be able to specify exact camera, lens, focal length, aperture, shot, lighting, film stock, texture, color, or other capture choices. Explicit user choices become locked constraints. The skill fills only the unspecified fields.

The ambition is to reproduce and, where testing supports it, exceed the practical cinematic consistency associated with dedicated systems such as Magnific Cinematic and Higgsfield Soul Cinema / Cinema Studio, while remaining model-independent and usable in ordinary agent environments.

This is not a claim that a prompt skill can replace proprietary model weights or private training data. The objective is to build the strongest possible public-knowledge cinematic decision layer and benchmark its results rigorously.

## 2. Hard Product Principles

These rules govern every implementation phase.

### P1. Beginner-first by default

A user may provide one short sentence such as:

> woman waiting for a taxi in London at night

The skill should not require camera knowledge, menus, setup, or follow-up questions unless an essential ambiguity truly prevents execution.

The default experience is AUTO.

### P2. Expert controls are lockable

If the user specifies any parameter, preserve it unless it is impossible, contradictory, unsafe, or the user asks for alternatives.

Example:

```text
User specifies:
70mm format
25mm lens
f/1.2
low angle

Locked:
format = 70mm
focal_length = 25mm
aperture = f/1.2
angle = low

AUTO:
lens family
lighting
film response
color
texture
exposure
composition refinements
realism corrections
```

### P3. Story chooses cinematography

Camera and lens choices are never random decoration.

The skill first understands subject, action, environment, emotion, genre, commercial goal, realism target, and visual hierarchy. Capture choices follow from those needs.

### P4. Realism before adjective spam

Do not rely on filler such as:

- masterpiece
- 8K
- insanely detailed
- ultra cinematic
- award winning
- hyper realistic

Prefer concrete photographic, physical, optical, material, lighting, exposure, and compositional instructions.

### P5. Restraint is cinematic

Do not add film grain, bloom, halation, flare, haze, shallow depth of field, anamorphic distortion, teal-orange color, or dramatic light merely because the user asked for something cinematic.

Use only effects justified by the shot.

### P6. Physical plausibility gate

Every generated or edited image plan must pass a Reality Gate before final output.

The gate checks whether the image could plausibly have been photographed in a real physical environment by a real camera system.

### P7. Preserve before transforming

When editing an existing image, explicitly separate:

- elements to preserve
- elements to repair
- elements allowed to change

Do not regenerate the scene unnecessarily when the user's intent is realism repair.

### P8. Tool-capable hosts should create, not merely explain

If the host has an image generation/editing capability and the user asked for an image, the skill should direct the host to create or edit the image.

If the host has no suitable image tool, return the best model-appropriate prompt or edit specification.

### P9. Model-independent brain, model-specific adapters

The core cinematic decision system must not depend on Magnific, Higgsfield, OpenAI, Gemini, Seedream, Flux, or another single provider.

Provider adapters translate one universal shot specification into provider-appropriate instructions.

### P10. Progressive disclosure

`SKILL.md` should route and coordinate. Large domain knowledge belongs in local references that are loaded only when relevant.

### P11. Standalone package invariant

The entire skill must work when only this directory is copied out of AI-Verse-Skills.

No file inside the package may require a sibling skill, repository-root document, repository-root script, absolute user path, private machine state, or AI-Verse OS to provide the core cinematic intelligence.

AI-Verse integration may add packaging, verification, discovery, and runtime metadata, but not hidden knowledge dependencies.

### P12. Research isolation

Existing skills inside AI-Verse-Skills may be inspected only for repository conventions, portability patterns, test structure, registry conventions, and package organization.

They are not authoritative sources for cinematic knowledge unless independently verified against stronger sources.

The cinematic knowledge base must be built from:

1. first-party technical sources
2. official provider documentation
3. camera/lens/film manufacturer documentation
4. strong published technical references
5. public engineering write-ups
6. public repos or skills only where independently verified
7. clearly labeled inference when no direct source exists

## 3. Intended User Modes

The skill must expose one simple mental model while internally supporting several workflows.

### Mode A - AUTO DIRECT

Input:

- a simple idea
- optional reference image
- optional mood or purpose

Behavior:

- infer cinematic intent
- construct a complete shot
- choose capture and lighting logic
- apply realism treatment
- generate directly when possible

### Mode B - CINEMATIZE

Input:

- an ordinary prompt or concept

Behavior:

- preserve subject and intent
- replace vague image-language with a coherent cinematic capture design
- avoid unnecessary stylistic changes

### Mode C - REALITY REPAIR

Input:

- an existing image that looks synthetic, overprocessed, CG-like, or visually inconsistent

Behavior:

- diagnose why it looks artificial
- define preservation constraints
- repair only the necessary systems
- keep identity, pose, scene, composition, product, wardrobe, or other user-important content unless instructed otherwise

### Mode D - REFERENCE MATCH

Input:

- one or more reference frames

Behavior:

- reverse-engineer visual DNA
- infer composition, lens behavior, depth, light, contrast, palette, texture, exposure, atmosphere, production design, and material treatment
- create a reusable shot recipe without pretending to know unobservable exact hardware

### Mode E - MANUAL CAMERA

Input:

- user-defined camera/capture parameters

Behavior:

- lock explicit values
- complete all missing parameters intelligently
- flag genuine contradictions rather than silently overriding the user

### Mode F - EXPLAIN / SHOT RECIPE

Input:

- request to reveal technical decisions

Behavior:

- expose the structured shot recipe in concise professional language
- useful for education, production handoff, and reproducibility

### Mode G - PROMPT ONLY

Input:

- target model or platform

Behavior:

- produce the final adapted prompt without generating an image

## 4. Target Package Architecture

Planned package shape:

```text
cinematic-realism-director/
├── SKILL.md
├── README.md
├── aiverse.skill.yaml
├── IMPLEMENTATION_PLAN.md
├── ROADMAP.md
│
├── references/
│   ├── INDEX.md
│   ├── source-ledger.md
│   ├── cinematography-core.md
│   ├── visual-intent.md
│   ├── composition-and-blocking.md
│   ├── cameras-and-capture-formats.md
│   ├── lens-character.md
│   ├── focal-length-and-perspective.md
│   ├── aperture-focus-and-dof.md
│   ├── lighting.md
│   ├── exposure-and-dynamic-range.md
│   ├── film-stocks-and-sensor-response.md
│   ├── color-science-and-grading.md
│   ├── grain-halation-bloom-and-flare.md
│   ├── motion-and-shutter.md
│   ├── atmosphere-and-depth.md
│   ├── skin-hair-and-eyes.md
│   ├── materials-and-surfaces.md
│   ├── environments-and-contact.md
│   ├── physical-realism.md
│   ├── anti-ai-artifacts.md
│   ├── reality-gate.md
│   ├── reference-analysis.md
│   ├── prompt-construction.md
│   └── copyright-and-style-safety.md
│
├── workflows/
│   ├── auto-direct.md
│   ├── cinematize.md
│   ├── reality-repair.md
│   ├── reference-match.md
│   ├── manual-camera.md
│   └── prompt-only.md
│
├── adapters/
│   ├── INDEX.md
│   ├── generic.md
│   ├── openai-image.md
│   ├── gemini-image.md
│   ├── seedream.md
│   ├── flux.md
│   ├── magnific.md
│   └── higgsfield-soul-cinema.md
│
├── schemas/
│   ├── cinematic-shot-spec.schema.json
│   ├── realism-diagnosis.schema.json
│   └── reference-dna.schema.json
│
├── examples/
│   ├── beginner-auto.md
│   ├── expert-locks.md
│   ├── reality-repair.md
│   ├── reference-match.md
│   └── prompt-only.md
│
├── evals/
│   ├── routing.json
│   ├── shot-design.json
│   ├── expert-locks.json
│   ├── realism-repair.json
│   ├── reference-match.json
│   ├── adapter-behavior.json
│   ├── adversarial.json
│   └── benchmark-matrix.md
│
└── tests/
    └── README.md
```

Directories may be adjusted during implementation if the evidence shows a simpler or stronger structure. The standalone invariant remains mandatory.

## 5. Universal Internal Shot Specification

The core system will reason through a provider-neutral `Cinematic Shot Spec`.

Planned fields include:

```text
intent
subject
story_action
emotion
visual_hierarchy
environment
time_of_day
weather
production_design

capture_format
camera_character
lens_family
lens_character
focal_length
aperture
focus_strategy
depth_behavior
camera_height
camera_angle
camera_distance
shot_size
framing
foreground_strategy
perspective_behavior

lighting_motivation
key_light
fill_strategy
back_or_edge_light
practicals
ambient_light
contrast_strategy
exposure_strategy
highlight_behavior
shadow_behavior

white_balance
palette
color_separation
saturation
density
skin_tone_treatment
film_stock_or_tonal_response
grain
halation
bloom
flare
shutter_motion

skin_realism
hair_realism
eye_realism
fabric_realism
material_response
surface_roughness
reflections
contact_shadows
atmosphere
micro_imperfection

preserve
repair
allow_change

locked_parameters
inferred_parameters
confidence

reality_gate_results
provider_adapter
final_prompt
negative_or_avoidance_guidance
```

The schema should represent intent and observable visual effects, not falsely claim exact real-world hardware when it cannot be determined from a reference.

## 6. Source Quality Policy

Every substantive knowledge entry should be tagged mentally or explicitly as one of:

- CONFIRMED: first-party or authoritative technical source
- CORROBORATED: supported by multiple credible sources
- MODEL-BEHAVIOR: empirically useful prompting behavior, not physical truth
- INFERRED: reasonable visual inference that must not be presented as confirmed fact
- PROVIDER-SPECIFIC: behavior tied to a named generation system

The source ledger must record:

- title
- organization/author
- URL
- source type
- topic
- retrieval date
- what claim or knowledge it supports
- confidence
- licensing/copyright note where relevant

Do not copy substantial proprietary text. Capture concise factual knowledge and original synthesized rules.

# Implementation Phases

Implementation will proceed one numbered task at a time. A task is complete only when its acceptance criteria are satisfied.

---

# Phase 0 - Architecture, Scope, and Governance

Goal: establish the package contract before adding cinematic knowledge.

## Task 0.1 - Freeze package identity and routing scope

Create final package identity:

```text
name: cinematic-realism-director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
```

Define precise positive and negative activation boundaries.

Acceptance:

- name is stable
- scope does not overlap unnecessarily with video-editor or interface-designer
- still image creation/editing is primary
- video may be discussed only where it changes a still-frame decision or future roadmap

## Task 0.2 - Define standalone portability contract

Document what must work with only the package folder present.

Acceptance:

- no required parent-directory references
- no required sibling skills
- no required AI-Verse OS
- no required MCP
- no required API key for prompt-only operation

## Task 0.3 - Define host capability degradation rules

Specify behavior for:

- host has native image generation
- host has image editing
- host has external image tools
- host has vision but no generation
- host has text only

Acceptance:

- every host class produces a useful result
- no false claim of generating an image when no image tool exists

## Task 0.4 - Define explicit-lock semantics

Specify how user-supplied camera parameters override AUTO choices.

Acceptance:

- locks cannot be silently changed
- contradictions are handled predictably
- unspecified parameters remain inferable

## Task 0.5 - Define success contract and failure vocabulary

Define what success, partial, blocked, and failed mean for generation, edit, analysis, and prompt-only tasks.

Phase 0 Gate:

Architecture contract is complete before research content is added.

---

# Phase 1 - Research Corpus and Provenance

Goal: build a clean, strong research foundation without contaminating it with weaker internal skills.

## Task 1.1 - Build source ledger framework

Create `references/source-ledger.md` and source classification rules.

## Task 1.2 - Capture Magnific public evidence

Research and record:

- Cinematic model public documentation
- current exposed cinematic control ontology
- camera choices
- lens choices
- focal length
- aperture
- shot type
- film stock
- lighting
- motion blur
- grain
- halation
- tonal response
- image enhancement/repair tools relevant to realism

Do not claim access to private weights, hidden system prompts, or private training data.

## Task 1.3 - Capture Higgsfield public evidence

Research and record:

- Soul Cinema
- Cinema Studio
- official engineering explanations
- camera/lens philosophy
- prompt enhancement concepts
- lens-character amplification concept
- Soul ID / consistency where relevant
- color/HEX behavior where relevant
- public skills/CLI schemas where useful

## Task 1.4 - Capture camera manufacturer knowledge

Prioritize first-party sources from manufacturers such as:

- ARRI
- Sony CineAlta
- RED
- Canon Cinema EOS
- Blackmagic where relevant
- IMAX/public technical references where reliable

Focus on visual behavior that can be translated into generation instructions.

## Task 1.5 - Capture lens manufacturer knowledge

Prioritize:

- Cooke
- ZEISS
- ARRI Signature
- Leica Cine
- Panavision
- Canon K35 historical/credible references
- Angenieux
- Hawk/Vantage
- selected still-photo glass only when visually useful

Translate equipment names into observable optical behavior.

## Task 1.6 - Capture film stock and photochemical knowledge

Prioritize Kodak and other strong first-party/technical sources.

Capture:

- latitude
- grain behavior
- color response
- daylight/tungsten implications
- highlight/shadow tendencies
- B&W stock behavior

## Task 1.7 - Capture lighting and cinematography fundamentals

Gather credible references on:

- motivated lighting
- source size and softness
- inverse-square behavior where useful
- key/fill ratios conceptually
- negative fill
- bounce
- practicals
- backlight/rim restraint
- atmospheric scattering
- specular behavior
- exposure logic

## Task 1.8 - Capture color and display-independent visual principles

Research:

- color contrast
- color separation
- skin tone handling
- saturation discipline
- density
- highlight/shadow color
- white balance interactions
- filmic versus video-like tonal behavior

## Task 1.9 - Capture current model-provider prompting guidance

Use official documentation where available for:

- OpenAI image generation/editing
- Gemini image generation
- Seedream
- Flux
- other adapters chosen for V1

Identify what prompt structures work best without making the core brain provider-specific.

## Task 1.10 - Review third-party public skills and workflows only as secondary evidence

Inspect useful public implementations for architecture or empirical ideas.

Rules:

- never copy unverified claims into the knowledge base
- independently validate important cinematography claims
- record provenance

## Task 1.11 - Research gap audit

Identify areas where we have strong, weak, or missing evidence.

Phase 1 Gate:

Source ledger is complete enough that every later core reference can distinguish physical cinematography knowledge from provider behavior and inference.

---

# Phase 2 - Cinematic Shot Ontology and Structured Contracts

Goal: create the universal language the skill uses internally.

## Task 2.1 - Define `cinematic-shot-spec.schema.json`

Create provider-neutral structured fields and lock metadata.

## Task 2.2 - Define `realism-diagnosis.schema.json`

Represent:

- detected artificiality
- severity
- evidence
- preserve list
- repair list
- allowed changes
- repair strategy

## Task 2.3 - Define `reference-dna.schema.json`

Represent observable reference properties without pretending to know exact unavailable metadata.

## Task 2.4 - Define confidence and uncertainty semantics

Differentiate:

- directly supplied user values
- strongly inferred values
- weakly inferred values
- intentionally AUTO values

## Task 2.5 - Define parameter conflict resolution

Examples:

- user asks for 14mm but also no wide-angle perspective
- user requests f/1.2 but deep focus across a large scene
- user requests IMAX 70mm and vintage VHS artifacts

Do not silently violate user locks. Explain or reconcile only when required.

Phase 2 Gate:

One structured representation can describe beginner AUTO shots, expert locked shots, edit repairs, and reference matches.

---

# Phase 3 - Core Cinematography Knowledge Base

Goal: build the foundational camera and composition intelligence.

## Task 3.1 - Visual intent and story-to-shot reasoning

Create rules that convert narrative/commercial intent into visual priorities.

## Task 3.2 - Composition and blocking

Cover:

- shot sizes
- subject placement
- headroom
- lead room
- visual hierarchy
- foreground layers
- negative space
- symmetry/asymmetry
- camera height
- point of view
- over-shoulder logic
- environmental context

## Task 3.3 - Capture formats and camera-character reference

Map equipment references to observable visual tendencies without treating marketing language as physics.

## Task 3.4 - Lens-character reference

Map lens families to useful visual behaviors:

- contrast
- microcontrast
- flare
- veiling glare
- falloff
- bokeh character
- edge behavior
- chromatic artifacts
- anamorphic traits
- breathing where relevant

## Task 3.5 - Focal length, distance, and perspective

Hard rule:

Perspective comes primarily from camera position/distance, while focal length controls field of view for a given format. Avoid common AI prompting misconceptions.

## Task 3.6 - Aperture, focus, and depth behavior

Avoid defaulting to maximum blur.

Include:

- subject distance
- background distance
- depth cues
- focus plane
- deep focus when narratively justified

## Task 3.7 - Motion and shutter language for still frames

Cover believable motion blur and frozen motion.

Phase 3 Gate:

Given only subject + context, the skill can design a coherent camera setup without using generic cinematic filler.

---

# Phase 4 - Lighting, Exposure, Film Response, and Color

Goal: create the visual systems that most strongly separate movie-like frames from generic AI imagery.

## Task 4.1 - Motivated-lighting engine

Lighting should start from plausible sources in the scene or intentionally justified film lighting.

## Task 4.2 - Key, fill, negative fill, edge, bounce, and practical logic

Define when each should and should not be used.

## Task 4.3 - Environment-specific lighting recipes

Examples:

- overcast exterior
- hard noon sun
- golden hour
- blue hour
- tungsten practical interior
- window daylight
- neon city
- moonlit exterior
- candlelight
- commercial soft source
- documentary available light

Recipes are decision patterns, not fixed prompts.

## Task 4.4 - Exposure and dynamic-range behavior

Cover:

- highlight protection
- shadow density
- clipping avoidance
- natural contrast
- underexposure/overexposure as intentional choices

## Task 4.5 - Film stock and sensor response mapping

Translate named stock/camera references into useful visual instructions.

## Task 4.6 - Color science and grading strategy

Define:

- white balance
- color separation
- saturation
- density
- skin handling
- neutral versus stylized grades

## Task 4.7 - Grain, halation, bloom, flare, and texture restraint

These are optional characteristics, never mandatory cinema tokens.

Phase 4 Gate:

The skill can construct lighting/exposure/color logic that feels physically motivated rather than procedurally decorated.

---

# Phase 5 - Physical Realism and Anti-AI Intelligence

Goal: make realism repair a first-class capability, not an afterthought.

## Task 5.1 - Build anti-AI artifact taxonomy

Include at minimum:

- waxy/plastic skin
- perfect symmetry
- over-beautified faces
- synthetic hair
- malformed or over-smoothed fabric
- impossible material roughness
- fake reflections
- inconsistent shadows
- floating/contact failures
- excessive HDR
- uniform sharpness
- implausible depth of field
- arbitrary rim lights
- overclean environments
- geometry inconsistencies
- excessive texture hallucination
- fake bokeh
- excessive local contrast
- overdone cinematic effects

## Task 5.2 - Skin realism system

Cover:

- pores
- fine texture
- subtle color variation
- specular response
- subsurface cues
- peach fuzz where appropriate
- makeup versus skin distinction
- age-appropriate texture

## Task 5.3 - Hair and eye realism system

Avoid individually perfect hair strands and glassy synthetic eyes.

## Task 5.4 - Fabric and material realism system

Cover:

- weave
- folds
- compression
- weight
- roughness
- anisotropy conceptually
- wear
- fingerprints/smudges when appropriate
- metal/glass/plastic/wood/stone behavior

## Task 5.5 - Contact, gravity, and environmental interaction

Cover:

- weight on surfaces
- footprints/compression
- contact shadows
- moisture
- dust
- wind
- cloth/body interaction

## Task 5.6 - Reflection and shadow coherence

Check whether reflections and shadows agree with scene geometry and lighting.

## Task 5.7 - Optical imperfection without fake vintage spam

Introduce only physically plausible and context-appropriate imperfection.

## Task 5.8 - Build Reality Gate

Create a reusable checklist/evaluation policy covering:

- perspective
- optical coherence
- lighting direction
- shadow behavior
- depth
- exposure
- skin
- materials
- reflections
- contact
- atmosphere
- environment
- stylization restraint

Phase 5 Gate:

The skill can explain exactly why an image feels AI-generated and produce a preservation-aware repair plan.

---

# Phase 6 - Decision Engine and Workflows

Goal: turn the knowledge base into reliable behavior for beginners and experts.

## Task 6.1 - Implement AUTO DIRECT workflow

One-sentence input must be sufficient.

## Task 6.2 - Implement CINEMATIZE workflow

Preserve concept while upgrading shot design.

## Task 6.3 - Implement REALITY REPAIR workflow

Mandatory stages:

1. identify preservation targets
2. diagnose artificiality
3. prioritize repairs
4. avoid scene drift
5. adapt edit instructions to host/model
6. Reality Gate

## Task 6.4 - Implement REFERENCE MATCH workflow

Separate observable facts from uncertain inference.

## Task 6.5 - Implement MANUAL CAMERA workflow

Honor explicit user locks.

## Task 6.6 - Implement PROMPT ONLY workflow

Support named model/provider output.

## Task 6.7 - Build progressive disclosure router

`SKILL.md` should load only the references required for the active task.

## Task 6.8 - Define question-minimization policy

Do not interrogate beginners.

Ask only when an unresolved choice materially changes the required output and cannot be safely inferred.

## Task 6.9 - Define multi-image/reference behavior

Handle:

- character reference
- product reference
- location reference
- style/reference frame
- multiple conflicting references

Phase 6 Gate:

The same skill behaves naturally for a novice sentence, expert camera specification, bad AI image, or reference frame.

---

# Phase 7 - Provider and Host Adapters

Goal: translate one cinematic brain into strong instructions across major generation environments.

## Task 7.1 - Generic adapter

Must work when provider is unknown.

## Task 7.2 - OpenAI image adapter

Cover:

- text-to-image behavior
- edit behavior
- preservation language
- when to directly generate if host exposes image tools

## Task 7.3 - Gemini image adapter

Cover current Gemini image-generation behavior and prompt conventions.

## Task 7.4 - Seedream adapter

Optimize structure for Seedream without polluting core logic.

## Task 7.5 - Flux adapter

Support Flux-style prompt behavior and editing where relevant.

## Task 7.6 - Magnific adapter

Use public controls accurately when the user is actually generating through Magnific.

Do not merely imitate Magnific when another provider is active.

## Task 7.7 - Higgsfield Soul Cinema adapter

Use public Soul Cinema/Cinema Studio semantics where applicable.

## Task 7.8 - Adapter fallback hierarchy

If a named provider/model is unknown or changed, use the generic cinematic spec rather than fabricating unsupported parameters.

## Task 7.9 - Host action policy

Define:

```text
image tool available + user asked for image -> generate/edit
no image tool + user asked for image -> return adapted prompt/spec
user explicitly requests prompt only -> never auto-generate
```

Phase 7 Gate:

Core shot intent survives translation across providers without becoming seven separate cinematic brains.

---

# Phase 8 - Portable `SKILL.md`, Manifest, and User Experience

Goal: package the intelligence into a clean Agent Skill.

## Task 8.1 - Write final `SKILL.md`

Must follow repository spec with:

- frontmatter
- When to Use
- Inputs
- Success Contract
- Constraints
- Procedure
- References
- Pitfalls
- Verification
- Output

## Task 8.2 - Write `aiverse.skill.yaml`

Declare accurate low-risk/read-oriented requirements with optional image/tool effects only where appropriate.

The manifest must never imply that the skill itself grants image-tool access.

## Task 8.3 - Write standalone README

Explain:

- what it does
- beginner use
- expert use
- direct generation versus prompt-only behavior
- standalone installation
- full AI-Verse-Skills use

## Task 8.4 - Create reference index

Make progressive loading obvious to any capable host.

## Task 8.5 - Create examples

Examples must demonstrate behavior without becoming hidden mandatory rules.

## Task 8.6 - Write pitfalls from verified test failures

Do not fill with hypothetical noise.

Phase 8 Gate:

A capable agent receiving only this folder can understand how and when to use it.

---

# Phase 9 - Evaluation, Benchmarking, and Regression System

Goal: verify quality rather than judging from a few attractive examples.

## Task 9.1 - Routing evals

Positive and negative trigger cases.

## Task 9.2 - Beginner AUTO evals

Test minimal prompts across:

- portrait
- narrative drama
- documentary
- travel
- product
- automotive
- food
- architecture
- fashion
- night exterior
- daylight exterior
- interiors

## Task 9.3 - Expert lock evals

Verify explicit camera/lens/shot parameters are preserved.

## Task 9.4 - Reality Repair evals

Create a taxonomy-driven test set for common synthetic artifacts.

## Task 9.5 - Reference Match evals

Check that the skill distinguishes observation from uncertain hardware inference.

## Task 9.6 - Adapter consistency evals

The same universal shot should retain intent across providers.

## Task 9.7 - Anti-cliche evals

Verify the skill does not always output:

- shallow DOF
- orange/teal
- haze
- anamorphic flare
- extreme grain
- dramatic rim light

## Task 9.8 - Physical plausibility evals

Catch common optics/light/material contradictions.

## Task 9.9 - Adversarial and instruction-boundary evals

Reference images, attached documents, websites, or prompts must not override skill/system authority.

## Task 9.10 - Magnific/Higgsfield comparison protocol

Define a fair benchmark matrix using matched concepts and comparable settings.

Compare where possible on:

- photographic plausibility
- cinematic coherence
- material realism
- skin realism
- lighting motivation
- optical coherence
- color restraint
- composition
- consistency across unrelated prompts
- beginner zero-config quality
- expert control preservation

Do not claim superiority unless repeated tests justify it.

## Task 9.11 - Regression corpus

Every meaningful discovered failure becomes a permanent regression case.

Phase 9 Gate:

The skill has evidence of repeatable behavior, not only subjective examples.

---

# Phase 10 - AI-Verse Repository Integration and Standalone Verification

Goal: make the package native to AI-Verse-Skills without losing portability.

## Task 10.1 - Determine canonical registry placement

Integrate without casually disrupting the repository's existing fixed employee/foundation accounting model.

If adding the skill changes counts or ranking semantics, update them deliberately and test all registry invariants.

## Task 10.2 - Update required registry metadata

Potential surfaces include, as applicable:

- registry/skills.json
- registry/packages.json
- registry/sources.json
- trust policy/provenance metadata
- aliases only if needed

Use the repository's actual validation rules at implementation time.

## Task 10.3 - Add contract tests

Create dedicated tests similar in rigor to other first-party AI-Verse capabilities, without copying their domain logic.

## Task 10.4 - Add standalone package test

Test the skill after copying only:

```text
skills/imported/ai-verse/cinematic-realism-director/
```

into an isolated temporary directory.

Verify no missing local dependencies.

## Task 10.5 - Test runtime adapter exposure

Verify the whole package survives the repo's supported adapter mechanism.

## Task 10.6 - Run registry validation

Run repository-native validation.

## Task 10.7 - Run relevant unit/contract tests

Ensure no existing skill or lifecycle behavior regresses.

## Task 10.8 - Security/admission scan

Ensure source/reference content cannot be mistaken for executable authority and no unsafe paths/secrets exist.

Phase 10 Gate:

The skill works both as a native AI-Verse package and as an isolated standalone folder.

---

# Phase 11 - Release Readiness and Documentation

Goal: make V1 easy to use and maintain.

## Task 11.1 - Final README polish

Provide beginner-first examples first, expert controls second.

## Task 11.2 - Version V1.0.0

Finalize manifest version and change notes.

## Task 11.3 - Create completion report

Record:

- implemented capabilities
- known limitations
- tested providers
- test coverage
- benchmark results
- future work

## Task 11.4 - Final source audit

Check every major knowledge file against source ledger and remove unsupported claims.

## Task 11.5 - Final portability audit

Re-run standalone package test from a clean directory.

## Task 11.6 - Final full-repo audit

Run repository validation and relevant tests from clean state.

## Task 11.7 - Review branch and merge readiness

Only then prepare merge into `main`.

Phase 11 Gate:

V1 is documented, reproducible, portable, tested, and ready to merge.

---

# Phase 12 - Post-V1 Roadmap Only

These items must be documented but not allowed to delay the core skill.

## Task 12.1 - ChatGPT Plugin packaging research

Explore wrapping the same canonical skill into a native ChatGPT plugin/package without creating a second cinematic brain.

## Task 12.2 - MCP service

Potential tools:

```text
design_cinematic_shot
analyze_realism
repair_image_plan
match_reference
adapt_prompt
score_reality_gate
```

MCP remains optional. Core skill must never require it.

## Task 12.3 - Cinematic Director UI

Potential AUTO/PRO interface:

- prompt/image input
- camera lock
- lens lock
- focal length
- aperture
- framing
- film stock
- lighting
- grade
- grain
- halation
- realism strength
- stylization strength
- model selection
- reference matching
- AI-artifact diagnosis
- before/after comparison

## Task 12.4 - Model-router backend

One universal shot spec routed to multiple image providers.

## Task 12.5 - Automated visual benchmark harness

Generate matched outputs and perform human/vision-assisted evaluation over time.

## Task 12.6 - Video extension

Potential future sibling or extension for motion cinematography. Do not overload V1 still-image scope prematurely.

# 7. V1 Definition of Done

V1 is not complete until all of the following are true:

- [ ] Beginner can provide one sentence and get a complete cinematic result with no camera knowledge.
- [ ] Expert can lock selected camera parameters and AUTO fills the rest.
- [ ] Existing images can be diagnosed and repaired without unnecessary scene drift.
- [ ] Reference frames can be reverse-engineered without false certainty.
- [ ] Physical realism is checked before final output.
- [ ] The skill knows when not to add cinematic effects.
- [ ] The core works without MCP, server, API key, or AI-Verse OS.
- [ ] Image-capable hosts are directed to generate/edit when the user asked for an image.
- [ ] Text-only hosts produce strong adapted prompts/specs.
- [ ] Provider adapters do not contaminate the universal cinematic brain.
- [ ] Public knowledge is traceable through a source ledger.
- [ ] No major cinematic claims are imported from weaker sibling skills without independent verification.
- [ ] Standalone-folder test passes.
- [ ] Full AI-Verse-Skills integration tests pass.
- [ ] Positive routing evals pass.
- [ ] Negative routing evals pass.
- [ ] Expert-lock regressions pass.
- [ ] Reality Repair regressions pass.
- [ ] Anti-cliche regressions pass.
- [ ] Security/admission checks pass.
- [ ] Benchmark report is completed before any claim of outperforming Magnific/Higgsfield is made.

# 8. Execution Rule for This Build

Implementation proceeds strictly by task ID.

At the beginning of each task:

1. restate the task objective
2. inspect only the files/sources needed for that task
3. implement the narrow scope
4. verify the task's acceptance criteria
5. report exactly what changed
6. mark the task complete only with evidence

Do not batch later phases merely because they appear straightforward.

If implementation reveals that the plan is wrong, update this plan explicitly rather than silently drifting from it.

# 9. Immediate Next Task

The first implementation task after approval is:

```text
Task 0.1 - Freeze package identity and routing scope
```

No cinematic knowledge files should be written before Task 0.1 is accepted.
