# MERCHANT-Shot-Travel-Agst25

Campana exacta de modulo 1 para MERCHANT - Socio. Usa componentes dedicados de `marigold-v4.2` y snippets dinamicos con defaults para reproducir la pieza de Travel de agosto 2025.

## Payloads de uso

### Version corta

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H02",
  "body": [
    "B12",
    "B13",
    "B14",
    "B15",
    "B17",
    "B16"
  ],
  "footer": "F03",
  "globals": {
    "includeSeparators": false
  }
}
```

### Edicion version corta

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H02",
    "props": {
      "greetingText": "Hola Travel Custom",
      "loginLabel": "Entrar"
    }
  },
  "body": [
    {
      "id": "B12",
      "props": {
        "heroImageUrl": "https://example.com/travel-hero.jpg",
        "headlineHtml": "Eleg&iacute; un nuevo destino"
      }
    },
    {
      "id": "B13",
      "props": {
        "primaryLogoUrl": "https://example.com/aerolineas-alt.png",
        "primaryBenefitLine": "en vuelos regionales",
        "secondaryCtaLabel": "Ver agencias"
      }
    },
    {
      "id": "B14",
      "props": {
        "offerImageUrl": "https://example.com/compras-offer.png",
        "benefitHtml": "20% OFF custom",
        "ctaLabel": "Comprar"
      }
    },
    {
      "id": "B15",
      "props": {
        "primaryLogoUrl": "https://example.com/spa-a.png",
        "offerImageAlt": "15% OFF custom spa",
        "ctaUrl": "https://example.com/spa"
      }
    },
    {
      "id": "B17",
      "props": {
        "headingHtml": "Hoteles custom",
        "step3LogoUrl": "https://example.com/hotel-logo.png",
        "disclaimerHtml": "Disclaimer hoteles custom"
      }
    },
    {
      "id": "B16",
      "props": {
        "closingHtml": "Cierre travel custom"
      }
    }
  ],
  "footer": {
    "id": "F03",
    "props": {
      "taglineDesktopUrl": "https://example.com/travel-footer.jpg",
      "instagramUrl": "https://example.com/instagram",
      "privacyLabel": "Privacidad Travel",
      "legalHtml": "LEGAL TRAVEL CUSTOM"
    }
  },
  "globals": {
    "includeSeparators": false
  }
}
```

### Version corta desde tipo de campana y grupo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-travel"
}
```

### Edicion corta desde tipo de campana y grupo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "MERCHANT - Socio",
  "campaignType": "shot-travel",
  "header": {
    "id": "H02",
    "props": {
      "greetingText": "Hola desde group",
      "loginLabel": "Ingresar"
    }
  },
  "body": [
    {
      "id": "B13",
      "props": {
        "primaryBenefitLine": "en vuelos internacionales",
        "primaryLogoUrl": "https://example.com/aerolineas-group.png"
      }
    },
    {
      "id": "B17",
      "props": {
        "headingHtml": "Hoteles desde group"
      }
    }
  ],
  "footer": {
    "id": "F03",
    "props": {
      "taglineDesktopUrl": "https://example.com/travel-group-footer.jpg",
      "legalHtml": "LEGAL TRAVEL GROUP"
    }
  }
}
```

### Detallada

