import logging
from pathlib import Path

from ai.guardrails import validate_question
from ai.retriever import PetCareRetriever

# Create the logs folder if it doesn't exist
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/pawpal.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class PawPalAssistant:
    """AI assistant for answering general pet-care questions."""

    def __init__(self, knowledge_path: str):
        self.retriever = PetCareRetriever(knowledge_path)

    def answer(self, question: str) -> dict:
        """Returns an AI-style response using retrieved knowledge."""

        valid, message = validate_question(question)

        if not valid:
            logging.warning("Blocked question: %s", question)

            return {
                "status": "blocked",
                "answer": message,
                "sources": [],
                "confidence": 0.0
            }

        documents = self.retriever.search(question)

        if not documents:
            logging.info("No documents found for question: %s", question)

            return {
                "status": "insufficient_context",
                "answer": (
                    "I could not find enough information in the PawPal "
                    "knowledge base. Please consult your veterinarian."
                ),
                "sources": [],
                "confidence": 0.2
            }

        evidence = " ".join(
            document["content"]
            for document in documents
        )

        sources = [
            document["source"]
            for document in documents
        ]

        confidence = min(
            0.55 + (0.15 * len(documents)),
            0.95
        )

        answer = (
            f"Based on the PawPal knowledge base:\n\n"
            f"{evidence}\n\n"
            "This information is educational and should not replace "
            "professional veterinary advice."
        )

        logging.info("Answered question: %s", question)

        return {
            "status": "success",
            "answer": answer,
            "sources": sources,
            "confidence": round(confidence, 2)
        }
