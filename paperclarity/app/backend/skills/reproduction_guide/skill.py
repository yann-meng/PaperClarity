from pydantic import BaseModel

from paperclarity.app.backend.skills.common import GenericSkill


class ReproductionGuideOutput(BaseModel):
    task_definition: str
    input_output: str
    environment_setup: list[str]
    data_preparation: list[str]
    model_architecture: str
    training_pipeline: list[str]
    inference_pipeline: list[str]
    hyperparameters: list[str]
    uncertainties: list[str]
    checklist: list[str]


class ReproductionGuideSkill(GenericSkill):
    name = "reproduction_guide"
    display_name = "复现指南"
    description = "产出可执行的复现操作手册。"
    supported_contexts = ["paper", "section"]
    schema_model = ReproductionGuideOutput
