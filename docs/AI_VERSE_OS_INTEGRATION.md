# AI-Verse OS Capability Provider Integration

Status: Skills provider v1, OS scoped discovery, supported OS host-adapter composition, and Brain receipt integration are implemented.

## Canonical contract

AI-Verse OS owns the shared [Capability Provider Contract v1](https://github.com/aiverse-filmmakers/AI-Verse-OS/blob/1d2280a031a60b5dd5cee23eabd19677debf1352/system/contracts/capability-provider-v1/README.md), including its [index schema](https://github.com/aiverse-filmmakers/AI-Verse-OS/blob/1d2280a031a60b5dd5cee23eabd19677debf1352/system/contracts/capability-provider-v1/capability-index.schema.json). These links pin the agreed revision. This producer implementation does not redefine that contract. Contract changes require an explicit pin update and compatibility review.

## Current implementation

The standalone checkout commands remain:

```bash
./aiverse-skills install
./aiverse-skills doctor
./aiverse-skills readiness
./aiverse-skills list
./aiverse-skills update
./aiverse-skills rollback
./aiverse-skills uninstall
```

New immutable generations publish manifest schema 3 with `provider_contract: aiverse-capability-provider-v1`, `provider_id: aiverse-skills`, and the immutable generation identity. Each generation also contains `.aiverse/capability-index.json`, derived from the verified installation manifest and bound to the exact `installed.json` bytes by SHA-256. Existing schema-2 immutable generations remain valid legacy generations and are not silently reinterpreted as provider v1.

The index publishes only selectable foundation/employee capabilities. Support-only packages remain installation members but are excluded from discovery. Each indexed capability carries a qualified `aiverse-skills:<id>` identity, static description/version/path, `aiverse-package-sha256-v1` digest, operators, and dependencies. The producer does not publish global runtime readiness, permission, or approval.

The readiness command reports live-verified operator readiness where a supported probe exists, but readiness still does not grant workspace access, action permission, or approval. Those remain host/runtime policy decisions.

AI-Verse OS now consumes this provider through its scoped capability resolver, combining OS, distributed Skills, local personal, and active-workspace providers without moving Skills packages into the OS repository. The supported OS host adapter exposes those resolved capabilities to Brain and demonstrates a generation-pinned, read-only local capability invocation with a validated Skills v2 receipt. Skills still does not own the OS resolver or write provider state into the OS repository.

## Separation and ownership

Skills owns distribution packages, profiles, source pins, provenance, installation integrity, generation publication, and its own lifecycle. OS owns scope, provider resolution, connections, operational permissions, and execution routing. Brain may consume OS-resolved capabilities; Memory supplies scoped history. Neither receives authority from this producer metadata.

Default distribution root remains `~/.aiverse/skills/`. Installation/update/rollback/uninstall must not write, copy, symlink, or vendor packages into the OS repository, and OS installation must not implicitly install Skills. Explicit generic runtime adapters remain a separate action against runtime-owned surfaces.

Personal reusable packages use a separate user-owned provider, default `~/.aiverse/local-skills/`. Workspace skills remain workspace-owned. Neither belongs to the installer-managed distribution. Promotion into the public library is separate from saving a private reusable method.

Foundation and `skills/imported/ai-verse/` packages can both be first-party. Keep provenance/ownership explicit and preserve original upstream packages. Roles compose methods; Operator Packs describe software competence and requirements, not credentials or actual access.

## Producer implementation mapping

| Installation field | Provider v1 implementation |
|---|---|
| Legacy `schema_version: 2` | Preserved as legacy; not treated as v1 |
| New `schema_version: 3` | Explicit provider-aware generation manifest |
| Distribution name | `provider_id: aiverse-skills` and `provider_contract: aiverse-capability-provider-v1` |
| Generation | Existing immutable `generation_id` retained as the provider generation identity |
| Package `id` | Selectable records publish normalized `aiverse-skills:<id>` and preserve the legacy package ID in the manifest |
| Package `path` | POSIX relative path from the pinned generation with resolved containment validation |
| Package digest | Portable `aiverse-package-sha256-v1` digest recomputed from package bytes |
| Source revision/version | SKILL frontmatter version when present; otherwise pinned immutable source revision/distribution version |
| Operators/dependencies | Static requirements only; never global `READY` or permission grants |
| Discovery index | `.aiverse/capability-index.json` generated inside the same immutable generation |

Support-only packages stay in the installation manifest and do not become independently selectable capabilities. Expected profile counts come from pinned release metadata, not a permanent fixed count.

The installer writes the final manifest first, hashes its exact UTF-8 bytes, and publishes that digest in the index. The index repeats the same generation and each indexed record must exactly match a selectable manifest package. The generation verifier checks schema semantics, membership, uniqueness, paths, manifest hash, generation identity, and portable package digests before a provider-v1 generation can activate or be pinned.

`installed.json` and `capability-index.json` are self-describing metadata and are excluded from the older generation-content digest. This preserves the digest of pre-index immutable generations and avoids a circular manifest/index binding. Package integrity remains independently bound by each package's portable digest.

## Lifecycle and runtime requirements

Install, update, rollback, and uninstall are serialized by the immutable generation lifecycle. Activation uses one atomic active-generation pointer; executions pin a generation before loading instructions/resources. Provider metadata lives with those immutable generation bytes, so rollback restores the exact previous manifest/index/package set and uninstall does not delete a generation already available to in-flight work.

OS remains responsible for contextual execution permission and scope. Skills readiness v2 supplies runtime/operator evidence separately from the static provider index; the static index does not claim `READY` globally, and readiness never substitutes for OS permission or Brain approval.

The implemented OS resolver applies relevance before limiting candidates, protects qualified identities and system aliases, and loads only selected package bodies/resources at execution time. An absent optional library is quiet and requires no network activity. Broken or unsupported libraries are excluded and diagnosed without breaking OS; an explicitly requested unavailable capability is reported.

## Existing extension compatibility

OS provider discovery must preserve the existing local extension registry and Memory integration. Skills lifecycle operations remain external and do not modify tracked OS files or claim ownership of Memory adapters.

Brain integration now consumes OS-resolved capabilities through the supported OS host adapter. The adapter pins the Skills generation before loading a capability and validates the resulting v2 receipt with Skills' semantic validator; Brain independently verifies the exact capability/generation/digest binding and translates receipt outcomes conservatively. `trace_id` remains correlation only, and Skills evidence does not itself close Brain objectives.

## Integration status

1. **Implemented:** immutable provider-v1 generation metadata and capability index from the standalone Skills installer.
2. **Implemented:** scoped OS provider discovery and selection across OS, distributed Skills, local personal, and active-workspace providers.
3. **Implemented:** supported OS host-adapter composition with generation-pinned read-only capability invocation and Skills v2 receipt validation.
4. **Implemented:** acceptance coverage for absent/degraded providers, scope isolation, protected aliases, stale indexes, and generation changes during execution.
5. **Implemented:** Brain receipt verification plus the maintained four-component OS host acceptance path.

This does not mean every capability can execute every external operator automatically. Operator-specific execution still depends on its runtime support, live readiness, OS permission, Brain policy/approval, and receipt/effect verification.
