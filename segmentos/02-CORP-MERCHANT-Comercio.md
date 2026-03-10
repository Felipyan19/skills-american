# Skill: Segmento CORP y MERCHANT Comercio

## Descripcion del segmento
Emails para audiencia corporativa y comercios (CORP / MERCHANT Comercio), sobre template `AMX_GBS Templates 4.2`.

Tipos frecuentes:
- IG / redes
- Travel corporativo
- Special Offers (catalogo de categorias/comercios)

## Referencias fuente
- `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-IG-Sep25/CORP-IG-Sep25.html`
- `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-Travel-Octubre25/CORP-Travel-Octubre25.html`
- `1. Referencias por segmento/CORP y MERCHANT Comercio/CORP-Special-Offers-Navidad-Dic25/CORP-Special-Offers-Navidad-Dic25.html`

---

## Reglas fijas (obligatorias)

| Item | Regla |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Tracking pixel | obligatorio: `<custom name="opencounter" type="tracking"/>` |
| Header | siempre `PH01-v4.2 + Consumer Default-v4.2 (CORP)` |
| Footer | siempre `FM05 -> FM02 -> FM03 -> FM04` |
| Tagline CORP | `No hagas negocios sin ella` |
| Personalizacion minima | `{(URLSignature1)}`, `{(EMAIL)}` |
| Legales | superindices en contenido y desarrollo completo en FM04 |

---

## Header fijo CORP/MERCHANT

```html
<!-- START: HEADER FIJO CORP/MERCHANT -->
<!-- START: PH01-v4.2 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td style="padding: 8px 0;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="middle" width="310" class="full-width-block ph-text" style="padding-left: 10px;">
            <p style="font-size: 14px; line-height: 20px; color: #3D3D3D; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">PUBLICIDAD</p>
          </td>
          <td align="right" valign="middle" width="310" class="full-width-block ph-text" style="padding-right: 10px;">
            <p style="font-size: 14px; line-height: 20px; color: #3D3D3D; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              &iquest;No pod&eacute;s ver el mail?
              <a href="https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}" style="color: #333333; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                <strong style="font-weight: normal; text-decoration: underline; color:#333333;">Hac&eacute; click aqu&iacute;</strong>
              </a>
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: PH01-v4.2 -->

<!-- START: Consumer Default-v4.2 (CORP sin saludo) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="border-bottom: solid 1px #E0E0E0; padding:20px;" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="top" width="137" style="width: 137px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <td width="60" style="width: 60px;" class="bp-logo">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_LOGO_AMEX]" alt="American Express" width="60" style="width:60px; height:auto; color:#3D3D3D;" class="bp-logo">
                  </a>
                </td>
                <td class="Slogn" width="150" style="padding-left: 10px;">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_TAGLINE_CORP]" alt="No hagas negocios sin ella" width="150" style="width:150px; height:auto; color:#3D3D3D;">
                  </a>
                </td>
              </tr>
            </table>
          </td>
          <td align="right" valign="top"><p class="bp-text" style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; color: #3D3D3D; font-size: 15px; line-height: 22px;">&nbsp;</p></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: Consumer Default-v4.2 -->
<!-- END: HEADER FIJO CORP/MERCHANT -->
```

---

## Footer fijo CORP/MERCHANT

