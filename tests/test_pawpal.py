from pawpal_system import Owner, Pet, Task, Scheduler
from ai.assistant import PawPalAssistant
from ai.guardrails import validate_question
from ai.retriever import PetCareRetriever


def test_task_completion():
    task = Task("Feed breakfast", "08:00", "daily")
    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Max", "Dog")
    task = Task("Morning walk", "09:00", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sort_by_time():
    owner = Owner("Anindita")
    pet = Pet("Max", "Dog")
    pet.add_task(Task("Walk", "09:00", "daily"))
    pet.add_task(Task("Feed", "08:00", "daily"))
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0][1].time == "08:00"


def test_conflict_detection():
    owner = Owner("Anindita")
    dog = Pet("Max", "Dog")
    cat = Pet("Luna", "Cat")

    dog.add_task(Task("Walk", "09:00", "daily"))
    cat.add_task(Task("Clean litter", "09:00", "daily"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1


def test_retriever_returns_dog_exercise_first():
    retriever = PetCareRetriever(
        "data/pet_care_knowledge.json"
    )

    results = retriever.search(
        "How often should I walk my dog?"
    )

    assert len(results) > 0
    assert results[0]["title"] == "General Dog Exercise"


def test_empty_question_is_blocked():
    valid, message = validate_question("")

    assert valid is False
    assert message != ""


def test_emergency_question_is_blocked():
    valid, message = validate_question(
        "My dog collapsed and is not breathing."
    )

    assert valid is False
    assert "emergency" in message.lower()


def test_normal_question_is_allowed():
    valid, message = validate_question(
        "How often should I walk my dog?"
    )

    assert valid is True
    assert message == ""


def test_ai_assistant_answers_normal_question():
    assistant = PawPalAssistant(
        "data/pet_care_knowledge.json"
    )

    result = assistant.answer(
        "How often should I walk my dog?"
    )

    assert result["status"] == "success"
    assert result["confidence"] > 0
    assert len(result["sources"]) > 0


def test_ai_assistant_blocks_emergency_question():
    assistant = PawPalAssistant(
        "data/pet_care_knowledge.json"
    )

    result = assistant.answer(
        "My dog collapsed and is not breathing."
    )

    assert result["status"] == "blocked"
    assert result["confidence"] == 0.0


def test_ai_assistant_handles_unknown_question():
    assistant = PawPalAssistant(
        "data/pet_care_knowledge.json"
    )

    result = assistant.answer(
        "How do I repair a spaceship engine?"
    )

    assert result["status"] == "insufficient_context"
