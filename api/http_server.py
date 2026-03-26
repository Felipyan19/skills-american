"""Minimal HTTP API exposing the composer endpoints."""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from .composer import compose_email, list_components
from .errors import ComposerError


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


def serve(host: str = "127.0.0.1", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), EmailComposerHandler)


def main() -> None:
    import os
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
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
