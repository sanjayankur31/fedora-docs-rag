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
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


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
repo_config_file = "antora.yml"
docs_url_base = "https://docs.fedoraproject.org/en-US"
current_release = "f43"


class RepoToSingleAdoc(object):
    def __init__(self, embedding_model):
        self.logger = logging.getLogger("fetch-fedora-docs")
        self.logger.setLevel(logging.DEBUG)
        self.repo_download_path = "./repos/"
        self.output_path = "./sources/"

    def runner(self):
        response = requests.get(all_docs_yaml)
        docs_config = load(response.text, Loader=Loader)
        self.logger.debug(docs_config)
        repo_urls = {}

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
            url = info["url"]
            branches = info["branches"]
            variables = {}
            full_text = ""
            web_url = ""
            url_map = {}

            self.logger.info(f"Processing {repo}")
            repo_path = f"./{self.repo_download_path}/{repo}"

            # repo_command = command + f" {url} {repo_path}"
            # res = subprocess.run(repo_command.split())
            # if res.returncode:
            #     self.logger.error(f"Git checkout failed for {repo}. Skipping.")
            #     continue
            # else:
            #     self.logger.info(f"Git repo for {repo} checked out at {repo_path}")

            with chdir(repo_path):
                self.logger.debug(f"Working in {repo_path}")
                cwd = Path(".")
                nav_files = list(cwd.rglob("nav.adoc"))
                if len(nav_files) == 0:
                    self.logger.info(
                        f"Repo '{repo}' does not include a 'nav.adoc' file. Skipping"
                    )
                    continue

                web_url = docs_url_base
                # get url:
                # for the moment, use the top level repo url
                # should be possible to map individual pages to web urls using the nav.adoc entries.
                if not Path(repo_config_file).exists():
                    self.logger.critical(f"{repo_config_file} not found! Skipping")
                    continue

                with open(repo_config_file, "r") as f:
                    repo_config = load(f, Loader=Loader)
                    self.logger.debug(f"{repo_config =}")
                    repo_ref = repo_config["name"]
                    self.logger.debug(f"{repo_ref = }")
                    web_url += f"/{repo_ref}"

                    repo_branch = repo_config.get("version", "main")
                    # TODO: how can it be None here?
                    if not repo_branch:
                        repo_branch = "main"

                    self.logger.debug(f"{repo_branch = } ({type(repo_branch)})")
                    self.logger.debug(f"{branches = }")

                    ignore_branches = ["None", "master", "main"]
                    if repo_branch not in ignore_branches:
                        if isinstance(branches, list):
                            if len(branches) > 1:
                                if current_release in branches:
                                    web_url += f"/{current_release}"
                                else:
                                    web_url += f"/{branches[0]}"
                        else:
                            web_url += f"/{repo_branch}"

                    self.logger.debug(f"Repo web url: {web_url}")
                    url_map["DEFAULT"] = web_url

                for nav_file in nav_files:
                    self.logger.debug(f"Processing {nav_file}")
                    if "ROOT" not in str(nav_file.parent):
                        module = str(nav_file.parent).split("/")[-1]
                    else:
                        module = ""
                    self.logger.debug(f"{ module = }")

                    with chdir(nav_file.parent):
                        pagesdir = Path("./pages")
                        partialsdir = Path("./partials")
                        full_text += self.process_adoc(
                            Path(nav_file.name),
                            module,
                            pagesdir,
                            partialsdir,
                            variables,
                            url_map,
                        )

                print(f"{variables =}")
                # replace all the variables we can
                for key, value in variables.items():
                    full_text = full_text.replace("{" + key + "}", value)

            self.logger.debug(
                f"Writing to {self.output_path}/{repo_ref}.adoc: {full_text}"
            )
            with open(f"{self.output_path}/{repo_ref}.adoc", "w") as f:
                f.write(full_text)

            self.logger.debug(
                f"Writing to {self.output_path}/{repo_ref}.json: {url_map}"
            )
            with open(f"{self.output_path}/{repo_ref}.json", "w") as f:
                json.dump(url_map, f)

    def process_adoc(
        self,
        afile: Path,
        module: str,
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
                    text += self.process_adoc(
                        Path(file_ref_path),
                        module,
                        pagesdir,
                        partialsdir,
                        variables,
                        url_map,
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
                        text += self.process_adoc(
                            Path(include_file_path),
                            module,
                            pagesdir,
                            partialsdir,
                            variables,
                            url_map,
                        )
                # a header: update map
                elif line.startswith("=") and not line.endswith("="):
                    header = line.replace("=", "").strip()

                    for key, value in variables.items():
                        header = header.replace("{" + key + "}", value)

                    url = (
                        url_map["DEFAULT"]
                        + "/"
                        + module
                        + "/"
                        + str(afile).replace("pages/", "").replace(".adoc", "")
                    )
                    if afile.name == "index.adoc":
                        url += ".html"
                    url_map[header] = url.replace("//", "/")

                    text += f"{line}\n"

                else:
                    text += f"{line}\n"
                    for key, value in variables.items():
                        text = text.replace("{" + key + "}", value)

            return text


if __name__ == "__main__":
    converter = RepoToSingleAdoc(embedding_model="ollama:bge-m3:latest")
    converter.runner()
