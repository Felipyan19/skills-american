# MERCHANT-Newsletter-Dic25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` para el newsletter de diciembre con secciones Compras, Gastronomia y Hoteles.

## Payload

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H03",
  "body": ["B18", "B19", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27"],
  "footer": "F04",
  "globals": {
    "includeSeparators": false
  }
}
```

Tambien se puede componer por ejemplo desde modulo 1 usando `group: "MERCHANT - Socio"` y `campaignType: "newsletter"` si no hay otra entrada que genere ambiguedad.

## Contrato de edicion

- Mantener el orden `H03 -> B18 -> B19 -> B20 -> B21 -> B22 -> B23 -> B24 -> B25 -> B26 -> B27 -> F04`.
- No activar separadores automaticos; el newsletter ya define su ritmo con headers azules, grillas y bloques de cierre.
- El HTML de referencia incluye un `HB08` vacio usado como espaciador. No existe como componente publico separado en la API actual; no agregarlo salvo que se cree un snippet dedicado.
- El contenido editable esta en snippets dedicados del Newsletter Dic25. No editar los snippets genericos `hb03.html`, `tm01.html`, `tm04.html`, `hb08.html` ni `fm04.html` para cambios de esta campana.
- Si cambia un beneficio, revisar claim visual, CTA y legal asociado en `F04`.
- El footer `F04` usa legales hardcodeados; no depende de `legalHtml` por props.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H03` | Preheader + brand panel | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-newsletter-dic25.html` |
| `B18` | Hero Diciembre | `catalog/snippets/marigold-v4.2/hb03-merchant-newsletter-dic25.html` |
| `B19` | Intro 1 al 31 de diciembre | `catalog/snippets/marigold-v4.2/tm04-merchant-newsletter-dic25-intro.html` |
| `B20` | Header Compras | `catalog/snippets/marigold-v4.2/tm01-merchant-newsletter-dic25-compras.html` |
| `B21` | Beneficios Compras | `catalog/snippets/marigold-v4.2/hb08-merchant-newsletter-dic25-compras.html` |
| `B22` | Header Gastronomia | `catalog/snippets/marigold-v4.2/tm01-merchant-newsletter-dic25-gastronomia.html` |
| `B23` | Beneficios Gastronomia | `catalog/snippets/marigold-v4.2/hb08-merchant-newsletter-dic25-gastronomia.html` |
| `B24` | Header Hoteles | `catalog/snippets/marigold-v4.2/tm01-merchant-newsletter-dic25-hoteles.html` |
| `B25` | Beneficio Hotel principal | `catalog/snippets/marigold-v4.2/tm04-merchant-newsletter-dic25-hoteles.html` |
| `B26` | Beneficios Hoteles 50/50 | `catalog/snippets/marigold-v4.2/hb08-merchant-newsletter-dic25-hoteles.html` |
| `B27` | CTA final | `catalog/snippets/marigold-v4.2/tm04-merchant-newsletter-dic25-cta.html` |
| `F04` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-newsletter-dic25.html`, `catalog/snippets/marigold-v4.2/fm03.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-newsletter-dic25.html` |
