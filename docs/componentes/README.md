# Catálogo Lego de Componentes

Este archivo es el punto de entrada para el agente `lego-block-builder`. No mapea campañas: mapea fichas reutilizables a señales visuales detectables en `visual_blocks`.

Cada sección documenta: para qué sirve el componente, cómo reconocerlo en `visual_blocks` usando `block_type`, `layout_signature`, y `text`, y qué `props` acepta.

---

## Guía de lectura para el agente

El nodo anterior entrega una lista de `visual_blocks`. Cada bloque tiene:

```json
{
  "block_index": 1,
  "y_start": 0.0,
  "y_end": 7.89,
  "block_type": "header",
  "text": "PUBLICIDAD Hola ((FULLNAME)) Tu cuenta termina en Mi cuenta",
  "images": [
    { "src": "https://...", "top": 2.4, "left": 20.53, "width": 2.58, "height": 2.58 }
  ],
  "layout_signature": {
    "columns": 2,
    "image_count": 3,
    "max_image_width": 3.88,
    "has_large_image": false,
    "has_preheader": true,
    "has_account_data": true,
    "has_greeting": true,
    "has_login_button": true,
    "has_cta": false,
    "has_discount": false,
    "has_installments": false,
    "has_footer_nav": false,
    "has_legal": false
  }
}
```

Para cada bloque, leer el `block_type` primero, luego verificar `layout_signature` y `text` para confirmar el componente. Siempre preferir el componente con más señales confirmadas.

---

## Familias soportadas en fase 1

| Familia | Estado |
|---|---|
| `marigold-v4.2` | Activo |
| `marigold-v4.0` | Pendiente fase 2 |
| `centurion-1.0` | Pendiente fase 2 |

Si el email tiene fondo negro o diseño Centurion, devolver `lower_html_flow` — no intentar lego aún.

---

## HEADERS

---

### H04

```
slot: header
templateFamily: marigold-v4.2
uso: Header estándar AMEX Argentina con logo, tagline "No vivas la vida sin ella", cuenta del titular, saludo personalizado y botón Mi cuenta. El más común en campañas MERCHANT Socio, MR y PLAT estándar.
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `header` |
| `layout_signature.has_preheader` | `true` |
| `layout_signature.has_account_data` | `true` |
| `layout_signature.has_greeting` | `true` |
| `layout_signature.has_login_button` | `true` |
| `layout_signature.has_large_image` | `false` |
| `text` contiene | `PUBLICIDAD`, `FULLNAME` o `Hola`, `LAST_5` o `Tu cuenta termina`, `Mi cuenta` |

**Props:**

| Prop | Descripción |
|---|---|
| `preheaderLabel` | Texto del preheader, normalmente `PUBLICIDAD` |
| `viewOnlineUrl` | URL "Ver online" con token `{(URLSignature1)}` |
| `logoHref` | URL del logo AMEX |
| `logoUrl` | Imagen del logo AMEX |
| `logoAlt` | Alt del logo |
| `taglineHref` | URL del tagline |
| `taglineUrl` | Imagen del tagline "No vivas la vida sin ella" |
| `taglineAlt` | Alt del tagline |
| `accountLabel` | Texto "Tu cuenta termina en:" |
| `accountSuffix` | Token `{(LAST_5)}` |
| `memberSinceLabel` | Texto "Miembro desde:" |
| `memberSince` | Token `{(MEMBER_SINCE)}` |
| `greetingText` | Texto "Hola {(FULLNAME)}" |
| `loginUrl` | URL del botón Mi cuenta |
| `loginAriaLabel` | Aria label del botón login |
| `loginLabel` | Texto del botón, normalmente `Mi cuenta` |

---

### H07

```
slot: header
templateFamily: marigold-v4.2
uso: Header PLAT con logo, tagline, cuenta, saludo, imagen de tarjeta Platinum y botón Mi cuenta. Igual que H04 pero incluye una imagen de la tarjeta en el panel.
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `header` |
| `layout_signature.has_preheader` | `true` |
| `layout_signature.has_account_data` | `true` |
| `layout_signature.has_greeting` | `true` |
| `layout_signature.has_login_button` | `true` |
| `layout_signature.image_count` | `4` o más (logo + tagline + tarjeta + login icon) |
| `text` contiene | `PUBLICIDAD`, `FULLNAME` o `Hola`, `Tu cuenta termina`, `Mi cuenta` |

**Props adicionales frente a H04:**

