# MERCHANT-Shot-deporte-DIC25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` para el Shot Deporte de diciembre 2025.

## Payloads de uso

### Version corta

Usa todos los defaults exactos definidos para `H04`, `B28` a `B32` y `F05`.

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H04",
  "body": ["B28", "B29", "B30", "B31", "B32"],
  "footer": "F05",
  "globals": {
    "includeSeparators": false
  }
}
```

### Edicion version corta

Mantiene el orden exacto, pero convierte solo los componentes editados a `{ "id": "...", "props": {...} }`.

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H04",
    "props": {
      "greetingText": "Hola {(FULLNAME)}",
      "loginLabel": "Entrar"
    }
  },
  "body": [
    {
      "id": "B28",
      "props": {
        "headlineHtml": "<strong style=\"font-family: 'BentonSans400', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;font-size:29px;\">Entren&aacute; distinto</strong> <br>este verano",
        "heroImageUrl": "https://example.com/custom-hero-deporte.jpg"
      }
    },
    "B29",
    {
      "id": "B30",
      "props": {
        "dateLabel": "Del 5 al 12 de enero",
        "ctaUrl": "https://example.com/beneficio-clubes",
        "ctaLabel": "Ver clubes"
      }
    },
    "B31",
    "B32"
  ],
  "footer": {
    "id": "F05",
    "props": {
      "taglineDesktopUrl": "https://example.com/footer-tagline-desktop.jpg",
      "taglineMobileUrl": "https://example.com/footer-tagline-mobile.jpg",
      "legalHtml": "<strong>1) Legal custom para clubes.</strong><br><br><strong>2) Legal custom para Decathlon.</strong><br><br><strong>3) Legal custom para padel.</strong><br><br>&reg; 2026 AMERICAN EXPRESS ARGENTINA S.A."
    }
  },
  "globals": {
    "includeSeparators": false
  }
}
```

### Version corta desde tipo de campana y grupo

Equivalente a la version corta, resuelto desde el ejemplo de modulo 1.

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-deporte"
}
```

### Edicion corta desde tipo de campana y grupo

El server toma el payload exacto de `group/campaignType` y mergea los overrides de `header`, `body`, `footer` y `globals`.

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-deporte",
  "header": {
    "id": "H04",
    "props": {
      "greetingText": "Hola {(FULLNAME)}",
      "loginLabel": "Entrar"
    }
  },
  "body": [
    {
      "id": "B28",
      "props": {
        "headlineHtml": "<strong style=\"font-family: 'BentonSans400', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;font-size:29px;\">Entren&aacute; distinto</strong> <br>este verano",
        "heroImageUrl": "https://example.com/custom-hero-deporte.jpg"
      }
    },
    {
      "id": "B30",
      "props": {
        "dateLabel": "Del 5 al 12 de enero",
        "ctaUrl": "https://example.com/beneficio-clubes",
        "ctaLabel": "Ver clubes"
      }
    }
  ],
  "footer": {
    "id": "F05",
    "props": {
      "taglineDesktopUrl": "https://example.com/footer-tagline-desktop.jpg",
      "taglineMobileUrl": "https://example.com/footer-tagline-mobile.jpg",
      "legalHtml": "<strong>1) Legal custom para clubes.</strong><br><br><strong>2) Legal custom para Decathlon.</strong><br><br><strong>3) Legal custom para padel.</strong><br><br>&reg; 2026 AMERICAN EXPRESS ARGENTINA S.A."
    }
  }
}
```

### Detallada

