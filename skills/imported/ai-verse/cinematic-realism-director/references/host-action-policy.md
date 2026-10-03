# Host Action Policy

Status: RUNTIME POLICY
Task: 7.9

Purpose: decide whether the skill should execute image generation/editing or return a prompt/specification, based on the user's requested output and the capabilities actually available in the current host.

## Core Decision Rule

```text
image tool available + user asked for image -> generate/edit
no image tool + user asked for image -> return adapted prompt/spec
user explicitly requests prompt only -> never auto-generate
```

This policy refines, but does not replace, `references/host-capabilities.md`.

## Decision Order

1. Determine the user's requested outcome.
2. Determine whether a real target image is available when editing is requested.
3. Determine the host capability class.
4. Identify an actually available, permitted image tool/provider.
5. Select the exact adapter or fallback hierarchy.
6. Execute only if the requested outcome and capability surface justify it.
7. Verify the returned image visually when the host can inspect it.
8. Otherwise return the strongest prompt/specification with truthful status.

## Output Intent Has Priority

### User asks for an image
If a suitable image tool is genuinely available and permitted, execute generation/editing.

Do not stop at prompt-writing merely because prompt output is easier.

### User asks for prompt/spec/JSON/settings only
Never generate automatically, even if an image tool is available.

### User asks to explain
Return the shot recipe/explanation. Generate only if image creation is also explicitly requested.

## Edit Target Requirement

For:

- Reality Repair;
- retouching;
- relighting;
- restoration;
- preservation-sensitive edits;
- reference-preserving transformations;

an actual target image must be present in the current host/tool environment.

If it is missing:

- do not invent or reconstruct it from memory;
- do not claim an edit was performed;
- return a repair/edit specification when enough information exists;
- request the target image only when it is essential and unavailable.

## Tool Selection

Choose tools by task fit, not brand prestige.

Prefer the smallest operation that can satisfy the request:

```text
local/region edit before whole-frame regeneration
relight before redesign when only lighting changes
upscale before reimagine when only quality changes
provider-native reference conditioning when preservation requires it
```

If a provider is requested explicitly, use it when actually connected and capable. Otherwise explain the limitation through the result status and use fallback only when the user's intent permits.

## External Provider Boundary

An adapter file does not mean the provider is connected.

Do not:

- send user images to an external provider merely because an adapter exists;
- request raw credentials inside the skill;
- claim provider execution without a real tool call;
- silently switch providers when provider identity is a locked user requirement.

## Host Capability Outcomes

### H1 - generate + edit
Execute generation or edit unless PROMPT ONLY or another explicit output constraint applies.

### H2 - generate only
Generate new images. For edits, analyze if possible and produce preservation-aware regeneration/handoff; disclose that exact editing is unavailable.

### H3 - edit only
Edit supplied targets. New-image requests return prompt/spec.

### H4 - vision + external image tools
Resolve shot first, choose granted provider/tool, adapt, execute, verify where possible.

### H5 - vision only
Analyze references/targets and return shot/edit spec. No false execution claim.

### H6 - text only
Return complete provider-neutral or adapted prompt/spec. Never pretend to inspect images.

## Verification Status

Distinguish:

```text
V0 reasoning complete
V1 execution confirmed
V2 visual inspection complete
V3 comparative / iterative acceptance
```

A successful generation API/tool call is only V1 unless the host actually inspects the result.

Do not claim visual success from tool execution alone.

## Retry / Repair Behavior

If generation succeeds but V2 Reality Gate fails:

- repair only the failed domains where practical;
- preserve successful areas and locks;
- do not restart the entire visual concept by default.

If the provider cannot perform the needed repair, fall back according to `adapter-fallback-hierarchy.md`.

## Failure Conditions

The policy fails if the skill:

- returns only a prompt when a suitable tool is available and an image was requested;
- generates despite PROMPT ONLY;
- edits without the real target image;
- claims inspection of an unavailable image;
- claims V2 quality verification after only a successful tool call;
- treats an adapter as authorization/access;
- silently switches a provider locked by the user;
- performs broad regeneration when a narrow preservation-safe edit is available.

## Acceptance

The skill always chooses a truthful action path: create/edit when permitted and requested, otherwise return a production-ready prompt/specification without fabricating capabilities or results.