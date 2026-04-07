# MR-Especial-bebidas-DIC25

Campana exacta de modulo 1 para MR. Usa `marigold-v4.2` y el orden base documentado por el dashboard.

Status API: `exacto`. Payload base disponible; no documenta variantes por `props`.

## Payload base

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H10",
  "body": [
    "B56",
    "B57",
    "B58",
    "B59",
    "B60"
  ],
  "footer": "F11"
}
```

## Payload por grupo y tipo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MR",
  "campaignType": "especial-bebidas"
}
```

## Mapa de componentes

| Slot | Componentes |
|---|---|
| Header | `H10` |
| Body | `B56 -> B57 -> B58 -> B59 -> B60` |
| Footer | `F11` |
