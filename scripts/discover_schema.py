from pathlib import Path

from collections import Counter

import json

fields = set()

replay = Path("replay/raw/honeypot-replay.jsonl")

with replay.open() as infile:
    for line in infile:
        event = json.loads(line)
        fields.update(event.keys())

print("\nReplay fields:\n")

for field in sorted(fields):
    print(field)


missing = Counter()

...

for key in fields:
    if event.get(key) in ("", None):
        missing[key] += 1
