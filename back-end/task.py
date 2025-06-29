from subtask import Subtask
from settings import ALLOWED_PRIORITIES, ALLOWED_STATUSES

class Task:
    def __init__(self, id, label, description, due_by, status="incomplete", priority="medium", project_id=None, subtasks=None, ):
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Must be one of {ALLOWED_PRIORITIES}")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of {ALLOWED_STATUSES}")
        self.id = id
        self.label = label
        self.description = description
        self.due_by = due_by
        self.status = status
        self.priority = priority
        self.project_id = project_id
        self.subtasks = subtasks if subtasks else []

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "description": self.description,
            "due_by": self.due_by,
            "status": self.status,
            "priority": self.priority,
            "project_id": self.project_id,
            "subtasks": [subtask.to_dict() for subtask in self.subtasks]
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            label=data["label"],
            description=data["description", ""],
            due_by=data["due_by", ""],
            status=data.get("status", "incomplete"),
            priority=data.get("priority", "medium"),
            project_id=data["project_id"],
            subtasks=[Subtask.from_dict(subtask) for subtask in data.get("subtasks", [])]
        )