"""Tiny placeholder renderer used by shells and snippets."""

from __future__ import annotations

import re
from typing import Any, Mapping


PLACEHOLDER_RE = re.compile(r"{{\s*([a-zA-Z0-9_.-]+)\s*}}")


def _lookup(context: Mapping[str, Any], path: str) -> Any:
    value: Any = context
    for part in path.split("."):
        if isinstance(value, Mapping):
            value = value.get(part, "")
        else:
            return ""
    return value


def render_template(template: str, context: Mapping[str, Any]) -> str:
    """Replace {{placeholders}} using dot-path lookups from context."""

    def replacer(match: re.Match[str]) -> str:
        value = _lookup(context, match.group(1))
        if value is None:
            return ""
        return str(value)

    return PLACEHOLDER_RE.sub(replacer, template)
