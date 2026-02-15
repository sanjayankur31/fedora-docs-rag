#!/usr/bin/env python3
"""
Generate a template vector store configuration

File: data-sources/vsconfig.py

Copyright 2026 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import json
import logging
from pathlib import Path

logging.basicConfig(
    format="%(name)s (%(levelname)s) >>> %(message)s\n", level=logging.WARNING
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def runner():
    ds = Path("./sources/")
    vs = Path("./vector-stores")
    domain_files = sorted(list(ds.glob("*.md")))
    store_list = []

    for df in domain_files:
        dn = df.name.replace(".md", "")
        print(dn)
        store = list(vs.glob(f"{dn}*.db"))
        print(store)

        if len(store) == 0:
            continue

        store_list.append({"name": dn, "path": str(store[0].absolute())})

    res = {"vector_stores": store_list}
    print(json.dumps(res, indent=4))


if __name__ == "__main__":
    runner()
