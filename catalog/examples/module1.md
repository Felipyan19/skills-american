# Catalogo operativo de payloads para modulo 1

Este archivo lo genera `scripts/generate_examples.py` y debe mantenerse alineado con el front `/module1`.
La idea es que una persona o un agente puedan mirar este catalogo, abrir la referencia visual en el front y decidir que payload de `compose-email` se parece mas al PDF entrante.

## Reglas estrictas para el agente

1. Usar exclusivamente la informacion publicada en este markdown para decidir el payload.
2. No inventar campañas, componentes, headers, bodies ni footers que no aparezcan aqui.
3. No usar memoria previa, conocimiento externo ni ejemplos fuera de este archivo.
4. Si un caso no coincide de forma exacta, elegir el ejemplo mas cercano de este mismo catalogo y reutilizar su payload.
5. Responder siempre con un payload valido de `compose-email` usando solo IDs presentes en este documento.

## Como usar este catalogo

1. Extrae del PDF todas las pistas posibles: titulo, rubro, fechas, marcas, estructura visual y textos repetidos.
2. Busca el ejemplo mas cercano por nombre, segmento, `sourceIds`, notas y ruta de referencia.
3. Si el match es fuerte, reutiliza el `payload` publicado aqui.
4. Si no hay match exacto, prioriza ejemplos con la misma `templateFamily` y secuencia estructural parecida.
5. Usa `frontPath` y `htmlApiPath` para contrastar visualmente el HTML de referencia contra el resultado generado.

## Leyenda
- `alta`: usa un set de componentes especifico del caso dentro del catalogo actual.
- `estructural`: reproduce la familia y el orden general con componentes publicos genericos.
- `aproximada`: ademas de lo anterior, hubo sustituciones o faltan sourceIds publicos.

## AAPLUS

### PP-LOC-GOLD-Febrero25

- ID estable: `pp-loc-gold-febrero25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/AAPLUS/PP-LOC-GOLD-Febrero25/PP-LOC-GOLD-Febrero25.html`
- Vista front: `/example/pp-loc-gold-febrero25`
- API detalle: `/api/module1/examples/pp-loc-gold-febrero25`
- API HTML: `/api/module1/examples/pp-loc-gold-febrero25/html`
- Familia: `marigold-v4.0`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.0, BP02-v4.0, HB03-v4.0, HB15-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM04-v4.0, FM05, FM01-v4.0, TM06-v4.0, FM02, FM03-v4.0, FM04-v4.0`
- Resumen para agente: `PP-LOC-GOLD-Febrero25 | grupo=AAPLUS | familia=marigold-v4.0 | fidelidad=estructural | sourceIds=PH01-v4.0, BP02-v4.0, HB03-v4.0, HB15-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM04-v4.0, FM05, FM01-v4.0, TM06-v4.0, FM02, FM03-v4.0, FM04-v4.0`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B03",
    "B03",
    "B03",
    "B03",
    "B04"
  ],
  "footer": "F01"
}
```

### PP-LOC-PLAT-Febrero25

- ID estable: `pp-loc-plat-febrero25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/AAPLUS/PP-LOC-PLAT-Febrero25/PP-LOC-PLAT-Febrero25.html`
- Vista front: `/example/pp-loc-plat-febrero25`
- API detalle: `/api/module1/examples/pp-loc-plat-febrero25`
- API HTML: `/api/module1/examples/pp-loc-plat-febrero25/html`
- Familia: `marigold-v4.0`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.0, BP02-v4.0, HB03-v4.0, HB15-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM04-v4.0, FM05, FM01-v4.0, TM06-v4.0, FM02, FM03-v4.0, FM04-v4.0`
- Resumen para agente: `PP-LOC-PLAT-Febrero25 | grupo=AAPLUS | familia=marigold-v4.0 | fidelidad=estructural | sourceIds=PH01-v4.0, BP02-v4.0, HB03-v4.0, HB15-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM04-v4.0, FM05, FM01-v4.0, TM06-v4.0, FM02, FM03-v4.0, FM04-v4.0`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B03",
    "B03",
    "B03",
    "B03",
    "B04"
  ],
  "footer": "F01"
}
```

## CORP y MERCHANT Comercio

### CORP-IG-Sep25

