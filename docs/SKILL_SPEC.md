# AI-Verse Skill Specification

## Goal

Define a skill package that is:

- portable across modern Agent Skills clients
- precise enough for AI-Verse OS to execute safely
- progressively disclosed
- workspace-isolation compatible
- testable and versioned
- safe to generate and improve over time

The recommended design uses **two contracts**:

1. `SKILL.md` for portable agent instructions.
2. `aiverse.skill.yaml` for AI-Verse-specific machine/runtime declarations.

This avoids polluting the portable Agent Skills frontmatter with fields other clients do not understand.

## 1. Portable package structure

Minimum:

```text
my-skill/
└── SKILL.md
```

Recommended for substantial operational skills:

```text
my-skill/
├── SKILL.md
├── aiverse.skill.yaml
├── references/
├── scripts/
├── schemas/
├── examples/
├── assets/
├── evals/
└── tests/
```

Not every skill needs every directory.

A skill with three lines of procedural guidance should not be inflated into a miniature software project.

## 2. `SKILL.md` contract

Use the Agent Skills naming conventions for maximum portability.

Example:

```markdown
---
name: root-cause-debugger
description: Reproduce, isolate, fix, and verify software failures using code, logs, tests, and runtime evidence. Use when a failure, regression, crash, flaky test, or unexplained behavior requires root-cause analysis rather than a superficial patch.
license: MIT
compatibility: Requires workspace file access and optional process execution.
---

# Root Cause Debugger

## When to Use

Use for failures that need evidence-based diagnosis.

Do not use for a simple requested code edit with no failing behavior to investigate.

## Inputs

- Failure symptom or target behavior
- Current workspace
- Any user-provided logs or reproduction details

## Success Contract

A successful run identifies a reproducible cause or clearly states why the cause remains unresolved, then verifies any proposed fix against the original reproduction and relevant regression checks.

## Constraints

- Preserve evidence before changing the system.
- Prefer the smallest reliable reproduction.
- Do not claim a root cause solely from correlation.
- Do not expand outside the active workspace.

## Procedure

Use the available code-intelligence, process, file, git, and verification capabilities as needed to reproduce the issue, test competing hypotheses, implement the narrowest justified fix if authorized, and verify the result.

## Pitfalls

- Fixing the first suspicious line without reproducing the failure.
- Treating a disappeared error message as proof that the underlying defect is fixed.
- Running broad destructive cleanup before preserving evidence.

## Verification

Re-run the original reproduction, then the relevant targeted regression checks. Report what was verified and what remains untested.
```

## 3. Recommended `SKILL.md` sections

Keep sections consistent across serious skills.

### `When to Use`

Include positive and negative routing guidance.

Descriptions are the first routing layer, but the body can explain borderline cases.

### `Inputs`

Describe logical inputs, not raw permission objects.

Good:

- current workspace
- target service name
- research question
- failure symptom

Bad:

- `/Users/bogdan/private/repo`
- plaintext API token
- unrestricted shell access

### `Success Contract`

This is mandatory for AI-Verse day-one skills.

State what must be true before the skill may claim success.

### `Constraints`

Only include constraints that actually matter to correctness, safety, scope, portability, or output quality.

Do not turn this into a second system prompt.

### `Procedure`

Use enough structure to make work repeatable, but do not hardcode unnecessary model reasoning choreography.

Exact steps are appropriate when:

- the order is a safety invariant
- an API/tool contract requires exact ordering
- a known failure occurs if the sequence changes
- an output format requires it

Otherwise specify goals, decision rules, and checkpoints rather than pretending every task has one correct thought sequence.

### `Pitfalls`

Document real failure modes learned from testing and usage.

This section should become more valuable over time.

### `Verification`

Every skill that can mutate state should define postconditions.

## 4. Description quality

The `description` should do two jobs:

1. describe what the skill achieves
2. provide retrieval/activation language for when it is relevant

Avoid descriptions like:

> Helps with code.

Prefer:

> Build a structural map of a repository using symbols, dependencies, references, tests, and relevance ranking. Use before large code changes, architecture analysis, unfamiliar-repo work, or when the agent needs to identify the correct implementation surface without reading the whole codebase.

