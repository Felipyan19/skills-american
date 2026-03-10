# Skill: Módulos Maquetados — Click Experts (Centurion)

## Descripción
Biblioteca de módulos HTML para la plataforma **Click Experts**, usada para los emails del segmento **Centurion** de American Express Argentina. Tiene su propio sistema de CSS classes y estructura diferente a Marigold.

**Archivos de referencia:**
- `B-Brand-Panels.html` → Brand panels estilo Centurion
- `C-Hero-Banners.html` → Heros Centurion (fondo oscuro, tipografía elegante)
- `D-Image-Modules.html` → Módulos de imagen Centurion
- `E-Text-Modules.html.html` → Módulos de texto Centurion
- `F-Footer-Modules.html` → Footer Centurion

**Template base:** `AMX_GBS Centurion Pack 1.0`
**Breakpoint mobile:** `max-width: 619px`

---

## Diferencias Clave vs Marigold

| Característica | Marigold (v4.2) | Click Experts (Centurion) |
|---|---|---|
| Template ID | `AMX_GBS Templates 4.2` | `AMX_GBS Centurion Pack 1.0` |
| Arquitectura CSS | Classes utilitarias (`full-width-block`, etc.) | Sistema propio (`im-block`, `tm-block`, `fm-nav`) |
| Fondo predominante | Blanco `#FFFFFF` | Negro / oscuro |
| Tipografía primaria | BentonSans, Helvetica | Guardian Egyptian, tipografía serif elegante |
| Paleta | `#00175A`, `#006FCF` | Negro, dorado, blanco |
| Samsung fix | `@media (max-width: 480px)` extra | Incluido |
| Yahoo fix | No | `@media screen yahoo` incluido |
| `.row-display-mobile` | No | Sí |

---

