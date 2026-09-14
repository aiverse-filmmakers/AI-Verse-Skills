# Mobile Art-Direction Gate

A substantial interface is not complete merely because desktop CSS fits inside a smaller viewport.

Mobile must be intentionally authored.

## When to Run

Run for substantial interfaces that have or are expected to have a mobile surface:

- full products;
- multi-screen flows;
- major screens;
- responsive web apps;
- PWAs;
- mobile web experiences;
- React Native / Expo work;
- immersive or reference-recreated experiences that must work on mobile.

For a desktop-only product, mark mobile as `NOT_APPLICABLE` with the product constraint.

For a task that cannot render mobile in the current runtime, mark it `UNVERIFIED_BLOCKED`, not passed.

## 1. Information Hierarchy

Verify which information remains primary on mobile.

Ask:

- What must be visible first?
- What moves below the fold?
- What becomes progressive disclosure?
- What can be summarized?
- What must never be hidden?
- Does the content order still match task priority?

A one-column collapse that preserves desktop order without thought is not automatically acceptable.

## 2. Navigation

Verify mobile navigation is intentional.

Possible outcomes include:

- persistent bottom navigation;
- compact top navigation;
- drawer/sheet;
- command/search-first;
- contextual back path;
- deliberately unchanged navigation when it still fits and remains usable.

Do not hide core navigation solely to make the header look cleaner.

## 3. Touch and Direct Manipulation

Verify:

- interactive targets satisfy the target platform/accessibility minimums;
- adjacent controls are not too easy to hit accidentally;
- drag/swipe behavior has a tap/keyboard alternative when appropriate;
- hover-only actions gain a touch path;
- reorder/direct-manipulation handles remain discoverable;
- edge gestures do not fight system navigation.

Do not invent a hardcoded universal pixel minimum when the target platform has its own governing rule. Apply the correct target-specific guideline.

## 4. Layout, Order, and Density

Verify intentional changes where needed:

- column order;
- card grouping;
- table treatment;
- inspector/panel placement;
- sidebars;
- dense toolbars;
- comparison layouts;
- charts;
- long code/log lines.

A desktop table may become a horizontally scrollable table, cards, detail drill-in, or another intentional mobile pattern. Choose based on the task, not a default conversion rule.

## 5. Media, Crop, and Layering

When visual media exists, verify:

- crop/framing;
- subject remains visible;
- text does not cover the key subject;
- foreground/background layers still make sense;
- decorative planes may be removed when they harm clarity;
- cinematic depth is re-authored rather than merely scaled down.

For reference recreation, compare to a mobile reference when one exists. If none exists, author a coherent mobile interpretation rather than guessing that desktop proportions should survive.

## 6. Safe Areas and Browser / Device Chrome

Where applicable verify:

- top/bottom safe-area insets;
- fixed headers/footers;
- bottom navigation;
- sheets/drawers;
- full-screen media;
- virtual keyboard/IME interaction;
- browser address-bar viewport changes;
- landscape if the product supports it.

Critical controls must not sit under notches, home indicators or keyboard overlays.

## 7. Overlays and Focus

Verify:

- dialogs and sheets fit small viewports;
- content remains scrollable inside overlays;
- background scroll is controlled;
- focused inputs remain visible when the keyboard appears;
- close/back controls remain reachable;
- nested overlays do not create impossible escape paths.

## 8. Motion

Mobile motion may differ from desktop.

Verify:

- motion serves the same hierarchy at a smaller scale;
- expensive depth/parallax is reduced when appropriate;
- gesture motion remains interruptible;
- reduced-motion mode remains complete;
- scroll-linked effects do not create jank or scroll traps.

Do not keep desktop motion merely because it technically runs.

## 9. Verification Evidence

Use rendered evidence from:

- mobile browser viewport;
- device emulator/simulator;
- physical device when available;
- React Native / Expo preview;
- screenshots/video of the actual mobile state.

Record:

```text
Mobile target:
Viewport/device:
Hierarchy changes:
Navigation changes:
Interaction changes:
Media/layer changes:
Safe-area/keyboard result:
Reduced-motion result:
Evidence:
Result:
Blocked items:
```

## DESIGN.md Persistence

For substantial products, durable mobile decisions belong in the `Responsive & Mobile Direction` section of `DESIGN.md`.

Persist principles such as:

- mobile prioritizes current task over global telemetry;
- desktop inspector becomes a bottom sheet;
- media crops around the subject instead of scaling proportionally;
- mobile navigation uses bottom tabs while desktop uses a sidebar.

Do not persist one-off bug fixes as global design-system rules.

## Completion Rule

Mobile art direction passes only when:

- hierarchy is intentional;
- navigation is usable and intentional;
- touch interactions have a valid mobile path;
- layout/density changes are coherent;
- media crop/layering is intentional where applicable;
- safe areas/keyboard/overlays are handled where applicable;
- motion and reduced-motion behavior are appropriate;
- rendered mobile evidence exists or blocked verification is reported.
