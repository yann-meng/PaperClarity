from __future__ import annotations

import json
import os
from typing import Any

import httpx


class LLMGateway:
    """OpenAI-compatible gateway with pluggable endpoint/model."""

    def __init__(self, base_url: str | None = None, api_key: str | None = None, model: str | None = None):
        self.base_url = base_url or os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
        self.api_key = api_key or os.getenv("LLM_API_KEY", "")
        self.model = model or os.getenv("LLM_MODEL", "gpt-4o-mini")

    async def generate_json(self, prompt: str, schema_hint: dict[str, Any] | None = None) -> dict[str, Any]:
        if not self.api_key:
            return {
                "mock": True,
                "message": "LLM_API_KEY is not configured, returning mock response.",
                "prompt_preview": prompt[:280],
                "schema_hint": schema_hint or {},
            }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a precise research-paper analysis engine."},
                {"role": "user", "content": prompt},
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.2,
        }

        async with httpx.AsyncClient(timeout=90) as client:
            response = await client.post(
                f"{self.base_url.rstrip('/')}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

        content = data["choices"][0]["message"]["content"]
        return json.loads(content)
