# Runtime Readiness Verification

AI-Verse Skills separates **package installation** from **runtime readiness**.

A capability being installed does not prove that its required app, CLI, connector, account, browser session, or host runtime can actually perform work now.

## Readiness rule

`ready` is reserved for an operator that has been verified usable during the current readiness check.

Static evidence is intentionally weaker:

- `installed-unverified` — an app or CLI is present, but usable/authenticated operation was not proved.
- `configured-unverified` — configuration indicates a connection should exist, but no live verification succeeded.
- `needs-connection` — a connector/API/MCP-backed operator has no usable connection proof.
- `host-runtime-unverified` — the host may supply the operator, but the host has not proved it usable.
- `missing-local-app` / `missing-local-dependency` — required local software is absent.
- `authentication-failed`, `unreachable`, `unusable`, `probe-failed`, `probe-timeout`, or `invalid-probe-result` — a live verification attempt failed closed.

Environment flags such as `AI_VERSE_CONNECTION_GOOGLE_WORKSPACE=connected` are retained only as migration/configuration hints. They can never produce `ready`.

Likewise, the mere presence of `gws`, `hs`, Premiere Pro, or After Effects cannot produce `ready` for their connector/automation-backed workflows.

FFmpeg is a deterministic local exception: Skills can execute `ffmpeg -version` and `ffprobe -version` directly. Both must execute successfully during the check.

## Live probe registry

Hosts and connector adapters can register live probes without giving AI-Verse Skills secrets.

Default registry path when the Skills root is `~/.aiverse/skills`:

```text
~/.aiverse/readiness/probes.json
```

A custom registry path can be selected with `AI_VERSE_READINESS_PROBES`. The variable points to configuration only; it is not readiness evidence.

Registry schema:

```json
{
  "schema_version": 1,
  "probes": {
    "google-workspace": {
      "command": ["my-host-adapter", "probe", "google-workspace", "--json"],
      "timeout_seconds": 5
    }
  }
}
```

Commands are executed directly with `shell=false`. Shell command strings are not accepted. Timeouts must be greater than zero and no more than 30 seconds.

A connector/API/MCP probe succeeds only when it exits zero and writes one strict JSON object to stdout:

```json
{
  "schema_version": 1,
  "operator_id": "google-workspace",
  "authenticated": true,
  "reachable": true,
  "usable": true
}
```

For non-authenticated runtime probes, `authenticated` may be omitted, but `reachable` and `usable` are always required.

Unknown payload fields are rejected. This prevents probe output from accidentally becoming a channel for tokens, account data, or arbitrary diagnostics.

AI-Verse Skills never includes probe stdout, stderr, command arguments, tokens, or secret values in its readiness report.

## Machine-readable output

Run:

```bash
python installer/aiverse_skills.py readiness --json
```

Readiness v2 preserves the compatibility map:

```json
"operators": {
  "google-workspace": "ready"
}
```

and adds structured evidence:

```json
"operator_details": {
  "google-workspace": {
    "status": "ready",
    "ready": true,
    "live_verified": true,
    "checked_at": "...",
    "evidence": [
      {
        "kind": "live-probe",
        "result": "passed",
        "authenticated": true,
        "reachable": true,
        "usable": true
      }
    ]
  }
}
```

The report also carries the active immutable `generation_id`. Skill-level readiness is computed only after operator verification: a skill is immediately ready when it requires no operator, or when every required operator is `ready`.

## Trust boundary

This contract proves runtime readiness only. It does **not** grant permissions, approvals, authority, or effect certainty. Those remain separate policy/execution concerns.

Provider Contract v1 remains static and generation-bound; live readiness is intentionally evaluated outside immutable provider metadata so a generation never becomes stale merely because a remote service changes state.
