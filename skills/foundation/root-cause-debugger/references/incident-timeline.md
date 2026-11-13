# What happened: rebuilding an incident

For when the failure is over and the question is why.

## Rules

1. **Save the evidence first.** Copy logs before they rotate. Do not restart or redeploy again until they are saved.
2. **One clock.** Convert every time to UTC. Note each source's time zone and how far its clock could be off.
3. **Fact or inference, every line.** A deploy five minutes before the failure is a suspect, not a cause, until you can show how it caused it.
4. **Never edit the originals** to make them easier to read. Work on copies.
5. **Write about systems, not people.** "The check did not run", not "X forgot".

## Sources

| Source | How |
| --- | --- |
| Code and deploy history | `git log --since="<start>" --until="<end>" --date=iso`, the host's deploy list |
| Application logs | The host's log viewer or log files, filtered to the window |
| Platform events | Restarts, scaling, failed health checks |
| Alerts and monitoring | When the first alert fired, and when someone saw it |
| Setting changes | Dashboard history, config commits |
| Outside services | Their status pages for the same window |
| People | When users first reported it, and what they saw |

## Timeline

| Time (UTC) | Source | Event | Fact or inference |
| --- | --- | --- | --- |

Start before the first sign of trouble and end after recovery is confirmed.

## Separate these five

- **Trigger:** what set it off.
- **Root cause:** why the system could fail that way at all.
- **Contributing factors:** what made it worse or longer.
- **Detection gap:** time from the start to someone knowing.
- **Recovery:** what ended it, and whether that was understood or lucky.

## Report

```
Summary:       two sentences
Impact:        who, what, for how long
Timeline:      the table
Trigger:
Root cause:
Contributing factors:
Detection gap:
Fixes:         done, and still to do (with an owner each)
Confidence:    high, medium or low, and the evidence that is missing
```
