# Campanas exactas de /api/compose-email

Estos archivos documentan campanas especificas que `/api/compose-email` puede armar desde los ejemplos de modulo 1. La regla para esta carpeta es simple: si una campana usa componentes hardcodeados y tiene fidelidad `alta`, debe tener un `.md` propio con su payload, orden de componentes y reglas de edicion.

## Router para agentes

Este archivo es el punto de entrada fijo para agentes externos. Primero leer este indice, elegir una fila por evidencia y despues leer el `Doc` correspondiente.

| Campana | group | campaignType | Señales fuertes | Doc |
|---|---|---|---|---|
| MERCHANT-Shot-Travel-Agst25 | `MERCHANT - Socio` | `shot-travel` | travel, viaje, agosto, Aerolineas, Despegar, Al Mundo, hoteles, spa, `1908-MERCHANT-Shot-Travel-Agst25` | `MERCHANT-Shot-Travel-Agst25.md` |
| MERCHANT-Newsletter-Dic25 | `MERCHANT - Socio` | `newsletter` | newsletter, diciembre, compras, gastronomia, hoteles, Shopping Days, PedidoYa Plus, NH, `271125_MERCHANT-Newsletter-Dic25` | `MERCHANT-Newsletter-Dic25.md` |
| MERCHANT-Shot-deporte-DIC25 | `MERCHANT - Socio` | `shot-deporte` | deporte, diciembre, entrenar, Megatlon, Fiter, Decathlon, Lasaigues, padel, `101225-MERCHANT-Shot-deporte-DIC25` | `MERCHANT-Shot-deporte-DIC25.md` |
| MERCHANT-SHOT-Navidad-Dic25 | `MERCHANT - Socio` | `shot-navidad` | navidad, regalos, indumentaria, perfumeria, diciembre, `MERCHANT-SHOT-Navidad-Dic25` | `MERCHANT-SHOT-Navidad-Dic25.md` |
| MERCHANT-Special-Offers-Dic25 | `MERCHANT - Socio` | `special-offers` | special offers, diciembre, wine, winestore, Ninja, Samsung, Garmin, `MERCHANT-Special-Offers-Dic25` | `MERCHANT-Special-Offers-Dic25.md` |

Si dos filas parecen posibles o la evidencia es debil, no inventar. Leer el `.md` de cada candidata y elegir la que tenga payload y snippets compatibles con el input.

## Campanas documentadas

| Campana | Fidelity | Status | Doc |
|---|---|---|---|
| MERCHANT-Shot-Travel-Agst25 | `alta` | `exacto` | `MERCHANT-Shot-Travel-Agst25.md` |
| MERCHANT-Newsletter-Dic25 | `alta` | `exacto` | `MERCHANT-Newsletter-Dic25.md` |
| MERCHANT-Shot-deporte-DIC25 | `alta` | `exacto` | `MERCHANT-Shot-deporte-DIC25.md` |
| MERCHANT-SHOT-Navidad-Dic25 | `alta` | `exacto` | `MERCHANT-SHOT-Navidad-Dic25.md` |
| MERCHANT-Special-Offers-Dic25 | `alta` | `exacto` | `MERCHANT-Special-Offers-Dic25.md` |

## Reglas generales

- Estas campanas no son templates genericos: la mayor parte del contenido vive en snippets HTML dedicados. Cuando un `.md` liste `Variantes por props`, esos campos pueden sobrescribirse desde `/api/compose-email`.
- Para editar una pieza exacta, modificar el snippet especifico de la campana, no el componente generico con el mismo `sourceId`.
- Mantener `globals.includeSeparators: false`; estas piezas ya traen su espaciado interno.
- Si cambia el orden, se agrega o se quita un bloque, actualizar tambien el payload del ejemplo correspondiente en `catalog/examples/module1.json` y el override en `scripts/generate_examples.py`.
- Validar que los legales y los numeros de referencia sigan alineados con los claims visuales del cuerpo.
- Preservar los tokens de Marigold usados por el HTML, por ejemplo `{(FULLNAME)}`, `{(EMAIL)}` y `{(URLSignature1)}`.
