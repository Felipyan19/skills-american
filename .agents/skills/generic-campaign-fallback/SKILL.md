---
name: generic-campaign-fallback
description: Use when reconstructing a pending or unrecognized campaign for /api/compose-email. Choose the nearest valid payload from docs/campanas/generic.md and catalog/examples/module1.md by group, campaignType, templateFamily, and visual rhythm instead of leaving the campaign unmatched.
---

# Generic Campaign Fallback

Use this skill when `docs/campanas/README.md` points to `sin doc`, the dashboard status is `pendiente`, or no exact router row is convincing enough.

## Workflow

1. Read `docs/campanas/generic.md`.
2. Read only the candidate examples named there inside `catalog/examples/module1.md`.
3. Reuse the closest valid payload. Do not invent component IDs.
4. Set `matched_campaign` to the example you actually cloned. Do not leave it empty.
5. Use `confidence = "estructural"` when the fallback keeps the same group or family with public components only.
6. Use `confidence = "aproximada"` only when the chosen example is already marked as approximate or the catalog documents substitutions.
7. Keep `needs_snippet_edit = false` unless exact fidelity would require a non-public snippet or an unsupported prop.
8. Put the fallback rationale inside `notes`, not outside the JSON.