- ID estable: `corp-ig-sep25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-IG-Sep25/CORP-IG-Sep25.html`
- Vista front: `/example/corp-ig-sep25`
- API detalle: `/api/module1/examples/corp-ig-sep25`
- API HTML: `/api/module1/examples/corp-ig-sep25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB21-v4.2, TM17-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `CORP-IG-Sep25 | grupo=CORP y MERCHANT Comercio | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB21-v4.2, TM17-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B06",
    "B10",
    "B09"
  ],
  "footer": "F01"
}
```

### CORP-Special-Offers-Navidad-Dic25

- ID estable: `corp-special-offers-navidad-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-Special-Offers-Navidad-Dic25/CORP-Special-Offers-Navidad-Dic25.html`
- Vista front: `/example/corp-special-offers-navidad-dic25`
- API detalle: `/api/module1/examples/corp-special-offers-navidad-dic25`
- API HTML: `/api/module1/examples/corp-special-offers-navidad-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `CORP-Special-Offers-Navidad-Dic25 | grupo=CORP y MERCHANT Comercio | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B04",
    "B02",
    "B02",
    "B02",
    "B07",
    "B07",
    "B07",
    "B09",
    "B09"
  ],
  "footer": "F01"
}
```

### CORP-Travel-Octubre25

- ID estable: `corp-travel-octubre25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-Travel-Octubre25/CORP-Travel-Octubre25.html`
- Vista front: `/example/corp-travel-octubre25`
- API detalle: `/api/module1/examples/corp-travel-octubre25`
- API HTML: `/api/module1/examples/corp-travel-octubre25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `CORP-Travel-Octubre25 | grupo=CORP y MERCHANT Comercio | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B01",
    "B09",
    "B08",
    "B09",
    "B08",
    "B09",
    "B08",
    "B09",
    "B09"
  ],
  "footer": "F01"
}
```

## ICS

### PP-Diderot-Nov25-ICS

- ID estable: `pp-diderot-nov25-ics`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/ICS/PP-Diderot-Nov25-ICS/PP-Diderot-Nov25-ICS.html`
- Vista front: `/example/pp-diderot-nov25-ics`
- API detalle: `/api/module1/examples/pp-diderot-nov25-ics`
- API HTML: `/api/module1/examples/pp-diderot-nov25-ics/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PP-Diderot-Nov25-ICS | grupo=ICS | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B02",
    "B02",
    "B02",
    "B09"
  ],
  "footer": "F01"
}
```

### PP-F1-Miami-Preventa-ICS-oct25

- ID estable: `pp-f1-miami-preventa-ics-oct25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/ICS/PP-F1-Miami-Preventa-ICS-oct25/PP-F1-Miami-Preventa-ICS-oct25.html`
- Vista front: `/example/pp-f1-miami-preventa-ics-oct25`
- API detalle: `/api/module1/examples/pp-f1-miami-preventa-ics-oct25`
- API HTML: `/api/module1/examples/pp-f1-miami-preventa-ics-oct25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, TM04-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PP-F1-Miami-Preventa-ICS-oct25 | grupo=ICS | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, TM04-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B04",
    "B02",
    "B09",
    "B07",
    "B09"
  ],
  "footer": "F01"
}
```

## MERCHANT - Socio

### MERCHANT-Newsletter-Dic25

- ID estable: `merchant-newsletter-dic25`
- Estado en front: `Exacta`
- Archivo: `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Newsletter-Dic25/MERCHANT-Newsletter-Dic25.html`
- Vista front: `/example/merchant-newsletter-dic25`
- API detalle: `/api/module1/examples/merchant-newsletter-dic25`
- API HTML: `/api/module1/examples/merchant-newsletter-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `alta`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, TM01-v4.2, HB08-v4.2, TM01-v4.2, HB08-v4.2, TM01-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MERCHANT-Newsletter-Dic25 | grupo=MERCHANT - Socio | familia=marigold-v4.2 | fidelidad=alta | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, TM01-v4.2, HB08-v4.2, TM01-v4.2, HB08-v4.2, TM01-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Nota: Usa el set dedicado de MERCHANT Newsletter.
- Nota: El HTML de referencia incluye un HB08 vacio que funciona como espaciador y no existe como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H03",
  "body": [
    "B18",
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

### MERCHANT-Shot-deporte-DIC25

- ID estable: `merchant-shot-deporte-dic25`
- Estado en front: `Exacta`
- Archivo: `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-deporte-DIC25/MERCHANT-Shot-deporte-DIC25.html`
- Vista front: `/example/merchant-shot-deporte-dic25`
- API detalle: `/api/module1/examples/merchant-shot-deporte-dic25`
- API HTML: `/api/module1/examples/merchant-shot-deporte-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `alta`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MERCHANT-Shot-deporte-DIC25 | grupo=MERCHANT - Socio | familia=marigold-v4.2 | fidelidad=alta | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Nota: Usa el set dedicado de MERCHANT Shot Deporte.

