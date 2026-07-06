import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown("Welcome to PawPal+, a simple pet care scheduling assistant.")

st.divider()

st.subheader("Quick Demo Inputs")

owner_name = st.text_input("Owner name", value="Anindita")
pet_name = st.text_input("Pet name", value="Max")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

st.markdown("### Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    task_time = st.text_input("Task time", value="09:00")

with col3:
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "time": task_time,
            "frequency": frequency,
            "completed": False,
        }
    )
    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    owner = Owner(owner_name)
    pet = Pet(pet_name, species)

    for task_data in st.session_state.tasks:
        pet.add_task(
            Task(
                task_data["title"],
                task_data["time"],
                task_data["frequency"],
                task_data["completed"],
            )
        )

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    st.success("Schedule generated!")

    schedule_rows = []
    for pet_name, task in scheduler.sort_by_time():
        schedule_rows.append(
            {
                "Time": task.time,
                "Pet": pet_name,
                "Task": task.description,
                "Frequency": task.frequency,
                "Status": "Done" if task.completed else "Not done",
            }
        )

    st.table(schedule_rows)

    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for conflict in conflicts:
            st.warning(conflict)
    else:
        st.success("No scheduling conflicts found.")