Esta version declara todos los defaults disponibles por componente. Debe renderizar igual que la version corta mientras no cambies los valores.

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H02",
    "props": {
      "preheaderLabel": "PUBLICIDAD",
      "viewOnlineUrl": "https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}",
      "logoHref": "http://www.americanexpress.com.ar",
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_01.jpg",
      "logoAlt": "American Express, opens a new tab",
      "taglineHref": "http://www.americanexpress.com.ar",
      "taglineUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_02.jpg",
      "taglineAlt": "No vivas la vida sin ella",
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
      "id": "B12",
      "props": {
        "heroImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_04b.jpg",
        "headlineHtml": "Eleg&iacute; el destino, <br> los beneficios ya los ten&eacute;s.",
        "subheadlineHtml": "<strong style=\"color: #006fcf;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">Del 25 al 31 de agosto,</strong> plane&aacute; tu pr&oacute;ximo <strong style=\"color: #006fcf;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">viaje</strong> con estos <strong style=\"color: #006fcf;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">beneficios &uacute;nicos.</strong>"
      }
    },
    {
      "id": "B13",
      "props": {
        "categoryIconUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_05.png",
        "categoryIconAlt": "Agencias",
        "categoryLabel": "Agencias",
        "primaryLogoHref": "https://www.aerolineas.com.ar/",
        "primaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_06.png",
        "primaryLogoAlt": "Aerol&iacute;neas Argentinas",
        "primaryOfferHtml": "<strong>3 Y 6 CUOTAS SIN INTER&Eacute;S</strong><span style=\"font-size: 10px; line-height: 11px; vertical-align: 13px;font-weight:normal;\">1</span>",
        "primaryBenefitLine": "en vuelos nacionales",
        "primaryCtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "primaryCtaLabel": "M&aacute;s informaci&oacute;n",
        "secondaryLogoHref": "https://www.despegar.com.ar/",
        "secondaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_07.jpg",
        "secondaryLogoAlt": "despegar",
        "tertiaryLogoHref": "https://almundo.com.ar/",
        "tertiaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_08.jpg",
        "tertiaryLogoAlt": "Al Mundo",
        "secondaryOfferHtml": "<strong>3 Y 6 CUOTAS SIN INTER&Eacute;S</strong><span style=\"font-size: 10px; line-height: 11px; vertical-align: 13px;font-weight:normal;\">2</span>",
        "secondaryCtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "secondaryCtaLabel": "M&aacute;s informaci&oacute;n",
        "noteHtml": "<strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">Despegar</strong> aplica a paquetes y hoteles. <br>\n                        <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">Al Mundo</strong> aplica a paquetes, hoteles, autos y actividades. <br>\n                        Consult&aacute; modalidad de compra de cada agencia.",
        "paymentDisclaimerHtml": "Beneficios no v&aacute;lidos para compras realizadas <br class=\"mobile-on\" style=\"display: none;\"> a trav&eacute;s de plataforma de pagos y/o agregadores."
      }
    },
    {
      "id": "B14",
      "props": {
        "categoryIconUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_09.png",
        "categoryIconAlt": "Compras",
        "categoryLabel": "Compras",
        "primaryLogoHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/samsonite-especialtravel/?utm_source=news&utm_medium=email&utm_campaign=samsonite",
        "primaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_10.jpg",
        "primaryLogoAlt": "Samsonite",
        "secondaryLogoHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/delsey-especial-travel/?utm_source=news&utm_medium=email&utm_campaign=delsey",
        "secondaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_11.jpg",
        "secondaryLogoAlt": "Delsey Par&iacute;s",
        "tertiaryLogoHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/equipaje-urbano-especial-travel/?utm_source=news&utm_medium=email&utm_campaign=equipajeurbano",
        "tertiaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_12.jpg",
        "tertiaryLogoAlt": "Equipaje Urbano",
        "offerImageHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "offerImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_13.png",
        "offerImageAlt": "25% OFF",
        "benefitHtml": "sin tope y en el acto <br> <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">+ 3 y 6 cuotas sin inter&eacute;s<span style=\"font-size:8px;line-height:8px;vertical-align:8px;font-weight: normal;\">3</span></strong> <br>\n                        <strong style=\"font-weight: normal;color:#00175A;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">en compras presenciales</strong>",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "ctaLabel": "M&aacute;s informaci&oacute;n",
        "paymentDisclaimerHtml": "Beneficios no v&aacute;lidos para compras realizadas <br class=\"mobile-on\" style=\"display: none;\"> a trav&eacute;s de plataforma de pagos y/o agregadores."
      }
    },
    {
      "id": "B15",
      "props": {
        "categoryIconUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_14.png",
        "categoryIconAlt": "Spa",
        "categoryLabel": "Spa",
        "primaryLogoHref": "https://www.alvearicon.com/",
        "primaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_15.jpg",
        "primaryLogoAlt": "Alvear Icon Spa &bull; Beauty &amp; Wellness",
        "secondaryLogoHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/nivel-23-club-amp-spa-buenos-aires-marriott-especialtravel/?utm_source=news&utm_medium=email&utm_campaign=nivel23club&spa",
        "secondaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_16.jpg",
        "secondaryLogoAlt": "Marriott Buenos Aires",
        "tertiaryLogoHref": "https://www.hotelmadero.com/es/relajate/",
        "tertiaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_19.jpg",
        "tertiaryLogoAlt": "Hotel Madero Buenos Aires",
        "quaternaryLogoHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/beneficio/viajes/las-balsas-relais-amp-chateaux2-especialtravel/?utm_source=news&utm_medium=email&utm_campaign=lasbalsas",
        "quaternaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_18.jpg",
        "quaternaryLogoAlt": "Las Balsas",
        "quinaryLogoHref": "https://www.palladiohotelbuenosaires.com/EN/",
        "quinaryLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_17.jpg",
        "quinaryLogoAlt": "Palladio Hotel MGallery Buenos Aires",
        "offerImageHref": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "offerImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_20.png",
        "offerImageAlt": "10% OFF(4)",
        "benefitHtml": "sin tope y en el acto <br>\n                        <strong style=\"font-weight: normal;color:#00175A;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">en servicios de Spa</strong>",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-travel/?utm_source=news&utm_medium=email&utm_campaign=especialtravel",
        "ctaLabel": "M&aacute;s informaci&oacute;n",
        "paymentDisclaimerHtml": "Beneficios no v&aacute;lidos para compras realizadas <br class=\"mobile-on\" style=\"display: none;\"> a trav&eacute;s de plataforma de pagos y/o agregadores."
      }
    },
    {
      "id": "B17",
      "props": {
        "headingHtml": "Adem&aacute;s, del 1 al 31 de agosto <br class=\"mobile-on\" style=\"display: none;\"> disfrut&aacute; de\n              <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">beneficios en hoteles.</strong>",
        "step1LinkUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/escapadas-con-amex/",
        "step1ImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_21.png",
        "step1ImageAlt": "25% OFF(5)",
        "step1ImageWidth": "97",
        "step1DescriptionHtml": "sin tope y en el acto <br> en hoteles seleccionados ",
        "step1CtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/escapadas-con-amex/",
        "step1CtaLabel": "M&aacute;s informaci&oacute;n",
        "step2LinkUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-viajes/",
        "step2ImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_22.png",
        "step2ImageAlt": "4x3(6)",
        "step2ImageWidth": "93",
        "step2DescriptionHtml": "Alojate 3 noches y obten&eacute; <br> una noche extra de regalo <br> en hoteles seleccionados <br class=\"mobile-on\" style=\"display: none;\">",
        "step2CtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-viajes/",
        "step2CtaLabel": "M&aacute;s informaci&oacute;n",
        "step3LinkUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-hoteles/",
        "step3ImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_23.png",
        "step3ImageAlt": "30% OFF(7)",
        "step3ImageWidth": "100",
        "step3DescriptionHtml": "sin tope y en el acto",
        "step3LogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_24.png",
        "step3LogoAlt": "Alvarez Arg&uuml;elles Hoteles",
        "step3LogoWidth": "107",
        "step3CtaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-hoteles/",
        "step3CtaLabel": "M&aacute;s informaci&oacute;n",
        "disclaimerHtml": "No acumulable con otras promociones. <br class=\"mobile-on\" style=\"display: none;\">  Pueden aplicar restricciones. Aplican fechas de veda. <br> Alvarez Arg&uuml;elles Hoteles: cupo diario de hasta 2 habitaciones por hotel."
      }
    },
    {
      "id": "B16",
      "props": {
        "closingHtml": "Disfrut&aacute; de cada destino al m&aacute;ximo <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">#conAmex</strong>"
      }
    }
  ],
  "footer": {
    "id": "F03",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_25a.jpg",
      "taglineMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_25mbl.jpg",
      "taglineAlt": "No vivas la vida sin ella(TM)",
      "instagramUrl": "https://www.instagram.com/americanexpressarg/",
      "instagramImg": "https://mailing.design/amex/CORP-Shot-Travel-Agst25/images/1908-CORP-Shot-Travel-Agst25_26.png",
      "instagramAlt": "Instagram",
      "facebookUrl": "https://www.facebook.com/americanexpressargentina",
      "facebookImg": "https://mailing.design/amex/CORP-Shot-Travel-Agst25/images/1908-CORP-Shot-Travel-Agst25_27.png",
      "facebookAlt": "Facebook",
      "youtubeUrl": "https://www.youtube.com/user/AmericanExpressArg",
      "youtubeImg": "https://mailing.design/amex/CORP-Shot-Travel-Agst25/images/1908-CORP-Shot-Travel-Agst25_28.png",
      "youtubeAlt": "YouTube",
      "privacyUrl": "https://www.americanexpress.com/argentina/legal/privacy_statement.shtml",
      "privacyLabel": "Privacidad",
      "contactUrl": "https://www.americanexpress.com/ar/content/ayuda/contactenos.html",
      "contactLabel": "Contacto",
      "updateEmailUrl": "https://www.americanexpress.com/es-ar/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Fmyca%2Fintl%2Facctmaintain%2Fcanlac%2FchangeDetails.do%3Frequest_type%3D%26Face%3Des_AR%26sorted_index%3D0",
      "updateEmailLabel": "Actualizar email",
      "unsubscribeUrl": "https://global.americanexpress.com/privacy/argentina/#/ipp",
      "unsubscribeLabel": "Desuscribirse",
      "cftImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1908-MERCHANT-Shot-Travel-Agst25_29.jpg",
      "cftImageAlt": "1)2)3) C.F.T.:0,00%",
      "legalHtml": "      AMERICAN EXPRESS ARGENTINA S.A., ARENALES 707- CABA - CP: 1061, CUIT 30-57481687-0. <br><br>\n      1) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA PARA COMPRAS REALIZADAS DESDE EL 25/08/2025 HASTA EL 31/08/2025, AMBAS FECHAS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR (I) AMERICAN EXPRESS ARGENTINA S.A., Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A 3 Y 6 CUOTAS SIN INTER&Eacute;S EN LA COMPRA DE PASAJES PARA VUELOS OPERADOS POR AEROL&Iacute;NEAS ARGENTINAS DENTRO DEL TERRITORIO ARGENTINO, ABONANDO LA TOTALIDAD DE LA COMPRA CON LAS TARJETAS. BENEFICIO V&Aacute;LIDO PARA COMPRAS REALIZADAS EN SUCURSALES DE AEROL&Iacute;NEAS ARGENTINAS, ONLINE A TRAV&Eacute;S DE LA P&Aacute;GINA WEB <a href=\"https://www.aerolineas.com.ar/\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AEROLINEAS.COM.AR,</strong></a> POR VENTA TELEF&Oacute;NICA AL <a href=\"tel:541151993555\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">+54 (11) 5199 3555</strong></a> (DE LUNES A VIERNES DE 8 A 20HS; S&Aacute;BADOS, DOMINGOS Y FERIADOS DE 8 A 14HS), POR WHATSAPP AL <a href=\"https://api.whatsapp.com/send?phone=++5491149404798&text=Hola\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">+54 9 1149404798</strong></a> (DE LUNES A VIERNES DE 8 A 20HS; S&Aacute;BADOS, DOMINGOS Y FERIADOS DE 8 A 14HS) Y A TRAV&Eacute;S DE AGENCIAS DE TURISMO AUTORIZADAS POR AEROL&Iacute;NEAS ARGENTINAS. LA COMPRA DEBE INICIARSE Y CONCLUIRSE DURANTE EL PERIODO DE VIGENCIA ANTES MENCIONADO. NO ACUMULABLE CON OTRAS PROMOCIONES VIGENTES. NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGO Y/O AGREGADORES. LAS COMPRAS CON PLAN DE PAGOS EST&Aacute;N SUJETAS AL L&Iacute;MITE DE CR&Eacute;DITO DISPONIBLE DE CADA TARJETA Y A LOS T&Eacute;RMINOS Y CONDICIONES DE LA ENTIDAD EMISORA. TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN: <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">www.americanexpress.com/es-ar/beneficios/promociones.</strong></a> AEROL&Iacute;NEAS ARGENTINAS S.A. C.U.I.T. N.&ordm; 30-57481687-0. AEP, AV. R. OBLIGADO, TERMINAL 4, S/N 5&deg;P (C1425DAA) CABA. <br><br>\n      2) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA PARA COMPRAS REALIZADAS DESDE EL 25/08/2025 HASTA EL 31/08/2025, AMBAS FECHAS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR (I) AMERICAN EXPRESS ARGENTINA S.A., Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A 3 Y 6 CUOTAS SIN INTER&Eacute;S EN LA COMPRA DE PAQUETES Y HOTELES EN DESPEGAR, Y PAQUETES, HOTELES, AUTOS Y ACTIVIDADES EN ALMUNDO. CONSULTE LA MODALIDAD DE RESERVA DE CADA ESTABLECIMIENTO PARTICIPANTE. PROMOCI&Oacute;N NO COMBINABLE NI ACUMULABLE CON OTRAS PROMOCIONES VIGENTES. NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGO Y/O AGREGADORES. PUEDEN APLICAR RESTRICCIONES ADICIONALES PROPIAS DEL CADA ESTALECIMIENTO PARTICIPANTE. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN: <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/.</strong></a> LAS COMPRAS CON PLAN DE PAGOS EST&Aacute;N SUJETAS AL L&Iacute;MITE DE CR&Eacute;DITO DISPONIBLE DE CADA TARJETA Y A LOS T&Eacute;RMINOS Y CONDICIONES PARA EL USO DE LAS TARJETAS AMERICAN EXPRESS DE LA ENTIDAD EMISORA. TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. <br><br>\n      3) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA PARA COMPRAS REALIZADAS DESDE EL 25/08/2025 HASTA EL 31/08/2025, AMBAS FECHAS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR (I) AMERICAN EXPRESS ARGENTINA S.A., Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A UN 25% DE DESCUENTO, SIN TOPE Y EN EL ACTO, Y A 3 Y 6 CUOTAS SIN INTER&Eacute;S EN SAMSONITE, DELSEY Y EQUIPAJE URBANO, ABONANDO LA TOTALIDAD DE LA COMPRA CON LAS TARJETAS. V&Aacute;LIDO &Uacute;NICAMENTE PARA COMPRAS PRESENCIALES EN SUCURSALES DE CADA MARCA PARTICIPANTE. NO ACUMULABLE CON OTRAS PROMOCIONES. NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGO Y/O AGREGADORES. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/.</strong></a> LAS COMPRAS CON PLAN DE PAGOS EST&Aacute;N SUJETAS AL L&Iacute;MITE DE CR&Eacute;DITO DISPONIBLE DE CADA TARJETA Y A LOS T&Eacute;RMINOS Y CONDICIONES PARA EL USO DE LAS TARJETAS AMERICAN EXPRESS DE LA ENTIDAD EMISORA. TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. <br><br>\n      4) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA PARA COMPRAS REALIZADAS DESDE EL 25/08/2025 HASTA EL 31/08/2025, AMBAS FECHAS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR (I) AMERICAN EXPRESS ARGENTINA S.A., Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A UN 10% DE DESCUENTO, SIN TOPE Y EN EL ACTO, EN EL SERVICIO DE SPA DE LOS HOTELES: LAS BALSAS RELAIS &amp; CHATEAUX, ALVEAR ICON, MARRIOTT BUENOS AIRES, PALLADIO HOTEL BUENOS AIRES &ndash; MGALLERY COLLECTION Y HOTEL MADERO. BENEFICIO V&Aacute;LIDO ABONANDO LA TOTALIDAD DE LA COMPRA CON LAS TARJETAS. BENEFICIO NO ACUMULABLE CON OTRAS PROMOCIONES. BENEFICIO NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGOS Y/O AGREGADORES. V&Aacute;LIDO PARA TARIFAS VIGENTES AL MOMENTO DE REALIZAR LA RESERVA Y SUJETO A DISPONIBILIDAD DEL HOTEL. CONSULTE LA MODALIDAD DE RESERVA Y RESTRICCIONES APLICABLES DE CADA ESTABLECIMIENTO PARTICIPANTE. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/.</strong></a> <br><br>\n      5) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/08/2025 HASTA EL 31/08/2025, AMBOS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR: (I) AMERICAN EXPRESS ARGENTINA S.A. Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A UN 25% DE DESCUENTO, SIN TOPE Y EN EL ACTO, EN HOTELES SELECCIONADOS DISPONIBLES EN <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/promo/escapadas-con-amex/\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/PROMO/ESCAPADAS-CON-AMEX,</strong></a> ABONANDO LA TOTALIDAD DE LA ESTAD&Iacute;A CON LAS TARJETAS. BENEFICIO NO ACUMULABLE CON OTRAS PROMOCIONES. PUEDEN APLICAR RESTRICCIONES. BENEFICIO NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGOS Y AGREGADORES. V&Aacute;LIDO PARA TARIFAS VIGENTES AL MOMENTO DE REALIZAR LA RESERVA Y SUJETO A DISPONIBILIDAD DEL HOTEL. APLICAN FECHAS DE VEDA. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/.</strong></a> <br><br>\n      6) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/08/2025 HASTA EL 31/08/2025, AMBOS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR: (I) AMERICAN EXPRESS ARGENTINA S.A. Y (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A UNA CUARTA NOCHE CONSECUTIVA SIN CARGO EN HOTELES SELECCIONADOS, ABONANDO LA TOTALIDAD DE LA ESTAD&Iacute;A DE TRES (3) NOCHES CON LAS TARJETAS. BENEFICIO NO ACUMULABLE CON OTRAS PROMOCIONES. PUEDEN APLICAR RESTRICCIONES. BENEFICIO NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGOS Y/O AGREGADORES. V&Aacute;LIDO PARA TARIFAS VIGENTES AL MOMENTO DE REALIZAR LA RESERVA Y SUJETO A DISPONIBILIDAD DEL HOTEL. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN: <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">www.americanexpress.com/es-ar/beneficios/promociones/.</strong></a> <br><br>\n      7) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/08/2025 HASTA EL 31/08/2025, AMBOS INCLUSIVE, PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR: (I) AMERICAN EXPRESS ARGENTINA S.A. (II) LOS BANCOS AUTORIZADOS EN LA REP&Uacute;BLICA ARGENTINA POR AMERICAN EXPRESS (LOS &quot;SOCIOS&quot; Y LAS &quot;TARJETAS&quot;). LOS SOCIOS ACCEDER&Aacute;N A UN 30% DE DESCUENTO, SIN TOPE Y EN EL ACTO, EN LA RESERVA DE HABITACIONES DE LOS HOTELES DEL GRUPO ALVAREZ ARG&Uuml;ELLES DISPONIBLES EN <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-hoteles\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/PROMO/ESPECIAL-HOTELES,</strong></a> ABONANDO LA TOTALIDAD DE LA COMPRA CON LAS TARJETAS. V&Aacute;LIDO &Uacute;NICAMENTE PARA RESERVAS POR TEL&Eacute;FONO AL 0810 345 7600 O POR MAIL A <a href=\"mailto:reservas@alvarezarguelles.com\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">RESERVAS@ALVAREZARGUELLES.COM.</strong></a> NO APLICA SOBRE TARIFAS CORPORATIVAS O ESPECIALES. BENEFICIO NO ACUMULABLE CON OTRAS PROMOCIONES. BENEFICIO NO V&Aacute;LIDO PARA RESERVAS EN TEMPORADA ALTA DE CADA DESTINO, FINES DE SEMANA LARGOS, FERIADOS O FESTIVIDADES. V&Aacute;LIDO PARA TARIFAS VIGENTES AL MOMENTO DE REALIZAR LA RESERVA Y SUJETO A DISPONIBILIDAD DEL HOTEL. CUPO DIARIO DE HASTA 2 HABITACIONES POR HOTEL. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN: <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-hoteles\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/PROMO/ESPECIAL-HOTELES.</strong></a> GRUPO HOTELERO ATL&Aacute;NTICO S.A., MONTEVIDEO 1250 &ndash; CP: 1018 &ndash; CABA, CUIT: 33-71138505-9.\n      <br><br>\n      Los datos personales son almacenados en una base de datos, cuyo responsable es American Express Argentina S.A. con domicilio legal en Arenales 707, entrepiso, CP C1061AAA, C.A.B.A. Usted podr&aacute; -en cualquier momento- solicitar el retiro o bloqueo de su nombre, total o parcial, de nuestra base de datos y podr&aacute; solicitar informaci&oacute;n acerca del nombre del responsable o usuario de la base de datos que provey&oacute; su informaci&oacute;n. Ley 25.326 art.27. - inc. 3. &ldquo;El titular podr&aacute; en cualquier momento solicitar el retiro o bloqueo de su nombre de los bancos de datos a los que se refiere el presente art&iacute;culo&rdquo;. Decreto 1558/01 - art. 27. - 3er. P&aacute;rrafo. &ldquo;En toda comunicaci&oacute;n con fines de publicidad que se realice por correo, tel&eacute;fono, correo electr&oacute;nico, internet u otro medio a distancia a conocer, se deber&aacute; indicar, en forma expresa y destacada, la posibilidad del titular del dato de solicitar el retiro o bloqueo, total o parcial, de su nombre de la base de datos. A pedido del interesado, se deber&aacute; informar el nombre del responsable o usuario del banco de datos que provey&oacute; la informaci&oacute;n&rdquo;.\n      <br/><br/>\n      Instrucciones para cancelar la suscripci&oacute;n: este correo electr&oacute;nico publicitario est&aacute; destinado a residentes de Argentina y fue enviado a <strong style=\"color:#000000;font-weight:normal;word-wrap: break-word;word-break: break-all;\">{(EMAIL)}</strong>. Si ha sido recibido en una direcci&oacute;n diferente, significa que fue reenviado. Si no desea recibir nuevos mensajes publicitarios en el futuro, por favor responda este e-mail con la palabra &ldquo;borrar&rdquo; en el asunto (subject), o visite las <a href=\"https://global.americanexpress.com/privacy/argentina/#/ipp\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">preferencias de correo electr&oacute;nico</a> en el sitio web de American Express. Servicio al cliente: por favor no responda (reply) este e-mail y dirija todas sus consultas a <a href=\"https://www.americanexpress.com/ar/content/ayuda/contactenos.html\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">Servicio al Cliente</a>. Declaraci&oacute;n sobre privacidad: para saber c&oacute;mo obtenemos, aseguramos y utilizamos su informaci&oacute;n personal cumpliendo con la ley 25.326, visite la declaraci&oacute;n sobre privacidad de American Express ingresando en: <a href=\"http://www.americanexpress.com/argentina/legal/privacy_statement.shtml\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">www.americanexpress.com.ar/privacidad</a>.\n      <br><br> &copy; 2025 American Express Company."
    }
  },
  "globals": {
    "includeSeparators": false
  }
}
```

## Contrato de edicion

- Mantener el orden `H02 -> B12 -> B13 -> B14 -> B15 -> B17 -> B16 -> F03`.
- No activar separadores automaticos; los bloques ya traen fondos, bordes y padding propios.
- Cada componente puede enviarse como string si no cambia, o como objeto `{ "id": "B12", "props": { ... } }` si necesita variantes.
- `props` se mezcla sobre los defaults definidos en `server/registry.py`, por eso una edicion parcial conserva el resto de la plantilla.
- Para `group: "MERCHANT - Socio"` y `campaignType: "shot-travel"`, el API conserva el payload base y aplica overrides parciales de `header`, `body`, `footer` y `globals`.
- Si se cambian fechas, descuentos o comercios, actualizar cuerpo y legales en la misma pasada.
- Las imagenes originales usan el prefijo `1908-MERCHANT-Shot-Travel-Agst25_`. Si se reemplazan assets, conservar dimensiones y `alt` equivalentes.

## Mapa de componentes

| API | Rol | Snippet a editar |
|---|---|---|
| `H02` | Preheader + brand panel | `catalog/snippets/marigold-v4.2/ph01.html`, `catalog/snippets/marigold-v4.2/brand-panel-merchant-shot-travel-agst25.html` |
| `B12` | Hero Travel | `catalog/snippets/marigold-v4.2/hb18-merchant-shot-travel-agst25.html` |
| `B13` | Agencias | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-agencias.html` |
| `B14` | Compras | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-compras.html` |
| `B15` | Spa | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-spa.html` |
| `B17` | Hoteles triptico | `catalog/snippets/marigold-v4.2/tm03-merchant-shot-travel-agst25.html` |
| `B16` | Cierre hashtag | `catalog/snippets/marigold-v4.2/tm04-merchant-shot-travel-agst25-hashtag.html` |
| `F03` | Footer + legales | `catalog/snippets/marigold-v4.2/fm05-merchant-shot-travel-agst25.html`, `catalog/snippets/marigold-v4.2/fm02-merchant-shot-travel-agst25.html`, `catalog/snippets/marigold-v4.2/fm03-merchant-shot-travel-agst25.html`, `catalog/snippets/marigold-v4.2/fm04-merchant-shot-travel-agst25.html` |

