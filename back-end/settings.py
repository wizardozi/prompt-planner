# settings.py
import json
import os
from dotenv import load_dotenv

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")
with open(SETTINGS_FILE, "r") as f:
    config = json.load(f)

ALLOWED_PRIORITIES = config.get("allowed_priorities", [])
ALLOWED_STATUSES = config.get("allowed_statuses", [])
PROJECT_CATEGORIES = config.get("project_categories", [])
MODEL = "gpt-4.1"

load_dotenv()  # Loads the .env file into environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



