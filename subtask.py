from settings import ALLOWED_PRIORITIES, ALLOWED_STATUSES
class Subtask:
    def __init__(self, id, label, description, estimate, status="to-do", priority="medium", task_id=None):
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Must be one of {ALLOWED_PRIORITIES}")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of {ALLOWED_STATUSES}")
        self.id = id
        self.label = label
        self.description = description
        self.estimate = estimate
        self.status = status
        self.priority = priority
        self.task_id = task_id

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "description": self.description,
            "estimate": self.estimate,
            "status": self.status,
            "priority": self.priority,
            "task_id": self.task_id
        }

    @staticmethod
    def from_dict(data):
        return Subtask(
            id=data["id"],
            label=data["label"],
            description=data["description", ""],
            estimate=data["estimate", ""],
            status=data.get("status", "to-do"),
            priority=data.get("priority", "medium"),
            task_id=data["task_id"]
        )