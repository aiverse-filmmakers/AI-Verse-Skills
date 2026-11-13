# Third-Party Notices

AI-Verse-Skills is an original-first distribution. Third-party Skill packages remain attributable to their upstream authors and are governed by their upstream terms. The repository's MIT license covers AI-Verse-owned repository code and content only. It does not relicense third-party packages.

The authoritative package pins are in `registry/packages.json`. The public-beta redistribution, trust and ownership decisions are in `registry/trust-policy.json`.

## Public-beta distribution decisions

| Source | Repository | License decision | Public-beta handling |
|---|---|---|---|
| Google Workspace CLI | `googleworkspace/cli` | Apache-2.0 | Redistributable where recorded; selected proof packages may be vendored |
| Hermes Agent | `NousResearch/hermes-agent` | MIT | Redistributable. Vendored and adapted, each with a `LICENSE` copy and a `SOURCE.json` change note: `email-inbox-triage`, `weekly-review-planning`, `one-three-one-rule`, `whisper`, `decision-questionnaire` (unchanged copy), and `action-items` (a merge of `meeting-action-items` and `document-to-action-items`) |
| LifeOS | `danielmiessler/LifeOS` | MIT | Redistributable; `ExtractWisdom` is vendored and adapted with a licence and source record |
| Marketing Skills | `coreyhaines31/marketingskills` | MIT | Redistributable; eight skills are vendored and adapted (`social-content`, `copywriting`, `ad-creative`, `content-strategy`, `customer-research`, `email-sequence`, `seo-audit`, `community-marketing`), each with a `LICENSE` copy and a `SOURCE.json` change note. `product-marketing-context` was replaced by per project marketing notes and its setup interview is adapted into `copywriting/references/marketing-project-setup.md` |
| FFmpeg Skill | `kajisho5/ffmpeg-skill` | MIT | Redistributable. `ffmpeg-skill` is vendored with only the skill itself (`SKILL.md`, `scripts/`, `references/`, `docs/contract.md`), a `LICENSE` copy and a `SOURCE.json` change note |
| ByteDance DeerFlow | `bytedance/deer-flow` | Upstream-controlled | Fetch-only |
| Anthropic Skills | `anthropics/skills` | Apache-2.0 for the two skills listed here only (each has its own `LICENSE.txt` at the pinned commit). Other skills in that repository, such as the document skills, are not covered | Redistributable for `canvas-design` and `frontend-design`, vendored unchanged with `LICENSE.txt` and a `SOURCE.json` record. `canvas-design` also ships its bundled fonts with their own OFL licence files |
| Anthropic Knowledge Work Plugins | `anthropics/knowledge-work-plugins` | Apache-2.0 | Redistributable; ten skills are vendored and adapted, each with a `LICENSE` copy and a `SOURCE.json` change note. The rest stay fetch-only |
| Figma MCP Server Guide | `figma/mcp-server-guide` | Upstream-controlled | Fetch-only |
| Social Media Skills | `social-media-skills/skills` | MIT | No skills left in the catalogue. Four reference files are reused, adapted, inside `social-content`, with the licence copied there |
| NovoAds Agent Skills | `novoads/agent-skills` | MIT | Redistributable. `meta-ad-builder` is vendored and adapted (Novoads requirement removed), with a `LICENSE` copy and a `SOURCE.json` change note |
| AI Film Skills | `62656456/ai-film-skills` | Apache-2.0 | `director-agent` and the merged `ai-video-director` are vendored and adapted in English, with licence and source records |
| Film Production Skills | `zhangzhangco/film-production-skills` | Upstream-controlled | Fetch-only |
| Premiere Agent | `Kemerd/premiere-agent` | Upstream-controlled | Fetch-only |
| Adobe Agent Skills | `aedev-tools/adobe-agent-skills` | Apache-2.0 | Redistributable. `after-effects-assistant` is vendored and adapted, with a `LICENSE` copy and a `SOURCE.json` change note |
| HubSpot Agent CLI Skills | `HubSpot/agent-cli-skills` | Upstream-controlled | Fetch-only |

| UI/UX Pro Max | `nextlevelbuilder/ui-ux-pro-max-skill` | MIT | Exact pinned upstream fetch |
| Vercel Agent Skills | `vercel-labs/agent-skills` | MIT, declared in each skill's own header (the repository has no top level licence file; the `LICENSE` copy in each package follows the one first recorded for `composition-patterns`) | Redistributable. `react-best-practices`, `composition-patterns` and `web-design-guidelines` are vendored, each with a `LICENSE` copy and a `SOURCE.json` change note; `web-design-guidelines` has one bounded immutable-rules adaptation |
| Vercel Web Interface Guidelines | `vercel-labs/web-interface-guidelines` | MIT | Rules snapshot pinned inside the adapted review package |
| Meng To Skills | `MengTo/Skills` | MIT | Redistributable. `video-to-superprompt` is vendored and adapted, with a `LICENSE` copy and a `SOURCE.json` change note |
| Emil Kowalski Skills | `emilkowalski/skills` | MIT | Redistributable; all skills in the catalogue are vendored, each with a `LICENSE` copy and a `SOURCE.json` change note: `pick-ui-library`, `review-animations`, `improve-animations`, `find-animation-opportunities` and `apple-design` (adapted), and `animate`, `prototype` and `animate-expo` (unchanged copies) |
| Scroll Craft | `nateherkai/scroll-craft` | MIT | Redistributable. `scroll-craft` is vendored unchanged with a `LICENSE` copy and a `SOURCE.json` record. It includes helper scripts (`scripts/*.mjs`, `encode.sh`) that run on the member's machine |
| Nate Herk HyperFrames Student Kit | `nateherkai/hyperframes-student-kit` | MIT | Bounded vendored editorial adaptations from the exact pinned source; package-local provenance and license retained; demonstration/AIS brand assets excluded |
| HyperFrames | `heygen-com/hyperframes` | Apache-2.0 | Exact pinned fetch-only provider support for Video Editor; provider packages are internal dependencies, not member-facing duplicate Skills |

"Upstream-controlled" means AI-Verse is not making a broader redistribution claim for public beta. The installer fetches the exact pinned upstream package rather than vendoring it into the distribution.

AI-Verse does not claim authorship of third-party Skill content. Installed package provenance, source revision and content digests remain inspectable in immutable generation metadata.

## Interface Designer adaptation note

The vendored `web-design-guidelines` package preserves Vercel's review Skill and exact rule text, but replaces its runtime fetch of mutable `main` with a package-local rules snapshot pinned to `vercel-labs/web-interface-guidelines@e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`. Full provenance is stored in the package `SOURCE.json`.
