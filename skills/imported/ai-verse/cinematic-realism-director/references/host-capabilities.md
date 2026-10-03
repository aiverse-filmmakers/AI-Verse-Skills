# Cinematic Realism Director - Host Capability Degradation Contract

Status: FROZEN FOR V1

This contract defines how the skill behaves across hosts with different image, vision, tool, and execution capabilities.

The cinematic reasoning layer must remain useful even when the host cannot generate or edit images directly.

## Core Rule

Always separate:

```text
WHAT THE SHOT SHOULD BE
```

from:

```text
WHAT THE CURRENT HOST CAN EXECUTE
```

The first is owned by the Cinematic Realism Director. The second depends on the host.

The skill must never pretend that a tool exists, fabricate generation, or claim an edit was performed when the host only produced instructions.

## Capability Classes

### H1 - Native image generation and image editing

Host capabilities:

- understands text instructions;
- can inspect supplied images;
- can generate new images;
- can edit supplied images.

Behavior:

- if the user asks for a new image, design the shot and execute generation;
- if the user asks to repair/edit an image, preserve the supplied image as the edit target and execute an edit;
- do not return a prompt instead of executing unless the user explicitly asks for prompt-only output or host/tool policy blocks execution;
- keep detailed internal shot reasoning concise unless the user asks to see it;
- if generation/editing fails, return the best available prompt/specification plus a clear partial/blocked status rather than pretending success.

Expected output priority:

1. generated or edited image;
2. concise result status;
3. optional shot recipe only when useful/requested.

### H2 - Native image generation, no image editing

Host capabilities:

- can generate images from text;
- may understand uploaded images;
- cannot perform a true edit against an existing target.

Behavior:

- new-image requests: execute generation normally;
- Reality Repair/reference-preservation requests: analyze the source if vision is available, then construct a preservation-aware regeneration prompt/specification;
- never claim that identity, composition, geometry, product design, or pose will be perfectly preserved when the host cannot perform source-conditioned editing;
- if preservation is critical, report the limitation and return the strongest edit/regeneration handoff specification.

### H3 - Image editing, no general text-to-image generation

Host capabilities:

- can edit a supplied image;
- cannot create a new image from scratch.

Behavior:

- edit/repair requests: execute the edit;
- new-image requests without a source image: produce a cinematic shot specification and final generation prompt;
- do not attempt to misuse an unrelated placeholder image merely to force execution.

### H4 - Vision + external image tool(s)

Host capabilities:

- can inspect images;
- has one or more external generation/editing providers through tools/plugins/connectors/MCP/API wrappers.

Behavior:

1. determine the requested operation first;
2. construct the provider-neutral Cinematic Shot Spec;
3. identify an actually available image tool/provider;
4. load the matching local adapter when known;
5. preserve user locks;
6. execute only within granted tool permissions;
7. verify returned output where the host can inspect it;
8. if the preferred provider is unavailable, fall back to another suitable granted image tool or return a prompt/specification.

Do not silently send images to an external service merely because an adapter exists. Tool availability and authorization belong to the host/user.

### H5 - Vision, no image generation/editing

Host capabilities:

- can inspect user-supplied images;
- cannot create or modify images.

Behavior:

- reference analysis: perform full observable visual analysis;
- Reality Repair: diagnose artificiality, create preserve/repair/allow-change sets, then produce an edit specification/prompt;
- new-image request: produce a complete Cinematic Shot Spec plus an adapted or generic prompt;
- explicitly distinguish analysis from execution.

This class must remain highly useful for users who intend to paste the resulting prompt into another generator.

### H6 - Text only

Host capabilities:

- no image understanding;
- no image generation;
- no image editing.

Behavior:

- simple text idea: perform AUTO DIRECT reasoning and return the final cinematic prompt/specification;
- manual-camera request: preserve locks and complete unspecified values;
- prompt enhancement: cinematize the user's text;
- if the user references an unseen image, do not pretend to inspect it;
- ask for a textual description only when the missing visual information is essential to the requested result;
- if enough user description exists, continue without unnecessary questions.

## Operation Matrix

| User request | H1 | H2 | H3 | H4 | H5 | H6 |
| --- | --- | --- | --- | --- | --- | --- |
| New cinematic image | generate | generate | prompt/spec | tool-generate | prompt/spec | prompt/spec |
| Repair supplied AI image | edit | analyze + regeneration handoff | edit | tool-edit | diagnose + edit prompt | requires description / prompt-only |
| Match supplied reference | analyze + generate/edit | analyze + generate | analyze + edit if target exists | analyze + tool execution | analyze + recipe | requires textual reference description |
| Expert camera locks | preserve + execute | preserve + execute | preserve + prompt/edit | preserve + execute | preserve + prompt | preserve + prompt |
| Prompt only | prompt only | prompt only | prompt only | prompt only | prompt only | prompt only |
| Explain shot recipe | explain | explain | explain | explain | explain | explain |

## Action Priority

When the user asks for an image rather than a prompt:

```text
1. USE SUITABLE NATIVE/GRANTED IMAGE TOOL IF AVAILABLE
2. OTHERWISE USE A SUITABLE GRANTED EXTERNAL IMAGE TOOL
3. OTHERWISE RETURN THE BEST EXECUTABLE PROMPT + SHOT SPEC
```

Do not stop at step 3 when step 1 or 2 is available and the user's request clearly asks for image creation/editing.

## Prompt-Only Override

If the user explicitly asks for:

- prompt only;
- JSON only;
- shot recipe only;
- settings only;
- no generation;

then do not generate an image even if the host can.

Explicit output intent overrides automatic execution.

## Image Target Rule

For edits, restoration, realism repair, relighting, lens-look changes, or preservation-sensitive operations, the host must have access to the actual target image.

If the image is not available in the active context/tool environment:

- do not invent it;
- do not claim the edit was performed;
- produce a repair/edit specification if enough description exists;
- otherwise request the missing image only when required to proceed.

## Verification Rule

If the host can inspect generated/edited output, perform a post-generation Reality Gate before claiming the visual target was achieved.

If the host cannot inspect the returned image, distinguish:

```text
EXECUTION CONFIRMED
```

from:

```text
VISUAL QUALITY VERIFIED
```

A successful tool call is not proof that the resulting frame meets realism/cinematic criteria.

## Provider Unknown Rule

If the host exposes an image capability but the exact underlying provider/model is unknown:

- use the universal Cinematic Shot Spec;
- use `adapters/generic.md` when available;
- avoid provider-specific syntax that cannot be verified;
- never fabricate model parameters.

## Degradation Quality Requirement

Degradation means reduced execution capability, not reduced cinematography quality.

A text-only host should still receive the same core decisions about:

- visual intent;
- framing;
- camera position;
- lens/focal behavior;
- focus/depth;
- lighting motivation;
- exposure;
- color;
- texture;
- materials;
- physical realism;
- preservation constraints;
- Reality Gate.

Only the final execution step changes.

## Failure Conditions

Host-capability behavior is incorrect if the skill:

- claims an image was created without an image tool;
- returns only explanation when a suitable image tool is available and the user requested an image;
- silently ignores a user request for prompt-only output;
- claims to have inspected an image unavailable to the host;
- treats a provider adapter as proof that the provider is connected;
- exposes or requests raw credentials unnecessarily;
- sacrifices locked creative intent merely because a particular tool has different defaults;
- treats a successful API/tool call as proof of visual-quality success without inspection when inspection is possible.

## V1 Acceptance

Task 0.3 is satisfied when every capability class above has a useful result path and no class requires the host to pretend it has capabilities it does not possess.
