# Skill: Segmento MERCHANT - Socio

## Descripcion del segmento
Emails para socios/beneficiarios de comercios adheridos a American Express.
Este segmento usa template v4.2 y se divide en 3 tipos principales:

- Newsletter (multiples promos apiladas)
- Shot (una promo principal)
- Special Offers (catalogo o grilla de comercios)

## Referencias fuente (usar como patron real)
- `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Newsletter-Dic25/MERCHANT-Newsletter-Dic25.html`
- `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-Travel-Agst25/MERCHANT-Shot-Travel-Agst25.html`
- `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-deporte-DIC25/MERCHANT-Shot-deporte-DIC25.html`
- `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-SHOT-Navidad-Dic25/MERCHANT-SHOT-Navidad-Dic25.html`
- `1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Special-Offers-Dic25/MERCHANT-Special-Offers-Dic25.html`

---

## Reglas obligatorias (siempre mantener)

| Item | Regla |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Tracking pixel | obligatorio: `<custom name="opencounter" type="tracking"/>` |
| Header | siempre: `PH01-v4.2 + Consumer Default-v4.2` |
| Footer | siempre: `FM05 + FM02 + FM03 + FM04` (orden fijo) |
| Personalizacion | `{(FULLNAME)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}`, `{(URLSignature1)}`, `{(EMAIL)}` |
| CTA principal | azul `#006FCF` |
| Legales | siempre numerados con superindice y texto legal completo al final |

---

## Estructura fija del email completo (base MERCHANT)

```html
<!-- START: ESTRUCTURA BASE COMPLETA MERCHANT -->
<div style="display:none;">
  <custom name="opencounter" type="tracking"/>
</div>

<div role="article" aria-roledescription="email" aria-label="Email from American Express" lang="en" dir="ltr" style="font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-weight: normal; font-size: 15px; line-height: 22px;">
  <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#E0E0E0">
    <tr>
      <td align="center">
        <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
          <tr>
            <td align="center" background="images/wsp-grey.png" bgcolor="#E0E0E0">
              <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width: 620px;" class="container">
                <tr>
                  <td>
                    <!-- PEGAR AQUI EL HEADER FIJO -->
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>

        <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width:620px; background:#FFFFFF" class="container">
          <tr>
            <td>
              <!-- PEGAR AQUI EL CONTENIDO DINAMICO -->
              <!-- PEGAR AQUI EL FOOTER FIJO -->
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</div>
<!-- END: ESTRUCTURA BASE COMPLETA MERCHANT -->
```

---

## Ejemplo completo SHOT (contenido dinamico)

```html
<!-- START: SHOT CONTENT -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-viajes/" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[SHOT_HERO_DESKTOP].jpg" alt="Especial viajes para Socios American Express" width="620" style="height:auto; display:block; color:#3D3D3D; width:100%;" class="full-width">
      </a>
    </td>
  </tr>
</table>

<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding: 40px 40px 20px;" class="pd20">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:26px; line-height:30px; padding-bottom:15px;">
            <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              Hasta 6 cuotas sin interes en viajes<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>
            </strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:15px; line-height:22px; padding-bottom:30px;">
            Aprovecha beneficios exclusivos para tus proximas reservas en agencias y aerolineas seleccionadas.
          </td>
        </tr>
        <tr>
          <td align="center">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="190" height="44" style="width:190px; height:44px; border-radius:4px; background:#006FCF;" class="button-primary-light">
              <tr>
                <td align="center" valign="middle">
                  <table role="none" cellpadding="0" cellspacing="0" border="0" style="border-radius:4px; border:2px solid #006FCF; width:186px; height:42px;">
                    <tr>
                      <td align="center" valign="middle" height="44">
                        <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-viajes/" target="_blank" style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color:#FFFFFF; display:inline-block; padding:12px 0; text-decoration:none; width:186px; font-size:15px; line-height:22px;">
                          <strong style="font-weight:normal; color:#FFFFFF;">Conoc&eacute; el beneficio</strong>
                        </a>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: SHOT CONTENT -->
```

---

## Ejemplo completo NEWSLETTER (contenido dinamico)

