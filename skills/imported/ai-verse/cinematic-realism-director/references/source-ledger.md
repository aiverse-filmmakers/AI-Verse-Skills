# Cinematic Realism Director - Source Ledger

Status: PHASE 1 RESEARCH RECORD

This file is the provenance backbone for the Cinematic Realism Director. It records where important technical and provider-specific knowledge came from, how strongly it should be trusted, and how it may be used later in the runtime knowledge base.

The ledger is evidence, not a dump of source text. Runtime references must synthesize concise original rules from these sources rather than copying substantial copyrighted material.

## Evidence Classes

Use these labels consistently:

### CONFIRMED

A factual claim directly supported by a first-party manufacturer, official provider documentation, official API/schema, standards/physics source, or another authoritative primary source.

Use for:

- documented camera specifications;
- documented lens design/behavior statements;
- documented film-stock characteristics;
- documented provider controls/capabilities;
- current exposed model schemas.

### CORROBORATED

A claim supported by multiple credible sources or by a primary source plus strong practitioner/technical evidence, but not stated as a single precise first-party fact.

Use for:

- practical optical character where manufacturer language and cinematographer experience agree;
- visual tendencies that are repeatable but not a literal measured specification.

### MODEL-BEHAVIOR

An empirically useful image-generation prompting/editing behavior. This is not a statement about real optical physics.

Use for:

- natural-language prompt structures;
- preservation wording for edits;
- model-specific negative-prompt behavior;
- reference-image handling;
- provider routing or version-specific prompt conventions.

### PROVIDER-SPECIFIC

A behavior, control, feature, limitation, or product concept tied to one named AI provider/product.

Use for:

- Magnific Cinematic control vocabulary;
- Soul Cinema routing;
- Cinema Studio control surfaces;
- provider-specific image sizes, modes, or adapters.

### INFERRED

A reasonable synthesis or visual inference that is not directly stated by a primary source.

Use sparingly. An inferred statement must never be presented as a confirmed hardware fact.

## Source Priority

When sources disagree, use this priority unless stronger contrary evidence exists:

1. current first-party technical documentation or live official schema;
2. current official product documentation;
3. manufacturer whitepaper/data sheet;
4. official engineering article/interview;
5. multiple credible technical/practitioner sources;
6. official public skill/CLI package describing provider behavior;
7. third-party public implementation;
8. community anecdote.

A lower-priority source may reveal a research lead, but it does not override a stronger source without explicit evidence.

## Time Sensitivity Rule

Provider behavior is volatile. Entries describing AI models, schemas, UI controls, product versions, routing, quality tiers, or APIs must carry a retrieval date and should be rechecked before release if they materially affect an adapter.

Physical camera/lens/film references are more stable, but product pages may still change.

## Copyright and Licensing Rule

- Record facts, concepts, and concise original summaries.
- Do not copy long provider docs, manuals, skill bodies, blog passages, or proprietary prompt text into this package.
- Public source availability does not mean public-domain copyright status.
- Third-party skills may inspire architecture or empirical tests, but their prose is not copied into the Cinematic Realism Director.
- No private model weights, private training data, hidden system prompts, confidential prompt enhancers, or non-public trade secrets are claimed or used.

## Core Ledger

Retrieval date for Phase 1 unless otherwise noted: **2026-10-03**.

