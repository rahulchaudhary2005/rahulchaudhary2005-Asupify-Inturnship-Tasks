from models.task import Task

class TaskService:
    """Contains task-management rules; independent of the Streamlit UI."""

    def __init__(self, repository):
        self.repository = repository

    def get_all_tasks(self):
        return [task.to_dict() for task in self.repository.get_all()]

    def add_task(self, title: str, description: str = ""):
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        return self.repository.add(Task.create(title, description.strip())).to_dict()

    def set_completed(self, task_id: str, completed: bool):
        for task in self.repository.get_all():
            if task.id == task_id:
                task.completed = bool(completed)
                updated = self.repository.update(task)
                return updated.to_dict() if updated else None
        return None

    def delete_task(self, task_id: str):
        return self.repository.delete(task_id)

    def filter_tasks(self, status="All", search_text=""):
        tasks = self.get_all_tasks()
        if status == "Pending":
            tasks = [task for task in tasks if not task["completed"]]
        elif status == "Completed":
            tasks = [task for task in tasks if task["completed"]]

        query = search_text.strip().casefold()
        if query:
            tasks = [
                task for task in tasks
                if query in task["title"].casefold()
                or query in task["description"].casefold()
            ]
        return tasks
