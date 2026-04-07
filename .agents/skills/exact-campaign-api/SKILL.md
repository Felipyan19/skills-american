---
name: exact-campaign-api
description: "Use when making an exact-status campaign dynamic in the email API: implementing component props variants from docs/campanas/*.md by updating registry defaults, snippets, group/campaignType payload merging, and tests so short and detailed payloads render correctly."
---

# Exact Campaign API

## Overview

Use this skill when a campaign doc describes editable variants and the API must actually support them.
The goal is to make an exact campaign render from compact payloads, partial `props` overrides, and full detailed payloads without changing the base output.

Use `exact-campaign-md` separately when the requested work is only to write or normalize the `.md` documentation.

## Inputs To Read First

1. Target doc in `docs/campanas/*.md`.
2. `docs/campanas/README.md` for the campaign `group`, `campaignType`, fidelity/status, and expected component order.
3. `server/registry.py` for component IDs, snippet keys, and defaults.
4. `server/composer.py` for the component request contract.
5. `server/http_server.py` for `/api/compose-email` and `group` plus `campaignType` resolution.
6. Referenced files in `catalog/snippets/<templateFamily>/`.

## Implementation Workflow

1. Confirm the base payload renders before editing:
   - Use the `.md` `Version corta` payload, or the example payload referenced by `group` and `campaignType`.
   - Save the expected component order mentally: header, body list, footer.
2. For each component in header, body, and footer:
   - Locate its `registry.py` entry.
   - Locate every snippet listed in `snippet_keys`.
   - Identify text, image URLs, image alts, CTAs, social/nav URLs, legal copy, and personalization labels that should vary.
3. Convert hardcoded exact values into snippet placeholders:
   - Replace only the fields that are intended to vary.
   - Use clear prop names such as `heroImageUrl`, `headlineHtml`, `ctaUrl`, `ctaLabel`, `legalHtml`.
   - Preserve Marigold tokens like `{(FULLNAME)}`, `{(EMAIL)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}`, and `{(URLSignature1)}`.
4. Add the current exact values as `defaults` in `server/registry.py`.
   - The compact payload must still render exactly the same output after the change.
   - Do not add props that are not used by snippets.
5. Avoid changing generic shared snippets for campaign-specific variants.
   - If a shared snippet needs campaign-only placeholders, copy it into a dedicated campaign snippet file and register a dedicated snippet key.
6. Ensure API payload forms work:
   - Explicit compact:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H04",
  "body": ["B28", "B29"],
  "footer": "F05"
}
```

   - Explicit partial variants:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": { "id": "H04", "props": { "greetingText": "Hola Test" } },
  "body": [
    { "id": "B28", "props": { "headlineHtml": "Texto test" } },
    "B29"
  ],
  "footer": { "id": "F05", "props": { "legalHtml": "Legal test" } }
}
```

   - Group/campaign partial variants:

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-deporte",
  "body": [
    { "id": "B28", "props": { "headlineHtml": "Texto test" } }
  ]
}
```

7. If `group` plus `campaignType` does not preserve base components while applying overrides, update `server/http_server.py` to merge:
   - `header` override over base header.
   - `body` overrides by component ID over the base body order.
   - `footer` override over base footer.
   - `globals` as a shallow merge.
8. Update or add tests.
   - Composer test: compact output still works, props variants appear, and rendered HTML has no unresolved `{{` or `}}`.
   - HTTP API test: `group` plus `campaignType` accepts partial component overrides and preserves the rest of the campaign.
   - If a detailed payload exists in the doc, test or script-check that it renders the same as the short payload.

## Validation

Run focused checks before finishing:

```bash
python -m unittest tests.test_composer tests.test_http_api
```

For the target `.md`, parse JSON blocks and compare short vs detailed output:

```python
import json
import re
from pathlib import Path

from server.composer import compose_email

doc = Path("docs/campanas/MERCHANT-Shot-deporte-DIC25.md").read_text(encoding="utf-8")
payloads = [json.loads(block) for block in re.findall(r"```json\n(.*?)\n```", doc, flags=re.S)]

assert compose_email(payloads[0])["html"] == compose_email(payloads[-1])["html"]
for payload in payloads:
    html = compose_email(payload)["html"]
    assert "{{" not in html
    assert "}}" not in html
```

Also run `git diff --check` on touched files when snippets or docs were edited.

## Done Criteria

- Compact payload renders unchanged.
- Detailed payload renders the same HTML as compact payload.
- Each documented prop is implemented in snippets and defaults.
- Each snippet placeholder has a default value.
- Partial `props` overrides work for header, body, and footer where documented.
- `group` plus `campaignType` partial overrides work if the doc advertises them.
- Tests pass, or any skipped validation is explicitly reported.
