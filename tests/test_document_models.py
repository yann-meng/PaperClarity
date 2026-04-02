from paperclarity.app.backend.models.document import Block, BoundingBox, DocumentModel


def test_document_model_minimal() -> None:
    document = DocumentModel(id="doc-1")
    block = Block(
        id="b1",
        page=1,
        section_id="s1",
        block_type="paragraph",
        text="hello",
        bbox=BoundingBox(x0=0, y0=0, x1=10, y1=10),
        order=1,
    )
    document.blocks.append(block)
    assert document.blocks[0].id == "b1"
