# Top 80 Existing Employee Skills to Add Above the AI-Verse Foundation

**Research snapshot:** 2026-09-09

## Executive conclusion

This is the research-backed sourcing shortlist for the **80 employee-facing skills that should sit on top of the original 20 Machine / Reliability Foundation skills**.

The goal is not to turn AI-Verse into a larger coding agent. The goal is to make it feel like an unusually capable employee who can enter a company, understand the work, use common business and creative software, make decisions, produce deliverables and operate across departments.

The original 20 remain intact underneath this list. They provide verification, deep research, browser operation, safe refactoring, incident analysis, structured write-back, delegation and capability self-improvement. They are not counted again here.

**Target after this shortlist:**

- 20 Machine / Reliability Foundation skills
- 80 employee-facing skills from this research
- 100 foundational first-party capabilities total
- additional specialist Operator Packs and industry packs later

This file supersedes the earlier conceptual 80 as the **sourcing priority list**. The earlier list remains useful as a capability taxonomy, but this list answers a different question: *Which excellent skills already exist today that AI-Verse should adopt, adapt, wrap or reimplement?*

---

## How the 80 were selected

I screened official vendor skills, major agent ecosystems, role packs, specialist creative repositories and current skill marketplaces. The strongest sources included:

- Nous Research Hermes Agent
- Anthropic Knowledge Work Plugins
- Anthropic Skills
- Google Workspace CLI skills and personas
- Daniel Miessler LifeOS
- Corey Haines Marketing Skills
- social-media-skills/skills
- ByteDance DeerFlow
- HubSpot Agent CLI Skills
- Figma MCP guidance and ecosystem skills
- Adobe Agent Skills
- Novoads marketing skills
- AI Film Skills
- Film Production Skills
- FFmpeg Skill
- Premiere Agent implementations

Marketplaces were used for discovery and adoption signals, not as a trust source. Popularity can surface useful candidates, but a high install count does not prove that a skill is safe, well scoped or well engineered.

### Selection score

Each candidate was judged approximately on:

| Dimension | Weight |
|---|---:|
| Professional leverage | 25% |
| Execution depth | 20% |
| Breadth and reusability | 15% |
| Quality, validation and failure handling | 15% |
| Real software/tool fluency | 10% |
| Composability with other skills | 10% |
| Maintenance and currentness | 5% |

### The hiring test

A skill survived only if the answer to this question was strong:

> If this capability were an employee, would I trust it to own a meaningful unit of work and deliver something useful?

This removed many skills that are merely persona prompts, tiny utility wrappers, duplicated workflows or collections of generic advice.

---

## Adoption modes

Do **not** mass-copy these repositories into AI-Verse.

| Mode | Meaning |
|---|---|
| **ADAPT** | Strong skill with a permissive license or clearly reusable implementation. Normalize it into the AI-Verse contract and preserve required attribution/notices. |
| **WRAP** | Valuable workflow tied to a particular application or provider. Preserve the professional workflow but bind it to AI-Verse connectors, APIs or Operator Packs. |
| **REBUILD** | Excellent behavior but unclear/restrictive licensing, excessive runtime coupling or incompatible architecture. Reimplement the capability from first principles without copying protected implementation text/code. |
| **EVAL-HARD** | Promising newer specialist skill with limited production history. Admit only after stronger adversarial and output-quality evaluations. |

Every imported or adapted capability must still pass AI-Verse security scanning, trigger/non-trigger tests, workspace isolation checks and functional evals.

---

# The Top 80

## A. Universal Employee and Office Operations

