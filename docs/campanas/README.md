# Campanas exactas de /api/compose-email

Estos archivos documentan campanas especificas que `/api/compose-email` puede armar desde los ejemplos de modulo 1. La regla para esta carpeta es simple: si una campana usa componentes hardcodeados y tiene fidelidad `alta`, debe tener un `.md` propio con su payload, orden de componentes y reglas de edicion.

## Router para agentes

Este archivo es el punto de entrada fijo para agentes externos. Primero leer este indice, elegir una fila por evidencia y despues leer el `Doc` correspondiente.

Antes de reconstruir o editar payloads, leer tambien `.agents/skills/exact-campaign-md/SKILL.md`. Si la campana no esta marcada como `dinamico` y se necesitan variantes por `props`, leer `.agents/skills/exact-campaign-api/SKILL.md` para confirmar que requiere trabajo de snippets/registry antes de prometer edicion dinamica.

Para entender la diferencia entre MD real, markdown generado, `campaignDoc` y `dashboardStatus`, leer `docs/campanas/ARQUITECTURA.md`.

| Campana | group | campaignType | Señales fuertes | Doc |
|---|---|---|---|---|
| PP-LOC-GOLD-Febrero25 | `AAPLUS` | `loc-gold` | loc, gold, febrero, AAPLUS | `PP-LOC-GOLD-Febrero25.md` |
| PP-LOC-PLAT-Febrero25 | `AAPLUS` | `loc-plat` | loc, plat, febrero, AAPLUS | `PP-LOC-PLAT-Febrero25.md` |
| CORP-IG-Sep25 | `CORP y MERCHANT Comercio` | `ig` | corp, merchant comercio, IG, septiembre | `sin doc` |
| CORP-Special-Offers-Navidad-Dic25 | `CORP y MERCHANT Comercio` | `corp-special-offers-navidad` | corp, special offers, navidad, diciembre | `sin doc` |
| CORP-Travel-Octubre25 | `CORP y MERCHANT Comercio` | `travel` | corp, travel, octubre, viajes | `sin doc` |
| PP-Diderot-Nov25-ICS | `ICS` | `diderot` | ICS, Diderot, noviembre | `sin doc` |
| PP-F1-Miami-Preventa-ICS-oct25 | `ICS` | `f1-miami-preventa` | ICS, F1, Miami, preventa, octubre | `sin doc` |
| MERCHANT-Shot-Travel-Agst25 | `MERCHANT - Socio` | `shot-travel` | travel, viaje, agosto, Aerolineas, Despegar, Al Mundo, hoteles, spa, `1908-MERCHANT-Shot-Travel-Agst25` | `MERCHANT-Shot-Travel-Agst25.md` |
| MERCHANT-Newsletter-Dic25 | `MERCHANT - Socio` | `newsletter` | newsletter, diciembre, compras, gastronomia, hoteles, Shopping Days, PedidoYa Plus, NH, `271125_MERCHANT-Newsletter-Dic25` | `MERCHANT-Newsletter-Dic25.md` |
| MERCHANT-Shot-deporte-DIC25 | `MERCHANT - Socio` | `shot-deporte` | deporte, diciembre, entrenar, Megatlon, Fiter, Decathlon, Lasaigues, padel, `101225-MERCHANT-Shot-deporte-DIC25` | `MERCHANT-Shot-deporte-DIC25.md` |
| MERCHANT-SHOT-Navidad-Dic25 | `MERCHANT - Socio` | `shot-navidad` | navidad, regalos, indumentaria, perfumeria, diciembre, `MERCHANT-SHOT-Navidad-Dic25` | `MERCHANT-SHOT-Navidad-Dic25.md` |
| MERCHANT-Special-Offers-Dic25 | `MERCHANT - Socio` | `merchant-special-offers` | special offers, diciembre, wine, winestore, Ninja, Samsung, Garmin, `MERCHANT-Special-Offers-Dic25` | `MERCHANT-Special-Offers-Dic25.md` |
| MR-Especial-bebidas-DIC25 | `MR` | `especial-bebidas` | MR, bebidas, diciembre | `MR-Especial-bebidas-DIC25.md` |
| MR-Especial-Starlink-ENERO25 | `MR` | `especial-starlink` | MR, Starlink, enero | `MR-Especial-Starlink-ENERO25.md` |
| MR-MFF-La-Gueya-Nov25 | `MR` | `mff-la-gueya` | MR, MFF, La Gueya, noviembre | `sin doc` |
| MR-Tecnologia-Dic25 | `MR` | `tecnologia` | MR, tecnologia, diciembre | `MR-Tecnologia-Dic25.md` |
| MR-Bonus-Smiles-Dic25-CENT | `PP (Cent y Plat)` | `bonus-smiles` | centurion, bonus smiles, diciembre, fondo negro | `sin doc` |
| MR-Bonus-Smiles-Dic25-PLAT | `PP (Cent y Plat)` | `bonus-smiles` | platinum, bonus smiles, diciembre | `sin doc` |
| PLAT-Spend-Farmacity-Oct25 | `PP (Cent y Plat)` | `spend-farmacity` | plat, farmacity, get the look, simplicity, the food market, octubre, `1909-PLAT-Spend-Farmacity-Oct25` | `PLAT-Spend-Farmacity-Oct25.md` |
| PP-Cata-Piedra-Pasillo-OCT25 | `PP (Cent y Plat)` | `cata-piedra-pasillo` | centurion, cata, Piedra Pasillo, octubre, fondo negro | `sin doc` |
| PP-Dining-Ultramarino-Nov25-CENT | `PP (Cent y Plat)` | `dining-ultramarino` | centurion, dining, Ultramarino, noviembre, fondo negro | `sin doc` |
| PP-Dining-Ultramarino-Nov25-PLAT | `PP (Cent y Plat)` | `dining-ultramarino` | platinum, dining, Ultramarino, noviembre | `sin doc` |
| PP-Min-Agostini-Oct25-CENT | `PP (Cent y Plat)` | `min-agostini` | centurion, Min Agostini, octubre, fondo negro | `sin doc` |
| PP-Spend-TBBM-Iphone17_CENT_dic25 | `PP (Cent y Plat)` | `spend-tbbm-iphone17` | centurion, TBBM, iPhone 17, diciembre, fondo negro | `sin doc` |
| PP-Spend-TBBM-Iphone17_PLAT_dic25 | `PP (Cent y Plat)` | `spend-tbbm-iphone17` | platinum, TBBM, iPhone 17, diciembre | `sin doc` |
| PP-Teatro-Colon-2026-Dic25-CENT | `PP (Cent y Plat)` | `teatro-colon` | centurion, Teatro Colon, 2026, diciembre, fondo negro | `sin doc` |
| PP-Teatro-Colon-2026-Dic25-PLAT | `PP (Cent y Plat)` | `teatro-colon` | platinum, Teatro Colon, 2026, diciembre | `PP-Teatro-Colon-2026-Dic25-PLAT.md` |
| TRAVEL-Dia-De-La-Madre-Oct25-CENT | `TRAVEL (Cent y Plat)` | `dia-de-la-madre` | centurion, dia de la madre, octubre, travel, fondo negro | `sin doc` |
| TRAVEL-Dia-De-La-Madre-Oct25-PLAT | `TRAVEL (Cent y Plat)` | `dia-de-la-madre` | platinum, dia de la madre, octubre, travel | `sin doc` |
| TRAVEL-Mexico-Sept25-CENT | `TRAVEL (Cent y Plat)` | `mexico` | centurion, Mexico, septiembre, travel, fondo negro | `sin doc` |
| TRAVEL-Mexico-Sept25-PLAT | `TRAVEL (Cent y Plat)` | `mexico` | platinum, Mexico, septiembre, travel | `sin doc` |
| TRAVEL-Miami-Nov25-CENT | `TRAVEL (Cent y Plat)` | `miami` | centurion, Miami, noviembre, travel, fondo negro | `sin doc` |
| TRAVEL-Miami-Nov25_PLAT | `TRAVEL (Cent y Plat)` | `miami` | platinum, Miami, noviembre, travel | `sin doc` |

