# Arquitectura de campanas, dashboard y MDs

Este documento explica de donde salen los estados del dashboard y como se relacionan con los archivos `docs/campanas/*.md`.

## Fuentes de datos

| Fuente | Uso |
|---|---|
| `catalog/examples/module1.json` | Inventario principal de campanas del dashboard: nombre, grupo, `campaignType`, familia, fidelidad y payload base. |
| `docs/campanas/README.md` | Router para agentes. Mapea una campana del inventario a un MD real cuando existe. |
| `docs/campanas/<Campana>.md` | Contrato dedicado para una campana: payload base, payload por `group/campaignType`, mapa de componentes y, si aplica, variantes por `props`. |
| `server/http_server.py` | Une inventario + router + MDs para exponer `dashboardStatus`, `campaignDoc` y markdown de detalle. |
| `server/registry.py` | Define los componentes reales, sus snippets y defaults. Una prop solo funciona si esta implementada en registry y en el snippet. |

## MD real vs markdown generado

El dashboard puede mostrar una pagina de detalle para cualquier campana, aunque no exista un archivo MD real.

| Caso | `markdownSource` | `campaignDoc` | Que significa |
|---|---|---|---|
| Existe `docs/campanas/<Campana>.md` y el router lo apunta | `campaign-doc` | Nombre del MD | El agente puede leer un contrato dedicado. |
| No existe MD real o el router dice `sin doc` | `generated` | `""` | El servidor genera una vista basica desde `module1.json`; no es un archivo de contrato. |

Por eso una campana podia verse en el dashboard antes de tener MD: se estaba mostrando el fallback generado por `_module1_example_markdown`.

## Como se calcula `dashboardStatus`

El status se calcula por campana en `server/http_server.py`:

1. Se busca una fila del router en `docs/campanas/README.md` que coincida por:
   - nombre de campana,
   - `group`,
   - `campaignType`.
2. Si el router apunta a un archivo `.md`, se carga ese doc como `campaignDoc`.
3. Si ese MD contiene marcadores de variantes, la campana queda como `dinamico`.
4. Si no tiene variantes pero `fidelity` en `module1.json` es `alta`, queda como `exacto`.
5. Si no es `alta`, queda como `pendiente`.

`pendiente` no significa "sin salida". Significa que no hay contrato exacto dedicado o que el caso sigue resolviendose con payloads estructurales/aproximados. Para esos casos, el fallback operativo vive en `docs/campanas/generic.md`.

Marcadores que convierten un MD en dinamico:

- `Edicion version corta`
- `Edicion corta desde tipo de campana y grupo`
- `Campos de variantes`
- `aceptan variantes por `props``

No agregar esos marcadores a MDs exactos basicos, porque cambiarian el status a `dinamico` sin que las props esten implementadas.

## Por que el router usa nombre + group + campaignType

Algunas campanas comparten `group` y `campaignType`, pero no tienen el mismo estado ni el mismo template. Ejemplo:

| Campana | group | campaignType | Estado |
|---|---|---|---|
| `PP-Teatro-Colon-2026-Dic25-CENT` | `PP (Cent y Plat)` | `teatro-colon` | `pendiente` |
| `PP-Teatro-Colon-2026-Dic25-PLAT` | `PP (Cent y Plat)` | `teatro-colon` | `exacto` |

Por eso `_load_campaign_docs_index` mapea por `(name, group, campaignType)`. Si solo mapeara por `(group, campaignType)`, una variante podria heredar el MD de otra.

## Tipos de MD

### MD exacto basico

Usar para campanas que ya se ven como `exacto` en el dashboard pero todavia no tienen contrato dedicado.

Debe incluir:

- `Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.`
- `Payload base`
- `Payload por grupo y tipo`
- `Mapa de componentes`

No debe incluir:

- `Edicion version corta`
- `Edicion corta desde tipo de campana y grupo`
- `Campos de variantes`

### MD dinamico

Usar cuando la campana ya soporta variantes reales por `props` en snippets y `server/registry.py`.

Debe incluir:

- `Status API: `dinamico`. ... aceptan variantes por `props`.`
- `Version corta`
- `Edicion version corta`
- `Version corta desde tipo de campana y grupo`
- `Edicion corta desde tipo de campana y grupo`
- `Detallada`
- `Contrato de edicion`
- `Mapa de componentes`
- `Campos de variantes`

## Reglas para agentes

1. Leer primero `.agents/skills/exact-campaign-md/SKILL.md`.
2. Leer `docs/campanas/README.md`.
3. Elegir una fila del router por evidencia del PDF.
4. Si la fila tiene MD real, leer `docs/campanas/<Doc>`.
5. Si la fila dice `sin doc`, si la campana sigue `pendiente`, o si no hay una fila fuerte, leer `.agents/skills/generic-campaign-fallback/SKILL.md` y `docs/campanas/generic.md`.
6. Solo despues del fallback global usar docs generales de segmento/modulo para reforzar la decision.
7. Para payloads de `/api/compose-email`, usar `id`, nunca `componentId`.
8. No incluir `role` ni `snippet` dentro de `header`, `body` o `footer`.
9. No usar props no documentadas o no implementadas.

## Comandos utiles de verificacion

```bash
python - <<'PY'
from server.http_server import _module1_examples_response
payload = _module1_examples_response()
print(payload["summary"])
for item in payload["examples"]:
    print(item["name"], item["dashboardStatus"], item.get("campaignDoc", ""))
PY
```

```bash
python -m unittest tests.test_composer tests.test_http_api
```