## Campos de variantes

| API | Props soportadas |
|---|---|
| `H02` | `preheaderLabel`, `viewOnlineUrl`, `logoHref`, `logoUrl`, `logoAlt`, `taglineHref`, `taglineUrl`, `taglineAlt`, `accountLabel`, `accountSuffix`, `memberSinceLabel`, `memberSince`, `greetingText`, `loginUrl`, `loginAriaLabel`, `loginLabel` |
| `B12` | `heroImageUrl`, `headlineHtml`, `subheadlineHtml` |
| `B13` | `categoryIconUrl`, `categoryIconAlt`, `categoryLabel`, `primaryLogoHref`, `primaryLogoUrl`, `primaryLogoAlt`, `primaryOfferHtml`, `primaryBenefitLine`, `primaryCtaUrl`, `primaryCtaLabel`, `secondaryLogoHref`, `secondaryLogoUrl`, `secondaryLogoAlt`, `tertiaryLogoHref`, `tertiaryLogoUrl`, `tertiaryLogoAlt`, `secondaryOfferHtml`, `secondaryCtaUrl`, `secondaryCtaLabel`, `noteHtml`, `paymentDisclaimerHtml` |
| `B14` | `categoryIconUrl`, `categoryIconAlt`, `categoryLabel`, `primaryLogoHref`, `primaryLogoUrl`, `primaryLogoAlt`, `secondaryLogoHref`, `secondaryLogoUrl`, `secondaryLogoAlt`, `tertiaryLogoHref`, `tertiaryLogoUrl`, `tertiaryLogoAlt`, `offerImageHref`, `offerImageUrl`, `offerImageAlt`, `benefitHtml`, `ctaUrl`, `ctaLabel`, `paymentDisclaimerHtml` |
| `B15` | `categoryIconUrl`, `categoryIconAlt`, `categoryLabel`, `primaryLogoHref`, `primaryLogoUrl`, `primaryLogoAlt`, `secondaryLogoHref`, `secondaryLogoUrl`, `secondaryLogoAlt`, `tertiaryLogoHref`, `tertiaryLogoUrl`, `tertiaryLogoAlt`, `quaternaryLogoHref`, `quaternaryLogoUrl`, `quaternaryLogoAlt`, `quinaryLogoHref`, `quinaryLogoUrl`, `quinaryLogoAlt`, `offerImageHref`, `offerImageUrl`, `offerImageAlt`, `benefitHtml`, `ctaUrl`, `ctaLabel`, `paymentDisclaimerHtml` |
| `B17` | `headingHtml`, `step1LinkUrl`, `step1ImageUrl`, `step1ImageAlt`, `step1ImageWidth`, `step1DescriptionHtml`, `step1CtaUrl`, `step1CtaLabel`, `step2LinkUrl`, `step2ImageUrl`, `step2ImageAlt`, `step2ImageWidth`, `step2DescriptionHtml`, `step2CtaUrl`, `step2CtaLabel`, `step3LinkUrl`, `step3ImageUrl`, `step3ImageAlt`, `step3ImageWidth`, `step3DescriptionHtml`, `step3LogoUrl`, `step3LogoAlt`, `step3LogoWidth`, `step3CtaUrl`, `step3CtaLabel`, `disclaimerHtml` |
| `B16` | `closingHtml` |
| `F03` | `taglineDesktopUrl`, `taglineMobileUrl`, `taglineAlt`, `instagramUrl`, `instagramImg`, `instagramAlt`, `facebookUrl`, `facebookImg`, `facebookAlt`, `youtubeUrl`, `youtubeImg`, `youtubeAlt`, `privacyUrl`, `privacyLabel`, `contactUrl`, `contactLabel`, `updateEmailUrl`, `updateEmailLabel`, `unsubscribeUrl`, `unsubscribeLabel`, `cftImageUrl`, `cftImageAlt`, `legalHtml` |
