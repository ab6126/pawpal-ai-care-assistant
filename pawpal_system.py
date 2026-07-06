from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to the pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Adds a pet to the owner's collection."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Returns all tasks for all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    """Manages scheduling operations for all pet tasks."""

    def __init__(self, owner):
        """Initializes the scheduler with an owner."""
        self.owner = owner

    def sort_by_time(self):
        """Returns all tasks sorted by scheduled time."""
        return sorted(self.owner.get_all_tasks(), key=lambda item: item[1].time)

    def filter_by_pet(self, pet_name):
        """Returns tasks belonging to the specified pet."""
        return [
            item for item in self.owner.get_all_tasks()
            if item[0] == pet_name
        ]

    def filter_by_status(self, completed):
        """Returns tasks filtered by completion status."""
        return [
            item for item in self.owner.get_all_tasks()
            if item[1].completed == completed
        ]

    def detect_conflicts(self):
        """Detects tasks that are scheduled at the same time."""
        seen = {}
        conflicts = []

        for pet_name, task in self.owner.get_all_tasks():
            if task.time in seen:
                conflicts.append(
                    f"Conflict at {task.time}: {seen[task.time]} and {pet_name}"
                )
            else:
                seen[task.time] = pet_name

        return conflicts
