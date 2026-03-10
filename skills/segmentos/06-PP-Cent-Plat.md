# Skill: Segmento PP (Centurion y Platinum)

## Descripción del Segmento
Emails para titulares de las tarjetas **premium** de American Express Argentina: **The Centurion Card** y **The Platinum Card**. El segmento se caracteriza por un tono exclusivo, beneficios de alta gama (dining, spend, teatro, lifestyle) y uso predominante del azul profundo `#00175A`.

**Archivos de referencia:**
- `MR-Bonus-Smiles-Dic25-CENT.html` / `...-PLAT.html` → Bonus puntos Smiles
- `PLAT-Spend-Farmacity-Oct25.html` → Spend & earn (Farmacity)
- `PP-Cata-Piedra-Pasillo-OCT25.html` → Evento gastronómico (Cata de vinos)
- `PP-Dining-Ultramarino-Nov25-CENT.html` / `...-PLAT.html` → Dining exclusivo
- `PP-Min-Agostini-Oct25-CENT.html` → Beneficio en comercio premium
- `PP-Spend-TBBM-Iphone17_CENT_dic25.html` / `...-PLAT.html` → Spend & get iPhone
- `PP-Teatro-Colon-2026-Dic25-CENT.html` / `...-PLAT.html` → Teatro Colón temporada
- `PP-F1-Miami-Preventa-ICS-oct25.html` → Preventa F1 Miami

---

## Características Distintivas

| Atributo | Valor CENT | Valor PLAT |
|---|---|---|
| Template | `AMX_GBS Templates 4.2` | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` | `#E0E0E0` |
| Color primario | `#00175A` | `#00175A` |
| Botón CTA | Fondo `#00175A` | Fondo `#00175A` |
| Imagen tarjeta | Centurion Card (negra) | Platinum Card (plateada) |
| Alt tarjeta | `"The Centurion Card®"` | `"The Platinum Card®"` |
| Tono copy | Ultra exclusivo, "solo para Centurion" | Premium, experiencias únicas |
| Personalización | `{(FULLNAME)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}` | igual |

---

## Brand Panel PP Premium (con imagen de tarjeta)

Incluye logo Amex + tagline + datos de cuenta + **imagen de tarjeta** (distingue CENT de PLAT).

```html
<!-- START: Consumer Default-v4.2 (PP Premium con tarjeta) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="border-bottom:solid 1px #E0E0E0; padding:20px;" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="top" width="137" style="width:137px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <!-- Logo Amex -->
                <td width="60" style="width:60px;" class="bp-logo">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_LOGO_AMEX]" alt="American Express, opens a new tab" width="60"
                         style="width:60px; height:auto; color:#3D3D3D;" class="bp-logo">
                  </a>
                </td>
                <!-- Tagline (desktop only) -->
                <td width="150" style="padding-left:10px" class="mobile-off">
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
              <span class="mobile-off">Miembro desde: {(MEMBER_SINCE)}</span>
            </p>
          </td>
          <!-- Imagen tarjeta (80×50px fija) -->
          <td align="right" valign="top" width="80" style="padding-left:12px;" class="bp02-card">
            <img src="[IMG_CARD_CENT_o_PLAT]" alt="The Platinum Card&reg;" width="80"
                 style="height:50px; width:80px; color:#3D3D3D;" class="bp02-card">
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- Saludo + Mi cuenta -->
  <tr>
    <td style="padding:10px 20px 11px; border-bottom:solid 1px #E0E0E0; border-top:solid 1px #E0E0E0" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td style="padding-right:20px;">
            <p style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color:#3D3D3D; font-size:15px; line-height:22px;" class="bp-text">
              Hola {(FULLNAME)}
            </p>
          </td>
          <td align="right">
            <a href="https://www.americanexpress.com/es-ar/account/login?email_consumer"
               class="button-secondary-light bp-login-button" target="_blank"
               style="border:2px solid #006FCF; border-radius:3px; color:#006FCF;
                      display:inline-block; font-size:15px; line-height:100%;
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

## Hero Banner con Fondo Azul (Overlay en #00175A)

Para emails PP, el hero muchas veces tiene fondo azul profundo con texto blanco.

```html
<!-- START: Hero Banner - Fondo Azul PP -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td bgcolor="#00175A" style="background:#00175A; padding:50px 40px;" align="center">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <!-- Eyebrow / categoría -->
        <tr>
          <td align="center"
              style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:14px; line-height:20px; letter-spacing:2px; padding-bottom:10px;">
            EXCLUSIVO PARA SOCIOS PLATINUM
          </td>
        </tr>
        <!-- Título principal -->
        <tr>
          <td align="center"
              style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                     font-size:36px; line-height:42px; padding-bottom:16px;">
            Título del beneficio premium
          </td>
        </tr>
        <!-- Subtítulo -->
        <tr>
          <td align="center"
              style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:16px; line-height:24px; padding-bottom:30px;">
            Descripci&oacute;n del beneficio.
          </td>
        </tr>
        <!-- CTA en blanco sobre azul -->
        <tr>
          <td align="center">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="180" height="44"
                   style="width:180px; height:44px; border-radius:4px; background:#FFFFFF;" class="button-primary-dark">
              <tr><td align="center" valign="middle">
                <table role="none" cellpadding="0" cellspacing="0" border="0"
                       style="border-radius:4px; border:2px solid #FFFFFF; width:176px; height:42px">
                  <tr><td align="center" valign="middle" height="44">
                    <a href="[URL_CTA]" target="_blank"
                       style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                              color:#00175A; display:inline-block; padding:12px 0;
                              text-decoration:none; width:176px; font-size:15px; line-height:22px;">
                      <strong style="font-weight:normal; color:#00175A;">Conoc&eacute; m&aacute;s</strong>
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

