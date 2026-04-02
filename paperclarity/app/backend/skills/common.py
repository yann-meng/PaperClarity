from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel

from paperclarity.app.backend.core.base_skill import BaseSkill
from paperclarity.app.backend.models.document import DocumentModel
from paperclarity.app.backend.schemas.skill_context import SkillContext


class GenericSkill(BaseSkill):
    prompt_filename = "prompt.txt"
    schema_model: type[BaseModel]

    def prompt_template(self) -> str:
        path = Path(__file__).parent / self.name / self.prompt_filename
        return path.read_text(encoding="utf-8")

    def build_prompt(self, context: SkillContext, document: DocumentModel, user_input: str | None = None) -> str:
        selected_blocks = [b for b in document.blocks if b.id in set(context.selected_block_ids)]
        selected_text = "\n\n".join(f"[p{b.page}#{b.id}] {b.text}" for b in selected_blocks) or "(none selected)"
        paper_excerpt = "\n".join(f"[p{b.page}] {b.text}" for b in document.blocks[:30])
        return self.prompt_template().format(
            metadata=document.metadata,
            context_type=context.context_type,
            selected_text=selected_text,
            selected_equation_id=context.selected_equation_id,
            user_input=user_input or "",
            paper_excerpt=paper_excerpt,
            extra_context=context.extra_context,
        )

    async def run(self, context: SkillContext, document: DocumentModel, llm_client: Any, user_input: str | None = None) -> BaseModel:
        prompt = self.build_prompt(context, document, user_input)
        payload = await llm_client.generate_json(prompt, schema_hint=self.output_schema().model_json_schema())
        return self.output_schema().model_validate(payload)

    def output_schema(self) -> type[BaseModel]:
        return self.schema_model
