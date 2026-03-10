# Skill: Módulos Maquetados — Plataforma Marigold

## Descripción
Biblioteca de módulos HTML pre-maquetados para la plataforma **Marigold** (anteriormente Cheetah Digital), usada para el envío de emails de American Express Argentina. Cada archivo es un catálogo de variantes de un tipo de módulo.

**Archivos de referencia:**
- `B-Brand-Panels.html` → Variantes del Brand Panel (encabezado con logo y datos)
- `C-Hero-Banners-01.html` → Heros tipo 1 (overlay, background image)
- `C-Hero-Banners-02.html` → Heros tipo 2 (full width, text-only)
- `D-Image-Modules.html` → Módulos con imagen (pares, imagen+texto, galería)
- `E-Text-Modules.html` → Módulos de texto (offer code, lista de beneficios)
- `F-Footer-Modules.html` → Módulos de pie de email (tagline, social, legales)

**Template base:** `AMX_GBS Templates 4.2`
**Plataforma destino:** Marigold (SFMC-like, requiere tracking pixel)

---

## B — Brand Panels

Los brand panels son el **encabezado del email** después del preheader. Identifican el producto/segmento.

### Variantes disponibles

| ID | Descripción | Uso |
|---|---|---|
| `BP01-v4.2` | Solo logo Amex, sin tarjeta | Genérico / CORP |
| `BP02-v4.0` | Logo + tagline + tarjeta + "Hola {FNAME}" | AAPLUS (v4.0) |
| `Consumer Default-v4.2` | Logo + MR logo o solo logo + cuenta | MR, MERCHANT, ICS |
| `BP02-v4.2 Premium` | Logo + tagline + imagen tarjeta PLAT/CENT | PP, TRAVEL |

### Elementos del Brand Panel

```
[LOGO AMEX 60px] [TAGLINE IMAGEN] ................. [CUENTA TERMINA EN: {LAST_5}]
                                                     [MIEMBRO DESDE: {MEMBER_SINCE}]
                                                     [IMAGEN TARJETA 80x50px]
─────────────────────────────────────────────────────────────────────────────────
Hola, {(FNAME)} / {(FULLNAME)}                       [MI CUENTA btn]
```

### Snippets de brand panels → Ver skill `01-AAPLUS.md`, `05-MR.md`, `06-PP-Cent-Plat.md`

---

## C — Hero Banners

El Hero Banner es la primera imagen / sección visual del email, justo debajo del brand panel.

### C1: HB03-v4.2 — Overlay (imagen de fondo + texto superpuesto)

```html
<!-- HB03-v4.2: Background image con overlay de texto -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td align="center" bgcolor="#00175A"
        background="[URL_IMG_HERO_620x320]"
        width="620" height="320" valign="middle"
        style="background: url('[URL_IMG_HERO_620x320]') center / cover no-repeat #00175A;">
      <!--[if gte mso 9]>
      <v:image xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0;display:inline-block;width:620px;height:320px;"
        src="[URL_IMG_HERO_620x320]" />
      <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0;display:inline-block;position:absolute;width:620px;height:320px;">
        <v:fill opacity="0%" color="#00175A" />
        <v:textbox inset="0,0,0,0">
      <![endif]-->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="480" class="wrapper">
        <tr>
          <td align="center" style="padding:40px 20px;">
            <h1 style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                       font-size:36px; line-height:42px; margin:0 0 16px;">
              Título del hero
            </h1>
            <p style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:16px; line-height:24px; margin:0 0 24px;">
              Subtítulo o descripción breve.
            </p>
            <!-- CTA en hero -->
            <table role="none" cellpadding="0" cellspacing="0" border="0"
                   width="160" height="44" class="hero-button"
                   style="width:160px;height:44px;border-radius:4px;background:#FFFFFF;">
              <tr><td align="center" valign="middle">
                <a href="[URL_CTA]" target="_blank"
                   style="color:#00175A;display:inline-block;padding:12px 0;text-decoration:none;
                          width:156px;font-size:15px;line-height:22px;
                          font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                  <strong style="font-weight:normal;color:#00175A;">Conocer m&aacute;s</strong>
                </a>
              </td></tr>
            </table>
          </td>
        </tr>
      </table>
      <!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
    </td>
  </tr>
</table>
```

### C2: HB15-v4.2 — Full Width (imagen sola, sin texto superpuesto)

