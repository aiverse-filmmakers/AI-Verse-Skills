# Skill library status

The single record of the 2026 library cleanup. Last updated 13 November 2026 (Group B marketing tidy added).
Starting point: 118 catalogue skills (main at `bab2834`).

| Status | Count |
|---|---|
| Removed in this change | 58 |
| Kept and improved (owned by AI-Verse) | 33 |
| Kept as they are | 3 |
| Still to review | 24 |
| **Catalogue after this change** | **60** (36 kept + 24 to review) |

`notion` and `shadcn` were removed earlier (pull request #28) and are not counted here.

## Kept and improved (33)

None of these has been tested with and without the skill yet. Scores are estimates.

**Developer, rebuilt (9):** `root-cause-debugger` (now also covers environment, configuration and incident timelines), `deep-research-synthesis`, `structured-ingestion-normalization`, `api-integration-engineer`, `dependency-supply-chain-audit`, `change-review`, `verification-harness`, `transactional-refactor` (now also covers codebase mapping), `git-change-lifecycle` (now also covers the release checklist)

**Outside skills, now owned copies with `LICENSE` and `SOURCE.json` (17):**
- Anthropic, Apache 2.0: `review-contract` (now includes legal risk scoring), `account-research` (now includes call briefs), `cash-flow-snapshot`, `job-post-builder`, `business-pulse`, `draft-response`, `draft-outreach`, `write-spec`, `product-brainstorming`, `roadmap-update`
- Vercel, MIT: `composition-patterns`
- Emil Kowalski, MIT: `pick-ui-library`, and from 13 November `review-animations`, `improve-animations`, `find-animation-opportunities`, `apple-design` (kept by decision; structure fixes only, the author's rules, values and tone are untouched)
- Corey Haines, MIT: `social-content` (13 November; inner name fixed, repurposing references added), and from the 13 November marketing tidy `copywriting`, `ad-creative`, `content-strategy`, `customer-research`, `email-sequence` (inner name was `emails`), `seo-audit`, `community-marketing` (pointers to skills and tools not in the library removed; the marketing advice is unchanged; the lines that read `.agents/product-marketing.md` are left on purpose until per project adjustments replace `product-marketing-context`)

## Kept as they are (3)

`react-best-practices` (Vercel), `animate-expo` (Emil Kowalski), `google-workspace` (Hermes; still to decide between porting it properly or relying on Claude's and ChatGPT's own Google connections).

## Removed (58)

- **Accounting (7):** `journal-entry-prep`, `reconciliation`, `close-management`, `3-statement-model`, `excel-author`, `financial-statements`, `variance-analysis`
- **Sales and support systems (6):** `customer-retention`, `deal-management`, `sales-execution`, `pipeline-review`, `ticket-triage`, `vendor-check`
- **Office personas (4):** `persona-event-coordinator`, `persona-exec-assistant`, `persona-hr-coordinator`, `persona-project-manager`
- **Wrong fit (7):** `brand-guidelines`, `internal-comms`, `Fabric`, `figma-use`, `figma-generate-design`, `airtable`, `shopify`
- **Developer stubs (6):** `skill-forge` (replaced by `/skill`), `skill-miner` (moving into `/learn`), `knowledge-writeback`, `delegation-orchestrator`, `database-migration-guardian`, plus `browser-workflow-operator`
- **Folded into kept skills (7):** `environment-doctor`, `configuration-contract-doctor`, `incident-forensics` (into `root-cause-debugger`), `semantic-codebase-sweep` (into `transactional-refactor`), `release-deploy-guard` (into `git-change-lifecycle`), `legal-risk-assessment` (into `review-contract`), `call-prep` (into `account-research`)
- **Second review (12):** `premiere-agent` (overlaps `video-editor`), `kanban-video-orchestrator` (Hermes only), `analytics`, `scheduling-and-queue` (WoopSocial only), `docx`, `xlsx`, `ppt-generation` (Claude and Codex have their own), `Council`, `Ideate` (broken outside the author's setup), `design-and-templates`, `baoyu-article-illustrator`, `theme-factory`
- **Third review, 13 November (9):** `structure-screenplay`, `plan-camera-shots` (built for an outside software pipeline; `director-agent` and `ai-storyboard-director` cover the same jobs), `cross-platform-repurposing` (mostly pointers to skills not in the library; `social-content` covers repurposing, and its reference files are to be reused there), `launch-strategy` (software product launches), `canva` (mostly pointers to WoopSocial and missing skills; Canva's own connection does the work), `RedTeam` (32 agents per run, outside voice server and folders; a small replacement is to be built), `ui-ux-pro-max` (commands fail outside a Claude plugin, 3.6 MB), `design-first-ui-prompting` (a thin image prompt template), `stitched-full-page-capture` (tied to its author's own article workflow)

`interface-designer` no longer routes to the removed Figma skills: its Figma target now reports "unavailable" unless the runtime has its own Figma skills. The same now applies to Canva. The interface designer does the UI and UX reasoning and the design specification itself, since `ui-ux-pro-max` and `design-first-ui-prompting` are gone.

## Still to review (24)

Decided 13 November: keep all of them. Group A (nine skills) is left as it is, Group B (marketing, seven skills) is done above, Groups C and D are still to do. See entry D33 of the skills plan.

Scores from a first read on 12 November (usefulness to members / craft, out of 10), with the recommended action. A second read of every skill in full gave different scores and recommendations for several of these; that review is entry D31 of the skills plan in the AI-Verse OS development workspace. Decided on 13 November: `product-marketing-context` will be replaced by per project adjustments once those exist. The four animation and Apple skills that review recommended removing were kept by decision on 13 November.

### Film and video (7)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `video-editor` | 9 | 8 | Keep |
| `director-agent` | 9 | 7 | Keep. Clean up the mixed Chinese terms |
| `video-to-superprompt` | 8 | 7 | Keep |
| `ffmpeg-skill` | 8 | 8 | Keep. Strip the author's 12 stray `.claude/skills` files |
| `produce-ai-video` | 8 | 6 | Keep. Make it work outside Codex |
| `ai-storyboard-director` | 8 | 6 | Translate to English (it never triggers on English requests) |
| `after-effects-assistant` | 6 | 7 | Keep. Fix the inner name (`after-effects`) |

### Marketing (2)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `product-marketing-context` | 7 | 8 | Decided 13 November: to be replaced by per project adjustments. It stays until those exist (skills plan, Phase 1). Then it is removed and the marketing skills read the current project's adjustments instead. Reason: it saves one file for the whole OS folder, so every project would share one brand |
| `meta-ad-builder` | 6 | 7 | Keep (needs Meta API keys) |

### Web and interface design (6), recommended as one optional pack
| Skill | Use | Craft |
|---|---|---|
| `interface-designer` | 7 | 7 |
| `frontend-design` | 6 | 8 |
| `scroll-craft` | 5 | 8 |
| `web-design-guidelines` | 5 | 7 |
| `animate` | 4 | 9 |
| `prototype` | 4 | 9 |

### Office (5)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `whisper` | 7 | 5 | Keep. Trim the GitHub star padding |
| `meeting-action-items` | 6 | 6 | Merge with `document-to-action-items`. Remove Hermes only tool names |
| `document-to-action-items` | 6 | 6 | As above |
| `email-inbox-triage` | 6 | 6 | Keep. Remove Hermes only tool names |
| `weekly-review-planning` | 6 | 6 | Keep. Remove Hermes only tool names |

### Thinking (3)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `ExtractWisdom` | 7 | 4 | Rewrite: remove the author's private voice server and folders, lowercase the name |
| `one-three-one-rule` | 5 | 7 | Keep |
| `decision-questionnaire` | 5 | 7 | Keep |

### Visual design (1)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `canvas-design` | 6 | 7 | Keep |

## Open items

1. No skill in this change has been tested with and without the skill in fresh chats.
2. Six AI-Verse specific rules taken out of `change-review` should become AI-Verse OS project adjustments for that skill.
3. Library skills are not yet copied into `.claude/skills` and `.agents/skills`, so Claude and Codex cannot trigger them by themselves. This is the main reason the library has barely been used.
4. A usage counter (count and last used date per skill) does not exist yet.
