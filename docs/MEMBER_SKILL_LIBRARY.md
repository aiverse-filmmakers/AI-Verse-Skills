# Member skill library v1

Status: step 2 implementation, not yet integrated into an admitted Core release.
Skills owns the private package lifecycle; OS discovery and workspace bindings are implemented in OS step 3; learning and
installation-root wiring are implemented locally in step 4. No composed release
is admitted yet.

## Purpose and boundaries

Create reusable member-owned skill packages by importing an authored package
folder. The same procedure has one stable ID and retained immutable revisions.
The command copies a package; it never moves/deletes its source, runs scripts,
installs dependencies, enables hooks, grants access or publishes it publicly.
The published managed Skills generation remains unchanged.

Use an explicit personal library root established by the host/installation.
There is no implicit global writable root. A managed Skills root is refused.
Sources must be separate from the destination root; existing legacy packages
remain in place, and no automatic migration or recursive workspace crawl occurs.

## Public CLI

Run through the existing `installer/aiverse_skills.py` entrypoint:

```text
python installer/aiverse_skills.py library --library-root <personal-root> list
python installer/aiverse_skills.py library --library-root <personal-root> doctor
python installer/aiverse_skills.py library --library-root <personal-root> import \
  --source <authored-package> --source-scope workspace:alpha --visibility shared \
  --admission-json <admission.json> [--provenance-json <provenance.json>]
```

The import command prints a read-only preview. Save that exact JSON, inspect it,
then repeat the command with `--apply-plan <preview.json>`. For a new revision,
include `--id <existing-stable-id>` during preview. Apply is bound to that ID;
if supplied again it must match. Same names never imply replacement.

Shared admission is exactly:

```json
{"reusable":true,"contains_workspace_data":false,"contains_credentials":false,"has_workspace_dependencies":false}
```

These are semantic declarations from the authorized caller after review, not a
claim that pattern matching can prove portability. For restricted packages use
`--visibility workspace:alpha` with the same source scope and `{}` admission;
credentials are forbidden for every scope. The trusted OS host must derive and
enforce caller scope. This owner CLI is not an authentication boundary between
users who already have filesystem access to the library.

Optional provenance JSON:

```json
{"origin":"member-authored","license":"local-private","dependencies":[],"requested_capabilities":[],"requires_connection":false,"requires_credential":false}
```

Without it, origin is `local-import` and license is `not-declared`; no public
redistribution right is inferred. Complete package content, including LICENSE,
references, helpers and assets, is retained. Declarations only document requested
requirements. The caller must inventory actual dependencies and resource needs;
the importer does not promise to discover every implicit dependency.

Rollback to an existing verified revision:

```text
python installer/aiverse_skills.py library --library-root <personal-root> \
  select-revision --id <stable-id> --revision <digest> --expected-index <index-digest>
```

`expected_index` is emitted by preview/apply and available as the Python
`index_digest(root)` function. No-op selection leaves the index unchanged.
Normal success exits 0; failed doctor and validation errors exit 2. No credentials
should appear in command arguments, admission or provenance files.

## Persisted contract

`aiverse-member-skill-library-v1` stores:

```text
<root>/.aiverse/member-library/index.json
<root>/.aiverse/member-library/packages/<stable-id>/<digest>/SKILL.md
```

The index has `contract`, monotonic `sequence`, `skills`, and `events`.
A skill record has `id`, `active_revision`, active `name`, `description`,
`visibility`, and `revisions`. Each revision records those metadata fields plus
`source_scope`, original `source` path, `admission`, `provenance`, and exact
relative `path`. The source path is private provenance, not an access grant.
Revision digest is existing `aiverse-package-sha256-v1`; qualified identity is
`local:skill-<UUID hex>`. Friendly names can collide. Owner index metadata must
be backed up with packages; it is not a disposable search index.

Preview contract `aiverse-member-skill-import-v1` binds contract, operation,
library_root, source, source_revision, expected_index, id, source_scope,
visibility, admission, provenance and metadata. Apply refuses altered source,
arguments, identity or library state; plans are not cryptographic authorization.
Read JSON with duplicate fields, non-finite values, redirection or excessive size
is refused. Packages require bounded name/description frontmatter in SKILL.md.

Admission reuses Skills scanning and refuses deny/review findings. Limit: 256
files, 1 MiB each, 8 MiB total; index limit 4 MB; plan limit 32 KiB; provenance
limit 16 KiB. Symlinks/junctions/reparse points, special entries and embedded Git
metadata require separate review and are not imported. Local trusted filesystem
access remains a prerequisite; hostile concurrent filesystem replacement is not
a supported isolation boundary.

## Transactions and recovery

1. Preview does not create the library.
2. Apply acquires the existing Skills lifecycle lock inside this library.
3. Revalidate source, metadata and expected index; stage and rehash a full copy.
4. Publish an immutable revision, then atomically replace the index as commit.
5. Append a timestamped effect ID/event; repeating the exact plan verifies its
   retained revision and returns `already-imported` without another event.

Failure before index commit never activates the new package. A verified orphan
revision can be reused by retrying the unchanged preview; it is not listed as an
active skill. No automatic garbage collection deletes interrupted artifacts.
A live or unknown lock holder is refused. Proven-dead local holders use the
existing owner's stale-lock threshold; foreign/ambiguous locks need inspection.
Doctor checks all indexed retained revisions; missing/damaged bytes produce
failure rather than success. An idempotent retry does not mask corruption.

Durability uses file fsync plus atomic local-filesystem replacement, matching the
existing owner mechanism; no power-loss or distributed/network filesystem
transaction guarantee is claimed. Cross-platform execution and composed Core
qualification belong to step 5.

## Evidence and limits

`tests/test_member_library.py` covers owner API and real CLI preview/apply/list/
doctor, source preservation, duplicate names, restricted visibility, revisions,
rollback, stale previews, admission, redirection, interruption/retry and locking.
It is included in the repository's existing unittest discovery workflow.

Step 2 does not yet make these packages selectable in the installed OS. It does
not change learned proposal activation or native runtime discovery. Those are
steps 3 and 4. Do not manually update member installations to this source.

## Governed learning binding (step 4)

`library --library-root <root> configure-learning` previews the managed owner's
learning destination; add `--apply` to establish it. A different existing root is
refused. This stores `aiverse-member-learning-route-v1` in the managed owner's
`.aiverse/learning/member-library.json` and does not create or move member skills.
Distribution supplies the same root to OS and Skills through these owner APIs.

New create proposals retain normal proposal/approval and auto-mode evaluation.
Explicit four-field portability admission plus `agent_learned` permits shared
placement. `workspace_local` stays private even with portable method. Unknown
portability remains workspace-restricted or an operator draft, never implicitly
shared, and cannot bypass the private-auto policy. Brain must bind origin scope.
Applied proposals record the new member identity and revision with their original
candidate/provenance retained. They do not publish a new managed generation.
Legacy repair/update flows retain their existing protected-owner restrictions.

Rollback of an unchanged member create disables that identity, retaining all
bytes. A newer active revision blocks rollback. Explicit `set-enabled --id <id>
--state enabled|disabled --expected-index <digest>` is the bounded owner operation;
it is not deletion. Re-enabling still grants no runtime permission.

Component doctor verifies a configured library, including retained revisions.
JSON doctor failures now have nonzero exit status, so the composing lifecycle
cannot mistake a failed integrity check for success.