```html
<!-- HB15-v4.2: Full width image hero, texto abajo -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="[URL_CTA]" target="_blank" style="text-decoration:none;border:none;outline:0;">
        <img src="[URL_IMG_HERO_620px]" alt="[Alt descriptivo]" width="620"
             style="height:auto;display:block;color:#3D3D3D;" class="full-width">
      </a>
    </td>
  </tr>
  <!-- Texto debajo de la imagen -->
  <tr>
    <td bgcolor="#FFFFFF" align="center" style="padding:30px 40px 20px;">
      <h2 style="color:#00175A;font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                 font-size:26px;line-height:32px;font-weight:normal;margin:0 0 12px;">
        <strong>Título de la sección</strong>
      </h2>
      <p style="color:#3D3D3D;font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:15px;line-height:22px;margin:0 0 20px;">
        Descripción del beneficio o campaña.
      </p>
    </td>
  </tr>
</table>
```

---

## D — Image Modules

### IM03-v4.2: Vertical Pairs (2 columnas de imagen + texto)

Ver snippet completo en skill `02-CORP-MERCHANT-Comercio.md`.

**Cuándo usarlo:** Mostrar 2 ofertas/destinos/productos side by side.

### IM04-v4.2: Small Image + Text (imagen + bloque de texto lateral)

Ver snippet completo en skill `03-ICS.md`.

**Cuándo usarlo:** Evento con imagen + lista de beneficios o instrucciones.

### IM01-v4.2: Full Width Image (imagen única ancho completo)

```html
<!-- IM01-v4.2: Full Width Image -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="[URL]" target="_blank" style="text-decoration:none;border:none;outline:0;">
        <img src="[IMG_620px]" alt="[Alt]" width="620"
             style="height:auto;display:block;color:#3D3D3D;" class="full-width">
      </a>
    </td>
  </tr>
</table>
```

### IM03-v4.2: Pares Horizontales con fondo de color alternado

```html
<!-- Par con fondo gris + Par con fondo blanco (alternados) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <th width="305" class="full-width-block" valign="top" bgcolor="#F4F4F4" style="background:#F4F4F4;">
      <!-- Producto / Oferta 1 -->
      <img src="[IMG_1]" alt="[Alt 1]" width="305" style="height:auto;display:block;width:100%;" class="full-width">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr><td align="center" style="padding:20px;color:#00175A;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;font-size:18px;line-height:22px;">
          <strong>Nombre Producto 1</strong>
        </td></tr>
        <tr><td align="center" style="padding:0 20px 20px;color:#3D3D3D;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;">
          Descripción breve.
        </td></tr>
      </table>
    </th>
    <th width="305" class="full-width-block" valign="top" bgcolor="#FFFFFF" style="background:#FFFFFF;">
      <!-- Producto / Oferta 2 — misma estructura -->
    </th>
  </tr>
</table>
```

---

## E — Text Modules

### TM04-v4.2: Offer Code / Caja de Descuento

Ver snippet completo en skill `02-CORP-MERCHANT-Comercio.md`.

**Cuándo usarlo:** Resaltar un descuento porcentual grande (30%, 40% OFF) con período y condiciones.

### TM01-v4.2: Bloque de texto centrado (título + párrafo + CTA)

```html
<!-- TM01-v4.2: Text Block centered -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding:40px 40px 30px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center"
              style="color:#00175A;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                     font-size:26px;line-height:32px;padding-bottom:16px;">
            <strong>Título del módulo</strong>
          </td>
        </tr>
        <tr>
          <td align="center"
              style="color:#3D3D3D;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                     font-size:15px;line-height:22px;padding-bottom:24px;">
            Descripción del beneficio o información relevante para el titular.
          </td>
        </tr>
        <tr>
          <td align="center">
            <!-- Botón CTA -->
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="160" height="44"
                   style="width:160px;height:44px;border-radius:4px;background:#006FCF;" class="button-primary-light">
              <tr><td align="center" valign="middle">
                <table role="none" cellpadding="0" cellspacing="0" border="0"
                       style="border-radius:4px;border:2px solid #006FCF;width:156px;height:42px">
                  <tr><td align="center" valign="middle" height="44">
                    <a href="[URL]" target="_blank"
                       style="color:#FFFFFF;display:inline-block;padding:12px 0;text-decoration:none;
                              width:156px;font-size:15px;line-height:22px;
                              font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;">
                      <strong style="font-weight:normal;color:#FFFFFF;">Conoc&eacute; m&aacute;s</strong>
                    </a>
                  </td></tr>
                </table>
              </td></tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

### TM Lista de Beneficios (bullet con ícono)

```html
<!-- Lista de beneficios con íconos -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="padding:30px 40px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <!-- Beneficio 1 -->
        <tr>
          <td width="24" valign="top" style="padding-right:12px; padding-bottom:16px;">
            <img src="[ICONO_CHECK]" alt="✓" width="20" style="width:20px;height:auto;display:block;">
          </td>
          <td valign="top" style="padding-bottom:16px;
                                   color:#3D3D3D;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                                   font-size:15px;line-height:22px;">
            <strong style="color:#00175A;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;">
              Nombre del beneficio.
            </strong>
            Descripción adicional del beneficio.
          </td>
        </tr>
        <!-- Repetir para cada beneficio -->
      </table>
    </td>
  </tr>
