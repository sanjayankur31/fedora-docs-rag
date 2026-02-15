#!/usr/bin/env python3
"""
Convert adoc to md using asciidoctor and pandoc

File: /home/asinha/Documents/02_Code/00_mine/fedora-stuff/fedora-docs-rag/data-sources/adoc2md.py

Copyright 2026 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import logging
from contextlib import chdir
from pathlib import Path
from subprocess import run

logging.basicConfig(
    format="%(name)s (%(levelname)s) >>> %(message)s\n", level=logging.WARNING
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def runner():
    with chdir("sources"):
        cwd = Path(".")
        adocs = cwd.glob("*.adoc")
        for adoc in adocs:
            logger.info(f"Processing {str(adoc)}")
            docbook_file = str(adoc).replace(".adoc", ".xml")
            md_file = str(adoc).replace(".adoc", ".md")

            logger.debug(f"Converting {str(adoc)} -> {docbook_file}")
            cmd1 = f"asciidoctor -b docbook {str(adoc)} -o {docbook_file}"
            run(cmd1.split())

            logger.debug(f"Converting {docbook_file} -> {md_file}")
            cmd2 = f"pandoc -f docbook -t markdown {str(docbook_file)} -o {md_file}"
            run(cmd2.split())


if __name__ == "__main__":
    runner()
