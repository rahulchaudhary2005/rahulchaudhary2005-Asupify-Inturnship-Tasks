import tempfile
import unittest
from pathlib import Path
from repositories.json_task_repository import JsonTaskRepository
from services.task_service import TaskService

class TaskServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        repo = JsonTaskRepository(Path(self.temp_dir.name) / "tasks.json")
        self.service = TaskService(repo)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_persist_task(self):
        self.service.add_task("Study Python", "Practice classes")
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Study Python")

    def test_complete_task(self):
        task = self.service.add_task("Finish assignment")
        self.service.set_completed(task["id"], True)
        self.assertTrue(self.service.get_all_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.service.add_task("Temporary task")
        self.assertTrue(self.service.delete_task(task["id"]))
        self.assertEqual(self.service.get_all_tasks(), [])

if __name__ == "__main__":
    unittest.main()
