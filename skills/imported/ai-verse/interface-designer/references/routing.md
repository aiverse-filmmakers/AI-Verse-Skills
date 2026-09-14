# Interface Designer Routing Reference

Load the smallest useful expert subset. These are canonical AI-Verse capability IDs, not mandatory stages.

## Design and reference

| Need | Capability |
|---|---|
| distinctive visual direction, anti-generic art direction | `frontend-design` |
| product UI/UX intelligence, palettes, typography, layout, accessibility | `ui-ux-pro-max` |
| turn a vague UI idea into a builder-ready design specification | `design-first-ui-prompting` |
| analyze a reference video for interface recreation | `video-to-superprompt` |
| reliable full-page evidence for lazy/animated/WebGL reference sites | `stitched-full-page-capture` |
| explore materially different UI directions | `prototype` |

## Interaction and motion

| Need | Capability |
|---|---|
| direct manipulation, momentum, springs, interruption, gesture/spatial physics | `apple-design` |
| construct meaningful UI animation | `animate` |
| review significant animation before delivery | `review-animations` |
| audit an existing animation system | `improve-animations` |
| optional mature-product motion-polish scan | `find-animation-opportunities` |
| React Native / Expo animation | `animate-expo` |
| immersive scroll/scrollytelling | `scroll-craft` |

## Implementation

| Need | Capability |
|---|---|
| choose a UI/component dependency | `pick-ui-library` |
| React/Next performance and implementation quality | `react-best-practices` |
| React component API/composition architecture | `composition-patterns` |
| correct shadcn project/component work | `shadcn` |
| Figma Plugin API operations | `figma-use` |
| composed Figma screens/views | `figma-generate-design` |
| Canva production | `canva` |

## Final review

| Need | Capability |
|---|---|
| substantial web UI/accessibility/UX final audit | `web-design-guidelines` |

## Trigger Notes

### References

A screenshot, video, URL, named product, "copy this", "make it like this", or "recreate this" activates reference analysis. Establish whether the goal is exact recreation or inspired adaptation before building.

### Prototype

Use for substantial or ambiguous choices. Skip for micro changes, bug fixes, and locked reference recreations unless alternatives were requested.

### Apple Design

Use for interaction physics, not as a mandatory Apple visual aesthetic.

### Scroll Craft

Use only when scrolling is itself a storytelling or interaction mechanism. Skip ordinary dashboard/settings/chat/admin screens.

### React

Load React experts only after source inspection or explicit user choice proves React/Next is the target.

### shadcn

Load only when `components.json` or existing shadcn usage is present, or the user/project intentionally selected shadcn.

### Video handoff

When the requested deliverable is a rendered video or motion composition rather than an interactive interface, provide visual/design intelligence as needed and hand execution to `video-editor` when available. Do not let web UX rules override editorial or video-runtime correctness.
