# settings.py
import json
import os

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

with open(SETTINGS_FILE, "r") as f:
    config = json.load(f)

ALLOWED_PRIORITIES = config.get("allowed_priorities", [])
ALLOWED_STATUSES = config.get("allowed_statuses", [])
PROJECT_CATEGORIES = config.get("project_categories", [])