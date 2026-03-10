# Skill Base: Plantilla HTML de Emails American Express

## Descripción
Todos los emails de American Express Argentina usan una arquitectura basada en tablas HTML, compatible con clientes de correo (Outlook, Gmail, Apple Mail, Samsung Email). El contenedor principal es de **620px** de ancho, responsive a **619px** o menos.

---

## Versiones de Template

| Versión | Autor meta | Fondo body | Uso |
|---|---|---|---|
| v4.0 | `AMX_GBS Templates 4.0` | `#D9D9D6` | AAPLUS (LOC cards) |
| v4.2 | `AMX_GBS Templates 4.2` | `#E0E0E0` | Todos los demás segmentos |
| Centurion 1.0 | `AMX_GBS Centurion Pack 1.0` | `#000000` / oscuro | Click Experts (Centurion) |

---

## Paleta de Colores

```
#00175A  →  Azul profundo Amex (textos premium, títulos, botones PP/Cent)
#006FCF  →  Azul brillante Amex (botones CTA, links)
#E0E0E0  →  Gris fondo body (v4.2)
#D9D9D6  →  Gris cálido fondo body (v4.0)
#FFFFFF  →  Blanco (área de contenido)
#3D3D3D  →  Gris oscuro (texto body)
#333333  →  Gris texto alternativo
#F4F4F4  →  Gris claro (hover botones secundarios, separadores)
```

---

## Tipografías

```css
/* Web fonts (solo en @media screen) */
@font-face { font-family: 'Guardian Egyptian'; /* serif, títulos */ }
@font-face { font-family: 'BentonSans300'; font-weight: 300; }
@font-face { font-family: 'BentonSans400'; font-weight: 400; }
@font-face { font-family: 'BentonSans500'; font-weight: 500; }

/* Fallback stack */
font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
```

---

