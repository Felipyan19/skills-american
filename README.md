# Skills — Agente de Generación HTML American Express Argentina

## Propósito
Esta carpeta contiene los skills para un agente de IA que genera emails HTML de American Express Argentina. Cada skill documenta las convenciones, estructura, componentes y ejemplos de código de un segmento o plataforma específica.

---

## Estructura de Skills

```
skills/
├── README.md                          ← Este archivo (índice)
├── 00-base-template.md                ← Boilerplate base + componentes comunes
│
├── segmentos/
│   ├── 01-AAPLUS.md                   ← Gold LOC / Platinum LOC (v4.0)
│   ├── 02-CORP-MERCHANT-Comercio.md   ← Corporativo + Comercios
│   ├── 03-ICS.md                      ← International Card Services
│   ├── 04-MERCHANT-Socio.md           ← Merchant Socio (Newsletter, Shots, Special Offers)
│   ├── 05-MR.md                       ← Membership Rewards (canje de puntos)
│   ├── 06-PP-Cent-Plat.md             ← Centurion + Platinum Premium
│   └── 07-TRAVEL-Cent-Plat.md         ← Travel para Centurion y Platinum
│
└── modulos/
    ├── 08-Marigold.md                  ← Biblioteca de módulos plataforma Marigold
    └── 09-Click-Experts-Centurion.md   ← Biblioteca de módulos plataforma Click Experts
```

---

## Guía de Uso Rápido

### ¿Qué skill usar según el email a generar?

| Tipo de email | Skills a consultar |
|---|---|
| Email Gold LOC / Platinum LOC | `00-base-template` + `01-AAPLUS` |
| Email corporativo o de comercio | `00-base-template` + `02-CORP-MERCHANT-Comercio` |
| Email ICS (eventos exclusivos) | `00-base-template` + `03-ICS` |
| Newsletter o Shot de comercios | `00-base-template` + `04-MERCHANT-Socio` |
| Email de canje de puntos MR | `00-base-template` + `05-MR` |
| Email de beneficios Centurion/Plat | `00-base-template` + `06-PP-Cent-Plat` |
| Email de viajes Centurion/Plat | `00-base-template` + `07-TRAVEL-Cent-Plat` |
| Módulo puntual para Marigold | `08-Marigold` |
| Módulo puntual para Click Experts | `09-Click-Experts-Centurion` |

---

## Workflow del Agente

```
1. IDENTIFICAR segmento → ¿A quién va dirigido? (AAPLUS, CORP, ICS, MR, PP, TRAVEL, MERCHANT)
2. LEER skill base (00) → boilerplate, colores, fuentes, tokens de personalización
3. LEER skill del segmento → brand panel específico, variantes, estructura típica
4. IDENTIFICAR tipo de email → Newsletter / Shot / Spend&Earn / Dining / Travel / etc.
5. LEER skill de módulos → seleccionar módulos según el contenido (hero, image pairs, offer code, etc.)
6. GENERAR HTML → ensamblar los componentes en el orden correcto
7. VERIFICAR → preheader, tracking pixel, tokens, legales, URLs de CTA
```

---

## Decisiones Clave al Generar

### ¿Qué template version usar?
- **v4.0** → Solo para AAPLUS (Gold LOC, Plat LOC). Fondo `#D9D9D6`
- **v4.2** → Todos los demás segmentos. Fondo `#E0E0E0`
- **Centurion Pack 1.0** → Solo Click Experts Centurion. Fondo oscuro/negro

### ¿Qué color de botón CTA usar?
- **`#006FCF`** (azul brillante) → MR, MERCHANT, ICS, CORP, AAPLUS
- **`#00175A`** (azul profundo) → PP Centurion, PP Platinum, TRAVEL

### ¿Qué brand panel usar?
- Con imagen de tarjeta → AAPLUS (BP02-v4.0), PP Premium (Consumer Default v4.2 + card)
- Sin tarjeta, con logo MR → MR (doble logo: Amex + MR)
- Sin tarjeta, simple → CORP, ICS, MERCHANT
- Oscuro/negro → Centurion (Click Experts)

### ¿Incluir tracking pixel?
- **Siempre** → `<custom name="opencounter" type="tracking"/>` en `<div style="display:none;">`

### ¿Qué token de saludo usar?
- `{(FNAME)}` → Consumer estándar (AAPLUS, v4.0)
- `{(FULLNAME)}` → Consumer v4.2 (MR, PP, ICS, MERCHANT)
- Sin saludo personalizado → CORP (emails corporativos)

---

## Paleta de Colores (referencia rápida)

| Color | Hex | Uso |
|---|---|---|
| Azul profundo Amex | `#00175A` | Textos principales PP/Cent, botones PP/Travel |
| Azul brillante Amex | `#006FCF` | Botones CTA consumer, links, puntos MR |
| Gris fondo v4.2 | `#E0E0E0` | Body background estándar |
| Gris fondo v4.0 | `#D9D9D6` | Body background AAPLUS |
| Blanco | `#FFFFFF` | Área de contenido |
| Gris texto | `#3D3D3D` | Texto body general |
| Gris alternativo | `#333333` | Texto footer, preheader |
| Gris claro hover | `#F4F4F4` | Hover botón secundario, separadores |
| Dorado Centurion | `#C9A84C` | Eyebrow/accent en emails Centurion |

---

## Componentes Comunes (siempre en 00-base-template)

- HTML boilerplate completo
- Importación de fuentes web (Guardian Egyptian, BentonSans)
- CSS resets y Mobile Media Queries
- Preheader (PH01-v4.2)
- Separador
- Botón primario azul
- Tokens de personalización
- Entidades HTML para acentos españoles
