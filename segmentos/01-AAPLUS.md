# Skill: Segmento AAPLUS (Gold LOC / Platinum LOC)

## Descripción del Segmento
Emails para titulares de tarjetas de línea de crédito local (LOC) de American Express Argentina: **Gold LOC** y **Platinum LOC**. Usan el template **v4.0** (el más antiguo del conjunto).

**Archivos de referencia:**
- `PP-LOC-GOLD-Febrero25.html` → Tarjeta Gold LOC
- `PP-LOC-PLAT-Febrero25.html` → Tarjeta Platinum LOC

---

## Características Distintivas

| Atributo | Valor |
|---|---|
| Template | `AMX_GBS Templates 4.0` |
| Fondo body | `#D9D9D6` (gris cálido, diferente al estándar) |
| Brand Panel | `BP02-v4.0` con imagen de tarjeta |
| Tagline logo | "No vivas la vida sin ella" |
| Saludo | `Hola, {(FNAME)}` |
| Botón header | "Mi cuenta" (borde azul `#006FCF`) |
| Hero | `HB03-v4.0` con overlay de texto sobre imagen |

---

## Brand Panel (BP02-v4.0)

Incluye: logo Amex + tagline + datos de cuenta + imagen de tarjeta + botón "Mi cuenta".

```html
<!-- START: BP02-v4.0 -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="padding: 20px 20px 14px 20px" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <!-- Logo Amex -->
          <td width="60" style="width: 60px" class="bp-logo">
            <a href="http://www.americanexpress.com.ar" target="_blank">
              <img src="[IMG_LOGO_AMEX]" alt="American Express" width="60"
                   style="width: 60px; height: auto; color: #333333" class="bp-logo" />
            </a>
          </td>
          <!-- Tagline (oculta en mobile) -->
          <td width="145" style="padding-left: 10px" class="mobile-off">
            <a href="http://www.americanexpress.com.ar" target="_blank">
              <img src="[IMG_TAGLINE]" alt="No vivas la vida sin ella" width="145"
                   style="width: 145px; height: auto; color: #333333" />
            </a>
          </td>
          <!-- Datos cuenta -->
          <td align="right" valign="middle" style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif">
            <p class="bp-text" style="color: #333333; font-size: 15px; line-height: 22px; padding-left: 20px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif">
              Tu cuenta termina en: {(LAST_5)}<br />
              <span class="mobile-off" style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif">
                Miembro desde: {(MEMBER_SINCE)}
              </span>
            </p>
          </td>
          <!-- Imagen tarjeta -->
          <td align="right" valign="middle" width="80" style="padding-left: 12px" class="bp02-card">
            <img src="[IMG_CARD]" alt="The Gold Credit Card&reg;" width="80"
                 style="height: 50px; width: 80px; color: #333333" class="bp02-card" />
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- Fila saludo + botón Mi cuenta -->
  <tr>
    <td style="padding: 10px 20px; border-bottom: solid 1px #d9d9d6; border-top: solid 1px #d9d9d6" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td style="padding-right: 10px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif">
            <p style="color: #333333; font-size: 15px; line-height: 22px; font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif">
              Hola, {(FNAME)}
            </p>
          </td>
          <td class="ButtonRadius Cuenta" width="auto" align="right" valign="middle"
              style="margin:0; padding:0; font-size:0; line-height:0; background:#FFFFFF;" bgcolor="#FFFFFF">
            <div align="right">
              <!--[if mso]>
              <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"
                href="https://www.americanexpress.com/es-ar/account/login?email_consumer"
                style="v-text-anchor:middle;width:100px;height:38px;" arcsize="4%"
                strokecolor="#006fcf" fillcolor="#FFFFFF" strokeweight="1pt">
                <w:anchorlock/><center>
              <![endif]-->
              <a class="button-secondary-light"
                 href="https://www.americanexpress.com/es-ar/account/login?email_consumer"
                 target="_blank"
                 style="width:100px; height:38px; display:inline-block; background-color:#FFFFFF;
                        border-radius:4px; color:#006fcf; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                        font-size:15px; font-weight:normal; line-height:38px; text-align:center;
                        text-decoration:none; border:1px solid #006fcf;">
                <strong style="color:#006fcf; text-decoration:none; font-weight: normal;">Mi cuenta</strong>
              </a>
              <!--[if mso]></center></v:roundrect><![endif]-->
            </div>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: BP02-v4.0 -->
```

