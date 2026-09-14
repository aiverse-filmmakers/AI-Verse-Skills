# Experience Curve for Major Flows

An experience curve describes how a meaningful multi-stage interface should feel or behave from one stage to the next.

It adapts Scroll Craft's feeling-curve method beyond landing pages while avoiding emotional ceremony in ordinary application work.

## Use It For

Use an experience curve when the flow has a meaningful progression, for example:

- onboarding;
- first-run setup;
- a major agent workflow;
- a launch or narrative marketing experience;
- an immersive product story;
- a high-stakes multi-step creation flow;
- a guided migration or import;
- a complex wizard where confidence and clarity need to build over stages.

## Do Not Use It For

Do not create an experience curve for:

- a settings page;
- CRUD forms;
- ordinary tables;
- a standard modal;
- simple search/filtering;
- a small component;
- routine dashboard inspection;
- a micro change.

The method must reduce design ambiguity, not add documentation overhead.

## The Curve

Write one line per meaningful stage:

```text
Stage | Intended state | What in the interface causes it
```

The intended state may be emotional or operational.

Examples:

- orientation;
- recognition;
- confidence;
- clarity;
- control;
- anticipation;
- relief;
- trust;
- readiness;
- completion.

For operational software, prefer states such as clarity, control, confidence and readiness over manipulative emotional language.

## Cause Before Decoration

The cause must be an interface decision, not a vague aspiration.

Good:

- Confidence | preflight shows exactly which integrations are healthy before launch
- Control | preview exposes the generated plan and lets the user edit each step
- Relief | failed imports remain recoverable with a clear retry path
- Readiness | final review summarizes permissions, cost and expected side effects

Weak:

- Excitement | cool animation
- Delight | gradient
- Premium | glass cards

The state chooses the interaction. The animation library does not choose the state.

## Adjacent-State Rule

If two adjacent stages are supposed to create the same state, inspect whether one stage is filler or whether the stages should be merged.

This is a review signal, not an automatic deletion rule.

Repeated "clarity" can be valid in a technical workflow when each stage resolves a different uncertainty.

The agent must explain why repetition is necessary rather than mechanically deleting useful product steps.

## Peak / Critical Moment

For an experience-led flow, identify the one critical moment that deserves the strongest emphasis.

Depending on the product, it may be:

- the first successful result;
- the moment a transformation becomes visible;
- an important approval;
- a live preview becoming interactive;
- a successful connection;
- a meaningful reveal in a narrative experience.

Do not manufacture a dramatic peak in routine enterprise/CRUD work.

In utility software, the "critical moment" may simply be the point where uncertainty becomes confidence.

## Contrast Before the Critical Moment

A strong major flow should not give every stage equal visual weight.

Use contrast intentionally:

- quieter setup before a major reveal;
- denser evidence before a concise decision;
- progressive simplification as the user approaches completion;
- increased direct manipulation when control becomes the goal.

Do not use visual noise merely to make the peak look louder.

## Resolution

The final state must feel complete.

Verify:

- the user knows what happened;
- the user knows whether it succeeded;
- the next available action is clear;
- unresolved problems remain visible;
- there is no dead-end final screen;
- success does not hide partial failures.

## Intended vs Felt Review

After implementation, compare the intended curve against the rendered flow.

For each meaningful stage ask:

1. What state was intended?
2. What does the actual screen/interaction communicate?
3. Where do they diverge?
4. Is the divergence caused by hierarchy, copy, pacing, interaction, missing feedback or visual noise?
5. What was changed to close the gap?

Do not rewrite the intended curve after the fact merely to match an accidental implementation.

If product direction intentionally changes, update the curve explicitly.

## Relationship to DESIGN.md

Do not persist every temporary flow curve into `DESIGN.md`.

Persist only durable product-wide principles, for example:

- onboarding becomes progressively more direct;
- destructive actions intentionally create friction;
- successful agent runs resolve into a calm summary state;
- the product moves from explanation to direct manipulation as confidence increases.

A one-off launch page curve belongs with that project/brief, not the global product system.

## Relationship to Signature Interaction

A signature interaction may live at the critical moment, but it does not have to.

If the signature interaction and the critical moment are unrelated, confirm that both are necessary.

Do not add a signature move merely to decorate the peak.

## Accessibility and Reduced Motion

The experience curve must survive:

- keyboard use;
- screen readers;
- reduced motion;
- slow networks;
- loading/error paths;
- mobile layout.

The intended state cannot depend exclusively on animation.

## Source Note

Conceptual inspiration was verified from Scroll Craft's feeling-curve methodology at `nateherkai/scroll-craft@0b816225945e45380397d6a0487efa3c98916858`.

AI-Verse generalizes it to major product flows and adds explicit utility-software exclusions, operational states, error/recovery resolution and accessibility requirements.
