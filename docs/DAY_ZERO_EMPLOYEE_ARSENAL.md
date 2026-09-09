# AI-Verse Skills: Day-Zero Employee Arsenal

**Status:** architecture direction
**Snapshot:** 2026-09-09

## North star

AI-Verse-Skills should make an AI agent feel less like a coding harness and more like an unusually capable employee who can join a company, learn how that company works, use its software, produce professional deliverables, communicate with people, and execute work across departments.

The agent should be able to function as an executive assistant, researcher, operations coordinator, marketer, social-media manager, designer, producer, editor, sales assistant, account manager, finance analyst, customer-support agent, recruiter, project coordinator, or technical operator depending on the job in front of it.

Coding is one department. It must not define the character of the whole capability system.

The previously proposed 20 operational skills are retained, but reclassified as the **Machine / Reliability Foundation** beneath this employee layer. They make execution safe and dependable. They are not the primary Day-Zero experience.

## Why this direction

The strongest general agents are already broadening beyond code. Hermes, for example, now exposes skills for creative ideation, article illustration, video orchestration, social-media calendars, financial models, PowerPoint production, email, telephony, research, shopping, Shopify, audio generation, image generation, Blender, Unreal and more. LifeOS similarly treats skills as the action surface rather than merely a programming toolkit.

AI-Verse should push this further and organize capability around **real work roles and deliverables**.

## Target architecture

The proposed first-party target is:

- **80 employee-facing capability skills**
- **20 Machine / Reliability Foundation skills** already identified
- **app/operator mastery packs** for the software companies actually use
- **role bundles** that combine the right skills and app packs for a job

This creates roughly **100 first-party foundational skills** before optional app-specific and industry-specific packs are counted.

The runtime should not load all of them into context. Progressive discovery keeps the agent broad without making each request bloated.

---

# The 80 employee-facing skills

## A. Universal Employee Core

These should feel useful in almost any company on the first day.

### 1. `company-onboarding`
Rapidly learns the company's products, customers, org structure, terminology, brand, policies, workflows, active projects, connected software and current priorities from the workspace it is granted.

### 2. `work-triage`
Turns a messy stream of requests, messages, tasks and deadlines into an ordered action queue with urgency, importance, dependencies and blockers.

### 3. `executive-briefing`
Compresses complex information into short decision-ready briefs containing what changed, why it matters, risks, options and recommended next actions.

### 4. `meeting-operator`
Prepares agendas and context, captures decisions and action items, produces useful notes and drives follow-up after meetings.

### 5. `inbox-operator`
Triages email and business messages, identifies what needs attention, drafts replies, extracts commitments and keeps communication from becoming a hidden task list.

### 6. `professional-writing`
Writes and rewrites emails, reports, memos, announcements, briefs, policies, client communication and internal business copy in the appropriate voice.

### 7. `document-builder`
Creates polished business documents from rough information, including reports, briefs, proposals, guides, plans, handbooks and structured PDFs/DOCX files.

### 8. `spreadsheet-analyst`
Builds, cleans, audits and analyzes spreadsheets with formulas, tables, charts, summaries, forecasts and defensible calculations.

### 9. `presentation-builder`
Turns an objective and source material into a coherent presentation with narrative, slide hierarchy, evidence, speaker logic and professional visual structure.

### 10. `project-coordinator`
Maintains plans, owners, dependencies, milestones, blockers, status, action items and follow-ups across multi-person work.

### 11. `stakeholder-follow-up`
Tracks promises, unanswered questions, approvals, waiting items and decisions so work does not silently stall between people.

### 12. `quality-control-review`
Reviews finished work from the perspective of the intended audience and checks accuracy, completeness, consistency, presentation and delivery readiness.

---

## B. Executive, Business and Strategy

### 13. `market-research-analyst`
Maps a market, customer segment or industry and turns fragmented information into usable commercial intelligence.

### 14. `competitor-intelligence`
Tracks competitors, positioning, products, pricing, campaigns, launches, messaging and strategic changes and explains what they mean for the company.

### 15. `customer-insight-synthesis`
Combines reviews, interviews, support tickets, sales notes, analytics and research into customer pains, jobs, objections, needs and opportunities.

### 16. `business-case-builder`
Evaluates a proposed initiative using expected value, costs, assumptions, risks, alternatives, operational consequences and success criteria.