These are the capabilities that make the agent immediately useful in an ordinary company before any specialist role is selected.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 1 | `persona-exec-assistant` | `googleworkspace/cli` | One of the best ready-made employee personas: inbox, calendar, meeting prep, scheduling and executive follow-through using real Workspace actions. | WRAP |
| 2 | `persona-project-manager` | `googleworkspace/cli` | Coordinates plans, status, documents, schedules and team communication through actual Google Workspace operations. | WRAP |
| 3 | `persona-hr-coordinator` | `googleworkspace/cli` | Gives the agent a practical HR coordination surface rather than a generic HR advice prompt. | WRAP |
| 4 | `persona-event-coordinator` | `googleworkspace/cli` | Handles calendars, invitations, materials, attendee coordination and event logistics with real Workspace primitives. | WRAP |
| 5 | `email-inbox-triage` | `NousResearch/hermes-agent` | Prioritizes inboxes and drafts replies with explicit safety around sending. This is core employee behavior. | ADAPT |
| 6 | `meeting-action-items` | `NousResearch/hermes-agent` | Converts meetings into cited decisions, owners and concrete follow-up work instead of generic summaries. | ADAPT |
| 7 | `document-to-action-items` | `NousResearch/hermes-agent` | Turns reports, notes and documents into owned actions, making passive knowledge operational. | ADAPT |
| 8 | `weekly-review-planning` | `NousResearch/hermes-agent` | Runs a professional weekly reset across commitments, stalled work and next-week priorities. | ADAPT |
| 9 | `one-three-one-rule` | `NousResearch/hermes-agent` | Produces concise 1-3-1 decision briefs: one problem, three options, one recommendation. Excellent manager communication discipline. | ADAPT |
| 10 | `google-workspace` | `NousResearch/hermes-agent` | Broad Gmail, Calendar, Drive, Docs and Sheets competence through deterministic tooling. | WRAP |
| 11 | `xlsx` | `NousResearch/hermes-agent` | Creates, reads and edits real Excel/CSV files with deterministic scripts rather than pretending spreadsheets are prose. | ADAPT |
| 12 | `docx` | `NousResearch/hermes-agent` | Creates, edits, templates and reviews Word documents, a universal employee deliverable. | ADAPT |
| 13 | `ppt-generation` | `bytedance/deer-flow` | Strong end-to-end presentation production capability rather than a thin PPTX writer. | ADAPT |
| 14 | `airtable` | `NousResearch/hermes-agent` | Real Airtable record CRUD, filtering and upserts. Useful across operations, production, CRM and content workflows. | WRAP |
| 15 | `notion` | `NousResearch/hermes-agent` | Real Notion pages/databases/Markdown operations for companies that use Notion as an operating system. | WRAP |
| 16 | `internal-comms` | `anthropics/skills` | High-quality internal updates, announcements and company communications with professional structure. | ADAPT after per-skill license check |

### Why this section is strong

Google Workspace's current repository contains not only low-level Gmail/Calendar/Docs/Sheets skills but complete employee personas and cross-application recipes. Hermes complements it with safer triage, meeting action extraction and file-format production. Together they give AI-Verse both role intelligence and real execution.

---

## B. Intelligence, Judgment and Strategy

These make the agent feel thoughtful and senior rather than simply obedient.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 17 | `Council` | `danielmiessler/LifeOS` | Multi-agent expert debate with visible intellectual friction. Excellent for difficult business decisions. | ADAPT |
| 18 | `RedTeam` | `danielmiessler/LifeOS` | Adversarially attacks plans, claims and strategies, then steelmans and ranks failures by severity. | ADAPT |
| 19 | `ExtractWisdom` | `danielmiessler/LifeOS` | Deeply distills interviews, podcasts, videos and articles with content-adaptive sections and contrarian analysis. | ADAPT |
| 20 | `Ideate` | `danielmiessler/LifeOS` | Structured high-divergence ideation that is materially stronger than “give me ten ideas.” | ADAPT |
| 21 | `Fabric` | `danielmiessler/LifeOS` | Routes into hundreds of specialized extraction, analysis, creation, improvement and security patterns. | ADAPT |
| 22 | `decision-questionnaire` | `NousResearch/hermes-agent` | Turns underspecified or unanswerable decisions into a structured questionnaire for the person who has the missing knowledge. | ADAPT |
| 23 | `product-brainstorming` | `anthropics/knowledge-work-plugins` | Product ideation grounded in actual product-management work rather than free-association brainstorming. | ADAPT |
| 24 | `business-pulse` | `anthropics/knowledge-work-plugins` | Produces a compact view of what matters in a small business, helping the agent behave like an operator/owner. | ADAPT |