---

## Hero Banner con Overlay (HB03-v4.0)

Imagen de fondo de 620×320px con texto superpuesto. Compatible con Outlook mediante VML.

```html
<!-- START: ID=HB03-v4.0 Overlay -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td class="HB03-v40" align="center" bgcolor="#ffffff"
        background="[URL_IMG_HERO]"
        width="620" height="320" valign="top"
        style="background: url('[URL_IMG_HERO]') top center / cover no-repeat #ffffff;
               background-position: top center; background-size: contain; background-repeat: no-repeat">
      <!--[if gte mso 9]>
      <v:image xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0; display:inline-block; width:620px; height:320px;"
        src="[URL_IMG_HERO]" />
      <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0; display:inline-block; position:absolute; width:620px; height:320px;">
        <v:fill opacity="0%" color="#ffffff" />
        <v:textbox inset="0,0,0,0">
      <![endif]-->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <th class="mobile-off" width="43" style="width: 43px">&nbsp;</th>
          <th class="full-width-auto BgBlue" style="width: 410px; font-weight: normal" valign="top">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" class="height-auto">
              <tr>
                <td class="height-auto pd40" style="padding: 53px 0 0" align="center" valign="middle">
                  <!-- Título principal -->
                  <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
                    <tr>
                      <td class="FSize01 center-text" valign="top"
                          style="font-family: 'BentonSans', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                 font-size: 35px; line-height: 38px; color: #00175a; padding: 0px 0 14px">
                        <strong>Título principal del email.</strong>
                      </td>
                    </tr>
                    <!-- Subtítulo opcional -->
                    <tr>
                      <td class="center-text" valign="top"
                          style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                 font-size: 18px; line-height: 22px; color: #00175a; padding: 0 10px 20px">
                        Texto descriptivo del beneficio.
                      </td>
                    </tr>
                    <!-- Botón CTA -->
                    <tr>
                      <td align="center" style="padding-bottom: 30px;">
                        <table role="none" cellpadding="0" cellspacing="0" border="0" width="150" height="44"
                               style="width:150px; height:44px; border-radius:4px; background:#006fcf;" class="hero-button button-primary-light">
                          <tr><td align="center" valign="middle">
                            <table role="none" cellpadding="0" cellspacing="0" border="0"
                                   style="border-radius:4px; border:2px solid #006fcf; width:146px; height:42px">
                              <tr><td align="center" valign="middle" height="44">
                                <a href="[URL_CTA]" target="_blank"
                                   style="color:#FFFFFF; display:inline-block; padding:12px 0;
                                          text-decoration:none; width:146px; font-size:15px; line-height:22px;
                                          font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                                  <strong style="font-weight:normal; color:#FFFFFF;">Ver beneficios</strong>
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
          </th>
        </tr>
      </table>
      <!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
    </td>
  </tr>
</table>
<!-- END: HB03-v4.0 Overlay -->
```

---

## Estructura Típica de Email AAPLUS

```
1. Preheader (PH01-v4.0) — "PUBLICIDAD" | "¿No podés ver el mail?"
2. Brand Panel (BP02-v4.0) — Logo + tagline + datos cuenta + tarjeta + "Hola, {FNAME}"
3. Hero Banner (HB03-v4.0) — Imagen con texto overlay + CTA
4. [Módulos de contenido según oferta: image+text, text blocks, etc.]
5. Separator
6. Footer — Legales, redes sociales, datos de contacto
```

---

## Diferencias Gold LOC vs Platinum LOC

| | Gold LOC | Platinum LOC |
|---|---|---|
| `alt` tarjeta | `"The Gold Credit Card®"` | `"The Platinum Credit Card®"` |
| Color primario body | `#D9D9D6` | `#D9D9D6` |
| Imagen tarjeta | Card dorada | Card plateada |
| Tono copy | Lifestyle / Verano / Disfrute | Premium / Exclusivo |

---

## Notas

- El fondo del body en v4.0 es `#D9D9D6` (NO `#E0E0E0` como en v4.2)
- El `button-primary-light:hover` en v4.0 usa `#006fcf` (no `#00175A`)
- La clase `mobile-off` oculta la tagline en mobile para ahorrar espacio
- Siempre incluir la imagen de la tarjeta en el brand panel (80×50px)
