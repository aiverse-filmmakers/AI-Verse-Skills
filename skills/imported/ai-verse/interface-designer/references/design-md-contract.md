# Project DESIGN.md Persistence Contract

This contract defines when AI-Verse Interface Designer should create, read, update, and preserve a project-local `DESIGN.md`.

The structure is compatible with the project-level design-system pattern verified from `google-labs-code/design.md@9bf8eae67128b6cc55ad9bf86665767deb4c11cd`, but AI-Verse does not require Google's CLI or services.

## Purpose

`DESIGN.md` is persistent visual product memory.

It records stable design decisions that future agents and humans should honor across substantial design work.

It is not:

- a substitute for source code;
- a changelog;
- a task scratchpad;
- a place for temporary experiments;
- a reason to redesign a product on every edit.

## Read Rule

If a project-level `DESIGN.md` exists, read it before any substantial interface change.

Substantial means any work that can materially affect:

- product visual direction;
- typography;
- palette or token roles;
- navigation or layout grammar;
- component visual language;
- responsive behavior;
- interaction language;
- motion language;
- accessibility design constraints;
- a product-wide signature interaction.

A `MICRO_CHANGE` may read only the relevant local section when that is enough, but it must not contradict the file.

## Create Rule

Create `DESIGN.md` when all of the following are true:

1. the product does not already have one;
2. the current task establishes reusable visual or interaction decisions;
3. those decisions should survive beyond the current task.

Typical creation scopes:

- `SCREEN` when it establishes a reusable product direction;
- `MULTI_SCREEN_FLOW`;
- `FULL_PRODUCT`;
- `DESIGN_SYSTEM_CHANGE`;
- `REFERENCE_RECREATION` when the reference becomes the persistent product direction;
- `SCROLL_IMMERSIVE` when the visual grammar should persist.

Do not create it for:

- a one-off spacing fix;
- a copy edit;
- a single bug fix;
- a temporary prototype that is not selected;
- an isolated experiment the user did not adopt.

## Update Rule

Update an existing `DESIGN.md` only when the accepted product grammar changed.

A source-code change does not automatically require a DESIGN.md change.

When updating:

1. preserve unrelated existing decisions;
2. modify the smallest relevant section;
3. keep established token names stable unless the design-system change intentionally renames them;
4. distinguish a deliberate exception from a new global rule;
5. do not silently erase constraints because a new expert prefers a different aesthetic.

## Authority

When recommendations conflict, apply:

1. current explicit user instruction;
2. repository/product authority;
3. current accepted `DESIGN.md`;
4. chosen reference-fidelity boundary;
5. runtime/platform correctness;
6. specialist guidance;
7. general visual taste.

A specialist may propose changing DESIGN.md, but the change becomes authoritative only after the product direction is intentionally accepted.

## Minimum Persistent Sections

A substantial `DESIGN.md` should preserve the sections that are actually relevant to the product.

Recommended minimum:

- Brand & Product Principles
- Color Roles / Tokens
- Typography
- Layout & Spacing
- Radii, Elevation & Surfaces
- Navigation / Information Architecture Grammar
- Components & Reusable UI Rules
- Interaction Language
- Motion Language
- Responsive & Mobile Direction
- Accessibility Requirements
- Signature Interaction, when one exists
- Forbidden Patterns / Product-Specific Anti-Patterns

Do not add empty sections merely to satisfy a template.

## Structured Frontmatter

For products that benefit from machine-readable tokens, use YAML frontmatter at the top of `DESIGN.md`.

Common optional keys:

```yaml
---
name: Product Design System
colors:
  background: "#..."
  surface: "#..."
  on-surface: "#..."
  primary: "#..."
  on-primary: "#..."
typography:
  headline-lg:
    fontFamily: Example
    fontSize: 40px
    fontWeight: "700"
    lineHeight: 44px
spacing:
  unit: 8px
  page-gutter: 24px
rounded:
  sm: 0.25rem
  md: 0.75rem
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
---
```

Only include structured fields the product actually uses.

Do not invent tokens unsupported by the implementation.

## Stable Narrative Sections

The narrative body should explain the design logic behind the tokens.

### Brand & Product Principles

Record the intended personality, product feel, hierarchy, density and visual philosophy.

### Color Roles / Tokens

Describe semantic roles, not only raw hex values.

### Typography

Record family, hierarchy, scale, weight, tracking and leading rules that matter.

### Layout & Spacing

Record grid, gutter, container, rhythm and density decisions.

### Radii, Elevation & Surfaces

Record material treatment, borders, shadows, glass, depth and surface hierarchy.

### Navigation / Information Architecture Grammar

Record stable navigation patterns, shell structure and major layout grammar.

### Components & Reusable UI Rules

Record reusable component behavior only when it is product-wide.

### Interaction Language

Record interaction principles such as direct manipulation, selection behavior, disclosure, gestures, sheets, drawers and focus behavior.

### Motion Language

Record duration families, easing/physics, continuity rules and reduced-motion expectations.

### Responsive & Mobile Direction

Record intentional mobile hierarchy, navigation changes, touch behavior, crop/order differences, safe areas and breakpoint philosophy.

Do not define mobile as "desktop but smaller."

### Accessibility Requirements

Record product-specific accessibility requirements that must persist, including contrast, focus, keyboard, reduced-motion, media alternatives or input constraints.

### Signature Interaction

Record one only when it is an intentional recurring product/experience behavior.

Do not manufacture a signature interaction for CRUD/admin utility screens.

### Forbidden Patterns

Record repeated failures the product should not regress into, for example:

- no generic 3-column SaaS hero;
- no gradient text;
- no floating glass cards;
- no hidden mobile navigation;
- no motion without reduced-motion behavior.

Forbidden patterns must be product-specific and evidence-based, not universal stylistic dogma.

## Reference Recreation

If the project direction is derived from a reference:

- record what was adopted;
- record what was intentionally changed;
- do not claim ownership of reference branding or assets;
- avoid copying protected assets unless the user has the right to do so;
- preserve the exact-vs-inspired boundary.

## Verification

Before calling a DESIGN.md update complete:

- confirm the file still matches the actual accepted implementation;
- ensure new global rules are represented in code or in an explicitly accepted design direction;
- ensure removed rules are truly obsolete;
- ensure mobile/accessibility/motion decisions are not contradicted by the implementation;
- ensure no unrelated product decisions were overwritten.

## Source Note

Structural inspiration was verified against:

- repository: `google-labs-code/design.md`
- commit: `9bf8eae67128b6cc55ad9bf86665767deb4c11cd`
- license: Apache-2.0

AI-Verse adds its own create/read/update authority, scope gating, mobile/accessibility requirements, conflict precedence and anti-ceremony rules.
