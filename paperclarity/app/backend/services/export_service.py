from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ExportService:
    def export_notes_markdown(self, document_id: str, notes: list[dict[str, Any]]) -> Path:
        out_dir = Path("data/exports")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{document_id}_notes.md"

        lines = [f"# PaperClarity Notes - {document_id}", ""]
        for note in notes:
            lines.append(f"## Note #{note['id']} - {note['skill_name']}")
            lines.append(f"- Created: {note['created_at']}")
            lines.append("```json")
            lines.append(json.dumps(note["content"], ensure_ascii=False, indent=2))
            lines.append("```")
            lines.append("")

        out_file.write_text("\n".join(lines), encoding="utf-8")
        return out_file
