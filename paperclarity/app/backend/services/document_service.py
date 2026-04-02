from __future__ import annotations

from pathlib import Path

import fitz

from paperclarity.app.backend.models.document import Block, BoundingBox, DocumentModel, Section


class DocumentService:
    def parse_pdf(self, file_path: Path, document_id: str) -> DocumentModel:
        doc = fitz.open(file_path)
        blocks: list[Block] = []
        sections: list[Section] = [Section(id="root", title="Document", level=1, page_start=1, page_end=len(doc))]

        order = 0
        for page_index, page in enumerate(doc, start=1):
            entries = page.get_text("blocks")
            for entry in entries:
                x0, y0, x1, y1, text, *_ = entry
                clean = (text or "").strip()
                if not clean:
                    continue
                order += 1
                block_id = f"b-{page_index}-{order}"
                blocks.append(
                    Block(
                        id=block_id,
                        page=page_index,
                        section_id="root",
                        block_type="paragraph",
                        text=clean,
                        bbox=BoundingBox(x0=x0, y0=y0, x1=x1, y1=y1),
                        order=order,
                    )
                )

        return DocumentModel(
            id=document_id,
            metadata={"filename": file_path.name, "pages": str(len(doc))},
            sections=sections,
            blocks=blocks,
            equations=[],
            figures=[],
            tables=[],
        )
