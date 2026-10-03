# Phase 1 Research - Higgsfield Soul Cinema and Cinema Studio

Status: RESEARCH EVIDENCE

Primary classification: `PROVIDER-SPECIFIC`, `MODEL-BEHAVIOR`, with engineering/product facts marked `CONFIRMED` when supported by Higgsfield first-party sources.

This file records public evidence about Higgsfield's cinematic image-generation approach. It does not claim access to private prompts, weights, training data, or proprietary enhancement logic.

## Why Higgsfield Matters to This Skill

Higgsfield is valuable for a different reason than Magnific.

Magnific exposes a rich control ontology. Higgsfield's public engineering material explains **why** technical cinematography vocabulary and a virtual-camera abstraction can improve generative results and how the team turned professional camera/lens language into a usable creative system.

That engineering philosophy strongly supports building a decision layer rather than a prompt suffix.

## Core Engineering Evidence

Primary source: `HIG-001`, Higgsfield's official engineering article about building Cinema Studio.

The article publicly describes several important development observations:

1. Prompt engineers noticed that prompts containing real cinematography language around cameras, lenses, optics and light often produced unusually cinematic outputs.
2. They dissected strong prompts line by line rather than treating `cinematic` as a magical adjective.
3. They reasoned that contemporary image/video models have encountered camera, lens and lighting concepts in their training distributions, so technical terms can act as useful learned visual priors.
4. They tested camera/lens combinations with a former director of photography and working camera operators.
5. Early lens choices did not always look sufficiently distinct, so the team deliberately pulled out and amplified the recognizable character of different lenses until the visual distinction was useful to creators.
6. The control system evolved from camera/lens/focal-length ideas toward aperture and broader cinematography controls.
7. A prompt-enhancement layer was built so a user with a short or technically imperfect prompt could still get a strong first batch.
8. The system treats a coherent camera/lens package as part of a project-level visual language rather than a random token per generation.

## Critical Interpretation

The strongest lesson is **not** that naming expensive cameras automatically creates realism.

The stronger architecture is:

```text
creative intent
-> choose observable cinematographic behavior
-> map that behavior to camera/lens/light concepts
-> translate for the active model
-> enhance incomplete user input
-> evaluate whether the result actually expresses those traits
```

The skill therefore needs a real cinematography decision layer, not just a dictionary of gear names.

## Lens-Character Amplification

Higgsfield publicly says that lens choices were initially insufficiently distinguishable and that recognizable lens character was intentionally amplified.

This is a major generative-media insight.

A real-world lens may differ subtly in:

- contrast;
- focus falloff;
- flare;
- bokeh;
- distortion;
- edge behavior;
- chromatic artifacts;
- anamorphic geometry;
- breathing;
- veiling glare.

A generative model may not reproduce those differences reliably from a lens name alone. Therefore our future lens knowledge should store:

1. the real-world evidence;
2. the **observable visual cues** that express it;
3. a restrained generative translation that may make the character legible without becoming caricature.

The translation must be calibrated by evals. `Amplify` does not mean `exaggerate every artifact`.

## Prompt Enhancement / Beginner AUTO

The public Cinema Studio engineering explanation describes enhancement intended to turn short, weak or physically awkward prompts into stronger first-pass generations.

This supports our beginner-first architecture.

Example user input:

```text
woman waiting alone at a bus stop in the rain
```

The user should not need to add:

```text
camera + lens + light + stock + contrast + material response + depth + atmosphere
```

The skill should infer those systems internally.

However, unlike an opaque `magic prompt` system, our implementation should keep the universal shot specification inspectable for expert users and tests.

## Soul Cinema

Sources: `HIG-002`, `HIG-004`, `HIG-007`.

Higgsfield publicly positions Soul Cinema as a specialized cinematic still-image path within the Soul family.

Publicly documented or officially routed concepts include:

- cinematic still generation as a distinct use case;
- rich photographic texture;
- skin/material detail and less synthetic cleanliness;
- film-grain aesthetics;
- cinematic depth/focus behavior;
- lighting/shadow treatment;
- natural/spontaneous photographic character;
- 1.5K and 2K quality tiers in current public tooling;
- interoperability with Soul identity/color systems where applicable.

These claims are product/provider evidence, not proof of exact physical camera simulation.

## Soul ID

Source: `HIG-003`.

Soul ID is Higgsfield's identity-consistency mechanism, using a trained/reusable character representation derived from a collection of images.

