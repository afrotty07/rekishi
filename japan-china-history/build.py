#!/usr/bin/env python3
"""Build comparative Japan foreign relations timeline (137+69+48+44+63 records)."""
from pathlib import Path
import csv
import json

base=Path(__file__).resolve().parent
sources=[("cn","events.json"),("kr","events-kr.json"),("ru","events-ru.json"),("uk","events-uk.json"),("us","events-us.json")]
names={"cn":"日中","kr":"日朝・日韓","ru":"日露・日ソ","uk":"日英","us":"日米"}
all_events=[]
for code, filename in sources:
    records=json.loads((base / filename).read_text(encoding="utf-8"))
    for i,record in enumerate(records):
        all_events.append({**record,"relation":code,"id":f"{code}-{i}"})
template=(base/"template.html").read_text(encoding="utf-8")
if "__EVENTS__" not in template:
    raise ValueError("Placeholder __EVENTS__ not found")
output=template.replace("__EVENTS__", json.dumps(all_events, ensure_ascii=False, separators=(",",":")))
(base/"index.html").write_text(output, encoding="utf-8")
with (base/"timeline.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["関係史","時代","年代","相手国・政権","分野","重要度","出来事","概要","入試ポイント","関連語"])
    for e in sorted(all_events, key=lambda x:x["order"]):
        writer.writerow([names[e["relation"]],e["era"],e["year"],e["dynasty"],e["theme"],"★"*e["level"],e["title"],e["summary"],e["point"],e["terms"]])
print(f"Built {len(all_events)} timeline events")