Payload requerido para `compose-email`:

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

### MERCHANT-SHOT-Navidad-Dic25

- ID estable: `merchant-shot-navidad-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-SHOT-Navidad-Dic25/MERCHANT-SHOT-Navidad-Dic25.html`
- Vista front: `/example/merchant-shot-navidad-dic25`
- API detalle: `/api/module1/examples/merchant-shot-navidad-dic25`
- API HTML: `/api/module1/examples/merchant-shot-navidad-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MERCHANT-SHOT-Navidad-Dic25 | grupo=MERCHANT - Socio | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM01-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B05",
    "B09",
    "B08",
    "B09",
    "B09",
    "B02",
    "B09"
  ],
  "footer": "F01"
}
```

### MERCHANT-Shot-Travel-Agst25

- ID estable: `merchant-shot-travel-agst25`
- Estado en front: `Exacta`
- Archivo: `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-Travel-Agst25/MERCHANT-Shot-Travel-Agst25.html`
- Vista front: `/example/merchant-shot-travel-agst25`
- API detalle: `/api/module1/examples/merchant-shot-travel-agst25`
- API HTML: `/api/module1/examples/merchant-shot-travel-agst25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `alta`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, TM04-v4.2, TM03-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MERCHANT-Shot-Travel-Agst25 | grupo=MERCHANT - Socio | familia=marigold-v4.2 | fidelidad=alta | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, TM04-v4.2, TM03-v4.2, TM04-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Nota: Usa el set dedicado de MERCHANT Shot Travel.
- Nota: Es la mejor aproximacion disponible hoy dentro del catalogo.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H02",
  "body": [
    "B12",
    "B13",
    "B14",
    "B15",
    "B17",
    "B16"
  ],
  "footer": "F03",
  "globals": {
    "includeSeparators": false
  }
}
```

### MERCHANT-Special-Offers-Dic25

- ID estable: `merchant-special-offers-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Special-Offers-Dic25/MERCHANT-Special-Offers-Dic25.html`
- Vista front: `/example/merchant-special-offers-dic25`
- API detalle: `/api/module1/examples/merchant-special-offers-dic25`
- API HTML: `/api/module1/examples/merchant-special-offers-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, HB08-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, TM04-v4.2, FM05-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MERCHANT-Special-Offers-Dic25 | grupo=MERCHANT - Socio | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB16-v4.2, HB08-v4.2, HB08-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, TM04-v4.2, FM05-v4.2, FM05-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B04",
    "B02",
    "B02",
    "B07",
    "B07",
    "B07",
    "B09",
    "B09"
  ],
  "footer": "F01"
}
```

## MR

### MR-Especial-bebidas-DIC25

- ID estable: `mr-especial-bebidas-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/MR/MR-Especial-bebidas-DIC25/MR-Especial-bebidas-DIC25.html`
- Vista front: `/example/mr-especial-bebidas-dic25`
- API detalle: `/api/module1/examples/mr-especial-bebidas-dic25`
- API HTML: `/api/module1/examples/mr-especial-bebidas-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MR-Especial-bebidas-DIC25 | grupo=MR | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B07",
    "B07",
    "B07",
    "B09"
  ],
  "footer": "F02"
}
```

### MR-Especial-Starlink-ENERO25

- ID estable: `mr-especial-starlink-enero25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/MR/MR-Especial-Starlink-ENERO26/MR-Especial-Starlink-ENERO25.html`
- Vista front: `/example/mr-especial-starlink-enero25`
- API detalle: `/api/module1/examples/mr-especial-starlink-enero25`
- API HTML: `/api/module1/examples/mr-especial-starlink-enero25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MR-Especial-Starlink-ENERO25 | grupo=MR | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B05",
    "B09",
    "B02",
    "B09"
  ],
  "footer": "F02"
}
```

### MR-MFF-La-Gueya-Nov25

