# Commands by package manager

Find the lockfile, use the matching row. Commands are as known in mid 2026; if one errors, check the tool's `--help` before guessing. Anything marked "separate install" needs the user's yes first.

## JavaScript

| Lockfile | Scan | Why is it here | What is behind | Change one |
| --- | --- | --- | --- | --- |
| `package-lock.json` (npm) | `npm audit --omit=dev`, then `npm audit` | `npm explain <pkg>` | `npm outdated` | `npm install <pkg>@<version>` |
| `pnpm-lock.yaml` (pnpm) | `pnpm audit --prod`, then `pnpm audit` | `pnpm why <pkg>` | `pnpm outdated` | `pnpm update <pkg>` |
| `yarn.lock` (yarn) | `yarn npm audit` (version 2 and later) or `yarn audit` (version 1) | `yarn why <pkg>` | `yarn outdated` | `yarn up <pkg>` or `yarn upgrade <pkg>` |

- Pin a nested package: `overrides` in `package.json` (npm), `pnpm.overrides` (pnpm), `resolutions` (yarn).
- Install exactly what the lockfile says: `npm ci`.
- Look at a package without running its scripts: `npm install --ignore-scripts`.

## Python

| File | Scan | Why is it here | What is behind |
| --- | --- | --- | --- |
| `requirements.txt` | `pip-audit -r requirements.txt` (separate install) | `pipdeptree -r -p <pkg>` (separate install) | `python3 -m pip list --outdated` |
| `uv.lock` | `pip-audit` inside the environment | `uv tree` | `uv pip list --outdated` |
| `poetry.lock` | `pip-audit` inside the environment | `poetry show --tree` | `poetry show --outdated` |

## Other languages

| Language | Scan | Why is it here |
| --- | --- | --- |
| Go | `govulncheck ./...` (separate install; reports only code that is really reached) | `go mod why -m <module>` |
| Rust | `cargo audit` (separate install) | `cargo tree -i <pkg>` |
| Ruby | `bundle audit check --update` (separate install) | `bundle outdated` |
| PHP | `composer audit` | `composer why <pkg>` |

## Any language

- `osv-scanner` (separate install) scans most lockfiles against the open OSV database. The command differs by version (`osv-scanner scan source -r .` in version 2, `osv-scanner -r .` in version 1); check `osv-scanner --help`.
- On GitHub, Dependabot alerts sit under the repository's Security tab.

## Licences

- JavaScript: `npx license-checker --summary` (downloads a tool; ask first).
- Python: `pip-licenses` (separate install).

Permissive licences (MIT, Apache 2.0, BSD, ISC) are fine for commercial work. Copyleft licences (GPL, AGPL) and packages with no licence need a decision from the user.
