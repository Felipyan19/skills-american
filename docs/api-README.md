# API de composición de emails

## Qué hace
Esta API compone emails HTML a partir de componentes reutilizables.

En vez de leer en runtime los HTML completos de `2. Modulos maquetados`, usa:

- `shells` por familia: estructura base del documento completo
- `snippets` curados: bloques HTML reutilizables
- `registry`: catálogo de componentes públicos `Hxx`, `Bxx`, `Fxx`

La API soporta estas familias:

- `marigold-v4.2`
- `marigold-v4.0`
- `centurion-1.0`

Cada request devuelve:

- `html`: email final ensamblado
- `manifest`: orden expandido real de los fragmentos usados

## Instalación
No requiere dependencias externas. Usa solo la librería estándar de Python.

Requisitos:

- Python 3.14+ disponible en el sistema

Opcional, crear un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Cómo correrla
Desde la raíz del repo:

```powershell
python -m api.http_server
```

Arranca en:

```text
http://127.0.0.1:8000
```

## Endpoints

### `GET /` o `GET /module1`
Abre una vista simple para revisar los ejemplos de `modulo 1`, ver el estado de cada caso y consultar la secuencia de componentes usada en cada referencia.

La vista consume:

- `GET /api/module1/examples`

Ese endpoint devuelve el catálogo completo con:

- `count`
- `summary` por estado de mapeo
- `examples` con el payload, la secuencia de sourceIds y las notas del caso

### `GET /api/components?templateFamily=...`
Devuelve el catálogo público de componentes para una familia.

Ejemplo:

```powershell
curl "http://127.0.0.1:8000/api/components?templateFamily=marigold-v4.2"
```

### `POST /api/compose-email`
Compone el HTML final.

Variantes de salida por query string:

- `POST /api/compose-email`: devuelve el JSON completo con `html` y `manifest`
- `POST /api/compose-email?html`: devuelve solo el HTML crudo para renderizarlo directo
- `POST /api/compose-email?manifest`: devuelve solo el `manifest`

Shape soportado:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    {
      "id": "B05",
      "props": {
        "headline": "Titulo"
      }
    }
  ],
  "footer": {
    "id": "F02",
    "props": {
      "legalHtml": "<p>Legales</p>"
    }
  },
  "globals": {
    "subject": "AMEX"
  }
}
```

Reglas:

- `header` acepta string o `{ "id": "...", "props": {...} }`
- `body` acepta mezcla de strings y objetos
- `body` mantiene el orden exacto recibido
- `footer` acepta string o objeto
- `header` y `footer` son públicos, pero internamente pueden expandirse a varios fragmentos
- si mandás solo IDs, la API usa defaults útiles para logo, imágenes, copys y legales placeholder

Ejemplo mínimo válido:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": ["B03"],
  "footer": "F01"
}
```

Ese payload ya devuelve HTML completo usando:

- logo placeholder
- hero placeholder
- tagline placeholder
- legales placeholder

Después podés sobrescribir solo los campos que necesites con `props`.

Ejemplos rÃ¡pidos:

```powershell
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/api/compose-email" -ContentType "application/json" -Body $body
```

```powershell
Invoke-WebRequest -Method POST -Uri "http://127.0.0.1:8000/api/compose-email?html" -ContentType "application/json" -Body $body
```

```powershell
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/api/compose-email?manifest" -ContentType "application/json" -Body $body
```

## Componentes disponibles

### `marigold-v4.2`

- `H01`: `PH01-v4.2 + Consumer Default-v4.2`
- `B01`: `HB03-v4.2`
- `B02`: `HB08-v4.2`
- `B03`: `HB15-v4.2`
- `B04`: `HB16-v4.2`
- `B05`: `HB18-v4.2`
- `B06`: `HB21-v4.2`
- `B07`: `IM03-v4.2`
- `B08`: `TM01-v4.2`
- `B09`: `TM04-v4.2`
- `B10`: `TM17-v4.2`
- `B11`: `TM03-v4.2`
- `F01`: `FM05-v4.2 + FM02 + FM03-v4.2 + FM04-v4.2`
- `F02`: `FM05-v4.2 + FM01-v4.2 + TM06-v4.2 + FM02 + FM03-v4.2 + FM04-v4.2`

### `marigold-v4.0`

