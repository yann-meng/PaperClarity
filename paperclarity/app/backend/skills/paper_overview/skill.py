from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class PaperOverviewOutput(BaseModel):
    one_sentence_summary: str
    problem_definition: str
    core_method: str
    key_mechanisms: list[str]
    experiment_conclusions: list[str]
    strengths: list[str]
    limitations: list[str]
    reproduction_hints: list[str]


class PaperOverviewSkill(GenericSkill):
    name = "paper_overview"
    display_name = "整篇论文理解"
    description = "快速结构化总结论文核心内容。"
    supported_contexts = ["paper"]
    schema_model = PaperOverviewOutput
