# Fallback global para campanas pendientes o no identificadas

Este documento se usa cuando `docs/campanas/README.md` no ofrece un MD exacto util, la fila del router esta en `sin doc`, la campana figura como `pendiente`, o la evidencia del PDF no alcanza para un match exacto.

## Objetivo

Devolver un payload valido de `/api/compose-email` lo mas cercano posible al PDF sin inventar componentes, sin dejar la campana sin match y sin prometer snippets exactos que todavia no existen.

## Orden de lectura obligatorio

1. `docs/campanas/README.md`
2. `.agents/skills/generic-campaign-fallback/SKILL.md`
3. `catalog/examples/module1.md`
4. `docs/README.md` y `docs/segmentos/*.md` solo para reforzar la eleccion
5. `docs/modulos/*.md` solo si hace falta confirmar el rol de un bloque

## Reglas duras

- No inventar `id`, `header`, `body`, `footer`, `templateFamily`, `group` ni `campaignType`.
- Reutilizar primero un payload real de `catalog/examples/module1.md`.
- Si hay varios candidatos, priorizar en este orden:
  1. mismo `group`
  2. mismo `campaignType`
  3. misma `templateFamily`
  4. mismo ritmo visual: hero unico, listado, grilla, pares, cierre legal
- Preferir un ejemplo `estructural` sobre uno `aproximada` cuando ambos sirvan.
- Usar `aproximada` solo si el mejor caso conocido ya es aproximado o el catalogo documenta sustituciones.
- Setear `matched_campaign` con el nombre del ejemplo realmente reutilizado. No dejarlo vacio.
- Incluir `docs/campanas/generic.md` en `skills_read` o mencionarlo dentro de `notes`.
- Mantener `needs_snippet_edit = false` salvo que la mejor solucion pida un snippet no publico o una prop no implementada.
- Toda la trazabilidad va dentro de `notes`.

## Como decidir la familia

### `centurion-1.0`

Usar cuando el PDF tiene varias de estas senales:

- fondo oscuro o negro
- tono ultra premium
- menciones explicitas a Centurion
- hero full width oscuro o con fotografia premium

### `marigold-v4.0`

Usar solo para AAPLUS LOC:

- menciones a Gold LOC o Platinum LOC
- look mas viejo de AAPLUS
- estructura clasica con muchos modulos `IM02`

### `marigold-v4.2`

Usar para el resto:

- CORP, ICS, MERCHANT, MR, PP Platinum, Travel Platinum
- fondo gris `#E0E0E0`
- header consumer comun

## Como elegir el arquetipo mas cercano

| Senal principal | Familia recomendada | Ejemplo a clonar primero | Segundo candidato |
|---|---|---|---|
| CORP, Instagram, redes, seguridad | `marigold-v4.2` | `CORP-IG-Sep25` | `CORP-Travel-Octubre25` |
| CORP, travel, agencias, aerolineas, destinos | `marigold-v4.2` | `CORP-Travel-Octubre25` | `CORP-Special-Offers-Navidad-Dic25` |
| CORP, special offers, multiples categorias, lista de comercios | `marigold-v4.2` | `CORP-Special-Offers-Navidad-Dic25` | `CORP-Travel-Octubre25` |
| ICS, evento, preventa, entradas, F1, beneficio puntual | `marigold-v4.2` | `PP-F1-Miami-Preventa-ICS-oct25` | `PP-Diderot-Nov25-ICS` |
| ICS, comercio o propuesta puntual con hero y pares | `marigold-v4.2` | `PP-Diderot-Nov25-ICS` | `PP-F1-Miami-Preventa-ICS-oct25` |
| MERCHANT, newsletter, varias categorias, compras, gastronomia, hoteles | `marigold-v4.2` | `MERCHANT-Newsletter-Dic25` | `MERCHANT-Special-Offers-Dic25` |
| MERCHANT, shot, una promo principal, travel, deporte o temporada | `marigold-v4.2` | `MERCHANT-Shot-Travel-Agst25` | `MERCHANT-Shot-deporte-DIC25` |
| MERCHANT, special offers, catalogo, productos o comercios | `marigold-v4.2` | `MERCHANT-Special-Offers-Dic25` | `MERCHANT-Newsletter-Dic25` |
| MR, puntos, canje, productos, tecnologia, hero + grilla | `marigold-v4.2` | `MR-Tecnologia-Dic25` | `MR-Especial-Starlink-ENERO25` |
| MR, bebidas, vinos, gastronomia, lifestyle | `marigold-v4.2` | `MR-Especial-bebidas-DIC25` | `MR-MFF-La-Gueya-Nov25` |
| PP Platinum, spend, premio, ecommerce, iPhone, retail | `marigold-v4.2` | `PP-Spend-TBBM-Iphone17_PLAT_dic25` | `PLAT-Spend-Farmacity-Oct25` |
| PP Platinum, dining o experiencia gastronomica | `marigold-v4.2` | `PP-Dining-Ultramarino-Nov25-PLAT` | `TRAVEL-Miami-Nov25_PLAT` |
| PP Centurion, dining o experiencia premium con fondo oscuro | `centurion-1.0` | `PP-Dining-Ultramarino-Nov25-CENT` | `PP-Cata-Piedra-Pasillo-OCT25` |
| PP Centurion, evento, teatro, acceso, invitacion | `centurion-1.0` | `PP-Teatro-Colon-2026-Dic25-CENT` | `PP-Cata-Piedra-Pasillo-OCT25` |
| PP Centurion, spend o premio con fondo oscuro | `centurion-1.0` | `PP-Spend-TBBM-Iphone17_CENT_dic25` | `PP-Min-Agostini-Oct25-CENT` |
| Travel Platinum, destinos, aereos, hoteles, hero claro | `marigold-v4.2` | `TRAVEL-Mexico-Sept25-PLAT` | `TRAVEL-Miami-Nov25_PLAT` |
| Travel Centurion, destinos, hoteles, fondo oscuro | `centurion-1.0` | `TRAVEL-Mexico-Sept25-CENT` | `TRAVEL-Miami-Nov25-CENT` |

