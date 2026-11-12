# A setting seems ignored

A setting is usually set in more than one place, and a place you forgot is winning.

## Who wins

Typical order, strongest first. Check the tool's own documentation, because some differ.

1. Command line flag
2. Environment variable set in the shell or by the host
3. Local env file (`.env.local`)
4. Env file (`.env`)
5. Project config file
6. User level config file
7. Built in default

## Method

1. **Find the value the program really used.** Print the effective config, or log it at startup. Show names and non secret values only; for secrets show whether it is set and its length.
2. **Find every place the key is set.** Search the project (`grep -rn "KEY_NAME" .`), then check the shell profile, the CI settings and the hosting dashboard.
3. **Apply the order above** to see which one wins.
4. **Fix it in one place**, the lowest level that should own it, and delete the copies that shadow it.
5. **Re-run and read the effective value again.**

## Traps

| Trap | Sign |
| --- | --- |
| Env file is not loaded in production | Works locally, default value on the host. Hosts read their own dashboard settings |
| Baked in at build time | Changing it does nothing until a rebuild. Many web frameworks freeze public variables when building |
| No restart | The old value stays until the process restarts |
| Set in one shell, started from another | Works in the terminal, not from the app launcher or the scheduler |
| Wrong name or wrong capitals | `API_KEY` and `APIKEY` are different keys |
| Quotes or a trailing space in the env file | The value is almost right |
| The text `false` | Any non empty text can count as true |
| Missing key, silent default | No error, wrong behaviour |
| Different key names per environment | Staging and production disagree |

## Report

| Key | Where it is set | Value (secrets hidden) | Wins? |
| --- | --- | --- | --- |

List the required keys, names only, in `.env.example` so the next machine is not a mystery.
