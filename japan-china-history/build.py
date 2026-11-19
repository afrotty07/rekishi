#!/usr/bin/env python3
"""Rebuild the standalone interactive timeline and CSV using events.json."""
from __future__ import annotations
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
events = json.loads((BASE / "events.json").read_text(encoding="utf-8"))
template = (BASE / "template.html").read_text(encoding="utf-8")
if "__EVENTS__" not in template:
    raise ValueError("Missing __EVENTS__ placeholder in template.html")
html = template.replace("__EVENTS__", json.dumps(events, ensure_ascii=False, separators=(",", ":")))
(BASE / "index.html").write_text(html, encoding="utf-8")

with (BASE / "timeline.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["時代", "年代", "中国の王朝・政権", "テーマ", "重要度", "出来事", "概要", "入試ポイント", "関連語"])
    for e in events:
        writer.writerow([e["era"], e["year"], e["dynasty"], e["theme"], "★" * e["level"], e["title"], e["summary"], e["point"], e["terms"]])
print(f"Built {len(events)} events")
