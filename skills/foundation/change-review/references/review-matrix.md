# Risk-based code review matrix

Use the sections relevant to the changed code; this is a question set, **not** an instruction to presume a defect.

| Area | Review questions | Minimum useful evidence |
| --- | --- | --- |
| Identity and scope | Is the user, account or workspace taken from a trusted server side source, or from text the client sent? Does switching account drop old access? | Tests where a different user and a different workspace are refused |
| Permissions and effects | Is permission checked at the final point where the change happens? Can someone approve their own action? | Refused before write, refused after access is withdrawn, forged approval rejected |
| API contracts | Does the API really exist at the target revision? Are the shapes and error states versioned? | The source pinned, valid and invalid shapes tested, no calls to routes that do not exist |
| Credentials and network | Could a token, a secret, sign in state, a private address or a raw upstream error reach the browser or the logs? | Redaction, redirect and origin checks, hostile error tests |
| Stored data | Are writes atomic and safe to repeat? Are stale versions rejected? Do backup and rollback really work? | Retry, stale version, restart and crash recovery tests |
| Async and streams | Can an old result arrive in the wrong view or workspace? Are duplicate events and uncertain sends handled? | Switch away and back, replay, cancel races |
| Files and media | Are type, size, path, links and remote addresses checked on the server? | Hostile uploads, a file id the user does not own |
| Paid calls | Can any request trigger a paid call without approval? Is an unknown cost shown as unknown? | Refusal at the final dispatch point, cost shown with its source |
| Browser and UX | Are focus, accessibility, feedback, empty and error states real, not decorative? | Real browser actions, including the failures |
| Dependencies and release | Is something from an unmerged draft treated as released? Are provenance and licence valid? | Comparison with the target branch, pinned CI, review and deploy gates |

## Acceptance decision

- `approve-ready`: examined scope has no observed material defect and all required *scoped* evidence is available; still not an independent or GitHub approval.
- `approve-ready-with-nonblocking-notes`: no blockers; documented low risk.
- `changes-required`: concrete P0/P1/P2 defect supported by source/trigger.
- `blocked-insufficient-evidence`: essential source, owner contract, test or review context is unavailable.

Review scope can be **partial**. A `no findings` verdict on a subcomponent never certifies the entire parent PR.

### GitHub status distinction

`draft`, `ready for review`, `CI green`, `AI-assessed`, `GitHub approved`, `merged`, `formally accepted` and `deployed` are separate states. For a stacked PR, record both its current base and the intended ultimate target. A second prompt, persona or account run by the same author is not an independent reviewer.

## Credits

Review workflow design informed by publicly available methodologies, not copied skill files:
- [Coder Deep Review](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/SKILL.md): depth triage, specialist review lenses, duplicate/contradiction handling, large PRs.
- [Google Gemini CLI Code Reviewer](https://github.com/google-gemini/gemini-cli/blob/main/.gemini/skills/code-reviewer/SKILL.md): PR/local target selection, preflight and source inspection.
- [Flutter iterative Code Review](https://github.com/flutter/agent-plugins/blob/main/.agents/agents/reidbaker-agent/skills/code-review/SKILL.md): iterative critique, concrete changed-line feedback and noise reduction.
- [Review governance](https://github.com/Quegenx/agent-skills/blob/main/skills/engineering/code-review/SKILL.md): verified findings, risk-based merge gates and rollback.

These projects may have different licenses or environment/tool requirements. This AI-Verse skill is independently authored and does not assume parallel agents, tool permissions or external installation.
