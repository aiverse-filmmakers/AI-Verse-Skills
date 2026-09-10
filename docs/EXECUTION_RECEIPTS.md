# Execution Receipt and Verification Contract

AI-Verse Skills execution receipt v2 separates four facts that must never be conflated:

1. **Which action was requested?**
2. **Which immutable capability generation executed it?**
3. **What effect is known to have occurred?**
4. **What evidence, if any, supports the objective's verification criteria?**

The contract is `aiverse-execution-receipt-v2` in `schemas/execution-receipt-v2.schema.json`. Receipt v1 remains unchanged for compatibility; consumers that need action/generation binding or Brain verification semantics must require v2.

## Exact execution binding

Every v2 receipt binds to:

- the Brain-compatible action `request_fingerprint`;
- scope, action class, and operation;
- provider `aiverse-skills`;
- a qualified capability ID such as `aiverse-skills:whisper`;
- the immutable Skills `generation_id` pinned for execution;
- the package digest using `aiverse-package-sha256-v1`.

A receipt from another request, capability, package digest, or generation is stale for the current action even if its human-readable summary looks correct.

## Receipt ID is not trace ID

`receipt_id` is the stable execution receipt identity used for replay/action accounting.

`trace_id` is debugging and correlation metadata only. It is explicitly forbidden as a substitute for `receipt_id` or as criterion evidence. A trace proves that events were correlated; it does not prove that an effect occurred or that a success criterion passed.

## Effect certainty

`effect.state` is one of:

- `occurred`
- `not_occurred`
- `uncertain`

The effect also records `source_kind`, `source_ref`, and `independence`.

For a side-effect action to claim receipt status `success`, the effect must be `occurred` and the effect source must be `ai_verse_os`. This makes OS/runtime verification mandatory at the success boundary. Skills cannot self-certify its own external side effect merely because its procedure returned normally.

A partial, failed, blocked, or aborted execution may still report an occurred or uncertain effect. Consumers must therefore inspect effect certainty rather than infer it from the execution status.

Read-only successful actions report `not_occurred` because no side effect is expected.

## Criterion verification

Receipt verification entries address explicit `criterion_id` values. Each verdict uses Brain-compatible states:

- `unverified`
- `passed`
- `failed`
- `insufficient_evidence`
- `not_applicable`

A passed criterion requires evidence. Each evidence item records:

- an evidence reference;
- evidence kind;
- source kind and source reference;
- independence;
- optional claim, timestamps, scope, and integrity metadata.

Strong evidence kinds cannot be self-labelled by the skill runtime. The semantic validator enforces these provenance pairings:

| Evidence kind | Required source |
| --- | --- |
| `measurement` | `ai_verse_os` |
| `canonical_state` | `ai_verse_os` |
| `user_confirmation` | `user` |
| `authoritative_external` | `external_authority` |
| `independent_evaluation` | `independent_evaluator` |

`observation` is deliberately weaker and may come from the skill runtime or OS.

Source kinds also constrain the independence they may claim. A skill runtime cannot label its own observation `independent_model` or `external_authoritative`.

## Brain integration boundary

The receipt does **not** close Brain objectives and does not grant `VERIFIED_EVIDENCE` authority by itself.

A Brain integration must:

1. validate the receipt and exact action/generation binding;
2. translate Skills execution/effect state to Brain action outcome semantics conservatively;
3. derive Brain evidence classes from the receipt's evidence kind and provenance rather than trusting arbitrary labels;
4. map receipt verdicts only to criterion IDs that exist on the target Brain objective;
5. enforce the objective's verification level and evaluator-independence floor;
6. let Brain's `EvaluationService` decide whether the objective becomes `PASSED`, `FAILED`, or `INSUFFICIENT_EVIDENCE`.

Execution `success` therefore means the bounded skill action completed with the required effect accounting. It never means the higher-level objective is verified complete.

## Semantic validator

`installer/execution_receipt_v2.py` performs the rules that are too relational for a JSON schema alone, including:

- exact expected binding checks;
- trace/receipt identity separation;
- successful side-effect OS verification;
- passed-criterion evidence requirements;
- evidence provenance restrictions;
- source/independence consistency;
- fresh-context builder/evaluator separation.

Consumers should validate both the structural schema and these semantic invariants, or implement equivalent fail-closed checks.