## Heuristicas de desempate

Si dos candidatos parecen buenos, elegir el que cumpla mas puntos:

1. mismo `group`
2. mismo `campaignType`
3. misma familia visual (`centurion-1.0`, `marigold-v4.2`, `marigold-v4.0`)
4. misma cantidad aproximada de bloques
5. misma logica del cuerpo:
   - hero unico
   - hero + texto
   - hero + pares
   - grilla de ofertas
   - varios cierres o legales intermedios
6. misma polaridad visual:
   - oscuro/premium
   - consumer claro

## Como reportar el fallback en la salida

Cuando uses este documento:

- `matched_campaign`: nombre del ejemplo reutilizado, por ejemplo `PP-Dining-Ultramarino-Nov25-CENT`
- `confidence`:
  - `alta` solo si terminaste usando un MD exacto real con evidencia fuerte
  - `estructural` si el payload viene de un ejemplo valido del mismo grupo o de la misma familia y no requiere sustituciones extra
  - `aproximada` solo si el propio ejemplo ya es aproximado o el catalogo advierte sustituciones
- `needs_snippet_edit`: `false` mientras el payload siga siendo valido con componentes publicos
- `notes`: explicar por que se eligio ese ejemplo y que elementos visuales lo vuelven el mejor fallback

## Reglas especiales por segmento

### MERCHANT - Socio

- Si no hay match exacto por nombre pero el patron es claro, si se puede caer a una campana exacta existente.
- Newsletter: usar `MERCHANT-Newsletter-Dic25`.
- Shot: usar `MERCHANT-Shot-Travel-Agst25` o `MERCHANT-Shot-deporte-DIC25` segun la evidencia.
- Special Offers: usar `MERCHANT-Special-Offers-Dic25`.

### MR

- Preferir ejemplos con logo MR y cuerpo de canje.
- Si hay precios en puntos y varias cards de producto, empezar por `MR-Tecnologia-Dic25`.
- Si la evidencia es gastronomica o de vinos, considerar `MR-Especial-bebidas-DIC25` o `MR-MFF-La-Gueya-Nov25`.

### PP / TRAVEL

- Distinguir primero Centurion vs Platinum.
- Si es Centurion, no mezclar un payload de Platinum salvo que no exista otra opcion con la misma familia.
- Si es Platinum, priorizar `marigold-v4.2` con `H01` o el ejemplo publico ya homologado del catalogo.

## Ultimo recurso

Si no hay una campana exacta ni un candidato muy fuerte, usar igual el ejemplo mas cercano del mismo `group` y `templateFamily` en `catalog/examples/module1.md`.

Es mejor devolver un payload valido y rastreable a un ejemplo existente que dejar `matched_campaign` vacio o fabricar una estructura nueva.
