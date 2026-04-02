from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class ExperimentAnalysisOutput(BaseModel):
    validated_claims: list[str]
    metric_quality: str
    baseline_coverage: str
    ablation_validity: str
    potential_issues: list[str]
    reviewer_followups: list[str]


class ExperimentAnalysisSkill(GenericSkill):
    name = "experiment_analysis"
    display_name = "实验分析"
    description = "评估实验设计是否支撑论文主张。"
    supported_contexts = ["section", "paper", "paragraph"]
    schema_model = ExperimentAnalysisOutput
