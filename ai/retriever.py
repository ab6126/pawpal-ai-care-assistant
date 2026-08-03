import json
import re
from pathlib import Path
from typing import Any


class PetCareRetriever:
    """Retrieves relevant pet-care information from a JSON knowledge base."""

    def __init__(self, knowledge_path: str):
        self.knowledge_path = Path(knowledge_path)
        self.documents = self._load_documents()

    def _load_documents(self) -> list[dict[str, Any]]:
        """Loads and validates the pet-care knowledge base."""
        if not self.knowledge_path.exists():
            raise FileNotFoundError(
                f"Knowledge-base file was not found: {self.knowledge_path}"
            )

        with self.knowledge_path.open("r", encoding="utf-8") as file:
            documents = json.load(file)

        if not isinstance(documents, list):
            raise ValueError("The knowledge base must contain a JSON list.")

        return documents

    @staticmethod
    def _tokenize(text: str) -> set[str]:
        """Converts text into meaningful lowercase search words."""
        stop_words = {
            "a",
            "an",
            "and",
            "are",
            "as",
            "at",
            "be",
            "by",
            "for",
            "from",
            "how",
            "i",
            "in",
            "is",
            "it",
            "my",
            "of",
            "on",
            "or",
            "should",
            "the",
            "to",
            "what",
            "when",
            "with"
        }

        words = re.findall(r"[a-zA-Z]+", text.lower())

        return {
            word
            for word in words
            if word not in stop_words and len(word) > 1
        }

    def search(
        self,
        query: str,
        limit: int = 3
    ) -> list[dict[str, Any]]:
        """Returns the most relevant documents for a query."""
        if not isinstance(query, str) or not query.strip():
            return []

        query_tokens = self._tokenize(query)
        scored_documents = []

        for document in self.documents:
            searchable_parts = [
                document.get("title", ""),
                document.get("species", ""),
                document.get("topic", ""),
                document.get("content", ""),
                " ".join(document.get("keywords", []))
            ]

            document_tokens = self._tokenize(" ".join(searchable_parts))
            matched_tokens = query_tokens.intersection(document_tokens)
            score = len(matched_tokens)

            species = document.get("species", "").lower()
            topic = document.get("topic", "").lower()

            if species in query_tokens:
                score += 3

            if topic in query_tokens:
                score += 2

            if score > 0:
                scored_documents.append((score, document))

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            document
            for _, document in scored_documents[:limit]
        ]