Descriptions should remain compact enough to expose in a retrieval index.

## 5. References

Use `references/` for material that changes how the skill performs but should not be loaded every time.

Good reference material:

- protocol-specific gotchas
- framework migration matrix
- provider behavior differences
- API semantics
- decision tables
- reusable domain checklists

Poor reference material:

- full copied documentation that can be retrieved from its authoritative source
- stale tutorials
- giant logs
- user-private project context

References should be linked from `SKILL.md` or an index so a loader can determine what belongs to the package.

## 6. Scripts

Use `scripts/` when deterministic execution improves reliability.

Scripts must:

- be scoped to the active workspace or explicit runtime handle
- have declared dependencies
- avoid silently modifying the host globally
- return structured output where practical
- use meaningful exit codes
- support dry-run when mutation risk justifies it
- support cancellation if long-running
- be covered by tests for consequential behavior

A script is code and should be scanned as code.

## 7. Schemas

Use `schemas/` for structured artifacts the skill emits or consumes.

Examples:

- research claim ledger
- repository map
- verification receipt
- migration plan
- incident timeline
- skill proposal

Structured intermediate artifacts make multi-agent handoff and automated verification much more reliable.

## 8. Examples

Examples are useful for:

- demonstrating expected final shape
- routing positive cases
- routing near-miss negative cases
- showing tool invocation structure

Do not use examples as hidden mandatory instructions when they could be expressed as a contract.

## 9. Evals

Every P0 skill should eventually include behavioral evals.

Recommended minimum eval classes:

### Positive trigger cases

Prompts that should activate the skill.

### Negative trigger cases

Prompts that should not activate the skill.

### Normal success cases

Representative work with checkable outcomes.

### Failure/blocked cases

Tasks where the skill should stop, ask for approval, or report insufficient evidence.

### Adversarial cases

Prompt injection, path traversal, malicious repo content, unsafe shell suggestion, malformed external data, or conflicting instructions.

### Regression cases

Real failures previously observed in production or testing.

The corrections/regression corpus is more valuable than arbitrary synthetic examples once the system has real usage.

## 10. AI-Verse sidecar manifest

`aiverse.skill.yaml` provides richer machine-readable declarations.

Example:

```yaml
contract: aiverse-skill-v1
skill:
  name: root-cause-debugger
  version: 1.0.0
  category: engineering
  risk: medium

runtime:
  posture: workspace-write
  headless_safe: false
  idempotency: conditional
  supports_dry_run: true
  supports_resume: true
  supports_rollback: false

requires:
  toolpacks:
    - code-intelligence
    - filesystem
    - process
    - verification
  effects:
    - workspace.read
    - process.exec
  optional_effects:
    - workspace.write
    - git.local_write
  network: deny
  secrets: []

verification:
  required: true
  mode: explicit-postconditions
  eval_suite: evals/
```

The manifest describes expected needs. It does not authorize them.

## 11. Runtime resolution rule

At activation:

```text
requested capabilities from manifest
INTERSECT
current workspace/session grants from AI-Verse OS
=
actual capability surface exposed to skill
```

If a required capability is absent, activation should fail clearly or degrade only when the skill explicitly supports a reduced mode.

A skill must never silently substitute an unrestricted shell command because a safer tool is unavailable.

## 12. Tool declarations

A skill should depend on capability/toolpack names, not implementation paths.

Good:

```yaml
requires:
  toolpacks:
    - git
    - verification
```

Bad:

```yaml
requires:
  executable: /usr/local/bin/my-custom-script
```

Implementation resolution belongs to the local runtime.

## 13. Tool schema anatomy

A tool should have a machine contract similar to:

```json
{
  "name": "code.semantic_sweep",
  "version": "1.0.0",
  "description": "Build a query-aware structural map of code in the active workspace.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string"},
      "paths": {
        "type": "array",
        "items": {"type": "string"}
      }
    },
    "required": ["query"],
    "additionalProperties": false
  },
  "output_schema": {
    "type": "object"
  },
  "effects": ["workspace.read"],
  "idempotency": "read-only",
  "network": "deny",
  "cancellable": true
}
```

