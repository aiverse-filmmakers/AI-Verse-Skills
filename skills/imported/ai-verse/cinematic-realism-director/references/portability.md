# Cinematic Realism Director - Standalone Portability Contract

Status: FROZEN FOR V1

This contract defines what must remain true when `cinematic-realism-director/` is copied, downloaded, zipped, vendored, or installed without the rest of the AI-Verse-Skills repository.

The package must provide its core cinematic intelligence from files contained inside its own directory. AI-Verse infrastructure may improve discovery, packaging, validation, lifecycle management, or runtime integration, but it must never be required for the skill to understand or perform its core job.

## Standalone Invariant

A capable Agent Skills host that receives only this directory must be able to:

- discover the skill from `SKILL.md`;
- understand when to activate it;
- apply beginner AUTO cinematic direction;
- preserve explicit expert camera/capture locks;
- produce a cinematic still-image prompt when no image-generation tool exists;
- diagnose and specify still-image realism repair when image understanding is available;
- adapt output using any provider reference that exists locally in the package;
- use the Reality Gate and other local quality rules;
- explain its shot recipe when requested;
- do all of the above without reading any file outside the package directory.

## Required Package Root

The standalone package root is:

```text
cinematic-realism-director/
```

All internal links and file references required for core operation must resolve from that root using package-local relative paths.

Allowed examples:

```text
references/routing.md
references/reality-gate.md
workflows/auto-direct.md
adapters/generic.md
schemas/cinematic-shot-spec.schema.json
```

Forbidden required references:

```text
../../../docs/SKILL_SPEC.md
../../video-editor/SKILL.md
/Users/<name>/...
/home/<name>/...
C:\Users\<name>\...
https://private-host/required-file
```

External URLs may appear as provenance or optional research links, but the live availability of an external webpage must not be required for normal V1 execution.

## Core Required Files

By V1 release, the standalone package must contain at minimum:

```text
SKILL.md
README.md
aiverse.skill.yaml
references/
workflows/
adapters/
schemas/
examples/
evals/
```

`aiverse.skill.yaml` is an AI-Verse sidecar. Non-AI-Verse hosts may ignore it. The portable behavior contract remains in `SKILL.md` plus package-local references.

`IMPLEMENTATION_PLAN.md`, `STATUS.md`, and `ROADMAP.md` are development/release documentation. They are not runtime dependencies.

## No Parent-Directory Dependency

No core instruction may require:

- repository-root documentation;
- repository-root schemas;
- repository-root scripts;
- repository-root registries;
- repository-root configuration;
- CI files;
- release manifests;
- git metadata;
- a particular repository checkout layout.

The full AI-Verse-Skills repository may validate or register the package, but those systems must wrap the package rather than supply missing cinematic knowledge.

## No Sibling-Skill Dependency

The skill must not require another skill directory to function.

In particular, it must not depend on:

- `video-editor`;
- `interface-designer`;
- foundation skills;
- imported third-party skills;
- future AI-Verse cinematic/video packages.

It may hand work off to another capability when the user's request crosses a scope boundary, but handoff availability is optional runtime behavior, not a prerequisite for the current still-image task.

Example:

- acceptable: "This request is now primarily video editing; use an available video-editing capability if the host has one."
- unacceptable: "Load `../video-editor/references/...` before designing this still."

## No AI-Verse OS Requirement

Prompt-only and reasoning-only operation must not require AI-Verse OS.

The standalone folder must remain useful in a compatible host even when the user has none of the following:

- AI-Verse OS;
- AI-Verse Gateway;
- AI-Verse Memory;
- AI-Verse Automations;
- AI-Verse registry tooling;
- AI-Verse installer;
- AI-Verse runtime adapters.

When installed inside AI-Verse, those systems may provide discovery, lifecycle, permission, generation, verification, or distribution benefits. They must not alter the meaning of the core cinematic rules.

## No MCP Requirement

V1 core behavior must not require MCP.

MCP may later provide optional tools such as:

- external model generation;
- image analysis services;
- provider routing;
- remote evaluation;
- asset storage;
- plugin/backend integration.

If no MCP server is available, the skill must still perform all reasoning and prompt/specification tasks that can be completed with the host's native capabilities.

No instruction in the core skill may say or imply that MCP access is mandatory for cinematic quality.

## No API-Key Requirement for Prompt-Only Operation

A user must be able to use the skill in prompt-only mode without supplying an API key.

The skill must never request a raw API key merely to perform its reasoning.

If the host exposes an authenticated image-generation tool, provider, plugin, or connector, the host owns that authentication flow.

If an optional external provider requires credentials and none are available:

1. do not fabricate access;
2. do not request plaintext credentials as ordinary chat content;
3. degrade to a provider-appropriate prompt or generic cinematic specification;
4. state the limitation only when it materially affects the requested output.

## Host Independence

The package must not assume one vendor or one model.

Core cinematography and realism logic must remain provider-neutral. Provider-specific behavior belongs in package-local adapters.

The standalone package should remain useful in hosts such as:

- ChatGPT or another OpenAI host with suitable skill/file support;
- Gemini environments that can consume skill instructions/files;
- Claude or other Agent Skills-compatible hosts;
- Hermes or similar agents;
- coding agents capable of loading Agent Skills;
- text-only LLM environments where the folder contents are supplied as context.

Exact installation mechanics differ by host and are not part of the core intelligence contract.

## Tool Independence and Graceful Degradation

The package may take advantage of tools granted by the host, but it must not assume they exist.

Core reasoning must separate:

```text
WHAT THE SHOT SHOULD BE
```

from:

```text
WHAT THE CURRENT HOST CAN EXECUTE
```

Therefore:

