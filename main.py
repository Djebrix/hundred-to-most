"""Entry for the-plan-make-fun-will-carry-20261122-2138.

Writes a single 279-code-point plan to <output dir>/entry.txt.
Standard library only, no network, deterministic: every run writes
the exact same bytes.
"""

import os

PLAN = (
    "Day 1: open a Fiverr gig selling $25 AI product photos for Etsy "
    "sellers, promoted in Etsy forums and r/Etsy. Deliver 5 photos per "
    "order in an hour with free AI tools. Reinvest the first $100 earned "
    "into promoted gigs. Likely 2-4 orders a day by day 10: about "
    "$500-$900 by day 30."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
