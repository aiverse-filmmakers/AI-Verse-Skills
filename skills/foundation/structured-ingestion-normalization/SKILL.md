---
name: structured-ingestion-normalization
description: "Convert messy documents, webpages, files, logs, or datasets into structured data while preserving provenance and uncertainty."
version: 1.0.0
metadata:
  ai-verse:
    foundation: true
    ownership: core
---

# Structured Ingestion Normalization

## Procedure
1. Define target schema, identifiers, required fields, validation rules, and provenance fields.
2. Inventory source formats and prefer deterministic parsers before model extraction.
3. Extract in bounded chunks while preserving source locations/raw references.
4. Normalize types, units, dates, entities, and missing-value conventions without inventing data.
5. Validate schema, duplicates, coverage, and representative samples.

## Constraints
- Ambiguous/missing values remain distinguishable from known values.
- Normalization must not silently alter semantic meaning.

## Verification
Every normalized record can be traced to source evidence and schema/coverage failures are reported.
