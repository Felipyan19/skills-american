# Skill: Segmento MERCHANT - Socio

## Descripción del Segmento
Emails para **socios/beneficiarios** de comercios que aceptan American Express. Incluye newsletters con múltiples promociones, "Shots" (email de una sola oferta) y Special Offers (catálogo de comercios).

**Archivos de referencia:**
- `MERCHANT-Newsletter-Dic25.html` → Newsletter multipromociones
- `MERCHANT-Shot-Travel-Agst25.html` → Shot travel (email único, viajes)
- `MERCHANT-Shot-deporte-DIC25.html` → Shot deporte (email único, deportes)
- `MERCHANT-SHOT-Navidad-Dic25.html` → Shot navidad
- `MERCHANT-Special-Offers-Dic25.html` → Catálogo de ofertas especiales

---

## Características Distintivas

| Atributo | Valor |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Brand Panel | `Consumer Default-v4.2` (logo Amex + tagline + cuenta) |
| Tagline logo | "No vivas la vida sin ella" |
| Personalización | `{(FULLNAME)}`, `{(LAST_5)}`, `{(MEMBER_SINCE)}` |
| Tipos de email | Newsletter (multi), Shot (mono), Special Offers |
| Formato Newsletter | Varias promociones apiladas con separadores |
| Formato Shot | Una sola oferta con hero grande |

---

## Brand Panel MERCHANT Socio (Consumer Default-v4.2)

```html
<!-- START: Consumer Default-v4.2 (MERCHANT Socio) -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="border-bottom:solid 1px #E0E0E0; padding:20px;" class="pd10">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="top" width="137" style="width:137px;">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <td width="60" style="width:60px;" class="bp-logo">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_LOGO_AMEX]" alt="American Express, opens a new tab" width="60"
                         style="width:60px; height:auto; color:#3D3D3D;" class="bp-logo">
                  </a>
                </td>
                <td width="150" style="padding-left:10px" class="mobile-off">
                  <a href="http://www.americanexpress.com.ar" target="_blank">
                    <img src="[IMG_TAGLINE]" alt="No vivas la vida sin ella" width="150"
                         style="width:150px; height:auto; color:#3D3D3D;">
                  </a>
                </td>
              </tr>
            </table>
          </td>
          <td align="right" valign="top">
            <p class="bp-text"
               style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color:#3D3D3D; font-size:15px; line-height:22px;">
              Tu cuenta termina en: <br class="mobile-on" style="display:none;" />
              {(LAST_5)} <br>
              <span class="mobile-off">Miembro desde: {(MEMBER_SINCE)}</span>
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
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

## Formato: SHOT (Email Mono-Oferta)

Un solo beneficio destacado con imagen hero grande y CTA claro.

```
1. Preheader
2. Brand Panel (Consumer Default-v4.2)
3. Hero Banner full width o con overlay (imagen temática: viaje, deporte, navidad)
4. Bloque de texto con beneficio
5. CTA principal
6. Legales
7. Footer
```

```html
<!-- Hero Shot - Full Width con texto debajo -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <a href="[URL_CTA]" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="[IMG_SHOT_HERO]" alt="[Descripción del beneficio]" width="620"
             style="height:auto; display:block; color:#3D3D3D; width:100%;" class="full-width">
      </a>
    </td>
  </tr>
</table>

