# Review depth

Choose before inspecting code.

- **Focused**: docs-only, a narrowly scoped single-file change or less than ~100 changed lines. Review the intended contract, diff, applicable tests, provenance and actual acceptance language. Never claim a code security audit for a docs-only PR.
- **Standard**: a bounded multi-file feature. Examine changed code plus callers, failure paths, existing abstractions and targeted tests. Apply test, edge-case and owner-contract passes.
- **Deep**: more than ~500 changed lines, 3+ affected subsystems, permissions, credentials, storage migration, cross-process concurrency or billable model dispatch. First split a huge stacked PR into reviewable dependency-ordered slices, then apply test authenticity, adversarial edge case and owner-contract analysis to **each** slice. Add security, database, performance, UI or concurrency passes based on touched surfaces.
- **Multiple agent reviewers**: when genuinely separate scoped agent executions exist, their findings may be cross-checked and consolidated. If parallel reviewers are unavailable, use sequential passes and mark them as **one AI reviewer**, never fabricate independently completed agents.
- **Risk-tiered closure**: low-risk docs may receive an AI-assisted technical clearance; higher-risk changes need the project's own sign off rules and, where required, an independently authorized reviewer or human before production use.

Treat thresholds as heuristics, not permission to ignore risk. A small authentication patch can require deep review.
