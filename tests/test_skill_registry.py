from paperclarity.app.backend.core.skill_registry import SkillRegistry


def test_skill_registry_loads_default_skills() -> None:
    registry = SkillRegistry()
    registry.load_skills()

    names = {item["name"] for item in registry.list()}
    assert {
        "paper_overview",
        "paragraph_close_reading",
        "equation_breakdown",
        "intuition_translation",
        "experiment_analysis",
        "reproduction_guide",
    }.issubset(names)
