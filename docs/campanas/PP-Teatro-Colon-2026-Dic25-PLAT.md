# PP-Teatro-Colon-2026-Dic25-PLAT

Campana exacta de modulo 1 para PP (Cent y Plat). Usa `marigold-v4.2` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H08",
  "body": [
    "B50",
    "B51"
  ],
  "footer": "F09"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "PP (Cent y Plat)",
  "campaignType": "teatro-colon"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H08` |
| Body | `B50 -> B51` |
| Footer | `F09` |
