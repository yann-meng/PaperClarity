from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse

from paperclarity.app.backend.core.skill_registry import SkillRegistry
from paperclarity.app.backend.db.database import Database
from paperclarity.app.backend.models.document import DocumentModel
from paperclarity.app.backend.schemas.skill_context import SkillContext
from paperclarity.app.backend.services.document_service import DocumentService
from paperclarity.app.backend.services.export_service import ExportService
from paperclarity.app.backend.services.llm_gateway import LLMGateway

router = APIRouter()
db = Database()
doc_service = DocumentService()
llm_gateway = LLMGateway()
export_service = ExportService()
registry = SkillRegistry()
registry.load_skills()


@router.get("/health", response_class=PlainTextResponse)
async def health() -> str:
    return "ok"


@router.get("/skills")
async def list_skills() -> list[dict[str, object]]:
    return registry.list()


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)) -> dict[str, str]:
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported for MVP")

    document_id = str(uuid.uuid4())
    save_path = Path("data") / f"{document_id}.pdf"
    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_bytes(await file.read())

    document = doc_service.parse_pdf(save_path, document_id)
    db.save_document(document_id, document.model_dump())
    return {"document_id": document_id}


@router.get("/documents/{document_id}")
async def get_document(document_id: str) -> dict:
    raw = db.get_document(document_id)
    if not raw:
        raise HTTPException(status_code=404, detail="Document not found")
    return raw


@router.post("/skills/{skill_name}/run")
async def run_skill(skill_name: str, context: SkillContext, user_input: str | None = None) -> dict:
    raw = db.get_document(context.document_id)
    if not raw:
        raise HTTPException(status_code=404, detail="Document not found")

    skill = registry.get(skill_name)
    document = DocumentModel.model_validate(raw)
    result = await skill.run(context=context, document=document, llm_client=llm_gateway, user_input=user_input)
    note_id = db.save_note(context.document_id, skill_name, result.model_dump())
    return {"note_id": note_id, "skill": skill_name, "result": result.model_dump()}


@router.get("/documents/{document_id}/notes")
async def list_notes(document_id: str) -> list[dict]:
    return db.list_notes(document_id)


@router.post("/documents/{document_id}/export_markdown")
async def export_notes(document_id: str) -> dict[str, str]:
    notes = db.list_notes(document_id)
    out = export_service.export_notes_markdown(document_id, notes)
    return {"path": str(out)}