```html
<!-- START: NEWSLETTER CONTENT -->

<!-- HERO PRINCIPAL -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[NEWSLETTER_HERO].jpg" alt="Beneficios para disfrutar este mes" width="620" style="height:auto; display:block; color:#3D3D3D; width:100%;" class="full-width">
      </a>
    </td>
  </tr>
</table>

<!-- PROMO BLOCK 1 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="padding: 30px 40px;" class="pd20">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="padding-bottom: 20px;">
            <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/shopping-days/" target="_blank" style="text-decoration:none; border:none; outline:0;">
              <img src="https://i.email.americanexpress.com/wpm/1288/Images/[PROMO1_IMAGE].jpg" alt="Shopping Days" width="540" style="height:auto; display:block; color:#3D3D3D;" class="full-width">
            </a>
          </td>
        </tr>
        <tr>
          <td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:22px; line-height:26px; padding-bottom:10px;">
            <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              Hasta 25% OFF en comercios adheridos<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>
            </strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:15px; line-height:22px; padding-bottom:20px;">
            Pagando con tus Tarjetas American Express en locales participantes.
          </td>
        </tr>
        <tr>
          <td align="center">
            <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/shopping-days/" target="_blank" style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color:#006FCF; font-size:15px; line-height:22px; text-decoration:underline; border:none; outline:0;">
              Ver m&aacute;s
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<!-- SEPARATOR -->
<table class="Separator" role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FFFFFF">
  <tr>
    <td style="height: 30px;" height="30"></td>
  </tr>
</table>

<!-- PROMO BLOCK 2 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="padding: 30px 40px;" class="pd20">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="padding-bottom: 20px;">
            <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-gastronomia/" target="_blank" style="text-decoration:none; border:none; outline:0;">
              <img src="https://i.email.americanexpress.com/wpm/1288/Images/[PROMO2_IMAGE].jpg" alt="Especial gastronomia" width="540" style="height:auto; display:block; color:#3D3D3D;" class="full-width">
            </a>
          </td>
        </tr>
        <tr>
          <td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:22px; line-height:26px; padding-bottom:10px;">
            <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              Beneficios en restaurantes seleccionados<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">2</span>
            </strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:15px; line-height:22px; padding-bottom:20px;">
            Descubri propuestas gastron&oacute;micas para compartir y ahorrar.
          </td>
        </tr>
        <tr>
          <td align="center">
            <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-gastronomia/" target="_blank" style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color:#006FCF; font-size:15px; line-height:22px; text-decoration:underline; border:none; outline:0;">
              Ver m&aacute;s
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<!-- END: NEWSLETTER CONTENT -->
```

---

## Ejemplo completo SPECIAL OFFERS (contenido dinamico)

```html
<!-- START: SPECIAL OFFERS CONTENT -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[SPECIAL_HERO].jpg" alt="Special Offers para Socios American Express" width="620" style="height:auto; display:block; color:#3D3D3D; width:100%;" class="full-width">
      </a>
    </td>
  </tr>
</table>

<!-- FILA 1 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;" class="half-width-block BrdrMobile">
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/moda/comercio-1" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[GRID_1].jpg" alt="Comercio 1" width="250" style="height:auto; display:block;" class="full-width">
      </a>
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:16px; line-height:20px; padding-top:10px; text-align:center;">
        <strong>20% OFF</strong><span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>
      </p>
    </td>
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;" class="half-width-block">
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/moda/comercio-2" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[GRID_2].jpg" alt="Comercio 2" width="250" style="height:auto; display:block;" class="full-width">
      </a>
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:16px; line-height:20px; padding-top:10px; text-align:center;">
        <strong>15% OFF</strong><span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">2</span>
      </p>
    </td>
  </tr>
</table>

<!-- FILA 2 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;" class="half-width-block BrdrMobile">
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/gastronomia/comercio-3" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[GRID_3].jpg" alt="Comercio 3" width="250" style="height:auto; display:block;" class="full-width">
      </a>
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:16px; line-height:20px; padding-top:10px; text-align:center;">
        <strong>10% OFF</strong><span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">3</span>
      </p>
    </td>
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;" class="half-width-block">
      <a href="https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/comercio-4" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="https://i.email.americanexpress.com/wpm/1288/Images/[GRID_4].jpg" alt="Comercio 4" width="250" style="height:auto; display:block;" class="full-width">
      </a>
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size:16px; line-height:20px; padding-top:10px; text-align:center;">
        <strong>25% OFF</strong><span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">4</span>
      </p>
    </td>
  </tr>
</table>
<!-- END: SPECIAL OFFERS CONTENT -->
```

---

## Modulos dinamicos reutilizables

