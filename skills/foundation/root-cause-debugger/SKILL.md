---
name: root-cause-debugger
description: "Find the real cause of a failure before changing anything, then fix it with a check that proves it. Use when something is broken or flaky: an error or crash, 'it worked yesterday', 'works on my machine but not on the server', a test that fails only sometimes, a wrong result, a setting that seems to be ignored, or when asked what went wrong after an outage."
license: MIT
compatibility: "Needs a terminal and read access to the code, logs or error text. Git helps but is not required."
metadata:
  tier: foundation
  owner: ai-verse
---

# Root Cause Debugger

Diagnose first. A fix made before the cause is known is a guess, and guesses pile up.

Two failure modes, and the first is worse:

1. **Patching the symptom.** Fixing the line that threw the error instead of the reason it received bad input. The bug comes back somewhere else.
2. **Shotgun changes.** Changing three things at once. Even when it works, nobody knows why, and one of the three is now a new bug.

## Hard rules

1. **No fix until you can state the cause in one sentence and show the evidence.** Temporary logging is allowed; remove it afterwards.
2. **Reproduce first.** If you cannot make it fail on demand, say so and gather more evidence. Do not guess.
3. **One hypothesis, one test, one change at a time.**
4. **Three failed hypotheses: stop.** Show what you ruled out and ask the user. A fourth guess is rarely better than the first three.
5. **Read the whole error, and the first error, not the last.** Later errors are usually fallout.
6. **Never print secret values.** Names of keys and variables only.
7. **Touch nothing unrelated.** Undo every experiment that did not help.

## Step 1 — Pick the path

| What you are told | Go to |
| --- | --- |
| "It worked before", broke after a change or update | **Regression** below |
| "Works here, not there" (another machine, the server, CI) | `references/environment.md` |
| A setting, flag or environment variable seems ignored, or differs between places | `references/configuration.md` |
| It is already over and the question is "what happened?" | `references/incident-timeline.md` |
| It fails only sometimes | **Flaky** below |
| Anything else | **Standard loop** below |

## Step 2 — Standard loop

1. **Reproduce.** Find the smallest command or input that fails. Write down the exact error and where it appears.
2. **Bound it.** What still works? Another input, the previous version, another machine. The cause lives in the difference.
3. **List hypotheses** in a table, cheapest test first:

   | # | Hypothesis | What it would explain | Cheapest test | Result |
   | --- | --- | --- | --- | --- |

4. **Test the top one. Record the result. Repeat.** A hypothesis that explains only part of the symptoms is not the cause.
5. **Trace backwards** from the failing line to where the bad value first appeared. That place is the cause; the failing line is only where it was noticed.

### Regression

Find the change, do not reason about it.

```bash
git log --oneline <last-good>..HEAD      # few commits: read them
git bisect start && git bisect bad && git bisect good <last-good>
# test, then: git bisect good   or   git bisect bad   (repeat until it names the commit)
git bisect reset
```

`git bisect` halves the list of changes each round until one is left. No code change in that commit? Compare the lockfile (the file that pins package versions): an updated package is a change too.

### Flaky

1. Run it 20 times and note the failure rate. You cannot prove a fix without the starting rate.
2. Suspects, most common first: state shared between tests or runs (order matters), timing and races, dates and time zones, the network, randomness without a fixed seed.
3. A fix counts only when it runs clean three times as many runs as it took to fail once (failed 1 in 10: 30 clean runs).

## Step 3 — Fix and prove

1. Make the smallest change that removes the cause.
2. Add a check that fails before the fix and passes after: a test, or the reproduce command.
3. Re-run the original failing case, not a similar one.
4. Remove temporary logging and experiments.

## Output

```
Cause:        one sentence
Evidence:     what showed it (command and result, file and line)
Ruled out:    each hypothesis and why
Fix:          what changed and where
Proof:        the check that failed before and passes now
Not verified: anything you could not check
```

If you did not find the cause, say so, and hand over the hypotheses table. That is a useful result; a confident wrong answer is not.

## Never

| Never | Instead |
| --- | --- |
| "It is probably X", then edit | Test X first |
| Catch the error and carry on | Find why it is raised |
| Add a retry or a wait to hide a flaky failure | Find the shared state or the race |
| Reinstall or upgrade everything | Compare versions, change one |
| Call it fixed because the message changed | Re-run the original failing case |
| Leave debug logging in | Remove it before reporting |

## Reference files

| File | Load when |
| --- | --- |
| `references/environment.md` | It works on one machine and not another |
| `references/configuration.md` | A setting seems ignored or differs between places |
| `references/incident-timeline.md` | Rebuilding what happened after an outage |