Esta version declara todos los defaults editables por componente. Debe renderizar igual que la version corta mientras no se cambien los valores.

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H04",
    "props": {
      "preheaderLabel": "PUBLICIDAD",
      "viewOnlineUrl": "https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}",
      "logoHref": "http://www.americanexpress.com.ar",
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_01.jpg",
      "logoAlt": "American Express, opens a new tab",
      "taglineHref": "http://www.americanexpress.com.ar",
      "taglineUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_02.jpg",
      "taglineAlt": "No vivas la vida sin ella(TM)",
      "accountLabel": "Tu cuenta termina en:",
      "accountSuffix": "{(LAST_5)}",
      "memberSinceLabel": "Miembro desde:",
      "memberSince": "{(MEMBER_SINCE)}",
      "greetingText": "Hola {(FULLNAME)}",
      "loginUrl": "https://www.americanexpress.com/es-ar/account/login?email_consumer",
      "loginAriaLabel": "American Express account, opens a new tab",
      "loginLabel": "Mi cuenta"
    }
  },
  "body": [
    {
      "id": "B28",
      "props": {
        "heroImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_04b.jpg",
        "headlineHtml": "<strong style=\"font-family: 'BentonSans400', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;font-size:29px;\">La energ&iacute;a</strong> <br>\n                        que te mueve"
      }
    },
    {
      "id": "B29",
      "props": {
        "introHtml": "Lo que necesit&aacute;s para entrenar mejor, <br class=\"mobile-off\"> ahora con <strong style=\"color: #006fcf;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">beneficios</strong> pensados para vos."
      }
    },
    {
      "id": "B30",
      "props": {
        "dateLabel": "Del 15 al 20 de diciembre",
        "discountImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_05.png",
        "discountImageAlt": "10% OFF sin tope y en el acto",
        "plusImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_06.png",
        "plusImageAlt": "+",
        "installmentsImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_07.png",
        "installmentsImageAlt": "3, 6, 9 Y 12 CUOTAS SIN INTER&Eacute;S(1)",
        "benefitLine": "en nuevos planes o renovaciones",
        "primaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_08.jpg",
        "primaryLogoAlt": "MEGATLON",
        "secondaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_09.jpg",
        "secondaryLogoAlt": "Fiter | Fitness para vos",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/megatlon-y-fiter?utm_source=news&utm_medium=email&utm_campaign=megatlon-fiter",
        "ctaLabel": "M&aacute;s info",
        "disclaimerHtml": "V&Aacute;LIDO PARA COMPRAS PRESENCIALES EN SUCURSALES SELECCIONADAS."
      }
    },
    {
      "id": "B31",
      "props": {
        "leftDateLabel": "Del 15 al 21 de diciembre",
        "leftOfferImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_10.png",
        "leftOfferImageAlt": "Hasta 6 CUOTAS SIN INTER&Eacute;S(2)",
        "leftBenefitLine": "en compras presenciales",
        "leftLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_11.jpg",
        "leftLogoAlt": "DECATHLON",
        "leftCtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/decathlon?utm_source=news&utm_medium=email&utm_campaign=decathlon",
        "leftCtaLabel": "M&aacute;s info",
        "rightDateLabel": "Del 1 al 31 de diciembre",
        "rightOfferImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_12.png",
        "rightOfferImageAlt": "15% OFF(3)",
        "rightBenefitLine": "en el pago del abono mensual",
        "rightLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_13.jpg",
        "rightLogoAlt": "LASAIGUES PADEL",
        "rightCtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/lasaigue?utm_source=news&utm_medium=email&utm_campaign=lasaigues",
        "rightCtaLabel": "M&aacute;s info",
        "rightDisclaimerHtml": "TOPE DE REINTEGRO DE $15.000 <br> POR CUENTA, POR MES. STOCK LIMITADO."
      }
    },
    {
      "id": "B32",
      "props": {
        "disclaimerHtml": "BENEFICIOS NO V&Aacute;LIDOS PARA PAGOS REALIZADOS <br class=\"mobile-on\" style=\"display: none;\"> A TRAV&Eacute;S DE PLATAFORMAS DE PAGO Y/O AGREGADORES."
      }
    }
  ],
  "footer": {
    "id": "F05",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_14.jpg",
      "taglineMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_15.jpg",
      "taglineAlt": "No vivas la vida sin ella(TM)",
      "instagramUrl": "https://www.instagram.com/americanexpressarg/",
      "instagramImg": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_16.png",
      "instagramAlt": "S&iacute;guenos en Instagram",
      "facebookUrl": "https://www.facebook.com/americanexpressargentina",
      "facebookImg": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_17.png",
      "facebookAlt": "S&iacute;guenos en Facebook",
      "youtubeUrl": "https://www.youtube.com/user/AmericanExpressArg",
      "youtubeImg": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_18.png",
      "youtubeAlt": "S&iacute;guenos en Youtube",
      "privacyUrl": "https://www.americanexpress.com/argentina/legal/privacy_statement.shtml",
      "privacyLabel": "Privacidad",
      "contactUrl": "https://www.americanexpress.com/ar/content/ayuda/contactenos.html",
      "contactLabel": "Contacto",
      "updateEmailUrl": "https://www.americanexpress.com/es-ar/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Fmyca%2Fintl%2Facctmaintain%2Fcanlac%2FchangeDetails.do%3Frequest_type%3D%26Face%3Des_AR%26sorted_index%3D0",
      "updateEmailLabel": "Actualizar email",
      "unsubscribeUrl": "https://global.americanexpress.com/privacy/argentina/#/ipp",
      "unsubscribeLabel": "Desuscribirse",
      "cftImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/101225-MERCHANT-Shot-deporte-DIC25_19.png",
      "cftImageAlt": "1)2) C.F.T.:0,00%",
      "legalHtml": "\n        <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">1) TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. PARA M&Aacute;S INFORMACI&Oacute;N O LIMITACIONES APLICABLES, CONSULTE EN</strong> <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/megatlon-y-fiter\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;\"><strong style=\"border:none;outline:0;text-decoration:none;color:#00175a;font-weight: bold;word-wrap: break-word;word-break: break-all;font-family:  HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/megatlon-y-fiter.</strong></a> <br><br>\n\n\n        <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">2) TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. PARA M&Aacute;S INFORMACI&Oacute;N O LIMITACIONES APLICABLES, CONSULTE EN</strong> <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/decathlon\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;\"><strong style=\"border:none;outline:0;text-decoration:none;color:#00175a;font-weight: bold;word-wrap: break-word;word-break: break-all;font-family:  HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/decathlon.</strong></a> <br><br>\n\n        <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">3) PARA M&Aacute;S INFORMACI&Oacute;N O LIMITACIONES APLICABLES, CONSULTE EN:</strong> <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/lasaigues\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;\"><strong style=\"border:none;outline:0;text-decoration:none;color:#00175a;font-weight: bold;word-wrap: break-word;word-break: break-all;font-family:  HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/salud-y-belleza/lasaigues.</strong></a>\n\n\n          <br><br>\n\n            Los datos personales son almacenados en una base de datos, cuyo responsable es American Express Argentina S.A. con domicilio legal en Arenales 707, entrepiso, CP C1061AAA, C.A.B.A. Usted podr&aacute; -en cualquier momento- solicitar el retiro o bloqueo de su nombre, total o parcial, de nuestra base de datos y podr&aacute; solicitar informaci&oacute;n acerca del nombre del responsable o usuario de la base de datos que provey&oacute; su informaci&oacute;n. Ley 25.326 art.27. - inc. 3. &ldquo;El titular podr&aacute; en cualquier momento solicitar el retiro o bloqueo de su nombre de los bancos de datos a los que se refiere el presente art&iacute;culo&rdquo;. Decreto 1558/01 - art. 27. - 3er. P&aacute;rrafo. &ldquo;En toda comunicaci&oacute;n con fines de publicidad que se realice por correo, tel&eacute;fono, correo electr&oacute;nico, internet u otro medio a distancia a conocer, se deber&aacute; indicar, en forma expresa y destacada, la posibilidad del titular del dato de solicitar el retiro o bloqueo, total o parcial, de su nombre de la base de datos. A pedido del interesado, se deber&aacute; informar el nombre del responsable o usuario del banco de datos que provey&oacute; la informaci&oacute;n&rdquo;.\n\n            <br/><br/>\n\n            Instrucciones para cancelar la suscripci&oacute;n: este correo electr&oacute;nico publicitario est&aacute; destinado a residentes de Argentina y fue enviado a <strong style=\"color:#000000;font-weight:normal;word-wrap: break-word;word-break: break-all;\">{(EMAIL)}</strong>. Si ha sido recibido en una direcci&oacute;n diferente, significa que fue reenviado. Si no desea recibir nuevos mensajes publicitarios en el futuro, por favor responda este e-mail con la palabra &ldquo;borrar&rdquo; en el asunto (subject), o visite las <a href=\"https://global.americanexpress.com/privacy/argentina/#/ipp\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">preferencias de correo electr&oacute;nico</a> en el sitio web de American Express. Servicio al cliente: por favor no responda (reply) este e-mail y dirija todas sus consultas a <a href=\"https://www.americanexpress.com/ar/content/ayuda/contactenos.html\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">Servicio al Cliente</a>. Declaraci&oacute;n sobre privacidad: para saber c&oacute;mo obtenemos, aseguramos y utilizamos su informaci&oacute;n personal cumpliendo con la ley 25.326, visite la declaraci&oacute;n sobre privacidad de American Express ingresando en: <a href=\"http://www.americanexpress.com/argentina/legal/privacy_statement.shtml\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">www.americanexpress.com.ar/privacidad</a>.\n\n\n           <!-- <br><br> &copy; 2025 American Express Company.-->\n            <br><br> &reg; 2025 AMERICAN EXPRESS ARGENTINA S.A.\n"
    }
  },
  "globals": {
    "includeSeparators": false
  }
}
```

## Contrato de edicion

- Mantener el orden `H04 -> B28 -> B29 -> B30 -> B31 -> B32 -> F05`.
- No activar separadores automaticos; los bloques ya incluyen sus propios fondos, bordes y paddings.
- El contenido editable esta en snippets dedicados de Shot Deporte. No editar los snippets genericos `hb18.html`, `tm04.html`, `hb08.html`, `fm05.html`, `fm02.html` ni `fm04.html` para cambios de esta campana.
- Si se cambian descuentos, cuotas o comercios, actualizar cuerpo y legales en la misma pasada.
- Las imagenes usan el prefijo `101225-MERCHANT-Shot-deporte-DIC25_`. Si se reemplazan assets, conservar dimensiones y `alt` equivalentes.
- El footer `F05` usa snippets dedicados y acepta `legalHtml` por props; si no se envia, usa el legal exacto de la pieza de referencia.
- `H04`, los body components `B28` a `B32` y `F05` aceptan variantes por `props`. Si no se envian `props`, usan los valores exactos del HTML de referencia.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H04` | Preheader + brand panel | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-shot-deporte-dic25.html` |
| `B28` | Hero energia | `catalog/snippets/marigold-v4.2/hb18-merchant-shot-deporte-dic25.html` |
| `B29` | Intro entrenamiento | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-intro.html` |
| `B30` | Megatlon + Fiter | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-clubs.html` |
| `B31` | Decathlon + Lasaigues Padel | `catalog/snippets/marigold-v4.2/hb08-merchant-shot-deporte-dic25.html` |
| `B32` | Closing oscuro | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-deporte-dic25-closing.html` |
| `F05` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05-merchant-shot-deporte-dic25.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-shot-deporte-dic25.html`, `catalog/snippets/marigold-v4.2/fm03-merchant-shot-deporte-dic25.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-shot-deporte-dic25.html` |

## Campos de variantes

Campos soportados por componente:

| API | Props |
|---|---|
| `H04` | `preheaderLabel`, `viewOnlineUrl`, `logoHref`, `logoUrl`, `logoAlt`, `taglineHref`, `taglineUrl`, `taglineAlt`, `accountLabel`, `accountSuffix`, `memberSinceLabel`, `memberSince`, `greetingText`, `loginUrl`, `loginAriaLabel`, `loginLabel` |
| `B28` | `heroImageUrl`, `headlineHtml` |
| `B29` | `introHtml` |
| `B30` | `dateLabel`, `discountImageUrl`, `discountImageAlt`, `plusImageUrl`, `plusImageAlt`, `installmentsImageUrl`, `installmentsImageAlt`, `benefitLine`, `primaryLogoUrl`, `primaryLogoAlt`, `secondaryLogoUrl`, `secondaryLogoAlt`, `ctaUrl`, `ctaLabel`, `disclaimerHtml` |
| `B31` | `leftDateLabel`, `leftOfferImageUrl`, `leftOfferImageAlt`, `leftBenefitLine`, `leftLogoUrl`, `leftLogoAlt`, `leftCtaUrl`, `leftCtaLabel`, `rightDateLabel`, `rightOfferImageUrl`, `rightOfferImageAlt`, `rightBenefitLine`, `rightLogoUrl`, `rightLogoAlt`, `rightCtaUrl`, `rightCtaLabel`, `rightDisclaimerHtml` |
| `B32` | `disclaimerHtml` |
| `F05` | `taglineDesktopUrl`, `taglineMobileUrl`, `taglineAlt`, `instagramUrl`, `instagramImg`, `instagramAlt`, `facebookUrl`, `facebookImg`, `facebookAlt`, `youtubeUrl`, `youtubeImg`, `youtubeAlt`, `privacyUrl`, `privacyLabel`, `contactUrl`, `contactLabel`, `updateEmailUrl`, `updateEmailLabel`, `unsubscribeUrl`, `unsubscribeLabel`, `cftImageUrl`, `cftImageAlt`, `legalHtml` |

Plan de prueba 1 a 1:

1. Probar el payload base y guardar el HTML generado como baseline visual.
2. Enviar `H04` como `{ "id": "H04", "props": {...} }`; confirmar logo, greeting y boton.
3. Enviar solo `B28` con `headlineHtml` y `heroImageUrl`; confirmar que cambia hero y que `manifest.requested.body` sigue en `B28 -> B29 -> B30 -> B31 -> B32`.
4. Enviar solo `B29` con `introHtml`; confirmar que no cambia el resto del cuerpo.
5. Enviar solo `B30` con un CTA o logo nuevo; revisar que legal/disclaimer siga coherente.
6. Enviar solo `B31` con cambios de lado izquierdo y derecho; revisar que los links y logos correspondan.
7. Enviar solo `B32` con `disclaimerHtml`; revisar que cierre y legales no contradigan los claims.
8. Enviar `F05` como `{ "id": "F05", "props": {...} }`; confirmar taglines, redes, nav y legales.
9. Si cambia un descuento, cuota, fecha o tope, actualizar tambien `F05` en la misma pasada.

## Checklist antes de cerrar

- Verificar CTAs de Megatlon/Fiter, Decathlon y Lasaigues.
- Verificar que los indicadores legales `(1)` a `(3)` correspondan con el footer.
- Probar `POST /api/compose-email?html` con el payload de arriba.
- Revisar el `manifest.expanded` para confirmar que la secuencia mantenga los snippets dedicados.
