---
name: api-integration-engineer
description: "Connect code to an outside service's API or SDK so it works on the first real run: sign in, paging, rate limits, retries, errors, and proof that it works. Use when the user says 'connect to the X API', 'pull my data from X', 'post to X when Y happens', 'set up a webhook', or when an integration fails with 401, 403, 429 or timeouts."
license: MIT
compatibility: "Needs network access and a way to read the service's official documentation. Credentials must be supplied by the user as environment variables or through the platform's secret store."
metadata:
  tier: foundation
  owner: ai-verse
---

# API Integration Engineer

An API is how one program talks to another service. Most integrations fail for the same three reasons, worst first:

1. **Written from memory.** The service changed its API since anyone last looked. The code is wrong before it runs.
2. **A write that runs twice.** A retry after a timeout charges the card again or posts the message twice.
3. **Page one only.** It works in the demo with 20 records and silently loses the other 480.

## Hard rules

1. **Open the official documentation for the exact version before writing a line.** Memory of an API is a lead, never a fact. Record the page and the date you read it.
2. **Keys never appear in code, chat, logs or commits.** They live in environment variables or the platform's secret store. Add `.env` to `.gitignore`; ship `.env.example` with names only.
3. **The first call is read only and as small as possible.** A "who am I" call proves sign in before anything else is built.
4. **A write that could repeat gets an idempotency key, or a check before writing.** Never retry a write automatically without one. (An idempotency key is a unique label that lets the service ignore a repeat.)
5. **Ask before any call that costs money, sends a message or changes live data.** Use the service's test mode when it has one.
6. **Ask for the narrowest permission that does the job.**
7. **Follow paging to the end,** with a safety cap.

## Step 1 — Fact sheet

Fill this from the documentation. Every blank is a bug waiting.

| Fact | Value |
| --- | --- |
| Base address and version | |
| Sign in method | |
| Permissions (scopes) needed | |
| Rate limit, and the headers that report it | |
| Paging style | |
| Error format | |
| Idempotency support | |
| Webhook signature method | |
| Test mode or sandbox | |
| Official SDK, and its last release date | |

Use the official SDK when it was released within the last year. Otherwise call the API directly: an abandoned SDK is worse than none.

## Step 2 — Smallest working path

Sign in, make one read call, print the shape of the answer. Do not write anything else until this works. Most failures are found here, cheaply.

## Step 3 — Build

Read `references/checklist.md` for the sign in types, paging loops, retry timing and webhook rules. Then:

- Set a timeout on every call.
- Check the answer has the fields you need before using it.
- Turn the service's errors into messages a person can act on.

| Status | Meaning | Retry? |
| --- | --- | --- |
| 400, 422 | The request is wrong. Read the body | No. Fix the request |
| 401 | Key missing, wrong or expired | No. Refresh or replace the key |
| 403 | Signed in, but not allowed | No. Missing permission or plan |
| 404 | Wrong id, or test data asked of the live service | No |
| 409 | Conflict or duplicate | No. Read the current state |
| 429 | Too many requests | Yes. Wait as long as `Retry-After` says, then back off |
| 500 to 504, timeout | The service's side | Yes, 3 to 5 times with growing waits, for safe calls only |

## Step 4 — Prove it

- [ ] The read call works
- [ ] Page two works, and the loop ends
- [ ] A deliberately wrong key gives a clear message, not a crash
- [ ] For writes: done in test mode, then read back
- [ ] For writes: run twice, and only one result exists
- [ ] No key appears in the code, the output or the logs

## Output

```
Service and version:  name, version (docs: link, read on <date>)
Sign in:              method, permissions; keys expected in NAME_A, NAME_B
What it does:
Proof:                read ok, page two ok, bad key handled, write read back, rerun made no duplicate
Limits:               rate limit; cost per call, if any
Not verified:
```

## Never

| Never | Instead |
| --- | --- |
| Code from memory of the API | Read the current documentation first |
| Paste a key into code or chat | Environment variable or secret store |
| Start with the write | Start with the smallest read |
| Retry a payment or a send blindly | Idempotency key, or check first |
| Loop forever on paging | Stop at the last page, with a cap |
| Swallow an error and return nothing | Say what failed and what to do |
| Test against live data | Test mode, then one confirmed live call |
