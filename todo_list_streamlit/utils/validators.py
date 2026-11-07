def validate_task_title(title: str):
    if not title or not title.strip():
        return "Please enter a task title."
    if len(title.strip()) > 120:
        return "Task title must be 120 characters or fewer."
    return None