```html
<!-- START: FOOTER FIJO CORP/MERCHANT -->
<!-- START: FM05 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FFFFFF">
  <tr>
    <td align="center" style="padding: 0px; border-bottom: 1px solid #DEDEDE;">
      <span class="mobile-off"><img src="[IMG_FM05_DESKTOP]" alt="No hagas negocios sin ella(TM)" width="100%" style="vertical-align: top; height: auto; color: #333333" /></span>
      <span class="mobile-on" style="display: none;"><img src="[IMG_FM05_MOBILE]" alt="No hagas negocios sin ella(TM)" width="100%" style="display:block; vertical-align: top; height: auto; color: #333333" /></span>
    </td>
  </tr>
</table>
<!-- END: FM05 -->

<!-- START: FM02 Social -->
<div style="background: #FFFFFF; margin: 0px auto; max-width: 620px; border:none;" align="center">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" align="center">
    <tbody><tr><td align="center" valign="top" style="padding: 20px 0px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tbody><tr>
        <th style="font-weight: normal; width: 28px;" align="left"><a href="https://www.instagram.com/americanexpressarg/" target="_blank"><img src="[IMG_SOCIAL_INSTAGRAM]" alt="Instagram" height="28" width="28" style="display:block;"></a></th>
        <th style="font-weight: normal; padding-left: 30px; width: 28px;" align="left"><a href="https://www.facebook.com/americanexpressargentina" target="_blank"><img src="[IMG_SOCIAL_FACEBOOK]" alt="Facebook" height="28" width="28" style="display:block;"></a></th>
        <th style="font-weight: normal; padding-left: 30px; width: 28px;" align="left"><a href="https://www.youtube.com/user/AmericanExpressArg" target="_blank"><img src="[IMG_SOCIAL_YOUTUBE]" alt="YouTube" height="28" width="28" style="display:block;"></a></th>
      </tr></tbody></table>
    </td></tr></tbody>
  </table>
</div>
<!-- END: FM02 Social -->

<!-- START: FM03 Nav -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td class="pd0" style="padding: 16px 0px 15px; border-top: 1px solid #DEDEDE;" align="center" valign="top">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr role="list">
          <th role="listitem" class="fm-nav-link full-width-block" style="padding: 0 10px;"><a href="https://www.americanexpress.com/argentina/legal/privacy_statement.shtml" class="link" target="_blank" style="color: #006fcf; font-size: 15px; line-height: 22px; text-decoration: none; display: block; padding: 12px 0; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">Privacidad</a></th>
          <th role="listitem" class="fm-nav-link full-width-block fm-border" style="padding: 0 10px;"><a href="https://www.americanexpress.com/ar/content/ayuda/contactenos.html" target="_blank" class="link" style="color: #006fcf; font-size: 15px; line-height: 22px; text-decoration: none; display: block; padding: 12px 0; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">Contacto</a></th>
          <th role="listitem" class="fm-nav-link full-width-block fm-border" style="padding: 0 10px;"><a href="https://www.americanexpress.com/es-ar/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Fmyca%2Fintl%2Facctmaintain%2Fcanlac%2FchangeDetails.do%3Frequest_type%3D%26Face%3Des_AR%26sorted_index%3D0" target="_blank" class="link" style="color: #006fcf; font-size: 15px; line-height: 22px; text-decoration: none; display: block; padding: 12px 0; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">Actualizar email</a></th>
          <th role="listitem" class="fm-nav-link full-width-block fm-border" style="padding: 0 10px;"><a href="https://global.americanexpress.com/privacy/argentina/#/ipp" target="_blank" class="link" style="color: #006fcf; font-size: 15px; line-height: 22px; text-decoration: none; display: block; padding: 12px 0; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">Desuscribirse</a></th>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: FM03 Nav -->

<!-- START: FM04 Legales -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#E0E0E0">
  <tr>
    <td align="justify" style="padding: 5px 10px 16px; color: #53565A; font-size: 13px; line-height: 18px; text-align: justify; text-transform: uppercase; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
      1) [LEGAL 1 CON URL].<br><br>
      2) [LEGAL 2 CON URL].<br><br>
      [AGREGAR TODOS LOS LEGALES SEGUN SUPERINDICES].<br><br>
      Los datos personales son almacenados en una base de datos, cuyo responsable es American Express Argentina S.A. con domicilio legal en Arenales 707, entrepiso, CP C1061AAA, C.A.B.A.<br><br>
      Instrucciones para cancelar la suscripcion: enviado a <strong style="color:#000000; font-weight:normal; word-wrap: break-word; word-break: break-all;">{(EMAIL)}</strong>. Para baja, responder con "borrar" o visitar <a href="https://global.americanexpress.com/privacy/argentina/#/ipp" target="_blank" style="color: #00175A; text-decoration: none;">preferencias de correo electronico</a>.<br><br>
      &copy; [ANIO] American Express Company.
    </td>
  </tr>
</table>
<!-- END: FM04 Legales -->
<!-- END: FOOTER FIJO CORP/MERCHANT -->
```

---

## Estructura base del email completo

```html
<div style="display:none;"><custom name="opencounter" type="tracking"/></div>
<div role="article" aria-roledescription="email" aria-label="Email from American Express" lang="en" dir="ltr" style="font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 22px;">
  <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#E0E0E0"><tr><td align="center">
    <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width:620px;" class="container"><tr><td><!-- HEADER FIJO --></td></tr></table>
    <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width:620px; background:#FFFFFF" class="container"><tr><td><!-- CONTENIDO DINAMICO --><!-- FOOTER FIJO --></td></tr></table>
  </td></tr></table>
</div>
```

---

## Ejemplo completo IG (contenido dinamico)

