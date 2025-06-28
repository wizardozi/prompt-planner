# storage.py

import json
import os
from utils import create_project_id, create_task_id, create_subtask_id
from subtask import Subtask
from task import Task
from project import Project

DATA_FILE = "projects.json"

def load_projects():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data.get("projects", [])

def save_projects(projects):
    with open(DATA_FILE, "w") as f:
        json.dump({"projects": projects}, f, indent=2)

def save_tasks(tasks):
    """Save task data to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks():
    """Load task data from the JSON file if it exists."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