### 17. `strategy-planner`
Turns an objective into strategic choices, priorities, sequencing, trade-offs, milestones and measurable outcomes.

### 18. `product-positioning`
Defines audience, problem, promise, differentiation, proof, objections and messaging so a product is easy to understand and sell.

### 19. `pricing-packaging`
Analyzes pricing, plans, bundles, unit economics, competitors and willingness-to-pay signals to propose clear packaging options.

### 20. `kpi-performance-review`
Reads operational and business metrics, explains movement, isolates likely drivers and produces management-ready performance reviews.

---

## C. Marketing, Growth and Social Media

### 21. `marketing-strategy`
Builds a practical marketing strategy around audience, positioning, channels, offers, content, funnel stages, budget and measurement.

### 22. `campaign-planner`
Turns a campaign objective into the creative brief, assets, channel plan, timeline, audience variants, approvals, launch checklist and measurement plan.

### 23. `brand-voice-guardian`
Learns and enforces a brand's vocabulary, tone, claims, style, do-not-say rules and personality across generated content.

### 24. `content-strategy`
Designs content pillars, formats, series, distribution logic and repurposing systems around business goals rather than posting for its own sake.

### 25. `social-media-manager`
Runs the operational social workflow from content selection through platform adaptation, scheduling, publishing, engagement and performance review.

### 26. `social-content-calendar`
Builds realistic multi-platform content calendars with campaign context, production requirements, publication timing and repurposing logic.

### 27. `social-copywriter`
Creates platform-native hooks, captions, posts, CTAs, titles, descriptions and variations that respect the brand and the actual content.

### 28. `trend-culture-radar`
Tracks emerging formats, conversations, memes, platform behavior, creative patterns and cultural moments and identifies relevant opportunities without blindly trend-chasing.

### 29. `community-manager`
Monitors community conversation, answers common questions, surfaces issues, identifies advocates and keeps discussions useful and on-brand.

### 30. `creator-influencer-outreach`
Finds relevant creators or partners, evaluates fit, personalizes outreach and manages collaboration follow-up.

### 31. `email-marketing`
Creates newsletters, broadcasts, sequences and lifecycle emails with segmentation, subject lines, message logic, CTAs and performance iteration.

### 32. `marketing-performance-analyst`
Combines channel metrics into a useful explanation of what is working, what is wasting effort and what should change next.

---

## D. Creative Direction and Design

### 33. `creative-director`
Turns a business or storytelling objective into a coherent creative direction and keeps multiple outputs visually and conceptually aligned.

### 34. `creative-ideation`
Generates and develops genuinely different concepts using useful creative methods instead of producing minor variations of the first idea.

### 35. `visual-design`
Creates professional visual compositions for social posts, ads, covers, posters, documents, presentations and digital assets using hierarchy, typography, layout and brand constraints.

### 36. `brand-identity-builder`
Develops or extends visual identity systems including typography, palette, graphic language, image treatment, layout rules and reusable design tokens.

### 37. `ad-creative-builder`
Develops advertising concepts and production-ready variants around hooks, value propositions, proof, visual metaphors, formats and audience segments.

### 38. `image-generation-director`
Converts creative intent into strong image-generation workflows, reference strategies, prompt systems, continuity controls, selection criteria and iteration loops.

### 39. `image-editing-retouch`
Plans and executes practical image edits such as cleanup, compositing, background replacement, object changes, retouching, resizing and campaign adaptation.

### 40. `design-qc`
Critiques design work for hierarchy, spacing, typography, alignment, brand consistency, legibility, format safety and overall professional finish.

---

## E. Film, Video, Audio and Production

### 41. `producer`
Turns a creative objective into a workable production plan covering scope, people, budget, assets, schedule, dependencies, risks and delivery.

### 42. `preproduction-planner`
Builds the practical pre-production package: creative brief, shot requirements, locations, cast, props, references, schedule, asset checklist and production dependencies.

### 43. `scriptwriter`
Writes scripts for ads, social videos, explainers, short films, branded content, narration and other formats with appropriate structure, pacing and tone.

### 44. `storyboard-shot-planner`
Converts a script or concept into a coherent shot sequence with framing, action, continuity, transitions, coverage and reference-image requirements.

### 45. `cinematography-director`
Plans camera language, lenses, lighting, composition, movement, coverage, visual continuity and image references appropriate to the story and production constraints.

### 46. `production-coordinator`
Creates and maintains call sheets, schedules, shot lists, asset lists, crew needs, logistics, dependencies and day-of-production information.

