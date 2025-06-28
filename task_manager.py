# task_manager.py
from task import Task
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, subtasks=None):
        task = Task(title, subtasks)
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} ({task.status})")
            for sub in task.subtasks:
                print(f"   - [ ] {sub}")

    def to_json(self):
        return [task.to_dict() for task in self.tasks]

    def load_from_json(self, data):
        self.tasks = [Task.from_dict(t) for t in data]