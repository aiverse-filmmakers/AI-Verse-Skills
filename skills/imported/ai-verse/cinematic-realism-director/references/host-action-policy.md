# Host Action Policy

Status: RUNTIME POLICY

Purpose: decide whether the skill should execute image generation/editing or return a prompt/specification while preserving native-first execution and user intent.

Use together with:

- `references/execution-priority.md`
- `references/host-capabilities.md`
- `references/professional-quality-floor.md`

## Core Decision Rule

```text
explicit provider lock -> use that provider if genuinely available/permitted
otherwise native/local suitable image tool -> use it first
otherwise permitted external tool -> use only when native/local cannot satisfy a material requirement
otherwise -> return the strongest adapted prompt/spec
prompt-only -> never execute any image tool
```

A specialized external tool is not automatically preferable to a native/local tool.

## Decision Order

1. Determine the requested outcome.
2. Determine explicit user locks, including any named provider.
3. Build the provider-neutral shot and apply the Professional Quality Floor.
4. Determine whether a real target image is available when editing is requested.
5. Identify the host-native/local image capability.
6. Use native/local execution when it can materially satisfy the operation.
7. Consider an external MCP/plugin/connector only when a required capability is unavailable natively or the user explicitly locked that provider.
8. Select the adapter for the execution path already chosen.
9. Execute.
10. Inspect/repair the output when possible.
11. Otherwise return the strongest prompt/specification with truthful status.

## Output Intent Has Priority

### User asks for an image

If a suitable native/local image tool is available, execute there first.

Do not stop at prompt-writing merely because prompt output is easier.

Do not bypass native/local generation because an external provider advertises more cinematic controls.

### User explicitly names a provider

Treat the provider as a lock.

Use it only when actually connected/permitted. If unavailable, disclose the limitation and fall back only when the user permits fallback.

### User asks for prompt/spec/JSON/settings only

Never generate automatically, even if image tools are available.

### User asks to explain

Return the shot recipe/explanation. Generate only if image creation is also requested.

## Native vs External

Native/local means the current host's normal built-in/default image generation/editing path.

External means an optional MCP, plugin, connector, third-party API wrapper, or dedicated provider service.

MCP is transport, not quality authority.

Never choose an external provider merely because:

- it has `cinematic` in its name;
- it exposes more controls;
- it is Magnific or Higgsfield;
- the package contains a detailed adapter for it;
- it appears more premium or specialized.

## Competitor Provider Boundary

Magnific Cinematic and Higgsfield Soul Cinema are not default generation backends for this skill.

Use them only when:

- the user explicitly requests that provider/export; or
- a controlled benchmark/evaluation explicitly requires it.

Ordinary image requests must not be routed to them automatically.

## Edit Target Requirement

For Reality Repair, retouching, relighting, restoration, preservation-sensitive edits, and reference-preserving transformations, an actual target image must be present in the active host/tool environment.

If it is missing:

- do not invent or reconstruct it from memory;
- do not claim an edit was performed;
- return a repair/edit specification when enough information exists;
- request the target image only when essential.

## Editing Priority

Prefer the smallest suitable operation:

```text
native/local region edit
> native/local whole-image edit/regeneration when preservation allows
> permitted external targeted edit when native/local lacks the required capability
> external reference-conditioned regeneration with disclosed preservation risk
> prompt/spec handoff
```

Relight before redesign when only lighting changes. Upscale before reimagine when only quality changes. Do not use broad external regeneration when a narrow native operation can satisfy the request.

## External Provider Boundary

An adapter file does not mean the provider is connected.

Do not:

- send user images externally merely because an adapter exists;
- request raw credentials inside the skill;
- claim provider execution without a real tool call;
- silently switch providers when provider identity is a locked user requirement.

## Host Capability Outcomes

### H1 - native generate + edit
Use native generation/editing by default unless PROMPT ONLY or an explicit provider lock applies.

### H2 - native generate only
Use native generation for new images. For edits, analyze if possible and use a permitted external edit only when the requested preservation cannot be achieved natively; otherwise return a preservation-aware handoff.

### H3 - native edit only
Edit supplied targets natively. New-image requests may use a permitted external generator only when appropriate under the execution-priority policy; otherwise return prompt/spec.

### H4 - vision + external tools, no native image execution
Resolve the shot first, then choose a granted external provider/tool. This class does not create permission to use Magnific/Higgsfield automatically; competitor-provider rules still apply.

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

A successful generation call is only V1 unless the host actually inspects the result.

If a native/local first result fails V2, attempt focused correction through the native/local path where practical. Do not immediately escape to an external competitor because the first result was imperfect.

## Failure Conditions

The policy fails if the skill:

- uses an external MCP/provider before an adequate native/local image path without an explicit provider lock or missing material capability;
- automatically routes an ordinary request to Magnific or Higgsfield;
- returns only a prompt when a suitable tool is available and an image was requested;
- generates despite PROMPT ONLY;
- edits without the real target image;
- claims visual inspection after tool success alone;
- treats adapter presence as provider authorization;
- performs broad regeneration when a narrow preservation-safe edit is available.
