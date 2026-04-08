from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from server.composer import compose_email, list_components
from server.errors import NotFoundError, ValidationError


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "tests" / "snapshots"


def _core_source_ids(result: dict) -> list[str]:
    return [
        item["sourceId"]
        for item in result["manifest"]["expanded"]
        if item["sourceId"] != "SEPARATOR"
    ]


def _load_snapshot(name: str) -> list[str]:
    return json.loads((SNAPSHOT_DIR / name).read_text(encoding="utf-8"))


def _extract_reference_ids(html_text: str) -> list[str]:
    ids: list[str] = []
    patterns = [
        (re.compile(r"START:\s+(?:ID=|TD=)?([A-Z]{2,4}\d{2}(?:-v\d\.\d)?)"), None),
        (re.compile(r"START:\s+Consumer Default-v4\.2"), "Consumer Default-v4.2"),
        (re.compile(r"START:\s+BP01 Master - Centurion"), "BP01"),
        (re.compile(r"START:\s+Hero banner area CHB01"), "CHB01"),
        (re.compile(r"START:\s+FM05_business Footer Tagline-v4\.0"), "FM05"),
    ]
    for line in html_text.splitlines():
        for pattern, fixed in patterns:
            match = pattern.search(line)
            if not match:
                continue
            ids.append(fixed or match.group(1))
            break
    return ids


def _is_subsequence(sequence: list[str], source: list[str]) -> bool:
    position = 0
    for item in source:
        if position < len(sequence) and sequence[position] == item:
            position += 1
    return position == len(sequence)


