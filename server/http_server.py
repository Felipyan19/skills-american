"""Minimal HTTP API exposing the composer endpoints."""

from __future__ import annotations

import json
import re
import unicodedata
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from functools import lru_cache
from typing import Any
from urllib.parse import parse_qs, urlparse

from .composer import compose_email, list_components
from .errors import ComposerError, NotFoundError, ValidationError


ROOT_DIR = Path(__file__).resolve().parents[1]
MODULE1_PAYLOADS_PATH = Path(__file__).resolve().parents[1] / "catalog" / "examples" / "module1.json"
MODULE1_UI_PATH = Path(__file__).resolve().parent / "ui" / "module1_ui.html"
EXAMPLE_UI_PATH = Path(__file__).resolve().parent / "ui" / "example_ui.html"
CAMPAIGN_DOCS_DIR = ROOT_DIR / "docs" / "campanas"
CAMPAIGN_DOCS_INDEX_PATH = CAMPAIGN_DOCS_DIR / "README.md"

_OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "Skills American – Email Composer API",
        "version": "1.0.0",
        "description": (
            "Component-driven email HTML composition service for American Express templates. "
            "Assemble emails by combining header, body, and footer components from a template family."
        ),
    },
    "servers": [{"url": "http://localhost:5050", "description": "Local"}],
    "paths": {
        "/api/components": {
            "get": {
                "summary": "List available components",
                "description": "Returns all components (headers, body blocks, footers) available for a given template family.",
                "operationId": "listComponents",
                "parameters": [
                    {
                        "name": "templateFamily",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "enum": ["marigold-v4.0", "marigold-v4.2", "centurion-1.0"],
                        },
                        "description": "The template family to list components for.",
                        "example": "marigold-v4.2",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "List of components",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ComponentList"},
                                "example": {
                                    "templateFamily": "marigold-v4.2",
                                    "components": [
                                        {
                                            "id": "H01",
                                            "slot": "header",
                                            "repeatable": False,
                                            "requiredProps": [],
                                            "defaults": {},
                                            "sourceIds": ["PH01-v4.2"],
                                            "composeType": "single",
                                        }
                                    ],
                                },
                            }
                        },
                    },
                    "404": {"description": "Unknown template family", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Error"}}}},
                },
            }
        },
        "/api/compose-email": {
            "post": {
                "summary": "Compose an email",
                "description": (
                    "Assembles a full HTML email from the specified template family and components. "
                    "Use `?html` to receive only the HTML string, `?manifest` to receive only the component manifest."
                ),
                "operationId": "composeEmail",
                "parameters": [
                    {
                        "name": "html",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "boolean"},
                        "description": "Return only the HTML string (no JSON wrapper).",
                    },
                    {
                        "name": "manifest",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "boolean"},
                        "description": "Return only the component manifest.",
                    },
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ComposeEmailRequest"},
                            "example": {
                                "templateFamily": "marigold-v4.2",
                                "header": "H01",
                                "body": [
                                    {
                                        "id": "B01",
                                        "props": {
                                            "headline": "Descubrí un beneficio especial",
                                            "description": "Texto del módulo.",
                                            "ctaLabel": "Conocé más",
                                            "ctaUrl": "https://www.americanexpress.com/",
                                        },
                                    }
                                ],
                                "footer": "F01",
                                "globals": {"includeSeparators": True},
                            },
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Composed email (full, html-only, or manifest-only depending on query params)",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ComposeEmailResponse"}
                            },
                            "text/html": {"schema": {"type": "string"}},
                        },
                    },
                    "400": {"description": "Validation error", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Error"}}}},
                    "404": {"description": "Unknown component or family", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Error"}}}},
                },
            }
        },
    },
    "components": {
        "schemas": {
            "ComponentDefinition": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "example": "B01"},
                    "slot": {"type": "string", "enum": ["header", "body", "footer"]},
                    "repeatable": {"type": "boolean"},
                    "requiredProps": {"type": "array", "items": {"type": "string"}},
                    "defaults": {"type": "object"},
                    "sourceIds": {"type": "array", "items": {"type": "string"}},
                    "composeType": {"type": "string"},
                },
            },
            "ComponentList": {
                "type": "object",
                "properties": {
                    "templateFamily": {"type": "string"},
                    "components": {"type": "array", "items": {"$ref": "#/components/schemas/ComponentDefinition"}},
                },
            },
            "ComponentRequest": {
                "oneOf": [
                    {"type": "string", "description": "Component ID shorthand, e.g. \"H01\""},
                    {
                        "type": "object",
                        "required": ["id"],
                        "properties": {
                            "id": {"type": "string"},
                            "props": {"type": "object", "description": "Override component default props"},
                        },
                    },
                ]
            },
            "ComposeEmailRequest": {
                "type": "object",
                "required": ["templateFamily", "header", "footer"],
                "properties": {
                    "templateFamily": {"type": "string", "enum": ["marigold-v4.0", "marigold-v4.2", "centurion-1.0"]},
                    "header": {"$ref": "#/components/schemas/ComponentRequest"},
                    "body": {"type": "array", "items": {"$ref": "#/components/schemas/ComponentRequest"}, "default": []},
                    "footer": {"$ref": "#/components/schemas/ComponentRequest"},
                    "globals": {
                        "type": "object",
                        "properties": {
                            "includeSeparators": {"type": "boolean", "default": True}
                        },
                    },
                },
            },
            "ManifestEntry": {
                "type": "object",
                "properties": {
                    "apiId": {"type": "string"},
                    "slot": {"type": "string"},
                    "sourceId": {"type": "string"},
                    "snippetKey": {"type": "string"},
                    "kind": {"type": "string", "enum": ["snippet", "separator-after"]},
                },
            },
            "ComposeEmailResponse": {
                "type": "object",
                "properties": {
                    "templateFamily": {"type": "string"},
                    "html": {"type": "string", "description": "Full rendered HTML email"},
                    "manifest": {
                        "type": "object",
                        "properties": {
                            "requested": {
                                "type": "object",
                                "properties": {
                                    "templateFamily": {"type": "string"},
                                    "header": {"type": "string"},
                                    "body": {"type": "array", "items": {"type": "string"}},
                                    "footer": {"type": "string"},
                                },
                            },
                            "expanded": {"type": "array", "items": {"$ref": "#/components/schemas/ManifestEntry"}},
                        },
                    },
                },
            },
            "Error": {
                "type": "object",
                "properties": {
                    "error": {"type": "string"},
                    "message": {"type": "string"},
                },
            },
        }
    },
}

