"""Helpers to extract tracked snippets from local HTML catalogs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ExtractionSpec:
    source_file: Path
    start_marker: str
    end_marker: str
    output_file: Path


def extract_between_markers(source_text: str, start_marker: str, end_marker: str) -> str:
    start_index = source_text.find(start_marker)
    if start_index == -1:
        raise ValueError(f"Start marker not found: {start_marker}")
    end_index = source_text.find(end_marker, start_index)
    if end_index == -1:
        raise ValueError(f"End marker not found: {end_marker}")
    end_index += len(end_marker)
    return source_text[start_index:end_index].strip() + "\n"


def write_extracted_snippet(spec: ExtractionSpec) -> Path:
    source_text = spec.source_file.read_text(encoding="utf-8")
    snippet = extract_between_markers(source_text, spec.start_marker, spec.end_marker)
    spec.output_file.parent.mkdir(parents=True, exist_ok=True)
    spec.output_file.write_text(snippet, encoding="utf-8")
    return spec.output_file
