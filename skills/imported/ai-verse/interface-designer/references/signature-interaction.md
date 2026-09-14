# Signature Interaction Rule

A signature interaction is one memorable, intentional behavior that belongs to the product or experience rather than to a generic component library.

This rule adapts Scroll Craft's bespoke signature-move concept for general interface design.

## When to Require One

Require a signature interaction only when the product is primarily an experience or expression surface and distinctiveness is part of the brief, for example:

- brand or campaign websites;
- launch pages;
- immersive product stories;
- portfolio/editorial experiences;
- scroll-driven experiences;
- experiential landing pages;
- interactive showcases.

Even in those contexts, an exact-reference brief may already define the signature behavior. Do not invent a competing one.

## When It Is Optional

Treat a signature interaction as optional and functional for:

- dashboards;
- admin tools;
- settings;
- CRUD applications;
- productivity software;
- monitoring surfaces;
- chat interfaces;
- forms and checkout;
- dense operational tools.

For these products, a clear workflow beats novelty.

Do not add an interaction merely so the fingerprint has a distinctive row.

## What Counts

A valid signature interaction:

1. is meaningful to the product or story;
2. changes the experience in a way users can describe;
3. is not a parameter tweak to an existing generic effect;
4. is implemented in the product, not only described in prose;
5. has an accessible and reduced-motion-safe equivalent when necessary;
6. does not obstruct the primary task;
7. remains understandable without requiring hidden gestures.

Examples:

- a live canvas where the central object visibly changes as the user adjusts the core product variable;
- a timeline that accumulates evidence as the visitor moves through a product story;
- a comparison divider that physically resolves the product's before/after argument;
- a workspace object that can be directly manipulated in a way central to the tool;
- a persistent spatial model that becomes the navigation for an immersive story.

## What Does Not Count

Do not call these signature interactions by themselves:

- a different hover color;
- a stronger shadow;
- a larger spring;
- changing easing values;
- a generic parallax layer;
- a standard carousel;
- a standard command palette;
- a standard drawer or sheet;
- adding more cards;
- recoloring an existing effect;
- a library component with a project-specific class name;
- animation that exists only to look busy.

## Utility Application Test

For dashboards and utility applications, ask:

- Does this behavior reduce cognitive load?
- Does it expose system state more clearly?
- Does it make a frequent action faster?
- Does it help direct manipulation?
- Would users miss the function if the effect disappeared?

If the answer is no, omit it.

## Experience Test

For marketing and experiential work, ask:

- Can a user describe the interaction without mentioning its implementation library?
- Does it reinforce the product's message or world?
- Is it different from the default devices already used elsewhere in the experience?
- Is it strong enough to be one of the things a user remembers?
- Does it remain coherent on mobile and with reduced motion?

If not, revise or omit it.

## Design Fingerprint Integration

When a signature interaction intentionally exists:

- record it in the fingerprint's `signature_element` dimension;
- if it becomes reusable product grammar, persist it in `DESIGN.md`;
- if it is one-off campaign behavior, do not promote it to a global product rule.

A missing signature interaction must not fail a dashboard, admin tool or ordinary application.

## Accessibility and Control

A signature interaction must not:

- hide critical content behind pointer-only behavior;
- require precision gestures without alternatives;
- block keyboard navigation;
- cause unavoidable motion;
- break reduced-motion mode;
- trap scroll or focus;
- replace a conventional control when the conventional control is necessary for clarity.

## Source Note

Conceptual inspiration was verified from Scroll Craft's signature-move rule at `nateherkai/scroll-craft@0b816225945e45380397d6a0487efa3c98916858`.

AI-Verse changes the requirement boundary so bespoke interaction is not imposed on dashboards or utility software where novelty can damage usability.
