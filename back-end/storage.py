# storage.py

import json
import os
from subtask import Subtask
from task import Task
from project import Project

# DATA_FILE = "projects.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'projects.json')
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.json')

def load_projects():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data.get("projects", [])

def save_projects(projects):
    with open(DATA_FILE, "w") as f:
        json.dump({"projects": projects}, f, indent=2)

def load_categories():
    if not os.path.exists(SETTINGS_FILE):
        return []
    with open(SETTINGS_FILE, "r") as f:
        data = json.load(f)
        return data.get("project_categories", [])

def save_categories(category):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"project_categories": category}, f, indent=2)

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
