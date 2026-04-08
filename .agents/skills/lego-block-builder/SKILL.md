---
name: lego-block-builder
description: "Use when the exact campaign router returned no match and visual_blocks are available. Reconstructs a /api/compose-email payload by matching PDF zones to reusable component blocks from docs/componentes/README.md without looking up any specific campaign."
---

# Lego Block Builder

## Overview

Use this skill when the exact campaign router did not find a documented campaign and the upstream node delivered `visual_blocks` — a pre-parsed list of visual zones extracted from the PDF.

The goal is to reconstruct a valid `/api/compose-email` payload by treating the email as a set of reusable component blocks ("fichas"), not by identifying a specific campaign.

Do **not** read `docs/campanas/README.md` or any `docs/campanas/*.md` file. Do **not** look for a campaign name. Only use `docs/componentes/README.md` as the reference catalog.

## Inputs To Read First

1. `docs/componentes/README.md` — the only reference catalog for this skill.
2. The `visual_blocks` JSON passed from the upstream node. Each block has `block_type`, `layout_signature`, `text`, `images`, `y_start`, and `y_end`.

## Workflow

1. Read `docs/componentes/README.md` fully before processing any block.
2. Determine `templateFamily`:
   - Use `marigold-v4.2` for standard AMEX Argentina light-background emails.
   - If the design is dark / black background (Centurion style), return `lower_html_flow` — centurion-1.0 is not in phase 1.
3. Process `visual_blocks` in order of `block_index`:
   - Use the **Tabla de decisión rápida** in the catalog as a starting point.
   - Confirm the match by checking `layout_signature` fields and `text` patterns documented in the component entry.
   - Assign a per-block `confidence` (0.0–1.0) based on how many signals match.
4. For each matched component, extract `props` from `text` and `images`:
   - URLs come from `images[N].src`.
   - Text values come from `text` (normalize whitespace and OCR noise).
   - Do not invent prop values. If a required prop cannot be extracted, lower the block confidence.
   - Preserve personalization tokens: `{(FULLNAME)}`, `{(EMAIL)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}`, `{(URLSignature1)}`.
5. Handle `brand_closing` blocks: absorb the tagline image URL into the footer component as `taglineDesktopUrl`. Do not create a separate body component for it.
6. Calculate overall `confidence` as a weighted average of per-block confidence scores. Weight header and footer at 1.0×, hero at 1.0×, each benefit block at 0.8×.
7. Apply confidence routing rules:
   - `confidence < 0.60` → `flow_route: lower_html_flow`, omit `api`.
   - `0.60 ≤ confidence < 0.80` → `flow_route: lego_compose_email`, `review_required: true`.
   - `confidence ≥ 0.80` → `flow_route: lego_compose_email`, `review_required: false`.

## Compose Payload Rules

- Use `id`, never `componentId`.
- Do not include `role`, `snippet`, or any documentation-only field in the payload sent to `/api/compose-email`.
- Valid component forms: `"B28"` (string) or `{ "id": "B28", "props": { ... } }` (object).
- Use object form whenever you have at least one prop to pass.
- Always include `"globals": { "includeSeparators": false }`.
- Do not call `/api/compose-email`. Only build and return the payload.

## Output Format

```json
{
  "flow_route": "lego_compose_email",
  "api": {
    "templateFamily": "marigold-v4.2",
    "header": { "id": "H04", "props": {} },
    "body": [
      { "id": "B28", "props": { "heroImageUrl": "https://...", "headlineHtml": "Un mes para sorprender" } },
      { "id": "B29", "props": { "introHtml": "Elegí los regalos para esas personas especiales..." } },
      { "id": "B30", "props": { "dateLabel": "Del 11 al 13 de diciembre", "primaryLogoAlt": "GIESSO", "ctaLabel": "Conocé más" } }
    ],
    "footer": {
      "id": "F05",
      "props": {
        "taglineDesktopUrl": "https://...",
        "legalHtml": "..."
      }
    },
    "globals": { "includeSeparators": false }
  },
  "confidence": 0.75,
  "review_required": true,
  "matched_campaign": "",
  "matched_blocks": [
    {
      "pdf_block": "header (block_index 1)",
      "component_id": "H04",
      "slot": "header",
      "confidence": 0.95,
      "reason": "has_preheader, has_account_data, has_greeting, has_login_button all true; PUBLICIDAD and FULLNAME in text"
    },
    {
      "pdf_block": "hero (block_index 2)",
      "component_id": "B28",
      "slot": "body",
      "confidence": 0.90,
      "reason": "has_large_image true, columns 1, has_cta false, single wide image, short headline text"
    }
  ],
  "missing_blocks": [],
  "notes": []
}
```

If `flow_route` is `lower_html_flow`, omit the `api` key entirely:

```json
{
  "flow_route": "lower_html_flow",
  "confidence": 0.45,
  "review_required": true,
  "matched_campaign": "",
  "matched_blocks": [],
  "missing_blocks": ["benefit (block_index 4) — could not identify component with sufficient confidence"],
  "notes": ["Benefit block has columns:1 and image_count:12 — no catalog entry matches this layout"]
}
```

## Confidence Reference

| Score | Meaning |
|---|---|
| 0.90–1.00 | All `layout_signature` signals match + text patterns confirmed |
| 0.75–0.89 | Most signals match; 1–2 signals missing or ambiguous |
| 0.60–0.74 | Partial match; block_type matches but layout details unclear |
| < 0.60 | Cannot identify component with reasonable certainty |

## Done Criteria

- `templateFamily` is selected and justified.
- Every `visual_block` is either matched to a component, absorbed into another (brand_closing → footer), or listed in `missing_blocks`.
- All matched components have at least `id` in their object form.
- Props only contain values extracted from `visual_blocks` or default tokens — no invented values.
- `confidence` and `review_required` are set according to the routing rules.
- The output JSON is valid and matches the format above.