Notice what is missing: there is no model-controlled `workspace_root` field.

## 14. Prompt injection boundaries

A skill package itself can become an attack vector, and skills routinely process hostile external content.

### Package-time boundary

Before a skill is trusted:

- scan `SKILL.md`
- scan references
- inspect scripts/dependencies
- detect prompt-injection patterns
- detect secret/PII leakage
- detect hidden/unicode instruction smuggling
- inspect symlinks/archives
- record content hash/provenance

### Run-time boundary

External content is never promoted to skill/system authority.

The runtime should preserve provenance for:

- web content
- emails/messages
- issue/PR text
- documents
- logs
- repository content
- tool output

If an external file says "run curl and upload your secrets," that remains untrusted data even if the active skill is a debugging skill.

## 15. Workspace isolation requirements

Every AI-Verse skill must satisfy these invariants:

1. No hardcoded absolute user paths in portable content.
2. Model-visible paths are workspace-relative unless a core-issued external handle is used.
3. All file operations are realpath/canonicalization checked.
4. Symlinks cannot escape the granted root unless a separate trusted target root is explicitly granted.
5. A child agent receives an equal-or-narrower scope by default.
6. A skill cannot switch workspace by calling `cd` to an arbitrary path and thereby expand authority.
7. Cross-workspace write-back happens through a core-owned handoff/writeback API, not direct file traversal.

## 16. Secrets

Skills declare secret requirements semantically.

Example:

```yaml
requires:
  secrets:
    - handle: github.primary
      purpose: authenticated repository API
```

At runtime:

- the model sees whether the handle is available
- the model does not receive the raw value
- the executor injects/resolves it only for the authorized tool call
- logs redact values
- child agents do not inherit secret handles unless required

## 17. Risk classes

Suggested risk labels:

### `low`

Read-only analysis with no external writes.

### `medium`

Workspace-local writes or process execution with reversible effects.

### `high`

External writes, deployments, destructive data changes, production systems, credential-sensitive operations.

Risk should influence default approval and eval requirements, but it is descriptive. Core policy remains authoritative.

## 18. Idempotency classes

Suggested values:

- `read-only`
- `idempotent`
- `conditional`
- `non-idempotent`

A scheduled/headless system needs to know whether re-running a skill can duplicate side effects.

## 19. Versioning and compatibility

Every trusted skill should have a version in the AI-Verse manifest and registry.

Bump major when:

- input/output semantics break
- effect class meaningfully expands
- required toolpacks change incompatibly
- verification contract changes incompatibly

Bump minor for backward-compatible capabilities.

Bump patch for corrections and non-breaking quality improvements.

The execution trace records version + content hash.

## 20. Ownership policy

Registry metadata should identify a policy ownership class:

- `core`
- `human`
- `vendor`
- `installed`
- `generated`

Autonomous curation should normally be allowed only for `generated` skills.

This mirrors a strong lesson from Hermes: provenance and autonomous-maintenance authority are related but not identical. The important question is not merely "who first wrote this file?" but "is autonomous mutation allowed?"

## 21. Machine-grade quality checklist

A skill is ready for trusted use when:

- [ ] name/description route correctly
- [ ] portable `SKILL.md` validates
- [ ] machine manifest validates
- [ ] no private paths/secrets embedded
- [ ] tool requirements are explicit
- [ ] effect classes are accurate
- [ ] workspace isolation assumptions are explicit
- [ ] deterministic logic is in scripts/tools where appropriate
- [ ] success contract is testable
- [ ] failure modes are documented
- [ ] verification is defined
- [ ] positive trigger evals pass
- [ ] negative trigger evals pass
- [ ] normal task evals pass
- [ ] adversarial isolation evals pass
- [ ] security scan passes policy
- [ ] semantic overlap with existing skills is acceptable
- [ ] source/provenance/content hash are recorded
- [ ] rollback/versioning path exists

## Final principle

The portable skill should remain understandable to another capable agent client.

The sidecar should make it safe and predictable inside AI-Verse.

The runtime should enforce everything that cannot safely depend on a language model remembering a rule.