</table>
```

---

## F — Footer Modules

### FM05-v4.2: Footer Tagline (estándar)

```html
<!-- START: FM05-v4.2 Footer Tagline -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FFFFFF;">
  <tr>
    <td align="center" style="padding:0; border-bottom:none;">
      <!-- Tagline imagen -->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#00175A" style="background:#00175A;">
        <tr>
          <td align="center" style="padding:30px 40px;">
            <img src="[IMG_TAGLINE_FOOTER]" alt="No vivas la vida sin ella" width="200"
                 style="height:auto;display:block;color:#FFFFFF;" class="RespImg">
          </td>
        </tr>
      </table>
      <!-- Redes sociales -->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
        <tr>
          <td align="center" style="padding:20px 0;">
            <table role="none" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="padding:0 8px;">
                  <a href="https://www.facebook.com/AmericanExpressArgentina" target="_blank" style="text-decoration:none;border:none;outline:0;">
                    <img src="[ICONO_FACEBOOK]" alt="Facebook" width="32" style="width:32px;height:32px;display:block;">
                  </a>
                </td>
                <td style="padding:0 8px;">
                  <a href="https://www.instagram.com/amexargentina/" target="_blank" style="text-decoration:none;border:none;outline:0;">
                    <img src="[ICONO_INSTAGRAM]" alt="Instagram" width="32" style="width:32px;height:32px;display:block;">
                  </a>
                </td>
                <td style="padding:0 8px;">
                  <a href="https://twitter.com/AmexArgentina" target="_blank" style="text-decoration:none;border:none;outline:0;">
                    <img src="[ICONO_TWITTER]" alt="Twitter/X" width="32" style="width:32px;height:32px;display:block;">
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <!-- Texto legal -->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
        <tr>
          <td align="center" style="padding:20px 40px 30px;">
            <p style="color:#333333;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                      font-size:11px;line-height:16px;margin:0 0 8px;">
              <sup>1</sup> [Legal del beneficio 1]. Consulte T&eacute;rminos y Condiciones en
              <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/" target="_blank"
                 style="color:#333333;text-decoration:underline;">americanexpress.com.ar</a>
            </p>
            <p style="color:#333333;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                      font-size:11px;line-height:16px;margin:0 0 8px;">
              Para darse de baja de las comunicaciones de American Express haga
              <a href="{{unsubscribeLink}}" style="color:#333333;text-decoration:underline;">clic aqu&iacute;</a>.
            </p>
            <p style="color:#333333;font-family:HelveticaNeue,Helvetica Neue Regular,Helvetica,Arial,sans-serif;
                      font-size:11px;line-height:16px;margin:0;">
              &copy; [AÑO] American Express Company. Todos los derechos reservados.
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: FM05-v4.2 Footer Tagline -->
```

---

## Resumen de IDs de Módulos Marigold

| Prefijo | Módulo | Variantes comunes |
|---|---|---|
| `PH01` | Preheader | v4.0, v4.2 |
| `BP02` | Brand Panel | v4.0 (tarjeta), Consumer Default v4.2 |
| `HB03` | Hero Overlay | v4.0, v4.2 |
| `HB15` | Hero Full Width | v4.2 |
| `IM01` | Image Full Width | v4.2 |
| `IM03` | Image Pairs Vertical | v4.2 |
| `IM04` | Image Small + Text | v4.2 |
| `TM01` | Text Block | v4.2 |
| `TM04` | Offer Code / Descuento | v4.2 |
| `FM05` | Footer Tagline | v4.2 |

---

## Notas de Plataforma Marigold

- Requiere **SFMC tracking pixel**: `<custom name="opencounter" type="tracking"/>`
- Variables de personalización con sintaxis `{(NOMBRE_VARIABLE)}`
- URL de desuscripción: `{{unsubscribeLink}}`
- URL viewer (ver en navegador): `https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}`
- Imágenes hosteadas en: `https://i.email.americanexpress.com/wpm/[ID]/Images/`
