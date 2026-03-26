"""Composition engine for component-driven email HTML."""

from __future__ import annotations

import html
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping

from .errors import NotFoundError, ValidationError
from .registry import ComponentDefinition, FAMILIES, FamilyDefinition
from .template_engine import render_template


def _camel_to_snake_key(name: str) -> str:
    chars: list[str] = []
    for char in name:
        if char.isupper() and chars:
            chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def _normalize_keys(value: Any) -> Any:
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            normalized[key] = _normalize_keys(item)
            if isinstance(key, str):
                normalized[_camel_to_snake_key(key)] = _normalize_keys(item)
        return normalized
    if isinstance(value, list):
        return [_normalize_keys(item) for item in value]
    return value


def _deep_merge(base: Mapping[str, Any], override: Mapping[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _ensure_dict(value: Any, field_name: str) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValidationError(f"'{field_name}' must be an object when provided.")
    return value


def _normalize_component_request(item: Any, slot: str) -> dict[str, Any]:
    if isinstance(item, str):
        return {"id": item, "props": {}}
    if not isinstance(item, dict):
        raise ValidationError(f"'{slot}' components must be a string ID or object.")
    component_id = item.get("id")
    if not isinstance(component_id, str) or not component_id:
        raise ValidationError(f"'{slot}' component objects require a non-empty 'id'.")
    props = item.get("props", {})
    if not isinstance(props, dict):
        raise ValidationError(f"'props' for component '{component_id}' must be an object.")
    return {"id": component_id, "props": props}


def _normalize_body(items: Any) -> list[dict[str, Any]]:
    if items is None:
        return []
    if not isinstance(items, list):
        raise ValidationError("'body' must be an array.")
    return [_normalize_component_request(item, "body") for item in items]


def _require_props(component: ComponentDefinition, context: Mapping[str, Any]) -> None:
    missing: list[str] = []
    for prop_name in component.required_props:
        if not context.get(prop_name) and not context.get(_camel_to_snake_key(prop_name)):
            missing.append(prop_name)
    if missing:
        raise ValidationError(
            f"Component '{component.api_id}' is missing required props: {', '.join(missing)}."
        )


def _render_cross_sell_items(items: Iterable[Mapping[str, Any]], light: bool = True) -> str:
    html_blocks: list[str] = []
    border = "#DEDEDE" if light else "#333333"
    background = "#FFFFFF" if light else "#111111"
    text_color = "#00175A" if light else "#FFFFFF"
    for item in items:
        title = html.escape(str(item.get("title", "")))
        subtitle = html.escape(str(item.get("subtitle", "")))
        icon_url = html.escape(str(item.get("iconUrl", item.get("icon_url", ""))))
        block = f"""
        <th class="full-width-block" style="padding:10px;" valign="top">
          <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:{background}; border:1px solid {border};">
            <tr>
              <td align="center" style="padding:20px;">
                <img src="{icon_url}" alt="" width="36" style="display:block; height:auto; margin:0 auto 12px;" />
                <p style="margin:0; color:{text_color}; font-size:16px; line-height:20px; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;"><strong>{title}</strong></p>
                <p style="margin:8px 0 0; color:{text_color}; font-size:14px; line-height:18px; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;">{subtitle}</p>
              </td>
            </tr>
          </table>
        </th>
        """
        html_blocks.append(block.strip())
    return "\n".join(html_blocks)


def _paired_items_builder(context: dict[str, Any], _: ComponentDefinition, family_id: str) -> dict[str, Any]:
    items = context.get("items")
    if not isinstance(items, list) or len(items) != 2:
        raise ValidationError(
            f"Component '{context['apiId']}' in family '{family_id}' expects exactly 2 items."
        )
    left = _normalize_keys(items[0])
    right = _normalize_keys(items[1])
    return {
        "left": left,
        "right": right,
        "left_title": left.get("title", ""),
        "left_subtitle": left.get("subtitle", ""),
        "left_description": left.get("description", ""),
        "left_image_url": left.get("image_url", ""),
        "left_logo_url": left.get("logo_url", ""),
        "left_cta_url": left.get("cta_url", ""),
        "left_cta_label": left.get("cta_label", context.get("ctaLabel", "Conocé más")),
        "left_badge": left.get("badge", ""),
        "right_title": right.get("title", ""),
        "right_subtitle": right.get("subtitle", ""),
        "right_description": right.get("description", ""),
        "right_image_url": right.get("image_url", ""),
        "right_logo_url": right.get("logo_url", ""),
        "right_cta_url": right.get("cta_url", ""),
        "right_cta_label": right.get("cta_label", context.get("ctaLabel", "Conocé más")),
        "right_badge": right.get("badge", ""),
    }


def _benefit_cards_builder(context: dict[str, Any], _: ComponentDefinition, family_id: str) -> dict[str, Any]:
    cards = context.get("cards")
    if not isinstance(cards, list) or not cards:
        raise ValidationError(
            f"Component '{context['apiId']}' in family '{family_id}' expects a non-empty 'cards' array."
        )
    light = not family_id.startswith("centurion")
    return {"cards_html": _render_cross_sell_items(cards, light=light)}


def _cross_sell_builder(context: dict[str, Any], _: ComponentDefinition, family_id: str) -> dict[str, Any]:
    items = context.get("crossSellItems", context.get("cross_sell_items", []))
    light = not family_id.startswith("centurion")
    return {"cross_sell_items_html": _render_cross_sell_items(items, light=light)}


def _tm03_triptych_builder(context: dict[str, Any], _: ComponentDefinition, __: str) -> dict[str, Any]:
    step3_logo_url = context.get("step3LogoUrl", context.get("step3_logo_url", ""))
    if not step3_logo_url:
        return {"step3LogoBlock": "", "step3_logo_block": ""}

    step3_logo_alt = html.escape(
        str(context.get("step3LogoAlt", context.get("step3_logo_alt", "")))
    )
    step3_logo_width = html.escape(
        str(context.get("step3LogoWidth", context.get("step3_logo_width", "107")))
    )
    step3_logo_url = html.escape(str(step3_logo_url))
    block = (
        f'<img class="center-align" src="{step3_logo_url}" alt="{step3_logo_alt}" '
        f'width="{step3_logo_width}" style="display:block; height:auto; color:#FFFFFF;">'
    )
    return {"step3LogoBlock": block, "step3_logo_block": block}


def _marigold_v42_header_builder(context: dict[str, Any], _: ComponentDefinition, __: str) -> dict[str, Any]:
    secondary_logo_url = context.get("secondaryLogoUrl", context.get("secondary_logo_url", ""))
    tagline_url = context.get("taglineUrl", context.get("tagline_url", ""))
    card_image_url = context.get("cardImageUrl", context.get("card_image_url", ""))
    account_suffix = html.escape(str(context.get("accountSuffix", context.get("account_suffix", ""))))
    member_since = html.escape(str(context.get("memberSince", context.get("member_since", ""))))
    greeting_name = html.escape(str(context.get("greetingName", context.get("greeting_name", ""))))
    logo_alt = html.escape(str(context.get("logoAlt", context.get("logo_alt", "American Express"))))
    secondary_logo_alt = html.escape(str(context.get("secondaryLogoAlt", context.get("secondary_logo_alt", ""))))
    tagline_alt = html.escape(str(context.get("taglineAlt", context.get("tagline_alt", ""))))
    card_image_alt = html.escape(str(context.get("cardImageAlt", context.get("card_image_alt", ""))))
    logo_block = f"""
      <td width="60" style="width:60px;" class="bp-logo">
        <a href="{html.escape(str(context.get('logoHref', context.get('logo_href', 'http://www.americanexpress.com.ar'))))}" target="_blank" style="text-decoration:none;border:none;outline:0;">
          <img src="{html.escape(str(context.get('logoUrl', context.get('logo_url', ''))))}" alt="{logo_alt}" width="60" style="width:60px;height:auto;color:#3D3D3D;" class="bp-logo">
        </a>
      </td>
    """.strip()
    secondary_logo_block = ""
    if secondary_logo_url:
        secondary_logo_block = f"""
        <td width="163" style="padding-left:14px" class="LogoMr">
          <a href="{html.escape(str(context.get('secondaryLogoHref', context.get('secondary_logo_href', '#'))))}" target="_blank">
            <img src="{html.escape(str(secondary_logo_url))}" alt="{secondary_logo_alt}" width="163" style="width:163px;height:auto;color:#3D3D3D;">
          </a>
        </td>
        """.strip()
    tagline_block = ""
    if tagline_url:
        tagline_block = f"""
        <td width="150" style="padding-left:10px" class="Slogn">
          <a href="{html.escape(str(context.get('taglineHref', context.get('tagline_href', 'http://www.americanexpress.com.ar'))))}" target="_blank">
            <img src="{html.escape(str(tagline_url))}" alt="{tagline_alt}" width="150" style="width:150px;height:auto;color:#3D3D3D;">
          </a>
        </td>
        """.strip()
    card_block = ""
    if card_image_url:
        card_block = f"""
        <td width="80" align="right" valign="top" style="padding-left:12px;">
          <img src="{html.escape(str(card_image_url))}" alt="{card_image_alt}" width="80" style="width:80px;height:auto;color:#3D3D3D;" class="bp02-card">
        </td>
        """.strip()
    account_details = "Tu cuenta termina en:"
    if context.get("showMemberSince", context.get("show_member_since", False)):
        account_details += f" <br><span class=\"mobile-off\">Miembro desde: {member_since}</span>"
    greeting_row = ""
    if context.get("showGreeting", context.get("show_greeting", False)):
        login_block = ""
        if context.get("showLogin", context.get("show_login", False)):
            login_block = f"""
            <td align="right">
              <a href="{html.escape(str(context.get('loginUrl', context.get('login_url', '#'))))}" class="button-secondary-light bp-login-button" target="_blank" style="border:2px solid #006FCF; border-radius:3px; color:#006FCF; display:inline-block; font-size:15px; line-height:100%; padding:13px 12px 13px; text-decoration:none; text-align:center; font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif; white-space:nowrap;">{html.escape(str(context.get('loginLabel', context.get('login_label', 'Mi cuenta'))))}</a>
            </td>
            """.strip()
        greeting_row = f"""
        <tr>
          <td style="padding:10px 20px 11px 20px;border-bottom:solid 1px #E0E0E0;border-top:solid 1px #E0E0E0" class="pd10">
            <table role="none" cellpadding="0" cellspacing="0" border="0" width="100%">
              <tr>
                <td style="padding-right:20px;">
                  <p style="font-family:HelveticaNeue, Helvetica Neue Regular, Helvetica, Arial, sans-serif;color:#3D3D3D; font-size:15px; line-height:22px;" class="bp-text">Hola {greeting_name}</p>
                </td>
                {login_block}
              </tr>
            </table>
          </td>
        </tr>
        """.strip()
    return {
        "logo_block": logo_block,
        "secondary_logo_block": secondary_logo_block,
        "tagline_block": tagline_block,
        "card_block": card_block,
        "account_suffix": account_suffix,
        "account_details": account_details,
        "greeting_row": greeting_row,
    }


def _context_builders() -> dict[str, Any]:
    return {
        "paired_items": _paired_items_builder,
        "benefit_cards": _benefit_cards_builder,
        "cross_sell_icons": _cross_sell_builder,
        "tm03_triptych": _tm03_triptych_builder,
        "marigold_v42_header": _marigold_v42_header_builder,
    }


@lru_cache(maxsize=None)
def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _get_family(family_id: str) -> FamilyDefinition:
    family = FAMILIES.get(family_id)
    if family is None:
        raise NotFoundError(f"Unknown templateFamily '{family_id}'.")
    return family


def list_components(template_family: str) -> dict[str, Any]:
    family = _get_family(template_family)
    items: list[dict[str, Any]] = []
    for component in family.components.values():
        items.append(
            {
                "id": component.api_id,
                "slot": component.slot,
                "repeatable": component.repeatable,
                "requiredProps": list(component.required_props),
                "defaults": dict(component.defaults),
                "sourceIds": list(component.source_ids),
                "composeType": component.compose_type,
            }
        )
    items.sort(key=lambda item: (item["slot"], item["id"]))
    return {"templateFamily": template_family, "components": items}


def _render_component(
    family: FamilyDefinition,
    component: ComponentDefinition,
    request_component: Mapping[str, Any],
    slot: str,
    globals_context: Mapping[str, Any],
) -> tuple[str, list[dict[str, Any]]]:
    if component.slot != slot:
        raise ValidationError(
            f"Component '{component.api_id}' cannot be used in slot '{slot}'. Expected '{component.slot}'."
        )
    props = _normalize_keys(request_component.get("props", {}))
    defaults = _normalize_keys(dict(component.defaults))
    globals_normalized = _normalize_keys(dict(globals_context))
    context = _deep_merge(defaults, props)
    context["globals"] = globals_normalized
    for key, value in globals_normalized.items():
        context.setdefault(key, value)
    context["apiId"] = component.api_id
    _require_props(component, context)
    if component.context_builder:
        builder = _context_builders()[component.context_builder]
        context.update(builder(context, component, family.family_id))

    fragments: list[str] = []
    manifest: list[dict[str, Any]] = []
    for snippet_key in component.snippet_keys:
        asset = family.snippets[snippet_key]
        rendered = render_template(_read_text(asset.path), context)
        fragments.append(rendered)
        manifest.append(
            {
                "apiId": component.api_id,
                "slot": slot,
                "sourceId": asset.source_id,
                "snippetKey": asset.key,
                "kind": "snippet",
            }
        )
    return "\n".join(fragment for fragment in fragments if fragment.strip()), manifest


def compose_email(payload: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, Mapping):
        raise ValidationError("Request payload must be a JSON object.")

    template_family = payload.get("templateFamily")
    if not isinstance(template_family, str) or not template_family:
        raise ValidationError("'templateFamily' is required.")
    family = _get_family(template_family)

    globals_context = _ensure_dict(payload.get("globals", {}), "globals")
    include_separators = globals_context.get("includeSeparators", globals_context.get("include_separators", True))
    if not isinstance(include_separators, bool):
        raise ValidationError("'globals.includeSeparators' must be a boolean when provided.")
    header_request = _normalize_component_request(payload.get("header"), "header")
    footer_request = _normalize_component_request(payload.get("footer"), "footer")
    body_requests = _normalize_body(payload.get("body", []))

    header_component = family.components.get(header_request["id"])
    footer_component = family.components.get(footer_request["id"])
    if header_component is None:
        raise NotFoundError(f"Unknown header component '{header_request['id']}' for family '{template_family}'.")
    if footer_component is None:
        raise NotFoundError(f"Unknown footer component '{footer_request['id']}' for family '{template_family}'.")

    body_components: list[ComponentDefinition] = []
    for item in body_requests:
        component = family.components.get(item["id"])
        if component is None:
            raise NotFoundError(f"Unknown body component '{item['id']}' for family '{template_family}'.")
        body_components.append(component)

    counts = Counter(item["id"] for item in body_requests)
    for component_id, count in counts.items():
        component = family.components[component_id]
        if count > 1 and not component.repeatable:
            raise ValidationError(f"Component '{component_id}' cannot be repeated in the body.")

    header_html, header_manifest = _render_component(
        family=family,
        component=header_component,
        request_component=header_request,
        slot="header",
        globals_context=globals_context,
    )

    body_fragments: list[str] = []
    body_manifest: list[dict[str, Any]] = []
    for index, (request_item, component) in enumerate(zip(body_requests, body_components, strict=True)):
        body_html, manifest_items = _render_component(
            family=family,
            component=component,
            request_component=request_item,
            slot="body",
            globals_context=globals_context,
        )
        body_fragments.append(body_html)
        body_manifest.extend(manifest_items)
        if include_separators and component.auto_separator_after and index < len(body_requests) - 1:
            separator_asset = family.snippets[component.auto_separator_after]
            separator_html = render_template(
                _read_text(separator_asset.path),
                _normalize_keys(_deep_merge(globals_context, request_item["props"])),
            )
            body_fragments.append(separator_html)
            body_manifest.append(
                {
                    "apiId": component.api_id,
                    "slot": "body",
                    "sourceId": separator_asset.source_id,
                    "snippetKey": separator_asset.key,
                    "kind": "separator-after",
                }
            )

    footer_html, footer_manifest = _render_component(
        family=family,
        component=footer_component,
        request_component=footer_request,
        slot="footer",
        globals_context=globals_context,
    )

    shell_context = _normalize_keys(_deep_merge(family.shell_defaults, globals_context))
    shell_context.update(
        {
            "subject": globals_context.get("subject", family.shell_defaults.get("subject", "AMEX")),
            "header_html": header_html,
            "body_html": "\n".join(fragment for fragment in body_fragments if fragment.strip()),
            "footer_html": footer_html,
        }
    )
    html_output = render_template(_read_text(family.shell_path), shell_context)
    manifest = {
        "requested": {
            "templateFamily": template_family,
            "header": header_request["id"],
            "body": [item["id"] for item in body_requests],
            "footer": footer_request["id"],
        },
        "expanded": header_manifest + body_manifest + footer_manifest,
    }
    return {
        "templateFamily": template_family,
        "html": html_output,
        "manifest": manifest,
    }


def compose_email_json(payload: str) -> str:
    """Helper used by manual CLI or future scripts."""

    data = json.loads(payload)
    return json.dumps(compose_email(data), ensure_ascii=False, indent=2)
