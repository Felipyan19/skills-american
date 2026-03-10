# Skill: Segmento TRAVEL (Centurion y Platinum)

## Descripción del Segmento
Emails de **beneficios de viaje** para titulares de tarjetas Centurion y Platinum de American Express Argentina. El contenido gira en torno a destinos, hoteles, aeropuertos, Duty Free y experiencias travel premium.

**Archivos de referencia:**
- `TRAVEL-Dia-De-La-Madre-Oct25-CENT.html` / `...-PLAT.html` → Día de la Madre travel deal
- `TRAVEL-Mexico-Sept25-CENT.html` / `...-PLAT.html` → Destino México
- `TRAVEL-Miami-Nov25-CENT.html` / `TRAVEL-Miami-Nov25_PLAT.html` → Destino Miami

---

## Características Distintivas

| Atributo | Valor |
|---|---|
| Template | `AMX_GBS Templates 4.2` |
| Fondo body | `#E0E0E0` |
| Brand Panel | `Consumer Default-v4.2` con tarjeta CENT o PLAT |
| Color primario | `#00175A` (igual que PP) |
| Audiencia | Titulares Platinum y Centurion |
| Temáticas | Destinos internacionales, hoteles, aeropuertos, Duty Free |
| CTAs comunes | "Reservá ahora", "Conocé más", "Ver paquetes" |

---

## Brand Panel TRAVEL (idéntico al de PP)

Ver skill `06-PP-Cent-Plat.md` — el brand panel es el mismo `Consumer Default-v4.2` con imagen de tarjeta Centurion o Platinum.

---

## Hero Banner: Imagen Destino Full Width

El hero de los emails TRAVEL suele ser una **imagen de alta calidad del destino** (ciudad, playa, hotel) a ancho completo de 620px.

```html
<!-- START: Hero Full Width — Destino -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td>
      <!-- Desktop: imagen del destino -->
      <img src="[URL_IMG_DESTINO_620px]" alt="[Ciudad, País]" width="620"
           style="height:auto; display:block; color:#3D3D3D;" class="full-width">
    </td>
  </tr>
</table>
<!-- END: Hero Full Width -->
```

---

## Hero Banner: Overlay con Nombre del Destino

Alternativa con texto del destino superpuesto sobre la imagen.

```html
<!-- START: Hero Destino con Overlay -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
  <tr>
    <td align="center" bgcolor="#00175A"
        background="[URL_IMG_DESTINO]" width="620" height="350" valign="bottom"
        style="background: url('[URL_IMG_DESTINO]') center / cover no-repeat #00175A;">
      <!--[if gte mso 9]>
      <v:image xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0; display:inline-block; width:620px; height:350px;"
        src="[URL_IMG_DESTINO]" />
      <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
        style="border:0; display:inline-block; position:absolute; width:620px; height:350px;">
        <v:fill opacity="0%" color="#00175A" />
        <v:textbox inset="0,0,0,0">
      <![endif]-->
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td align="center" style="padding:0 40px 40px;">
            <!-- Nombre del destino -->
            <p style="color:#FFFFFF; font-family:'Guardian Egyptian', Georgia, serif;
                      font-size:48px; line-height:54px; margin:0 0 8px;">
              [Ciudad]
            </p>
            <!-- País -->
            <p style="color:#FFFFFF; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                      font-size:18px; line-height:24px; letter-spacing:3px; margin:0;">
              [PAÍS]
            </p>
          </td>
        </tr>
      </table>
      <!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
    </td>
  </tr>
</table>
<!-- END: Hero Destino con Overlay -->
```

---

## Módulo: Beneficio Travel con Borde (TM04 adaptado)

Para mostrar un beneficio travel específico: Duty Free, hotel, upgrade, etc.