---

## C. Creative Direction, Brand and Design

These are essential if AI-Verse is supposed to feel like a creative employee rather than a business analyst with image tools attached.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 25 | `brand-guidelines` | `anthropics/skills` | Converts brand rules into consistent decisions across visual and written artifacts. | ADAPT |
| 26 | `canvas-design` | `anthropics/skills` | Strong general visual-design skill for creating polished static design artifacts. | ADAPT |
| 27 | `figma-use` | Figma/OpenAI agent ecosystem | Teaches the agent to use Figma as a design environment rather than merely describe UI. | REBUILD/WRAP |
| 28 | `figma-generate-design` | `figma/mcp-server-guide` | Official Figma-oriented generation workflow with direct MCP integration concepts. | REBUILD/WRAP because repository licensing is unclear |
| 29 | `canva` | `social-media-skills/skills` | One of the strongest current Canva operator skills, covering Brand Kit, Bulk Create, resize, Magic Studio and real automation paths. | ADAPT/WRAP |
| 30 | `design-and-templates` | `social-media-skills/skills` | Builds repeatable visual systems instead of one-off graphics, important for company-scale content production. | ADAPT |
| 31 | `baoyu-article-illustrator` | `NousResearch/hermes-agent` / `JimLiu/baoyu-skills` | Generates coherent article illustration systems using type, style and palette consistency. | ADAPT with upstream attribution |
| 32 | `theme-factory` | `anthropics/skills` | Creates reusable visual themes that can be applied across documents and presentations. | ADAPT after per-skill license check |

---

## D. Marketing, Content and Social Media

This category was heavily filtered because the public ecosystem contains many shallow marketing prompts. The winners below either have high real-world adoption, strong process depth or actual platform execution.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 33 | `product-marketing-context` | `coreyhaines31/marketingskills` | Establishes the strategic product/market/customer context other marketing work should inherit. | ADAPT |
| 34 | `customer-research` | `coreyhaines31/marketingskills` | Turns qualitative customer material into usable positioning and marketing intelligence. | ADAPT |
| 35 | `content-strategy` | `coreyhaines31/marketingskills` | Creates a coherent content system instead of isolated posts. | ADAPT |
| 36 | `social-content` | `coreyhaines31/marketingskills` | Strong multi-platform social planning and creation discipline with major ecosystem adoption. | ADAPT |
| 37 | `copywriting` | `coreyhaines31/marketingskills` | Broad conversion-oriented professional copywriting skill with one of the strongest adoption signals in the skill ecosystem. | ADAPT |
| 38 | `ad-creative` | `coreyhaines31/marketingskills` | Focuses on actual performance creative, hooks, angles and variants rather than generic ad prose. | ADAPT |
| 39 | `email-sequence` | `coreyhaines31/marketingskills` | Builds complete lifecycle/campaign email sequences rather than single emails. | ADAPT |
| 40 | `seo-audit` | `coreyhaines31/marketingskills` | Mature, highly adopted SEO auditing workflow. | ADAPT |
| 41 | `analytics` | `coreyhaines31/marketingskills` | Interprets marketing analytics and instrumentation in a decision-oriented way. | ADAPT |
| 42 | `launch-strategy` | `coreyhaines31/marketingskills` | Plans product/content launches as coordinated campaigns rather than a post calendar. | ADAPT |
| 43 | `community-marketing` | `coreyhaines31/marketingskills` | Adds a people/community growth discipline often missing from generic marketing agents. | ADAPT |
| 44 | `scheduling-and-queue` | `social-media-skills/skills` | Covers the operational publishing side of social media, not only ideation and captions. | ADAPT/WRAP |
| 45 | `cross-platform-repurposing` | `social-media-skills/skills` | Converts one source asset into platform-native derivatives rather than simple cross-posting. | ADAPT |
| 46 | `meta-ad-builder` | `novoads` | Produces and publishes real Meta ad structures, using performance/ad-library context and safe paused creation patterns. | ADAPT/WRAP |