| Prop | Descripción |
|---|---|
| `cardImageUrl` | Imagen de la tarjeta Platinum |
| `cardImageAlt` | Alt de la tarjeta |

Incluye todas las props de H04.

---

## BODY — HERO

---

### B28

```
slot: body
templateFamily: marigold-v4.2
uso: Bloque hero principal con imagen grande ancha y headline tipográfico superpuesto. Primer bloque visual después del header. Sin CTA propio.
fuente: HB18-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `hero` |
| `layout_signature.has_large_image` | `true` |
| `layout_signature.has_cta` | `false` |
| `layout_signature.columns` | `1` |
| `images[0].width` | Mayor a 20 rem (imagen que ocupa todo el ancho) |
| `y_start` | Menor a 30 (primer bloque visual) |
| `text` | Headline corto, 2–6 palabras, sin precio ni CTA |

**Props:**

| Prop | Descripción |
|---|---|
| `heroBgColor` | Color hex de respaldo del hero |
| `heroBgPosition` | Posición CSS del background del hero, normalmente `center` |
| `heroBgSize` | Tamaño CSS del background del hero, normalmente `cover` |
| `heroImageUrl` | URL de la imagen hero (extraer de `images[0].src`) |
| `headlineAccentColor` | Color hex de la barra lateral del headline |
| `headlineBoxBgColor` | Color hex del fondo de la caja de headline |
| `headlineHtml` | HTML del headline (extraer de `text`, puede tener negrita o salto de línea) |
| `headlineTextColor` | Color hex del texto del headline |

**Override estructural San Valentín / febrero:**

Si el router exacto devuelve `flow_route: lower_html_flow`, `route_reason: no_match` y el texto de `visual_blocks` contiene señales de MERCHANT San Valentín (`San Valentín` o `San Valentin`, `febrero`, `JOYERÍA`, `VINOS`, `PERFUMERÍA`, `EXPERIENCIAS` o `VIAJES`), usar el fallback estructural de newsletter con hero editable en lugar de devolver `lower_html_flow`.

Payload base:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H03",
  "body": [
    {
      "id": "B28",
      "props": {
        "heroBgColor": "#00175a",
        "heroBgPosition": "center",
        "heroBgSize": "cover",
        "heroImageUrl": "https://...",
        "headlineAccentColor": "#006FCF",
        "headlineBoxBgColor": "#00175A",
        "headlineHtml": "",
        "headlineTextColor": "#FFFFFF"
      }
    },
    "B19",
    "B20",
    "B21",
    "B22",
    "B23",
    "B24",
    "B25",
    "B26",
    "B27"
  ],
  "footer": "F04",
  "globals": {
    "includeSeparators": false
  }
}
```

Para `heroImageUrl`, usar la primera imagen no-data dentro del bloque superior que no sea fondo full-width global si existe; en el caso extraído con prefijo `b64-1775620787767`, usar `.../b64-1775620787767-1.png`. Mantener `headlineHtml` vacío si el texto ya viene integrado en la imagen.

---

### B48

```
slot: body
templateFamily: marigold-v4.2
uso: Hero con imagen grande y color de fondo configurable. Igual que B28 pero permite cambiar el color de fondo del bloque.
fuente: HB18-v4.2
```

Mismas señales que B28. Preferir B48 cuando el bloque tiene fondo notoriamente diferente al blanco.

**Props:**

| Prop | Descripción |
|---|---|
| `heroBgColor` | Color hex del fondo (ej: `#00175a`) |
| `heroImageUrl` | URL de la imagen hero |
| `headlineHtml` | HTML del headline |

---

## BODY — INTRO

---

### B29

```
slot: body
templateFamily: marigold-v4.2
uso: Párrafo de introducción corto después del hero. Texto centrado, sin imágenes de contenido, sin CTA. Introduce el beneficio antes del primer bloque de oferta.
fuente: TM04-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `intro` |
| `layout_signature.has_cta` | `false` |
| `layout_signature.has_discount` | `false` |
| `layout_signature.has_large_image` | `false` |
| `text` | Frase corta descriptiva, sin precio ni fecha |
| `y_start` | Entre 20 y 40 |

Nota: puede aparecer una imagen decorativa delgada (height < 3 rem) en este bloque — es un separador gráfico, no un bloque de contenido.

**Props:**

| Prop | Descripción |
|---|---|
| `introHtml` | HTML del párrafo intro (extraer de `text`) |

---

## BODY — BENEFIT (columna única)

---

### B30

```
slot: body
templateFamily: marigold-v4.2
uso: Bloque de beneficio estándar en columna única. Incluye etiqueta de fecha, imagen de descuento o cuotas, dos logos de marca, CTA y disclaimer corto. Para campañas con 1–2 marcas por beneficio.
fuente: TM04-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `benefit` |
| `layout_signature.columns` | `1` |
| `layout_signature.has_discount` | `true` |
| `layout_signature.has_cta` | `true` |
| `layout_signature.image_count` | Entre 2 y 5 (imagen descuento + 1–2 logos + posible plus) |
| `text` contiene | Fecha (`Del ... al ...` o `TODOS LOS ...`), `OFF` o `CUOTAS`, nombre de marca, `Conocé más` o `Más info` |