class ComposerTests(unittest.TestCase):
    def test_list_components_returns_public_catalog(self) -> None:
        result = list_components("marigold-v4.2")
        catalog = {item["id"]: item for item in result["components"]}
        self.assertEqual(result["templateFamily"], "marigold-v4.2")
        self.assertIn("H01", catalog)
        self.assertIn("B03", catalog)
        self.assertIn("B11", catalog)
        self.assertIn("F02", catalog)
        self.assertEqual(catalog["H01"]["slot"], "header")
        self.assertIn("sourceIds", catalog["B03"])

    def test_minimal_payload_uses_defaults(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": "H01",
            "body": ["B03"],
            "footer": "F01",
        }
        result = compose_email(payload)
        self.assertEqual(result["templateFamily"], "marigold-v4.2")
        self.assertIn("Hero principal", result["html"])
        self.assertIn("Legales pendientes de definir", result["html"])
        self.assertEqual(_core_source_ids(result), ["PH01-v4.2", "Consumer Default-v4.2", "HB15-v4.2", "FM05-v4.2", "FM02", "FM03-v4.2", "FM04-v4.2"])

    def test_compose_marigold_mr_matches_snapshot_order(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {
                "id": "H01",
                "props": {
                    "logoUrl": "https://example.com/logo.png",
                    "secondaryLogoUrl": "https://example.com/mr.png",
                    "secondaryLogoAlt": "Membership Rewards",
                    "secondaryLogoHref": "https://example.com/mr",
                    "accountSuffix": "{(LAST_5)}",
                    "greetingName": "{(FULLNAME)}",
                },
            },
            "body": [
                {
                    "id": "B03",
                    "props": {
                        "imageDesktopUrl": "https://example.com/hero.jpg",
                        "imageMobileUrl": "https://example.com/hero-m.jpg",
                        "headline": "Transformá puntos",
                        "description": "Canjeá productos seleccionados.",
                        "ctaUrl": "https://example.com/hero",
                    },
                },
                {
                    "id": "B07",
                    "props": {
                        "items": [
                            {
                                "title": "Oferta 1",
                                "description": "Desc 1",
                                "badge": "40% OFF",
                                "imageUrl": "https://example.com/1.jpg",
                                "ctaUrl": "https://example.com/1",
                            },
                            {
                                "title": "Oferta 2",
                                "description": "Desc 2",
                                "badge": "35% OFF",
                                "imageUrl": "https://example.com/2.jpg",
                                "ctaUrl": "https://example.com/2",
                            },
                        ]
                    },
                },
                {
                    "id": "B07",
                    "props": {
                        "items": [
                            {
                                "title": "Oferta 3",
                                "description": "Desc 3",
                                "badge": "25% OFF",
                                "imageUrl": "https://example.com/3.jpg",
                                "ctaUrl": "https://example.com/3",
                            },
                            {
                                "title": "Oferta 4",
                                "description": "Desc 4",
                                "badge": "20% OFF",
                                "imageUrl": "https://example.com/4.jpg",
                                "ctaUrl": "https://example.com/4",
                            },
                        ]
                    },
                },
                {
                    "id": "B07",
                    "props": {
                        "items": [
                            {
                                "title": "Oferta 5",
                                "description": "Desc 5",
                                "badge": "15% OFF",
                                "imageUrl": "https://example.com/5.jpg",
                                "ctaUrl": "https://example.com/5",
                            },
                            {
                                "title": "Oferta 6",
                                "description": "Desc 6",
                                "badge": "10% OFF",
                                "imageUrl": "https://example.com/6.jpg",
                                "ctaUrl": "https://example.com/6",
                            },
                        ]
                    },
                },
                {
                    "id": "B09",
                    "props": {
                        "headline": "Consejos",
                        "offerCode": "40% OFF",
                        "description": "Válido por tiempo limitado.",
                    },
                },
            ],
            "footer": {
                "id": "F02",
                "props": {
                    "taglineDesktopUrl": "https://example.com/tagline.jpg",
                    "taglineMobileUrl": "https://example.com/tagline-m.jpg",
                    "legalHtml": "<p>Legal MR</p>",
                    "crossSellItems": [
                        {"title": "Viajes", "subtitle": "Descubrí beneficios", "iconUrl": "https://example.com/i1.png"},
                        {"title": "Dining", "subtitle": "Reservas exclusivas", "iconUrl": "https://example.com/i2.png"},
                    ],
                },
            },
            "globals": {"subject": "AMEX"},
        }
        result = compose_email(payload)
        self.assertEqual(_core_source_ids(result), _load_snapshot("mr_marigold_v42_order.json"))
        self.assertIn("<!-- START: EMAIL HEADER CONTAINER -->", result["html"])
        self.assertIn("<!-- START: EMAIL CONTENT CONTAINER -->", result["html"])

    def test_compose_corp_matches_snapshot_order(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {
                "id": "H01",
                "props": {
                    "logoUrl": "https://example.com/logo.png",
                    "taglineUrl": "https://example.com/tagline.png",
                    "taglineAlt": "No hagas negocios sin ella",
                    "accountSuffix": "",
                    "showGreeting": False,
                    "showLogin": False,
                    "showMemberSince": False,
                },
            },
            "body": [
                {
                    "id": "B06",
                    "props": {
                        "imageUrl": "https://example.com/corp.jpg",
                        "headlineTop": "Seguinos",
                        "headlineAccent": "en Instagram",
                        "description": "Descubrí novedades de la tarjeta.",
                    },
                },
                {
                    "id": "B10",
                    "props": {
                        "headline": "Beneficios destacados",
                        "buttonUrl": "https://example.com/instagram",
                        "cards": [
                            {"title": "Comercios", "subtitle": "Beneficios exclusivos", "iconUrl": "https://example.com/c1.png"},
                            {"title": "Supermercados", "subtitle": "Ahorros en compras", "iconUrl": "https://example.com/c2.png"},
                        ],
                    },
                },
                {
                    "id": "B09",
                    "props": {
                        "headline": "Consejos de seguridad",
                        "offerCode": "Instagram",
                        "description": "Nuestras cuentas oficiales tienen tilde azul.",
                    },
                },
            ],
            "footer": {
                "id": "F01",
                "props": {
                    "taglineDesktopUrl": "https://example.com/tagline.jpg",
                    "taglineMobileUrl": "https://example.com/tagline-m.jpg",
                    "legalHtml": "<p>Legal CORP</p>",
                },
            },
        }
        result = compose_email(payload)
        self.assertEqual(_core_source_ids(result), _load_snapshot("corp_marigold_v42_order.json"))

    def test_compose_merchant_matches_snapshot_order(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": "H01",
            "body": ["B05", "B09", "B09", "B09", "B11", "B09"],
            "footer": "F01",
        }
        result = compose_email(payload)
        self.assertEqual(_core_source_ids(result), _load_snapshot("merchant_marigold_v42_order.json"))

    def test_compose_merchant_exact_payload_uses_reference_assets(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": "H02",
            "body": [
                "B12",
                "B13",
                "B14",
                "B15",
                "B17",
                "B16",
            ],
            "footer": "F03",
            "globals": {"includeSeparators": False},
        }
        result = compose_email(payload)
        self.assertIn("Eleg&iacute; el destino", result["html"])
        self.assertIn("Aerol&iacute;neas Argentinas", result["html"])
        self.assertIn("1908-MERCHANT-Shot-Travel-Agst25_21.png", result["html"])
        self.assertIn("AMERICAN EXPRESS ARGENTINA S.A.", result["html"])
        self.assertNotIn("dummyimage.com", result["html"])
        self.assertNotIn("Legales pendientes de definir", result["html"])
        self.assertNotIn("Separator", result["html"])

    def test_compose_centurion_matches_snapshot_order(self) -> None:
        payload = {
            "templateFamily": "centurion-1.0",
            "header": {
                "id": "H01",
                "props": {
                    "logoUrl": "https://example.com/logo-white.png",
                    "taglineUrl": "https://example.com/tagline.png",
                    "cardImageUrl": "https://example.com/card.png",
                    "accountSuffix": "{(LAST_5)}",
                    "greetingName": "{(FULLNAME)}",
                },
            },
            "body": [
                {
                    "id": "B01",
                    "props": {
                        "imageUrl": "https://example.com/hero.jpg",
                        "headline": "México exclusivo",
                        "description": "Itinerarios curados para socios Centurion.",
                        "ctaUrl": "https://example.com/mexico",
                    },
                },
                {
                    "id": "B02",
                    "props": {
                        "headline": "Fine Hotels + Resorts",
                        "description": "Reservas con upgrades y experiencias únicas.",
                    },
                },
                {
                    "id": "B03",
                    "props": {
                        "items": [
                            {
                                "title": "Conrad Tulum",
                                "description": "Tercera noche bonificada.",
                                "imageUrl": "https://example.com/conrad.jpg",
                                "ctaUrl": "https://example.com/conrad",
                            },
                            {
                                "title": "Alexander México",
                                "description": "Beneficios exclusivos por reserva.",
                                "imageUrl": "https://example.com/alexander.jpg",
                                "ctaUrl": "https://example.com/alexander",
                            },
                        ]
                    },
                },
            ],
            "footer": {
                "id": "F01",
                "props": {
                    "legalHtml": "<p>Legal Centurion</p>",
                    "crossSellItems": [
                        {"title": "Dining", "subtitle": "Experiencias selectas", "iconUrl": "https://example.com/c1.png"},
                        {"title": "Travel", "subtitle": "Asesor dedicado", "iconUrl": "https://example.com/c2.png"},
                    ],
                },
            },
        }
        result = compose_email(payload)
        self.assertEqual(_core_source_ids(result), _load_snapshot("centurion_order.json"))

    def test_body_preserves_order_and_repetition(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {"id": "H01", "props": {"logoUrl": "https://example.com/logo.png", "accountSuffix": "12345", "greetingName": "Name"}},
            "body": [
                {"id": "B08", "props": {"headline": "Uno", "description": "Desc", "ctaUrl": "https://example.com/1"}},
                {"id": "B08", "props": {"headline": "Dos", "description": "Desc", "ctaUrl": "https://example.com/2"}},
                {"id": "B09", "props": {"headline": "Tres", "offerCode": "ABC", "description": "Desc"}},
            ],
            "footer": {"id": "F01", "props": {"taglineDesktopUrl": "https://example.com/tag.jpg", "taglineMobileUrl": "https://example.com/tag-m.jpg", "legalHtml": "<p>Legal</p>"}},
        }
        result = compose_email(payload)
        ordered = [item["sourceId"] for item in result["manifest"]["expanded"] if item["kind"] == "snippet"]
        self.assertEqual(ordered[2:5], ["TM01-v4.2", "TM01-v4.2", "TM04-v4.2"])

    def test_merchant_shot_deporte_accepts_component_variants(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {
                "id": "H04",
                "props": {
                    "logoUrl": "https://example.com/header-logo.jpg",
                    "taglineUrl": "https://example.com/header-tagline.jpg",
                    "greetingText": "Hola Tester",
                    "loginLabel": "Entrar",
                },
            },
            "body": [
                {
                    "id": "B28",
                    "props": {
                        "heroBgColor": "#4b1231",
                        "headlineAccentColor": "#e7b7c8",
                        "headlineBoxBgColor": "#2b0b1c",
                        "heroImageUrl": "https://example.com/deporte-hero.jpg",
                        "headlineHtml": "<strong>Nuevo headline</strong><br>para deporte",
                        "headlineTextColor": "#fff4f8",
                    },
                },
                "B29",
                {
                    "id": "B30",
                    "props": {
                        "dateLabel": "Del 2 al 9 de enero",
                        "primaryLogoUrl": "https://example.com/club-a.jpg",
                        "ctaUrl": "https://example.com/clubes",
                    },
                },
                {
                    "id": "B31",
                    "props": {
                        "leftBenefitLine": "en compras online",
                        "leftLogoUrl": "https://example.com/decathlon-alt.jpg",
                        "rightOfferImageUrl": "https://example.com/padel-offer.png",
                        "rightCtaLabel": "Ver beneficio",
                    },
                },
                {"id": "B32", "props": {"disclaimerHtml": "DISCLAIMER FINAL CUSTOM"}},
            ],
            "footer": {
                "id": "F05",
                "props": {
                    "taglineDesktopUrl": "https://example.com/footer-tagline-desktop.jpg",
                    "taglineMobileUrl": "https://example.com/footer-tagline-mobile.jpg",
                    "instagramImg": "https://example.com/instagram.png",
                    "privacyLabel": "Privacidad custom",
                    "legalHtml": "<strong>LEGAL CUSTOM FOOTER</strong>",
                },
            },
            "globals": {"includeSeparators": False},
        }
        result = compose_email(payload)
        self.assertIn("https://example.com/header-logo.jpg", result["html"])
        self.assertIn("https://example.com/header-tagline.jpg", result["html"])
        self.assertIn("Hola Tester", result["html"])
        self.assertIn(">Entrar</a>", result["html"])
        self.assertIn("https://example.com/deporte-hero.jpg", result["html"])
        self.assertIn("#4b1231", result["html"])
        self.assertIn("#e7b7c8", result["html"])
        self.assertIn("#2b0b1c", result["html"])
        self.assertIn("#fff4f8", result["html"])
        self.assertIn("<strong>Nuevo headline</strong><br>para deporte", result["html"])
        self.assertIn("Del 2 al 9 de enero", result["html"])
        self.assertIn("https://example.com/club-a.jpg", result["html"])
        self.assertIn("https://example.com/clubes", result["html"])
        self.assertIn("en compras online", result["html"])
        self.assertIn("https://example.com/decathlon-alt.jpg", result["html"])
        self.assertIn("https://example.com/padel-offer.png", result["html"])
        self.assertIn("Ver beneficio", result["html"])
        self.assertIn("DISCLAIMER FINAL CUSTOM", result["html"])
        self.assertIn("https://example.com/footer-tagline-desktop.jpg", result["html"])
        self.assertIn("https://example.com/footer-tagline-mobile.jpg", result["html"])
        self.assertIn("https://example.com/instagram.png", result["html"])
        self.assertIn("Privacidad custom", result["html"])
        self.assertIn("<strong>LEGAL CUSTOM FOOTER</strong>", result["html"])
        self.assertNotIn("{{", result["html"])

    def test_merchant_shot_travel_accepts_component_variants(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {
                "id": "H02",
                "props": {
                    "logoUrl": "https://example.com/travel-header-logo.jpg",
                    "greetingText": "Hola Travel",
                    "loginLabel": "Ingresar",
                },
            },
            "body": [
                {
                    "id": "B12",
                    "props": {
                        "heroImageUrl": "https://example.com/travel-hero.jpg",
                        "headlineHtml": "Eleg&iacute; otro destino",
                    },
                },
                {
                    "id": "B13",
                    "props": {
                        "primaryLogoUrl": "https://example.com/aerolineas-alt.png",
                        "primaryBenefitLine": "en vuelos regionales",
                        "secondaryCtaLabel": "Ver agencias",
                    },
                },
                {
                    "id": "B14",
                    "props": {
                        "offerImageUrl": "https://example.com/compras-offer.png",
                        "benefitHtml": "20% OFF custom",
                        "ctaLabel": "Comprar",
                    },
                },
                {
                    "id": "B15",
                    "props": {
                        "primaryLogoUrl": "https://example.com/spa-a.png",
                        "offerImageAlt": "15% OFF custom spa",
                        "ctaUrl": "https://example.com/spa",
                    },
                },
                {
                    "id": "B17",
                    "props": {
                        "headingHtml": "Hoteles custom",
                        "step3LogoUrl": "https://example.com/hotel-logo.png",
                        "disclaimerHtml": "Disclaimer hoteles custom",
                    },
                },
                {"id": "B16", "props": {"closingHtml": "Cierre travel custom"}},
            ],
            "footer": {
                "id": "F03",
                "props": {
                    "taglineDesktopUrl": "https://example.com/travel-footer.jpg",
                    "instagramUrl": "https://example.com/instagram",
                    "privacyLabel": "Privacidad Travel",
                    "legalHtml": "LEGAL TRAVEL CUSTOM",
                },
            },
            "globals": {"includeSeparators": False},
        }
        result = compose_email(payload)
        self.assertIn("https://example.com/travel-header-logo.jpg", result["html"])
        self.assertIn("Hola Travel", result["html"])
        self.assertIn(">Ingresar</a>", result["html"])
        self.assertIn("https://example.com/travel-hero.jpg", result["html"])
        self.assertIn("Eleg&iacute; otro destino", result["html"])
        self.assertIn("https://example.com/aerolineas-alt.png", result["html"])
        self.assertIn("en vuelos regionales", result["html"])
        self.assertIn("Ver agencias", result["html"])
        self.assertIn("https://example.com/compras-offer.png", result["html"])
        self.assertIn("20% OFF custom", result["html"])
        self.assertIn(">Comprar</strong>", result["html"])
        self.assertIn("https://example.com/spa-a.png", result["html"])
        self.assertIn("15% OFF custom spa", result["html"])
        self.assertIn("https://example.com/spa", result["html"])
        self.assertIn("Hoteles custom", result["html"])
        self.assertIn("https://example.com/hotel-logo.png", result["html"])
        self.assertIn("Disclaimer hoteles custom", result["html"])
        self.assertIn("Cierre travel custom", result["html"])
        self.assertIn("https://example.com/travel-footer.jpg", result["html"])
        self.assertIn("https://example.com/instagram", result["html"])
        self.assertIn("Privacidad Travel", result["html"])
        self.assertIn("LEGAL TRAVEL CUSTOM", result["html"])
        self.assertNotIn("{{", result["html"])

    def test_plat_spend_farmacity_accepts_component_variants(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {
                "id": "H07",
                "props": {
                    "greetingText": "Hola Farmacity Custom",
                    "loginLabel": "Entrar",
                    "logoUrl": "https://example.com/farmacity-header-logo.jpg",
                },
            },
            "body": [
                {
                    "id": "B48",
                    "props": {
                        "heroImageUrl": "https://example.com/farmacity-hero.jpg",
                        "headlineHtml": "Un plus custom",
                    },
                },
                {
                    "id": "B49",
                    "props": {
                        "dateLabel": "TODOS LOS LUNES DE NOVIEMBRE",
                        "discountImageUrl": "https://example.com/farmacity-descuento.jpg",
                        "farmacityUrl": "https://example.com/farmacity",
                        "ctaLabel": "Ver promo",
                        "disclaimerHtml": "Disclaimer custom Farmacity.",
                    },
                },
            ],
            "footer": {
                "id": "F08",
                "props": {
                    "taglineDesktopUrl": "https://example.com/farmacity-footer-desktop.jpg",
                    "instagramUrl": "https://example.com/instagram",
                    "privacyLabel": "Privacidad custom",
                    "legalHtml": "LEGAL FARMACITY CUSTOM",
                },
            },
        }
        result = compose_email(payload)
        self.assertIn("Hola Farmacity Custom", result["html"])
        self.assertIn(">Entrar</a>", result["html"])
        self.assertIn("https://example.com/farmacity-header-logo.jpg", result["html"])
        self.assertIn("https://example.com/farmacity-hero.jpg", result["html"])
        self.assertIn("Un plus custom", result["html"])
        self.assertIn("TODOS LOS LUNES DE NOVIEMBRE", result["html"])
        self.assertIn("https://example.com/farmacity-descuento.jpg", result["html"])
        self.assertIn("https://example.com/farmacity", result["html"])
        self.assertIn(">Ver promo</a>", result["html"])
        self.assertIn("Disclaimer custom Farmacity.", result["html"])
        self.assertIn("https://example.com/farmacity-footer-desktop.jpg", result["html"])
        self.assertIn("https://example.com/instagram", result["html"])
        self.assertIn("Privacidad custom", result["html"])
        self.assertIn("LEGAL FARMACITY CUSTOM", result["html"])
        self.assertNotIn("{{", result["html"])

    def test_footer_uses_defaults_when_props_are_missing(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {"id": "H01", "props": {"logoUrl": "https://example.com/logo.png", "accountSuffix": "12345"}},
            "body": [],
            "footer": "F01",
        }
        result = compose_email(payload)
        self.assertIn("Legales pendientes de definir", result["html"])

    def test_rejects_unknown_component(self) -> None:
        payload = {
            "templateFamily": "marigold-v4.2",
            "header": {"id": "H01", "props": {"logoUrl": "https://example.com/logo.png", "accountSuffix": "12345"}},
            "body": ["B99"],
            "footer": {"id": "F01", "props": {"taglineDesktopUrl": "https://example.com/tag.jpg", "taglineMobileUrl": "https://example.com/tag-m.jpg", "legalHtml": "<p>Legal</p>"}},
        }
        with self.assertRaises(NotFoundError):
            compose_email(payload)

    def test_golden_reference_subsequence_when_local_html_exists(self) -> None:
        reference_specs = [
            (
                ROOT / "1. Referencias por segmento" / "MR" / "MR-Tecnologia-Dic25" / "MR-Tecnologia-Dic25.html",
                _load_snapshot("mr_marigold_v42_order.json"),
            ),
            (
                ROOT / "1. Referencias por segmento" / "CORP y MERCHANT Comercio" / "CORP-IG-Sep25" / "CORP-IG-Sep25.html",
                _load_snapshot("corp_marigold_v42_order.json"),
            ),
            (
                ROOT / "1. Referencias por segmento" / "MERCHANT - Socio" / "MERCHANT-Shot-Travel-Agst25" / "MERCHANT-Shot-Travel-Agst25.html",
                _load_snapshot("merchant_marigold_v42_order.json"),
            ),
            (
                ROOT / "1. Referencias por segmento" / "TRAVEL (Cent y Plat)" / "TRAVEL-Mexico-Sept25-CENT" / "TRAVEL-Mexico-Sept25-CENT.html",
                [item for item in _load_snapshot("centurion_order.json") if item != "CFM01"],
            ),
        ]
        for path, expected in reference_specs:
            if not path.exists():
                continue
            extracted = _extract_reference_ids(path.read_text(encoding="utf-8", errors="ignore"))
            self.assertTrue(_is_subsequence(expected, extracted), msg=f"{path} did not contain expected subsequence.")