### 47. `post-production-supervisor`
Plans and coordinates edit, VFX, motion graphics, color, audio, subtitles, reviews, versioning, approvals, masters and delivery requirements.

### 48. `video-editor`
Builds or directs edits around story, rhythm, performance, continuity, music, sound, graphics, platform format and the intended audience response.

### 49. `motion-graphics`
Designs and produces titles, lower thirds, kinetic typography, graphic animation, UI motion, explainers and branded motion systems.

### 50. `color-grading`
Analyzes and directs exposure, balance, shot matching, look development, skin treatment and delivery-safe grading across a sequence.

### 51. `sound-design-audio-post`
Plans and executes dialogue cleanup, sound effects, ambience, transitions, mix priorities, loudness and final audio delivery.

### 52. `ai-video-generation-director`
Builds image-to-video and text-to-video production workflows with reference selection, shot prompts, continuity, motion control, iteration and final assembly in mind.

---

## F. Sales, CRM, Accounts, Support and Commerce

### 53. `lead-research-qualification`
Researches prospects and accounts, evaluates fit and produces concise reasons to pursue, deprioritize or personalize the approach.

### 54. `sales-outreach`
Writes and manages personalized prospecting across email, LinkedIn and other channels without reducing outreach to generic templates.

### 55. `proposal-pitch-builder`
Creates proposals, scopes, pitch decks and commercial narratives tailored to the customer's problem, context, objections and buying criteria.

### 56. `crm-pipeline-manager`
Maintains clean opportunity state, next actions, notes, stages, follow-ups, forecast signals and stale-deal warnings in the CRM.

### 57. `account-manager`
Maintains client context, commitments, deliverables, risks, opportunities, communication history and renewal/expansion follow-up.

### 58. `customer-support`
Resolves customer questions using product knowledge and account context, escalates correctly and turns recurring problems into useful feedback.

### 59. `customer-success`
Supports onboarding, adoption, value realization, health monitoring, renewals and intervention when a customer is drifting or blocked.

### 60. `ecommerce-merchandising`
Maintains product listings, collections, descriptions, imagery, promotions, merchandising logic and storefront quality across an ecommerce operation.

---

## G. Finance and Business Administration

### 61. `fp-and-a-analyst`
Analyzes revenue, costs, margins, variance, runway and operating performance and converts the numbers into management-relevant explanations.

### 62. `financial-modeling`
Builds auditable financial models for scenarios, valuations, investments, business plans and operating decisions using explicit assumptions.

### 63. `budget-forecasting`
Builds and maintains budgets and forecasts, compares actuals to plan and explains material deviations.

### 64. `bookkeeping-reconciliation`
Supports categorization, reconciliation, exception detection and financial record cleanup while keeping an auditable trail.

### 65. `invoice-billing`
Prepares, tracks and reconciles invoices, payment status, billing schedules, supporting documentation and follow-up.

### 66. `expense-procurement`
Processes expense information, compares vendor options, organizes approvals and maintains purchase documentation and spend visibility.

### 67. `commercial-contract-summary`
Extracts commercial obligations, dates, payment terms, deliverables, renewal conditions and operational risks from agreements for business review, without pretending to replace legal counsel.

### 68. `travel-event-coordinator`
Researches and organizes travel, meetings, shoots, events and offsites around schedule, budget, logistics, participants and contingency needs.

---

## H. Research, Data and Knowledge Work

### 69. `research-analyst`
Takes a business question, gathers the relevant evidence and turns it into a structured answer, landscape, report or recommendation using the deeper research foundation underneath it.

### 70. `fact-checker-source-verifier`
Verifies important claims against primary or high-quality sources, flags uncertainty and distinguishes evidence from inference.

### 71. `data-cleaning-analysis`
Turns messy CSV, spreadsheet or exported operational data into a clean analyzable dataset and produces useful findings rather than only charts.

### 72. `survey-feedback-analysis`
Analyzes surveys, reviews, interviews, comments and qualitative feedback to identify themes, sentiment, recurring problems and actionable insights.

### 73. `document-intelligence`
Extracts, compares, classifies and structures information from reports, contracts, PDFs, decks, forms, transcripts and document collections.

### 74. `knowledge-base-curator`
Turns useful company knowledge into discoverable, deduplicated, current documentation and identifies stale or contradictory material.

---

