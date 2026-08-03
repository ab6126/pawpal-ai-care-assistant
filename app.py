import streamlit as st

from ai.assistant import PawPalAssistant
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal AI",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal AI")
st.markdown(
    "A pet-care scheduling assistant with retrieval-based AI support."
)

schedule_tab, assistant_tab, about_tab = st.tabs(
    ["Care Schedule", "AI Assistant", "About"]
)


with schedule_tab:
    st.subheader("Pet-Care Schedule")

    owner_name = st.text_input(
        "Owner name",
        value="Anindita",
        key="owner_name"
    )

    pet_name = st.text_input(
        "Pet name",
        value="Max",
        key="pet_name"
    )

    species = st.selectbox(
        "Species",
        ["Dog", "Cat", "Other"],
        key="species"
    )

    st.markdown("### Add a Task")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    col1, col2, col3 = st.columns(3)

    with col1:
        task_title = st.text_input(
            "Task title",
            value="Morning walk",
            key="task_title"
        )

    with col2:
        task_time = st.text_input(
            "Task time",
            value="09:00",
            key="task_time"
        )

    with col3:
        frequency = st.selectbox(
            "Frequency",
            ["once", "daily", "weekly"],
            key="frequency"
        )

    if st.button("Add task", key="add_task"):
        if not task_title.strip():
            st.warning("Please enter a task title.")
        elif not task_time.strip():
            st.warning("Please enter a task time.")
        else:
            st.session_state.tasks.append(
                {
                    "title": task_title.strip(),
                    "time": task_time.strip(),
                    "frequency": frequency,
                    "completed": False
                }
            )
            st.success("Task added.")

    if st.session_state.tasks:
        st.markdown("### Current Tasks")
        st.table(st.session_state.tasks)

        if st.button("Clear all tasks", key="clear_tasks"):
            st.session_state.tasks = []
            st.rerun()
    else:
        st.info("No tasks yet. Add one above.")

    st.divider()
    st.subheader("Build Schedule")

    if st.button("Generate schedule", key="generate_schedule"):
        if not owner_name.strip():
            st.warning("Please enter the owner's name.")
        elif not pet_name.strip():
            st.warning("Please enter the pet's name.")
        elif not st.session_state.tasks:
            st.warning("Please add at least one task.")
        else:
            owner = Owner(owner_name.strip())
            pet = Pet(pet_name.strip(), species)

            for task_data in st.session_state.tasks:
                pet.add_task(
                    Task(
                        task_data["title"],
                        task_data["time"],
                        task_data["frequency"],
                        task_data["completed"]
                    )
                )

            owner.add_pet(pet)
            scheduler = Scheduler(owner)

            schedule_rows = []

            for scheduled_pet_name, task in scheduler.sort_by_time():
                schedule_rows.append(
                    {
                        "Time": task.time,
                        "Pet": scheduled_pet_name,
                        "Task": task.description,
                        "Frequency": task.frequency,
                        "Status": (
                            "Done"
                            if task.completed
                            else "Not done"
                        )
                    }
                )

            st.success("Schedule generated.")
            st.table(schedule_rows)

            conflicts = scheduler.detect_conflicts()

            if conflicts:
                st.markdown("### Scheduling Conflicts")

                for conflict in conflicts:
                    st.warning(conflict)
            else:
                st.success("No scheduling conflicts found.")


with assistant_tab:
    st.subheader("Ask PawPal AI")

    st.write(
        "Ask a general question about pet feeding, exercise, "
        "play, medication safety, or veterinary appointments."
    )

    assistant = PawPalAssistant(
        "data/pet_care_knowledge.json"
    )

    question = st.text_area(
        "Pet-care question",
        placeholder="How often should I walk my adult dog?",
        key="ai_question"
    )

    if st.button("Get answer", key="get_ai_answer"):
        result = assistant.answer(question)

        if result["status"] == "blocked":
            st.warning(result["answer"])

        elif result["status"] == "insufficient_context":
            st.info(result["answer"])

        else:
            st.markdown("### Answer")
            st.write(result["answer"])

            st.markdown("### Confidence")
            st.progress(result["confidence"])
            st.write(f"{result['confidence']:.0%}")

            if result["sources"]:
                st.markdown("### Sources")

                unique_sources = list(
                    dict.fromkeys(result["sources"])
                )

                for source in unique_sources:
                    st.write(f"- {source}")


with about_tab:
    st.subheader("About PawPal AI")

    st.write(
        "PawPal AI combines a traditional pet-care scheduler "
        "with a retrieval-based question-answering system."
    )

    st.markdown("### How the AI feature works")

    st.write(
        "1. The user's question is checked by safety guardrails.\n"
        "2. PawPal searches a pet-care knowledge base.\n"
        "3. The most relevant information is retrieved.\n"
        "4. PawPal produces an answer based on that information.\n"
        "5. The system displays sources and a confidence estimate."
    )

    st.markdown("### Responsible-use notice")

    st.warning(
        "PawPal provides general educational information only. "
        "It cannot diagnose illnesses, prescribe medication, "
        "change dosages, or replace a veterinarian."
    )