- ID estable: `mr-mff-la-gueya-nov25`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/MR/MR-MFF-La-Gueya-Nov25/MR-MFF-La-Gueya-Nov25.html`
- Vista front: `/example/mr-mff-la-gueya-nov25`
- API detalle: `/api/module1/examples/mr-mff-la-gueya-nov25`
- API HTML: `/api/module1/examples/mr-mff-la-gueya-nov25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, TM04-v4.2, TM23-v4.2, HB08-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MR-MFF-La-Gueya-Nov25 | grupo=MR | familia=marigold-v4.2 | fidelidad=aproximada | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB03-v4.2, TM04-v4.2, HB08-v4.2, TM04-v4.2, TM04-v4.2, TM23-v4.2, HB08-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Sustituciones aplicadas: `TM23-v4.2 -> B09`
- Nota: Se sustituyo TM23-v4.2 por B09 como aproximacion al bloque promocional.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B01",
    "B09",
    "B02",
    "B09",
    "B09",
    "B09",
    "B02"
  ],
  "footer": "F02"
}
```

### MR-Tecnologia-Dic25

- ID estable: `mr-tecnologia-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/MR/MR-Tecnologia-Dic25/MR-Tecnologia-Dic25.html`
- Vista front: `/example/mr-tecnologia-dic25`
- API detalle: `/api/module1/examples/mr-tecnologia-dic25`
- API HTML: `/api/module1/examples/mr-tecnologia-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MR-Tecnologia-Dic25 | grupo=MR | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, IM03-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B07",
    "B07",
    "B07",
    "B09"
  ],
  "footer": "F02"
}
```

## PP (Cent y Plat)

### MR-Bonus-Smiles-Dic25-CENT

- ID estable: `mr-bonus-smiles-dic25-cent`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/MR-Bonus-Smiles-Dic25-CENT/MR-Bonus-Smiles-Dic25-CENT.html`
- Vista front: `/example/mr-bonus-smiles-dic25-cent`
- API detalle: `/api/module1/examples/mr-bonus-smiles-dic25-cent`
- API HTML: `/api/module1/examples/mr-bonus-smiles-dic25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CHB01, CTM03, CIM05, CIM02, CIM02, CTM04, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `MR-Bonus-Smiles-Dic25-CENT | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CHB01, CTM03, CIM05, CIM02, CIM02, CTM04, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Sustituciones aplicadas: `CTM04 -> B02`
- Nota: Se sustituyo CTM04 por B02 porque aun no existe un componente publico especifico para CTM04.
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B01",
    "B02",
    "B05",
    "B03",
    "B03",
    "B02",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### MR-Bonus-Smiles-Dic25-PLAT

- ID estable: `mr-bonus-smiles-dic25-plat`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/MR-Bonus-Smiles-Dic25-PLAT/MR-Bonus-Smiles-Dic25-PLAT/MR-Bonus-Smiles-Dic25-PLAT.html`
- Vista front: `/example/mr-bonus-smiles-dic25-plat`
- API detalle: `/api/module1/examples/mr-bonus-smiles-dic25-plat`
- API HTML: `/api/module1/examples/mr-bonus-smiles-dic25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, TM03, FM05-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `MR-Bonus-Smiles-Dic25-PLAT | grupo=PP (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, TM03, FM05-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B05",
    "B09",
    "B09",
    "B09",
    "B02",
    "B02",
    "B09",
    "B11"
  ],
  "footer": "F02"
}
```

### PLAT-Spend-Farmacity-Oct25

- ID estable: `plat-spend-farmacity-oct25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PLAT-Spend-Farmacity-Oct25/PLAT-Spend-Farmacity-Oct25.html`
- Vista front: `/example/plat-spend-farmacity-oct25`
- API detalle: `/api/module1/examples/plat-spend-farmacity-oct25`
- API HTML: `/api/module1/examples/plat-spend-farmacity-oct25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PLAT-Spend-Farmacity-Oct25 | grupo=PP (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB18-v4.2, TM04-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B05",
    "B09"
  ],
  "footer": "F02"
}
```

### PP-Cata-Piedra-Pasillo-OCT25

