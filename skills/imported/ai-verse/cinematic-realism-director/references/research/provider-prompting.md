# Phase 1 Research - Current Image-Provider Prompting Guidance

Status: RESEARCH EVIDENCE

Retrieval date: 2026-10-03

Primary classification: `MODEL-BEHAVIOR` and `PROVIDER-SPECIFIC`.

This file records provider-specific prompting behavior for later adapters. It must not become the universal cinematography brain. The core skill should decide what the shot is first, then translate that shot into provider-appropriate instructions.

## Universal Provider-Adapter Rule

Always separate:

```text
CINEMATIC INTENT / SHOT SPEC
        ↓
PROVIDER ADAPTER
        ↓
MODEL-SPECIFIC PROMPT / CONTROLS
```

Do not design seven different cinematic brains around seven image models.

Provider behavior is time-sensitive and must be rechecked before release if the adapter depends on model names, exact parameters, or limits.

# OpenAI / GPT Image

Primary sources:

- OpenAI Image Prompting guide;
- OpenAI image generation documentation;
- OpenAI Academy image-generation guidance.

## Confirmed current prompting guidance

OpenAI recommends describing the intended result through concrete visible properties such as:

- subject;
- intended use;
- composition;
- aspect ratio/placement constraints;
- lighting;
- materials;
- colors;
- visual medium;
- framing;
- texture.

For complex requests, labeled sections or other structured layouts can improve maintainability. There is no required magical syntax.

Camera specifications should be treated as **appearance cues**, not guarantees of exact physical camera simulation.

For edits, OpenAI explicitly recommends separating:

```text
WHAT TO CHANGE
WHAT TO PRESERVE
```

and iterating with small targeted revisions when preservation matters.

## Adapter implications

The OpenAI adapter should:

- favor clear natural-language instructions;
- preserve the universal shot structure rather than keyword stuffing;
- use explicit photographic language when photorealism is intended;
- describe materials and physical light rather than only quality adjectives;
- state preservation constraints directly during edits;
- assign roles to multiple reference images when used;
- use iterative editing for Reality Repair when the host supports it;
- never claim that a camera/lens name guarantees physical emulation.

## Avoid

- giant comma-separated prestige-word lists;
- relying on `8K`, `masterpiece`, or `cinematic` instead of visible properties;
- assuming exact hardware simulation from camera names;
- broad `transform everything` wording when a targeted edit is required.

# Google Gemini Native Image Generation / Nano Banana Family

Primary source: Google AI for Developers image-generation documentation.

## Confirmed current behavior

Google's current native Gemini image models support conversational image generation and editing with text plus image inputs. Google's documentation presents image editing as natural-language modification of supplied images and recommends conversational/multi-turn refinement.

Current model names and tiers are volatile and belong in the future adapter, not the universal brain.

Google's examples rely on direct descriptions of:

- scene;
- layout;
- visible objects;
- materials;
- lighting;
- text/typography;
- spatial relationships;
- style;
- reference-image use.

## Adapter implications

The Gemini adapter should:

- preserve conversational natural-language instructions;
- describe scene relationships explicitly;
- use attached reference images directly when available;
- perform multi-turn edits rather than rewriting the entire image request when one change is needed;
- restate critical preservation constraints when drift appears;
- use the current host/model's supported reference behavior rather than assuming all Gemini image tiers have identical capabilities.

## Avoid

- hardcoding one Nano Banana model name permanently into the core skill;
- assuming reference count/quality limits are stable;
- replacing concrete spatial instructions with aesthetic tags only.

# ByteDance Seedream

Primary sources:

- ByteDance Seed official Seedream 5.0 Pro material;
- BytePlus/ModelArk Seedream 5.0 Pro/Flash interactive editing guide and API documentation.

## Confirmed current behavior

Seedream 5.0 Pro emphasizes:

- image-text alignment;
- structural coherence;
- professional production imagery;
- realistic physical lighting/material/skin rendering;
- multimodal/reference-conditioned generation;
- interactive precision editing;
- spatial grounding and regional semantics.

Current Seedream 5.0 Pro/Flash editing documentation supports precise target specification through normalized point and bounding-box coordinates embedded in prompts, alongside natural-language edit instructions.

The same guidance explicitly allows marking areas that must remain unchanged.

## Adapter implications

The Seedream adapter should:

