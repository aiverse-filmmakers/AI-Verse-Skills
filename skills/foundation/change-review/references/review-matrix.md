# Risk-based code review matrix

Use the sections relevant to the changed code; this is a question set, **not** an instruction to presume a defect.

| Area | Review questions | Minimum useful evidence |
| --- | --- | --- |
| Identity and scope | Is principal/system/workspace derived from trusted host or arbitrary client text? Does retarget/rebind revoke leases? | Negative different-principal, different-workspace, root swap checks |
| Authorization/effects | Is owner grant checked at the final effect edge? Can an untrusted user or agent approve their own action? | Deny-before-write, revoke-before-dispatch, forged grant tests |
| API contracts | Does owner actually expose the route at the target revision? Are schema and error states versioned? | Owner source pin, valid/invalid shape checks, no phantom routes |
| Credentials/network | Could token, secret handle, OAuth state, private URL or raw upstream errors leak to browser/logs? | Redaction, origin/redirect, payload-bound, malicious error tests |
| Persistence | Are CAS revision, atomicity, idempotency and backup/rollback truthful? | Retry, stale version, process restart and crash recovery tests |
| Async/stream | Can old events/results cross pane/workspace? Are duplicate SSE or uncertain POSTs handled? | A→B→A, replay, terminal reconciliation, cancel races |
| Files and media | Are MIME, digest, size, path, symlink, remote URL and modality verified by actual owner? | Hostile uploads, unauthorized asset ID and revoked receipt tests |
| Model/provider costs | Can any model ID trigger unapproved paid inference? Is unknown cost displayed as unknown? | Gateway final-dispatch model admission, Token receipt provenance |
| Browser and UX | Is focus, accessibility, feedback, empty state and error/recovery real, not decorative? | Playwright browser actions and explicit failures |
| Dependency/release | Are draft owner PRs accidentally treated as released main? Is provenance/licensing valid? | Target-base comparison, pinned CI, review and deploy gates |

## Acceptance decision

- `approve-ready`: examined scope has no observed material defect and all required *scoped* evidence is available; still not an independent or GitHub approval.
- `approve-ready-with-nonblocking-notes`: no blockers; documented low risk.
- `changes-required`: concrete P0/P1/P2 defect supported by source/trigger.
- `blocked-insufficient-evidence`: essential source, owner contract, test or review context is unavailable.

Review scope can be **partial**. A `no findings` verdict on a subcomponent never certifies the entire parent PR.

### GitHub status distinction

`draft`, `ready for review`, `CI green`, `AI-assessed`, `GitHub approved`, `merged`, `formally accepted` and `deployed` are separate states. For a stacked PR, record both its current base and the intended ultimate target. Never use a role-played agent, own second account or a self-authored skill to fake independent reviewer status.
