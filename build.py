#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble index.html from template.html + the data modules.

Edit items.py / legs.py / bags.py / daybags.py / shopping.py, then run this.
Never edit index.html by hand — it is generated and will be overwritten.

Verification: after writing, it re-reads the output, pulls the DATA object back
out and checks it round-trips to exactly what went in. If that fails, the old
index.html is restored and nothing ships.
"""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from items import I as ITEMS
from legs import LEGS
from bags import BAGS
from daybags import DAYBAGS
from shopping import SHOPPING

TPL = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "index.html")


def main():
    data = {
        "items": ITEMS,
        "legs": LEGS,
        "bags": BAGS,
        "daybags": DAYBAGS,
        "shopping": SHOPPING,
    }

    tpl = open(TPL, encoding="utf-8").read()
    if "__DATA__" not in tpl:
        sys.exit("template.html has no __DATA__ placeholder — refusing to build.")

    blob = json.dumps(data, ensure_ascii=True, separators=(",", ":"))
    # </script> inside a string would close the tag early.
    blob = blob.replace("</", "<\\/")

    html = tpl.replace("__DATA__", blob)

    backup = None
    if os.path.exists(OUT):
        backup = OUT + ".bak"
        shutil.copy2(OUT, backup)

    open(OUT, "w", encoding="utf-8").write(html)

    # --- verify the output parses back to the same data ---
    try:
        got = open(OUT, encoding="utf-8").read()
        m = re.search(r"const DATA=(\{.*?\});\n", got, re.S)
        if not m:
            raise AssertionError("could not find DATA in the output")
        back = json.loads(m.group(1).replace("<\\/", "</"))
        if back != data:
            raise AssertionError("DATA did not round-trip")
    except Exception as e:
        if backup:
            shutil.copy2(backup, OUT)
        sys.exit("BUILD FAILED (%s). index.html restored from backup." % e)

    if backup:
        os.remove(backup)

    counts = {k: len(v) for k, v in data.items()}
    weight = sum(i.get("g", 0) or 0 for i in ITEMS)
    print("Built index.html — %d bytes" % len(html))
    print("  " + "  ".join("%s %d" % (k, v) for k, v in counts.items()))
    print("  total listed weight %.1f kg" % (weight / 1000.0))
    print("  DATA verified: round-trips exactly.")


if __name__ == "__main__":
    main()
