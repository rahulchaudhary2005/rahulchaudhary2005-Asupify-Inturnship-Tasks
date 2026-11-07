import json
from pathlib import Path
from models.task import Task

class JsonTaskRepository:
    """Handles reading and writing tasks to a local JSON file."""

    def __init__(self, file_path="data/tasks.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write([])

    def _read(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                raw = json.load(file)
            if not isinstance(raw, list):
                raise ValueError("Task data must be a JSON list.")
            return [Task.from_dict(item) for item in raw]
        except json.JSONDecodeError as exc:
            raise RuntimeError("The task data file contains invalid JSON.") from exc

    def _write(self, tasks):
        temporary = self.file_path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4, ensure_ascii=False)
        temporary.replace(self.file_path)

    def get_all(self):
        return self._read()

    def add(self, task: Task):
        tasks = self._read()
        tasks.append(task)
        self._write(tasks)
        return task

    def update(self, updated_task: Task):
        tasks = self._read()
        for index, task in enumerate(tasks):
            if task.id == updated_task.id:
                tasks[index] = updated_task
                self._write(tasks)
                return updated_task
        return None

    def delete(self, task_id: str):
        tasks = self._read()
        remaining = [task for task in tasks if task.id != task_id]
        if len(remaining) == len(tasks):
            return False
        self._write(remaining)
        return True
