# MERCHANT-Shot-Travel-Agst25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` y snippets hardcodeados para reproducir la pieza de Travel de agosto 2025.

## Payload

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H02",
  "body": ["B12", "B13", "B14", "B15", "B17", "B16"],
  "footer": "F03",
  "globals": {
    "includeSeparators": false
  }
}
```

Tambien se puede componer por ejemplo desde modulo 1 usando `group: "MERCHANT - Socio"` y `campaignType: "shot-travel"` si no hay otra entrada que genere ambiguedad.

## Contrato de edicion

- Mantener el orden `H02 -> B12 -> B13 -> B14 -> B15 -> B17 -> B16 -> F03`.
- No activar separadores automaticos; los bloques ya traen fondos, bordes y padding propios.
- El contenido editable esta en los snippets dedicados de Travel. No editar `hb18.html`, `tm04.html`, `tm03.html` ni `fm04.html` genericos para cambios de esta campana.
- Si se cambian fechas, descuentos o comercios, actualizar cuerpo y legales en la misma pasada.
- Las imagenes usan el prefijo `1908-MERCHANT-Shot-Travel-Agst25_`. Si se reemplazan assets, conservar dimensiones y `alt` equivalentes.
- El footer `F03` usa legales hardcodeados; no depende de `legalHtml` por props.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H02` | Preheader + brand panel | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-shot-travel-agst25.html` |
| `B12` | Hero Travel | `catalog/snippets/marigold-v4.2/hb18-merchant-shot-travel-agst25.html` |
| `B13` | Agencias | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-agencias.html` |
| `B14` | Compras | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-compras.html` |
| `B15` | Spa | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-spa.html` |
| `B17` | Hoteles triptico | `catalog/snippets/marigold-v4.2/tm03-merchant-shot-travel-agst25.html` |
| `B16` | Cierre hashtag | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-hashtag.html` |
| `F03` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05.html`, `catalog/snippets/marigold-v4.2/fm02.html`, `catalog/snippets/marigold-v4.2/fm03.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-shot-travel-agst25.html` |

## Checklist antes de cerrar

- Verificar CTAs de Aerolineas, Despegar, Al Mundo, Samsonite, Delsey, Equipaje Urbano, Spa y hoteles.
- Verificar que los indicadores legales `(1)` a `(7)` correspondan con el footer.
- Probar `POST /api/compose-email?html` con el payload de arriba.
- Revisar el `manifest.expanded` para confirmar que la secuencia mantenga los snippets dedicados.