### Why Corey Haines is heavily represented

The `coreyhaines31/marketingskills` repository is unusually strong for a community skill collection: it is MIT-licensed, actively maintained in September 2026, has tens of thousands of GitHub stars and millions of cumulative installs across its skills. That does not make every skill automatically good, but it makes the best members of that collection significantly more battle-tested than typical prompt packs.

---

## E. Film, Video, Audio and Post-Production

This is intentionally deeper than most general agent systems because creative media should be a first-class AI-Verse department.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 47 | `director-agent` | `62656456/ai-film-skills` | Encodes actual directing logic and shot/story decisions rather than prompt decoration. | EVAL-HARD + ADAPT |
| 48 | `ai-storyboard-director` | `62656456/ai-film-skills` | Converts story intent into storyboard-oriented visual planning and continuity. | EVAL-HARD + ADAPT |
| 49 | `produce-ai-video` | `62656456/ai-film-skills` | Ambitious end-to-end autonomous AI video production from approved material through generation, edit, sound and QC. | EVAL-HARD + ADAPT |
| 50 | `structure-screenplay` | `zhangzhangco/film-production-skills` | Produces structured screenplay handoffs suitable for downstream production workflows. | EVAL-HARD + ADAPT |
| 51 | `plan-camera-shots` | `zhangzhangco/film-production-skills` | Creates generation-ready shot planning rather than generic shot lists. | EVAL-HARD + ADAPT |
| 52 | `ffmpeg-skill` | `kajisho5/ffmpeg-skill` | One of the strongest operational media skills found: structured local FFmpeg tools, probe-edit-check-verify workflow and machine-readable contracts. | ADAPT |
| 53 | `premiere-agent` | `InfoEconFilms/premiere-agent` / `Kemerd/premiere-agent` | Excellent benchmark for real editor behavior: multimodal preprocessing, persistent project context and Premiere/FCPXML handoff. | REBUILD because no clear license was found |
| 54 | `after-effects-assistant` | `aedev-tools/adobe-agent-skills` | Real After Effects automation with project inspection, scripts, layers, keyframes, effects, comps, assets and render workflows. | ADAPT/WRAP |
| 55 | `kanban-video-orchestrator` | `NousResearch/hermes-agent` | Plans and runs multi-agent video production pipelines with explicit work decomposition. | ADAPT |
| 56 | `whisper` | `NousResearch/hermes-agent` | Reliable transcription/translation capability across 99 languages, foundational for meetings, interviews, podcasts and post-production. | ADAPT |

### Film skill caution

Some of the most interesting AI-film repositories are very new in August/September 2026. They made this shortlist because their workflow design is unusually relevant, not because they have long production histories. AI-Verse should run them through harder continuity, timing, asset-lock, prompt-quality and final-video evals before promoting them to trusted first-party skills.

---

## F. Sales, CRM, Customer Success and Commerce

The best skills here combine professional sales/support reasoning with actual CRM operations.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 57 | `account-research` | `anthropics/knowledge-work-plugins` | Prepares account intelligence specifically for sales work rather than producing generic company research. | ADAPT |
| 58 | `call-prep` | `anthropics/knowledge-work-plugins` | Builds a useful sales-call brief covering account context, attendees, discovery, likely objections and goals. | ADAPT |
| 59 | `draft-outreach` | `anthropics/knowledge-work-plugins` | Produces contextual outbound communication rather than generic cold-email templates. | ADAPT |
| 60 | `pipeline-review` | `anthropics/knowledge-work-plugins` | Reviews sales pipeline quality, risk and next actions as a manager would. | ADAPT |
| 61 | `deal-management` | `hubspot/agent-cli-skills` | Real CRM deal operations with pipeline discovery and safer mutation patterns. | WRAP |
| 62 | `sales-execution` | `hubspot/agent-cli-skills` | Executes actual CRM sales work, activity logging and next-step management instead of only advising a rep. | WRAP |
| 63 | `draft-response` | `anthropics/knowledge-work-plugins` | Produces grounded customer-support replies using case/customer context. | ADAPT |
| 64 | `ticket-triage` | `anthropics/knowledge-work-plugins` | Prioritizes and routes incoming support work with a professional support workflow. | ADAPT |
| 65 | `customer-retention` | `hubspot/agent-cli-skills` | Detects and acts on retention/churn situations using CRM/customer signals. | WRAP |
| 66 | `shopify` | `NousResearch/hermes-agent` | Gives the agent a serious ecommerce operations surface through the Shopify Admin GraphQL API. | WRAP |

