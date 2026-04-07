# MERCHANT-Special-Offers-Dic25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` para Special Offers de diciembre 2025.

## Status

- `exacto`

## Payload

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H06",
  "body": ["B40", "B41", "B42", "B43", "B44", "B45", "B46", "B47"],
  "footer": "F07"
}
```

Tambien se puede componer desde modulo 1 usando `group: "MERCHANT - Socio"` y `campaignType: "special-offers"` cuando el input apunte a esta pieza.

## Contrato de edicion

- Mantener el orden `H06 -> B40 -> B41 -> B42 -> B43 -> B44 -> B45 -> B46 -> B47 -> F07`.
- El contenido editable vive en snippets dedicados de Special Offers. No editar snippets genericos `hb16.html`, `hb08.html`, `im03.html`, `tm04.html`, `fm05.html`, `fm02.html`, `fm03.html` ni `fm04.html` para cambios de esta campana.
- Si cambian beneficios o CTAs, actualizar tambien disclaimers y legales en la misma pasada.
- El footer `F07` combina dos bloques `FM05` dedicados antes del legal final; no simplificar esa secuencia porque rompe fidelidad exacta.
- Preservar tokens Marigold como `{(FULLNAME)}`, `{(EMAIL)}` y `{(URLSignature1)}` en los snippets donde ya existen.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H06` | Preheader + brand panel Special Offers | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-special-offers-dic25.html` |
| `B40` | Hero principal Special Offers | `catalog/snippets/marigold-v4.2/hb16-merchant-special-offers-dic25.html` |
| `B41` | Bloque wine | `catalog/snippets/marigold-v4.2/hb08-merchant-special-offers-dic25-wine.html` |
| `B42` | Bloque winestore | `catalog/snippets/marigold-v4.2/hb08-merchant-special-offers-dic25-winestore.html` |
| `B43` | Grilla Ninja + Samsung | `catalog/snippets/marigold-v4.2/im03-merchant-special-offers-dic25-ninja-samsung.html` |
| `B44` | Grilla Gadnic + Whirlpool | `catalog/snippets/marigold-v4.2/im03-merchant-special-offers-dic25-gadnic-whirlpool.html` |
| `B45` | Grilla Garmin + Hisense | `catalog/snippets/marigold-v4.2/im03-merchant-special-offers-dic25-garmin-hisense.html` |
| `B46` | CTA final | `catalog/snippets/marigold-v4.2/tm04-merchant-special-offers-dic25-cta.html` |
| `B47` | Disclaimer final | `catalog/snippets/marigold-v4.2/tm04-merchant-special-offers-dic25-disclaimer.html` |
| `F07` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05-merchant-special-offers-dic25-foodies.html`, `catalog/snippets/marigold-v4.2/fm05-merchant-special-offers-dic25-tagline.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-special-offers-dic25.html`, `catalog/snippets/marigold-v4.2/fm03.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-special-offers-dic25.html` |