## Boilerplate HTML Completo

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml"
      xmlns:v="urn:schemas-microsoft-com:vml"
      xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <!-- BEGIN SUBJECT LINE PREVIEW TEXT LOCATION #1 -->
  <title>AMEX</title>
  <!-- END SUBJECT LINE PREVIEW TEXT LOCATION #1 -->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="AMX_GBS Templates 4.2">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
  <meta name="x-apple-disable-message-reformatting">
  <link rel="icon" type="image/png" href="https://www.americanexpress.com/favicon.ico" sizes="32x32">

  <!-- Web Fonts -->
  <style>
    @media screen {
      @font-face {
        font-family: 'Guardian Egyptian';
        font-style: normal; font-weight: 400;
        src: url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/guardianregular.woff2) format('woff2'),
             url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/guardianregular.woff) format('woff');
      }
      @font-face {
        font-family: 'BentonSans300'; font-style: normal; font-weight: 300;
        src: url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/325e6ad0-38fb-4bad-861c-d965eab101d5-3.woff2) format('woff2'),
             url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/325e6ad0-38fb-4bad-861c-d965eab101d5-3.woff) format('woff');
      }
      @font-face {
        font-family: 'BentonSans400'; font-style: normal; font-weight: 400;
        src: url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/3be50273-0b2e-4aef-ae68-882eacd611f9-3.woff2) format('woff2');
      }
      @font-face {
        font-family: 'BentonSans500'; font-style: normal; font-weight: 500;
        src: url(https://www.aexp-static.com/cdaas/one/statics/@americanexpress/dls-fonts/1.1.0/package/dist/fonts/0fababca-4914-46dd-9b0f-efbd51f67ae8-3.woff2) format('woff2');
      }
    }
  </style>

  <!--[if mso]>
  <style>
    li { text-align: -webkit-match-parent; display: list-item !important; text-indent: -1em !important; }
    a { text-decoration: none !important; }
  </style>
  <xml>
    <o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings>
  </xml>
  <![endif]-->

  <!-- Base styles -->
  <style>
    * { margin: 0; padding: 0; font-family: Helvetica Neue, Helvetica, Arial, sans-serif; }
    body { background-color: #E0E0E0; width: 100%; }
    table { mso-table-lspace: 0; mso-table-rspace: 0; }
    .body { word-wrap: normal; word-spacing: normal; }
    div[style*="margin: 16px 0"] { margin: 0 !important; }
    th { font-weight: normal !important; }
    h1, h2, h3 { font-weight: normal; }
    sup, sub { font-size: 0.65em !important; position: relative !important; vertical-align: baseline !important; }
    sup { top: -0.4em !important; }
    sub { top: 0.4em !important; }
    .link:hover { text-decoration: underline !important; }
    [class^="button"] { transition: all .2s ease-in-out !important; }
    .button-primary-light:hover { background-color: #00175A !important; }
    .button-primary-dark:hover { background-color: rgba(255,255,255,0.90) !important; }
    .button-secondary-light:hover { background-color: #F4F4F4 !important; }
    .button-secondary-dark:hover { background-color: rgba(0,0,0,0.05) !important; }
    #MessageViewBody, #MessageWebViewDiv { min-width: 100vw; margin: 0 !important; zoom: 1 !important; width: 100% !important; }
    *:focus { outline-color: #006FCF; outline-style: solid; outline-offset: 4px; outline-width: 2px; border-radius: 1px; }
  </style>

  <!-- Link resets -->
  <style>
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; }
    #MessageViewBody a { color: inherit !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; text-decoration: none !important; }
    u+.body a { color: inherit; text-decoration: none; font-size: inherit; font-weight: inherit; line-height: inherit; }
    span.MsoHyperlink { color: inherit !important; mso-style-priority: 99 !important; }
    span.MsoHyperlinkFollowed { color: inherit !important; mso-style-priority: 99 !important; }
  </style>

  <!-- Mobile styles -->
  <style>
    @media only screen and (max-width: 619px) {
      .show-desktop { display: none !important; font-size: 0 !important; max-height: 0 !important; line-height: 0 !important; mso-hide: all !important; }
      .wrapper { margin: 0 auto; width: 100% !important; max-width: 619px !important; min-width: 310px !important; padding: 0 !important; }
      .container { padding: 0 !important; width: 100% !important; }
      .full-width { width: 100% !important; }
      .full-width-block, .cell-display-mobile { width: 100% !important; display: block !important; }
      .half-width-block { width: 50% !important; display: inline-block !important; vertical-align: top; }
      .height-auto { height: auto !important; }
      .mobile-off { display: none !important; height: 0px !important; width: 0px !important; }
      .mobile-on, .mobile-display-block { display: block !important; }
      .pd0 { padding: 0 !important; }
      .pd10 { padding: 10px !important; }
      .pd20 { padding: 20px !important; }
      .pd40 { padding: 40px !important; }
      .pdbtm0 { padding-bottom: 0px !important; }
      .pdbtm30 { padding-bottom: 30px !important; }
      .pdtop20 { padding-top: 20px !important; }
      .pdtop40 { padding-top: 40px !important; }
      .center-text { text-align: center !important; }
      .hero-button { width: 230px !important; }
      /* Custom helpers */
      .TxtBlue { color: #00175a !important; }
      .hideMbl { display: none !important; }
      .showMbl { display: inline-block !important; }
      .Separator { background: #F4F4F4 !important; font-size: 0 !important; line-height: 10px !important; }
      .Separator TD { height: 10px !important; }
    }
  </style>
</head>

<body style="margin: 0 auto !important; padding: 0; background: #E0E0E0" class="body">

  <!-- Samsung Email Margin Fix -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin: 0 auto !important;">
    <tr><td><div align="center">

  <!-- SFMC Tracking Pixel (REQUIRED - DO NOT REMOVE) -->
  <div style="display:none;">
    <custom name="opencounter" type="tracking"/>
  </div>

  <div role="article" aria-roledescription="email" aria-label="Email from American Express"
       lang="en" dir="ltr"
       style="font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-weight: normal; font-size: 15px; line-height: 22px;">

    <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: #E0E0E0">
      <tr><td align="center">

        <!-- ===== HEADER SECTION ===== -->
        <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
          <tr><td align="center" bgcolor="#E0E0E0">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width: 620px;" class="container">
              <tr><td>
                <!-- [PREHEADER] -->
                <!-- [BRAND PANEL] -->
              </td></tr>
            </table>
          </td></tr>
        </table>
        <!-- ===== END HEADER ===== -->

        <!-- ===== CONTENT SECTION ===== -->
        <table role="none" cellpadding="0" cellspacing="0" border="0" width="620"
               style="width: 620px; background: #ffffff" class="container">
          <tr><td>
            <!-- [HERO BANNER] -->
            <!-- [CONTENT MODULES] -->
            <!-- [FOOTER] -->
          </td></tr>
        </table>
        <!-- ===== END CONTENT ===== -->

      </td></tr>
    </table>
  </div>

    </div></td></tr>
  </table>
</body>
</html>
```

---

## Tokens de Personalización (SFMC)

| Token | Descripción |
|---|---|
| `{(FNAME)}` | Nombre del titular |
| `{(FULLNAME)}` | Nombre completo |
| `{(LAST_5)}` | Últimos 5 dígitos de la cuenta |
| `{(MEMBER_SINCE)}` | Fecha de membresía |
| `{(URLSignature1)}` | URL firmada para el link "ver en web" |

---

## Componente: Preheader (PH01-v4.2)

```html
<!-- START: ID=PH01-v4.2 Preheader Text -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td style="padding: 8px 0;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="middle" width="310" class="full-width-block ph-text" style="padding-left: 10px;">
            <p style="font-size: 14px; line-height: 20px; color: #3D3D3D; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              PUBLICIDAD
            </p>
          </td>
          <td align="right" valign="middle" width="310" class="full-width-block ph-text" style="padding-right: 10px;">
            <p style="font-size: 14px; line-height: 20px; color: #3D3D3D; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              &iquest;No pod&eacute;s ver el mail?
              <a href="https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}"
                 style="color: #333333; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                <strong style="font-weight: normal; text-decoration: underline; color: #333333;">Hac&eacute; click aqu&iacute;</strong>
              </a>
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: PH01-v4.2 Preheader Text -->
```

---

## Componente: Separador

```html
<!-- START: SEPARATOR -->
<table class="Separator" role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: #FFFFFF">
  <tr>
    <td style="height: 30px;" height="30"></td>
  </tr>
</table>
<!-- END: SEPARATOR -->
```

---

## Componente: Botón Primario (Azul)

```html
<!-- START: PRIMARY BUTTON - BLUE -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="150" height="44"
       style="width:150px; height:44px; border-radius: 4px; background:#006FCF;" class="button-primary-light">
  <tr>
    <td align="center" valign="middle">
      <table role="none" cellpadding="0" cellspacing="0" border="0"
             style="border-radius: 4px; border: 2px solid #006FCF; mso-border-alt: 2px solid #006FCF; width:146px; height:42px">
        <tr>
          <td align="center" valign="middle" height="44">
            <a href="[URL]" target="_blank"
               style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color: #FFFFFF; display: inline-block; padding: 12px 0;
                      text-decoration: none; width: 146px; font-size: 15px; line-height: 22px;">
              <strong style="font-weight: normal; color: #FFFFFF;">Conoc&eacute; m&aacute;s</strong>
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: PRIMARY BUTTON - BLUE -->
```

---

## Reglas Generales

- Siempre usar `role="none"` en las tablas de layout
- Imágenes con `alt` descriptivo, `width` fijo y `height: auto`
- Nunca usar `height` fijo en imágenes (salvo card en brand panel: 50px)
- Links con `target="_blank"` y `text-decoration: none`
- Superíndices de legales: `<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>`
- Acentos en HTML entities: `&eacute;` `&aacute;` `&oacute;` `&uacute;` `&ntilde;` `&iquest;`
