# API integration checklist

## Sign in types

| Type | What you store | Watch for |
| --- | --- | --- |
| API key in a header | The key | Test and live keys are different; do not mix them |
| Bearer token | The token | It expires. Handle 401 by getting a new one |
| OAuth 2 (the user approves in a browser) | Client id, client secret, refresh token | Access tokens are short lived. Store the refresh token safely and renew before expiry |
| Basic (name and password) | Both | Only over HTTPS |
| Signed requests | A secret used to sign each call | Clocks must agree. A wrong clock looks like a wrong key |

## Paging styles

| Style | How to loop | Ends when |
| --- | --- | --- |
| Page number | Ask for page 1, 2, 3 | A page comes back empty or short |
| Offset and limit | Raise the offset by the limit | Fewer rows than the limit |
| Cursor or next token | Send back the token from the last answer | No token is returned |
| Link header | Follow the `next` link | No `next` link |

Always cap the loop (for example 1,000 pages) and say so if the cap is hit. Prefer cursors when offered: page numbers skip or repeat rows when data changes mid run.

## Retries

- Retry only calls that are safe to repeat: reads, and writes with an idempotency key.
- Wait = the smaller of a ceiling (say 60 seconds) and base × 2 to the power of the attempt, plus a little randomness so many clients do not retry together.
- If the answer has `Retry-After`, obey it.
- Stop after 3 to 5 attempts and report.

## Timeouts

Always set them. A sensible start: 10 seconds to connect, 30 seconds to read. A call with no timeout can hang forever.

## Webhooks

A webhook is the service calling you when something happens.

1. **Verify the signature** using the raw, unparsed body. Reject anything unsigned.
2. **Answer fast** (a 2xx within a few seconds), then do the work. Slow answers get retried.
3. **Expect repeats.** Store each event id and ignore one you have seen.
4. **Expect the wrong order.** Use the event's own timestamp, or fetch the current state.
5. **Reject old events** by timestamp, to stop replays.

## Data

- Dates: store in UTC, in `YYYY-MM-DDTHH:MM:SSZ` form.
- Money: whole numbers of the smallest unit (pence, cents), never decimals.
- Check required fields exist before using them. Services add and remove fields.
- Save one real answer as a sample file for tests.

## Logs

- Never log keys, tokens or full bodies holding personal data.
- Do log the request id from the response headers. Support teams ask for it.
