---
name: verification-harness
description: "Prove that work is really done before saying so: run the right checks and report what passed, what failed and what was not checked. Use when the user asks 'is it done', 'does it work', 'check it', 'make sure nothing broke' or 'test this', and before telling anyone that a fix, feature, page, export or upload is finished."
license: MIT
compatibility: "Needs a way to run or open the thing being checked: a terminal for code, a browser tool for pages, or the output file itself. Says so when one is missing."
metadata:
  tier: foundation
  owner: ai-verse
---

# Verification Harness

"Looks done" is a guess. Done is something you watched work.

Three failure modes, worst first:

1. **Calling it done from reading your own work.** Rereading code or a draft and finding it convincing is not a check.
2. **A green check that tests something else.** The tests pass and the button is still broken, because no test presses the button.
3. **Hiding what was not checked.** Silence reads as "all fine".

## Hard rules

1. **Never say done, fixed or working without a receipt** (Step 4).
2. **Check the outcome that was asked for, not a neighbour.** "The form sends a message" is proven by a message arriving, not by the test suite passing.
3. **Never report a check you did not run.** Not run is written "not run", with the reason.
4. **A check that cannot fail proves nothing.** For a bug fix, see the check fail on the old version first, or say why you could not.
5. **Read back anything stored or sent.** After writing a file, a record, an upload or a message, fetch it from where it lives.
6. **Report failures as they are.** No softening, and no quiet retries until it turns green.
7. **Checking and fixing are separate.** If a check fails, report it. After a fix, run every check again, not only the one that failed.

## Step 1 — Write the claim

Turn the request into one to five statements that can be seen to be true or false.

| Request | Claim to prove |
| --- | --- |
| "Fix the contact form" | A message sent from the live page arrives in the owner's inbox |
| "Export the video at 4K" | The file opens, is 3840 by 2160, and runs the full length with sound |
| "Add dark mode" | Every page switches, the choice survives a reload, text stays readable |

If you cannot write the claim, you do not yet know what done means. Ask.

## Step 2 — Choose the proof

| Kind of work | Proof that counts | Not proof |
| --- | --- | --- |
| Code change | The changed behaviour exercised, plus the project's own tests, build and lint | "The code looks right" |
| Bug fix | The original failing case now passes, with a check that failed before | A different case passing |
| Web page or app screen | Loaded in a browser, clicked through, no console errors, tried at phone width | A successful build |
| File or export (video, image, PDF, spreadsheet) | It opens, and size, length, resolution or row count match | The command ending without an error |
| Data change | Read back, with counts before and after | "Wrote 40 rows" |
| Message, upload, publish, deploy | Read back from the service; the live address loads | A "sent" status alone |
| Document or copy | Each requirement in the brief ticked against the text; facts traced to sources | Liking your own draft |

To find a project's own checks, look in `package.json` scripts, a `Makefile`, the README, `pyproject.toml` and any `.github/workflows` folder. If there are none, say so and check by hand.

## Step 3 — Run, in this order

1. **The direct proof of each claim.**
2. **What the project already has:** tests, build, lint, type check. Fast ones first.
3. **One neighbour that could have broken.** The page next to the one you changed; the feature that shares the code.
4. **The awkward inputs,** for anything a person types into: empty, very long, wrong type.

Stop at the first failure and report it. Later checks on a broken thing mislead.

### When a check fails: is it the work or the check?

- **The work:** the behaviour really is wrong. Report it.
- **The check:** a missing package, the wrong environment, a stale saved result, a test that fails at random. Say which, and how you know.
- **Already failing before your change:** prove it by running the same check on the earlier version, then say "failing before this change".

Never delete, skip or loosen a failing check to get a pass.

## Step 4 — The receipt

```
Claim:        the contact form sends a message to the owner
Verdict:      DONE | NOT DONE | PARTLY
Passed:       - sent a test message from the live page; it arrived in 20 seconds
              - npm test: 42 passed
Failed:       - none
Not checked:  - phone layout (no browser tool available at narrow width)
Evidence:     commands run, screenshots, file paths, links
```

| Verdict | Only when |
| --- | --- |
| DONE | Every claim has a proof that passed, and nothing failed |
| NOT DONE | Anything failed |
| PARTLY | Nothing failed, but at least one claim has no proof yet |

Lead with the verdict. A person reading only the first line must not be misled.

## Never

| Never | Instead |
| --- | --- |
| "Should work now" | Run it, then say what happened |
| "All tests pass", when none cover the change | Say the tests do not cover it, then prove it directly |
| Report a command you did not run | "Not run", with the reason |
| Retry a random failure until it passes, quietly | Report the failure rate |
| Skip or weaken a failing check | Report it |
| Bury an unchecked item in the middle | List it under "Not checked" |

## Project adjustments

If the current project has adjustments for this skill (its check commands, its definition of done, the browsers and devices that matter), apply them. Where they disagree with these instructions, the project's adjustments win.
