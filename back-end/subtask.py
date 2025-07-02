class Subtask:
    def __init__(self, id, name, description, estimate, status="to-do", task_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.estimate = estimate
        self.status = status
        self.task_id = task_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "estimate": self.estimate,
            "status": self.status,
            "task_id": self.task_id
        }

    @staticmethod
    def from_dict(data):
        return Subtask(
            id=data["id"],
            name=data["name"],
            description=data["description", ""],
            estimate=data["estimate", ""],
            status=data.get("status", "to-do"),
            task_id=data["task_id"]
        )