- `H01`: `PH01-v4.0 + BP02-v4.0`
- `B01`: `HB03-v4.0`
- `B02`: `HB15-v4.0`
- `B03`: `IM02-v4.0`
- `B04`: `TM04-v4.0`
- `F01`: `FM05 + FM01-v4.0 + TM06-v4.0 + FM02 + FM03-v4.0 + FM04-v4.0`

### `centurion-1.0`

- `H01`: `PH01 + BP01`
- `B01`: `CHB01`
- `B02`: `CTM03`
- `B03`: `CIM02`
- `B04`: `CIM03`
- `B05`: `CIM05`
- `F01`: `TM06 + CFM01 + CFM02 + CTM14 + CFM03`

## Cómo guardar el HTML resultante
Ejemplo en PowerShell:

```powershell
$body = @{
  templateFamily = "marigold-v4.2"
  header = @{
    id = "H01"
    props = @{
      logoUrl = "https://example.com/logo.png"
      accountSuffix = "{(LAST_5)}"
      greetingName = "{(FULLNAME)}"
    }
  }
  body = @(
    @{
      id = "B09"
      props = @{
        headline = "Titulo"
        offerCode = "ABC"
        description = "Texto"
      }
    }
  )
  footer = @{
    id = "F01"
    props = @{
      taglineDesktopUrl = "https://example.com/tagline.jpg"
      taglineMobileUrl = "https://example.com/tagline-mobile.jpg"
      legalHtml = "<p>Legal</p>"
    }
  }
} | ConvertTo-Json -Depth 10

$response = Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/api/compose-email" -ContentType "application/json" -Body $body
$response.html | Out-File -Encoding utf8 salida.html
```

## Ejemplos para replicar `modulo 1`
Abajo tenés payloads base para reproducir la misma estructura y el mismo orden de componentes de ejemplos reales en `1. Referencias por segmento`.

Importante:

- Estos ejemplos ya respetan la secuencia de módulos del HTML de referencia.
- Para lograr una salida casi literal, usá las mismas URLs de imágenes y el mismo `legalHtml` del archivo fuente.
- Los `legalHtml` de `modulo 1` son largos. Lo normal es copiarlos completos desde el HTML de referencia.

### 1. MR Tecnología Dic25
Referencia:

