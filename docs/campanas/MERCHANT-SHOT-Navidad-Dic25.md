# MERCHANT-SHOT-Navidad-Dic25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` para el Shot de Navidad diciembre 2025.

## Status

- `exacto`

## Payload

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H05",
  "body": ["B33", "B34", "B35", "B36", "B37", "B38", "B39"],
  "footer": "F06"
}
```

Tambien se puede componer desde modulo 1 usando `group: "MERCHANT - Socio"` y `campaignType: "shot-navidad"` cuando el input apunte a esta pieza.

## Contrato de edicion

- Mantener el orden `H05 -> B33 -> B34 -> B35 -> B36 -> B37 -> B38 -> B39 -> F06`.
- El contenido editable vive en snippets dedicados de Shot Navidad. No editar snippets genericos `hb18.html`, `tm01.html`, `tm04.html`, `hb08.html`, `fm05.html`, `fm02.html`, `fm03.html` ni `fm04.html` para cambios de esta campana.
- Si cambian descuentos, cuotas o comercios, actualizar cuerpo y legales en la misma pasada.
- El footer `F06` usa legales hardcodeados del set de Navidad; no depende de `legalHtml` por props.
- Preservar tokens Marigold como `{(FULLNAME)}`, `{(EMAIL)}` y `{(URLSignature1)}` en los snippets donde ya existen.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H05` | Preheader + brand panel Navidad | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-shot-navidad-dic25.html` |
| `B33` | Hero Shot Navidad | `catalog/snippets/marigold-v4.2/hb18-merchant-shot-navidad-dic25.html` |
| `B34` | Intro principal | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-navidad-dic25-intro.html` |
| `B35` | Header Indumentaria | `catalog/snippets/marigold-v4.2/tm01-merchant-shot-navidad-dic25-indumentaria.html` |
| `B36` | Beneficios Indumentaria | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-navidad-dic25-indumentaria.html` |
| `B37` | Beneficios Perfumeria | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-navidad-dic25-perfumeria.html` |
| `B38` | Modulo 50/50 comercios | `catalog/snippets/marigold-v4.2/hb08-merchant-shot-navidad-dic25.html` |
| `B39` | Cierre Shot Navidad | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-navidad-dic25-closing.html` |
| `F06` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05-merchant-shot-navidad-dic25.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-shot-navidad-dic25.html`, `catalog/snippets/marigold-v4.2/fm03-merchant-shot-navidad-dic25.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-shot-navidad-dic25.html` |

## Checklist antes de cerrar

- Verificar coherencia entre claims del cuerpo y referencias legales en footer.
- Probar `POST /api/compose-email?html` con el payload de arriba.
- Revisar `manifest.expanded` para confirmar la secuencia exacta de `sourceId`.