| ID | Source | Authority | Class | Supports | Notes |
| --- | --- | --- | --- | --- | --- |
| MAG-001 | Magnific live `Cinematic` image-model schema exposed through the connected Magnific product | Magnific first-party live schema | CONFIRMED / PROVIDER-SPECIFIC | Current Cinematic model support, resolutions, aspect ratios, references, `cinematicControls` | Treat as current product surface, not private implementation |
| MAG-002 | Magnific live `cinematicControls` settings schema | Magnific first-party live schema | CONFIRMED / PROVIDER-SPECIFIC | Camera, lens, focal, aperture, shot, film-stock, movie-look, lighting, blur, grain, halation, tonal-look ontology | Strong blueprint for control taxonomy only |
| MAG-003 | https://www.magnific.com/ai/docs/image-editor | Magnific official docs | CONFIRMED / PROVIDER-SPECIFIC | Editor operations such as retouch, restyle, camera changes, skin/adjustment workflow | Product behavior can change |
| MAG-004 | https://www.magnific.com/ai/docs/relight | Magnific official docs | CONFIRMED / PROVIDER-SPECIFIC | Relighting controls and multi-light/reference-light concepts | Use as provider behavior, not universal light physics |
| MAG-005 | Connected Magnific tool schemas for reimagine/upscale/skin-enhancement workflows | Magnific first-party live schema | CONFIRMED / PROVIDER-SPECIFIC | Structure preservation, creative/resemblance controls, film/photography optimization, grain/skin/realism enhancement concepts | Do not expose internal IDs or claim algorithm internals |
| HIG-001 | https://higgsfield.ai/blog/how-we-built-cinema-studio | Higgsfield official engineering blog | CONFIRMED / PROVIDER-SPECIFIC | Technical camera/optics/light vocabulary, DP/operator testing, lens-character amplification, prompt enhancement, equipment-package philosophy | Key architectural source |
| HIG-002 | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images | Higgsfield official help | CONFIRMED / PROVIDER-SPECIFIC | Soul family, Soul Cinema, Soul HEX, Soul ID relationships and image workflow | Recheck current model names before adapter release |
| HIG-003 | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character | Higgsfield official help | CONFIRMED / PROVIDER-SPECIFIC | Soul ID identity-consistency workflow | Identity feature, not optical physics |
| HIG-004 | https://higgsfield.ai/blog/soul-cinema-preview | Higgsfield official product blog | CONFIRMED / PROVIDER-SPECIFIC | Soul Cinema positioning around texture, depth, grain, natural/spontaneous photographic character | Marketing wording must not be treated as measured physics |
| HIG-005 | https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-cinema-studio | Higgsfield official help | CONFIRMED / PROVIDER-SPECIFIC | Cinema Studio camera/lens/aperture/light/color/reference controls | Version-sensitive |
| HIG-006 | https://higgsfield.ai/blog/cinema-studio-4-0 | Higgsfield official product blog | CONFIRMED / PROVIDER-SPECIFIC | Optical-character-at-generation approach, camera/aperture/movement/era concepts | Version-sensitive |
| HIG-007 | https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/SKILL.md | Higgsfield official public GitHub | CONFIRMED / PROVIDER-SPECIFIC / MODEL-BEHAVIOR | Current public agent routing, Soul Cinema selection, quality/routing conventions | Architecture/provider routing only, not physical truth |
| CAM-ARRI-001 | https://www.arri.com/en/camera-systems/cameras/alexa-35 | ARRI first-party | CONFIRMED | ALEXA 35 latitude, sensitivity, REVEAL, camera positioning | Current product facts |
| CAM-ARRI-002 | https://www.arri.com/en/learn-help/learn-help-camera-system/image-science/reveal-color-science | ARRI first-party technical | CONFIRMED | REVEAL color science, LogC4/AWG4 color handling, highlight/color behavior | Core camera-color reference |
| CAM-ARRI-003 | https://www.arri.com/en/learn-help/learn-help-camera-system/image-science/log-c | ARRI first-party technical | CONFIRMED | Log capture principles and ARRI log pipeline | Do not conflate log encoding with final display look |
| CAM-SONY-001 | https://pro.sony/en_CO/products/digital-cinema-cameras/venice2 | Sony first-party | CONFIRMED | VENICE 2 sensor options, dual-base ISO, latitude/color/capture characteristics | Regional page URL, facts cross-check before release if page changes |
| CAM-RED-001 | https://docs.red.com/955-0199/955-0199_V1.2_Rev_A_RED_PS_V-RAPTOR_Operation_Guide/Content/C_TechSpecs/Specs_V-RAPTOR.htm | RED first-party technical | CONFIRMED | V-RAPTOR 8K VV sensor dimensions and documented dynamic-range claim | Distinguish manufacturer claim from independent measurement |
| CAM-RED-002 | https://docs.red.com/955-0225/955-0225_V2.0%20Rev-A%20RED%20PS%2C%20V-RAPTOR%20%5BX%5D%208K%20VV%20Operation%20Guide/Content/B_TechSpecs/Specs_V-RAPTOR%20%5BX%5D.htm | RED first-party technical | CONFIRMED | V-RAPTOR [X] global-shutter/current specs | Current model differs from original V-RAPTOR |
| CAM-CANON-001 | https://downloads.canon.com/nw/learn/white-papers/cinema-eos/EOS_C500_MarkII_White_Paper.pdf | Canon first-party whitepaper | CONFIRMED | Canon Log 2/3, Cinema Gamut, dynamic-range claims | Primary C500 II technical source |
| CAM-BMD-001 | https://www.blackmagicdesign.com/products/blackmagicursaminipro | Blackmagic Design first-party | CONFIRMED | URSA Mini Pro family, dynamic range, sensor/color-science positioning | Model variants differ |
| CAM-BMD-002 | https://www.blackmagicdesign.com/nz/products/blackmagicursaminipro/blackmagicraw | Blackmagic Design first-party | CONFIRMED | Generation 5 color-science and BRAW pipeline concepts | Useful for color-response reference |
| LEN-ARRI-001 | https://www.arri.com/en/cine-lenses/signature-lenses/signature-primes-zooms/signature-primes | ARRI first-party | CONFIRMED | Signature Prime skin rendering, shadows/blacks, bokeh, flare, distortion/CA statements | Translate marketing language cautiously into observable traits |
| LEN-PAN-001 | https://www.panavision.com/camera-and-optics/optics/product-detail/g-g-series | Panavision first-party | CONFIRMED | G-Series anamorphic contrast/resolution, aberration balance, breathing, squeeze behavior | Strong anamorphic source |
| LEN-COOKE-001 | https://cookeoptics.com/lens/panchro-classic-i-s35/ | Cooke first-party | CONFIRMED | Panchro Classic specifications and classic-look positioning | Manufacturer source |
| LEN-COOKE-002 | https://cookeoptics.com/news-and-events/recreating-the-panchro-look/ | Cooke official engineering/history article | CONFIRMED / CORROBORATED | Coating/internal reflection and lower-contrast/falloff explanation | Especially useful for observable behavior |
| LEN-COOKE-003 | https://cookeoptics.com/news-and-events/cooke-at-cannes-2025/ | Cooke official publication quoting cinematographers | CORROBORATED | Practitioner descriptions of S4-type skin/falloff/flare/texture | Testimony, not lab measurement |
| LEN-ZEISS-001 | https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/supreme-prime-lenses.html | ZEISS first-party | CONFIRMED | Supreme Prime focus falloff, bokeh, sharpness/skin positioning | Translate to visual tendencies |
| LEN-ZEISS-002 | https://www.zeiss.com/photonics-and-optics/en/cinematography/lenses/supreme-prime-radiance-lenses.html | ZEISS first-party | CONFIRMED | Controlled flare, warmth and contrast positioning | Radiance differs from standard Supreme |
| LEN-HAWK-001 | https://www.vantagefilm.com/en/products/hawk-anamorphic-lenses/v-lite | Vantage/Hawk first-party | CONFIRMED | V-Lite anamorphic family characteristics | Primary Hawk source |
| LEN-HAWK-002 | https://www.vantagefilm.com/en/products/hawk-1-3x/v-lite | Vantage/Hawk first-party | CONFIRMED | 1.3x anamorphic squeeze/use of sensor area | Technical behavior |
| LEN-ANG-001 | https://www.angenieux.com/lenses/legacy-series/long-lens-zoom-optimo-style-25-250/ | Angenieux first-party | CONFIRMED | Optimo Style 25-250 aperture/focus/breathing/distortion/color statements | Legacy product but useful lens-family reference |
| LEN-CANON-001 | https://downloads.canon.com/nw/camera/downloads/brochures/cinema/cinema-lenses/sumire-prime-film-and-digital-times-report.pdf | Canon first-party/historical brochure | CONFIRMED for historical specs only | Canon K35 focal/T-stop history and production context | Insufficient alone for a detailed K35 optical-look profile |
| FILM-KODAK-001 | https://www.kodak.com/en/motion/product/camera-films/500t-5219-7219 | Kodak first-party | CONFIRMED | VISION3 500T tungsten balance, low-light/shadow-grain/highlight-latitude positioning | Primary motion stock source |
| FILM-KODAK-002 | https://www.kodak.com/en/motion/product/camera-films/250d-5207-7207/ | Kodak first-party | CONFIRMED | VISION3 250D daylight balance, highlight latitude, shadow grain | Primary motion stock source |
| FILM-KODAK-003 | https://www.kodak.com/en/motion/product/camera-films/eastman-double-x-black-white-5222-7222/features/ | Kodak first-party | CONFIRMED | DOUBLE-X B&W stock and tonal/lighting role | Primary motion stock source |
| FILM-KODAK-004 | https://www.kodak.com/en/motion/blog-post/malcolm-marie/ | Kodak official production article | CORROBORATED | DP testimony about DOUBLE-X contrast/grain relative to 500T | Practitioner comparison, not universal measurement |
| FILM-KODAK-005 | https://www.kodak.com/content/products-brochures/motion-picture/KODAK-EKTACHROME-100D-5294-7294-technical-information.pdf | Kodak first-party technical | CONFIRMED | EKTACHROME 100D daylight balance, saturation, skin/neutral rendering, sharpness/grain | Reversal stock distinct from negative |
| FILM-KODAK-006 | https://www.kodak.com/en/motion/products/camera-films/ | Kodak first-party catalog | CONFIRMED | Current motion-stock family roles | Catalog/index source |
| FILM-KODAK-007 | https://www.kodak.com/global/plugins/acrobat/en/professional/products/films/2012Brochure.pdf | Kodak first-party brochure | CONFIRMED for documented photo-stock traits | Portra/Ektar/T-MAX documented positioning | Older document, use cautiously and only for stable emulsion-family traits |
| LIGHT-001 | https://www.bhphotovideo.com/explora/photography/tips-and-solutions/how-to-achieve-soft-light-for-portraits | B&H technical education | CORROBORATED | Apparent source size/distance and shadow softness | Good educational source, not manufacturer physics spec |
| LIGHT-002 | https://medium.com/aputure/lit-by-aputure-marshall-adams-asc-better-call-saul-50d2cf378910 | Aputure official publication / cinematographer interview | CORROBORATED | Negative fill, controlling environmental bounce, practical cinematography workflow | Practitioner evidence |
| COLOR-ARRI-001 | ARRI REVEAL source CAM-ARRI-002 | ARRI first-party | CONFIRMED | Color space/log/display-transform concepts and highlight/saturated-color handling | Reused source ID relationship |
| COLOR-BMD-001 | https://www.blackmagicdesign.com/products/davinciresolve/color | Blackmagic Design first-party | CONFIRMED | Lift/gamma/gain, log/HDR wheels, saturation/temp/tint, scopes/color management | Color-workflow reference |
| COLOR-BMD-002 | https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-18-Colorist-Guide.pdf | Blackmagic Design official training guide | CONFIRMED / CORROBORATED | Natural-skin grading discipline, hue/saturation/contrast workflow | Older Resolve version but foundational principles stable |
| COLOR-FL-001 | https://www.filmlight.ltd.uk/customers/meet-the-colourist/andreas_brueckl.php | FilmLight practitioner interview | CORROBORATED | Highlight rolloff, skin, midtone contrast, shadow distribution, dense-black practice | Practitioner workflow, not universal law |
| MODEL-OAI-001 | https://developers.openai.com/api/docs/guides/image-prompting | OpenAI first-party docs | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Current image prompt/edit guidance, structured description and preservation | Recheck before adapter release |
| MODEL-OAI-002 | https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide | OpenAI first-party cookbook | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Detailed edit preservation, reference roles, realistic materials/light instructions | Cookbook guidance, not physics source |
| MODEL-GOOG-001 | https://ai.google.dev/gemini-api/docs/image-generation | Google first-party docs | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Gemini image generation/editing, descriptive cinematic language, iterative editing | Recheck active model names at adapter release |
| MODEL-SEED-001 | https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite | ByteDance Seed first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Seedream 5.0 Lite reasoning, style/color transfer, editing capability | Current provider behavior |
| MODEL-SEED-002 | https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro | ByteDance Seed first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Seedream 5.0 Pro instruction alignment, structure/coherence, professional visual tasks | Current provider behavior |
| MODEL-SEED-003 | https://seed.bytedance.com/en/seedream5_0_pro | ByteDance Seed first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Current Seedream product capability summary | Version-sensitive |
| MODEL-BFL-001 | https://help.bfl.ai/articles/4292391522-what-is-flux-2 | Black Forest Labs first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | FLUX.2 generation/editing/multi-reference role | Current product docs |
| MODEL-BFL-002 | https://help.bfl.ai/articles/7734566352-does-flux-2-support-negative-prompting | Black Forest Labs first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | FLUX.2 positive-description preference/no negative prompting | Important adapter constraint |
| MODEL-BFL-003 | https://bfl.ai/models/flux-kontext | Black Forest Labs first-party | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Kontext image editing, consistency, local edits/reference style | Older/specialized relative to FLUX.2; keep version distinction |
| SEC-001 | https://github.com/fal-ai-community/skills/blob/main/skills/cinematography/SKILL.md | fal.ai community public skill | MODEL-BEHAVIOR / secondary | Prompt-architecture ideas and quality checks | Secondary only; independently validate technical claims |
| SEC-002 | https://github.com/replicate/skills/blob/main/skills/prompt-images/SKILL.md | Replicate public skill | MODEL-BEHAVIOR / secondary | Natural-language prompting, preservation wording, iteration/model-selection practices | Secondary empirical guidance |
| SEC-003 | https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/skills/higgsfield-cinema/SKILL.md | Third-party public skill | PROVIDER-SPECIFIC / secondary | Higgsfield workflow/UI/API leads and version-specific cross-checks | Never authoritative over Higgsfield official docs/schema |

## Known Source Gaps at Phase 1 Start

These are deliberately not filled with guesses:

- a sufficiently strong first-party IMAX 65/70mm image-character reference for the exact behaviors we want to encode;
- a current first-party Leitz/Leica Summilux-C optical-character page with enough usable detail;
- a strong first-party ZEISS/ARRI Master Prime optical-character source in the current web corpus;
- a first-party detailed Canon K35 optical-character explanation beyond historical specifications;
- a first-party current Fuji motion-stock source for discontinued ETERNA-style characteristics;
- authoritative measured cross-system comparisons that would justify saying one digital camera body inherently has a precise aesthetic over another after normalization;
- any private Magnific/Higgsfield weights, training datasets, hidden system prompts, or proprietary enhancer prompts. These are outside scope and must remain outside scope.

The formal gap audit at Task 1.11 determines which gaps must be resolved before V1 and which can safely remain represented as unknown or lower-confidence.