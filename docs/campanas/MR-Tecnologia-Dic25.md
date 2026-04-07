# MR-Tecnologia-Dic25

Campana exacta de modulo 1 para MR. Usa `marigold-v4.2` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H11",
  "body": [
    "B61",
    "B62",
    "B63",
    "B64",
    "B65"
  ],
  "footer": "F12"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MR",
  "campaignType": "tecnologia"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H11` |
| Body | `B61 -> B62 -> B63 -> B64 -> B65` |
| Footer | `F12` |
