# Runtime Adapters

AI-Verse installs one canonical library and exposes it to runtimes through adapters instead of maintaining uncontrolled rewritten copies.

`registry/runtime-adapters.json` defines supported adapter modes. The installer `adapt` command takes an explicit target directory because AI-Verse-Skills must not guess user-specific runtime paths or silently alter another agent's configuration.

Adapters expose packages only. Filesystem scope, connections, secrets, approvals, memory authority and scheduling remain owned by the host runtime.