Si dos filas parecen posibles o la evidencia es debil, no inventar. Leer el `.md` de cada candidata y elegir la que tenga payload y snippets compatibles con el input. Si la fila dice `sin doc`, no inventar un MD: usar los docs generales de segmento/modulo o marcar que falta documentacion exacta.

## Inventario dashboard

| Campana | Familia | Fidelity | Status dashboard | Doc |
|---|---|---|---|---|
| PP-LOC-GOLD-Febrero25 | `marigold-v4.0` | `alta` | `exacto` | `PP-LOC-GOLD-Febrero25.md` |
| PP-LOC-PLAT-Febrero25 | `marigold-v4.0` | `alta` | `exacto` | `PP-LOC-PLAT-Febrero25.md` |
| CORP-IG-Sep25 | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| CORP-Special-Offers-Navidad-Dic25 | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| CORP-Travel-Octubre25 | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| PP-Diderot-Nov25-ICS | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| PP-F1-Miami-Preventa-ICS-oct25 | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| MERCHANT-Newsletter-Dic25 | `marigold-v4.2` | `alta` | `exacto` | `MERCHANT-Newsletter-Dic25.md` |
| MERCHANT-Shot-deporte-DIC25 | `marigold-v4.2` | `alta` | `dinamico` | `MERCHANT-Shot-deporte-DIC25.md` |
| MERCHANT-SHOT-Navidad-Dic25 | `marigold-v4.2` | `alta` | `exacto` | `MERCHANT-SHOT-Navidad-Dic25.md` |
| MERCHANT-Shot-Travel-Agst25 | `marigold-v4.2` | `alta` | `dinamico` | `MERCHANT-Shot-Travel-Agst25.md` |
| MERCHANT-Special-Offers-Dic25 | `marigold-v4.2` | `alta` | `exacto` | `MERCHANT-Special-Offers-Dic25.md` |
| MR-Especial-bebidas-DIC25 | `marigold-v4.2` | `alta` | `exacto` | `MR-Especial-bebidas-DIC25.md` |
| MR-Especial-Starlink-ENERO25 | `marigold-v4.2` | `alta` | `exacto` | `MR-Especial-Starlink-ENERO25.md` |
| MR-MFF-La-Gueya-Nov25 | `marigold-v4.2` | `aproximada` | `pendiente` | `sin doc` |
| MR-Tecnologia-Dic25 | `marigold-v4.2` | `alta` | `exacto` | `MR-Tecnologia-Dic25.md` |
| MR-Bonus-Smiles-Dic25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| MR-Bonus-Smiles-Dic25-PLAT | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| PLAT-Spend-Farmacity-Oct25 | `marigold-v4.2` | `alta` | `dinamico` | `PLAT-Spend-Farmacity-Oct25.md` |
| PP-Cata-Piedra-Pasillo-OCT25 | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| PP-Dining-Ultramarino-Nov25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| PP-Dining-Ultramarino-Nov25-PLAT | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| PP-Min-Agostini-Oct25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| PP-Spend-TBBM-Iphone17_CENT_dic25 | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| PP-Spend-TBBM-Iphone17_PLAT_dic25 | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| PP-Teatro-Colon-2026-Dic25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| PP-Teatro-Colon-2026-Dic25-PLAT | `marigold-v4.2` | `alta` | `exacto` | `PP-Teatro-Colon-2026-Dic25-PLAT.md` |
| TRAVEL-Dia-De-La-Madre-Oct25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| TRAVEL-Dia-De-La-Madre-Oct25-PLAT | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| TRAVEL-Mexico-Sept25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| TRAVEL-Mexico-Sept25-PLAT | `marigold-v4.2` | `estructural` | `pendiente` | `sin doc` |
| TRAVEL-Miami-Nov25-CENT | `centurion-1.0` | `estructural` | `pendiente` | `sin doc` |
| TRAVEL-Miami-Nov25_PLAT | `marigold-v4.2` | `aproximada` | `pendiente` | `sin doc` |

## Reglas generales

- El contrato de `/api/compose-email` usa `id`, no `componentId`. Un componente editable debe tener la forma `{ "id": "B28", "props": { ... } }`.
- No incluir `role` ni `snippet` dentro del payload final de `/api/compose-email`; esos datos son documentacion para decidir estructura, no campos del API.
- Estas campanas no son templates genericos: la mayor parte del contenido vive en snippets HTML dedicados. Cuando un `.md` liste `Variantes por props`, esos campos pueden sobrescribirse desde `/api/compose-email`.
- Para editar una pieza exacta, modificar el snippet especifico de la campana, no el componente generico con el mismo `sourceId`.
- Mantener `globals.includeSeparators: false`; estas piezas ya traen su espaciado interno.
- Si cambia el orden, se agrega o se quita un bloque, actualizar tambien el payload del ejemplo correspondiente en `catalog/examples/module1.json` y el override en `scripts/generate_examples.py`.
- Validar que los legales y los numeros de referencia sigan alineados con los claims visuales del cuerpo.
- Preservar los tokens de Marigold usados por el HTML, por ejemplo `{(FULLNAME)}`, `{(EMAIL)}` y `{(URLSignature1)}`.
