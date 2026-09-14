# Third-Party Notices

AI-Verse-Skills is an original-first distribution. Third-party Skill packages remain attributable to their upstream authors and are governed by their upstream terms. The repository's MIT license covers AI-Verse-owned repository code and content only. It does not relicense third-party packages.

The authoritative package pins are in `registry/packages.json`. The public-beta redistribution, trust and ownership decisions are in `registry/trust-policy.json`.

## Public-beta distribution decisions

| Source | Repository | License decision | Public-beta handling |
|---|---|---|---|
| Google Workspace CLI | `googleworkspace/cli` | Apache-2.0 | Redistributable where recorded; selected proof packages may be vendored |
| Hermes Agent | `NousResearch/hermes-agent` | MIT | Redistributable where recorded; selected proof package may be vendored |
| LifeOS | `danielmiessler/LifeOS` | MIT | Redistributable where recorded; selected proof package may be vendored |
| Marketing Skills | `coreyhaines31/marketingskills` | MIT | Fetch-only in the public-beta distribution |
| FFmpeg Skill | `kajisho5/ffmpeg-skill` | MIT | Fetch-only in the public-beta distribution |
| ByteDance DeerFlow | `bytedance/deer-flow` | Upstream-controlled | Fetch-only |
| Anthropic Skills | `anthropics/skills` | Upstream-controlled | Fetch-only |
| Anthropic Knowledge Work Plugins | `anthropics/knowledge-work-plugins` | Upstream-controlled | Fetch-only |
| Figma MCP Server Guide | `figma/mcp-server-guide` | Upstream-controlled | Fetch-only |
| Social Media Skills | `social-media-skills/skills` | Upstream-controlled | Fetch-only |
| NovoAds Agent Skills | `novoads/agent-skills` | Upstream-controlled | Fetch-only |
| AI Film Skills | `62656456/ai-film-skills` | Upstream-controlled | Fetch-only |
| Film Production Skills | `zhangzhangco/film-production-skills` | Upstream-controlled | Fetch-only |
| Premiere Agent | `Kemerd/premiere-agent` | Upstream-controlled | Fetch-only |
| Adobe Agent Skills | `aedev-tools/adobe-agent-skills` | Upstream-controlled | Fetch-only |
| HubSpot Agent CLI Skills | `HubSpot/agent-cli-skills` | Upstream-controlled | Fetch-only |

| Anthropic Frontend Design | `anthropics/skills` | Package-level Apache-2.0 verified; repository policy remains conservative | Exact pinned upstream fetch |
| UI/UX Pro Max | `nextlevelbuilder/ui-ux-pro-max-skill` | MIT | Exact pinned upstream fetch |
| Vercel Agent Skills | `vercel-labs/agent-skills` | MIT | Exact pinned upstream fetch; web-design-guidelines has one bounded immutable-rules adaptation |
| Vercel Web Interface Guidelines | `vercel-labs/web-interface-guidelines` | MIT | Rules snapshot pinned inside the adapted review package |
| shadcn/ui Skill | `shadcn-ui/ui` | MIT | Exact pinned upstream fetch |
| Meng To Skills | `MengTo/Skills` | MIT | Exact pinned upstream fetch |
| Emil Kowalski Skills | `emilkowalski/skills` | MIT | Exact pinned upstream fetch |
| Scroll Craft | `nateherkai/scroll-craft` | MIT | Exact pinned upstream fetch |
| Nate Herk HyperFrames Student Kit | `nateherkai/hyperframes-student-kit` | MIT | Bounded vendored editorial adaptations from the exact pinned source; package-local provenance and license retained; demonstration/AIS brand assets excluded |
| HyperFrames | `heygen-com/hyperframes` | Apache-2.0 | Exact pinned fetch-only provider support for Video Editor; provider packages are internal dependencies, not member-facing duplicate Skills |

"Upstream-controlled" means AI-Verse is not making a broader redistribution claim for public beta. The installer fetches the exact pinned upstream package rather than vendoring it into the distribution.

AI-Verse does not claim authorship of third-party Skill content. Installed package provenance, source revision and content digests remain inspectable in immutable generation metadata.

## Interface Designer adaptation note

The vendored `web-design-guidelines` package preserves Vercel's review Skill and exact rule text, but replaces its runtime fetch of mutable `main` with a package-local rules snapshot pinned to `vercel-labs/web-interface-guidelines@e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`. Full provenance is stored in the package `SOURCE.json`.