---

## G. Finance and Accounting

This category intentionally favors operational accounting/FP&A work over speculative trading or consumer-finance gimmicks.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 67 | `cash-flow-snapshot` | `anthropics/knowledge-work-plugins` | Produces the immediate cash view a small-business operator actually needs. | ADAPT |
| 68 | `financial-statements` | `anthropics/knowledge-work-plugins` | Prepares and reasons over professional financial statements. | ADAPT |
| 69 | `variance-analysis` | `anthropics/knowledge-work-plugins` | Explains actual-vs-budget/forecast differences and focuses attention on material drivers. | ADAPT |
| 70 | `reconciliation` | `anthropics/knowledge-work-plugins` | Encodes a real finance-control workflow rather than generic spreadsheet arithmetic. | ADAPT |
| 71 | `close-management` | `anthropics/knowledge-work-plugins` | Coordinates month/period close work, dependencies and evidence. | ADAPT |
| 72 | `journal-entry-prep` | `anthropics/knowledge-work-plugins` | Prepares journal entries with support and review discipline. | ADAPT |
| 73 | `excel-author` | `NousResearch/hermes-agent` | Produces auditable finance workbooks headlessly with formulas and structured modeling. | ADAPT |
| 74 | `3-statement-model` | `NousResearch/hermes-agent` | Builds integrated income statement, balance sheet and cash-flow models, a serious finance capability. | ADAPT |

---

## H. Product, People, Legal and Business Operations

These fill important departments that would otherwise make the “any company” claim hollow.

| # | Existing skill | Source | Why it belongs | Mode |
|---:|---|---|---|---|
| 75 | `write-spec` | `anthropics/knowledge-work-plugins` | Produces proper product specs/PRDs with goals, non-goals, requirements, metrics and acceptance criteria. | ADAPT |
| 76 | `roadmap-update` | `anthropics/knowledge-work-plugins` | Maintains product roadmaps and stakeholder-facing changes instead of treating a roadmap as a static list. | ADAPT |
| 77 | `job-post-builder` | `anthropics/knowledge-work-plugins` | Creates hiring-ready role/job specifications for small-business and people operations. | ADAPT |
| 78 | `review-contract` | `anthropics/knowledge-work-plugins` | Reviews commercial contracts systematically and surfaces relevant clauses/issues for human legal judgment. | ADAPT with high-stakes approval policy |
| 79 | `legal-risk-assessment` | `anthropics/knowledge-work-plugins` | Structures legal risk, severity and escalation rather than pretending the agent is final legal authority. | ADAPT with high-stakes approval policy |
| 80 | `vendor-check` | `anthropics/knowledge-work-plugins` | Performs practical vendor diligence and flags issues before procurement/engagement decisions. | ADAPT |

---

# Source quality notes

## 1. Hermes Agent

Hermes is one of the most useful benchmarks because its skill ecosystem is no longer coding-centric. It contains productivity, communication, creative, finance, ecommerce, media and software-operation skills, while retaining progressive disclosure and a real skill manager/curator.

Particularly strong patterns worth preserving:

- concise discovery metadata
- explicit related skills
- deterministic helper scripts for file/media work
- tool availability requirements
- secure environment-variable declarations
- safe fallbacks
- platform gating
- current software/API knowledge

