from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REFERENCE_DIR = ROOT / "1. Referencias por segmento"
OUTPUT_JSON = ROOT / "catalog" / "examples" / "module1.json"
OUTPUT_MD = ROOT / "catalog" / "examples" / "module1.md"


PATTERNS = [
    (re.compile(r"START:\s+(?:ID=|TD=)?([A-Z]{2,4}\d{2}(?:-v\d\.\d)?)"), None),
    (re.compile(r"START:\s+Consumer Default-v4\.2"), "Consumer Default-v4.2"),
    (re.compile(r"START:\s+BP01 Master - Centurion"), "BP01"),
    (re.compile(r"START:\s+Hero banner area CHB01"), "CHB01"),
    (re.compile(r"START:\s+FM05_business Footer Tagline-v4\.0"), "FM05"),
]

EXACT_OVERRIDES: dict[str, dict[str, Any]] = {
    "1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-Travel-Agst25/MERCHANT-Shot-Travel-Agst25.html": {
        "templateFamily": "marigold-v4.2",
        "header": "H02",
        "body": ["B12", "B13", "B14", "B15", "B17", "B16"],
        "footer": "F03",
        "globals": {"includeSeparators": False},
        "fidelity": "alta",
        "notes": [
            "Usa el set dedicado de MERCHANT Shot Travel.",
            "Es la mejor aproximacion disponible hoy dentro del catalogo.",
        ],
    },
    "1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Newsletter-Dic25/MERCHANT-Newsletter-Dic25.html": {
        "templateFamily": "marigold-v4.2",
        "header": "H03",
        "body": ["B18", "B19", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27"],
        "footer": "F04",
        "globals": {"includeSeparators": False},
        "fidelity": "alta",
        "notes": [
            "Usa el set dedicado de MERCHANT Newsletter.",
            "El HTML de referencia incluye un HB08 vacio que funciona como espaciador y no existe como componente publico separado.",
        ],
    },
    "1. Referencias por segmento/MERCHANT - Socio/MERCHANT-Shot-deporte-DIC25/MERCHANT-Shot-deporte-DIC25.html": {
        "templateFamily": "marigold-v4.2",
        "header": "H04",
        "body": ["B28", "B29", "B30", "B31", "B32"],
        "footer": "F05",
        "globals": {"includeSeparators": False},
        "fidelity": "alta",
        "notes": [
            "Usa el set dedicado de MERCHANT Shot Deporte.",
        ],
    },
}

MARIGOLD_V42_BODY = {
    "HB03-v4.2": "B01",
    "HB08-v4.2": "B02",
    "HB15-v4.2": "B03",
    "HB16-v4.2": "B04",
    "HB18-v4.2": "B05",
    "HB21-v4.2": "B06",
    "IM03-v4.2": "B07",
    "TM01-v4.2": "B08",
    "TM04-v4.2": "B09",
    "TM17-v4.2": "B10",
    "TM03-v4.2": "B11",
    "TM03": "B11",
}

MARIGOLD_V42_SUBSTITUTIONS = {
    "IM02-v4.0": ("B07", "Se sustituyo IM02-v4.0 por B07 porque ese HTML mezcla shell v4.2 con un modulo heredado v4.0."),
    "TM23-v4.2": ("B09", "Se sustituyo TM23-v4.2 por B09 como aproximacion al bloque promocional."),
}

MARIGOLD_V40_BODY = {
    "HB03-v4.0": "B01",
    "HB15-v4.0": "B02",
    "IM02-v4.0": "B03",
    "TM04-v4.0": "B04",
}

CENTURION_BODY = {
    "CHB01": "B01",
    "CTM03": "B02",
    "CIM02": "B03",
    "CIM03": "B04",
    "CIM05": "B05",
}

CENTURION_SUBSTITUTIONS = {
    "CTM02": ("B02", "Se sustituyo CTM02 por B02 como el texto full-width mas cercano disponible."),
    "CTM04": ("B02", "Se sustituyo CTM04 por B02 porque aun no existe un componente publico especifico para CTM04."),
}

SKIP_IDS = {
    "PH01-v4.2",
    "Consumer Default-v4.2",
    "FM05-v4.2",
    "FM01-v4.2",
    "TM06-v4.2",
    "FM02",
    "FM03-v4.2",
    "FM04-v4.2",
    "PH01-v4.0",
    "BP02-v4.0",
    "FM05",
    "FM01-v4.0",
    "TM06-v4.0",
    "FM03-v4.0",
    "FM04-v4.0",
    "PH01",
    "BP01",
    "TM06",
    "CFM02",
    "CTM14",
    "CFM03",
}

FIDELITY_LABELS = {
    "alta": "Exacta",
    "estructural": "Homologada",
    "aproximada": "Pendiente",
}


def extract_source_ids(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    ids: list[str] = []
    for line in text.splitlines():
        for pattern, fixed in PATTERNS:
            match = pattern.search(line)
            if match:
                ids.append(fixed or match.group(1))
                break
    return ids


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return normalized or "example"


def detect_family(source_ids: list[str]) -> str:
    if "BP02-v4.0" in source_ids:
        return "marigold-v4.0"
    if "BP01" in source_ids or "CHB01" in source_ids:
        return "centurion-1.0"
    return "marigold-v4.2"


def select_footer(family: str, source_ids: list[str]) -> str:
    if family == "marigold-v4.0":
        return "F01"
    if family == "centurion-1.0":
        return "F01"
    if "FM01-v4.2" in source_ids:
        return "F02"
    return "F01"


def map_generic_payload(relative_path: str, source_ids: list[str]) -> dict[str, Any]:
    family = detect_family(source_ids)
    notes: list[str] = []
    unsupported: list[str] = []
    substitutions: list[dict[str, str]] = []
    omissions: list[str] = []
    body: list[str] = []
    noted_substitutions: set[str] = set()

    if family == "marigold-v4.2":
        body_map = MARIGOLD_V42_BODY
        substitution_map = MARIGOLD_V42_SUBSTITUTIONS
    elif family == "marigold-v4.0":
        body_map = MARIGOLD_V40_BODY
        substitution_map = {}
    else:
        body_map = CENTURION_BODY
        substitution_map = CENTURION_SUBSTITUTIONS

    for source_id in source_ids:
        if source_id in SKIP_IDS:
            continue
        if source_id == "CFM01":
            omissions.append(source_id)
            notes.append("El HTML de referencia incluye CFM01 en footer, pero la API actual no lo expone como componente publico separado.")
            continue
        component_id = body_map.get(source_id)
        if component_id:
            body.append(component_id)
            continue
        substitute = substitution_map.get(source_id)
        if substitute:
            body.append(substitute[0])
            substitutions.append({"sourceId": source_id, "componentId": substitute[0]})
            if source_id not in noted_substitutions:
                notes.append(substitute[1])
                noted_substitutions.add(source_id)
            continue
        unsupported.append(source_id)

    payload: dict[str, Any] = {
        "templateFamily": family,
        "header": "H01",
        "body": body,
        "footer": select_footer(family, source_ids),
    }
    fidelity = "estructural"
    if substitutions or unsupported or omissions:
        fidelity = "aproximada"
    if relative_path.endswith("TRAVEL-Miami-Nov25_PLAT/TRAVEL-Miami-Nov25_PLAT.html"):
        notes.append("Este caso mezcla modulos v4.2 con IM02-v4.0 dentro del mismo HTML.")
    if unsupported:
        notes.append(
            "Hay sourceIds del HTML de referencia que todavia no tienen componente publico: "
            + ", ".join(unsupported)
        )
    notes = list(dict.fromkeys(notes))
    return {
        "templateFamily": family,
        "referenceSourceIds": source_ids,
        "payload": payload,
        "fidelity": fidelity,
        "substitutions": substitutions,
        "unsupportedSourceIds": unsupported,
        "notes": notes,
    }


def build_entry(relative_path: str, source_ids: list[str]) -> dict[str, Any]:
    override = EXACT_OVERRIDES.get(relative_path)
    if override:
        payload = {
            "templateFamily": override["templateFamily"],
            "header": override["header"],
            "body": override["body"],
            "footer": override["footer"],
        }
        if override.get("globals"):
            payload["globals"] = override["globals"]
        return {
            "templateFamily": override["templateFamily"],
            "referenceSourceIds": source_ids,
            "payload": payload,
            "fidelity": override["fidelity"],
            "substitutions": [],
            "unsupportedSourceIds": [],
            "notes": override["notes"],
        }
    return map_generic_payload(relative_path, source_ids)


def build_catalog_metadata(entries: list[dict[str, Any]]) -> None:
    seen: dict[str, int] = {}
    for entry in entries:
        base_slug = slugify(entry.get("name", "example"))
        count = seen.get(base_slug, 0) + 1
        seen[base_slug] = count
        entry_id = base_slug if count == 1 else f"{base_slug}-{count}"
        entry["id"] = entry_id
        entry["frontPath"] = f"/example/{entry_id}"
        entry["detailApiPath"] = f"/api/module1/examples/{entry_id}"
        entry["htmlApiPath"] = f"/api/module1/examples/{entry_id}/html"
        entry["coverageLabel"] = FIDELITY_LABELS.get(entry["fidelity"], entry["fidelity"])
        entry["agentSummary"] = (
            f"{entry['name']} | grupo={entry['group']} | familia={entry['templateFamily']} | "
            f"fidelidad={entry['fidelity']} | sourceIds={', '.join(entry['referenceSourceIds']) or 'sin-sourceIds'}"
        )


def load_entries_from_reference_html() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in sorted(REFERENCE_DIR.rglob("*.html")):
        relative_path = str(path.relative_to(ROOT)).replace("\\", "/")
        source_ids = extract_source_ids(path)
        mapped = build_entry(relative_path, source_ids)
        mapped["relativePath"] = relative_path
        mapped["name"] = path.stem
        mapped["group"] = path.relative_to(REFERENCE_DIR).parts[0]
        entries.append(mapped)
    return entries


def load_existing_entries() -> list[dict[str, Any]]:
    if not OUTPUT_JSON.exists():
        return []
    entries = json.loads(OUTPUT_JSON.read_text(encoding="utf-8-sig"))
    return [entry for entry in entries if isinstance(entry, dict)]


def render_markdown(entries: list[dict[str, Any]]) -> str:
    lines = [
        "# Catalogo operativo de payloads para modulo 1",
        "",
        "Este archivo lo genera `scripts/generate_examples.py` y debe mantenerse alineado con el front `/module1`.",
        "La idea es que una persona o un agente puedan mirar este catalogo, abrir la referencia visual en el front y decidir que payload de `compose-email` se parece mas al PDF entrante.",
        "",
        "## Reglas estrictas para el agente",
        "",
        "1. Usar exclusivamente la informacion publicada en este markdown para decidir el payload.",
        "2. No inventar campañas, componentes, headers, bodies ni footers que no aparezcan aqui.",
        "3. No usar memoria previa, conocimiento externo ni ejemplos fuera de este archivo.",
        "4. Si un caso no coincide de forma exacta, elegir el ejemplo mas cercano de este mismo catalogo y reutilizar su payload.",
        "5. Responder siempre con un payload valido de `compose-email` usando solo IDs presentes en este documento.",
        "",
        "## Como usar este catalogo",
        "",
        "1. Extrae del PDF todas las pistas posibles: titulo, rubro, fechas, marcas, estructura visual y textos repetidos.",
        "2. Busca el ejemplo mas cercano por nombre, segmento, `sourceIds`, notas y ruta de referencia.",
        "3. Si el match es fuerte, reutiliza el `payload` publicado aqui.",
        "4. Si no hay match exacto, prioriza ejemplos con la misma `templateFamily` y secuencia estructural parecida.",
        "5. Usa `frontPath` y `htmlApiPath` para contrastar visualmente el HTML de referencia contra el resultado generado.",
        "",
        "## Leyenda",
        "- `alta`: usa un set de componentes especifico del caso dentro del catalogo actual.",
        "- `estructural`: reproduce la familia y el orden general con componentes publicos genericos.",
        "- `aproximada`: ademas de lo anterior, hubo sustituciones o faltan sourceIds publicos.",
        "",
    ]
    current_group = None
    for entry in entries:
        group = entry["group"]
        if group != current_group:
            lines.extend([f"## {group}", ""])
            current_group = group
        lines.append(f"### {entry['name']}")
        lines.append("")
        lines.append(f"- ID estable: `{entry['id']}`")
        lines.append(f"- Estado en front: `{entry['coverageLabel']}`")
        lines.append(f"- Archivo: `{entry['relativePath']}`")
        lines.append(f"- Vista front: `{entry['frontPath']}`")
        lines.append(f"- API detalle: `{entry['detailApiPath']}`")
        lines.append(f"- API HTML: `{entry['htmlApiPath']}`")
        lines.append(f"- Familia: `{entry['templateFamily']}`")
        lines.append(f"- Fidelidad: `{entry['fidelity']}`")
        lines.append(f"- SourceIds de referencia: `{', '.join(entry['referenceSourceIds']) or 'sin-sourceIds'}`")
        lines.append(f"- Resumen para agente: `{entry['agentSummary']}`")
        if entry["unsupportedSourceIds"]:
            lines.append(f"- SourceIds sin componente publico: `{', '.join(entry['unsupportedSourceIds'])}`")
        if entry["substitutions"]:
            substitutions = ", ".join(
                f"{item['sourceId']} -> {item['componentId']}" for item in entry["substitutions"]
            )
            lines.append(f"- Sustituciones aplicadas: `{substitutions}`")
        if entry["notes"]:
            for note in entry["notes"]:
                lines.append(f"- Nota: {note}")
        lines.append("")
        lines.append("Payload requerido para `compose-email`:")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(entry["payload"], indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    entries = load_entries_from_reference_html() if REFERENCE_DIR.exists() else []
    if not entries:
        entries = load_existing_entries()
    if not entries:
        raise SystemExit(
            "No se encontraron HTMLs de referencia ni un catalogo previo en catalog/examples/module1.json."
        )

    build_catalog_metadata(entries)
    OUTPUT_JSON.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(entries), encoding="utf-8")
    print(f"Generated {OUTPUT_JSON}")
    print(f"Generated {OUTPUT_MD}")


if __name__ == "__main__":
    main()
