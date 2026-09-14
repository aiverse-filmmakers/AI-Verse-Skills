# State-Based Visual QA

Visual QA verifies the interface users actually experience, not only the source code.

The QA pass is state-based and evidence-based.

## Core Rule

Do not claim a visual state passed unless the runtime actually rendered or inspected that state.

Every requested/applicable state must end as one of:

- `VERIFIED_PASS`
- `VERIFIED_FAIL`
- `NOT_APPLICABLE`
- `UNVERIFIED_BLOCKED`

`UNVERIFIED_BLOCKED` is a truthful outcome. It is not a pass.

## Select Applicable States

Do not mechanically test states the feature does not have.

### Data / Async States

Check when applicable:

- initial;
- loading;
- empty;
- populated;
- error;
- partial data;
- retry/recovery;
- stale/offline if the product supports them.

### Control States

Check when applicable:

- default;
- hover;
- focus-visible;
- active/pressed;
- selected;
- disabled;
- validation error;
- success/confirmed.

### Disclosure / Overlay States

Check when applicable:

- collapsed;
- expanded;
- menu open;
- popover open;
- tooltip;
- dialog open;
- sheet/drawer open;
- nested overlay if the product allows it.

### Navigation States

Check when applicable:

- current location visible;
- active tab/section;
- deep-linked state;
- back/forward behavior;
- destructive confirmation or undo surface.

### Theme / Preference States

Check when applicable:

- light;
- dark;
- high contrast if supported;
- reduced motion;
- text scaling/zoom where relevant.

### Viewport States

Check when the product is responsive:

- desktop;
- tablet;
- mobile.

Phase 8.3 adds the stronger mobile-art-direction gate. This state QA only proves that the applicable viewports were inspected.

## What to Inspect

For each state inspect the parts that matter, including:

- hierarchy;
- clipping/overflow;
- unwanted horizontal scroll;
- overlap;
- readable contrast;
- content truncation;
- empty-space balance;
- broken or missing assets;
- focus visibility;
- disabled-state legibility;
- overlay containment;
- scroll lock;
- safe layering/z-index;
- loading stability/layout shift;
- long-content behavior;
- error recovery clarity;
- touch target plausibility where visible;
- visual consistency with the current DESIGN.md;
- reference fidelity when a reference is part of the task.

## Evidence Record

For each checked state record:

```text
State:
Viewport:
Theme/preference:
Evidence:
Result:
Finding:
Fix:
Reverified:
```

Evidence may be:

- browser screenshot;
- rendered frame;
- live preview inspection;
- device/simulator capture;
- explicit automated visual artifact;
- other direct rendered evidence.

Source inspection alone does not prove visual appearance.

## Fix Loop

For every `VERIFIED_FAIL`:

1. state the visible defect;
2. make the smallest relevant fix;
3. render the affected state again;
4. record the new result;
5. rerun neighboring states when the fix can affect shared layout or tokens.

Do not mark the whole feature verified because one screenshot looks correct.

## Existing DESIGN.md

If the project has a `DESIGN.md`, use it as the visual consistency authority.

Do not treat a deliberate product-specific exception as a generic QA failure.

## Reference Recreation

When recreating a reference:

- compare the same viewport/state when possible;
- inspect hierarchy, geometry, typography, materials and motion state;
- separate unavoidable asset/content differences from implementation errors;
- do not use similarity language as a substitute for rendered comparison.

## Accessibility Relationship

Visual QA does not replace semantic/accessibility testing.

It should still catch visible accessibility failures such as:

- missing focus indication;
- illegible contrast;
- clipped enlarged text;
- reduced-motion mode that still contains major unavoidable motion.

## Completion Rule

A substantial interface is visually complete only when:

- required/applicable states are verified or explicitly blocked;
- failures were fixed and reverified;
- blocked states are reported;
- no unrendered state is silently counted as a pass.

## Output

Keep the final QA report concise:

```text
Visual QA: 12 pass, 1 fixed/reverified, 2 not applicable, 1 blocked
Blocked: iOS safe-area state, no simulator available
```

Never turn a blocked state into a fabricated success.
