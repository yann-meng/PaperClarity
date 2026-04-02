from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from paperclarity.app.backend.models.document import DocumentModel
from paperclarity.app.backend.schemas.skill_context import SkillContext


class BaseSkill(ABC):
    """Base class for all PaperClarity skills."""

    name: str
    display_name: str
    description: str
    supported_contexts: list[str]

    @abstractmethod
    def build_prompt(
        self,
        context: SkillContext,
        document: DocumentModel,
        user_input: str | None = None,
    ) -> str:
        ...

    @abstractmethod
    async def run(
        self,
        context: SkillContext,
        document: DocumentModel,
        llm_client: Any,
        user_input: str | None = None,
    ) -> BaseModel:
        ...

    @abstractmethod
    def output_schema(self) -> type[BaseModel]:
        ...
