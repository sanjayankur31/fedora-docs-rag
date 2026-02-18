#!/usr/bin/env python3
"""
Fetch documentation repositories

File: fetch-docs.py

Copyright 2026 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import json
import logging
import re
import subprocess
from contextlib import chdir
from pathlib import Path

import requests
import typer
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from typing import Optional

logging.basicConfig(
    format="%(name)s (%(levelname)s) >>> %(message)s\n", level=logging.WARNING
)

all_docs_yaml = "https://gitlab.com/fedora/docs/docs-website/docs-fp-o/-/raw/prod/site.yml?inline=false"
# docs we want to skip
exclude_doc_urls = [
    "https://gitlab.com/fedora/docs/docs-website/pages.git",
    "https://gitlab.com/fedora/docs/fedora-linux-documentation/release-docs-home.git",
    "https://gitlab.com/fedora/docs/fedora-linux-documentation/install-guide.git",
    "https://gitlab.com/fedora/docs/fedora-linux-documentation/fedora-linux-sysadmin-guide.git",
    "https://pagure.io/fedora-docs/localization.git",
]
docs_proj_config_file = "antora.yml"
docs_url_base = "https://docs.fedoraproject.org/en-US"
current_release = "f43"
# order is important
replacements = {
    "&": "\\&amp;",
    "#": "\\&#35;",
    "<": "\\&lt;",
    ">": "\\&gt;",
    "*": "\\&#42;",
    "...": "\\&#8230;",
    # "[": "&#91;",
    # "]": "&#93;",
    # "_": "&#95;",
    "`": "\\&#96;",
    '"': "'",
}


class RepoToSingleAdoc(object):
    def __init__(self):
        self.app = typer.Typer()
        self.logger = logging.getLogger("fetch-fedora-docs")
        self.logger.setLevel(logging.DEBUG)
        self.repo_download_path = Path("./repos/").absolute()
        self.output_path = Path("./sources/").absolute()

        self.app.command()(self.runner)

    def runner(self, fetch_git_repos: bool = False, repo_filter: Optional[str] = None):
        response = requests.get(all_docs_yaml)
        docs_config = load(response.text, Loader=Loader)
        self.logger.debug(f"{docs_config =}")
        repo_urls = {}

        self.fetch_git_repos = fetch_git_repos
        self.repo_filter = repo_filter
        self.logger.debug(f"{self.repo_filter =}")

        for src in docs_config["content"]["sources"]:
            git_url = src["url"]

            # TODO: unused
            branches = []
            try:
                branches = src["branches"]
            except KeyError:
                pass

            if git_url in exclude_doc_urls:
                self.logger.info(f"Skipping {git_url} from excludes")
                continue

            repo_name = git_url.split("//")[1].replace("/", "-").replace(".git", "")
            repo_urls[repo_name] = {"url": git_url, "branches": branches}

        self.logger.debug(f"{repo_urls =}")

        command = "git clone --depth=1"
        for repo, info in repo_urls.items():
            branches = info["branches"]
            url = info["url"]
            repo_path = f"{self.repo_download_path}/{repo}"
            self.logger.debug(f"{repo_path =}")

            self.logger.info(f"Processing {repo}")
            if self.repo_filter:
                if self.repo_filter not in repo:
                    self.logger.info(
                        f"{repo} not matched by filter ({self.repo_filter}). Skipping"
                    )
                    continue

            if self.fetch_git_repos:
                repo_command = command + f" {url} {repo_path}"
                res = subprocess.run(repo_command.split())
                if res.returncode:
                    self.logger.error(f"Git checkout failed for {repo}. Skipping.")
                    continue
                else:
                    self.logger.info(f"Git repo for {repo} checked out at {repo_path}")
            else:
                self.logger.info("Repo fetching disabled. Did not clone repos.")

            with chdir(repo_path):
                self.logger.debug(f"Working in {repo_path}")
                cwd = Path(".")

                docs_proj_config_file_paths = list(cwd.rglob(docs_proj_config_file))
                if len(docs_proj_config_file_paths) == 0:
                    self.logger.critical(f"{docs_proj_config_file} not found! Skipping")
                    continue
                for docs_proj_config_file_path in docs_proj_config_file_paths:
                    self.logger.debug(
                        f"processing {docs_proj_config_file_path.absolute()}"
                    )
                    config_file = docs_proj_config_file_path

                    variables: dict[str, str] = {}
                    full_text = ""
                    url_map: dict[str, str] = {}
                    web_url = docs_url_base

                    with chdir(config_file.parent):
                        nav_files = []
                        with open(config_file.name, "r") as f:
                            docs_proj_config = load(f, Loader=Loader)
                            self.logger.debug(f"{docs_proj_config =}")
                            docs_proj_ref = docs_proj_config["name"]
                            self.logger.debug(f"{docs_proj_ref = }")
                            web_url += f"/{docs_proj_ref}"
                            nav_files = docs_proj_config.get("nav", [])
                            self.logger.debug(f"{nav_files =}")

                            if len(nav_files) == 0:
                                self.logger.warning(
                                    f"Repo '{repo}/{docs_proj_config_file_path.parent}' does not include a 'nav.adoc' file! Iterating over all docs in no order, starting with index.adoc"
                                )
                                nav_files = list(cwd.rglob("index.adoc"))
                                nav_files.extend(
                                    [
                                        p
                                        for p in cwd.rglob("*.adoc")
                                        if p.name != "index.adoc"
                                    ]
                                )
                                self.logger.debug(
                                    f"(no nav file): All files are: {nav_files}"
                                )

                            docs_proj_branch = docs_proj_config.get("version", "main")
                            # TODO: how can it be None here?
                            if not docs_proj_branch:
                                docs_proj_branch = "main"

                            self.logger.debug(
                                f"{docs_proj_branch = } ({type(docs_proj_branch)})"
                            )
                            self.logger.debug(f"{branches = }")

                            ignore_branches = ["None", "master", "main"]
                            if docs_proj_branch not in ignore_branches:
                                if isinstance(branches, list):
                                    if len(branches) > 1:
                                        if current_release in branches:
                                            web_url += f"/{current_release}"
                                        else:
                                            web_url += f"/{branches[0]}"
                                else:
                                    web_url += f"/{docs_proj_branch}"

                            self.logger.debug(f"Repo web url: {web_url}")
                            url_map["DEFAULT"] = web_url

                        for anav_file in nav_files:
                            nav_file = Path(anav_file)
                            self.logger.debug(f"Processing {nav_file}")
                            if "ROOT" not in str(nav_file.parent):
                                module_root = str(nav_file.parent).split("/")[-1]
                            else:
                                module_root = ""
                            self.logger.debug(f"{ module_root = }")

                            with chdir(nav_file.parent):
                                pagesdir = Path("./pages")
                                partialsdir = Path("./partials")
                                full_text += self.process_adoc(
                                    Path(nav_file.name),
                                    web_url,
                                    module_root,
                                    pagesdir,
                                    partialsdir,
                                    variables,
                                    url_map,
                                )

                    print(f"{variables =}")
                    # replace all the variables we can
                    for key, value in variables.items():
                        full_text = full_text.replace("{" + key + "}", value)

                    # more replacements
                    for a, b in replacements.items():
                        full_text = full_text.replace(a, b)

                    # self.logger.debug(
                    #     f"Writing to {self.output_path}/{docs_proj_ref}.adoc: {full_text}"
                    # )
                    with open(f"{self.output_path}/{docs_proj_ref}.adoc", "w") as f:
                        f.write(full_text)

                    self.logger.debug(
                        f"Writing to {self.output_path}/{docs_proj_ref}.json: {url_map}"
                    )
                    with open(f"{self.output_path}/{docs_proj_ref}.json", "w") as f:
                        json.dump(url_map, f)

    def process_adoc(
        self,
        afile: Path,
        web_url: str,
        module_root: str,
        pagesdir: Path,
        partialsdir: Path,
        variables: dict[str, str],
        url_map: dict[str, str],
    ) -> str:
        """Process an adoc file"""
        text = ""
        self.logger.debug(f"Processing file: {afile}")
        if not afile.exists():
            self.logger.critical(f"{afile} not found! Skipping.")
            return ""

        with open(afile, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                # variables
                varmatch = re.match(r"^:(\w+):\s+(.+)", line)
                if varmatch:
                    key = varmatch.group(1)
                    val = varmatch.group(2)
                    variables[key] = val
                    continue

                if "xref:" in line and afile.name == "nav.adoc":
                    self.logger.debug(f"Processing xref: {line}")
                    matchres = re.match(r".*xref:(.+\.adoc).*\[.+", line)
                    assert matchres and (len(matchres.groups()) > 0)
                    file_ref = matchres.group(1)
                    file_ref_path = pagesdir / Path(file_ref)
                    self.logger.debug(f"Referenced file: {file_ref_path}")

                    if file_ref_path.exists():
                        text += self.process_adoc(
                            Path(file_ref_path),
                            web_url,
                            module_root,
                            pagesdir,
                            partialsdir,
                            variables,
                            url_map,
                        )
                        text += "\n\n"
                    else:
                        self.logger.warning(
                            f"Referenced file {file_ref_path} not found. Skipping."
                        )
                # includes
                elif line.startswith("include::"):
                    self.logger.debug(f"Processing include:: {line}")
                    include_file = line.replace("include::", "")
                    if "partial$" in include_file:
                        include_file_path = include_file.replace(
                            "partial$", str(partialsdir) + "/"
                        )
                        include_file_path = include_file_path.replace(
                            ".adoc[]", ".adoc"
                        )
                        self.logger.debug(f"Included file: {include_file_path}")
                        if Path(include_file_path).exists():
                            text += self.process_adoc(
                                Path(include_file_path),
                                web_url,
                                module_root,
                                pagesdir,
                                partialsdir,
                                variables,
                                url_map,
                            )
                            text += "\n\n"
                        else:
                            self.logger.warning(
                                f"Included file {include_file_path} not found. Skipping."
                            )
                # a header: update map
                elif line.startswith("=") and not line.endswith("="):
                    header = line.replace("=", "").strip()

                    url = (
                        web_url
                        + "/"
                        + str(afile).replace("pages/", "").replace(".adoc", "")
                    )
                    if afile.name == "index.adoc":
                        url += ".html"
                    url_map[header] = url.replace("//", "/")

                    text += f"{line}\n"

                # some section links/references have spaces in them
                elif line.startswith("[") and line.endswith("]"):
                    line = line.replace(" ", "_")
                    text += f"{line}\n"

                else:
                    text += f"{line}\n"

            for key, value in variables.items():
                text = text.replace("{" + key + "}", value)

            return text


if __name__ == "__main__":
    converter = RepoToSingleAdoc()
    converter.app()