**Architectural lesson for our skill:** identity consistency is a distinct axis from cinematography. A cinematic director must preserve identity assets when they exist rather than constantly redefining the person stylistically.

Our standalone skill will not depend on Soul ID, but provider adapters should respect identity-reference systems exposed by the active platform.

## Soul HEX / Color Systems

Higgsfield publicly exposes Soul HEX/palette-oriented controls within the Soul ecosystem.

**Architectural lesson:** color continuity may be represented independently of camera/lens. Our universal shot spec should distinguish:

- white balance;
- palette;
- hue relationships;
- saturation;
- luminance/density;
- highlight/shadow chroma;
- skin treatment.

Do not collapse all of those into a named LUT or movie-look token.

## Cinema Studio Control Philosophy

Sources: `HIG-005`, `HIG-006`.

Current Cinema Studio documentation exposes a professional control surface around concepts such as:

- camera/capture references;
- lenses;
- aperture;
- lighting presets and adjustable light properties;
- color palettes;
- era/genre/tempo or related directorial controls depending on version;
- multiple reference inputs;
- hero-frame/reference-led workflows;
- movement controls for video contexts.

For this V1 still-image skill, temporal camera motion remains outside primary scope. The relevant carry-forward is the idea of a virtual camera department where image-generation decisions are organized into professional cinematography dimensions.

## Hero Frame Principle

Cinema Studio uses a hero-frame/key-image-first concept in broader workflows.

This strongly supports our still-focused V1 boundary:

- design the frozen frame properly first;
- establish visual DNA;
- only then hand it to a temporal/video system if animation is desired.

A good hero frame can therefore be a valid end product and a clean handoff object.

## Public Agent Skill Evidence

Source: `HIG-007`.

Higgsfield's official public `higgsfield-generate` Agent Skill currently routes:

- cinematic still frames toward Soul Cinema;
- Soul Character work toward Soul 2.0;
- environment/location-oriented work toward Soul Location;
- other general image tasks toward a different general-purpose image model.

**Architectural lesson:** not every image task deserves the same model. Our core skill should remain model-independent, while later provider/model routing can choose the most suitable renderer when a host exposes several.

The official skill is useful evidence for current provider routing and Agent Skill packaging. It is not used as a source for universal optics or lighting physics.

## Cinema Studio Versions and Third-Party Claims

A third-party public Higgsfield skill (`SEC-003`) contains extensive version-specific UI/API observations. It is useful for finding things to verify, but it is lower authority than Higgsfield's official docs and schemas.

Rules for our later adapter:

- never assume one Cinema Studio version's fields exist in another;
- never fabricate unpublished enum values;
- current provider schemas override remembered UI lists;
- adapter tests must be version-aware;
- do not copy third-party skill text or treat community values as permanent truth.

## What We Can Legitimately Learn from Higgsfield

Public evidence supports the following design conclusions:

1. Real cinematography vocabulary can be a useful learned prior for generative models.
2. The best results come from decomposing a shot into camera/optics/light decisions rather than adding generic quality adjectives.
3. Professional cinematographers/operators can help calibrate whether generated camera/lens behaviors are visually meaningful.
4. Named-lens differences may need translation into observable traits because model response to equipment names can be weak or inconsistent.
5. Short beginner prompts benefit from an intelligent enhancement/decision layer.
6. Identity consistency, color continuity and cinematography are separate concerns that should interoperate.
7. Hero-frame-first workflows are a strong bridge between still generation and later video generation.
8. Core creative logic should be able to survive changes in underlying generation models.

## What We Must NOT Claim

Do not state or imply that we know:

- the exact Higgsfield system prompt;
- the proprietary prompt enhancer text;
- model weights;
- private fine-tunes;
- training datasets;
- proprietary lens-profile coefficients;
- internal control weights;
- private data from DP/operator testing;
- undisclosed production infrastructure.

## Requirements Carried Forward

Later phases should incorporate:

- short-prompt AUTO completion;
- observable lens-character translation;
- camera/lens/aperture/light as independent but coherent choices;
- reference and identity preservation when provider supports it;
- color continuity independent of optics;
- hero-frame-quality stills as a first-class output;
- provider routing outside the universal brain;
- model/version drift checks;
- eval-driven calibration of how strongly lens/camera character should be expressed.

The objective is not to clone Higgsfield's hidden implementation. It is to build an original portable cinematic reasoning layer from the strongest public principles.