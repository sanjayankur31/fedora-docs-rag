#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2026 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import logging
import random
from glob import glob
from pathlib import Path

import chromadb
import numpy
from langchain_chroma import Chroma
from langchain_chroma.vectorstores import cosine_similarity
from neuroml_ai_utils.llm import setup_embedding

logging.basicConfig(level=logging.WARNING)


class FedoraDocsTest(object):
    def __init__(self, embedding_model: str, logging_level: int = logging.DEBUG):
        """TODO: to be defined."""
        self.embedding_model = embedding_model

        my_path = Path(__file__).parent
        self.stores_sources_path = f"{my_path}/sources"

        self.logger = logging.getLogger("Fedora-vs-generator")
        self.logger.setLevel(logging_level)
        self.logger.propagate = True

    def setup(self):
        """Setup embeddings"""
        self.embeddings = setup_embedding(self.embedding_model, self.logger)
        # extract model name
        if self.embedding_model.lower().startswith("huggingface:"):
            # strip suffix/prefix
            self.embedding_model = self.embedding_model.replace("huggingface:", "")
            # strip collection name
            splits = self.embedding_model.split("/")
            self.embedding_model = "".join(splits[1:])
        elif self.embedding_model.lower().startswith("ollama:"):
            # strip prefix
            self.embedding_model = self.embedding_model.replace("ollama:", "")

        self.embedding_model = (
            self.embedding_model.replace(":cheapest", "")
            .replace(":fastest", "")
            .replace(":latest", "")
        )

    def test(self):
        """Create the vector store"""
        assert self.embeddings

        info_files = sorted(glob(f"{self.stores_sources_path}/*.md", recursive=True))

        for src in info_files:
            src_path = Path(src)
            vs_persist_dir = f"./vector-stores/{src_path.name.replace('.md', '')}_{self.embedding_model.replace(':', '_')}.db"

            chroma_client_settings_text = chromadb.config.Settings(
                is_persistent=True,
                persist_directory=vs_persist_dir,
                anonymized_telemetry=False,
            )
            collection_name = src_path.name.replace(".md", "")
            if "fedora" not in collection_name:
                collection_name = f"fedora-{collection_name}"
            store = Chroma(
                collection_name=collection_name,
                embedding_function=self.embeddings,
                client_settings=chroma_client_settings_text,
            )

            # res = store.similarity_search_with_relevance_scores(query=query, k=2)
            # self.logger.debug(f"-> {query}:\n{res}\n\n")

            docs = store.get(include=["embeddings"])

            self.logger.debug(f"{docs =}")
            # leave out beginning and end to prevent out of index errors
            all_ids = docs["ids"]
            all_embeddings = docs["embeddings"]
            if len(all_ids) > 3:
                random_ids = random.sample(all_ids, k=int(len(all_ids) / 3))
            else:
                random_ids = [all_ids[1]]

            similarities = []

            for id_ in random_ids:
                id_x = all_ids.index(id_)
                neighbours = all_embeddings[[id_x - 1, id_x + 1]]
                main = all_embeddings[[id_x]]
                self.logger.debug(f"{neighbours =}")
                self.logger.debug(f"{neighbours.shape =}")
                self.logger.debug(f"{main.shape =}")
                similarity = cosine_similarity(main, neighbours)[0]
                print(f"Similarity: {similarity}")
                similarities.extend(similarity)

            avg = numpy.mean(numpy.array(similarities))
            file = src_path.name.replace(".md", "").replace("-", " ")
            print(f"-> std ({file}): {avg}")
            if avg < 0.60:
                print("-> Disjoined!")
            elif avg > 0.95:
                print("-> Redundant!")
            else:
                print("-> OK")

            print()


if __name__ == "__main__":
    converter = FedoraDocsTest(embedding_model="ollama:bge-m3:latest")
    converter.setup()
    converter.test()
