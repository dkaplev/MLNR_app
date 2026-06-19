"""Scout Agent — discovers emerging solo SaaS opportunities via web search."""
from __future__ import annotations

import json
from typing import Any

import config
from .base import BaseAgent

SYSTEM_PROMPT = """You are a sharp business analyst specialising in emerging B2B SaaS opportunities.
Your job is to identify REAL, specific, under-served problems that a solo developer could build a
product around. You prioritise:

- Opportunities that are EMERGING (appeared in the last 6–18 months)
- Problems where the buyer immediately understands the value — no pitch needed
- B2B contexts where companies will happily pay $100–$1 000/month
- Problems that a single developer can ship an MVP for in under 3 months

You output strictly valid JSON — no prose, no markdown fences.
"""

EXTRACTION_PROMPT = """Below are raw web search results about: "{theme}"

---
{results}
---

Extract 2–4 concrete, specific SaaS opportunity ideas from this content.
Each idea must be grounded in an ACTUAL pain point mentioned in the results (not invented).

Return a JSON array. Each element:
{{
  "title": "short name for the opportunity",
  "problem": "exact pain point, quoted or paraphrased from results",
  "target_customer": "specific type of business or role affected",
  "signal": "why this is EMERGING now — regulatory, technological, or market shift",
  "source_hint": "brief note on where this signal appeared"
}}

Return ONLY the JSON array. No other text.
"""


class ScoutAgent(BaseAgent):
    SYSTEM_PROMPT = SYSTEM_PROMPT

    def __init__(self) -> None:
        super().__init__()
        self._searcher = _build_searcher()

    def run(self, themes: list[str] | None = None) -> list[dict[str, Any]]:
        """Search all themes and return a deduplicated list of raw opportunities."""
        themes = themes or config.SCOUT_THEMES
        all_opportunities: list[dict[str, Any]] = []

        for theme in themes:
            print(f"  [Scout] Searching: {theme[:60]}…")
            raw_results = self._searcher.search(theme)
            if not raw_results:
                continue
            opportunities = self._extract_opportunities(theme, raw_results)
            all_opportunities.extend(opportunities)

        return self._deduplicate(all_opportunities)

    def _extract_opportunities(self, theme: str, results: str) -> list[dict[str, Any]]:
        prompt = EXTRACTION_PROMPT.format(theme=theme, results=results[:6000])
        try:
            text = self._call(prompt, temperature=0.5)
            return self._parse_json(text)
        except Exception as exc:
            print(f"  [Scout] Parse error for theme '{theme[:40]}': {exc}")
            return []

    def _deduplicate(self, items: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Rough dedup by title similarity — ask LLM to merge near-duplicates."""
        if len(items) <= 5:
            return items

        titles = json.dumps([i.get("title", "") for i in items], indent=2)
        prompt = f"""Here are opportunity titles extracted from multiple searches:
{titles}

Some may be near-duplicates covering the same core idea.
Return a JSON array of 0-based indices to KEEP (remove duplicates, keep the most specific title).
Example: [0, 1, 4, 7, 9]
Return ONLY the JSON array.
"""
        try:
            text = self._call(prompt, temperature=0.0)
            indices: list[int] = self._parse_json(text)
            return [items[i] for i in indices if 0 <= i < len(items)]
        except Exception:
            return items


class _TavilySearcher:
    def __init__(self, api_key: str) -> None:
        from tavily import TavilyClient  # type: ignore
        self._client = TavilyClient(api_key=api_key)

    def search(self, query: str) -> str:
        result = self._client.search(
            query=query,
            search_depth="advanced",
            max_results=8,
            include_answer=True,
        )
        parts: list[str] = []
        if result.get("answer"):
            parts.append(f"SUMMARY: {result['answer']}\n")
        for r in result.get("results", []):
            parts.append(f"SOURCE: {r.get('url', '')}")
            parts.append(f"TITLE: {r.get('title', '')}")
            parts.append(f"CONTENT: {r.get('content', '')[:800]}\n")
        return "\n".join(parts)


class _DummySearcher:
    """Used when no Tavily key is configured — returns placeholder text."""

    DUMMY_RESULTS = {
        "default": """
SOURCE: https://news.ycombinator.com/item?id=123456
TITLE: Ask HN: What B2B software do you desperately wish existed?
CONTENT: Many small logistics companies struggle with automated invoice reconciliation against
carrier APIs. They currently export CSVs and manually match thousands of line items per month.
Even a simple rule-based matcher would save 20+ hours per week per company.

SOURCE: https://www.reddit.com/r/Entrepreneur/comments/abc123
TITLE: The compliance gap nobody is solving
CONTENT: EU AI Act compliance tooling for mid-size SaaS companies is almost non-existent.
Legal teams are scrambling to understand what documentation they need; nobody offers an
automated audit trail generator for AI model decisions.

SOURCE: https://techcrunch.com/2026/05/12/vertical-saas-wave
TITLE: The next wave of vertical SaaS is boring — and that's the point
CONTENT: Niches like dental supply ordering, HVAC service dispatch, and independent pharmacy
inventory are still being managed in Excel. Founders who can tolerate mundane domains are
capturing high-NPS, low-churn revenue that tech-adjacent founders overlook.
"""
    }

    def search(self, query: str) -> str:
        return self.DUMMY_RESULTS.get("default", "")


def _build_searcher() -> _TavilySearcher | _DummySearcher:
    if config.TAVILY_API_KEY:
        return _TavilySearcher(config.TAVILY_API_KEY)
    print("  [Scout] No TAVILY_API_KEY — using dummy search results for demo.")
    return _DummySearcher()