## I. People and Operations

### 75. `recruiter-hiring-coordinator`
Supports role definition, candidate research, screening, interview preparation, scheduling, candidate communication and hiring pipeline organization.

### 76. `employee-onboarding`
Builds role-aware onboarding plans, setup checklists, reading paths, introductions, training tasks and first-week/first-month milestones.

### 77. `sop-process-builder`
Observes or analyzes how work is actually done and converts it into concise, maintainable SOPs, checklists and operational playbooks.

### 78. `operations-manager`
Tracks recurring business operations, handoffs, queues, deadlines, bottlenecks, capacity and exceptions across teams.

### 79. `vendor-procurement-manager`
Researches vendors, compares offers, organizes requirements and quotations, tracks approvals and maintains supplier follow-up.

### 80. `risk-issue-manager`
Maintains a live view of operational risks, issues, blockers, mitigations, owners, escalation thresholds and unresolved decisions.

---

# The original 20 are still useful, but move underneath

The earlier list is now treated as the Machine / Reliability Foundation:

- semantic-codebase-sweep
- root-cause-debugger
- transactional-refactor
- verification-harness
- deep-research-synthesis
- browser-workflow-operator
- api-integration-engineer
- git-change-lifecycle
- dependency-supply-chain-audit
- environment-doctor
- database-migration-guardian
- incident-forensics
- structured-ingestion-normalization
- knowledge-writeback
- delegation-orchestrator
- release-deploy-guard
- change-review
- configuration-contract-doctor
- skill-forge
- skill-miner

These capabilities make other skills safer and stronger. They should not dominate the user's perception of the agent.

Examples:

- `research-analyst` can compose `deep-research-synthesis`.
- `quality-control-review` can compose `verification-harness`.
- `project-coordinator` can compose `delegation-orchestrator`.
- `knowledge-base-curator` can compose `knowledge-writeback`.
- `social-media-manager` can compose `browser-workflow-operator` when no direct API exists.
- `ecommerce-merchandising` can compose `api-integration-engineer` when adapting to an unfamiliar commerce platform.

This is the correct relationship: **employee skills describe the job; foundation skills make execution reliable.**

---

# App and software mastery packs

A company-ready agent must know how to operate software, not just understand the job conceptually.

These should be a separate class of skill called **Operator Packs**. The business capability remains application-independent; the operator pack teaches execution in a particular product.

Initial high-value operator packs should include:

## Office and collaboration

- `google-workspace-operator` — Gmail, Calendar, Drive, Docs, Sheets, Slides.
- `microsoft-365-operator` — Outlook, Calendar, OneDrive, Word, Excel, PowerPoint, Teams.
- `slack-operator`
- `microsoft-teams-operator`
- `notion-operator`
- `airtable-operator`
- `asana-operator`
- `clickup-operator`
- `monday-operator`
- `trello-operator`

## Creative and design

- `canva-operator`
- `figma-operator`
- `photoshop-operator`
- `illustrator-operator`
- `indesign-operator`

## Film and post production

- `premiere-pro-operator`
- `after-effects-operator`
- `davinci-resolve-operator`
- `capcut-operator`
- `frameio-operator`

## Sales, marketing and commerce

- `hubspot-operator`
- `salesforce-operator`
- `mailchimp-operator`
- `klaviyo-operator`
- `shopify-operator`
- `wordpress-operator`
- `webflow-operator`
- `meta-business-suite-operator`
- `youtube-studio-operator`
- `tiktok-studio-operator`
- `linkedin-operator`

## Finance and administration

- `quickbooks-operator`
- `xero-operator`
- `stripe-operator`

Operator packs can use direct APIs, MCP/connectors, local application automation, browser automation or computer-use depending on what the runtime grants. The skill does not grant itself access.

---

# Role bundles: how the agent becomes an employee instantly

The agent should not require the user to know which ten skills to invoke. A **role bundle** is a thin composition layer that preloads or prioritizes the relevant capabilities for a job without creating a new monolithic persona prompt.

Examples:

### Executive Assistant

`company-onboarding` + `work-triage` + `executive-briefing` + `meeting-operator` + `inbox-operator` + `stakeholder-follow-up` + `travel-event-coordinator` + office operator pack.

### Marketing Manager

`marketing-strategy` + `campaign-planner` + `brand-voice-guardian` + `content-strategy` + `marketing-performance-analyst` + `market-research-analyst` + relevant marketing operator packs.

