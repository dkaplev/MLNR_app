import os
from dotenv import load_dotenv

load_dotenv()

# LLM provider — "anthropic" or "openai"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "anthropic")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Model names
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-5")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Search API (Tavily)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# Pipeline settings
TOP_OPPORTUNITIES = int(os.getenv("TOP_OPPORTUNITIES", "3"))   # how many to pitch
REFINE_ITERATIONS = int(os.getenv("REFINE_ITERATIONS", "2"))   # critic/refiner loops
REPORTS_DIR = os.getenv("REPORTS_DIR", "reports")

# Scout search themes — extend freely
SCOUT_THEMES = [
    "emerging SaaS tools 2025 2026 small business pain points",
    "new workflow automation problems companies face",
    "AI integration pain points B2B software",
    "developer tooling gaps trending GitHub 2026",
    "compliance automation new regulations software",
    "vertical SaaS underserved industries opportunity",
    "no-code low-code gaps enterprise automation",
    "API integration pain points startup tools",
    "remote team collaboration software gaps",
    "AI agents enterprise adoption friction points",
]

# Scoring weights — must sum to 100
SCORING_WEIGHTS = {
    "solo_buildability": 20,   # Can 1 dev ship MVP in < 3 months?
    "value_clarity": 20,       # Is the ROI to the buyer undeniable?
    "market_timing": 20,       # Demand emerging but not saturated?
    "b2b_monetization": 20,    # Can you charge $100–$500/mo reliably?
    "pull_factor": 20,         # Does the product sell itself (PLG/word-of-mouth)?
}