AI-Verse should adopt the capability pattern but replace Hermes-specific permissions, profile paths and runtime assumptions with AI-Verse contracts.

## 2. Anthropic Knowledge Work Plugins

This collection produced more genuinely employable department workflows than almost any other source reviewed. Finance alone includes close management, reconciliations, journal entries, statements, audit support, variance analysis and SOX work. Sales, support, product and legal have similarly concrete units of work.

The strongest lesson is that a professional skill should own a **deliverable or business process**, not merely a topic.

## 3. Google Workspace CLI

Google's skill catalog is an unusually good example of the distinction between:

- low-level application skills
- reusable cross-application recipes
- full employee personas

AI-Verse should preserve this three-level idea, but a Google “persona” should become an AI-Verse Role Bundle plus capabilities and Operator Packs rather than a giant always-on persona prompt.

## 4. LifeOS

LifeOS contributes unusually strong judgment skills. `Council`, `RedTeam`, `ExtractWisdom`, `Ideate` and `Fabric` give the agent ways to think, challenge and distill rather than simply execute.

These should remain bounded capabilities, not become the personality or Brain of AI-Verse.

## 5. Marketing Skills

The Corey Haines collection is the clearest example of a community skill repository earning significant real-world adoption. The winning lesson is breadth plus specialization: context, research, copy, ads, email, SEO, analytics, launch and community are separate disciplines that can compose.

## 6. Film/post-production

The film ecosystem is younger and less standardized than finance or office work. However, the best skills are beginning to show the right traits:

- explicit screenplay/storyboard/shot handoffs
- visual continuity and asset locks
- generation-stage gates
- local deterministic media processing
- actual NLE interchange formats
- review and QC loops
- production orchestration

`ffmpeg-skill` is especially notable because it treats media operations as structured tools with verification rather than free-form shell commands.

---

# What was deliberately NOT selected

Hundreds of useful skills were found but did not make the first 80. Examples include:

### Strong marketing bench

- `marketing-psychology`
- `programmatic-seo`
- `cold-email`
- `sales-enablement`
- `revops`
- `churn-prevention`
- `pricing-strategy`
- `public-relations`
- `influencer-marketing`

### Strong social/content bench

- `caption-writer`
- `short-form-video-script`
- `community-management`
- `analytics-and-reporting`
- `trend-jacking`
- `capcut`

### Strong finance/legal/support bench

- `audit-support`
- `sox-testing`
- `customer-escalation`
- `kb-article`
- `signature-request`
- `triage-nda`
- `compliance-check`

### Strong CRM bench

- `quote-to-cash`
- `crm-data-quality`
- `ticket-resolution`
- `workflow-automation`

### Strong film bench

- `review-and-assemble`
- `compile-generation-prompts`
- `design-production-assets`
- `execute-media-generation`

These are excellent Wave 2 candidates. The point of the 80 is not to claim that skill 81 is bad. It is to establish the highest-leverage first-party surface without immediately creating a 300-skill catalog.

---

# Import strategy for AI-Verse

## Do not preserve foreign runtime authority

No imported skill may retain the ability to decide its own:

- workspace root
- filesystem grant
- secret visibility
- network permission
- connector permission
- destructive-operation approval
- cross-workspace access
- long-term knowledge write target

These are always resolved by AI-Verse OS.

## Normalize each selected skill

Every selected capability should be translated into the AI-Verse package shape:

```text
skill-name/
├── SKILL.md
├── aiverse.skill.yaml
├── references/
├── scripts/
├── schemas/
├── examples/
└── evals/
```

The normalized version should preserve the best professional method while replacing foreign runtime assumptions.

## Separate skill from operator

Several items in this list should eventually become or depend on Operator Packs:

- Google Workspace
- Airtable
- Notion
- Canva
- Figma
- HubSpot
- Shopify
- Premiere Pro
- After Effects