```html
<!-- HERO IG -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td align="center" bgcolor="#00175a" background="[IMG_HERO_IG]" width="620" height="620" valign="top" style="background: url('[IMG_HERO_IG]') center / cover no-repeat #ffffff;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="620" style="width:620px;" class="full-width">
        <tr>
          <td align="center" style="padding:40px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="540" style="width:540px;" class="full-width">
              <tr><td align="center" style="font-family:'BentonSans400', HelveticaNeue, Helvetica, Arial, sans-serif; font-size:51px; line-height:50px; color:#00175A;">SEGUINOS</td></tr>
              <tr><td align="center"><table cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#006FCD" style="font-family:'BentonSans500', HelveticaNeue, Helvetica, Arial, sans-serif; font-size:44px; line-height:47px; color:#FFFFFF; padding:7px 33px;"><strong>en Instagram.</strong></td></tr></table></td></tr>
              <tr><td align="center" style="font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:18px; line-height:23px; color:#00175A; padding-top:24px;">Entr&aacute; a nuestro Instagram y no te pierdas de nada.</td></tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<!-- BLOQUE SEGURIDAD -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#EBECED" style="background:#EBECED;">
  <tr>
    <td style="padding:30px 40px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr><td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:20px; line-height:23px;"><strong>Consejos de seguridad:</strong></td></tr>
        <tr><td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:16px; line-height:20px; padding-top:12px;">Nuestras cuentas oficiales tienen tilde azul y nunca pedimos informacion por redes.</td></tr>
        <tr><td align="center" style="padding-top:24px;"><a href="https://www.instagram.com/americanexpressarg/" target="_blank" style="font-family:HelveticaNeue, Helvetica, Arial, sans-serif; color:#00175A; text-decoration:none;"><strong>@AmericanExpressArg</strong></a></td></tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Ejemplo completo TRAVEL (contenido dinamico)

```html
<!-- HERO TRAVEL -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td align="center" bgcolor="#ffffff" background="[IMG_HERO_TRAVEL]" width="620" height="320" valign="top" style="background: url('[IMG_HERO_TRAVEL]') center / cover no-repeat #ffffff;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="left" style="padding:60px 40px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="230" bgcolor="#00175A">
              <tr><td style="padding:7px 20px; background:#006FCF; color:#FFFFFF; font-family:'BentonSans400', HelveticaNeue, Helvetica, Arial, sans-serif; font-size:22px; line-height:25px;">NOVIEMBRE</td></tr>
              <tr><td style="padding:14px 20px; color:#FFFFFF; font-family:'BentonSans400', HelveticaNeue, Helvetica, Arial, sans-serif; font-size:33px; line-height:36px;">Beneficios en viajes<br><strong>#conAmex.</strong></td></tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<!-- OFERTA TRAVEL -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td style="padding:48px 20px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr><td align="center" style="color:#006FCF; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:15px; line-height:19px;">Del 1 de noviembre al 20 de diciembre</td></tr>
        <tr><td align="center" style="padding-top:7px;"><img src="[IMG_BADGE_10OFF]" alt="10% OFF" width="154" style="display:block; height:auto;"></td></tr>
        <tr><td align="center" style="color:#006FCF; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:15px; line-height:18px; padding-top:4px;"><strong>Upgrade en Day Tour<span style="font-size:8px;line-height:8px;vertical-align:8px;font-weight:normal;">1</span></strong></td></tr>
        <tr><td align="center" style="padding-top:26px;"><a href="[URL_TRAVEL]" target="_blank" style="font-family:HelveticaNeue, Helvetica, Arial, sans-serif; color:#00175A; text-decoration:underline;"><strong>Conoc&eacute; m&aacute;s</strong></a></td></tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Ejemplo completo SPECIAL OFFERS (contenido dinamico)

```html
<!-- IM03 - PARES -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <th width="310" class="full-width-block" align="left" valign="top" style="background-color:#deedfa;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr><td align="center"><a href="[URL_CAT_1]" target="_blank"><img src="[IMG_CAT_1]" alt="Gaming y tecnologia" width="310" style="display:block; height:auto;" class="full-width"></a></td></tr>
        <tr><td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:18px; line-height:21px;"><strong>GAMING &amp; TECNOLOGIA</strong></td></tr>
        <tr><td align="center" style="padding:25px 0 40px;"><a href="[URL_CAT_1]" target="_blank" style="font-family:HelveticaNeue, Helvetica, Arial, sans-serif; color:#006FCF; text-decoration:none;"><strong>Compr&aacute; ahora</strong></a></td></tr>
      </table>
    </th>
    <th width="310" class="full-width-block" valign="top" style="background-color:#edf5fc;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr><td align="center"><a href="[URL_CAT_2]" target="_blank"><img src="[IMG_CAT_2]" alt="Pequenos electrodomesticos" width="310" style="display:block; height:auto;" class="full-width"></a></td></tr>
        <tr><td align="center" style="color:#00175A; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:18px; line-height:21px;"><strong>PEQUENOS ELECTRODOMESTICOS</strong></td></tr>
        <tr><td align="center" style="padding:25px 0 40px;"><a href="[URL_CAT_2]" target="_blank" style="font-family:HelveticaNeue, Helvetica, Arial, sans-serif; color:#006FCF; text-decoration:none;"><strong>Compr&aacute; ahora</strong></a></td></tr>
      </table>
    </th>
  </tr>
</table>

<!-- CTA FINAL -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td align="center" style="padding:38px 0;">
      <a href="[URL_TBBM]" target="_blank" style="display:inline-block; width:292px; background:#006FCF; color:#FFFFFF; font-family:HelveticaNeue, Helvetica, Arial, sans-serif; font-size:15px; line-height:22px; text-decoration:none; padding:8px 0;">
        Descubr&iacute; m&aacute;s en <strong style="color:#FFFFFF;">The Blue Box Market</strong>
      </a>
    </td>
  </tr>
</table>
```

---

## Checklist rapido

- Header fijo presente (`PH01 + Consumer Default CORP`).
- Footer fijo presente (`FM05 + FM02 + FM03 + FM04`) en ese orden.
- Tracking pixel presente.
- Superindices en contenido y legales completos en FM04.
- Todos los CTA con `target="_blank"`.
- Imagenes con `alt` y `height:auto`.
