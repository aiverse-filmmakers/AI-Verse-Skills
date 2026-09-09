# Original Upstream Skill Import Policy

**Decision:** use the best original upstream skill packages wherever possible.

## Rules

1. Do not rewrite an upstream skill merely to make it sound like AI-Verse.
2. Preserve the upstream package structure and filenames.
3. Preserve upstream authorship and required license notices.
4. Record provenance in `SOURCE.json` plus the central registries.
5. AI-Verse-specific permission, workspace, memory and secret policy must stay outside the original skill body.
6. A third-party skill never becomes first-party simply because it is vendored.
7. Future AI-Verse-authored skills live only under `skills/imported/ai-verse/`.
8. If direct redistribution is not appropriate, the installer may fetch the pinned original package from upstream.
9. Upstream updates are reviewed and diffed before they replace a trusted installed package.
10. Imported external instructions remain bounded by the host runtime's higher-priority permission and safety policy.

## SOURCE.json

Every vendored package gets a sibling `SOURCE.json` that records at least:

```json
{
  "source_namespace": "hermes",
  "upstream_repo": "NousResearch/hermes-agent",
  "upstream_path": "skills/email/email-inbox-triage",
  "upstream_commit": "<pinned commit>",
  "license": "MIT",
  "import_type": "original-vendored",
  "modified": false,
  "imported_at": "2026-09-09"
}
```

If the original package must be fetched rather than vendored, the same fields live in registry state with:

```json
{
  "import_type": "original-upstream-fetch"
}
```

## Modifications

If AI-Verse eventually must patch an upstream skill for compatibility:

- retain the original source record
- set `modified: true`
- record the patch/diff
- keep the upstream original available for comparison
- prefer adapter-side compatibility over editing upstream instructions

The default is zero modification.
