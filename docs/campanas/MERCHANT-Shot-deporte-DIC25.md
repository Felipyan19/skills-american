# MERCHANT-Shot-deporte-DIC25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` para el Shot Deporte de diciembre 2025.

## Payload

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H04",
  "body": ["B28", "B29", "B30", "B31", "B32"],
  "footer": "F05",
  "globals": {
    "includeSeparators": false
  }
}
```

Tambien se puede componer por ejemplo desde modulo 1 usando `group: "MERCHANT - Socio"` y `campaignType: "shot-deporte"` si no hay otra entrada que genere ambiguedad.

## Contrato de edicion

- Mantener el orden `H04 -> B28 -> B29 -> B30 -> B31 -> B32 -> F05`.
- No activar separadores automaticos; los bloques ya incluyen sus propios fondos, bordes y paddings.
- El contenido editable esta en snippets dedicados de Shot Deporte. No editar los snippets genericos `hb18.html`, `tm04.html`, `hb08.html`, `fm05.html`, `fm02.html` ni `fm04.html` para cambios de esta campana.
- Si se cambian descuentos, cuotas o comercios, actualizar cuerpo y legales en la misma pasada.
- Las imagenes usan el prefijo `101225-MERCHANT-Shot-deporte-DIC25_`. Si se reemplazan assets, conservar dimensiones y `alt` equivalentes.
- El footer `F05` usa snippets dedicados y no depende de `legalHtml` por props.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H04` | Preheader + brand panel | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-shot-deporte-dic25.html` |
| `B28` | Hero energia | `catalog/snippets/marigold-v4.2/hb18-merchant-shot-deporte-dic25.html` |
| `B29` | Intro entrenamiento | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-intro.html` |
| `B30` | Megatlon + Fiter | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-clubs.html` |
| `B31` | Decathlon + Lasaigues Padel | `catalog/snippets/marigold-v4.2/hb08-merchant-shot-deporte-dic25.html` |
| `B32` | Closing oscuro | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-closing.html` |
| `F05` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05-merchant-shot-deporte-dic25.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-shot-deporte-dic25.html`, `catalog/snippets/marigold-v4.2/fm03.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-shot-deporte-dic25.html` |

## Checklist antes de cerrar

- Verificar CTAs de Megatlon/Fiter, Decathlon y Lasaigues.
- Verificar que los indicadores legales `(1)` a `(3)` correspondan con el footer.
- Probar `POST /api/compose-email?html` con el payload de arriba.
- Revisar el `manifest.expanded` para confirmar que la secuencia mantenga los snippets dedicados.
