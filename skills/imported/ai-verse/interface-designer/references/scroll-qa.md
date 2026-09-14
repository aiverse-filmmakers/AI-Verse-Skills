# Scroll-State Visual QA

Use this gate only when scrolling is a primary interaction, storytelling mechanism, or state driver.

Do not apply this harness to ordinary application pages that simply happen to scroll.

## When to Run

Run for:

- `SCROLL_IMMERSIVE`;
- scrollytelling;
- scroll-scrubbed media;
- scroll-driven state machines;
- continuous spatial journeys;
- pinned narrative sequences;
- reference recreations where scroll progression is a defining behavior.

For ordinary dashboards, settings, feeds, forms and documentation pages, use the simpler state-based visual QA contract instead.

## Sampling Strategy

Inspect:

1. the initial/top state;
2. every semantic transition or authored waypoint;
3. the midpoint of long continuous transitions when behavior changes gradually;
4. the final/bottom state;
5. representative intermediate positions where backgrounds, text or media cross.

Do not rely on only the top and bottom screenshots.

Fixed percentage samples such as 25/50/75% are useful fallbacks, not substitutes for semantic transition sampling.

## Required Checks

### Progression

Verify:

- scroll input actually advances the intended state;
- progress is monotonic unless an intentional reversible interaction says otherwise;
- pinned states release correctly;
- scrubbed media reaches intended frames/states;
- state does not freeze after resize or navigation;
- progress indicators match the actual position.

### Dead Scroll

Flag unintentional regions where substantial scroll input produces no visible or meaningful change.

An authored pause can be valid when it is intentional and documented.

A blank or apparently broken pause is not.

### Visibility

Verify:

- major content becomes visible when intended;
- content does not disappear before it can be read;
- pinned/fixed layers do not permanently cover later content;
- ending content remains visible long enough to resolve;
- final state is not blank or half-transitioned.

### Background and Legibility

At each meaningful background/material transition verify:

- text remains legible;
- contrast remains sufficient;
- overlays/scrims arrive at the correct time;
- transparent surfaces do not become unreadable;
- fixed chrome remains coherent across backgrounds.

### Media / State Synchronization

Verify:

- video/frame progression matches scroll progression;
- captions/copy match the current visual state;
- counters/labels/waypoint indicators update at the correct moment;
- no obvious state jumps, stale frames or backwards transitions exist.

### Reduced Motion

Reduced-motion mode must be complete.

It must not:

- hide information that only appears through motion;
- leave content at opacity 0;
- leave the page stuck in a pinned state;
- require a scrubbed video frame to understand the argument;
- create giant empty scroll spans after motion is removed.

### Mobile

A scroll experience must be intentionally authored on mobile.

Phase 8.3 defines the stronger mobile-art-direction gate.

For scroll QA verify at minimum that mobile:

- progresses;
- remains readable;
- has no impossible hover/pointer dependency;
- does not trap scroll;
- does not depend on desktop-only viewport geometry.

## Evidence

For each semantic checkpoint record:

```text
Checkpoint:
Scroll position / waypoint:
Viewport:
Rendered evidence:
Expected state:
Observed state:
Result:
Finding/fix:
```

Use rendered browser/device evidence.

DOM/source inspection alone is not scroll-state evidence.

## Tooling

Use the simplest trustworthy verification mechanism available.

Allowed examples:

- Playwright browser screenshots at explicit scroll positions;
- live browser inspection;
- project-native visual test harness;
- Scroll Craft's own verifier when Scroll Craft is the selected specialist.

Do not install or force Scroll Craft infrastructure merely to test an ordinary site.

## Completion Rule

A scroll-driven experience is not complete until:

- semantic transitions were sampled;
- no unexplained dead scroll remains;
- major content reaches intended visibility;
- background changes preserve legibility;
- scroll-driven media/state actually advances;
- reduced-motion mode is complete;
- mobile progression is intentionally verified or explicitly blocked.