_SWAGGER_UI_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Email Composer API – Swagger UI</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({
      url: "/openapi.json",
      dom_id: "#swagger-ui",
      presets: [SwaggerUIBundle.presets.apis, SwaggerUIBundle.SwaggerUIStandalonePreset],
      layout: "BaseLayout",
      deepLinking: true,
    });
  </script>
</body>
</html>"""


@lru_cache(maxsize=1)
def _load_module1_examples() -> list[dict]:
    with MODULE1_PAYLOADS_PATH.open(encoding="utf-8") as handle:
        raw_examples = json.load(handle)

    seen: dict[str, int] = {}
    enriched: list[dict] = []
    for item in raw_examples:
        base_slug = _slugify(item.get("name", "example"))
        count = seen.get(base_slug, 0) + 1
        seen[base_slug] = count
        example_id = base_slug if count == 1 else f"{base_slug}-{count}"
        enriched.append({**item, "id": example_id})
    return enriched


@lru_cache(maxsize=1)
def _load_campaign_docs_index() -> dict[tuple[str, str, str], str]:
    if not CAMPAIGN_DOCS_INDEX_PATH.is_file():
        return {}

    index_content = CAMPAIGN_DOCS_INDEX_PATH.read_text(encoding="utf-8")
    mapping: dict[tuple[str, str, str], str] = {}
    in_router_section = False
    for raw_line in index_content.splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            in_router_section = line == "## Router para agentes"
            continue
        if not in_router_section:
            continue
        if not line.startswith("|"):
            continue
        if "Campana" in line and "campaignType" in line:
            continue
        if line.startswith("|---"):
            continue

        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        campaign_name = parts[0].strip("`").strip()
        group = parts[1].strip("`").strip()
        campaign_type = parts[2].strip("`").strip()
        doc = parts[4].strip("`").strip()
        if not campaign_name or not group or not campaign_type or not doc:
            continue
        if not doc.endswith(".md"):
            continue
        mapping[(campaign_name.casefold(), group.casefold(), campaign_type.casefold())] = doc
    return mapping


def _campaign_doc_for_example(example: dict) -> str:
    name = str(example.get("name", "")).casefold()
    group = str(example.get("group", "")).casefold()
    campaign_type = str(example.get("campaignType", "")).casefold()
    return _load_campaign_docs_index().get((name, group, campaign_type), "")


@lru_cache(maxsize=32)
def _campaign_doc_supports_variants(doc_name: str) -> bool:
    doc_path = CAMPAIGN_DOCS_DIR / doc_name
    if not doc_path.is_file():
        return False
    content = doc_path.read_text(encoding="utf-8").casefold()
    markers = (
        "edicion version corta",
        "edicion corta desde tipo de campana y grupo",
        "campos de variantes",
        "aceptan variantes por `props`",
    )
    return any(marker in content for marker in markers)


def _dashboard_status_for_example(example: dict) -> str:
    doc_name = _campaign_doc_for_example(example)
    has_dynamic_doc = bool(doc_name) and _campaign_doc_supports_variants(doc_name)

    if has_dynamic_doc:
        return "dinamico"
    if example.get("fidelity") == "alta":
        return "exacto"
    return "pendiente"


def _with_dashboard_fields(example: dict) -> dict:
    enriched = dict(example)
    dashboard_status = _dashboard_status_for_example(example)
    doc_name = _campaign_doc_for_example(example)
    enriched["dashboardStatus"] = dashboard_status
    enriched["campaignDoc"] = doc_name or ""
    return enriched


def _slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "example"


@lru_cache(maxsize=1)
def _load_module1_ui_html() -> str:
    return MODULE1_UI_PATH.read_text(encoding="utf-8")


_MODULE1_UI_HTML = _load_module1_ui_html()


@lru_cache(maxsize=1)
def _load_example_ui_html() -> str:
    return EXAMPLE_UI_PATH.read_text(encoding="utf-8")


_EXAMPLE_UI_HTML = _load_example_ui_html()


def _module1_examples_response(group: str = "", campaign_type: str = "") -> dict:
    examples = _load_module1_examples()
    if group:
        examples = [e for e in examples if e.get("group", "").lower() == group.lower()]
    if campaign_type:
        examples = [e for e in examples if e.get("campaignType", "").lower() == campaign_type.lower()]
    examples = [_with_dashboard_fields(item) for item in examples]
    summary = {
        "dynamic": sum(1 for item in examples if item.get("dashboardStatus") == "dinamico"),
        "exactDashboard": sum(1 for item in examples if item.get("dashboardStatus") == "exacto"),
        "pending": sum(1 for item in examples if item.get("dashboardStatus") == "pendiente"),
        "total": len(examples),
        "exact": sum(1 for item in examples if item.get("fidelity") == "alta"),
        "structural": sum(1 for item in examples if item.get("fidelity") == "estructural"),
        "approximate": sum(1 for item in examples if item.get("fidelity") == "aproximada"),
    }
    return {"count": len(examples), "summary": summary, "examples": examples}


def _find_module1_example(example_id: str) -> dict | None:
    for example in _load_module1_examples():
        if example.get("id") == example_id:
            return example
    return None


def _component_request_id(item: Any) -> str:
    if isinstance(item, str):
        return item
    if isinstance(item, dict) and isinstance(item.get("id"), str):
        return item["id"]
    return ""


def _merge_component_request(base: Any, override: Any) -> Any:
    if override is None:
        return base
    if isinstance(override, str):
        return override
    if not isinstance(override, dict):
        return override

    if isinstance(base, dict):
        merged = dict(base)
    else:
        merged = {"id": _component_request_id(base)}

    override_id = _component_request_id(override)
    if override_id and merged.get("id") and override_id != merged["id"]:
        return override
    if override_id:
        merged["id"] = override_id

    base_props = merged.get("props", {})
    override_props = override.get("props", {})
    if isinstance(base_props, dict) and isinstance(override_props, dict):
        merged["props"] = {**base_props, **override_props}
    elif "props" in override:
        merged["props"] = override_props

    for key, value in override.items():
        if key not in {"id", "props"}:
            merged[key] = value
    return merged


def _merge_body_requests(base_body: Any, override_body: Any) -> Any:
    if override_body is None:
        return base_body
    if not isinstance(base_body, list) or not isinstance(override_body, list):
        return override_body

    merged = list(base_body)
    used_indexes: set[int] = set()
    use_position_fallback = len(override_body) == len(base_body)
    for index, override_item in enumerate(override_body):
        override_id = _component_request_id(override_item)
        target_index = None
        if override_id:
            for candidate_index, candidate_item in enumerate(merged):
                if candidate_index in used_indexes:
                    continue
                if _component_request_id(candidate_item) == override_id:
                    target_index = candidate_index
                    break
        if target_index is None and use_position_fallback and index < len(merged):
            target_index = index

        if target_index is None:
            merged.append(override_item)
            continue

        merged[target_index] = _merge_component_request(merged[target_index], override_item)
        used_indexes.add(target_index)
    return merged


def _resolve_compose_payload(raw: dict) -> dict:
    """If raw contains group/campaignType, look up the example and return its payload.
    Otherwise return raw unchanged (classic explicit-components flow).

    Component fields in raw act as overrides over the selected example, so callers
    can address exact campaigns with group/campaignType and still pass props.
    """
    group = raw.get("group", "")
    campaign_type = raw.get("campaignType", "")
    if not group and not campaign_type:
        return raw

    examples = _load_module1_examples()
    if group:
        examples = [e for e in examples if e.get("group", "").lower() == group.lower()]
    if campaign_type:
        examples = [e for e in examples if e.get("campaignType", "").lower() == campaign_type.lower()]

    template_family = raw.get("templateFamily", "")
    if template_family:
        examples = [e for e in examples if e.get("templateFamily", "").lower() == template_family.lower()]

    if not examples:
        raise NotFoundError("No example matches the given group/campaignType.")
    if len(examples) > 1:
        families = sorted({e["templateFamily"] for e in examples})
        raise ValidationError(
            f"Found {len(examples)} examples for that group/campaignType. "
            f"Specify 'templateFamily' to disambiguate: {families}."
        )

    payload = dict(examples[0]["payload"])
    if "globals" in raw:
        payload["globals"] = raw["globals"]
    if "header" in raw:
        payload["header"] = _merge_component_request(payload.get("header"), raw["header"])
    if "body" in raw:
        payload["body"] = _merge_body_requests(payload.get("body"), raw["body"])
    if "footer" in raw:
        payload["footer"] = _merge_component_request(payload.get("footer"), raw["footer"])
    return payload


def _module1_example_response(example_id: str) -> dict | None:
    example = _find_module1_example(example_id)
    if example is None:
        return None
    return {"example": _with_dashboard_fields(example)}


def _module1_example_markdown(example: dict) -> str:
    lines = [
        f"### {example['name']}",
        "",
        f"- Archivo: `{example.get('relativePath', '')}`",
        f"- Familia: `{example.get('templateFamily', '')}`",
        f"- Fidelidad: `{example.get('fidelity', '')}`",
    ]
    reference_source_ids = example.get("referenceSourceIds") or []
    if reference_source_ids:
        lines.append(f"- SourceIds de referencia: `{', '.join(reference_source_ids)}`")
    substitutions = example.get("substitutions") or []
    for substitution in substitutions:
        lines.append(f"- Sustitucion: {substitution}")
    unsupported_source_ids = example.get("unsupportedSourceIds") or []
    if unsupported_source_ids:
        lines.append(f"- SourceIds sin componente publico: `{', '.join(unsupported_source_ids)}`")
    for note in example.get("notes") or []:
        lines.append(f"- Nota: {note}")
    lines.extend([
        "",
        "```json",
        json.dumps(example.get("payload", {}), indent=2, ensure_ascii=False),
        "```",
    ])
    return "\n".join(lines).strip() + "\n"


def _module1_campaign_doc_markdown(example: dict) -> tuple[str, str]:
    dashboard_example = _with_dashboard_fields(example)
    doc_name = dashboard_example.get("campaignDoc", "")
    if not isinstance(doc_name, str) or not doc_name:
        return _module1_example_markdown(example), ""

    doc_path = (CAMPAIGN_DOCS_DIR / doc_name).resolve()
    docs_root = CAMPAIGN_DOCS_DIR.resolve()
    if doc_path != docs_root and docs_root not in doc_path.parents:
        return _module1_example_markdown(example), ""
    if not doc_path.is_file():
        return _module1_example_markdown(example), ""
    return doc_path.read_text(encoding="utf-8"), doc_name


def _module1_example_markdown_response(example_id: str) -> dict | None:
    example = _find_module1_example(example_id)
    if example is None:
        return None
    dashboard_example = _with_dashboard_fields(example)
    markdown, markdown_doc = _module1_campaign_doc_markdown(example)
    return {
        "exampleId": dashboard_example["id"],
        "name": dashboard_example["name"],
        "group": dashboard_example["group"],
        "dashboardStatus": dashboard_example["dashboardStatus"],
        "markdownDoc": markdown_doc,
        "markdownSource": "campaign-doc" if markdown_doc else "generated",
        "markdown": markdown,
    }


def _module1_reference_html(example: dict) -> str | None:
    relative_path = example.get("relativePath")
    if not isinstance(relative_path, str) or not relative_path:
        return None

    root = ROOT_DIR.resolve()
    candidate = (ROOT_DIR / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        return None
    if not candidate.is_file():
        return None
    return candidate.read_text(encoding="utf-8", errors="ignore")


def _module1_example_html_response(example_id: str) -> dict | None:
    example = _find_module1_example(example_id)
    if example is None:
        return None

    reference_html = _module1_reference_html(example)
    if reference_html is not None:
        return {
            "exampleId": example["id"],
            "name": example["name"],
            "group": example["group"],
            "relativePath": example.get("relativePath", ""),
            "source": "reference",
            "html": reference_html,
        }

    result = compose_email(example["payload"])
    return {
        "exampleId": example["id"],
        "name": example["name"],
        "group": example["group"],
        "relativePath": example.get("relativePath", ""),
        "source": "generated",
        "html": result["html"],
    }


class EmailComposerHandler(BaseHTTPRequestHandler):
    server_version = "EmailComposerHTTP/1.0"

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, status: int, payload: str) -> None:
        body = payload.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _post_response_mode(self, query: str) -> str:
        params = parse_qs(query, keep_blank_values=True)
        wants_html = "html" in params
        wants_manifest = "manifest" in params
        if wants_html and wants_manifest:
            raise ValueError("Use either '?html' or '?manifest', not both.")
        if wants_html:
            return "html"
        if wants_manifest:
            return "manifest"
        return "full"

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/module1", "/module1/"):
            self._send_html(HTTPStatus.OK, _MODULE1_UI_HTML)
            return
        if parsed.path.startswith("/example/"):
            example_id = parsed.path.removeprefix("/example/").strip("/")
            if not example_id or _module1_example_response(example_id) is None:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            self._send_html(HTTPStatus.OK, _EXAMPLE_UI_HTML)
            return
        if parsed.path in ("/docs", "/docs/"):
            self._send_html(HTTPStatus.OK, _SWAGGER_UI_HTML)
            return
        if parsed.path == "/openapi.json":
            self._send_json(HTTPStatus.OK, _OPENAPI_SPEC)
            return
        if parsed.path.startswith("/api/module1/examples/") and parsed.path.endswith("/html"):
            example_id = parsed.path.removesuffix("/html").removeprefix("/api/module1/examples/").strip("/")
            if not example_id:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            try:
                payload = _module1_example_html_response(example_id)
            except ComposerError as exc:
                self._send_json(exc.status_code, exc.to_dict())
                return
            if payload is None:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path.startswith("/api/module1/examples/") and parsed.path.endswith("/markdown"):
            example_id = parsed.path.removesuffix("/markdown").removeprefix("/api/module1/examples/").strip("/")
            if not example_id:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            payload = _module1_example_markdown_response(example_id)
            if payload is None:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path.startswith("/api/module1/examples/"):
            example_id = parsed.path.removeprefix("/api/module1/examples/").strip("/")
            payload = _module1_example_response(example_id)
            if payload is None:
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Example not found."})
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path == "/api/module1/examples":
            qs = parse_qs(parsed.query)
            group = qs.get("group", [""])[0]
            campaign_type = qs.get("campaignType", [""])[0]
            self._send_json(HTTPStatus.OK, _module1_examples_response(group, campaign_type))
            return
        if parsed.path != "/api/components":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Endpoint not found."})
            return
        template_family = parse_qs(parsed.query).get("templateFamily", [""])[0]
        try:
            result = list_components(template_family)
            self._send_json(HTTPStatus.OK, result)
        except ComposerError as exc:
            self._send_json(exc.status_code, exc.to_dict())

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/api/compose-email":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "NotFound", "message": "Endpoint not found."})
            return
        content_length = int(self.headers.get("Content-Length", "0"))
        try:
            response_mode = self._post_response_mode(parsed.query)
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
            payload = _resolve_compose_payload(payload)
            result = compose_email(payload)
            if response_mode == "html":
                self._send_html(HTTPStatus.OK, result["html"])
            elif response_mode == "manifest":
                self._send_json(HTTPStatus.OK, result["manifest"])
            else:
                self._send_json(HTTPStatus.OK, result)
        except json.JSONDecodeError:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "ValidationError", "message": "Malformed JSON body."})
        except ValueError as exc:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "ValidationError", "message": str(exc)})
        except ComposerError as exc:
            self._send_json(exc.status_code, exc.to_dict())

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def serve(host: str = "127.0.0.1", port: int = 5050) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), EmailComposerHandler)


def main() -> None:
    import os
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5050"))
    server = serve(host=host, port=port)
    try:
        print(f"Serving email composition API on http://{host}:{port}")
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