**Props:**

| Prop | Descripción |
|---|---|
| `dateLabel` | Texto de fecha (ej: "Del 15 al 20 de diciembre") |
| `discountImageUrl` | Imagen del descuento o cuotas |
| `discountImageAlt` | Alt de la imagen de descuento |
| `plusImageUrl` | Imagen del símbolo "+" entre descuento y cuotas (opcional) |
| `plusImageAlt` | Alt del "+" |
| `installmentsImageUrl` | Imagen de cuotas (opcional) |
| `installmentsImageAlt` | Alt de cuotas |
| `benefitLine` | Texto explicativo bajo la oferta |
| `primaryLogoUrl` | Logo de la primera marca |
| `primaryLogoAlt` | Alt del primer logo (nombre de la marca) |
| `secondaryLogoUrl` | Logo de la segunda marca |
| `secondaryLogoAlt` | Alt del segundo logo |
| `ctaUrl` | URL del CTA |
| `ctaLabel` | Texto del CTA (ej: "Más info", "Conocé más") |
| `disclaimerHtml` | Texto legal corto en mayúsculas |

---

### B49

```
slot: body
templateFamily: marigold-v4.2
uso: Bloque de beneficio con cuatro marcas con logos individuales y CTAs por marca. Para campañas tipo Farmacity con múltiples tiendas en un solo bloque.
fuente: TM04-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `benefit` |
| `layout_signature.columns` | `1` |
| `layout_signature.has_discount` | `true` |
| `layout_signature.has_cta` | `true` |
| `layout_signature.image_count` | 6 o más (descuento + cuotas + 4 logos de marca) |
| `text` contiene | `OFF`, `cuotas`, 4 o más nombres de marca, `Más info` o `Comprá ahora` |

**Props:**

| Prop | Descripción |
|---|---|
| `introHtml` | Párrafo introductorio del beneficio |
| `dateLabel` | Etiqueta de fecha |
| `discountImageUrl` | Imagen del descuento |
| `discountImageAlt` | Alt del descuento |
| `plusImageUrl` | Símbolo "+" |
| `plusImageAlt` | Alt del "+" |
| `installmentsImageUrl` | Imagen de cuotas |
| `installmentsImageAlt` | Alt de cuotas |
| `benefitLine` | Texto bajo la oferta |
| `brandImageUrl` | Imagen decorativa de marca principal |
| `brandImageAlt` | Alt de la imagen decorativa |
| `farmacityUrl` | URL de la primera marca |
| `farmacityLogoUrl` | Logo de la primera marca |
| `farmacityLogoAlt` | Alt del primer logo |
| `getTheLookUrl` | URL de la segunda marca |
| `getTheLookLogoUrl` | Logo de la segunda marca |
| `getTheLookLogoAlt` | Alt del segundo logo |
| `simplicityUrl` | URL de la tercera marca |
| `simplicityLogoUrl` | Logo de la tercera marca |
| `simplicityLogoAlt` | Alt del tercer logo |
| `theFoodMarketUrl` | URL de la cuarta marca |
| `theFoodMarketLogoUrl` | Logo de la cuarta marca |
| `theFoodMarketLogoAlt` | Alt del cuarto logo |
| `closingHtml` | Texto de cierre del bloque |
| `ctaUrl` | URL del CTA general |
| `ctaAriaLabel` | Aria label del CTA |
| `ctaLabel` | Texto del CTA |
| `disclaimerHtml` | Texto legal |

---

## BODY — BENEFIT (dos columnas)

---

### B31

```
slot: body
templateFamily: marigold-v4.2
uso: Bloque de beneficio en dos columnas paralelas. Cada columna tiene fecha, imagen de oferta, logo de marca y CTA independiente. Para campañas con dos marcas distintas con condiciones diferentes.
fuente: HB08-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `benefit` |
| `layout_signature.columns` | `2` |
| `layout_signature.has_discount` | `true` |
| `layout_signature.has_cta` | `true` |
| `layout_signature.has_large_image` | `true` (imagen de separación horizontal arriba del bloque) |
| `text` contiene | Dos fechas distintas, dos nombres de marca, dos CTAs (`Conocé más` × 2) |

