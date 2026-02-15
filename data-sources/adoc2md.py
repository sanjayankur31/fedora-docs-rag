#!/usr/bin/env python3
"""
Convert adoc to md using asciidoctor and pandoc

File: /home/asinha/Documents/02_Code/00_mine/fedora-stuff/fedora-docs-rag/data-sources/adoc2md.py

Copyright 2026 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import logging
import sys
from contextlib import chdir
from pathlib import Path
from subprocess import run
from typing import Optional

logging.basicConfig(
    format="%(name)s (%(levelname)s) >>> %(message)s\n", level=logging.WARNING
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def runner(filename: Optional[str] = None):
    with chdir("sources"):
        cwd = Path(".")
        if not filename:
            adocs = list(cwd.glob("*.adoc"))
        else:
            adocs = [Path(filename)]
        failures = []
        for adoc in adocs:
            logger.info(f"Processing {str(adoc)}")
            docbook_file = str(adoc).replace(".adoc", ".xml")
            md_file = str(adoc).replace(".adoc", ".md")

            logger.debug(f"Converting {str(adoc)} -> {docbook_file}")
            cmd1 = f"asciidoctor -b docbook {str(adoc)} -o {docbook_file}"
            res = run(cmd1.split())
            if res.returncode != 0:
                failures.append(str(adoc))

            logger.debug(f"Converting {docbook_file} -> {md_file}")
            cmd2 = f"pandoc -f docbook -t markdown {str(docbook_file)} -o {md_file}"
            res2 = run(cmd2.split())
            if res2.returncode != 0:
                failures.append(str(docbook_file))

        with open("adoc2md-failures.txt", "w") as f:
            f.write(str(failures))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        runner()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        runner(filename)
    else:
        print("Error: only zero or one arguments allowed.")