Estos bloques se insertan dentro del contenido dinamico. Se pueden combinar libremente segun el tipo de email (Shot, Newsletter, Special Offers).

---

### TM01 - Encabezado de seccion con icono

Barra azul `#006FCF` con icono + titulo. Separa secciones dentro de un Newsletter (ej: COMPRAS, VIAJES, GASTRONOMIA).

```html
<!-- START: TM01-v4.2 Section Header -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#006FCF">
  <tr>
    <td bgcolor="#006FCF" width="620" align="center" valign="middle" style="width: 620px; padding: 25px 0px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="auto">
        <tr>
          <td valign="middle" style="padding: 0 5px 0 0;">
            <img src="[IMG_ICONO_SECCION]" alt="[NOMBRE SECCION]" width="51" height="auto" style="color: #000000; display: block;">
          </td>
          <td valign="middle" style="padding: 0px;">
            <h2 style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color: #ffffff; font-size: 20px; line-height: 23px;">
              <strong style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">[NOMBRE SECCION]</strong>
            </h2>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: TM01-v4.2 Section Header -->
```

---

### HB08 - Layout de dos columnas 50-50

Dos columnas de 309-310px con contenido independiente. Cada columna puede tener imagen de oferta, badge, texto, superindice legal y link. Separadas por borde `#C8C9C7`. Usar con `dir="ltr"` para compatibilidad RTL.

```html
<!-- START: ID=HB08-v4.2 50-50 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" dir="ltr" style="direction: ltr; width: 100%;">
  <tr>
    <!-- Columna izquierda -->
    <th class="full-width-auto pd40 BrdrMobile" width="309" style="direction: ltr; padding: 0 15px; width: 309px; font-weight: normal; border-right: 1px solid #C8C9C7;" align="center" valign="top">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; padding: 0px 0px 5px 15px; color: #00175A; font-size: 23px; line-height: 26px; font-weight: bold;">
            [Titulo promo columna izquierda]
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 16px; line-height: 21px;">
            [Subtitulo o fecha]
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px;">
            <img src="[IMG_BADGE_DESCUENTO]" alt="[20% OFF]" width="169" style="width: 169px; height: auto; color: #333333; display: block;">
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 20px;">
            [Descripcion breve del descuento]
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px;">
            <img src="[IMG_PLUS_SIGN]" alt="+" width="25" style="width: 25px; height: auto; color: #333333; display: block;">
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px;">
            <img src="[IMG_CUOTAS]" alt="[3 y 6 cuotas sin interes]" width="259" style="width: 259px; height: auto; color: #333333; display: block;">
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 20px;">
            en marcas participantes<span style="font-size: 8px; line-height: 8px; vertical-align: 7px;">1</span>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 25px 0px 20px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 18px; color: #00175a;">
            <a href="[URL_PROMO_IZQUIERDA]" target="_blank" style="text-decoration: underline; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              <strong>Compr&aacute; ahora</strong>
            </a>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 10px; line-height: 12px; color: #333333; padding-bottom: 40px;">
            [RESTRICCION LEGAL BREVE EN MAYUSCULAS]
          </td>
        </tr>
      </table>
    </th>
    <!-- Columna derecha -->
    <th class="full-width-block pdtop50 BrdrMobile" width="310" style="direction: ltr; width: 310px;" align="center" valign="top">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="padding: 0px;">
            <img src="[IMG_LOGO_COMERCIO]" alt="[NOMBRE COMERCIO]" width="154" style="width: 154px; height: auto; color: #333333; display: block;">
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 20px 0px 0px; color: #006fcf; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 18px;">
            <strong>[Nombre comercio o beneficio]</strong>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 0px;">
            <img src="[IMG_BADGE_DERECHA]" alt="[BENEFICIO]" width="214" style="width: 214px; height: auto; color: #333333; display: block;">
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 2px 0 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 20px;">
            [Descripcion del beneficio]<span style="font-size: 8px; line-height: 8px; vertical-align: 7px;">2</span>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 3px 0px 0px; color: #006fcf; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 18px;">
            [Condicion o vigencia]
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 35px 0px 0px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 18px; color: #00175a; padding-bottom: 40px;">
            <a href="[URL_PROMO_DERECHA]" target="_blank" style="text-decoration: underline; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              <strong>Suscribite ahora</strong>
            </a>
          </td>
        </tr>
      </table>
    </th>
  </tr>
</table>
<!-- END: HB08-v4.2 50-50 -->
```

