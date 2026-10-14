#!/usr/bin/env python3
"""Rebuilds corrections.json, and records who approved a reviewed correction.

corrections/<id>.json is the source of truth; corrections.json is the single
file the site fetches, because a browser cannot fetch 7592 little files. It is
rebuilt here rather than in a correction's pull request, so that two pending
pull requests on different notices never conflict over the aggregate.

Run after a correction pull request is merged (APPROVER, ISSUE_NUM and PR_NUM
set): the record that came from that issue is stamped with the reviewer who
merged it. Run without them, it only rebuilds the aggregate.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

CORRECTIONS = Path("corrections")
AGGREGATE = Path("corrections.json")


def write_aggregate() -> None:
    agg = {}
    for f in sorted(CORRECTIONS.glob("*.json")):
        agg[f.stem] = json.loads(f.read_text(encoding="utf-8"))
    AGGREGATE.write_text(json.dumps(agg, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                         encoding="utf-8")


def stamp_approval(approver: str, issue: int, pr: int) -> list[str]:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    stamped = []
    for f in sorted(CORRECTIONS.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        if rec.get("source_issue") != issue or rec.get("approved_in") == pr:
            continue
        rec.update(approved_by=approver, approved_at=now, approved_in=pr)
        f.write_text(json.dumps(rec, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                     encoding="utf-8")
        stamped.append(f.stem)
    return stamped


def main() -> int:
    approver = os.environ.get("APPROVER")
    issue, pr = os.environ.get("ISSUE_NUM", ""), os.environ.get("PR_NUM", "")
    if approver and issue.isdigit() and pr.isdigit():
        stamped = stamp_approval(approver, int(issue), int(pr))
        print(f"approved by {approver}: {', '.join(stamped) or 'no record from #' + issue}")
    write_aggregate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
