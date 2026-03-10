# Skill: Segmento ICS (International Card Services)

## Descripción del Segmento
Emails para titulares de tarjetas **internacionales** de American Express Argentina. Incluye beneficios premium como eventos exclusivos (F1, gastronomía fina), acceso a experiencias únicas.

**Archivos de referencia:**
- `PP-Diderot-Nov25-ICS.html` → Restaurante Diderot — evento gastronómico
- `PP-F1-Miami-Preventa-ICS-oct25.html` → Preventa F1 Miami — evento deportivo premium

---

## Características Distintivas

| Atributo | Valor |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Brand Panel | `Consumer Default-v4.2` (Amex logo + tagline + cuenta) |
| Color primario | `#00175A` (azul profundo, idéntico a PP) |
| Audiencia | Titulares de tarjetas internacionales Amex |
| Tipo de contenido | Eventos únicos, experiencias exclusivas, preventas |
| Personalización | `{(LAST_5)}`, `{(MEMBER_SINCE)}`, `{(FULLNAME)}` |

---

## Brand Panel ICS (Consumer Default-v4.2)

Similar al de PP Platinum pero sin imagen de tarjeta. Muestra logo Amex + tagline.

```html
<!-- START: Consumer Default-v4.2 (ICS) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="border-bottom: solid 1px #E0E0E0; padding: 20px;" class="pd10">
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
                <!-- Tagline (desktop only) -->
                <td width="150" style="padding-left: 10px" class="mobile-off">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_TAGLINE]" alt="No vivas la vida sin ella" width="150"
                         style="width:150px; height:auto; color:#3D3D3D;">
                  </a>
                </td>
              </tr>
            </table>
          </td>
          <!-- Datos cuenta -->
          <td align="right" valign="top">
            <p class="bp-text"
               style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color:#3D3D3D; font-size:15px; line-height:22px;">
              Tu cuenta termina en: <br class="mobile-on" style="display:none;" />
              {(LAST_5)} <br>
              <span class="mobile-off"
                    style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                Miembro desde: {(MEMBER_SINCE)}
              </span>
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- Fila saludo + Mi cuenta -->
  <tr>
    <td style="padding:10px 20px 11px 20px; border-bottom:solid 1px #E0E0E0; border-top:solid 1px #E0E0E0" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td style="padding-right: 20px;">
            <p style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color:#3D3D3D; font-size:15px; line-height:22px;" class="bp-text">
              Hola {(FULLNAME)}
            </p>
          </td>
          <td align="right">
            <a href="https://www.americanexpress.com/es-ar/account/login?email_consumer"
               class="button-secondary-light bp-login-button" target="_blank"
               aria-label="American Express account, opens a new tab"
               style="border:2px solid #006FCF; mso-border-alt:2px solid #006FCF; border-radius:3px;
                      color:#006FCF; display:inline-block; font-size:15px; line-height:100%;
                      padding:13px 12px; text-decoration:none; text-align:center;
                      font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      white-space:nowrap;">
              Mi cuenta
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: Consumer Default-v4.2 -->
```

---

## Módulo: Imagen + Texto Lateral (IM04-v4.2 Small Image)

Imagen a la izquierda + bloque de texto con bullets de beneficios a la derecha. Ideal para eventos con detalles (horarios, instrucciones, beneficios).

```html
<!-- START: ID=IM04-v4.2 Small Image -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td class="pd40-">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <!-- Imagen izquierda -->
          <th class="full-width-block pdbtm40" width="207" style="width:207px;" align="center">
            <img src="[IMG_EVENTO]" alt="[Nombre del evento]" width="207"
                 style="height:auto; display:block; color:#3D3D3D;" class="full-width-block center-align">
          </th>
          <!-- Bloque de texto derecha con fondo de color -->
          <th class="full-width-block pd0 height-auto"
              style="height:244px; padding:0 25px; background:#e7e6e9;" valign="middle" bgcolor="#e7e6e9">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <!-- Beneficio 1 con ícono -->
              <tr>
                <td class="pdtop40 pd-X-40" style="padding: 0;">
                  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
                    <tr>
                      <td style="padding:0 3px 0 0;">
                        <img src="[ICONO_BENEFICIO]" alt="*" width="20"
                             style="border:0; display:block; height:auto; width:20px;">
                      </td>
                      <td style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                 font-size:15px; line-height:20px; border:none; padding:0;">
                        <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                          Nombre del beneficio<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>.
                        </strong>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <!-- Descripción del beneficio -->
              <tr>
                <td class="pd-X-40" align="left"
                    style="color:#333333; padding:2px 0 0; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:15px; line-height:20px; border:none;">
                  Descripción detallada del beneficio.
                </td>
              </tr>
              <!-- Cómo acceder (con ícono app) -->
              <tr>
                <td class="pd-X-40" style="padding:20px 0 0;">
                  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
                    <tr>
                      <td style="padding:0 18px 0 0;">
                        <a href="[URL_APP]" target="_blank" style="text-decoration:none; border:none; outline:0;">
                          <img src="[ICONO_APP]" alt="*" width="48"
                               style="border:0; display:block; height:auto; width:48px;">
                        </a>
                      </td>
                      <td align="left"
                          style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                                 font-size:15px; line-height:20px; border:none; padding:0;">
                        Reserv&aacute; a trav&eacute;s de <br>
                        <a href="[URL_APP]" target="_blank"
                           style="color:#00175A; text-decoration:underline; font-weight:normal;
                                  font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
                          <strong style="font-weight:normal;">Amex Experiences App</strong>
                        </a>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <!-- Legales pequeños -->
              <tr>
                <td class="pd-X-40 padding-btm-40" align="left"
                    style="color:#333333; padding:25px 0 0; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:10px; line-height:12px; border:none;">
                  [Texto de condiciones del evento o beneficio.]
                </td>
              </tr>
            </table>
          </th>
        </tr>
      </table>
    </td>
  </tr>
</table>
<!-- END: IM04-v4.2 Small Image -->
```

---

## Estructura Típica de Email ICS

```
1. Preheader (PH01-v4.2)
2. Brand Panel ICS (Consumer Default-v4.2 con logo + cuenta + "Hola {FULLNAME}")
3. Hero Banner — Imagen del evento (full width o con overlay)
4. Módulo de detalles (IM04-v4.2) — Imagen + beneficios del evento con íconos
5. Separator
6. Información adicional (fechas, cómo reservar, requisitos)
7. CTA principal
8. Footer con legales numerados
```

---

## Ejemplos de Contenido ICS

### Evento gastronómico (Diderot)
- Hero: foto del restaurante
- Beneficios: mesa prioritaria, menú especial, descuento
- CTA: "Reservá tu mesa"
- App link: Amex Experiences App

### Preventa F1 Miami
- Hero: imagen del circuito / Grand Prix
- Beneficios: acceso preventa exclusivo, descuento en tickets, hospitality
- CTA: "Comprá tus tickets"
- Copy: enfocado en exclusividad y escasez ("Cupos limitados")

---

## Notas

- El color de fondo del bloque de texto en IM04 varía por email (`#e7e6e9`, `#f0f0f0`, etc.)
- Los íconos de beneficios son imágenes pequeñas (20×20px aproximado), no emoji
- Siempre incluir superíndices de legales en los beneficios: `<span style="font-size:11px; ...">1</span>`
- Los legales se listan al final del email como párrafos numerados con `font-size: 12px`
- El CTA puede ser un link a la app Amex Experiences o a la web de americanexpress.com.ar
