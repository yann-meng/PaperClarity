from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class EquationBreakdownOutput(BaseModel):
    symbol_table: list[str]
    term_meanings: list[str]
    overall_purpose: str
    mathematical_role: str


class EquationBreakdownSkill(GenericSkill):
    name = "equation_breakdown"
    display_name = "公式逐项拆解"
    description = "将公式按符号和项进行解释。"
    supported_contexts = ["equation", "paragraph"]
    schema_model = EquationBreakdownOutput
