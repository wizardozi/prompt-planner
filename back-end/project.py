from task import Task
class Project:
    def __init__(self, name, description, category, id, tasks=None):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tasks = tasks if tasks else []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        return Project(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            category=data["category"],
            tasks=[Task.from_dict(task) for task in data.get("tasks", [])]
        )