```html
<!-- Beneficio Travel destacado -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <td align="center" style="padding:0;">
      <table role="none" cellpadding="0" cellspacing="0" border="0" width="90%">
        <tr>
          <td align="center" style="padding:40px 20px; border:1px solid #737880;">
            <table width="100%" role="none" cellpadding="0" cellspacing="0" border="0">
              <!-- Período de vigencia -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:20px; line-height:23px; padding:0;">
                  <strong>Del [DD/MM] al [DD/MM]</strong>
                </td>
              </tr>
              <!-- Descuento o beneficio -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:69px; line-height:72px; padding:30px 0 0;">
                  <strong>[X]% OFF</strong>
                </td>
              </tr>
              <!-- Beneficio secundario -->
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:25px; line-height:28px; padding:0;">
                  <strong>
                    + Fila preferencial<span style="font-size:11px; line-height:8px; vertical-align:11px; font-weight:normal;">1</span>
                  </strong>
                </td>
              </tr>
              <tr>
                <td align="center"
                    style="color:#00175a; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                           font-size:20px; line-height:23px; padding:4px 0 0;">
                  para socios American Express.
                </td>
              </tr>
              <!-- Logo comercio/aeropuerto -->
              <tr>
                <td align="center" valign="top" style="padding:19px 0 0;">
                  <img src="[LOGO_PARTNER_TRAVEL]" alt="[Nombre del partner]"
                       style="border:0; display:block; height:auto; width:149px;" width="149">
                </td>
              </tr>
              <!-- CTA -->
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
                  <strong>[Condiciones del beneficio travel.]</strong>
                  Beneficio no v&aacute;lido para compras realizadas a trav&eacute;s de plataformas de pago.
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Módulo: Imagen de Hotel / Destino con Descripción

```html
<!-- Hotel / Destino con info lateral -->
<table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#FFFFFF">
  <tr>
    <!-- Imagen del hotel/destino -->
    <th width="310" class="full-width-block" valign="top" align="left">
      <a href="[URL_HOTEL]" target="_blank" style="text-decoration:none; border:none; outline:0;">
        <img src="[IMG_HOTEL]" alt="[Nombre del hotel]" width="310"
             style="height:auto; display:block; color:#3D3D3D;" class="full-width">
      </a>
    </th>
    <!-- Información del beneficio -->
    <th width="310" class="full-width-block" valign="middle" align="left"
        style="padding:30px; background:#F8F8F8;" bgcolor="#F8F8F8">
      <!-- Nombre del hotel -->
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:20px; line-height:24px; margin-bottom:8px;">
        <strong>[Nombre del Hotel]</strong>
      </p>
      <!-- Destino -->
      <p style="color:#3D3D3D; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:14px; line-height:20px; letter-spacing:1px; margin-bottom:16px;">
        [CIUDAD, PAÍS]
      </p>
      <!-- Beneficio -->
      <p style="color:#00175A; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                font-size:16px; line-height:22px; margin-bottom:20px;">
        ✦ Upgrade de habitaci&oacute;n<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">1</span><br>
        ✦ Desayuno sin cargo<span style="font-size:11px; line-height:8px; vertical-align:7px; font-weight:normal;">2</span><br>
        ✦ Check-out tardío
      </p>
      <!-- CTA -->
      <a href="[URL_RESERVA]" target="_blank"
         style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;
                color:#006FCF; font-size:15px; line-height:22px; text-decoration:underline;">
        Reserv&aacute; ahora
      </a>
    </th>
  </tr>
</table>
```

---

## Estructura Típica de Email TRAVEL

```
1. Preheader (PH01-v4.2)
2. Brand Panel (Consumer Default-v4.2 con tarjeta CENT o PLAT)
3. Hero Banner — Imagen del destino / aeropuerto (full width o con overlay)
4. [Según tipo de campaña:]

   DESTINO (Miami, México, etc.):
   → Bloque con nombre del destino + descripción + qué incluye
   → Grid de hoteles o experiencias en el destino
   → CTA: "Reservá tu viaje"

   DÍA DE LA MADRE / FECHA ESPECIAL:
   → Hero temático + copy afectivo
   → Destinos sugeridos (2-3 opciones)
   → Beneficios por pagar con Amex
   → CTA: "Regalá una experiencia"

   DUTY FREE / AEROPUERTO:
   → Caja de descuento (TM04) con % OFF
   → Logo del aeropuerto/local
   → Condiciones de uso (cupo máximo, período)
   → CTA: "Conocé más"

5. Separator
6. Beneficios adicionales del programa travel (FHR, IATA, etc.)
7. Footer con legales
```

---

## Destinos Recurrentes y Copy

| Destino | Temporada | Copy típico |
|---|---|---|
| Miami | Nov-Feb (verano boreal) | "La energía de Miami te espera" |
| México | Sep-Nov | "Descubrí la magia de México" |
| Día de la Madre | Octubre (AR) | "El mejor regalo eres vos" |
| Navidad / Año Nuevo | Dic | "Celebrá en el destino soñado" |

---

## Notas

- Los botones CTA en TRAVEL usan `#00175A` (igual que PP), nunca `#006FCF`
- Duty Free: el beneficio aplica en **Duty Free Shop Argentina** (Aeropuerto Internacional Ezeiza)
- Siempre incluir tope de reintegro en legales: "Tope de reintegro $[MONTO] por cuenta, por mes"
- Diferencias CENT/PLAT: los beneficios pueden ser más exclusivos para Centurion (cupo más limitado, montos más altos)
- Fine Hotels & Resorts (FHR) es el programa de hoteles para Platinum y Centurion — incluir si es relevante
- Los emails de destino pueden incluir un grid de 2-3 hoteles recomendados en el destino