- exploit precise spatial editing when host/tool support exposes it;
- convert preservation-sensitive repairs into explicit target regions plus unchanged regions when possible;
- retain natural-language scene/cinematography description around spatial controls;
- use reference images for structure/identity/material continuity when available;
- reserve exact model/API syntax for the adapter, not the core brain;
- treat spatial editing as especially useful for Reality Repair because it can reduce unnecessary whole-frame drift.

## Avoid

- assuming every Seedream host exposes coordinate/box controls;
- inventing API tags when a host only accepts ordinary language;
- using regional editing to change preservation-locked areas.

# Black Forest Labs FLUX

Primary sources:

- official Black Forest Labs documentation;
- official `black-forest-labs/skills` repository, `flux-image-best-practices`.

## Confirmed current guidance

Black Forest Labs' official agent-skill guidance recommends:

```text
Subject + Action/Pose + Style/Medium + Context/Setting + Lighting + Camera/Technical
```

for structured natural-language prompting.

The official guidance also states that FLUX image prompting should describe desired positive outcomes rather than rely on negative prompts, and supports detailed natural-language prompts, structured prompting, color specification, typography, and reference-based editing depending on model.

Current FLUX generations/editing are model-family specific, so adapter behavior must be tied to the actual available model rather than remembered legacy behavior.

## Adapter implications

The FLUX adapter should:

- translate avoidances into positive desired-state descriptions where the target model lacks negative prompting;
- front-load the important subject/action;
- keep lighting explicit;
- retain technical/camera cues near the end of the visual description;
- use reference-conditioned editing where supported;
- avoid generic negative-prompt blocks when unsupported;
- verify model-specific features at execution time when possible.

## Example translation principle

Universal constraint:

```text
avoid plastic skin and over-retouching
```

FLUX-positive translation:

```text
natural unretouched skin with visible pores, fine texture, subtle tonal variation and realistic specular response
```

The meaning remains the same while syntax changes.

# Magnific

See `research/magnific.md`.

Magnific differs from plain prompt-only systems because its Cinematic surface exposes discrete camera, lens, focal, aperture, shot, stock, lighting, blur, grain, halation and tonal controls.

Adapter rule:

- map universal shot-spec fields into actual exposed controls when the current control exists;
- describe unsupported nuances in prompt language;
- do not encode Magnific's control list into the universal ontology as if every provider supports it;
- do not imitate Magnific controls on another provider unless they translate into visible photographic behavior.

# Higgsfield Soul Cinema / Cinema Studio

See `research/higgsfield.md`.

Adapter rule:

- use Soul Cinema when the current Higgsfield routing explicitly calls for cinematic stills;
- treat equipment/control vocabulary as provider semantics, not proof of exact optical simulation;
- use current version-specific controls only after checking the active product surface;
- do not mix Cinema Studio versions or invent controls from obsolete versions.

# Generic Adapter Requirements

A generic adapter must remain strong even if the target provider is unknown.

Use a natural-language order such as:

1. subject and action;
2. environment and story context;
3. composition / camera position / shot size;
4. lens/focal/depth behavior;
5. motivated lighting and exposure;
6. color/tonal treatment;
7. skin/material/physical realism;
8. film/sensor texture where justified;
9. preservation constraints for edits;
10. explicit output/aspect-ratio constraints.

Do not depend on provider-only syntax.

# Cross-Provider Findings

## Strong common ground

Across current official guidance, these behaviors generalize well:

- concrete natural language beats empty prestige adjectives;
- describe visible spatial relationships;
- lighting needs explicit direction;
- materials and texture matter for photorealism;
- editing requires explicit preservation instructions;
- reference images should have clear roles;
- iterative targeted changes are safer than full rewrites for precision work;
- provider capabilities must be checked rather than assumed.

## Provider-specific differences

The adapter layer must handle differences such as:

- negative-prompt support;
- regional/coordinate editing;
- reference-image count/roles;
- explicit cinematic control panels;
- output resolution/aspect-ratio controls;
- literal camera/lens selectors versus prompt-only visual cues;
- multi-turn edit behavior;
- model-specific syntax and parameter names.

# Requirements Carried Forward

Phase 7 must:

- recheck current provider documentation before freezing adapters;
- never let adapter syntax overwrite user locks;
- fall back to `generic.md` when a provider/model is unknown;
- translate unsupported controls into observable language rather than fabricate parameters;
- keep prompt-only output usable even without API/tool access;
- distinguish provider capability from cinematic intent.

Phase 9 must test the same Cinematic Shot Spec through multiple adapters and verify that the visual intent survives translation.