- ID estable: `pp-cata-piedra-pasillo-oct25`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Cata-Piedra-Pasillo-OCT25/PP-Cata-Piedra-Pasillo-OCT25.html`
- Vista front: `/example/pp-cata-piedra-pasillo-oct25`
- API detalle: `/api/module1/examples/pp-cata-piedra-pasillo-oct25`
- API HTML: `/api/module1/examples/pp-cata-piedra-pasillo-oct25/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CIM02, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `PP-Cata-Piedra-Pasillo-OCT25 | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CIM02, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B03",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### PP-Dining-Ultramarino-Nov25-CENT

- ID estable: `pp-dining-ultramarino-nov25-cent`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Dining-Ultramarino-Nov25-CENT/PP-Dining-Ultramarino-Nov25-CENT.html`
- Vista front: `/example/pp-dining-ultramarino-nov25-cent`
- API detalle: `/api/module1/examples/pp-dining-ultramarino-nov25-cent`
- API HTML: `/api/module1/examples/pp-dining-ultramarino-nov25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CIM02, CTM03, CIM02, CTM03, CTM04, CTM03, CHB01, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `PP-Dining-Ultramarino-Nov25-CENT | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CIM02, CTM03, CIM02, CTM03, CTM04, CTM03, CHB01, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Sustituciones aplicadas: `CTM04 -> B02`
- Nota: Se sustituyo CTM04 por B02 porque aun no existe un componente publico especifico para CTM04.
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B03",
    "B02",
    "B03",
    "B02",
    "B02",
    "B02",
    "B01",
    "B02"
  ],
  "footer": "F01"
}
```

### PP-Dining-Ultramarino-Nov25-PLAT

- ID estable: `pp-dining-ultramarino-nov25-plat`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Dining-Ultramarino-Nov25-PLAT/PP-Dining-Ultramarino-Nov25-PLAT.html`
- Vista front: `/example/pp-dining-ultramarino-nov25-plat`
- API detalle: `/api/module1/examples/pp-dining-ultramarino-nov25-plat`
- API HTML: `/api/module1/examples/pp-dining-ultramarino-nov25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, HB08-v4.2, TM04-v4.2, HB08-v4.2, TM03, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PP-Dining-Ultramarino-Nov25-PLAT | grupo=PP (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, HB08-v4.2, TM04-v4.2, HB08-v4.2, TM03, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B02",
    "B09",
    "B02",
    "B11"
  ],
  "footer": "F02"
}
```

### PP-Min-Agostini-Oct25-CENT

- ID estable: `pp-min-agostini-oct25-cent`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Min-Agostini-Oct25-CENT/PP-Min-Agostini-Oct25-CENT.html`
- Vista front: `/example/pp-min-agostini-oct25-cent`
- API detalle: `/api/module1/examples/pp-min-agostini-oct25-cent`
- API HTML: `/api/module1/examples/pp-min-agostini-oct25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CIM02, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `PP-Min-Agostini-Oct25-CENT | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CIM02, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B03",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### PP-Spend-TBBM-Iphone17_CENT_dic25

- ID estable: `pp-spend-tbbm-iphone17-cent-dic25`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Spend-TBBM-Iphone17_CENT_dic25/PP-Spend-TBBM-Iphone17_CENT_dic25.html`
- Vista front: `/example/pp-spend-tbbm-iphone17-cent-dic25`
- API detalle: `/api/module1/examples/pp-spend-tbbm-iphone17-cent-dic25`
- API HTML: `/api/module1/examples/pp-spend-tbbm-iphone17-cent-dic25/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CTM03, CIM05, CIM05, CTM03, CIM03, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `PP-Spend-TBBM-Iphone17_CENT_dic25 | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CTM03, CIM05, CIM05, CTM03, CIM03, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B05",
    "B05",
    "B02",
    "B04",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### PP-Spend-TBBM-Iphone17_PLAT_dic25