- image generation availability changes whether the host can render directly;
- image editing availability changes whether Reality Repair can be executed directly;
- vision availability changes whether an uploaded image can be independently diagnosed;
- none of those change the underlying cinematic knowledge or shot specification.

Detailed degradation behavior is defined separately in Task 0.3.

## Local-Reference Rule

All knowledge required for V1 repeatable behavior must be either:

1. in `SKILL.md`; or
2. in a package-local file referenced by `SKILL.md` or a package-local index.

Progressive disclosure is required. Large knowledge files should be loaded only when relevant, but they must remain discoverable from inside the package.

Do not create orphan references that materially change behavior but are never linked from the portable skill/index.

## Local Adapter Rule

Provider adapters must live inside:

```text
adapters/
```

Adapters may describe public provider behavior and prompt translation, but they must not become mandatory dependencies for the universal brain.

`adapters/generic.md` must remain a viable fallback if:

- the user's provider is unknown;
- a provider changes;
- a named adapter is unavailable;
- a host exposes generation without revealing the exact underlying image model.

## Local Schema Rule

Structured contracts required for the skill's own outputs must live inside:

```text
schemas/
```

A standalone host should not need the repository-root `schemas/` directory to interpret the Cinematic Shot Spec, realism diagnosis, or reference-DNA structures.

AI-Verse's root schemas may validate AI-Verse packaging/runtime metadata separately.

## Optional External Research

The package may contain a source ledger with public links to Magnific, Higgsfield, ARRI, Cooke, Kodak, OpenAI, Google, or other authoritative sources.

Those links are evidence/provenance, not live runtime dependencies.

The skill must not need to browse the web on every image request merely to remember basic lens, lighting, film, or realism principles already captured in its local knowledge base.

Fresh web research is appropriate when the user explicitly asks about a current provider feature, a newly released model, changed API behavior, or another genuinely time-sensitive fact.

## Data and Privacy Boundary

The standalone package itself contains no requirement to upload user images, prompts, or references to a particular third-party service.

If the host chooses a generation/editing provider, that host/provider's own data handling applies.

The skill must not silently route user content to an external service merely because an adapter exists.

## Filesystem Boundary

The skill must not require arbitrary host filesystem access to perform its core reasoning.

When a host installs the folder as an Agent Skill, package-local reads are sufficient for normal operation.

If a workflow later writes artifacts, outputs, or eval results, those writes must respect the host-granted workspace and must not be a prerequisite for basic use.

## Standalone Distribution Forms

The following forms should preserve equivalent core behavior:

```text
1. Full AI-Verse-Skills repository install
2. Copy of cinematic-realism-director/ only
3. ZIP containing cinematic-realism-director/
4. Git vendor/subtree of this directory
5. Agent Skills installation that materializes only this package
6. Manual upload of the package files to a capable host
```

A single flattened `.md` edition may be generated later for beginner convenience, but it is a distribution derivative, not the canonical V1 source. The canonical source is the self-contained package folder.

## AI-Verse Integration Boundary

When used inside AI-Verse-Skills, the surrounding repository may provide:

- canonical registry identity;
- package discovery;
- version/lifecycle management;
- manifest/schema validation;
- runtime adapters;
- immutable generation tracking;
- installation verification;
- CI/readiness gates.

These are integration benefits, not cinematic-brain dependencies.

The same package-local `SKILL.md`, references, workflows, adapters, and schemas must remain authoritative in standalone use.

## Dependency Policy

### Required runtime dependencies for core V1 reasoning

```text
None outside the package folder and the host LLM/agent itself.
```

### Optional runtime capabilities

Depending on the requested result:

- vision/image understanding;
- native image generation;
- native image editing;
- external generation/editing tools;
- web access for current provider research;
- filesystem access for packaging/evals;
- MCP or plugin integrations.

Optional capabilities must enhance execution, not determine whether the skill can think cinematically.

## Portability Failure Conditions

V1 portability is considered broken if any required workflow:

- imports a sibling skill;
- requires a repository-root file;
- requires AI-Verse OS for prompt-only use;
- requires MCP for prompt-only use;
- requires an API key for prompt-only use;
- relies on a developer-specific absolute path;
- depends on an unbundled private document;
- cannot discover a required local reference from the package itself;
- claims direct image generation in a host that has no image tool instead of degrading appropriately.

The last item is further specified by Task 0.3 but is included here because false execution assumptions undermine portability.

## V1 Standalone Acceptance Checklist

Before release, test the package in an isolated temporary directory containing only `cinematic-realism-director/` and verify:

- [ ] `SKILL.md` is present at package root;
- [ ] all required links from `SKILL.md` resolve inside the package;
- [ ] all required links from local indexes/references resolve inside the package;
- [ ] no required `../` or repository-root path escapes exist;
- [ ] no sibling skill is required;
- [ ] no AI-Verse OS service is required for prompt-only execution;
- [ ] no MCP server is required for prompt-only execution;
- [ ] no API credential is required for prompt-only execution;
- [ ] generic provider fallback remains usable;
- [ ] beginner AUTO workflow can be understood from package-local material;
- [ ] expert lock behavior can be understood from package-local material;
- [ ] Reality Repair can produce a useful repair specification without external package knowledge;
- [ ] source/provenance links are optional evidence rather than mandatory runtime fetches;
- [ ] core results are semantically equivalent when run from full-repo and standalone-package contexts, given equivalent host capabilities.

Task 10.4 will perform the final isolated-folder acceptance test after the complete package exists.

## Change Control

Any future feature that makes core cinematic reasoning depend on an external server, AI-Verse OS component, sibling skill, proprietary local installation, MCP server, or mandatory API credential is a portability-breaking architectural change and must be explicitly approved rather than introduced as an implementation convenience.