**Props:**

| Prop | Descripción |
|---|---|
| `leftDateLabel` | Fecha columna izquierda |
| `leftOfferImageUrl` | Imagen de oferta columna izquierda |
| `leftOfferImageAlt` | Alt de la oferta izquierda |
| `leftBenefitLine` | Texto bajo la oferta izquierda |
| `leftLogoUrl` | Logo de marca columna izquierda |
| `leftLogoAlt` | Alt del logo izquierdo (nombre de marca) |
| `leftCtaUrl` | URL CTA izquierdo |
| `leftCtaLabel` | Texto CTA izquierdo |
| `rightDateLabel` | Fecha columna derecha |
| `rightOfferImageUrl` | Imagen de oferta columna derecha |
| `rightOfferImageAlt` | Alt de la oferta derecha |
| `rightBenefitLine` | Texto bajo la oferta derecha |
| `rightLogoUrl` | Logo de marca columna derecha |
| `rightLogoAlt` | Alt del logo derecho (nombre de marca) |
| `rightCtaUrl` | URL CTA derecho |
| `rightCtaLabel` | Texto CTA derecho |
| `rightDisclaimerHtml` | Disclaimer opcional columna derecha |

---

## BODY — DISCLAIMER / CIERRE

---

### B32

```
slot: body
templateFamily: marigold-v4.2
uso: Bloque de disclaimer corto standalone. Texto legal en mayúsculas, sin imágenes, sin logo, sin CTA. Aparece al final del cuerpo antes del footer, después del último bloque de beneficio.
fuente: TM04-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `benefit` (puede clasificarse como benefit por el contenido legal) |
| `layout_signature.has_cta` | `false` |
| `layout_signature.has_discount` | `false` |
| `layout_signature.image_count` | `0` |
| `text` contiene | `NO VÁLIDO`, `NO ACUMULABLE`, `PLATAFORMAS DE PAGO`, `AGREGADORES`, texto en MAYÚSCULAS |
| `y_start` | Después de todos los bloques de beneficio |

**Props:**

| Prop | Descripción |
|---|---|
| `disclaimerHtml` | HTML del disclaimer (extraer de `text`, normalizar a minúsculas con HTML entities) |

---

## BODY — BRAND CLOSING

---

### (parte de footer F05 / F08)

```
block_type: brand_closing
```

El bloque `brand_closing` corresponde al cierre visual antes del footer legal. Incluye la imagen del tagline "No vivas la vida sin ella" más los iconos de redes sociales. **Este bloque forma parte del componente footer** (F05 o F08) y no se mapea a un componente body independiente.

Cuando aparezca `brand_closing` en `visual_blocks`, incluir ese bloque dentro del componente footer seleccionado y pasar `taglineDesktopUrl` con la URL de la imagen grande del bloque.

---

## FOOTERS

---

### F05

```
slot: footer
templateFamily: marigold-v4.2
uso: Footer estándar AMEX Argentina. Incluye tagline, iconos de redes sociales (Instagram, Facebook, YouTube), links de navegación (Privacidad, Contacto, Actualizar email, Desuscribirse), imagen CFT y legales largos con T.N.A y C.F.T. El más común en campañas MERCHANT Socio y MR.
fuente: FM05-v4.2 + FM02 + FM03-v4.2 + FM04-v4.2
```

**Señales para identificar:**

| Campo | Valor esperado |
|---|---|
| `block_type` | `footer` |
| `layout_signature.has_footer_nav` | `true` |
| `layout_signature.has_legal` | `true` |
| `text` contiene | `Privacidad`, `Contacto`, `Actualizar email`, `Desuscribirse`, `T.N.A`, `C.F.T`, `LEY 25.326`, `AMERICAN EXPRESS` |
| `layout_signature.image_count` | Entre 2 y 6 (tagline + redes + CFT imagen) |

**Props:**

| Prop | Descripción |
|---|---|
| `taglineDesktopUrl` | Imagen tagline desktop |
| `taglineMobileUrl` | Imagen tagline mobile |
| `taglineAlt` | Alt del tagline |
| `instagramUrl` | URL Instagram |
| `instagramImg` | Icono Instagram |
| `instagramAlt` | Alt Instagram |
| `facebookUrl` | URL Facebook |
| `facebookImg` | Icono Facebook |
| `facebookAlt` | Alt Facebook |
| `youtubeUrl` | URL YouTube |
| `youtubeImg` | Icono YouTube |
| `youtubeAlt` | Alt YouTube |
| `privacyUrl` | URL Privacidad |
| `privacyLabel` | Texto "Privacidad" |
| `contactUrl` | URL Contacto |
| `contactLabel` | Texto "Contacto" |
| `updateEmailUrl` | URL Actualizar email |
| `updateEmailLabel` | Texto "Actualizar email" |
| `unsubscribeUrl` | URL Desuscribirse |
| `unsubscribeLabel` | Texto "Desuscribirse" |
| `cftImageUrl` | Imagen del C.F.T. |
| `cftImageAlt` | Alt de la imagen CFT (ej: "1) C.F.T.:0,00%") |
| `legalHtml` | HTML de los legales largos (T.N.A, C.F.T, datos personales, instrucciones de desuscripción) |

---

### F08

```
slot: footer
templateFamily: marigold-v4.2
uso: Footer PLAT con sección cross-sell adicional antes de las redes sociales. Igual que F05 pero incluye un módulo de "También te puede interesar" o similar. Para campañas PLAT Spend.
fuente: FM05-v4.2 + FM01-v4.2 + TM06-v4.2 + FM02 + FM03-v4.2 + FM04-v4.2
```

**Señales para identificar:** Mismas que F05, más:

| Campo | Valor esperado |
|---|---|
| `text` contiene | Además de señales de F05: texto de cross-sell o módulo de descubrimiento de beneficios |
| `layout_signature.image_count` | Mayor que en F05 (más imágenes por el módulo adicional) |

**Props:** Todas las de F05, más:

| Prop | Descripción |
|---|---|
| `crossSellTitle` | Título de la sección cross-sell |
| `cross_sell_items_html` | HTML de los ítems cross-sell |

---

## Tabla de decisión rápida

Usar esta tabla para mapeo inicial. Siempre confirmar con `layout_signature` y `text`.

| `block_type` | `layout_signature` clave | → Componente |
|---|---|---|
| `header` | `has_account_data: true`, `has_greeting: true`, `has_login_button: true` | **H04** |
| `header` | Como H04 + `image_count >= 4` con imagen de tarjeta | **H07** |
| `hero` | `has_large_image: true`, `has_cta: false`, `columns: 1` | **B28** |
| `hero` | Como B28 + fondo de color visible | **B48** |
| `intro` | `has_cta: false`, `has_discount: false`, texto párrafo corto | **B29** |
| `benefit` | `columns: 1`, `has_discount: true`, `image_count` 2–5 | **B30** |
| `benefit` | `columns: 1`, `has_discount: true`, `image_count` 6+ | **B49** |
| `benefit` | `columns: 2`, `has_discount: true` | **B31** |
| `benefit` | `has_cta: false`, `has_discount: false`, `image_count: 0`, texto MAYÚSCULAS | **B32** |
| `brand_closing` | imagen grande tagline + redes sociales | *(incluir en footer)* |
| `footer` | `has_footer_nav: true`, `has_legal: true` | **F05** |
| `footer` | Como F05 + sección cross-sell | **F08** |

---

## Reglas del agente

1. Leer este catálogo antes de procesar cualquier bloque.
2. No leer `docs/campanas/*.md` — la ruta lego no busca campañas exactas.
3. Usar `id`, nunca `componentId`.
4. No incluir `role` ni `snippet` en el payload de `/api/compose-email`.
5. No inventar props que no estén documentadas en este catálogo.
6. No llamar `/api/compose-email` — solo construir y devolver el payload.
7. Si un bloque `brand_closing` aparece antes del footer, absorberlo en el componente footer pasando la imagen como `taglineDesktopUrl`.
8. Calcular `confidence` por bloque (0.0–1.0) y promediarlo para el total.
9. Si `confidence < 0.60`, devolver `flow_route: lower_html_flow`.
10. Si `confidence` entre 0.60 y 0.79, devolver `lego_compose_email` con `review_required: true`.
11. Si `confidence >= 0.80`, devolver `lego_compose_email` con `review_required: false`.
12. Preservar tokens de personalización: `{(FULLNAME)}`, `{(EMAIL)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}`, `{(URLSignature1)}`.