- ID estable: `pp-spend-tbbm-iphone17-plat-dic25`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Spend-TBBM-Iphone17_PLAT_dic25/PP-Spend-TBBM-Iphone17_PLAT_dic25.html`
- Vista front: `/example/pp-spend-tbbm-iphone17-plat-dic25`
- API detalle: `/api/module1/examples/pp-spend-tbbm-iphone17-plat-dic25`
- API HTML: `/api/module1/examples/pp-spend-tbbm-iphone17-plat-dic25/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, HB08-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PP-Spend-TBBM-Iphone17_PLAT_dic25 | grupo=PP (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, IM03-v4.2, IM03-v4.2, TM04-v4.2, HB08-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B09",
    "B07",
    "B07",
    "B09",
    "B02"
  ],
  "footer": "F02"
}
```

### PP-Teatro-Colon-2026-Dic25-CENT

- ID estable: `pp-teatro-colon-2026-dic25-cent`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Teatro-Colon-2026-Dic25-CENT/PP-Teatro-Colon-2026-Dic25-CENT.html`
- Vista front: `/example/pp-teatro-colon-2026-dic25-cent`
- API detalle: `/api/module1/examples/pp-teatro-colon-2026-dic25-cent`
- API HTML: `/api/module1/examples/pp-teatro-colon-2026-dic25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CTM03, CTM03, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `PP-Teatro-Colon-2026-Dic25-CENT | grupo=PP (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CTM03, CTM03, CTM03, CTM03, CFM01, TM06, CFM02, CTM14, CFM03`
- Nota: El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B02",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### PP-Teatro-Colon-2026-Dic25-PLAT

- ID estable: `pp-teatro-colon-2026-dic25-plat`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/PP (Cent y Plat)/PP-Teatro-Colon-2026-Dic25-PLAT/PP-Teatro-Colon-2026-Dic25-PLAT.html`
- Vista front: `/example/pp-teatro-colon-2026-dic25-plat`
- API detalle: `/api/module1/examples/pp-teatro-colon-2026-dic25-plat`
- API HTML: `/api/module1/examples/pp-teatro-colon-2026-dic25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, FM05-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `PP-Teatro-Colon-2026-Dic25-PLAT | grupo=PP (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, FM05-v4.2, FM05-v4.2, FM05-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, FM02, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B09"
  ],
  "footer": "F02"
}
```

## TRAVEL (Cent y Plat)

### TRAVEL-Dia-De-La-Madre-Oct25-CENT

- ID estable: `travel-dia-de-la-madre-oct25-cent`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Dia-De-La-Madre-Oct25-CENT/TRAVEL-Dia-De-La-Madre-Oct25-CENT.html`
- Vista front: `/example/travel-dia-de-la-madre-oct25-cent`
- API detalle: `/api/module1/examples/travel-dia-de-la-madre-oct25-cent`
- API HTML: `/api/module1/examples/travel-dia-de-la-madre-oct25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01, BP01, CHB01, CIM03, CIM03, CIM03, CIM02, CTM02, CTM03, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `TRAVEL-Dia-De-La-Madre-Oct25-CENT | grupo=TRAVEL (Cent y Plat) | familia=centurion-1.0 | fidelidad=aproximada | sourceIds=PH01, BP01, CHB01, CIM03, CIM03, CIM03, CIM02, CTM02, CTM03, TM06, CFM02, CTM14, CFM03`
- Sustituciones aplicadas: `CTM02 -> B02`
- Nota: Se sustituyo CTM02 por B02 como el texto full-width mas cercano disponible.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B04",
    "B04",
    "B04",
    "B03",
    "B02",
    "B02"
  ],
  "footer": "F01"
}
```

### TRAVEL-Dia-De-La-Madre-Oct25-PLAT

- ID estable: `travel-dia-de-la-madre-oct25-plat`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Dia-De-La-Madre-Oct25-PLAT/TRAVEL-Dia-De-La-Madre-Oct25-PLAT.html`
- Vista front: `/example/travel-dia-de-la-madre-oct25-plat`
- API detalle: `/api/module1/examples/travel-dia-de-la-madre-oct25-plat`
- API HTML: `/api/module1/examples/travel-dia-de-la-madre-oct25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `TRAVEL-Dia-De-La-Madre-Oct25-PLAT | grupo=TRAVEL (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM04-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B09",
    "B02",
    "B02",
    "B02",
    "B02",
    "B09",
    "B10"
  ],
  "footer": "F02"
}
```

### TRAVEL-Mexico-Sept25-CENT