### Social Media Manager

`social-media-manager` + `social-content-calendar` + `social-copywriter` + `trend-culture-radar` + `community-manager` + `creative-director` + `visual-design` + `video-editor` + social platform operator packs.

### Creative Director

`creative-director` + `creative-ideation` + `brand-identity-builder` + `visual-design` + `ad-creative-builder` + `image-generation-director` + `design-qc` + Canva/Figma/Adobe operator packs.

### Film Producer

`producer` + `preproduction-planner` + `scriptwriter` + `storyboard-shot-planner` + `production-coordinator` + `post-production-supervisor` + `project-coordinator` + `risk-issue-manager`.

### Post Producer

`post-production-supervisor` + `video-editor` + `motion-graphics` + `color-grading` + `sound-design-audio-post` + `quality-control-review` + Frame.io/Resolve/Premiere/After Effects operator packs.

### Sales Representative

`lead-research-qualification` + `sales-outreach` + `proposal-pitch-builder` + `crm-pipeline-manager` + `meeting-operator` + `stakeholder-follow-up` + CRM operator pack.

### Account Manager

`account-manager` + `meeting-operator` + `stakeholder-follow-up` + `project-coordinator` + `customer-insight-synthesis` + `risk-issue-manager` + CRM/office operator packs.

### Finance Analyst

`fp-and-a-analyst` + `financial-modeling` + `budget-forecasting` + `spreadsheet-analyst` + `kpi-performance-review` + finance operator pack.

### Research Analyst

`research-analyst` + `fact-checker-source-verifier` + `document-intelligence` + `data-cleaning-analysis` + `presentation-builder` + `executive-briefing`.

### Customer Support Agent

`company-onboarding` + `customer-support` + `inbox-operator` + `knowledge-base-curator` + `customer-insight-synthesis` + support/CRM operator pack.

### Operations Coordinator

`work-triage` + `project-coordinator` + `operations-manager` + `sop-process-builder` + `risk-issue-manager` + `stakeholder-follow-up` + project-management operator pack.

---

# Important design distinction

AI-Verse should model four different things separately:

1. **Capability skill** — knows how to do a class of professional work.
2. **Operator pack** — knows how to execute that work inside specific software.
3. **Role bundle** — selects a useful combination for a job.
4. **Runtime permission** — determines what the agent is actually allowed to access or change.

Do not collapse these into one giant prompt.

A social-media manager should understand content strategy even when Buffer is unavailable. A Canva operator should know Canva without pretending to be a creative director. A role bundle should combine both when appropriate. And neither should be able to give itself credentials or cross workspace boundaries.

---

# Day-Zero shipping recommendation

The repository can ultimately contain all 80 employee skills, but the first implementation wave should optimize the feeling of breadth.

A strong initial build order would be:

### Wave E0: make it feel like an employee

- company-onboarding
- work-triage
- executive-briefing
- meeting-operator
- inbox-operator
- professional-writing
- document-builder
- spreadsheet-analyst
- presentation-builder
- project-coordinator
- research-analyst
- fact-checker-source-verifier

### Wave E1: make it commercially useful

- marketing-strategy
- campaign-planner
- brand-voice-guardian
- content-strategy
- social-media-manager
- social-content-calendar
- social-copywriter
- marketing-performance-analyst
- lead-research-qualification
- sales-outreach
- proposal-pitch-builder
- crm-pipeline-manager

### Wave E2: make it creatively exceptional

- creative-director
- creative-ideation
- visual-design
- ad-creative-builder
- image-generation-director
- image-editing-retouch
- producer
- preproduction-planner
- scriptwriter
- storyboard-shot-planner
- post-production-supervisor
- video-editor
- ai-video-generation-director

### Wave E3: make it operationally complete

- customer-support
- customer-success
- fp-and-a-analyst
- financial-modeling
- budget-forecasting
- data-cleaning-analysis
- document-intelligence
- recruiter-hiring-coordinator
- employee-onboarding
- sop-process-builder
- operations-manager
- vendor-procurement-manager

Then continue through the remaining first-party employee skills and operator packs.

---

# Success test

The success criterion for AI-Verse-Skills should not be:

> Can the agent use many tools?

It should be:

> If this agent joined a real company this morning and was given the same apps, files, permissions and instructions as a capable new employee, how many useful jobs could it begin performing before lunch?

That is the Day-Zero standard.