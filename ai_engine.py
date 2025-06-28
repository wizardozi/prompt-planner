import requests
import re
MODEL = "mistral"
ALLOWED_PRIORITIES = {"low", "medium", "high", "urgent"}
ALLOWED_STATUSES = {"to-do", "in-progress", "done", "incomplete"}

def generate_response(prompt):
    pass
# def generate_subtasks(task_description):
#     prompt = f"Break the following task into 3-5 clear subtasks:\n\nTask: {task_description}\n\nSubtasks:"
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": MODEL,
#             "prompt": prompt,
#             "stream": False
#         }
#     )
#     lines = response.json()["response"].split("\n")
#     return clean_subtasks(lines)

# Function will generate a descriptive project title based on the task

def generate_project_response(prompt):
    print("Generating subtasks (fake AI)...")
    return """1.	Today (1–2 hours) – Define Integration Requirements
	•	Clarify what features the AI should support (e.g., task expansion, deadline suggestions)
	•	Decide on local model vs. API-based model (e.g., DeepSeek, Mistral, OpenAI)
	•	Write example prompts and desired output formats
	2.	Tomorrow Morning (2–3 hours) – Set Up the AI Engine Module
	•	Create or update ai_engine.py to include prompt formatting and request handling
	•	Add support for selecting different models (Mistral, DeepSeek, etc.)
	•	Mock the responses for initial testing
	3.	Tomorrow Afternoon (1–2 hours) – Integrate AI Calls into CLI/Interface
	•	Hook up the AI module to your main CLI workflow
	•	Format AI output to match clean_subtasks() expectations
	•	Add loading animation (spinner) to indicate “thinking”
	4.	Tuesday (2–3 hours) – Test Real Prompts with Live Models
	•	Use realistic task inputs and verify that responses are formatted well
	•	Adjust prompts to improve output structure
	•	Handle model timeouts or bad responses gracefully
	5.	Wednesday (2 hours) – Add Scheduling and Deadlines Layer
	•	Modify prompt structure to generate time-aware subtasks
	•	Parse durations and timestamps from AI responses
	•	Display tasks in chronological order or timeline view
	6.	Thursday (1–2 hours) – Final Polish and UX Improvements
	•	Refactor AI logic into a clean helper or service class
	•	Add fallback or retry if model fails
	•	Ensure output is readable in both CLI and future GUI"""