- ID estable: `travel-mexico-sept25-cent`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Mexico-Sept25-CENT/TRAVEL-Mexico-Sept25-CENT.html`
- Vista front: `/example/travel-mexico-sept25-cent`
- API detalle: `/api/module1/examples/travel-mexico-sept25-cent`
- API HTML: `/api/module1/examples/travel-mexico-sept25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01, BP01, CHB01, CTM03, CIM02, CTM03, CTM03, CIM02, CIM03, CIM02, CTM03, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `TRAVEL-Mexico-Sept25-CENT | grupo=TRAVEL (Cent y Plat) | familia=centurion-1.0 | fidelidad=estructural | sourceIds=PH01, BP01, CHB01, CTM03, CIM02, CTM03, CTM03, CIM02, CIM03, CIM02, CTM03, TM06, CFM02, CTM14, CFM03`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B03",
    "B02",
    "B02",
    "B03",
    "B04",
    "B03",
    "B02"
  ],
  "footer": "F01"
}
```

### TRAVEL-Mexico-Sept25-PLAT

- ID estable: `travel-mexico-sept25-plat`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Mexico-Sept25-PLAT/TRAVEL-Mexico-Sept25-PLAT.html`
- Vista front: `/example/travel-mexico-sept25-plat`
- API detalle: `/api/module1/examples/travel-mexico-sept25-plat`
- API HTML: `/api/module1/examples/travel-mexico-sept25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `TRAVEL-Mexico-Sept25-PLAT | grupo=TRAVEL (Cent y Plat) | familia=marigold-v4.2 | fidelidad=estructural | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, TM04-v4.2, HB08-v4.2, HB08-v4.2, HB08-v4.2, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B09",
    "B09",
    "B02",
    "B02",
    "B02",
    "B10"
  ],
  "footer": "F02"
}
```

### TRAVEL-Miami-Nov25-CENT

- ID estable: `travel-miami-nov25-cent`
- Estado en front: `Homologada`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Miami-Nov25-CENT/TRAVEL-Miami-Nov25-CENT.html`
- Vista front: `/example/travel-miami-nov25-cent`
- API detalle: `/api/module1/examples/travel-miami-nov25-cent`
- API HTML: `/api/module1/examples/travel-miami-nov25-cent/html`
- Familia: `centurion-1.0`
- Fidelidad: `estructural`
- SourceIds de referencia: `PH01, BP01, CHB01, CTM03, CIM02, CTM03, CIM02, CIM03, CTM03, TM06, CFM02, CTM14, CFM03`
- Resumen para agente: `TRAVEL-Miami-Nov25-CENT | grupo=TRAVEL (Cent y Plat) | familia=centurion-1.0 | fidelidad=estructural | sourceIds=PH01, BP01, CHB01, CTM03, CIM02, CTM03, CIM02, CIM03, CTM03, TM06, CFM02, CTM14, CFM03`

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "centurion-1.0",
  "header": "H01",
  "body": [
    "B01",
    "B02",
    "B03",
    "B02",
    "B03",
    "B04",
    "B02"
  ],
  "footer": "F01"
}
```

### TRAVEL-Miami-Nov25_PLAT

- ID estable: `travel-miami-nov25-plat`
- Estado en front: `Pendiente`
- Archivo: `1. Referencias por segmento/TRAVEL (Cent y Plat)/TRAVEL-Miami-Nov25_PLAT/TRAVEL-Miami-Nov25_PLAT.html`
- Vista front: `/example/travel-miami-nov25-plat`
- API detalle: `/api/module1/examples/travel-miami-nov25-plat`
- API HTML: `/api/module1/examples/travel-miami-nov25-plat/html`
- Familia: `marigold-v4.2`
- Fidelidad: `aproximada`
- SourceIds de referencia: `PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`
- Resumen para agente: `TRAVEL-Miami-Nov25_PLAT | grupo=TRAVEL (Cent y Plat) | familia=marigold-v4.2 | fidelidad=aproximada | sourceIds=PH01-v4.2, Consumer Default-v4.2, HB15-v4.2, TM04-v4.2, IM02-v4.0, IM02-v4.0, IM02-v4.0, TM06-v4.2, FM01-v4.2, TM06-v4.2, TM17-v4.2, FM03-v4.2, FM04-v4.2`
- Sustituciones aplicadas: `IM02-v4.0 -> B07, IM02-v4.0 -> B07, IM02-v4.0 -> B07`
- Nota: Se sustituyo IM02-v4.0 por B07 porque ese HTML mezcla shell v4.2 con un modulo heredado v4.0.
- Nota: Este caso mezcla modulos v4.2 con IM02-v4.0 dentro del mismo HTML.

Payload requerido para `compose-email`:

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H01",
  "body": [
    "B03",
    "B09",
    "B07",
    "B07",
    "B07",
    "B10"
  ],
  "footer": "F02"
}
```