- [MR-Tecnologia-Dic25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/MR/MR-Tecnologia-Dic25/MR-Tecnologia-Dic25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB15-v4.2 -> IM03-v4.2 -> IM03-v4.2 -> IM03-v4.2 -> TM04-v4.2 -> FM05-v4.2 -> FM01-v4.2 -> TM06-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload base:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H01",
    "props": {
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_01.jpg",
      "secondaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_02.jpg",
      "secondaryLogoAlt": "Membership Rewards",
      "secondaryLogoHref": "https://www.americanexpress.com/es-ar/rewards/membership-rewards/",
      "accountSuffix": "{(LAST_5)}",
      "greetingName": "{(FULLNAME)}"
    }
  },
  "body": [
    {
      "id": "B03",
      "props": {
        "imageDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_03a.jpg",
        "imageMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_03mbla.jpg",
        "headline": "Transformá puntos en tecnología.",
        "description": "Del 11 al 18 de diciembre canjeá puntos Membership Rewards por productos de tecnología seleccionados con hasta 40% OFF.",
        "ctaUrl": "https://www.americanexpress.com/es-ar/rewards/membership-rewards/"
      }
    },
    {
      "id": "B07",
      "props": {
        "items": [
          {
            "title": "Smart TV 65\" Philips",
            "badge": "40% OFF",
            "description": "310.500 puntos",
            "imageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_06.jpg",
            "ctaUrl": "https://www.americanexpress.com/es-ar/rewards/membership-rewards/award/Philips/OFED-5800/OFED-5800",
            "ctaLabel": "Canjeá ahora"
          },
          {
            "title": "Tablet Galaxy S10 FE 10.9\" Samsung",
            "badge": "35% OFF",
            "description": "202.500 puntos",
            "imageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_07.jpg",
            "ctaUrl": "https://www.americanexpress.com/es-ar/rewards/membership-rewards/award/Samsung/OFED-5801/OFED-5801",
            "ctaLabel": "Canjeá ahora"
          }
        ]
      }
    },
    {
      "id": "B07",
      "props": {
        "items": [
          {
            "title": "Par 2 izquierda",
            "badge": "X% OFF",
            "description": "Texto",
            "imageUrl": "https://example.com/producto-3.jpg",
            "ctaUrl": "https://example.com/producto-3",
            "ctaLabel": "Canjeá ahora"
          },
          {
            "title": "Par 2 derecha",
            "badge": "X% OFF",
            "description": "Texto",
            "imageUrl": "https://example.com/producto-4.jpg",
            "ctaUrl": "https://example.com/producto-4",
            "ctaLabel": "Canjeá ahora"
          }
        ]
      }
    },
    {
      "id": "B07",
      "props": {
        "items": [
          {
            "title": "Par 3 izquierda",
            "badge": "X% OFF",
            "description": "Texto",
            "imageUrl": "https://example.com/producto-5.jpg",
            "ctaUrl": "https://example.com/producto-5",
            "ctaLabel": "Canjeá ahora"
          },
          {
            "title": "Par 3 derecha",
            "badge": "X% OFF",
            "description": "Texto",
            "imageUrl": "https://example.com/producto-6.jpg",
            "ctaUrl": "https://example.com/producto-6",
            "ctaLabel": "Canjeá ahora"
          }
        ]
      }
    },
    {
      "id": "B09",
      "props": {
        "headline": "Beneficio destacado",
        "offerCode": "40% OFF",
        "description": "Copiá acá el copy exacto del bloque TM04 del HTML original."
      }
    }
  ],
  "footer": {
    "id": "F02",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_12.jpg",
      "taglineMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/271125_MR-Tecnologia-Dic25_12mbl.jpg",
      "crossSellItems": [
        {
          "title": "Viajes",
          "subtitle": "Beneficios",
          "iconUrl": "https://example.com/icono-viajes.png"
        },
        {
          "title": "Dining",
          "subtitle": "Experiencias",
          "iconUrl": "https://example.com/icono-dining.png"
        }
      ],
      "legalHtml": "<p>PEGAR ACA EL BLOQUE COMPLETO DE LEGALES FM04 DEL HTML MR-Tecnologia-Dic25.html</p>"
    }
  },
  "globals": {
    "subject": "AMEX"
  }
}
```

### 2. CORP IG Sep25
Referencia:

- [CORP-IG-Sep25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/CORP%20y%20MERCHANT%20Comercio/CORP-IG-Sep25/CORP-IG-Sep25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB21-v4.2 -> TM17-v4.2 -> TM04-v4.2 -> FM05-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload base:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H01",
    "props": {
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_01.jpg",
      "taglineUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_02.jpg",
      "taglineAlt": "No hagas negocios sin ella",
      "showGreeting": false,
      "showLogin": false,
      "showMemberSince": false,
      "accountSuffix": ""
    }
  },
  "body": [
    {
      "id": "B06",
      "props": {
        "imageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_03.jpg",
        "headlineTop": "SEGUINOS",
        "headlineAccent": "en Instagram.",
        "description": "¿Querés saber todas las novedades de la Tarjeta? Entrá a nuestro Instagram y no te pierdas de nada."
      }
    },
    {
      "id": "B10",
      "props": {
        "headline": "Beneficios destacados",
        "buttonLabel": "Seguinos",
        "buttonUrl": "https://www.instagram.com/americanexpressarg/",
        "cards": [
          {
            "title": "Beneficios",
            "subtitle": "en comercios",
            "iconUrl": "https://example.com/c1.png"
          },
          {
            "title": "Descuentos",
            "subtitle": "en supermercados",
            "iconUrl": "https://example.com/c2.png"
          }
        ]
      }
    },
    {
      "id": "B09",
      "props": {
        "headline": "Consejos de seguridad:",
        "offerCode": "Instagram",
        "description": "Nuestras cuentas oficiales son las que tienen el tilde azul y nunca te pediremos información a través de ellas."
      }
    }
  ],
  "footer": {
    "id": "F01",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_12.jpg",
      "taglineMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_13.jpg",
      "instagramImg": "https://i.email.americanexpress.com/wpm/1288/Images/1709-CORP-IG-Sep25_14.png",
      "legalHtml": "<p>PEGAR ACA EL BLOQUE COMPLETO DE LEGALES FM04 DEL HTML CORP-IG-Sep25.html</p>"
    }
  }
}
```

### 3. MERCHANT Shot Travel Agst25
Referencia:

- [MERCHANT-Shot-Travel-Agst25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/MERCHANT%20-%20Socio/MERCHANT-Shot-Travel-Agst25/MERCHANT-Shot-Travel-Agst25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB18-v4.2 -> TM04-v4.2 -> TM04-v4.2 -> TM04-v4.2 -> TM03-v4.2 -> TM04-v4.2 -> FM05-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload estructural equivalente:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": ["B05", "B09", "B09", "B09", "B11", "B09"],
  "footer": "F01"
}
```

Importante:

- ese payload ya reproduce el mismo orden de componentes del HTML MERCHANT
- si querés que además salga casi literal, necesitás pasar las mismas URLs, copys y `legalHtml` del archivo fuente
- con solo IDs, la API usa defaults genéricos; por eso la estructura coincide, pero el contenido no necesariamente

### 4. TRAVEL Mexico Sept25 Centurion
Referencia:

- [TRAVEL-Mexico-Sept25-CENT.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/TRAVEL%20(Cent%20y%20Plat)/TRAVEL-Mexico-Sept25-CENT/TRAVEL-Mexico-Sept25-CENT.html)

Secuencia equivalente soportada por la API:

```text
PH01 -> BP01 -> CHB01 -> CTM03 -> CIM02 -> TM06 -> CFM01 -> CFM02 -> CTM14 -> CFM03
```

Payload base:

```json
{
  "templateFamily": "centurion-1.0",
  "header": {
    "id": "H01",
    "props": {
      "logoUrl": "https://example.com/amex-centurion-white.png",
      "taglineUrl": "https://example.com/the-centurion-card.png",
      "cardImageUrl": "https://example.com/centurion-card.png",
      "accountSuffix": "{(LAST_5)}",
      "greetingName": "{(FULLNAME)}"
    }
  },
  "body": [
    {
      "id": "B01",
      "props": {
        "imageUrl": "https://example.com/100925_TRAVEL-Mexico-Sept25-CENT_hero.jpg",
        "headline": "México exclusivo",
        "description": "Itinerarios curados para socios Centurion.",
        "ctaUrl": "https://www.americanexpress.com/es-ar/account/login?DestPage=https%3A%2F%2Fwww.americanexpress.com%2Far%2Fbeneficios%2Fcenturion%2Findex.html"
      }
    },
    {
      "id": "B02",
      "props": {
        "headline": "Fine Hotels + Resorts",
        "description": "Usá el mismo copy del primer bloque CTM03. En el HTML de referencia aparece junto al asset 100925_TRAVEL-Mexico-Sept25-CENT_03.jpg."
      }
    },
    {
      "id": "B03",
      "props": {
        "items": [
          {
            "title": "Conrad Tulum Riviera Maya",
            "description": "Tercera noche bonificada.",
            "imageUrl": "https://example.com/100925_TRAVEL-Mexico-Sept25-CENT_12b.jpg",
            "ctaUrl": "https://example.com/conrad",
            "ctaLabel": "VER BENEFICIO"
          },
          {
            "title": "Hotel Alexander, Ciudad de México",
            "description": "Beneficios exclusivos por reserva.",
            "imageUrl": "https://example.com/100925_TRAVEL-Mexico-Sept25-CENT_13.jpg",
            "ctaUrl": "https://example.com/alexander",
            "ctaLabel": "VER BENEFICIO"
          }
        ]
      }
    }
  ],
  "footer": {
    "id": "F01",
    "props": {
      "crossSellItems": [],
      "legalHtml": "<p>PEGAR ACA EL BLOQUE COMPLETO DE LEGALES CFM03 DEL HTML TRAVEL-Mexico-Sept25-CENT.html</p>"
    }
  },
  "globals": {
    "subject": "Centurion"
  }
}
```

### 5. AAPLUS Gold Feb25
Referencia:

- [PP-LOC-GOLD-Febrero25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/AAPLUS/PP-LOC-GOLD-Febrero25/PP-LOC-GOLD-Febrero25.html)

Secuencia original:

```text
PH01-v4.0 -> BP02-v4.0 -> HB03-v4.0 -> HB15-v4.0 -> IM02-v4.0 -> IM02-v4.0 -> IM02-v4.0 -> IM02-v4.0 -> TM04-v4.0 -> FM05 -> FM01-v4.0 -> TM06-v4.0 -> FM02 -> FM03-v4.0 -> FM04-v4.0
```

Payload base:

```json
{
  "templateFamily": "marigold-v4.0",
  "header": {
    "id": "H01",
    "props": {
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/155012025-PP-LOC-GOLD-Enero25_01.jpg",
      "taglineUrl": "https://i.email.americanexpress.com/wpm/1288/Images/155012025-PP-LOC-GOLD-Enero25_02.jpg",
      "cardImageUrl": "https://example.com/gold-card.png",
      "cardImageAlt": "The Gold Credit Card",
      "accountSuffix": "{(LAST_5)}",
      "greetingName": "{(FNAME)}"
    }
  },
  "body": [
    {
      "id": "B01",
      "props": {
        "imageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/155012025-PP-LOC-GOLD-Enero25_04.jpg",
        "headline": "Más límite, más viajes.",
        "description": "Ponele destino a tus compras.",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-viajes/"
      }
    },
    {
      "id": "B02",
      "props": {
        "imageUrl": "https://example.com/hb15.jpg",
        "headline": "Extendimos tu límite de crédito.",
        "description": "Usá el texto exacto del bloque HB15 del HTML original."
      }
    },
    {
      "id": "B03",
      "props": {
        "imageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/155012025-PP-LOC-GOLD-Enero25_10.jpg",
        "headline": "Viví tus Shopping Days",
        "description": "Copiá acá el texto exacto del bloque IM02.",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-gastronomia/?utm_source=news&utm_medium=email&utm_campaign=especialgastronomia",
        "ctaLabel": "Conocé más"
      }
    },
    {
      "id": "B04",
      "props": {
        "headline": "Beneficio destacado",
        "description": "Copiá acá el texto exacto del bloque TM04."
      }
    }
  ],
  "footer": {
    "id": "F01",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/155012025-PP-LOC-GOLD-Enero25_12.jpg",
      "legalHtml": "<p>PEGAR ACA EL BLOQUE COMPLETO DE LEGALES FM04 DEL HTML PP-LOC-GOLD-Febrero25.html</p>"
    }
  }
}
```

### 5. MERCHANT Shot Travel Agst25
Referencia:

- [MERCHANT-Shot-Travel-Agst25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/MERCHANT%20-%20Socio/MERCHANT-Shot-Travel-Agst25/MERCHANT-Shot-Travel-Agst25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB18-v4.2 -> TM04-v4.2 (Agencias) -> TM04-v4.2 (Compras) -> TM04-v4.2 (Spa) -> TM03-v4.2 -> TM04-v4.2 (Hashtag) -> FM05-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload base:

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

> Todos los componentes son **estáticos hardcodeados** para este email. No requieren props adicionales.

| Componente | Módulo | Contenido |
|---|---|---|
| `H02` | PH01-v4.2 + Consumer Default-v4.2 | Brand panel hardcodeado |
| `B12` | HB18-v4.2 | Hero: "Elegí el destino, los beneficios ya los tenés." |
| `B13` | TM04-v4.2 | Bloque Agencias (Aerolíneas, Despegar, Al Mundo) |
| `B14` | TM04-v4.2 | Bloque Compras (Samsonite, Delsey, Equipaje Urbano) |
| `B15` | TM04-v4.2 | Bloque Spa (Alvear, Marriott, Madero, Las Balsas, Palladio) |
| `B17` | TM03-v4.2 | How To hoteles (25% OFF, 4x3, 30% OFF Alvarez Argüelles) |
| `B16` | TM04-v4.2 | Banner hashtag "#conAmex" |
| `F03` | FM05 + FM02 + FM03 + FM04 | Footer con taglines + legales hardcodeados |

### 6. MERCHANT Newsletter DIC25
Referencia:

- [MERCHANT-Newsletter-Dic25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/MERCHANT%20-%20Socio/MERCHANT-Newsletter-Dic25/MERCHANT-Newsletter-Dic25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB03-v4.2 -> TM04-v4.2 (intro) -> TM01-v4.2 + HB08 (compras) -> TM01-v4.2 + HB08 (gastronomía) -> TM01-v4.2 + TM04 + HB08 (hoteles) -> TM04-v4.2 (CTA) -> FM05-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload base:

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

> Todos los componentes son **estáticos hardcodeados** para este email. No requieren props adicionales.

| Componente | Módulo | Contenido |
|---|---|---|
| `H03` | PH01-v4.2 + Consumer Default-v4.2 | Brand panel con imágenes `_01`, `_02` |
| `B18` | HB03-v4.2 | Hero banner principal |
| `B19` | TM04-v4.2 | Texto intro: "Compras, gastronomía y hoteles..." |
| `B20` | TM01-v4.2 | Header sección Compras |
| `B21` | HB08-v4.2 | Módulo 50-50 Compras |
| `B22` | TM01-v4.2 | Header sección Gastronomía |
| `B23` | HB08-v4.2 | Módulo 50-50 Gastronomía |
| `B24` | TM01-v4.2 | Header sección Hoteles |
| `B25` | TM04-v4.2 | Bloque NH Hotels |
| `B26` | HB08-v4.2 | Módulo 50-50 Hoteles |
| `B27` | TM04-v4.2 | CTA final "Descubrí todos los beneficios" |
| `F04` | FM05 + FM02 + FM03 + FM04 | Footer con tagline `_20`, redes `_21-23`, legales `_24` |

### 7. MERCHANT Shot Deporte DIC25
Referencia:

- [MERCHANT-Shot-deporte-DIC25.html](C:/Users/USUARIO/Documents/codes/Niawi/skills-american/1.%20Referencias%20por%20segmento/MERCHANT%20-%20Socio/MERCHANT-Shot-deporte-DIC25/MERCHANT-Shot-deporte-DIC25.html)

Secuencia original:

```text
PH01-v4.2 -> Consumer Default-v4.2 -> HB18-v4.2 -> TM04-v4.2 (intro) -> TM04-v4.2 (clubs) -> HB08-v4.2 -> TM04-v4.2 (closing) -> FM05-v4.2 -> FM02 -> FM03-v4.2 -> FM04-v4.2
```

Payload base:

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

> Todos los componentes son **estáticos hardcodeados** para este email. No requieren props adicionales.

| Componente | Módulo | Contenido |
|---|---|---|
| `H04` | PH01-v4.2 + Consumer Default-v4.2 | Brand panel con imágenes `_01`, `_02` |
| `B28` | HB18-v4.2 | Hero: "La energía que te mueve" (imagen `_04b.jpg`) |
| `B29` | TM04-v4.2 | Texto intro: "Lo que necesitás para entrenar mejor..." |
| `B30` | TM04-v4.2 | Oferta clubs: 10% OFF + cuotas, Megatlon + Fiter, botón "Más info" |
| `B31` | HB08-v4.2 | 50-50: Decathlon (izq, cuotas) + Lasaigues Padel (der, 15% OFF) |
| `B32` | TM04-v4.2 | Closing oscuro: "BENEFICIOS NO VÁLIDOS PARA PAGOS..." |
| `F05` | FM05 + FM02 + FM03 + FM04 | Footer con taglines `_14`/`_15`, redes `_16-18`, legales `_19` |

## Payloads para todos los HTMLs de referencia

Para generar el payload de todos los HTMLs del módulo 1 en forma automática:

```powershell
python -m api.generate_module1_payloads
```

Genera dos archivos:

- `api/module1_payloads.json` — todos los payloads en JSON
- `api/module1_payloads.md` — mismo contenido en Markdown legible

Los emails con fidelidad `alta` (componentes hardcodeados, resultado 1:1) son:

| HTML de referencia | Header | Body | Footer |
|---|---|---|---|
| MERCHANT-Shot-Travel-Agst25 | `H02` | `B12, B13, B14, B15, B17, B16` | `F03` |
| MERCHANT-Newsletter-Dic25 | `H03` | `B18, B19, B20, B21, B22, B23, B24, B25, B26, B27` | `F04` |
| MERCHANT-Shot-deporte-DIC25 | `H04` | `B28, B29, B30, B31, B32` | `F05` |

## Cómo validar que salió igual en estructura
La respuesta trae un `manifest.expanded`. Si querés verificar que quedó alineado con `modulo 1`, compará el orden de `sourceId`.

Ejemplo esperado MR:

```json
[
  "PH01-v4.2",
  "Consumer Default-v4.2",
  "HB15-v4.2",
  "IM03-v4.2",
  "IM03-v4.2",
  "IM03-v4.2",
  "TM04-v4.2",
  "FM05-v4.2",
  "FM01-v4.2",
  "TM06-v4.2",
  "FM02",
  "FM03-v4.2",
  "FM04-v4.2"
]
```

## Tests
Correr toda la suite:

```powershell
python -m unittest discover -s tests -v
```

La suite cubre:

- composición por familia
- validaciones
- orden del body
- endpoints HTTP
- snapshots de secuencia
- golden checks contra HTML reales de `modulo 1` cuando los archivos están disponibles localmente