---

### TM04 - Beneficios apilados con badges + logos + CTA (SHOT)

Patron tipico de Shot con descuento en imagen, signo +, cuotas en imagen, texto y logos de comercios en fila. Incluye nota legal mini y borde inferior `#006FCF`. Usado en shots de deporte, gastronomia, etc.

```html
<!-- START: ID=TM04-v4.2 Offer Code -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td style="padding: 0px 40px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="padding: 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 18px; line-height: 21px;">
            [Vigencia: "Del X al Y de mes"]
          </td>
        </tr>
        <!-- Fila de badges: OFF% + signo + + cuotas -->
        <tr>
          <td align="center" style="padding: 12px 0 0px;">
            <table width="auto" role="none" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="padding: 0px;" align="center" valign="top">
                  <img src="[IMG_DESCUENTO]" alt="[10% OFF sin tope y en el acto]" width="153" height="auto" style="display: block; width: 153px; max-width: 153px;">
                </td>
                <td style="padding: 0px 13px 0px;" align="center" valign="top">
                  <img src="[IMG_PLUS]" alt="+" width="25" height="auto" style="display: block; width: 25px; max-width: 25px;">
                </td>
                <td style="padding: 0px;" align="center" valign="top">
                  <img src="[IMG_CUOTAS]" alt="[3, 6, 9 Y 12 CUOTAS SIN INTERES]" width="244" height="auto" style="display: block; width: 244px; max-width: 244px;">
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 10px 0 0px; color: #00175a; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 18px; line-height: 21px;">
            [Condicion: "en nuevos planes o renovaciones"]
          </td>
        </tr>
        <!-- Fila de logos de comercios -->
        <tr>
          <td align="center" style="padding: 20px 0 0px;">
            <table width="auto" role="none" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="padding: 0px;" align="center" valign="middle">
                  <img src="[IMG_LOGO_COMERCIO_1]" alt="[NOMBRE COMERCIO 1]" width="222" height="auto" style="display: block; width: 222px; max-width: 222px;">
                </td>
                <td style="padding: 0px 0px 0px 30px;" align="center" valign="middle">
                  <img src="[IMG_LOGO_COMERCIO_2]" alt="[NOMBRE COMERCIO 2]" width="117" height="auto" style="display: block; width: 117px; max-width: 117px;">
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <!-- CTA solido azul -->
        <tr>
          <td align="center" style="padding-top: 23px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="126" height="44" style="width:126px; height:44px; border-radius: 3px; background:#006FCF;" class="button-primary-light">
              <tr>
                <td align="center" valign="middle">
                  <table role="none" cellpadding="0" cellspacing="0" border="0" style="border-radius: 3px; border: 2px solid #006FCF; mso-border-alt: 2px solid #006FCF; width:122px; height:42px;">
                    <tr>
                      <td align="center" valign="middle" height="44">
                        <a href="[URL_PROMO]" target="_blank" style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color: #FFFFFF; display: inline-block; padding: 12px 0; text-decoration: none; width: 122px; font-size: 15px; line-height: 22px;">
                          <strong style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color: #FFFFFF; font-weight: normal;">M&aacute;s info</strong>
                        </a>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <!-- Nota legal mini + borde inferior -->
        <tr>
          <td align="center" style="padding: 30px 0px 40px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; font-size: 10px; line-height: 12px; color: #000000; text-transform: uppercase; border-bottom: 1px solid #006FCF;">
            [RESTRICCION LEGAL BREVE]
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: TM04-v4.2 Offer Code -->
```

---

### SEPARATOR - Separador vertical entre bloques

```html
<!-- START: SEPARATOR -->
<table class="mobile-off" role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FFFFFF;" align="center">
  <tr>
    <td style="height: 35px;" height="35"></td>
  </tr>
</table>
<!-- END: SEPARATOR -->
```

---

## Checklist de validacion rapida para MERCHANT

- Header fijo presente y sin cambios en links de preheader/login.
- Footer fijo presente en orden `FM05 -> FM02 -> FM03 -> FM04`.
- Tracking pixel presente.
- Todos los descuentos con superindice legal correcto.
- Cantidad de legales en FM04 coincide con la cantidad de superindices del contenido.
- CTA y links de nav con `target="_blank"`.
- Imagenes con `alt` descriptivo y `height:auto`.
