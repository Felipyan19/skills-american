from __future__ import annotations

import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from server.http_server import serve


class HttpApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = serve(port=0)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        host, port = self.server.server_address
        self.base_url = f"http://{host}:{port}"

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def test_get_components_returns_catalog(self) -> None:
        with urlopen(f"{self.base_url}/api/components?templateFamily=marigold-v4.2") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["templateFamily"], "marigold-v4.2")
        ids = {item["id"] for item in payload["components"]}
        self.assertIn("H01", ids)
        self.assertIn("F02", ids)

    def test_get_module1_examples_returns_catalog(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["count"], 33)
        dashboard_total = (
            payload["summary"]["dynamic"]
            + payload["summary"]["exactDashboard"]
            + payload["summary"]["pending"]
        )
        fidelity_total = (
            payload["summary"]["exact"]
            + payload["summary"]["structural"]
            + payload["summary"]["approximate"]
        )
        self.assertEqual(dashboard_total, payload["count"])
        self.assertEqual(fidelity_total, payload["count"])
        self.assertEqual(payload["examples"][0]["name"], "PP-LOC-GOLD-Febrero25")
        self.assertEqual(payload["examples"][0]["id"], "pp-loc-gold-febrero25")
        self.assertIn(payload["examples"][0]["dashboardStatus"], {"dinamico", "exacto", "pendiente"})

    def test_get_module1_page_returns_html(self) -> None:
        with urlopen(f"{self.base_url}/module1") as response:
            payload = response.read().decode("utf-8")
            content_type = response.headers.get_content_type()
        self.assertEqual(content_type, "text/html")
        self.assertIn("Componentes HTML", payload)
        self.assertIn("Ir al contenido", payload)
        self.assertIn("HTML del registro", payload)

    def test_get_single_example_returns_example(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples/pp-loc-gold-febrero25") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["example"]["id"], "pp-loc-gold-febrero25")
        self.assertEqual(payload["example"]["name"], "PP-LOC-GOLD-Febrero25")
        self.assertIn(payload["example"]["dashboardStatus"], {"dinamico", "exacto", "pendiente"})

    def test_get_single_example_html_returns_rendered_html(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples/pp-loc-gold-febrero25/html") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["exampleId"], "pp-loc-gold-febrero25")
        self.assertIn(payload["source"], {"generated", "reference"})
        self.assertIn("<!DOCTYPE html>", payload["html"])

    def test_get_example_page_returns_html(self) -> None:
        with urlopen(f"{self.base_url}/example/pp-loc-gold-febrero25") as response:
            payload = response.read().decode("utf-8")
            content_type = response.headers.get_content_type()
        self.assertEqual(content_type, "text/html")
        self.assertIn("American Express", payload)
        self.assertIn("Markdown del componente", payload)
        self.assertNotIn("Ver payload", payload)

    def test_get_single_example_markdown_returns_markdown(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples/pp-loc-gold-febrero25/markdown") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["exampleId"], "pp-loc-gold-febrero25")
        self.assertIn(payload["dashboardStatus"], {"dinamico", "exacto", "pendiente"})
        self.assertEqual(payload["markdownSource"], "generated")
        self.assertEqual(payload["markdownDoc"], "")
        self.assertIn("### PP-LOC-GOLD-Febrero25", payload["markdown"])
        self.assertIn("```json", payload["markdown"])

    def test_get_dynamic_campaign_marks_dashboard_status(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples/merchant-shot-deporte-dic25") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["example"]["dashboardStatus"], "dinamico")
        self.assertEqual(payload["example"]["campaignDoc"], "MERCHANT-Shot-deporte-DIC25.md")

    def test_get_dynamic_campaign_markdown_uses_campaign_doc(self) -> None:
        with urlopen(f"{self.base_url}/api/module1/examples/merchant-shot-deporte-dic25/markdown") as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertEqual(payload["markdownSource"], "campaign-doc")
        self.assertEqual(payload["markdownDoc"], "MERCHANT-Shot-deporte-DIC25.md")
        self.assertIn("# MERCHANT-Shot-deporte-DIC25", payload["markdown"])

    def test_post_compose_email_returns_html_and_manifest(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "header": {"id": "H01", "props": {"logoUrl": "https://example.com/logo.png", "accountSuffix": "12345", "greetingName": "Name"}},
            "body": [{"id": "B09", "props": {"headline": "Titulo", "offerCode": "ABC", "description": "Desc"}}],
            "footer": {"id": "F01", "props": {"taglineDesktopUrl": "https://example.com/tag.jpg", "taglineMobileUrl": "https://example.com/tag-m.jpg", "legalHtml": "<p>Legal</p>"}},
        }
        request = Request(
            f"{self.base_url}/api/compose-email",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertIn("<!DOCTYPE html>", payload["html"])
        self.assertEqual(payload["manifest"]["requested"]["body"], ["B09"])

    def test_post_compose_email_merges_module1_component_variants(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "group": "MERCHANT - Socio",
            "campaignType": "shot-deporte",
            "header": {
                "id": "H04",
                "props": {
                    "greetingText": "Hola desde group",
                    "loginLabel": "Acceder",
                },
            },
            "body": [
                {
                    "id": "B28",
                    "props": {
                        "headlineHtml": "Headline desde group",
                        "heroImageUrl": "https://example.com/group-hero.jpg",
                    },
                }
            ],
            "footer": {
                "id": "F05",
                "props": {
                    "taglineDesktopUrl": "https://example.com/group-footer.jpg",
                    "legalHtml": "LEGAL GROUP CUSTOM",
                },
            },
        }
        request = Request(
            f"{self.base_url}/api/compose-email",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertIn("Hola desde group", payload["html"])
        self.assertIn(">Acceder</a>", payload["html"])
        self.assertIn("Headline desde group", payload["html"])
        self.assertIn("https://example.com/group-hero.jpg", payload["html"])
        self.assertIn("https://example.com/group-footer.jpg", payload["html"])
        self.assertIn("LEGAL GROUP CUSTOM", payload["html"])
        self.assertEqual(payload["manifest"]["requested"]["body"], ["B28", "B29", "B30", "B31", "B32"])

    def test_post_compose_email_merges_travel_component_variants(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "group": "MERCHANT - Socio",
            "campaignType": "shot-travel",
            "header": {
                "id": "H02",
                "props": {
                    "greetingText": "Hola Travel group",
                    "loginLabel": "Entrar",
                },
            },
            "body": [
                {
                    "id": "B13",
                    "props": {
                        "primaryBenefitLine": "en vuelos internacionales",
                        "primaryLogoUrl": "https://example.com/aerolineas-group.png",
                    },
                },
                {
                    "id": "B17",
                    "props": {
                        "headingHtml": "Hoteles desde group",
                    },
                },
            ],
            "footer": {
                "id": "F03",
                "props": {
                    "taglineDesktopUrl": "https://example.com/travel-group-footer.jpg",
                    "legalHtml": "LEGAL TRAVEL GROUP",
                },
            },
        }
        request = Request(
            f"{self.base_url}/api/compose-email",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertIn("Hola Travel group", payload["html"])
        self.assertIn(">Entrar</a>", payload["html"])
        self.assertIn("en vuelos internacionales", payload["html"])
        self.assertIn("https://example.com/aerolineas-group.png", payload["html"])
        self.assertIn("Hoteles desde group", payload["html"])
        self.assertIn("https://example.com/travel-group-footer.jpg", payload["html"])
        self.assertIn("LEGAL TRAVEL GROUP", payload["html"])
        self.assertEqual(payload["manifest"]["requested"]["body"], ["B12", "B13", "B14", "B15", "B17", "B16"])

    def test_post_compose_email_html_query_returns_raw_html(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "header": "H01",
            "body": ["B09"],
            "footer": "F01",
        }
        request = Request(
            f"{self.base_url}/api/compose-email?html",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = response.read().decode("utf-8")
            content_type = response.headers.get_content_type()
        self.assertEqual(content_type, "text/html")
        self.assertIn("<!DOCTYPE html>", payload)

    def test_post_compose_email_manifest_query_returns_only_manifest(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "header": "H01",
            "body": ["B09"],
            "footer": "F01",
        }
        request = Request(
            f"{self.base_url}/api/compose-email?manifest",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
        self.assertIn("requested", payload)
        self.assertIn("expanded", payload)
        self.assertNotIn("html", payload)

    def test_post_compose_email_rejects_conflicting_output_queries(self) -> None:
        body = {
            "templateFamily": "marigold-v4.2",
            "header": "H01",
            "body": ["B09"],
            "footer": "F01",
        }
        request = Request(
            f"{self.base_url}/api/compose-email?html&manifest",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with self.assertRaises(HTTPError) as error:
            urlopen(request)
        exception = error.exception
        payload = json.loads(exception.read().decode("utf-8"))
        exception.close()
        self.assertEqual(exception.code, 400)
        self.assertEqual(payload["error"], "ValidationError")

    def test_post_compose_email_rejects_malformed_json(self) -> None:
        request = Request(
            f"{self.base_url}/api/compose-email",
            data=b"{",
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with self.assertRaises(HTTPError) as error:
            urlopen(request)
        exception = error.exception
        payload = json.loads(exception.read().decode("utf-8"))
        exception.close()
        self.assertEqual(exception.code, 400)
        self.assertEqual(payload["error"], "ValidationError")
