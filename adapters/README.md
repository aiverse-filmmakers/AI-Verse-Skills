# Runtime Adapters

AI-Verse installs one canonical library and exposes it to runtimes through adapters instead of maintaining uncontrolled rewritten copies.

`registry/runtime-adapters.json` defines supported adapter modes. The installer `adapt` command takes an explicit target directory because AI-Verse-Skills must not guess user-specific runtime paths or silently alter another agent's configuration.

Every materialized adapter is bound to one immutable Skills generation. Its `.aiverse-adapter.json` records the generation ID, generation digest, package digests, source paths and materialization mode.

When the active Skills generation changes, an older copied or linked adapter is **stale**. `adapter-verify` rejects it as current even if its old files are still internally valid. Use `--allow-stale` only to prove that the adapter still exactly matches the immutable generation it was created from.

Package replacement during `adapt --force` is staged per package before the destination is swapped. An interrupted refresh therefore leaves either the old package or the complete new package; the adapter manifest/digests expose any partial cross-package refresh and verification fails closed.

Adapters expose packages only. Filesystem scope, connections, secrets, approvals, memory authority and scheduling remain owned by the host runtime.
