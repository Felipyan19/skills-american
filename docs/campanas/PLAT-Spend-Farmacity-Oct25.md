# PLAT-Spend-Farmacity-Oct25

Campana exacta de modulo 1 para PP (Cent y Plat). Usa componentes dedicados de `marigold-v4.2` y snippets dinamicos con defaults para reproducir la pieza de Farmacity de octubre 2025.

Status API: `dinamico`. `H07`, `B48`, `B49` y `F08` aceptan variantes por `props`.

## Payloads de uso

### Version corta

```json
{
  "templateFamily": "marigold-v4.2",
  "header": "H07",
  "body": [
    "B48",
    "B49"
  ],
  "footer": "F08"
}
```

### Edicion version corta

```json
{
  "templateFamily": "marigold-v4.2",
  "header": {
    "id": "H07",
    "props": {
      "greetingText": "Hola Farmacity Custom",
      "loginLabel": "Entrar",
      "logoUrl": "https://example.com/farmacity-header-logo.jpg"
    }
  },
  "body": [
    {
      "id": "B48",
      "props": {
        "heroImageUrl": "https://example.com/farmacity-hero.jpg",
        "headlineHtml": "Un plus custom <br><strong style=\"font-family: 'BentonSans400', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;font-size:35px;\">para hoy.</strong>"
      }
    },
    {
      "id": "B49",
      "props": {
        "dateLabel": "TODOS LOS LUNES DE NOVIEMBRE",
        "discountImageUrl": "https://example.com/farmacity-descuento.jpg",
        "farmacityUrl": "https://example.com/farmacity",
        "ctaLabel": "Ver promo",
        "disclaimerHtml": "Disclaimer custom Farmacity."
      }
    }
  ],
  "footer": {
    "id": "F08",
    "props": {
      "taglineDesktopUrl": "https://example.com/farmacity-footer-desktop.jpg",
      "instagramUrl": "https://example.com/instagram",
      "privacyLabel": "Privacidad custom",
      "legalHtml": "LEGAL FARMACITY CUSTOM"
    }
  }
}
```

