# Package Resolution and Reproducibility

**Snapshot:** 2026-09-09

AI-Verse-Skills preserves original upstream packages and pins every employee-facing source to an exact Git commit.

## Acquisition modes

- `vendored`: the complete original package is stored in this repository and provenance is recorded beside it.
- `upstream-fetch`: the installer fetches the pinned upstream commit, resolves the package, and copies the complete original package directory without rewriting it.

The six proof packages remain vendored. The remaining employee packages use pinned upstream-fetch so the distribution can be complete without duplicating dozens of actively maintained upstream repositories.

## Selector order

1. Exact package path when verified.
2. Repository root for a skill whose whole repository is the package.
3. Deterministic `SKILL.md` frontmatter-name search at the pinned commit when the upstream folder structure is not stable or was not worth hard-coding.

Canonical AI-Verse names are stable. An upstream rename is represented as an alias/selector change, not by breaking the canonical capability ID.

## Dependencies

Support packages required by a canonical capability are installed automatically and do not increase the canonical count of 100. For example, Google employee personas can require `gws-gmail`, `gws-calendar`, `gws-drive`, `gws-chat`, and `gws-sheets`.

## Trust boundary

Fetching an original package does not make it a permission authority. Runtime grants are still enforced by AI-Verse OS or whichever host agent is using the library. Third-party instructions are not allowed to expand filesystem scope, network access, secret access, approvals, memory authority, or scheduling.
