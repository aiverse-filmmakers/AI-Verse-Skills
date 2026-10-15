# Execution Priority

Status: RUNTIME POLICY

Purpose: make image execution order deterministic and prevent optional external/MCP providers from displacing the host's native/local image capability.

## Core Rule

Unless the user explicitly names a provider, the skill must prefer the host-native/local image model first.

```text
1. explicit user-locked provider, if actually available and permitted
2. native/local host image generation or editing capability
3. external MCP/plugin/connector/API image provider only when native/local cannot satisfy a material requirement
4. provider-neutral or adapted prompt/specification fallback
```

A provider being more specialized, premium, cinematic, expensive, or feature-rich is **not** sufficient reason to skip the native/local model.

## Definitions

### Native / local

The image generation/editing capability that belongs to the current host's normal image workflow and does not require routing the request to an optional third-party MCP/plugin/connector/provider.

Examples conceptually include:

- the host's built-in image generator;
- a locally configured/default image model;
- a first-party native image action surfaced directly by the host.

Do not assume a particular brand or model name when the host does not expose it.

### External

Any optional provider reached through:

- MCP;
- plugin;
- connector;
- external API wrapper;
- third-party image service;
- dedicated provider tool not constituting the host's normal local/native image path.

## Explicit Provider Lock

If the user explicitly says:

- `use Magnific`;
- `make this in Higgsfield`;
- `give me a Seedream prompt`;
- `run this through FLUX`;
- or otherwise names a provider as a required execution target;

then that provider becomes a user lock.

Use it only if it is genuinely connected/permitted. If unavailable, report the limitation rather than silently replacing it unless the user permits fallback.

## Native-First Default

If the user asks simply:

```text
make an image of ...
generate this ...
create a cinematic picture ...
fix this image ...
```

and does not name an external provider, the skill must:

1. build the provider-neutral Cinematic Shot Spec;
2. use the host-native/local image capability if it can perform the requested operation;
3. inspect/repair the result where the host allows;
4. consider an external provider only if a material capability is missing.

Do not browse available providers and choose whichever appears most `cinematic`.

## When External Fallback Is Allowed

External execution may be selected without an explicit provider request only when the native/local path cannot satisfy a material requirement and external execution is permitted by the host/user.

Examples:

- native generator cannot edit an existing image but an external tool can perform preservation-sensitive editing;
- native system cannot accept a required identity/product reference while a granted external provider can;
- native system cannot produce the required output class at all;
- a user-requested operation requires a specialized transformation not available natively.

Even then:

- use the smallest external operation needed;
- preserve all locks and reference roles;
- disclose material provider switching when relevant;
- never send user assets externally merely because an external route exists.

## Competitor Provider Rule

Magnific Cinematic and Higgsfield Soul Cinema are benchmark/reference competitors for this skill.

They are **not automatic execution backends**.

They may be used only when:

1. the user explicitly requests Magnific/Higgsfield execution or prompt export; or
2. a controlled benchmark/evaluation is explicitly being run.

The skill must never route ordinary image generation to Magnific or Higgsfield merely because their adapters exist or because they appear specialized for cinema.

Their local adapter/research files exist to:

- understand public provider behavior;
- support explicit user-requested export/translation;
- support controlled benchmarking;
- maintain comparative research.

Adapter presence does not imply default execution permission.

## Provider Adapter Selection

Provider adaptation happens **after** execution-path selection.

Correct order:

```text
user intent
-> universal shot
-> quality floor
-> Reality Gate
-> choose execution path
-> select adapter for that chosen path
-> execute
```

Incorrect order:

```text
scan adapters
-> choose the most cinematic-looking provider
-> redesign the shot around it
```

## MCP Rule

MCP is a transport/capability surface, not a creative-quality signal.

Never prefer MCP solely because:

- an MCP tool has `cinematic` in its name;
- an MCP tool exposes more controls;
- an MCP tool belongs to Magnific/Higgsfield;
- an MCP provider appears more premium;
- the skill contains a detailed adapter for it.

When native/local can satisfy the image request, use native/local first.

## Editing Priority

For preservation-sensitive edits:

```text
native/local targeted edit
> native/local broader edit/regeneration if preservation is acceptable
> granted external targeted edit when native cannot do it
> external reference-conditioned regeneration with disclosed preservation risk
> prompt/spec handoff
```

Do not use a broad external regeneration when a narrower native/local edit can satisfy the request.

## Prompt-Only Override

If the user requests prompt/spec/JSON/settings only, do not execute any image provider—native or external.

## Verification

Tool success does not change the priority model.

After execution:

- V1 = execution confirmed;
- V2 = visual inspection completed;
- V3 = iterative acceptance.

If the native/local result fails V2, first attempt correction through the native/local path when practical. Do not immediately escape to an external competitor merely because the first generation was imperfect.

## Failure Conditions

This policy fails if the skill:

- uses MCP/external generation before an adequate native/local model without an explicit user provider request;
- automatically chooses Magnific or Higgsfield for an ordinary request;
- treats a provider adapter as a routing recommendation;
- switches to an external service because it appears more cinematic rather than because a material native capability is missing;
- ignores an explicit provider lock;
- sends user images externally merely because an adapter is available;
- executes any provider despite PROMPT ONLY.
