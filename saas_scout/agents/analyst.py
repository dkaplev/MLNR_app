"""Analyst Agent — scores each opportunity and selects the top N."""
from __future__ import annotations

import json
from typing import Any

import config
from .base import BaseAgent

SYSTEM_PROMPT = """You are a razor-sharp SaaS business analyst evaluating ideas for a solo founder.
You score ideas with brutal honesty. A high score means: real pain, obvious value, no complex sales
cycle, and a realistic solo build. You output strictly valid JSON — no prose, no markdown fences.
"""

SCORING_PROMPT = """Evaluate this SaaS opportunity for a solo founder:

---
{opportunity_json}
---

Score it across FIVE dimensions (each 0–20, total max 100):

1. solo_buildability  — Can ONE developer ship a useful MVP in < 3 months?
   (20 = yes easily; 0 = requires a team or years of work)

2. value_clarity      — Is the ROI to the buyer immediately obvious without explanation?
   (20 = buyer sees it in 30 seconds; 0 = requires a complex sales pitch)

3. market_timing      — Is demand clearly emerging NOW but the space is not yet crowded?
   (20 = perfect timing; 0 = too early or already saturated)

4. b2b_monetization   — Can this realistically charge $100–$1 000/month per customer?
   (20 = obvious pricing; 0 = consumer-only or race-to-zero pricing)

5. pull_factor        — Will satisfied customers tell others or will it spread organically?
   (20 = strong PLG/word-of-mouth; 0 = needs heavy outbound to grow)

Also provide:
- "strengths": top 2–3 genuine strengths as a list of strings
- "risks": top 2–3 honest risks as a list of strings
- "verdict": one sentence buy/pass recommendation

Return ONLY this JSON:
{{
  "title": "<same title as input>",
  "scores": {{
    "solo_buildability": <int>,
    "value_clarity": <int>,
    "market_timing": <int>,
    "b2b_monetization": <int>,
    "pull_factor": <int>
  }},
  "total": <sum of scores>,
  "strengths": ["...", "..."],
  "risks": ["...", "..."],
  "verdict": "..."
}}
"""


class AnalystAgent(BaseAgent):
    SYSTEM_PROMPT = SYSTEM_PROMPT

    def run(self, opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Score all opportunities and return the top N, richest first."""
        scored: list[dict[str, Any]] = []

        for opp in opportunities:
            print(f"  [Analyst] Scoring: {opp.get('title', '?')[:60]}…")
            analysis = self._score(opp)
            if analysis:
                combined = {**opp, "analysis": analysis}
                scored.append(combined)

        scored.sort(key=lambda x: x.get("analysis", {}).get("total", 0), reverse=True)
        top = scored[: config.TOP_OPPORTUNITIES]

        print(f"  [Analyst] Top {len(top)} selected out of {len(scored)} scored.")
        return top

    def _score(self, opportunity: dict[str, Any]) -> dict[str, Any] | None:
        prompt = SCORING_PROMPT.format(
            opportunity_json=json.dumps(opportunity, indent=2)
        )
        try:
            text = self._call(prompt, temperature=0.3)
            return self._parse_json(text)
        except Exception as exc:
            print(f"  [Analyst] Scoring error for '{opportunity.get('title', '?')}': {exc}")
            return None
