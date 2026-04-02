from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

from paperclarity.app.backend.core.base_skill import BaseSkill


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, BaseSkill] = {}

    def load_skills(self, package: str = "paperclarity.app.backend.skills") -> None:
        module = importlib.import_module(package)
        package_path = Path(module.__file__).parent

        for mod in pkgutil.iter_modules([str(package_path)]):
            if not mod.ispkg:
                continue
            skill_module = importlib.import_module(f"{package}.{mod.name}.skill")
            for obj in skill_module.__dict__.values():
                if isinstance(obj, type) and issubclass(obj, BaseSkill) and obj is not BaseSkill:
                    skill: BaseSkill = obj()
                    self._skills[skill.name] = skill

    def get(self, skill_name: str) -> BaseSkill:
        if skill_name not in self._skills:
            raise KeyError(f"Skill not found: {skill_name}")
        return self._skills[skill_name]

    def list(self) -> list[dict[str, object]]:
        return [
            {
                "name": skill.name,
                "display_name": skill.display_name,
                "description": skill.description,
                "supported_contexts": skill.supported_contexts,
                "output_schema": skill.output_schema().model_json_schema(),
            }
            for skill in self._skills.values()
        ]
