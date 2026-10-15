# Cinematic Realism Director - Host Capability Contract

Status: RUNTIME POLICY

Purpose: define useful behavior across hosts with different native image, vision, and external-tool capabilities without sacrificing the Professional Quality Floor.

Use with:

- `references/execution-priority.md`
- `references/host-action-policy.md`
- `references/professional-quality-floor.md`

## Core Separation

Always separate:

```text
WHAT THE IMAGE SHOULD BE
```

from:

```text
HOW THE CURRENT HOST CAN EXECUTE IT
```

The Cinematic Realism Director owns the first. Host capability owns the second.

Execution limitations must never lower the cinematography/photography reasoning quality.

## Universal Execution Priority

Unless the user explicitly locks a provider:

```text
native/local image capability
> permitted external MCP/plugin/connector only when native/local lacks a material requirement
> prompt/spec fallback
```

Magnific Cinematic and Higgsfield Soul Cinema are not default backends. They are explicit-request/benchmark targets only.

## Capability Classes

### H1 - Native generation + native editing

Host can generate and edit images directly.

Behavior:

- apply the Professional Quality Floor;
- use native generation for new-image requests;
- use native editing for supplied-target edits;
- do not route externally merely because another provider appears more cinematic;
- if the first result fails visual inspection, repair through native tools where practical;
- use an external provider only for a missing material capability or explicit provider lock.

Expected output priority:

1. generated/edited image;
2. concise material limitation only when needed;
3. shot recipe only if requested/useful.

### H2 - Native generation, no native editing

Behavior:

- new images: use native generation;
- supplied-image repair: analyze if vision exists;
- if a preservation-sensitive external editor is permitted and materially required, it may be used under `execution-priority.md`;
- otherwise return the strongest repair/regeneration handoff;
- never call external generation merely because it has more cinematic controls.

### H3 - Native editing, no native text-to-image generation

Behavior:

- edit supplied targets natively;
- new-image requests may use a permitted external generator only when native generation truly does not exist and execution is appropriate;
- otherwise return a production-ready shot/prompt;
- never misuse a placeholder image to force edit execution.

### H4 - Vision + external image tools, no native image execution

Behavior:

1. analyze the request/reference;
2. resolve the provider-neutral shot and Professional Quality Floor;
3. identify a genuinely granted external provider;
4. use a generic/non-competitor route by default when several are available;
5. use Magnific/Higgsfield only if explicitly requested or benchmarking;
6. adapt after the execution path is selected;
7. execute and inspect where possible.

### H5 - Vision only

Behavior:

- analyze references/targets fully;
- build the same professional shot/repair specification a generation-capable host would use;
- return prompt/spec without pretending execution occurred.

### H6 - Text only

Behavior:

- one-line request: run AUTO DIRECT with the Professional Quality Floor;
- expert request: preserve locks and complete missing decisions;
- prompt enhancement: produce a professionalized shot/prompt;
- if an unseen image is essential, say so rather than pretending to inspect it.

## Operation Matrix

| User request | H1 | H2 | H3 | H4 | H5 | H6 |
| --- | --- | --- | --- | --- | --- | --- |
| New image | native generate | native generate | external if appropriate, else prompt | external generate | prompt/spec | prompt/spec |
| Repair supplied image | native edit | analyze + external edit if materially needed, else handoff | native edit | external edit | diagnose + edit prompt | requires description / prompt-only |
| Match reference | native analyze + generate/edit | analyze + native generate | analyze + native edit if target exists | analyze + external execution | analyze + recipe | textual reference description |
| Expert locks | preserve + native execute | preserve + native execute | preserve + native edit/prompt | preserve + external execute | preserve + prompt | preserve + prompt |
| Prompt only | prompt only | prompt only | prompt only | prompt only | prompt only | prompt only |
| Explain | explain | explain | explain | explain | explain | explain |

## Professional Quality Is Host-Independent

Every host class should retain the same core direction quality:

- best-professional interpretation of the requested medium;
- composition and camera relationship;
- optics/focus logic;
- motivated lighting;
- exposure and premium tonal response;
- color separation and finishing;
- subtle organic texture where appropriate;
- physical material/skin/contact realism;
- Reality Gate verification at the strongest level available.

A text-only host should not receive lower-quality cinematography reasoning than an image-capable host.

## Prompt-Only Override

If the user explicitly asks for prompt/JSON/settings/shot recipe/no generation, execute no image provider—native or external.

## Target Availability

Preservation-sensitive edit claims require the actual target image in the active context.

If unavailable:

- do not invent it;
- do not claim inspection/edit;
- return a repair/edit handoff when possible;
- request the image only when essential.

## Verification

```text
V0 reasoning/spec verified
V1 execution confirmed
V2 actual image inspected
V3 inspected + corrected/accepted
```

API/tool success is not V2.

## Failure Conditions

Incorrect behavior includes:

- external/MCP execution taking precedence over an adequate native/local model without justification;
- ordinary requests automatically sent to Magnific/Higgsfield;
- a one-line request receiving merely ordinary/under-directed photography because the user did not specify cinema terminology;
- generation claims without generation;
- edit claims without target image;
- prompt-only being ignored;
- provider adapters treated as access or routing authority;
- execution limitations degrading the Professional Quality Floor.
