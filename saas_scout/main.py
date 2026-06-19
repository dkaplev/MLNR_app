"""Entry point — run the full SaaS Opportunity Pipeline."""
import argparse
import sys
import os

# Allow running from the saas_scout directory or from the project root
sys.path.insert(0, os.path.dirname(__file__))

from pipeline import SaaSOpportunityPipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Weekly solo SaaS opportunity finder pipeline.",
    )
    parser.add_argument(
        "--themes",
        nargs="*",
        help="Override the default search themes (space-separated strings).",
    )
    parser.add_argument(
        "--report-dir",
        default=None,
        help="Override the reports output directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.report_dir:
        import config
        config.REPORTS_DIR = args.report_dir

    pipeline = SaaSOpportunityPipeline()
    report_path = pipeline.run(themes=args.themes or None)

    if report_path:
        print(f"\nDone. Open your report:\n  {os.path.abspath(report_path)}\n")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
