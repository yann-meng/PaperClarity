from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class BoundingBox(BaseModel):
    x0: float
    y0: float
    x1: float
    y1: float


class Block(BaseModel):
    id: str
    page: int
    section_id: str | None = None
    block_type: Literal["paragraph", "equation", "figure", "table", "title", "caption"]
    text: str
    bbox: BoundingBox | None = None
    order: int


class Section(BaseModel):
    id: str
    title: str
    level: int = 1
    page_start: int | None = None
    page_end: int | None = None


class Equation(BaseModel):
    id: str
    page: int
    latex: str | None = None
    text: str | None = None
    block_id: str | None = None


class Figure(BaseModel):
    id: str
    page: int
    caption: str | None = None
    block_id: str | None = None


class Table(BaseModel):
    id: str
    page: int
    caption: str | None = None
    block_id: str | None = None


class DocumentModel(BaseModel):
    id: str
    metadata: dict[str, str] = Field(default_factory=dict)
    sections: list[Section] = Field(default_factory=list)
    blocks: list[Block] = Field(default_factory=list)
    equations: list[Equation] = Field(default_factory=list)
    figures: list[Figure] = Field(default_factory=list)
    tables: list[Table] = Field(default_factory=list)
