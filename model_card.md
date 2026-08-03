# Model Card: PawPal AI Care Assistant

# Model Overview

PawPal AI Care Assistant is a Retrieval-Augmented Generation (RAG) system designed to provide educational pet-care information while helping users organize pet care schedules.

Unlike a general chatbot, PawPal only answers questions using its local pet-care knowledge base. It also includes safety guardrails that block dangerous or medical questions.

---

# Intended Use

The system is intended for:

- General pet-care education
- Pet care scheduling
- Learning basic pet-care information
- Demonstrating Retrieval-Augmented Generation (RAG)
- Demonstrating responsible AI practices

The assistant should not replace professional veterinary advice.

---

# Out of Scope

PawPal is NOT intended to:

- Diagnose diseases
- Recommend medications
- Prescribe treatments
- Handle emergencies
- Replace licensed veterinarians

Emergency questions are blocked automatically.

---

# Data Source

The knowledge base consists of a small JSON dataset stored in:

```

data/pet_care_knowledge.json

```

The information is educational and intended only for demonstration purposes.

---

# AI Architecture

The system contains four AI components:

1. Guardrails
2. Retriever
3. Knowledge Base
4. AI Assistant

Workflow:

User Question

↓

Guardrails

↓

Retriever

↓

Knowledge Base

↓

Assistant Response

↓

Confidence Score

↓

Logging

---

# Confidence Score

The assistant returns a confidence score with every answer.

Current confidence values are heuristic estimates based on retrieval quality.

Example:

- 0.85 = strong match
- 0.20 = insufficient knowledge
- 0.00 = blocked question

---

# Safety Measures

The assistant blocks:

- Emergency situations
- Medication dosage questions
- Veterinary diagnosis requests
- Empty questions

Instead of answering, it directs the user to contact a licensed veterinarian when appropriate.

---

# Limitations

Current limitations include:

- Small knowledge base
- Keyword retrieval only
- No semantic embeddings
- Limited pet species
- No conversation memory
- Confidence scores are estimated rather than learned

The assistant may fail if relevant information is not available in the local database.

---

# Potential Biases

The knowledge base is small and manually created.

As a result:

- Some pet species receive more coverage than others.
- Certain care topics are missing.
- Answers depend entirely on the available documents.

Expanding the knowledge base would reduce these biases.

---

# Potential Misuse

Possible misuse includes:

- Attempting to obtain medical diagnoses
- Requesting medication recommendations
- Using educational information instead of professional veterinary care

To reduce misuse, PawPal blocks medical and emergency questions.

---

# Testing Summary

The project includes automated testing.

Current results:

- 11 automated tests passed.

Tests cover:

- Scheduling
- Conflict detection
- Retrieval
- Guardrails
- AI responses
- Unknown questions

---

# Reflection

## What surprised me?

I learned that building an AI system involves much more than generating answers.

Retrieving relevant information, validating user input, testing the system, logging interactions, and handling unsafe requests are equally important.

---

## Helpful AI Suggestion

One helpful AI suggestion was implementing Retrieval-Augmented Generation instead of relying only on hardcoded responses.

This made the assistant more modular and easier to expand.

---

## Flawed AI Suggestion

One AI suggestion initially ranked unrelated pet-care documents too highly.

I improved the retrieval algorithm by giving additional weight to matching species and topics, producing more relevant search results.

---

## Responsible AI Lessons

This project taught me that responsible AI requires:

- safety guardrails
- transparent limitations
- testing
- documentation
- human oversight

Even small AI systems should clearly communicate what they can and cannot do.

---

# Future Improvements

Future versions could include:

- Semantic search using embeddings
- Larger veterinarian-reviewed knowledge base
- Multi-turn conversation memory
- Personalized pet profiles
- Cloud database
- Calendar integration
- Reminder notifications
