"""Critic Agent — stress-tests each pitch, finds holes, missed competitors."""
from __future__ import annotations

import json
from typing import Any

from .base import BaseAgent

SYSTEM_PROMPT = """You are a cynical but constructive venture critic and experienced SaaS founder.
Your job is to find every hole in a pitch BEFORE the founder wastes months building the wrong thing.
You are not trying to kill the idea — you want to make it bulletproof.
You output strictly valid JSON — no prose, no markdown fences.
"""

CRITIQUE_PROMPT = """Critique this SaaS pitch with the goal of making it sharper and more honest.

Pitch (iteration {iteration}):
---
{pitch_json}
---

Identify weaknesses across these dimensions:

1. Is the target customer too broad or too narrow?
2. Are there obvious competitors the pitch ignores?
3. Are the pricing assumptions realistic?
4. Is the "no-sell" claim (value clarity) actually valid, or does it need education?
5. Is the solo build plan realistic, or is it underestimating complexity?
6. Is the "why now" signal strong enough, or is it vague?
7. Is there a fundamental reason this business wouldn't work?

Return ONLY this JSON:
{{
  "iteration": {iteration},
  "overall_rating": <int 1–10, 10 = nearly perfect>,
  "critical_issues": ["<issue>", "..."],
  "minor_issues": ["<issue>", "..."],
  "missed_competitors": ["<competitor name + why it matters>", "..."],
  "strongest_part": "<what works best in the current pitch>",
  "single_most_important_fix": "<the ONE change that would most improve this pitch>"
}}
"""


class CriticAgent(BaseAgent):
    SYSTEM_PROMPT = SYSTEM_PROMPT

    def run(self, pitched_opportunities: list[dict[str, Any]], iteration: int = 1) -> list[dict[str, Any]]:
        """Add a critique to each pitched opportunity."""
        results: list[dict[str, Any]] = []

        for opp in pitched_opportunities:
            title = opp.get("pitch", {}).get("title") or opp.get("title", "?")
            print(f"  [Critic] Reviewing (iter {iteration}): {title[:60]}…")
            critique = self._critique(opp.get("pitch", {}), iteration)
            critiques = list(opp.get("critiques", []))
            critiques.append(critique)
            results.append({**opp, "critiques": critiques})

        return results

    def _critique(self, pitch: dict[str, Any], iteration: int) -> dict[str, Any]:
        prompt = CRITIQUE_PROMPT.format(
            pitch_json=json.dumps(pitch, indent=2),
            iteration=iteration,
        )
        try:
            text = self._call(prompt, temperature=0.5)
            return self._parse_json(text)
        except Exception as exc:
            print(f"  [Critic] Error: {exc}")
            return {"error": str(exc), "iteration": iteration}
