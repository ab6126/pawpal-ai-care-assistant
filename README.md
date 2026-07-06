# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

Daily plan for Luna:
08:00 — Feeding (10 min) [priority: high]
08:30 — Walk (30 min) [priority: high]
09:15 — Grooming (15 min) [priority: medium]

## 🧪 Testing PawPal+

To run the tests, use:

```bash
python -m pytest
```

The test suite checks task completion, adding tasks to pets, sorting tasks by time, and detecting schedule conflicts.

Successful test output:

```text
4 passed
```

Confidence level: 5/5 stars because all current tests passed.

```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.


| Task sorting | sort_tasks_by_priority() | Sorts high-priority tasks first |
| Filtering | generate_daily_plan() | Skips tasks if there is not enough time |
| Conflict handling | has_conflict() | Detects overlapping task times |
| Recurring tasks | Task.frequency | Marks tasks as daily or weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

1. Open the Streamlit app.
2. Enter the owner name and pet information.
3. Add care tasks with duration and priority.
4. Click “Generate Plan.”
5. Review the daily schedule and reasoning.
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
```