### Version corta desde tipo de campana y grupo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "PP (Cent y Plat)",
  "campaignType": "spend-farmacity"
}
```

### Edicion corta desde tipo de campana y grupo

```json
{
  "templateFamily": "marigold-v4.2",
  "group": "PP (Cent y Plat)",
  "campaignType": "spend-farmacity",
  "header": {
    "id": "H07",
    "props": {
      "greetingText": "Hola desde group Farmacity",
      "loginLabel": "Ingresar"
    }
  },
  "body": [
    {
      "id": "B49",
      "props": {
        "benefitLine": "en compras online seleccionadas",
        "ctaUrl": "https://example.com/farmacity-group",
        "ctaLabel": "Comprar"
      }
    }
  ],
  "footer": {
    "id": "F08",
    "props": {
      "taglineDesktopUrl": "https://example.com/farmacity-group-footer.jpg",
      "legalHtml": "LEGAL FARMACITY GROUP"
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
    "id": "H07",
    "props": {
      "preheaderLabel": "PUBLICIDAD",
      "viewOnlineUrl": "https://x.email.americanexpress.com/ats/msg.aspx?sg1={(URLSignature1)}",
      "logoHref": "http://www.americanexpress.com.ar",
      "logoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_01.jpg",
      "logoAlt": "American Express",
      "taglineHref": "http://www.americanexpress.com.ar",
      "taglineUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_02.jpg",
      "taglineAlt": "No vivas la vida sin ella",
      "accountLabel": "Tu cuenta termina en:",
      "accountSuffix": "{(LAST_5)}",
      "memberSinceLabel": "Miembro desde:",
      "memberSince": "{(MEMBER_SINCE)}",
      "cardImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_03.png",
      "cardImageAlt": "American Express Card",
      "greetingText": "Hola {(FULLNAME)}",
      "loginUrl": "https://www.americanexpress.com/es-ar/account/login?email_consumer",
      "loginAriaLabel": "American Express account, opens a new tab",
      "loginLabel": "Mi cuenta"
    }
  },
  "body": [
    {
      "id": "B48",
      "props": {
        "heroBgColor": "#00175a",
        "heroImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_04b.jpg",
        "headlineHtml": "Un plus para <br>\n                        tus <strong style=\"font-family: 'BentonSans400', HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;font-size:35px;\">viernes.</strong>"
      }
    },
    {
      "id": "B49",
      "props": {
        "introHtml": "Disfrut&aacute; de este <strong style=\"color:#00175a;\">beneficio exclusivo</strong> con American Express.",
        "dateLabel": "TODOS LOS VIERNES DE OCTUBRE",
        "discountImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_05.jpg",
        "discountImageAlt": "25% OFF",
        "plusImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_06.jpg",
        "plusImageAlt": "+",
        "installmentsImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_07.jpg",
        "installmentsImageAlt": "Hasta 3 cuotas sin inter&eacute;s(1)",
        "benefitLine": "en compra presencial y online",
        "brandImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_08.gif",
        "brandImageAlt": "Farmacity",
        "farmacityUrl": "https://www.farmacity.com/",
        "farmacityLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_09.jpg",
        "farmacityLogoAlt": "Farmacity",
        "getTheLookUrl": "http://www.getthelook.com.ar/",
        "getTheLookLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_10.jpg",
        "getTheLookLogoAlt": "Get the Look | the beauty store",
        "simplicityUrl": "https://www.simplicity.com.ar/",
        "simplicityLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_11.jpg",
        "simplicityLogoAlt": "Simplicity",
        "theFoodMarketUrl": "https://www.thefoodmarket.com.ar/",
        "theFoodMarketLogoUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_12.jpg",
        "theFoodMarketLogoAlt": "The Food Market",
        "closingHtml": "&iexcl;Dale click al logo de tu marca preferida <br class=\"hideMbl\"/> y <strong style=\"font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">compr&aacute; ahora online!</strong>",
        "ctaUrl": "https://www.americanexpress.com/es-ar/beneficios/promociones/promo/especial-del-mes/",
        "ctaAriaLabel": "M&aacute;s info",
        "ctaLabel": "M&aacute;s info",
        "disclaimerHtml": "Tope de reintegro: $12.000 por cuenta, por mes, para The Platinum Card<span style=\"font-size: 6px; vertical-align: 5px;\">&reg;</span><br class=\"mobile-off\"> y en conjunto para la totalidad de las tiendas. Beneficio no v&aacute;lido para compras realizadas a trav&eacute;s <br class=\"mobile-off\"> de plataformas de pago y/o agregadores."
      }
    }
  ],
  "footer": {
    "id": "F08",
    "props": {
      "taglineDesktopUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_13.jpg",
      "taglineMobileUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_14.jpg",
      "taglineAlt": "No vivas la velocidad sin ella(TM)",
      "crossSellTitle": "",
      "cross_sell_items_html": "",
      "instagramUrl": "https://www.instagram.com/americanexpressarg/",
      "instagramImg": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_18.png",
      "instagramAlt": "S&iacute;guenos en Instagram",
      "facebookUrl": "https://www.facebook.com/americanexpressargentina",
      "facebookImg": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_19.png",
      "facebookAlt": "S&iacute;guenos en Facebook",
      "youtubeUrl": "https://www.youtube.com/user/AmericanExpressArg",
      "youtubeImg": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_20.png",
      "youtubeAlt": "S&iacute;guenos en Youtube",
      "privacyUrl": "https://www.americanexpress.com/argentina/legal/privacy_statement.shtml",
      "privacyLabel": "Privacidad",
      "contactUrl": "https://www.americanexpress.com/ar/content/ayuda/contactenos.html",
      "contactLabel": "Contacto",
      "updateEmailUrl": "https://www.americanexpress.com/es-ar/account/login?DestPage=https%3A%2F%2Fglobal.americanexpress.com%2Fmyca%2Fintl%2Facctmaintain%2Fcanlac%2FchangeDetails.do%3Frequest_type%3D%26Face%3Des_AR%26sorted_index%3D0",
      "updateEmailLabel": "Actualizar email",
      "unsubscribeUrl": "https://global.americanexpress.com/privacy/argentina/#/ipp",
      "unsubscribeLabel": "Desuscribirse",
      "cftImageUrl": "https://i.email.americanexpress.com/wpm/1288/Images/1909-PLAT-Spend-Farmacity-Oct25_21.jpg",
      "cftImageAlt": "1) C.F.T.:0,00%",
      "legalHtml": "        1) BENEFICIO V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA &Uacute;NICAMENTE LOS D&Iacute;AS VIERNES DESDE EL 01/10/2025 HASTA EL 31/10/2025 PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES DE AMERICAN EXPRESS, EMITIDAS Y ADMINISTRADAS POR AMERICAN EXPRESS ARGENTINA S.A (LOS &ldquo;SOCIOS&rdquo; Y LAS &ldquo;TARJETAS&rdquo;). LOS SOCIOS ACCEDER&Aacute;N A UN REINTEGRO DEL 25% Y A HASTA 3 CUOTAS SIN INTER&Eacute;S EN SUS COMPRAS EN FARMACITY, GET THE LOOK, SIMPLICITY Y THE FOOD MARKET, ABONANDO LA TOTALIDAD DE LA COMPRA CON LAS TARJETAS. V&Aacute;LIDO PARA COMPRAS ONLINE EN <a href=\"https://www.farmacity.com/\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;word-wrap: break-word;word-break: break-all;\"><strong style=\"text-decoration:none;border:none;outline:0;font-weight: normal;\">WWW.FARMACITY.COM,</strong></a> <a href=\"http://www.getthelook.com.ar/\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;word-wrap: break-word;word-break: break-all;\"><strong style=\"text-decoration:none;border:none;outline:0;font-weight: normal;\">WWW.GETTHELOOK.COM.AR,</strong></a> <a href=\"https://www.simplicity.com.ar/\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;word-wrap: break-word;word-break: break-all;\"><strong style=\"text-decoration:none;border:none;outline:0;font-weight: normal;\">WWW.SIMPLICITY.COM.AR</strong></a> Y <a href=\"https://www.thefoodmarket.com.ar/\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;word-wrap: break-word;word-break: break-all;\"><strong style=\"text-decoration:none;border:none;outline:0;font-weight: normal;\">WWW.THEFOODMARKET.COM.AR,</strong></a> Y PRESENCIALES EN SUCURSALES OFICIALES. BENEFICIO ACUMULABLE CON EL 2X1 DE TODAS LAS MARCAS. NO ACUMULABLE CON EL RESTO DE LAS PROMOCIONES VIGENTES. NO V&Aacute;LIDO PARA COMPRAS REALIZADAS A TRAV&Eacute;S DE PLATAFORMAS DE PAGO Y/O AGREGADORES. EL REINTEGRO DEL 25% DE LA COMPRA SE VER&Aacute; REFLEJADO EN LA CUENTA DEL SOCIO TITULAR DENTRO DE LOS PR&Oacute;XIMOS DOS RES&Uacute;MENES DE REALIZADA LA MISMA. TOPE M&Aacute;XIMO DE REINTEGRO: $12.000 PARA THE PLATINUM CARD&reg; POR MES, POR CUENTA, Y EN CONJUNTO PARA LA TOTALIDAD DE LAS TIENDAS. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES, CONSULTE EN: <a href=\"https://www.americanexpress.com/es-ar/beneficios/promociones/\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;word-wrap: break-word;word-break: break-all;\"><strong style=\"text-decoration:none;border:none;outline:0;font-weight: normal;\">WWW.AMERICANEXPRESS.COM/ES-AR/BENEFICIOS/PROMOCIONES/.</strong></a> TASA NOMINAL ANUAL (T.N.A): 0,00%. TASA EFECTIVA ANUAL (T.E.A): 0,00%. COSTO FINANCIERO TOTAL EXPRESADO EN TASA EFECTIVA ANUAL (C.F.T.): 0,00%. AMERICAN EXPRESS ARGENTINA S.A., ARENALES 707- CABA - CP: 1061, CUIT 30-57481687-0.\n        \n        \n        \n           <br><br>\n        \n            \n            2) V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/01/2025 HASTA EL 31/12/2025, INCLUSIVE. SERVICIO SUJETO A T&Eacute;RMINOS Y CONDICIONES PARA EL USO DEL BUSCADOR DE BENEFICIOS, DISPONIBLES EN <a href=\"https://www.americanexpress.com/ar/empresa/terminos-y-condiciones.html?vanity=www.americanexpress.com.ar%2Fterminosycondiciones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/AR/TERMINOSYCONDICIONES.</strong></a> PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES aplicables CONSULTE EN <a href=\"https://www.americanexpress.com/ar/empresa/terminos-y-condiciones.html?vanity=www.americanexpress.com.ar%2Fterminosycondiciones\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;\">WWW.AMERICANEXPRESS.COM/AR/TERMINOSYCONDICIONES.</strong></a>\n                      AMERICAN EXPRESS ARGENTINA S.A., ARENALES 707- CABA - CP: 1061, CUIT 30-57481687-0.\n                      <br><br>\n\n                    3)  V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/01/2025 HASTA EL 31/12/2025 INCLUSIVE. SUJETO A T&Eacute;RMINOS Y CONDICIONES DEL PROGRAMA MEMBERSHIP REWARDS DISPONIBLES EN <a href=\"https://www.americanexpress.com/es-ar/rewards/membership-rewards\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;\"><strong style=\"border:none;outline:0;text-decoration:none;color:#00175a;font-weight: normal;word-wrap: break-word;word-break: break-all;\">WWW.AMERICANEXPRESS.COM.AR/MR,</strong></a> EN LA OPCI&Oacute;N &ldquo;SOBRE EL PROGRAMA&rdquo;. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES APLICABLES CONSULTE EN <a href=\"https://www.americanexpress.com/es-ar/rewards/membership-rewards\" target=\"_blank\" style=\"border:none;outline:0;text-decoration:none;color:#00175a;\"><strong style=\"border:none;outline:0;text-decoration:none;color:#00175a;font-weight: normal;word-wrap: break-word;word-break: break-all;\">WWW.AMERICANEXPRESS.COM.AR/MR.</strong></a> AMERICAN EXPRESS ARGENTINA S.A., ARENALES 707- CABA - CP: 1061, CUIT 30-57481687-0. <br><br>\n\n                    4) V&Aacute;LIDO EN LA REP&Uacute;BLICA ARGENTINA DESDE EL 01/01/2025 HASTA EL 31/12/2025, INCLUSIVE. AMEX APP ES UNA aplicaci&oacute;n DE AMERICAN EXPRESS ARGENTINA S.A. DISPONIBLE PARA LOS SOCIOS TITULARES Y ADICIONALES DE LAS TARJETAS PERSONALES Y CORPORATIVAS EMITIDAS Y ADMINISTRADAS POR AMERICAN EXPRESS ARGENTINA S.A.. AMEX APP EST&Aacute; DISPONIBLE PARA SU DESCARGA EN DISPOSITIVOS ANDROID e IOS. PARA M&Aacute;S INFORMACI&Oacute;N Y CONDICIONES O LIMITACIONES aplicables CONSULTE EN <a href=\"https://www.americanexpress.com/es-ar/servicios/amexapp/index.html\" target=\"_blank\" style=\"color: #00175a; text-decoration: none;border:none;outline:0;\"><strong style=\"font-weight:normal;color: #00175a; text-decoration: none;border:none;outline:0;word-wrap: break-word;word-break: break-all;font-family: HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif\">WWW.AMERICANEXPRESS.COM/AR/AMEXAPP.</strong></a>  AMERICAN EXPRESS ARGENTINA S.A., ARENALES 707- CABA - CP: 1061, CUIT 30-57481687-0.\n\n        \n          <br><br>\n          \n            Los datos personales son almacenados en una base de datos, cuyo responsable es American Express Argentina S.A. con domicilio legal en Arenales 707, entrepiso, CP C1061AAA, C.A.B.A. Usted podr&aacute; -en cualquier momento- solicitar el retiro o bloqueo de su nombre, total o parcial, de nuestra base de datos y podr&aacute; solicitar informaci&oacute;n acerca del nombre del responsable o usuario de la base de datos que provey&oacute; su informaci&oacute;n. Ley 25.326 art.27. - inc. 3. &ldquo;El titular podr&aacute; en cualquier momento solicitar el retiro o bloqueo de su nombre de los bancos de datos a los que se refiere el presente art&iacute;culo&rdquo;. Decreto 1558/01 - art. 27. - 3er. P&aacute;rrafo. &ldquo;En toda comunicaci&oacute;n con fines de publicidad que se realice por correo, tel&eacute;fono, correo electr&oacute;nico, internet u otro medio a distancia a conocer, se deber&aacute; indicar, en forma expresa y destacada, la posibilidad del titular del dato de solicitar el retiro o bloqueo, total o parcial, de su nombre de la base de datos. A pedido del interesado, se deber&aacute; informar el nombre del responsable o usuario del banco de datos que provey&oacute; la informaci&oacute;n&rdquo;.\n\n            <br/><br/>\n\n            Instrucciones para cancelar la suscripci&oacute;n: este correo electr&oacute;nico publicitario est&aacute; destinado a residentes de Argentina y fue enviado a <strong style=\"color:#000000;font-weight:normal;word-wrap: break-word;word-break: break-all;\">{(EMAIL)}</strong>. Si ha sido recibido en una direcci&oacute;n diferente, significa que fue reenviado. Si no desea recibir nuevos mensajes publicitarios en el futuro, por favor responda este e-mail con la palabra &ldquo;borrar&rdquo; en el asunto (subject), o visite las <a href=\"https://global.americanexpress.com/privacy/argentina/#/ipp\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">preferencias de correo electr&oacute;nico</a> en el sitio web de American Express. Servicio al cliente: por favor no responda (reply) este e-mail y dirija todas sus consultas a <a href=\"https://www.americanexpress.com/ar/content/ayuda/contactenos.html\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">Servicio al Cliente</a>. Declaraci&oacute;n sobre privacidad: para saber c&oacute;mo obtenemos, aseguramos y utilizamos su informaci&oacute;n personal cumpliendo con la ley 25.326, visite la declaraci&oacute;n sobre privacidad de American Express ingresando en: <a href=\"http://www.americanexpress.com/argentina/legal/privacy_statement.shtml\" target=\"_blank\" style=\"color: #00175A; text-decoration: none;\">www.americanexpress.com.ar/privacidad</a>.\n\n\n            <br><br> &copy; 2025 American Express Company.\n"
    }
  }
}
```

## Contrato de edicion

Los componentes aceptan variantes por `props`. El renderer mezcla `defaults + props`, asi que podés enviar solo el campo que quieras modificar y el resto queda igual al template exacto.

## Mapa de componentes

| Slot | API ID | Snippets |
|---|---|---|
| Header | `H07` | `ph01.html`, `brand-panel-plat-spend-farmacity-oct25.html` |
| Body | `B48` | `hb18-plat-spend-farmacity-oct25.html` |
| Body | `B49` | `tm04-plat-spend-farmacity-oct25.html` |
| Footer | `F08` | `fm05-plat-spend-farmacity-oct25.html`, `fm01.html`, `tm06.html`, `fm02-plat-spend-farmacity-oct25.html`, `fm03-plat-spend-farmacity-oct25.html`, `fm04-plat-spend-farmacity-oct25.html` |

## Campos de variantes

| Componente | Props soportadas |
|---|---|
| `H07` | `preheaderLabel, viewOnlineUrl, logoHref, logoUrl, logoAlt, taglineHref, taglineUrl, taglineAlt, accountLabel, accountSuffix, memberSinceLabel, memberSince, cardImageUrl, cardImageAlt, greetingText, loginUrl, loginAriaLabel, loginLabel` |
| `B48` | `heroBgColor, heroImageUrl, headlineHtml` |
| `B49` | `introHtml, dateLabel, discountImageUrl, discountImageAlt, plusImageUrl, plusImageAlt, installmentsImageUrl, installmentsImageAlt, benefitLine, brandImageUrl, brandImageAlt, farmacityUrl, farmacityLogoUrl, farmacityLogoAlt, getTheLookUrl, getTheLookLogoUrl, getTheLookLogoAlt, simplicityUrl, simplicityLogoUrl, simplicityLogoAlt, theFoodMarketUrl, theFoodMarketLogoUrl, theFoodMarketLogoAlt, closingHtml, ctaUrl, ctaAriaLabel, ctaLabel, disclaimerHtml` |
| `F08` | `taglineDesktopUrl, taglineMobileUrl, taglineAlt, crossSellTitle, cross_sell_items_html, instagramUrl, instagramImg, instagramAlt, facebookUrl, facebookImg, facebookAlt, youtubeUrl, youtubeImg, youtubeAlt, privacyUrl, privacyLabel, contactUrl, contactLabel, updateEmailUrl, updateEmailLabel, unsubscribeUrl, unsubscribeLabel, cftImageUrl, cftImageAlt, legalHtml` |
