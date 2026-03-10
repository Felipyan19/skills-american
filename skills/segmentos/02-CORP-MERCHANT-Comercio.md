# Skill: Segmento CORP y MERCHANT Comercio

## Descripción del Segmento
Emails para tarjetas **corporativas** (CORP) y **comercios/merchants** (MERCHANT Comercio). Foco en beneficios de negocio: viajes corporativos, ofertas especiales, Instagram/redes.

**Archivos de referencia:**
- `CORP-IG-Sep25.html` → Campaña Instagram / Redes sociales corporativo
- `CORP-Travel-Octubre25.html` → Beneficios de viaje corporativo
- `CORP-Special-Offers-Navidad-Dic25.html` → Ofertas especiales navidad

---

## Características Distintivas

| Atributo | Valor |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Brand Panel | `Consumer Default-v4.2` (simplificado, sin tarjeta) |
| Tagline logo | "No hagas negocios sin ella" |
| Saludo | Puede ser sin saludo personalizado (solo logo) |
| Color primario | `#00175A` (azul profundo) |
| Audiencia | Titulares corporativos / dueños de comercios |

---

## Brand Panel CORP — Sin Saludo (simplificado)

Para emails corporativos donde el titular no siempre es identificable individualmente.

```html
<!-- START: Consumer Default-v4.2 (CORP — sin greeting personalizado) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="border-bottom: solid 1px #d9d9d7; padding: 20px;" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="top" width="137" style="width: 137px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <!-- Logo Amex -->
                <td width="60" style="width: 60px;" class="bp-logo">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_LOGO_AMEX]" alt="American Express, opens a new tab" width="60"
                         style="width:60px; height:auto; color:#3D3D3D;" class="bp-logo">
                  </a>
                </td>
                <!-- Tagline "No hagas negocios sin ella" (desktop only) -->
                <td class="Slogn" width="150" style="padding-left: 10px">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_TAGLINE_CORP]" alt="No hagas negocios sin ella" width="150"
                         style="width:150px; height:auto; color:#3D3D3D;">
                  </a>
                </td>
              </tr>
            </table>
          </td>
          <!-- Espacio derecho (sin datos de cuenta en versión corporativa) -->
          <td align="right" valign="top">
            <p class="bp-text"
               style="font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color: #3D3D3D; font-size: 15px; line-height: 22px;">&nbsp;</p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: Consumer Default-v4.2 -->
```

---

## Hero Banner Full Width (HB15-v4.2)

Imagen full width sin overlay de texto (imagen ya contiene el copy).

```html
<!-- START: HB15-v4.2 Full Width Hero -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="[URL_CTA]" target="_blank" style="text-decoration: none; border: none; outline: 0;">
        <img src="[URL_IMG_HERO_FULL]" alt="[Descripción del beneficio]" width="620"
             style="height: auto; display: block; color: #3D3D3D;" class="full-width">
      </a>
    </td>
  </tr>
</table>
<!-- END: HB15-v4.2 Full Width Hero -->
```

---

## Módulo: Pares de Imágenes Verticales (IM03-v4.2)

Dos columnas de imagen + título + subtítulo + botón CTA. Ideal para mostrar dos ofertas distintas.

```html
<!-- START: ID=IM03-v4.2 Vertical Pairs -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <!-- COLUMNA IZQUIERDA -->
    <th width="305" class="full-width-block pdbtm40" align="left" valign="top">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td class="height-auto" height="207" align="center" valign="bottom" style="height:207px;">
            <a href="[URL_OFERTA_1]" target="_blank" style="text-decoration:none; border:none; outline:0;">
              <img src="[IMG_OFERTA_1]" alt="[Nombre oferta 1]" width="305"
                   style="height:auto; display:block; color:#3D3D3D;" class="full-width">
            </a>
          </td>
        </tr>
        <tr>
          <td valign="top">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:19px; line-height:21px; padding:15px 10px 0;">
                  <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                    Título oferta 1
                  </strong>
                </td>
              </tr>
              <tr>
                <td align="center"
                    style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:15px; line-height:22px; padding:8px 10px 0;">
                  Descripción breve del beneficio.
                </td>
              </tr>
              <tr>
                <td align="center" style="padding-top: 20px; padding-bottom: 20px;">
                  <!-- Botón CTA -->
                  <table role="none" cellpadding="0" cellspacing="0" border="0" width="126" height="44"
                         style="width:126px; height:44px; border-radius:3px; background:#006fcf;" class="button-primary-light">
                    <tr><td align="center" valign="middle">
                      <table role="none" cellpadding="0" cellspacing="0" border="0"
                             style="border-radius:3px; border:2px solid #006fcf; width:122px; height:42px">
                        <tr><td align="center" valign="middle" height="44">
                          <a href="[URL_OFERTA_1]" target="_blank"
                             style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                    color:#FFFFFF; display:inline-block; padding:12px 0;
                                    text-decoration:none; width:122px; font-size:15px; line-height:22px;">
                            <strong style="font-weight:normal; color:#FFFFFF;">Ver m&aacute;s</strong>
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

    <!-- COLUMNA DERECHA (misma estructura) -->
    <th width="305" class="full-width-block pdbtm40" align="left" valign="top">
      <!-- Repetir la misma estructura con oferta 2 -->
    </th>
  </tr>
</table>
<!-- END: IM03-v4.2 Vertical Pairs -->
```

