import streamlit as st

st.title("📚 Student To-Do App")

# File to store tasks
TASK_FILE = "tasks.txt"

# Read tasks
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)

tasks = load_tasks()

# Add task
new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task:
        tasks.append(new_task + "\n")
        save_tasks(tasks)
        st.success("Task added successfully!")

# Display tasks
st.subheader("Your Tasks")
for i, task in enumerate(tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(task)
    if col2.button("❌", key=i):
        tasks.pop(i)
        save_tasks(tasks)
        st.experimental_rerun()