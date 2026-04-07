# PP-LOC-PLAT-Febrero25

Campana exacta de modulo 1 para AAPLUS. Usa `marigold-v4.0` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.0",
  "header": "H03",
  "body": [
    "B12",
    "B13",
    "B14",
    "B15",
    "B16",
    "B17",
    "B18"
  ],
  "footer": "F01"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.0",
  "group": "AAPLUS",
  "campaignType": "loc-plat"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H03` |
| Body | `B12 -> B13 -> B14 -> B15 -> B16 -> B17 -> B18` |
| Footer | `F01` |
