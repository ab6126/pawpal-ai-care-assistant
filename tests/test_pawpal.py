from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Feed breakfast", "08:00", "daily")
    task.mark_complete()
    assert task.completed == True


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