## Head y CSS Base Centurion

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:v="urn:schemas-microsoft-com:vml"
      xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <title>Centurion</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="author" content="AMX_GBS Centurion Pack 1.0" />

  <style type="text/css">
    #outlook a { padding: 0; }
    .ReadMsgBody { width: 100%; }
    .ExternalClass { width: 100%; }
    .ExternalClass * { line-height: 100%; }

    #MessageViewBody, #MessageWebViewDiv {
      min-width: 100vw; margin: 0 !important; zoom: 1 !important;
    }

    span.MsoHyperlink { mso-style-priority: 99; color: inherit; }
    span.MsoHyperlinkFollowed { mso-style-priority: 99; color: inherit; }

    a[x-apple-data-detectors='true'] {
      color: inherit !important; text-decoration: inherit !important;
    }

    /* Yahoo fix */
    @media screen yahoo {
      * { overflow: visible !important; }
      .y-overflow-hidden { overflow: hidden !important; }
      .hb-mobile-only { display: none !important; }
    }

    /* Mobile (619px) */
    @media only screen and (max-width: 619px) {
      u ~ div { min-width: 95vw; }

      .wrapper { margin: 0 auto; width: 100% !important; max-width: 800px !important; }
      .logo-hide { height: 0 !important; display: none !important; }

      .ph-text {
        width: 100% !important; display: block !important;
        font-size: 12px !important; line-height: 16px !important;
        text-align: center !important;
      }

      .full-width { width: 100% !important; }
      .full-height { height: 100% !important; }

      .show-desktop { display: none !important; font-size: 0 !important; max-height: 0 !important; line-height: 0 !important; mso-hide: all !important; }
      .show-mobile { display: block !important; }
      .no-padding-mobile { padding: 0 !important; }
      .text-centre-mobile { text-align: center !important; }
      .small-padding-mobile { padding-bottom: 10px !important; }

      /* Celda display mobile */
      .cell-display-mobile { display: block !important; width: 84% !important; padding: 30px 8% !important; }
      .cta-display-mobile { display: block !important; width: 230px !important; margin: 0 auto !important; text-align: center !important; }
      .row-display-mobile { display: table-row !important; }
      .mobile-display-block { display: block !important; }

      /* Image modules */
      .im-horz-pair-padding { padding: 10px !important; }
      .im-block, .im-gutter { width: 100% !important; }
      .im-block, .im-block-auto { height: auto !important; display: block !important; }
      .im-gutter { height: 40px !important; display: block !important; }

      /* Text modules */
      .tm-block, .tm-heading { clear: left !important; display: block !important; }
      .tm-block { margin: 0 auto 40px; }
      .h1 { font-size: 24px !important; line-height: 32px !important; }
      .tm-heading { width: 100% !important; }
      .tm-gap-filler { width: 20px !important; }
      .tm-gutter { height: 0 !important; max-height: 0 !important; display: none !important; line-height: 0 !important; }

      /* Footer modules */
      .fm-nav { padding: 0 !important; }
      .fm-nav-link-container { width: 100% !important; }
      .fm-nav-link { width: 100% !important; display: inline-block !important; padding: 15px 0 !important; text-align: center !important; }
      .fm-border { border-top: 1px solid #63666a !important; }
      .fm-cross-icon { display: inline-block !important; padding: 0 0 24px !important; width: 50% !important; text-align: center !important; }
      .fm-cross-container { padding: 33px 0 8px !important; }
    }

    .row-display-mobile { display: none; mso-hide: all; }
    .show-mobile { display: none; mso-hide: all; }
  </style>

  <!-- Samsung fix -->
  <style>
    @media screen and (max-width: 480px) {
      #MessageViewBody, #MessageWebViewDiv { min-width: 100vw; margin: 0 !important; zoom: 1 !important; }
    }
  </style>
</head>
```

---

## B — Brand Panels Centurion

El brand panel del Centurion es más austero y elegante. Fondo negro o muy oscuro con logo Amex en blanco.

```html
<!-- Brand Panel Centurion (oscuro) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width:620px;" class="wrapper">
  <tr>
    <td bgcolor="#000000" style="background:#000000; padding:20px 30px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <!-- Logo Amex (versión blanca para fondo oscuro) -->
          <td width="60" valign="middle">
            <a href="http://www.americanexpress.com.ar" target="_blank">
              <img src="[IMG_LOGO_AMEX_WHITE]" alt="American Express" width="60"
                   style="width:60px; height:auto; color:#FFFFFF; display:block;">
            </a>
          </td>
          <!-- Tagline Centurion -->
          <td valign="middle" style="padding-left:15px;" class="logo-hide">
            <img src="[IMG_TAGLINE_CENTURION]" alt="The Centurion Card" width="150"
                 style="width:150px; height:auto; color:#FFFFFF;">
          </td>
          <!-- Datos cuenta (texto blanco) -->
          <td align="right" valign="middle">
            <p style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:14px; line-height:20px; margin:0;">
              Tu cuenta termina en: {(LAST_5)}<br>
              <span class="show-desktop">Miembro desde: {(MEMBER_SINCE)}</span>
            </p>
          </td>
          <!-- Tarjeta Centurion (negra) -->
          <td align="right" valign="middle" width="80" style="padding-left:12px;">
            <img src="[IMG_CENTURION_CARD]" alt="The Centurion Card&reg;" width="80"
                 style="height:50px; width:80px; display:block;">
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- Saludo en fila separada -->
  <tr>
    <td bgcolor="#111111" style="background:#111111; padding:12px 30px;
                                  border-top:1px solid #333333;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td>
            <p style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:15px; line-height:22px; margin:0;">
              Hola {(FULLNAME)}
            </p>
          </td>
          <td align="right">
            <a href="https://www.americanexpress.com/es-ar/account/login?email_consumer"
               target="_blank"
               style="border:1px solid #FFFFFF; border-radius:3px; color:#FFFFFF;
                      display:inline-block; font-size:14px; line-height:100%;
                      padding:10px 14px; text-decoration:none; text-align:center;
                      font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              Mi cuenta
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## C — Hero Banners Centurion

Los heros del Centurion son cinematográficos: imágenes de alta calidad, tipografía serif elegante, mucho espacio en blanco / negro.

```html
<!-- Hero Centurion — Fondo oscuro con imagen y serif -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td bgcolor="#000000" style="background:#000000;">
      <!-- Imagen hero full width -->
      <a href="[URL_CTA]" target="_blank" style="text-decoration:none;border:none;outline:0;">
        <img src="[IMG_HERO_CENTURION]" alt="[Alt]" width="620"
             style="height:auto;display:block;width:100%;" class="full-width">
      </a>
    </td>
  </tr>
  <!-- Texto debajo de la imagen (sobre negro) -->
  <tr>
    <td bgcolor="#000000" style="background:#000000; padding:40px 50px;" align="center">
      <!-- Eyebrow / categoría en oro/blanco -->
      <p style="color:#C9A84C; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:12px; line-height:18px; letter-spacing:3px; text-transform:uppercase; margin:0 0 16px;">
        EXCLUSIVO CENTURION
      </p>
      <!-- Título serif -->
      <h1 style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                 font-size:38px; line-height:46px; font-weight:normal; margin:0 0 20px;">
        Título del beneficio exclusivo
      </h1>
      <!-- Subtítulo -->
      <p style="color:#CCCCCC; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:16px; line-height:24px; margin:0 0 32px;">
        Descripci&oacute;n del beneficio para The Centurion Card.
      </p>
      <!-- CTA (contorno blanco sobre negro) -->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="180" style="margin:0 auto;"
             class="cta-display-mobile">
        <tr>
          <td align="center" valign="middle"
              style="border:1px solid #FFFFFF; border-radius:2px; padding:14px 20px;">
            <a href="[URL_CTA]" target="_blank"
               style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:14px; line-height:20px; text-decoration:none; letter-spacing:1px;
                      display:block; text-align:center;">
              CONOCER M&Aacute;S
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## D — Image Modules Centurion

### Pares de imagen (`.im-block`)

```html
<!-- IM Centurion — Pares con clase im-block -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#000000">
  <tr>
    <!-- Item 1 -->
    <td class="im-block" width="290" valign="top" align="center"
        style="width:290px; padding:20px;">
      <a href="[URL_1]" target="_blank" style="text-decoration:none;border:none;outline:0;">
        <img src="[IMG_1]" alt="[Alt 1]" width="250"
             class="im-block-auto full-width"
             style="height:auto; display:block; color:#FFFFFF; max-width:250px;">
      </a>
      <p style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                font-size:18px; line-height:24px; margin:16px 0 8px; text-align:center;">
        Nombre del item 1
      </p>
      <p style="color:#AAAAAA; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:14px; line-height:20px; margin:0; text-align:center;">
        Descripción breve.
      </p>
    </td>
    <!-- Gutter (oculto en mobile) -->
    <td class="im-gutter" width="40" style="width:40px; font-size:1px; line-height:1px;">&nbsp;</td>
    <!-- Item 2 -->
    <td class="im-block" width="290" valign="top" align="center"
        style="width:290px; padding:20px;">
      <!-- misma estructura -->
    </td>
  </tr>
</table>
```

---

## E — Text Modules Centurion

### Bloque de texto con fondo oscuro (`.tm-block`)

```html
<!-- TM Centurion — Bloque de contenido texto -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#111111">
  <tr>
    <td class="tm-block" style="padding:50px 60px;" align="center">
      <!-- Título serif -->
      <h2 class="h1 tm-heading"
          style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                 font-size:32px; line-height:40px; font-weight:normal; margin:0 0 20px;
                 text-align:center;">
        Título del módulo de texto
      </h2>
      <!-- Párrafo body -->
      <p style="color:#CCCCCC; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:15px; line-height:22px; margin:0 0 30px; text-align:center;">
        Descripci&oacute;n del beneficio o experiencia exclusiva para titulares
        de The Centurion Card.
      </p>
      <!-- Steps / pasos (horizontal en desktop, vertical en mobile) -->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <!-- Paso 1 -->
          <td class="tm-vert-step" width="33%" valign="top" align="center"
              style="width:33%; padding:0 10px;">
            <img src="[ICONO_PASO_1]" alt="1" width="48"
                 style="width:48px; height:auto; display:block; margin:0 auto 12px;">
            <p style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:14px; line-height:20px; margin:0; text-align:center;">
              <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                Paso 1
              </strong><br>
              Descripción del primer paso.
            </p>
          </td>
          <!-- Spacer (tm-gap-filler) -->
          <td class="tm-gap-filler" width="20" style="width:20px; font-size:1px;">&nbsp;</td>
          <!-- Paso 2 -->
          <td class="tm-vert-step" width="33%" valign="top" align="center"
              style="width:33%; padding:0 10px;">
            <!-- misma estructura -->
          </td>
          <td class="tm-gap-filler" width="20" style="width:20px; font-size:1px;">&nbsp;</td>
          <!-- Paso 3 -->
          <td class="tm-vert-step" width="33%" valign="top" align="center"
              style="width:33%; padding:0 10px;">
            <!-- misma estructura -->
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## F — Footer Modules Centurion

El footer del Centurion tiene un estilo más minimalista y oscuro.

```html
<!-- Footer Centurion -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#000000">
  <tr>
    <!-- Navegación de links (unsubscribe, privacy, etc.) -->
    <td class="fm-nav" style="padding:24px 30px 0;" align="center">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td class="fm-nav-link-container" width="33%" align="center"
              style="width:33%; border-right:1px solid #444444;">
            <a class="fm-nav-link" href="https://www.americanexpress.com/es-ar/privacidad/" target="_blank"
               style="color:#AAAAAA; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:11px; line-height:16px; text-decoration:none; display:inline-block; padding:0 10px;">
              Privacidad
            </a>
          </td>
          <td class="fm-nav-link-container" width="33%" align="center"
              style="width:33%; border-right:1px solid #444444;">
            <a class="fm-nav-link" href="{{unsubscribeLink}}" target="_blank"
               style="color:#AAAAAA; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:11px; line-height:16px; text-decoration:none; display:inline-block; padding:0 10px;">
              Darse de baja
            </a>
          </td>
          <td class="fm-nav-link-container" width="34%" align="center" style="width:34%;">
            <a class="fm-nav-link" href="https://www.americanexpress.com.ar" target="_blank"
               style="color:#AAAAAA; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:11px; line-height:16px; text-decoration:none; display:inline-block; padding:0 10px;">
              americanexpress.com.ar
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- Legales -->
  <tr>
    <td class="fm-border" style="border-top:1px solid #333333; padding:20px 30px;" align="center">
      <p style="color:#666666; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:10px; line-height:15px; margin:0 0 8px; text-align:center;">
        <sup>1</sup> [Legal del beneficio 1].
      </p>
      <p style="color:#666666; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:10px; line-height:15px; margin:0; text-align:center;">
        &copy; [AÑO] American Express Company. Todos los derechos reservados.
      </p>
    </td>
  </tr>
  <!-- Redes sociales (cross-promotion) -->
  <tr>
    <td class="fm-cross-container" style="padding:24px 30px 8px;" align="center">
      <table role="none" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td class="fm-cross-icon" style="padding:0 12px;">
            <a class="fm-cross-link" href="[URL_INSTAGRAM]" target="_blank"
               style="text-decoration:none; border:none; outline:0;">
              <img src="[ICONO_IG_WHITE]" alt="Instagram" width="28"
                   style="width:28px; height:28px; display:inline-block;">
            </a>
          </td>
          <td class="fm-cross-icon" style="padding:0 12px;">
            <a class="fm-cross-link" href="[URL_FACEBOOK]" target="_blank"
               style="text-decoration:none; border:none; outline:0;">
              <img src="[ICONO_FB_WHITE]" alt="Facebook" width="28"
                   style="width:28px; height:28px; display:inline-block;">
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Resumen de Classes CSS Click Experts

| Clase | Propósito |
|---|---|
| `.wrapper` | Contenedor principal (620px, 100% mobile) |
| `.im-block` | Módulo de imagen (100% wide en mobile) |
| `.im-gutter` | Espacio entre módulos de imagen (oculto mobile) |
| `.im-block-auto` | Imagen auto-width en mobile |
| `.tm-block` | Módulo de texto (full width, centrado mobile) |
| `.tm-heading` | Título del módulo texto |
| `.tm-gap-filler` | Gap entre elementos de texto (reducido mobile) |
| `.tm-vert-step` | Paso en lista horizontal (block en mobile) |
| `.fm-nav` | Navegación del footer |
| `.fm-nav-link-container` | Celda del nav link |
| `.fm-nav-link` | Link individual del nav |
| `.fm-border` | Borde superior de sección del footer |
| `.fm-cross-icon` | Ícono de red social en footer |
| `.fm-cross-container` | Contenedor de redes en footer |
| `.cell-display-mobile` | Celda que se hace block en mobile |
| `.cta-display-mobile` | CTA centrado en mobile |
| `.show-desktop` | Oculto en mobile |
| `.show-mobile` | Oculto en desktop |
| `.logo-hide` | Logo secundario oculto en mobile |

---

## Notas de Plataforma Click Experts

- El template Centurion usa tipografía **Guardian Egyptian** (serif) para títulos — más prominente que en Marigold
- El color dorado `#C9A84C` se usa como acento para el branding Centurion
- Los fondos son oscuros (negro, `#111111`) a diferencia del blanco de Marigold
- El gutter (`.im-gutter`) entre columnas de imagen se oculta completamente en mobile (height: 0)
- Los pasos (`.tm-vert-step`) se reorganizan en columna en mobile automáticamente
- Variables de personalización: mismo sistema `{(NOMBRE)}` que Marigold
- Links de desuscripción: `{{unsubscribeLink}}`
