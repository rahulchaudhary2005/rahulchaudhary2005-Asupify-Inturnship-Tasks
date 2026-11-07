import streamlit as st
from services.task_service import TaskService
from repositories.json_task_repository import JsonTaskRepository
from utils.validators import validate_task_title

st.set_page_config(page_title="TaskFlow - To-Do List", page_icon="✅", layout="wide")

@st.cache_resource
def get_service():
    return TaskService(JsonTaskRepository())

service = get_service()

st.title("✅ TaskFlow")
st.caption("A simple, organized place to manage your daily tasks.")

# Load fresh data for each rerun
tasks = service.get_all_tasks()
total = len(tasks)
completed = sum(task["completed"] for task in tasks)
pending = total - completed

m1, m2, m3 = st.columns(3)
m1.metric("Total tasks", total)
m2.metric("Pending", pending)
m3.metric("Completed", completed)

st.divider()

left, right = st.columns([1, 1.6], gap="large")

with left:
    st.subheader("➕ Add a task")
    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("Task title", placeholder="e.g. Complete Python assignment")
        description = st.text_area("Description (optional)", placeholder="Add a few details...")
        submitted = st.form_submit_button("Add task", use_container_width=True)
        if submitted:
            error = validate_task_title(title)
            if error:
                st.error(error)
            else:
                service.add_task(title.strip(), description.strip())
                st.success("Task added successfully.")
                st.rerun()

    st.subheader("🔎 Filter tasks")
    filter_value = st.selectbox("Show", ["All", "Pending", "Completed"])
    search_text = st.text_input("Search tasks", placeholder="Search by title or description")

with right:
    st.subheader("📋 Your tasks")
    visible_tasks = service.filter_tasks(filter_value, search_text)
    if not visible_tasks:
        st.info("No tasks found. Add a task or change your filters.")
    else:
        for task in visible_tasks:
            with st.container(border=True):
                top = st.columns([0.08, 0.72, 0.20])
                checked = top[0].checkbox(
                    "Complete",
                    value=task["completed"],
                    key=f"complete_{task['id']}",
                    label_visibility="collapsed",
                )
                if checked != task["completed"]:
                    service.set_completed(task["id"], checked)
                    st.rerun()

                title_text = f"~~{task['title']}~~" if task["completed"] else f"**{task['title']}**"
                top[1].markdown(title_text)
                top[2].caption("Completed" if task["completed"] else "Pending")

                if task["description"]:
                    st.write(task["description"])
                st.caption(f"Created: {task['created_at']}")

                delete_col, _ = st.columns([0.22, 0.78])
                if delete_col.button("🗑️ Delete", key=f"delete_{task['id']}"):
                    service.delete_task(task["id"])
                    st.toast("Task deleted.")
                    st.rerun()

st.divider()
st.caption("Your tasks are stored locally in data/tasks.json. No account or external database is required.")
