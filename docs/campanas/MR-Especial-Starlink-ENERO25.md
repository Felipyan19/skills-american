# MR-Especial-Starlink-ENERO25

Campana exacta de modulo 1 para MR. Usa `marigold-v4.2` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H09",
  "body": [
    "B52",
    "B53",
    "B54",
    "B55"
  ],
  "footer": "F10"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MR",
  "campaignType": "especial-starlink"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H09` |
| Body | `B52 -> B53 -> B54 -> B55` |
| Footer | `F10` |