---

## Módulo: Oferta Especial con Borde (TM04-v4.2)

Caja con borde, descuento grande (ej: "40% OFF"), subtítulo, logo de comercio y botón.

```html
<!-- START: ID=TM04-v4.2 Offer Code -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding: 0px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="90%">
        <tr>
          <td align="center"
              style="color:#000000; font-size:0px; padding:40px 20px; border:1px solid #737880;">
            <table width="100%" role="none" cellpadding="0" cellspacing="0" border="0">
              <!-- Período -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:20px; line-height:23px; padding:0;">
                  <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                    Del [FECHA INICIO] al [FECHA FIN]
                  </strong>
                </td>
              </tr>
              <!-- Descuento principal -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:69px; line-height:72px; padding:30px 0 0;">
                  <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                    [X]% OFF
                  </strong>
                </td>
              </tr>
              <!-- Beneficio adicional -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:25px; line-height:28px; padding:0;">
                  <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                    Beneficio adicional<span style="font-size:11px; line-height:8px; vertical-align:11px; font-weight:normal;">1</span>
                  </strong>
                </td>
              </tr>
              <!-- Descripción -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:20px; line-height:23px; padding:4px 0 0;">
                  para socios American Express.
                </td>
              </tr>
              <!-- Logo del comercio -->
              <tr>
                <td align="center" valign="top" style="padding:19px 0 0;">
                  <img src="[LOGO_COMERCIO]" alt="[Nombre Comercio]"
                       style="border:0 none; display:block; height:auto; width:149px;" width="149" height="auto">
                </td>
              </tr>
              <!-- Botón -->
              <tr>
                <td align="center" style="padding-top:31px;">
                  <table role="none" cellpadding="0" cellspacing="0" border="0" width="150" height="44"
                         style="width:150px; height:44px; border-radius:4px; background:#00175A;" class="button-primary-light">
                    <tr><td align="center" valign="middle">
                      <table role="none" cellpadding="0" cellspacing="0" border="0"
                             style="border-radius:4px; border:2px solid #00175A; width:146px; height:42px">
                        <tr><td align="center" valign="middle" height="44">
                          <a href="[URL_CTA]" target="_blank"
                             style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                    color:#FFFFFF; display:inline-block; padding:12px 0;
                                    text-decoration:none; width:146px; font-size:15px; line-height:22px;">
                            <strong style="font-weight:normal; color:#FFFFFF;">Conoc&eacute; m&aacute;s</strong>
                          </a>
                        </td></tr>
                      </table>
                    </td></tr>
                  </table>
                </td>
              </tr>
              <!-- Legales -->
              <tr>
                <td align="center"
                    style="padding:31px 0 0; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:12px; line-height:14px; color:#000000;">
                  <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                    [Texto de términos y condiciones resumido.]
                  </strong>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: TM04-v4.2 Offer Code -->
```

---

## Estructura Típica de Email CORP

```
1. Preheader (PH01-v4.2)
2. Brand Panel CORP (logo + tagline "No hagas negocios sin ella", sin greeting)
3. Hero Banner (full width o con overlay)
4. [Módulos según tipo de campaña:]
   - IG/Social: imagen full width + texto descriptivo
   - Travel: pares de destinos (IM03) + beneficios
   - Special Offers: caja de oferta (TM04) + logos de comercios
5. Separator
6. Footer con legales
```

---

## Notas

- Las campañas CORP generalmente no llevan saludo personalizado `{(FNAME)}` porque se envían a cuentas corporativas donde el titular puede ser una empresa
- El copy usa "No hagas negocios sin ella" (vs "No vivas la vida sin ella" en Consumer)
- Estilo visual más austero / ejecutivo que los segmentos consumer
- Las Special Offers navideñas incluyen múltiples marcas en una sola pieza (grid de logos)
