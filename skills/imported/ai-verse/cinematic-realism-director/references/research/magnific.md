# Phase 1 Research - Magnific Cinematic

Status: RESEARCH EVIDENCE

Primary classification: `PROVIDER-SPECIFIC`, with live schema facts marked `CONFIRMED`.

This file records what is publicly/documentably knowable about Magnific's cinematic image workflow. It does not claim knowledge of private weights, private training data, hidden system prompts, proprietary fine-tuning, or undisclosed prompt-rewrite logic.

## Why Magnific Matters to This Skill

Magnific's current Cinematic product exposes a unusually explicit cinematography control ontology. That makes it valuable as evidence for **which creative dimensions deserve first-class representation** in a model-independent cinematic director.

The key lesson is not to copy Magnific's labels blindly. The lesson is that cinematic control becomes more reliable when camera/capture, optics, framing, lighting, film/tonal response, motion signature, and texture are represented as separate decisions rather than one vague `cinematic` style word.

## Current Live Cinematic Model Surface

Source: `MAG-001` and `MAG-002` in `../source-ledger.md`.

Observed on 2026-10-03 through Magnific's connected first-party model/settings schemas:

- model name: Cinematic;
- image model family surfaced as Imagen-family;
- output resolutions: 1K, 2K, 4K;
- aspect ratios include square, widescreen/cinema, landscape, portrait, and common photographic formats;
- supports image, character, and product references;
- exposes a `cinematicControls` settings layer.

These are current product facts, not assumptions about Magnific's underlying model architecture.

## Exposed Control Ontology

### Camera / capture references

Current choices include:

- ARRI ALEXA 35;
- ARRI ALEXA Mini LF;
- Sony VENICE;
- Sony VENICE 2;
- RED V-RAPTOR;
- Canon C500 Mark II;
- Sony FX9;
- Blackmagic URSA Mini Pro;
- IMAX 70mm;
- medium format;
- 35mm film;
- 8mm film;
- VHS camcorder;
- Pixelvision;
- Auto.

**Research interpretation:** the category deliberately mixes literal camera bodies, capture formats, film/video media, and lo-fi acquisition references. Therefore our universal schema should not force all of these into a single literal `camera_body` field. Later ontology work should separate:

- capture format/media;
- camera-system reference;
- capture character;
- intentionally degraded/legacy acquisition character.

### Lens family / lens reference

Current choices include:

- Panavision G-Series;
- ZEISS Master;
- Cooke S4;
- Cooke Panchro;
- ARRI Signature;
- Canon K35;
- Leica Summilux;
- ZEISS Distagon;
- Contax G;
- Hasselblad Planar;
- Pentax 67;
- Mamiya Sekor;
- Cooke S4 35mm;
- ZEISS Master Prime 50mm;
- Leica Summilux-C 75mm;
- Cooke Anamorphic/i 40mm;
- Hawk V-Lite 65mm anamorphic;
- Angenieux Optimo 25-250mm;
- Auto.

**Research interpretation:** Magnific allows both family-level and exact focal/lens references. Our skill should likewise allow an expert to lock an exact reference while beginner AUTO may choose only the observable lens behavior needed for the story.

### Focal length

Exposed values:

`14mm, 24mm, 35mm, 50mm, 85mm, 135mm, 200mm, Auto`

This reinforces focal length as a separate control from lens family.

### Aperture

Exposed values:

`f/1.2, f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, f/16, Auto`

This reinforces aperture/depth behavior as a separate decision rather than simply asking for `bokeh`.

### Shot type / camera viewpoint

Current schema includes combinations of:

- extreme close, close, medium, three-quarter, long and wide framing;
- front, 45-degree and profile orientations;
- over-shoulder;
- back;
- POV;
- high angle;
- low angle;
- Dutch angle;
- bird's-eye;
- worm's-eye.

**Research interpretation:** Magnific's single `shotType` field actually combines multiple concepts. Our schema should decompose them into at least:

- shot size;
- camera angle/elevation;
- subject orientation;
- POV/OTS relationship;
- camera height/distance where relevant.

This allows more precise expert locks and prevents conflicting compound labels.

### Film-stock references

Current controls include motion, still-photo, reversal, B&W, instant, and consumer emulsions, including:

- Kodak VISION3 500T and 250D;
- Kodak Portra 400/800;
- Kodak Gold 200;
- Kodak Ektar 100;
- Kodak Tri-X 400;
- Kodak T-MAX 400;
- CineStill 800T;
- Fuji Pro 400H, Superia 400, Velvia 50, Provia 100F;
- Ilford Delta 3200;
- Ektachrome E100;
- Lomography 800;
- Agfa Vista 400;
- Polaroid 600.

**Research interpretation:** a stock token is being used as a visual prior. Our skill should map a named stock to observable tendencies when evidence exists, but never claim a provider is performing a literal physical emulsion simulation.

### Movie / filmmaker look references

The product exposes named film and filmmaker look presets alongside a `documentary-natural` option.

