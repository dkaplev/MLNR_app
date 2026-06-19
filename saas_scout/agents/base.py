"""Base class shared by all agents."""
from __future__ import annotations

import json
import re
from typing import Any

import config


class BaseAgent:
    """Thin wrapper around the configured LLM provider."""

    SYSTEM_PROMPT = "You are a helpful assistant."

    def __init__(self) -> None:
        self._client = _build_client()

    def _call(self, prompt: str, system: str | None = None, temperature: float = 0.7) -> str:
        sys = system or self.SYSTEM_PROMPT
        if config.LLM_PROVIDER == "anthropic":
            import anthropic  # type: ignore
            response = self._client.messages.create(
                model=config.ANTHROPIC_MODEL,
                max_tokens=4096,
                temperature=temperature,
                system=sys,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        else:
            response = self._client.chat.completions.create(
                model=config.OPENAI_MODEL,
                temperature=temperature,
                messages=[
                    {"role": "system", "content": sys},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content or ""

    def _parse_json(self, text: str) -> Any:
        """Extract JSON from the model output (handles markdown fences)."""
        cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.MULTILINE)
        cleaned = re.sub(r"\s*```$", "", cleaned, flags=re.MULTILINE)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # Try to extract a JSON array or object from the text
            match = re.search(r"(\[.*\]|\{.*\})", cleaned, re.DOTALL)
            if match:
                return json.loads(match.group(1))
            raise


def _build_client() -> Any:
    if config.LLM_PROVIDER == "anthropic":
        import anthropic  # type: ignore
        return anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    else:
        import openai  # type: ignore
        return openai.OpenAI(api_key=config.OPENAI_API_KEY)
