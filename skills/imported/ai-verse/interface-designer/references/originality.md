# Design Fingerprint Gate

This gate prevents accidental template convergence without forcing arbitrary novelty.

It adapts the useful structural-uniqueness idea verified from Scroll Craft at `nateherkai/scroll-craft@0b816225945e45380397d6a0487efa3c98916858`, but broadens it from scroll landing pages to product interfaces, apps, dashboards, websites and design systems.

## Scope

Run the gate when the task establishes a new substantial visual direction, including:

- a new product;
- a substantial redesign;
- a new full screen or flow that establishes reusable visual grammar;
- a new marketing/experience direction;
- a reference-inspired build where the user asked for the feel rather than an exact copy.

Do not run it as a novelty requirement for:

- `MICRO_CHANGE`;
- ordinary maintenance inside an established `DESIGN.md`;
- exact reference recreation;
- platform-required UI conventions;
- accessibility-required behavior;
- a user instruction that intentionally preserves an existing product system.

## Fingerprint Dimensions

Record these 10 dimensions:

1. **information architecture**: how information is grouped and ordered;
2. **navigation model**: sidebar, tabs, command surface, chapter rail, bottom navigation, etc.;
3. **layout grammar**: shell, split stage, editorial spread, dense grid, free canvas, continuous world, etc.;
4. **density**: sparse, editorial, utility-dense, monitoring-dense, immersive, etc.;
5. **typography hierarchy**: scale contrast, family roles, label/display relationship, measure and rhythm;
6. **surface/material treatment**: flat, bordered, tonal, glass, paper, metal, canvas, photographic, etc.;
7. **interaction model**: forms, direct manipulation, command-driven, canvas manipulation, progressive disclosure, etc.;
8. **motion language**: static, spring/direct manipulation, cinematic, hard-cut, reveal-led, scroll-driven, etc.;
9. **primary composition**: the dominant composition a user remembers;
10. **signature element**: one distinctive recurring element or interaction when one intentionally exists.

The first four dimensions are not visual decoration. They define what the product is structurally.

## Fingerprint Record

A fingerprint should describe decisions, not marketing adjectives.

Good:

- navigation_model: persistent left tool rail with command search as the secondary path
- layout_grammar: single working canvas with contextual inspector
- density: dense operational surface with compact labels
- primary_composition: live run graph occupying the central canvas

Weak:

- modern
- premium
- sleek
- blue
- Apple-like

## Comparison Boundary

Compare only against fingerprints that are legitimately available inside the current authorized workspace or product context.

Allowed sources:

- the current project's `DESIGN.md`;
- prior accepted fingerprints stored in the same authorized workspace;
- explicit references supplied by the current user;
- project-owned design archives the current task is allowed to read.

Do not create a shared cross-member fingerprint registry.

Do not use another member's private product design as a novelty constraint.

## Reskin Detection

A proposal is a likely reskin when it preserves nearly the same product structure and changes mostly palette, imagery, copy or surface decoration.

Treat these as the structural dimensions:

- information architecture;
- navigation model;
- layout grammar;
- interaction model;
- primary composition;
- signature element.

If 5 or more of those 6 structural dimensions materially match a prior unrelated design, the proposal requires an explicit structural justification.

Changing only:

- color;
- font;
- image style;
- card radius;
- shadow;
- decorative motion;

does not clear the gate.

## High-Similarity Review

If 8 or more of the 10 total dimensions materially match a prior unrelated design, classify the proposal as HIGH_SIMILARITY.

For HIGH_SIMILARITY:

1. determine whether the similarity is required by reference fidelity, an existing `DESIGN.md`, platform convention, accessibility, or explicit user intent;
2. if required, record the reason and proceed;
3. if not required, revise at least one meaningful structural dimension before implementation;
4. do not solve the failure with arbitrary ornament.

The goal is not to maximize differences. The goal is to prove the structure was chosen rather than inherited from habit.

## Exact Reference Rule

For exact recreations, fidelity outranks originality.

Do not distort a requested reference merely to clear the fingerprint gate.

Still record the fingerprint when useful so later unrelated products do not accidentally reuse the same structure.

## Established Product Rule

For an established product with an accepted `DESIGN.md`, consistency outranks cross-product novelty.

A new feature should usually match the product fingerprint.

Only run a divergence decision when the task is actually a redesign or design-system change.

## Design-System Persistence

When a new fingerprint becomes an accepted reusable product direction, record it in `DESIGN.md` under a concise `Design Fingerprint` section.

Do not add a fingerprint section for temporary rejected prototypes.

## Verification Questions

Before implementation of a new substantial direction, answer:

- What is structurally different from prior unrelated work?
- Which similarities are intentional constraints?
- Is the navigation model actually chosen?
- Is the layout grammar actually chosen?
- Is the primary composition memorable without naming the palette?
- Would the product still feel materially different in grayscale?
- If the signature element were removed, would the structure still be intentional?

A design that only becomes "different" when color is visible has probably not cleared the structural gate.

## Source Note

Structural inspiration was verified from Scroll Craft's uniqueness/fingerprint methodology. AI-Verse changes the dimensions, comparison boundary and pass logic so the method applies safely to general product UI rather than imposing a landing-page grammar on applications.
