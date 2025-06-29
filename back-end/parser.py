import re
from project import Project
from task import Task
from datetime import datetime, timedelta
import re

def parse_response_to_project(name, response):
    tasks = []
    current_task = None

    lines = response.split("\n")
    for line in lines:
        stripped = line.replace("\t", " ").strip()
        if not stripped:
            continue

        # Header: "1. Today – Define Integration Requirements"
        header_match = re.match(r"^\d+\.\s*(.*?)\s*[–-]\s*(.+)", stripped)
        if header_match:
            due_by = header_match.group(1).strip()
            label = header_match.group(2).strip()
            current_task = Task(
                id=create_task_id(),
                label=label,
                due_by=due_by,
                datetime=due_by_to_datetime(due_by),
                estimate="~1h",  # Placeholder, you can infer later
                status="incomplete",
                subtasks=[]
            )
            tasks.append(current_task)
            continue

        # Subtask line
        if current_task:
            subtask_match = re.match(r"^\s*[-•\d\.\)]*\s*(.+)", stripped)
            if subtask_match:
                cleaned = subtask_match.group(1).strip()
                if cleaned:
                    current_task.subtasks.append({
                        "description": cleaned,
                        "status": "pending"
                    })

    return Project(name=name, id=create_project_id(), tasks=tasks)



def due_by_to_datetime(due_by: str) -> datetime:
    due_by = due_by.lower().strip()
    now = datetime.now()

    # Handle simple keywords
    if "today" in due_by:
        return now.replace(hour=10, minute=0, second=0, microsecond=0)
    elif "tomorrow" in due_by:
        return (now + timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0)

    # Weekday mapping
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for i, day in enumerate(weekdays):
        if day in due_by:
            today_idx = now.weekday()
            days_ahead = (i - today_idx + 7) % 7
            target_date = now + timedelta(days=days_ahead)

            # Time of day
            if "morning" in due_by:
                return target_date.replace(hour=9, minute=0, second=0, microsecond=0)
            elif "afternoon" in due_by:
                return target_date.replace(hour=14, minute=0, second=0, microsecond=0)
            elif "evening" in due_by:
                return target_date.replace(hour=18, minute=0, second=0, microsecond=0)
            else:
                return target_date.replace(hour=10, minute=0, second=0, microsecond=0)

    # Fallback if nothing matched
    return now
