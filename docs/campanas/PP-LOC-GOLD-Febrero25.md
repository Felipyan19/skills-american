# PP-LOC-GOLD-Febrero25

Campana exacta de modulo 1 para AAPLUS. Usa `marigold-v4.0` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.0",
  "header": "H02",
  "body": [
    "B05",
    "B06",
    "B07",
    "B08",
    "B09",
    "B10",
    "B11"
  ],
  "footer": "F01"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.0",
  "group": "AAPLUS",
  "campaignType": "loc-gold"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H02` |
| Body | `B05 -> B06 -> B07 -> B08 -> B09 -> B10 -> B11` |
| Footer | `F01` |
