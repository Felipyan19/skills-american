---
name: exact-campaign-md
description: Use when creating or updating docs/campanas/*.md for exact-status campaign templates that need short payloads, group/campaignType payloads, editable props variants, and a detailed payload that reproduces the short version exactly.
---

# Exact Campaign MD

## Overview

Use this skill to document an exact campaign API contract in `docs/campanas/*.md`.
The expected outcome is a reusable MD with short examples, editable examples, and a fully detailed component-by-component payload whose defaults render the same HTML as the short payload.

## Workflow

1. Identify the target campaign doc in `docs/campanas/` and read `docs/campanas/README.md` to confirm its group, campaign type, and exact-status expectations.
2. If the router says `sin doc`, the dashboard status is `pendiente`, or no exact row is convincing, switch to `.agents/skills/generic-campaign-fallback/SKILL.md` and `docs/campanas/generic.md` before falling back to broader segment docs.
3. Read the target `.md`, the component definitions in `server/registry.py`, and the referenced snippets under `catalog/snippets/<templateFamily>/`.
4. For every header, body, and footer component in the campaign, identify editable fields:
   - Text and HTML copy.
   - Image URLs and alt text.
   - CTA URLs and labels.
   - Social/nav links.
   - Legal/disclaimer HTML.
   - Account, greeting, preheader, or member labels when the header owns them.
5. If code changes are required, make campaign-specific snippets dynamic with `{{placeholder}}` values and put the current exact values into `defaults` in `server/registry.py`.
6. Avoid changing generic shared snippets for campaign-specific behavior. Prefer creating or using a dedicated campaign snippet key in `registry.py` when only one exact campaign needs different placeholders.
7. If using `group` plus `campaignType`, verify the server can merge `header`, `body`, `footer`, and `globals` overrides onto the looked-up example payload.
8. Update the campaign `.md` with the required sections below.
9. Validate the JSON blocks and render equivalence before finishing.

## Required MD Sections

For an exact campaign that is not dynamic yet and only needs a basic routing contract, use a minimal doc with:

- `Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.`
- `Payload base`
- `Payload por grupo y tipo`
- `Mapa de componentes`

Do not include dynamic markers such as `Edicion version corta`, `Edicion corta desde tipo de campana y grupo`, or `Campos de variantes` unless those props are actually implemented in snippets and `server/registry.py`.

The campaign doc should include a `Payloads de uso` section with these examples, in this order:

Before `Payloads de uso`, include a short status line when variants are supported:

```text
Status API: `dinamico`. `H04`, `B28` and `F05` accept variants by `props`.
```

1. `Version corta`
   - Explicit compact payload with string component IDs.
   - Example shape:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H04",
  "body": [
    "B28",
    "B29",
    "B30",
    "B31",
    "B32"
  ],
  "footer": "F05",
  "globals": {
    "includeSeparators": false
  }
}
```

2. `Edicion version corta`
   - Explicit payload where any editable component can become `{ "id": "...", "props": { ... } }`.
   - Include realistic edits for header, at least one body component, and footer when those are dynamic.
   - Leave unchanged components as strings to demonstrate mixed compact/detailed usage.

3. `Version corta desde tipo de campana y grupo`
   - Payload using lookup fields only:

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-deporte"
}
```

4. `Edicion corta desde tipo de campana y grupo`
   - Payload using `group` and `campaignType` plus only the components that are being edited.
   - Demonstrate that partial overrides keep the base component order and defaults.

5. `Detallada`
   - Full payload where header, every body component, and footer are represented as objects with `id` and every default `props` value.
   - This payload must render the same HTML as `Version corta`.
   - Use the exact values from `server/registry.py`, not approximations.

Also keep or add these sections when useful:

- `Contrato de edicion`: explain that `props` are merged over registry defaults.
- `Mapa de componentes`: list header, body, and footer IDs with snippet filenames.
- `Campos de variantes`: table of each component and its supported props.

Do not add QA/process notes, test plans, checklists, or agent-facing validation sections to campaign MDs. Keep validation steps in your own execution and final response, not in the campaign contract.

## Rules For Defaults And Variants

- The `/api/compose-email` component contract is strict: use `id`, never `componentId`.
- Do not include documentation-only fields such as `role` or `snippet` in the final compose payload. Use those only in tables or analysis, not in JSON examples sent to the API.
- Preserve all exact default values in `server/registry.py` so the short payload remains unchanged.
- Preserve personalization tokens such as `{(FULLNAME)}`, `{(EMAIL)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}`, `{(URLSignature1)}`, and similar Marigold placeholders.
- Preserve `globals.includeSeparators: false` when the exact campaign requires no separators.
- Keep legal and disclaimer fields editable, but make sure example edits do not contradict the offers shown elsewhere in the same payload.
- Use HTML entities consistently with the existing snippets and registry defaults.
- Do not invent props that are not implemented in snippets and registry defaults.
- Do not leave unresolved `{{placeholder}}` strings in rendered output.

## Validation

Run the narrowest useful checks:

- Docs-only change: parse all JSON code blocks in the target `.md` and check that the detailed payload renders exactly like the short payload.
- Code or registry change: also run `python -m unittest tests.test_composer tests.test_http_api`.

Useful validation pattern:

```python
import json
import re
from pathlib import Path

from server.composer import compose_email

doc = Path("docs/campanas/MERCHANT-Shot-deporte-DIC25.md").read_text(encoding="utf-8")
blocks = re.findall(r"```json\n(.*?)\n```", doc, flags=re.S)
payloads = [json.loads(block) for block in blocks]

short_payload = payloads[0]
detailed_payload = payloads[-1]

short_html = compose_email(short_payload)["html"]
detailed_html = compose_email(detailed_payload)["html"]

assert short_html == detailed_html
assert "{{" not in detailed_html
assert "}}" not in detailed_html
print(f"{len(payloads)} json blocks ok")
```

When the doc contains editable examples, also render those examples and assert a custom string or URL appears in the result.
