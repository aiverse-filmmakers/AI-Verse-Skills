# AI-Verse OS Capability Provider Integration

Status: provider v1 implementation contract; runtime integration is not shipped by this documentation change.

## Canonical contract

AI-Verse OS owns the shared [Capability Provider Contract v1](https://github.com/aiverse-filmmakers/AI-Verse-OS/blob/1d2280a031a60b5dd5cee23eabd19677debf1352/system/contracts/capability-provider-v1/README.md), including its [index schema](https://github.com/aiverse-filmmakers/AI-Verse-OS/blob/1d2280a031a60b5dd5cee23eabd19677debf1352/system/contracts/capability-provider-v1/capability-index.schema.json). These links pin the agreed revision. This producer mapping must not redefine that contract. Contract changes require an explicit pin update and compatibility review.

## Current implementation versus next stage

Currently the standalone checkout command is:

```bash
./aiverse-skills install
./aiverse-skills doctor
./aiverse-skills readiness
./aiverse-skills list
./aiverse-skills update
./aiverse-skills rollback
./aiverse-skills uninstall
```

The current installer writes `.aiverse/installed.json` using its existing schema 2. It does not yet emit the v1 generation envelope or capability index. Current readiness is a dependency hint, not verified workspace access or action authorization.

The current OS CLI has no `ai-verse-os skills` command and its shipped runtime does not implement this provider resolver. A future `ai-verse-skills` installed command may wrap the standalone implementation; optional OS convenience commands must delegate to it without owning a second lifecycle. Neither command spelling is advertised as shipped until implemented and tested.

## Separation and ownership

Skills owns distribution packages, profiles, source pins, provenance, installation integrity, and its own lifecycle. OS owns scope, provider resolution, connections, operational permissions, and execution routing. Brain may consume OS-resolved capabilities; Memory supplies scoped history. Neither is implemented or modified by this contract step.

Default distribution root remains `~/.aiverse/skills/`. Installation/update/rollback/uninstall must not write, copy, symlink, or vendor packages into the OS repository, and OS installation must not implicitly install Skills. Explicit generic runtime adapters remain a separate action against runtime-owned surfaces.

Personal reusable packages use a separate user-owned provider, default `~/.aiverse/local-skills/`. Workspace skills remain workspace-owned. Neither belongs to the installer-managed distribution. Promotion into the public library is separate from saving a private reusable method.

Foundation and future `skills/imported/ai-verse/` packages can both be first-party. Keep provenance/ownership explicit and preserve original upstream packages. Roles compose methods; Operator Packs describe software competence and requirements, not credentials or actual access.

## Producer implementation mapping

| Current installation field | Required v1 behavior |
|---|---|
| `schema_version: 2` | Preserve legacy interpretation; introduce an explicit versioned migration, not silent reinterpretation |
| Distribution name | Add `provider_id: aiverse-skills` and `provider_contract: aiverse-capability-provider-v1` |
| Installation timestamp | Add a distinct immutable `generation_id`; time alone is not generation identity |
| Package `id` | Publish `aiverse-skills:<id>`; record any legacy alias explicitly |
| Package `path` | POSIX path relative to pinned generation, validate resolved containment |
| Package digest | Recompute and identify the contract's portable versioned digest algorithm during migration |
| Source revision | Preserve provenance; publish a stable package version (upstream version when pinned, otherwise immutable revision/digest identifier) |
| Operators/dependencies | Static requirements only, never global `READY` or permission grants |
| No discovery index | Generate `.aiverse/capability-index.json` from verified installation metadata |

The migrated manifest must expose the qualified ID, version, path, and versioned digest needed to match each index record. Support-only packages stay in the installation manifest and do not become independently selectable capabilities. Expected profile counts come from pinned release metadata, not a permanent fixed count.

Hash the exact manifest bytes after writing the final manifest. The index carries that hash and the same generation. Schema validity, matching manifest membership, paths, and generation must all pass before activation. The index is disposable; a valid index cannot make an invalid package trusted. Do not add an index hash back into the manifest and create a circular binding.

## Lifecycle and runtime requirements

Serialize lifecycle mutations and pin a coherent generation for each invocation. The present two-rename activation is not proof of concurrent-reader or crash safety. Future activation must preserve in-flight instructions/resources, retain referenced generations, handle interrupted activation, and keep copy adapters consistent. Rollback invalidates discovery caches; uninstall blocks new selections while respecting active generation leases and host cancellation policy.

OS computes readiness for the active scope/runtime from package integrity, runtime support, verified connections, permission, and approval. Expired evidence becomes unknown. A binary or environment flag is not a live connection test. The static index must not claim `READY` globally.

OS applies relevance before limiting candidates, protects qualified identities and system aliases, and only loads selected package bodies/resources. An absent optional library is quiet and requires no network activity. Broken/unsupported libraries are excluded and diagnosed without breaking OS; an explicitly requested unavailable capability must be reported.

## Existing extension compatibility

A future OS registry migration and adapter generator must preserve Memory's registry entry, `AGENTS.md` marker, and both adapters in either installation order. Generators only replace owned, unmodified files. This step leaves the existing registry, OS schema, and adapter source paths intact.

Brain integration must consume the OS resolver and normalize Skills receipts into verified host outcomes. `trace_id` is not an external-effect receipt. Skills evidence does not itself close Brain objectives. Full requirements and acceptance cases live in the pinned canonical contract.

## Next implementation gates

1. Emit a validated index and immutable generation metadata from the standalone installer.
2. Implement OS provider discovery and prove one real runtime invocation, including resource loading and receipts.
3. Verify absent/degraded providers, scope isolation, protected aliases, stale indexes, and generation changes during execution.
4. Verify OS Git state is unchanged by Skills lifecycle operations, and private/workspace skills survive them.
5. Verify Memory adapter preservation before migrating built-in canonical paths.
6. Complete the separate Brain host adapter and four-component acceptance suite before claiming integrated autonomous operation.