<!-- Bloque texto principal -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding: 40px 40px 20px;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center"
              style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:26px; line-height:30px; padding-bottom:15px;">
            <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              Título principal del beneficio
            </strong>
          </td>
        </tr>
        <tr>
          <td align="center"
              style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:15px; line-height:22px; padding-bottom:30px;">
            Descripción detallada del beneficio para socios American Express.
          </td>
        </tr>
        <!-- CTA -->
        <tr>
          <td align="center">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="180" height="44"
                   style="width:180px; height:44px; border-radius:4px; background:#006FCF;" class="button-primary-light">
              <tr><td align="center" valign="middle">
                <table role="none" cellpadding="0" cellspacing="0" border="0"
                       style="border-radius:4px; border:2px solid #006FCF; width:176px; height:42px">
                  <tr><td align="center" valign="middle" height="44">
                    <a href="[URL_CTA]" target="_blank"
                       style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                              color:#FFFFFF; display:inline-block; padding:12px 0;
                              text-decoration:none; width:176px; font-size:15px; line-height:22px;">
                      <strong style="font-weight:normal; color:#FFFFFF;">Conoc&eacute; el beneficio</strong>
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

## Formato: NEWSLETTER (Email Multi-Oferta)

Múltiples promociones apiladas, cada una con su propia imagen, título y CTA. Separadas por `Separator`.

```
1. Preheader
2. Brand Panel(s) (puede haber más de uno si es co-branded)
3. Hero Banner principal
4. [Promoblock 1: Imagen + Texto + CTA]
5. Separator
6. [Promoblock 2: Imagen + Texto + CTA]
7. Separator
8. [Promoblock 3...]
9. Footer con todos los legales numerados
```

### Bloque de Promoción (Newsletter)

```html
<!-- PROMO BLOCK — para cada oferta en el newsletter -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td style="padding: 30px 40px;" class="pd20">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <!-- Imagen del comercio/oferta -->
        <tr>
          <td align="center" style="padding-bottom: 20px;">
            <a href="[URL_OFERTA]" target="_blank" style="text-decoration:none; border:none; outline:0;">
              <img src="[IMG_OFERTA]" alt="[Nombre Comercio]" width="540"
                   style="height:auto; display:block; color:#3D3D3D;" class="full-width">
            </a>
          </td>
        </tr>
        <!-- Título oferta -->
        <tr>
          <td align="center"
              style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:22px; line-height:26px; padding-bottom:10px;">
            <strong style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">
              [X]% OFF en [Comercio]<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>
            </strong>
          </td>
        </tr>
        <!-- Descripción -->
        <tr>
          <td align="center"
              style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                     font-size:15px; line-height:22px; padding-bottom:20px;">
            Pagando con tu tarjeta American Express.
          </td>
        </tr>
        <!-- CTA -->
        <tr>
          <td align="center">
            <a href="[URL_OFERTA]" target="_blank"
               style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      color:#006FCF; font-size:15px; line-height:22px; text-decoration:underline;
                      border:none; outline:0;">
              Ver m&aacute;s
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Formato: SPECIAL OFFERS (Grilla de Comercios)

Grid de logos o thumbnails de comercios participantes, organizados en 2-3 columnas.

```html
<!-- Grid de 2 comercios por fila -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <!-- Comercio 1 -->
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;"
        class="half-width-block BrdrMobile">
      <a href="[URL_COMERCIO_1]" target="_blank" style="text-decoration:none;">
        <img src="[LOGO_COMERCIO_1]" alt="[Nombre]" width="250"
             style="height:auto; display:block;" class="full-width">
      </a>
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:16px; line-height:20px; padding-top:10px; text-align:center;">
        <strong>[X]% OFF</strong><span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span>
      </p>
    </td>
    <!-- Comercio 2 -->
    <td width="50%" align="center" valign="top" style="padding: 20px 10px;"
        class="half-width-block">
      <!-- misma estructura -->
    </td>
  </tr>
</table>
```

---

## Notas

- Newsletter usa `BrdrMobile` en mobile para mostrar separadores entre columnas
- Los Shot emails son más simples y directos, el Newsletter es más complejo con múltiples secciones
- En Special Offers, los porcentajes de descuento se destacan en azul `#00175A`
- Siempre incluir referencia numérica a legales en superíndice al lado de cada descuento
- El footer del Newsletter incluye todos los legales de todas las promos numeradas
- Temáticas recurrentes: viajes, deporte, gastronomía, navidad/temporada
