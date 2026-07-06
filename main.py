from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Anindita")

dog = Pet("Max", "Dog")
cat = Pet("Luna", "Cat")

dog.add_task(Task("Morning walk", "09:00", "daily"))
dog.add_task(Task("Feed breakfast", "08:00", "daily"))
cat.add_task(Task("Clean litter box", "09:00", "daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

print("Today's Schedule")
print("----------------")

for pet_name, task in scheduler.sort_by_time():
    status = "Done" if task.completed else "Not done"
    print(f"{task.time} - {pet_name}: {task.description} ({status})")

print("\nConflicts")
print("---------")

for conflict in scheduler.detect_conflicts():
    print(conflict)
