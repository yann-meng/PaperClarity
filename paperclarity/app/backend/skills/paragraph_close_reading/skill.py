from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class ParagraphCloseReadingOutput(BaseModel):
    plain_restatement: str
    sentence_by_sentence: list[str]
    terminology: list[str]
    role_in_paper: str
    implicit_assumptions: list[str]


class ParagraphCloseReadingSkill(GenericSkill):
    name = "paragraph_close_reading"
    display_name = "段落精读"
    description = "针对选中段落进行逐句解释与假设挖掘。"
    supported_contexts = ["paragraph", "section"]
    schema_model = ParagraphCloseReadingOutput
