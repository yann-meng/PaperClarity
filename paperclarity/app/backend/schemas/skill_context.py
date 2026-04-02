from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class SkillContext(BaseModel):
    document_id: str
    context_type: Literal["paper", "section", "paragraph", "equation"]
    selected_block_ids: list[str] = Field(default_factory=list)
    selected_equation_id: str | None = None
    extra_context: dict[str, Any] = Field(default_factory=dict)
