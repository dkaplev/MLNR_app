"""Pipeline orchestrator — runs the full Scout → Analyse → Pitch → Critique → Refine → Report cycle."""
from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any

import config
from agents import AnalystAgent, CriticAgent, PitcherAgent, RefinerAgent, ScoutAgent


class SaaSOpportunityPipeline:
    """End-to-end pipeline. Call `run()` to execute one full cycle."""

    def run(self, themes: list[str] | None = None) -> str:
        """Execute the full pipeline and return the path to the saved report."""
        date_tag = datetime.now().strftime("%Y-%m-%d")
        print(f"\n{'='*60}")
        print(f"  SaaS Opportunity Pipeline — {date_tag}")
        print(f"{'='*60}\n")

        # Stage 1: Scout
        print("[Stage 1/5] Scouting emerging opportunities…")
        scout = ScoutAgent()
        raw_opportunities = scout.run(themes)
        print(f"  Found {len(raw_opportunities)} raw opportunities.\n")

        if not raw_opportunities:
            print("No opportunities found. Check your API keys and search themes.")
            return ""

        # Stage 2: Analyse & rank
        print("[Stage 2/5] Analysing and scoring…")
        analyst = AnalystAgent()
        top_opportunities = analyst.run(raw_opportunities)
        print()

        # Stage 3: Initial pitch
        print("[Stage 3/5] Drafting initial pitches…")
        pitcher = PitcherAgent()
        pitched = pitcher.run(top_opportunities)
        print()

        # Stage 4 + 5: Critic ↔ Refiner loop
        print(f"[Stage 4+5/5] Critic/Refiner loop ({config.REFINE_ITERATIONS} iterations)…")
        refiner = RefinerAgent()
        final_opportunities = refiner.run(pitched)
        print()

        # Compile report
        report_path = self._compile_report(final_opportunities, date_tag)
        print(f"\n{'='*60}")
        print(f"  Report saved → {report_path}")
        print(f"{'='*60}\n")
        return report_path

    # ------------------------------------------------------------------
    # Report compilation
    # ------------------------------------------------------------------

    def _compile_report(self, opportunities: list[dict[str, Any]], date_tag: str) -> str:
        os.makedirs(config.REPORTS_DIR, exist_ok=True)
        report_md = self._render_markdown(opportunities, date_tag)
        report_json = json.dumps(opportunities, indent=2)

        md_path = os.path.join(config.REPORTS_DIR, f"report_{date_tag}.md")
        json_path = os.path.join(config.REPORTS_DIR, f"report_{date_tag}.json")

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(report_md)
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(report_json)

        return md_path

    def _render_markdown(self, opportunities: list[dict[str, Any]], date_tag: str) -> str:
        lines: list[str] = [
            f"# Solo SaaS Opportunity Report — {date_tag}",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ",
            f"**Opportunities evaluated:** {len(opportunities)}  ",
            f"**Refinement iterations:** {config.REFINE_ITERATIONS}",
            "",
            "---",
            "",
        ]

        for rank, opp in enumerate(opportunities, start=1):
            pitch: dict[str, Any] = opp.get("pitch", {})
            analysis: dict[str, Any] = opp.get("analysis", {})
            critiques: list[dict[str, Any]] = opp.get("critiques", [])
            scores: dict[str, int] = analysis.get("scores", {})
            total: int = analysis.get("total", 0)

            lines += [
                f"## #{rank} — {pitch.get('title', opp.get('title', 'Untitled'))}",
                "",
                f"> {pitch.get('tagline', '')}",
                "",
                f"**Score:** {total}/100",
                "",
            ]

            # Score breakdown
            if scores:
                lines += ["### Score breakdown", ""]
                for dim, weight in config.SCORING_WEIGHTS.items():
                    s = scores.get(dim, 0)
                    bar = "█" * s + "░" * (weight - s)
                    lines.append(f"- **{dim.replace('_', ' ').title()}** `{s}/{weight}` {bar}")
                lines.append("")

            # Strengths / risks from analyst
            if analysis.get("strengths"):
                lines += ["**Strengths:**", ""]
                for st in analysis["strengths"]:
                    lines.append(f"- {st}")
                lines.append("")
            if analysis.get("risks"):
                lines += ["**Risks:**", ""]
                for r in analysis["risks"]:
                    lines.append(f"- {r}")
                lines.append("")

            # Core pitch
            lines += [
                "### The Pitch",
                "",
                f"**Problem:** {pitch.get('problem', '')}",
                "",
                f"**Solution:** {pitch.get('solution', '')}",
                "",
                f"**Target customer:** {pitch.get('target_customer', '')}",
                "",
                f"**Why now:** {pitch.get('why_now', '')}",
                "",
                f"**Why they buy without being sold to:** {pitch.get('why_they_buy', '')}",
                "",
                f"**Revenue model:** {pitch.get('revenue_model', '')}",
                "",
                f"**Unfair advantage:** {pitch.get('unfair_advantage', '')}",
                "",
            ]

            # Build plan
            build_plan = pitch.get("solo_build_plan", [])
            if build_plan:
                lines += ["### Solo Build Plan", ""]
                for step in build_plan:
                    lines.append(f"1. {step}")
                lines.append("")

            # Critique summary (last iteration)
            if critiques:
                last = critiques[-1]
                lines += [
                    "### Critic's Final Notes",
                    "",
                    f"**Rating after refinement:** {last.get('overall_rating', '?')}/10",
                    "",
                ]
                if last.get("strongest_part"):
                    lines.append(f"**Strongest part:** {last['strongest_part']}")
                    lines.append("")
                if last.get("single_most_important_fix"):
                    lines.append(
                        f"**Remaining open question:** {last['single_most_important_fix']}"
                    )
                    lines.append("")

            lines += ["---", ""]

        lines += [
            "## Methodology",
            "",
            "1. **Scout** — web searches across emerging tech, business, and regulatory themes",
            "2. **Analyst** — scores each opportunity on solo-buildability, value clarity,",
            "   market timing, B2B monetisation, and pull factor",
            f"3. **Pitcher** — drafts a structured pitch for the top {config.TOP_OPPORTUNITIES} ideas",
            f"4. **Critic / Refiner** — {config.REFINE_ITERATIONS} rounds of critique and refinement",
            "",
        ]
        return "\n".join(lines)
