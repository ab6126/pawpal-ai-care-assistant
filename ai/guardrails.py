EMERGENCY_TERMS = {
    "not breathing",
    "unconscious",
    "collapsed",
    "seizure",
    "severe bleeding",
    "poisoned",
    "choking"
}

DIAGNOSIS_TERMS = {
    "diagnose",
    "what disease",
    "what illness",
    "does my pet have",
    "is my pet sick"
}

MEDICATION_TERMS = {
    "change the dose",
    "change the dosage",
    "how much medicine",
    "how much medication",
    "prescribe",
    "increase the dose",
    "decrease the dose"
}


def validate_question(question: str) -> tuple[bool, str]:
    """
    Validates a pet-care question before it reaches the AI assistant.

    Returns:
        A tuple containing:
        - True and an empty message when the question is allowed.
        - False and a safety message when the question is blocked.
    """
    if not isinstance(question, str):
        return False, "Please enter your question as text."

    cleaned_question = question.strip()

    if not cleaned_question:
        return False, "Please enter a pet-care question."

    if len(cleaned_question) > 1000:
        return False, (
            "Your question is too long. Please shorten it to fewer than "
            "1,000 characters."
        )

    lowered_question = cleaned_question.lower()

    if any(term in lowered_question for term in EMERGENCY_TERMS):
        return False, (
            "This may be a pet emergency. Contact a veterinarian or emergency "
            "veterinary service immediately. PawPal cannot diagnose or manage "
            "emergencies."
        )

    if any(term in lowered_question for term in MEDICATION_TERMS):
        return False, (
            "PawPal cannot prescribe medication or recommend changing a dose. "
            "Please contact a licensed veterinarian."
        )

    if any(term in lowered_question for term in DIAGNOSIS_TERMS):
        return False, (
            "PawPal cannot diagnose illnesses. Please contact a licensed "
            "veterinarian for an examination and diagnosis."
        )

    return True, ""
