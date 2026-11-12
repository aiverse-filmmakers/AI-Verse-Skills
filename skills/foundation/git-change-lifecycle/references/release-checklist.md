# Release checklist

Releasing is the user's decision. This checklist says whether the evidence supports it. Never release, deploy or publish without an explicit yes.

## Before: every line needs evidence

| Gate | Evidence |
| --- | --- |
| What is going out | Version, the list of changes, who is affected |
| Checks | Passing on the exact commit being released, not an earlier one |
| Security | No open critical finding in the code or its packages |
| Settings and secrets | Every required name exists in the target environment (names only, never values) |
| Data changes | Can be reversed, or a backup was taken and its restore is known to work |
| Way back | The previous version's id, and the exact command or button that returns to it |
| Rollout | All at once or gradual; any switch that can turn the new part off |
| Watching | Who is watching, which signals, for how long |
| Timing | Not late on a Friday; not right before the only person who can fix it leaves |
| People | Change notes written; anyone affected has been told |

## Verdict

| Verdict | When |
| --- | --- |
| GO | Every gate has evidence |
| GO, WITH CONDITIONS | A gate is open, the user accepts it by name, and it is written down |
| NO GO | Any gate has no evidence, or two pieces of evidence disagree |

Pressure, deadlines and "it worked last time" are not evidence.

## After: prove it is healthy

1. Load the main pages. Do the most important thing a user does, once, for real.
2. Confirm the version shown is the new one.
3. Watch the logs for new errors for at least ten minutes.
4. Compare the key signals with before: errors, sign in, payments, page speed.

**If it is bad: go back first, find out why afterwards.** A slow investigation on a broken live service costs more than a quick return to the last good version.

## Report

```
Released:    version, commit, when, by whom
Verdict:     GO, GO WITH CONDITIONS or NO GO, with the open gates
Health:      what was checked after, and the result
Way back:    still available? how?
Follow ups:
```
