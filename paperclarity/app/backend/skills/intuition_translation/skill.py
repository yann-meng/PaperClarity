from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class IntuitionTranslationOutput(BaseModel):
    one_line_intuition: str
    encourages_or_suppresses: str
    parameter_sensitivity: list[str]
    design_rationale: str


class IntuitionTranslationSkill(GenericSkill):
    name = "intuition_translation"
    display_name = "公式→直觉转换"
    description = "把数学表达转化成易理解的直觉解释。"
    supported_contexts = ["equation", "paragraph"]
    schema_model = IntuitionTranslationOutput
