"""Refiner Agent — improves each pitch based on critic feedback."""
from __future__ import annotations

import json
from typing import Any

import config
from .base import BaseAgent
from .critic import CriticAgent

SYSTEM_PROMPT = """You are a master B2B copywriter and SaaS strategist. You receive a pitch and
the critic's feedback, and you produce a tighter, more honest, more compelling version.
You fix every critical issue, address every minor issue where possible, and you never add fluff.
You output strictly valid JSON — no prose, no markdown fences.
"""

REFINE_PROMPT = """Improve this pitch based on the critic's feedback below.

Current pitch:
---
{pitch_json}
---

Critic feedback (iteration {iteration}):
---
{critique_json}
---

Rules:
- Fix every "critical_issue" the critic identified.
- Address "minor_issues" where possible without adding bloat.
- Directly acknowledge missed competitors in the "unfair_advantage" or "why_they_buy" fields.
- Keep the same JSON structure as the original pitch.
- Make every sentence earn its place. Delete anything that doesn't add concrete value.

Return ONLY the improved pitch JSON with the SAME keys as the original pitch.
"""


class RefinerAgent(BaseAgent):
    SYSTEM_PROMPT = SYSTEM_PROMPT

    def run(self, opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Run N iterations of critic → refine for each opportunity."""
        critic = CriticAgent()
        current = opportunities

        for iteration in range(1, config.REFINE_ITERATIONS + 1):
            print(f"\n  --- Refine iteration {iteration}/{config.REFINE_ITERATIONS} ---")
            critiqued = critic.run(current, iteration=iteration)
            current = self._refine_all(critiqued, iteration)

        return current

    def _refine_all(self, opportunities: list[dict[str, Any]], iteration: int) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for opp in opportunities:
            title = opp.get("pitch", {}).get("title") or opp.get("title", "?")
            print(f"  [Refiner] Refining (iter {iteration}): {title[:60]}…")
            last_critique = opp.get("critiques", [{}])[-1]
            refined_pitch = self._refine(opp.get("pitch", {}), last_critique, iteration)
            results.append({**opp, "pitch": refined_pitch})
        return results

    def _refine(
        self,
        pitch: dict[str, Any],
        critique: dict[str, Any],
        iteration: int,
    ) -> dict[str, Any]:
        prompt = REFINE_PROMPT.format(
            pitch_json=json.dumps(pitch, indent=2),
            critique_json=json.dumps(critique, indent=2),
            iteration=iteration,
        )
        try:
            text = self._call(prompt, temperature=0.6)
            return self._parse_json(text)
        except Exception as exc:
            print(f"  [Refiner] Error: {exc}")
            return pitch  # fall back to previous version
