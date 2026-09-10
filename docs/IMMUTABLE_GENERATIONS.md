# Immutable Generation Lifecycle

**Status:** implemented lifecycle contract for audit item 9 / 19  
**Scope:** AI-Verse-Skills only

## Why this exists

A live skill is more than `SKILL.md`. It may include scripts, references, templates, assets and support files. If an update replaces a live tree while an execution is in progress, one execution can read instructions from version A and then invoke a script from version B.

That mixed-generation state is forbidden.

AI-Verse-Skills therefore treats every installed distribution as an immutable generation and makes activation a single atomic pointer change.

## Filesystem model

The canonical root is still:

```text
~/.aiverse/skills/
```

It is now a lifecycle controller rather than the mutable package tree:

```text
~/.aiverse/skills/
└── .aiverse/
    ├── active.json
    └── generations/
        ├── gen-.../
        │   ├── foundation/
        │   ├── imported/
        │   ├── dependencies/
        │   └── .aiverse/installed.json
        └── gen-.../
            └── ...
```

Each generation manifest records:

- `generation_id`
- `generation_schema_version`
- `generation_digest_sha256`
- profile and snapshot metadata
- every package path and package digest
- pinned source provenance already present in the distribution manifest

The generation digest excludes only its self-describing `installed.json` file so the manifest can contain the digest without recursion.

## Activation contract

`active.json` is the only mutable selection point.

Activation is performed by writing a complete temporary JSON file, flushing it, then replacing `active.json` atomically. A reader therefore sees either the previous complete pointer or the next complete pointer.

A malformed existing pointer is never treated as if it were absent. Activation fails closed instead of overwriting unknown or damaged rollback state.

## Execution pinning

Every execution must capture the active generation before reading package content:

```bash
./aiverse-skills pin --json
```

or for a specific package:

```bash
./aiverse-skills pin --package <canonical-package-id> --json
```

The pin returns:

- `generation_id`
- `generation_path`
- `generation_digest_sha256`
- optional package path / `SKILL.md` path

The runtime must use that returned generation path for the entire execution. It must not re-resolve the active generation halfway through the task.

Because update, rollback and uninstall never delete or rewrite committed generations, an in-flight execution can safely continue to read its original `SKILL.md`, scripts and assets after the active pointer changes.

## Lifecycle serialization

The following operations are serialized by one per-root lifecycle lock:

- install
- update
- rollback
- uninstall

The lock lives beside the canonical root rather than inside a generation, so replacing or deactivating a generation cannot invalidate the lock itself.

A recent lock is not stolen. A clearly stale lock can be recovered after the stale threshold.

## Install and update

The lifecycle is:

1. acquire the lifecycle lock
2. build the requested profile into a unique staging directory
3. write its generation-aware manifest
4. verify every package digest and the full generation digest
5. commit the stage to `.aiverse/generations/<generation-id>/`
6. verify the committed generation again
7. atomically activate only the new generation ID

If activation fails, the previous `active.json` remains authoritative. A handled failed commit is cleaned up when it was never activated.

No update edits the currently active generation in place.

## Legacy schema-2 install migration

A pre-generation install is recognized by the old root-level `.aiverse/installed.json` without `active.json`.

On the first lifecycle mutation, the installer:

1. verifies the old install before touching it
2. moves it to a timestamped recovery backup
3. copies that verified content into an immutable legacy generation
4. adds generation metadata and digests
5. activates the migrated generation
6. continues with the requested mutation

The old content therefore becomes a valid rollback generation rather than being discarded.

## Rollback

Rollback never swaps or rewrites package directories.

It verifies the selected previous generation and atomically changes `active.json` back to that generation ID. The generation being left remains on disk and can itself become a later rollback target.

## Uninstall

Uninstall is pointer-level deactivation.

It changes `active.json` to `state: uninstalled` and retains the last active generation in rollback history. Generation bytes remain present so:

- in-flight executions keep working from their pins
- rollback can recover the install
- forensic verification remains possible

This is intentionally different from deleting a mutable live tree.

## Runtime adapters

Materialized adapters write `.aiverse-adapter.json` containing:

- adapter schema version
- runtime ID
- canonical source root
- exact `generation_id`
- exact generation digest
- each package digest
- source and target path
- `symlink` or `copy` mode

A copied adapter never silently becomes a mixture of generations. Package refreshes are staged before destination replacement.

After the canonical active generation changes, `adapter-verify` rejects an adapter bound to an older generation as stale:

```bash
./aiverse-skills adapter-verify --target <runtime-skill-root>
```

For diagnostics only, this verifies internal consistency without claiming currentness:

```bash
./aiverse-skills adapter-verify --target <runtime-skill-root> --allow-stale
```

A stale adapter may still be internally valid for its old generation, but a runtime must not claim it represents the current active Skills distribution.

## Failure invariants

The lifecycle must preserve these invariants:

1. A committed generation is never updated in place.
2. The active selection changes through one atomic pointer replacement.
3. A pin identifies one complete generation for the lifetime of an execution.
4. Update cannot make an existing pin resolve to new bytes.
5. Rollback cannot make an existing pin resolve to different bytes.
6. Uninstall cannot delete bytes needed by an existing pin.
7. A malformed active pointer fails closed.
8. Concurrent lifecycle mutations cannot interleave.
9. A copied adapter records and verifies its source generation.
10. A stale adapter is rejected as current.
11. Package and generation digest mismatches block pin/verification.

## Acceptance coverage

`tests/test_generation_lifecycle.py` covers:

- one execution pinned to v1 while v2 activates
- the same pin surviving rollback
- the same pin surviving uninstall
- instruction + helper-script consistency across those transitions
- simulated interruption during atomic activation
- concurrent lifecycle lock contention
- committed generation tampering
- copied adapter generation binding
- stale adapter rejection after active generation changes

The full E2E workflow additionally exercises the real 100-capability distribution through install, pin, copied adaptation, update, stale-adapter rejection, rollback, uninstall and recovery.

## Deliberate boundary

This lifecycle does **not** implement the provider capability index or OS-side four-provider discovery. Those are later audit items. Generation metadata here exists only to guarantee lifecycle consistency and safe execution pinning.
