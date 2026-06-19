"""Pitcher Agent — writes the first-draft pitch for each top opportunity."""
from __future__ import annotations

from typing import Any
import json

from .base import BaseAgent

SYSTEM_PROMPT = """You are an expert copywriter and B2B SaaS founder who writes pitches that
convert without hype. Your pitches are direct, specific, and let the product's value speak for
itself. You never use buzzwords, filler phrases, or vague superlatives. Every sentence earns its
place. You output strictly valid JSON — no prose, no markdown fences.
"""

PITCH_PROMPT = """Write a compelling first-draft pitch for this SaaS opportunity.

Opportunity & analysis:
---
{opportunity_json}
---

The pitch must be structured for a SOLO FOUNDER targeting BUSINESS BUYERS.
It must require zero arm-twisting — the buyer should immediately see "I need this."

Return ONLY this JSON:
{{
  "title": "<product name — crisp, descriptive, no puns>",
  "tagline": "<one sentence, concrete benefit, under 15 words>",
  "problem": "<2–3 sentences: the exact pain, who feels it, quantified if possible>",
  "solution": "<2–3 sentences: what the product does, no jargon>",
  "target_customer": "<specific: company type, size, role who buys and uses>",
  "why_now": "<1–2 sentences: the market or regulatory shift that makes this urgent today>",
  "why_they_buy": "<2 sentences: why a rational buyer agrees without being sold to>",
  "revenue_model": "<pricing structure: e.g. $149/mo per seat, annual contracts only, etc.>",
  "solo_build_plan": "<3–5 bullet strings: key milestones from zero to first paying customer>",
  "unfair_advantage": "<1 sentence: the moat or distribution edge available to an early solo founder>"
}}
"""


class PitcherAgent(BaseAgent):
    SYSTEM_PROMPT = SYSTEM_PROMPT

    def run(self, top_opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Draft a pitch for each opportunity and attach it."""
        results: list[dict[str, Any]] = []

        for opp in top_opportunities:
            print(f"  [Pitcher] Drafting pitch for: {opp.get('title', '?')[:60]}…")
            pitch = self._draft(opp)
            results.append({**opp, "pitch": pitch})

        return results

    def _draft(self, opportunity: dict[str, Any]) -> dict[str, Any]:
        prompt = PITCH_PROMPT.format(
            opportunity_json=json.dumps(opportunity, indent=2)
        )
        try:
            text = self._call(prompt, temperature=0.7)
            return self._parse_json(text)
        except Exception as exc:
            print(f"  [Pitcher] Pitch error for '{opportunity.get('title', '?')}': {exc}")
            return {"error": str(exc)}