**Research interpretation:** these are provider-level convenience presets, not a universal cinematography ontology. The core skill should prefer decomposition into observable traits such as palette, density, lighting, framing, contrast, texture, production design, and optical behavior. Named-film/style references belong only in adapters or user-requested style matching, with copyright/style safety rules applied separately.

### Lighting

Current choices cover:

- time/environment: golden hour, blue hour, overcast, hard sunlight, moonlight;
- portrait patterns: Rembrandt, butterfly, loop, split, broad, short;
- exposure/contrast families: high-key, low-key, silhouette, chiaroscuro;
- source/placement concepts: rim, backlight, three-point, natural window, candle, neon, stage, practical, overhead, bounce, contre-jour;
- atmosphere/modifier concepts: volumetric, dappled;
- studio modifiers: studio soft, beauty dish, parabolic.

**Research interpretation:** one provider menu merges source motivation, pattern, time of day, modifier, direction, and contrast strategy. Our skill should decompose those dimensions so combinations remain physically coherent.

### Motion blur

Current options include:

- none;
- subtle/moderate/heavy cinematic;
- subject-only motion blur;
- camera-only motion blur;
- rack-focus/pull blur;
- zoom blur;
- long-exposure light trails.

**Research interpretation:** motion signature belongs in still-image cinematography even when full temporal video direction is out of scope. Later rules should distinguish subject motion, camera motion and shutter/exposure effects.

### Grain

Current options include:

- 35mm silver-halide;
- 16mm coarse;
- fine organic sensor noise;
- barely visible shadow grain.

**Research interpretation:** grain should have type, scale/coarseness, placement/visibility, and strength rather than a binary film-grain switch.

### Halation

Current options include:

- none;
- warm orange-red halo;
- strong warm bloom;
- green-yellow fringe.

**Research interpretation:** halation and bloom must remain separate concepts in our knowledge base. A provider may combine them in presets, but the skill should use them only when visually justified.

### Tonal look

Current options include:

- Kodak VISION3 500T;
- Fujifilm ETERNA 500;
- Kodak Portra 400;
- Kodak Double-X;
- ARRI ALEXA natural;
- Sony VENICE natural.

**Research interpretation:** tonal response is distinct from the initial camera/lens selection. This supports a separate layer for:

- highlight rolloff;
- shadow density/detail;
- saturation behavior;
- color separation;
- overall contrast curve;
- grain/texture.

## Image Editing and Reality-Repair Evidence

Sources: `MAG-003`, `MAG-004`, `MAG-005`.

Magnific exposes several distinct operations relevant to Reality Repair rather than treating every correction as a full re-generation:

- image editing/retouching;
- restyling;
- camera-change operations;
- skin enhancement;
- relighting;
- image reimagination/re-rendering with controllable drift;
- structure-preserving reimagination options;
- creative upscaling/detail synthesis;
- grain/skin/detail/lighting/realism-oriented enhancement controls.

The connected reimagination schema explicitly distinguishes how far a new take may drift and can preserve layout via structure/depth guidance.

**Architectural lesson:** Reality Repair should choose the smallest appropriate operation. It should not automatically regenerate an entire scene when the defect is local or when composition/identity/product geometry is preservation-locked.

## Relighting Evidence

Magnific's official relight workflow exposes light direction/position/elevation, color and intensity, supports multiple lights, and can use lighting references.

**Architectural lesson:** our lighting model should not be a list of aesthetic labels alone. It needs explicit dimensions for:

- motivated source;
- direction/position;
- apparent source size/softness;
- intensity/exposure relationship;
- color temperature/tint;
- fill/negative fill;
- practicals and ambient contribution;
- atmosphere.

## What We Can Legitimately Learn from Magnific

Strong evidence supports these product-design conclusions:

1. Separate cinematography controls outperform one undifferentiated `cinematic` style switch as an interface/ontology.
2. Camera reference, lens family, focal length and aperture deserve separate representation.
3. Shot geometry deserves more structure than generic composition adjectives.
4. Lighting needs its own structured system.
5. Film/tonal response, grain and halation are separate from optics.
6. Motion signature can matter in a still frame.
7. Reality repair benefits from preservation-aware edit operations instead of full-scene regeneration.
8. Beginner AUTO and expert manual control can coexist because every control may remain automatic until explicitly locked.

## What We Must NOT Claim

Do not state or imply that we know:

- Magnific's private base-model weights;
- training datasets;
- private fine-tunes;
- private LoRAs;
- hidden system prompts;
- exact prompt-enhancement strings;
- internal weighting of controls;
- whether a named camera/lens control corresponds to literal optical simulation versus learned visual conditioning;
- exact private post-processing chain.

## Requirements Carried Forward

Later phases should preserve these Magnific-inspired but model-independent capabilities:

- AUTO plus manual locks;
- explicit capture system;
- lens family/character;
- focal length;
- aperture/depth;
- shot geometry;
- lighting motivation and geometry;
- film/tonal response;
- grain;
- halation/bloom restraint;
- motion/shutter signature;
- preservation-aware repair;
- provider adapter translating the universal shot spec into Magnific's actual current controls when Magnific is the chosen provider.

This research file is not itself a Magnific adapter. The adapter will be built later from current verified controls and must be rechecked for schema drift.