For example, `deal-management` is the professional capability. `hubspot-operator` is software competence. The final AI-Verse design may split the imported HubSpot skill into those two layers while preserving its behavior.

## Preserve provenance

The registry should record at least:

```yaml
provenance:
  upstream_repo: owner/repo
  upstream_skill: skill-name
  upstream_commit: <sha>
  upstream_license: <license>
  adaptation: adapted | wrapped | rebuilt
  imported_at: <timestamp>
```

This allows future upstream-diff monitoring without letting upstream changes silently enter production.

---

# Security and quality gate before adoption

Every one of these 80 should enter through the same admission pipeline:

1. Pin the exact upstream commit.
2. Read and record the applicable license.
3. Copy only when the license permits it.
4. Scan all instructions, scripts, references and assets.
5. Remove foreign permission/self-authority instructions.
6. Normalize paths and secret handling.
7. Deduplicate against the existing 20 and previously imported skills.
8. Write trigger and non-trigger evals.
9. Write happy-path and failure-path functional evals.
10. Add workspace escape and indirect prompt-injection tests.
11. Run in an isolated test workspace.
12. Promote only after the output quality beats a no-skill baseline.
13. Record provenance and upstream version.

For newer film/creative skills, add visual continuity, asset consistency, final-output QC and human-review gates where appropriate.

---

# Recommended implementation waves

The ranking above is the top 80 overall, but implementation should be staged by how quickly the capability makes AI-Verse feel like an employee.

## Wave 1: Immediate employee effect

Start with:

- `persona-exec-assistant`
- `email-inbox-triage`
- `meeting-action-items`
- `google-workspace`
- `xlsx`
- `docx`
- `ppt-generation`
- `one-three-one-rule`
- `Council`
- `ExtractWisdom`
- `brand-guidelines`
- `canva`
- `product-marketing-context`
- `customer-research`
- `content-strategy`
- `social-content`
- `copywriting`
- `cross-platform-repurposing`
- `account-research`
- `call-prep`
- `cash-flow-snapshot`
- `variance-analysis`
- `write-spec`
- `review-contract`

This already creates a remarkably broad employee.

## Wave 2: Creative production and operating software

Add:

- Figma pair
- Airtable
- Notion
- HubSpot pair
- Shopify
- social scheduling
- Meta ads
- AI-film skills
- FFmpeg
- After Effects
- video orchestration
- transcription

## Wave 3: Department depth

Add the remaining finance, legal, product, support, HR and advanced marketing skills.

---

# Final recommendation

The original conceptual employee list was useful for deciding **what kinds of abilities AI-Verse should have**.

This research changes the next step. We should not invent most of those abilities from scratch.

A large amount of excellent work already exists. AI-Verse should become a **curated capability integrator**:

1. take the best existing professional workflow,
2. preserve its useful domain knowledge,
3. strip its runtime assumptions and self-authority,
4. bind it to AI-Verse workspace and permission contracts,
5. add stronger verification and evals,
6. track upstream provenance,
7. improve it over time.

The target is not “100 prompt files.”

The target is **100 dependable professional abilities that make the agent employable on day zero**.

---

# Primary source repositories

- https://github.com/NousResearch/hermes-agent
- https://github.com/anthropics/knowledge-work-plugins
- https://github.com/anthropics/skills
- https://github.com/googleworkspace/cli
- https://github.com/danielmiessler/LifeOS
- https://github.com/coreyhaines31/marketingskills
- https://github.com/social-media-skills/skills
- https://github.com/bytedance/deer-flow
- https://github.com/hubspot/agent-cli-skills
- https://github.com/figma/mcp-server-guide
- https://github.com/aedev-tools/adobe-agent-skills
- https://github.com/62656456/ai-film-skills
- https://github.com/zhangzhangco/film-production-skills
- https://github.com/kajisho5/ffmpeg-skill
- https://github.com/InfoEconFilms/premiere-agent

**Important:** repository-level licenses are not enough when a project contains per-skill licenses. Verify the exact file/license at the pinned commit before any direct import.