---

## Módulo: Spend & Earn

Para campañas donde el titular gana puntos/millas al gastar cierto monto.

```html
<!-- Módulo Spend & Earn -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding:40px 40px 20px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <!-- Condición -->
        <tr>
          <td align="center"
              style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:16px; line-height:22px; padding-bottom:8px;">
            Gast&aacute; $[MONTO] en [Comercio]
          </td>
        </tr>
        <!-- Separador "y ganá" -->
        <tr>
          <td align="center"
              style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:14px; line-height:20px; padding-bottom:8px;">
            y ganá
          </td>
        </tr>
        <!-- Premio destacado -->
        <tr>
          <td align="center"
              style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:36px; line-height:42px; font-weight:bold; padding-bottom:16px;">
            <strong>[Premio: iPhone 17 / Puntos / Millas]</strong>
          </td>
        </tr>
        <!-- Imagen del premio -->
        <tr>
          <td align="center" style="padding-bottom:30px;">
            <img src="[IMG_PREMIO]" alt="[Descripción del premio]" width="300"
                 style="height:auto; display:block; color:#3D3D3D;" class="RespImg">
          </td>
        </tr>
        <!-- CTA -->
        <tr>
          <td align="center">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="180" height="44"
                   style="width:180px; height:44px; border-radius:4px; background:#00175A;" class="button-primary-light">
              <tr><td align="center" valign="middle">
                <table role="none" cellpadding="0" cellspacing="0" border="0"
                       style="border-radius:4px; border:2px solid #00175A; width:176px; height:42px">
                  <tr><td align="center" valign="middle" height="44">
                    <a href="[URL_CTA]" target="_blank"
                       style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                              color:#FFFFFF; display:inline-block; padding:12px 0;
                              text-decoration:none; width:176px; font-size:15px; line-height:22px;">
                      <strong style="font-weight:normal; color:#FFFFFF;">Conocer m&aacute;s</strong>
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

---

## Estructura Típica de Email PP

```
1. Preheader (PH01-v4.2)
2. Brand Panel PP (Consumer Default-v4.2 con imagen de tarjeta CENT o PLAT)
3. Hero Banner (azul #00175A o imagen de calidad premium)
4. [Según tipo de campaña:]
   - Dining: Imagen restaurante + nombre + beneficio (% descuento / mesa prioritaria)
   - Spend & Earn: Mecánica clara + imagen del premio
   - Cultural (Teatro Colón): Imagen del venue + fechas + botón de abonos
   - Partner (Smiles, Farmacity): Logo partner + mecánica + CTA
5. Separator
6. Módulos adicionales de beneficios
7. Footer con legales numerados y URL de T&C
```

---

## Diferencias CENT vs PLAT

| | Centurion (CENT) | Platinum (PLAT) |
|---|---|---|
| Tarjeta | Negra mate | Plateada metalizada |
| Copy eyebrow | "EXCLUSIVO CENTURION" | "EXCLUSIVO PLATINUM" |
| Tono | Ultralujo, "sin límites" | Premium, sofisticado |
| Umbrales de gasto | Más altos | Altos |
| Versión del email | `-CENT` en nombre de archivo | `-PLAT` en nombre de archivo |

---

## Notas

- El botón `#00175A` (azul profundo) es el CTA estándar del segmento PP (no el azul `#006FCF`)
- El `button-primary-dark` es para botón blanco sobre fondo azul
- Teatro Colón: el email incluye la temporada completa con fechas y abonos
- Los emails de Dining requieren link a la reserva (OpenTable, teléfono, app Amex Experiences)
- En campañas Smiles: distinguir bien CENT de PLAT ya que tienen distintos multiplicadores
