import requests
from project import Project
from task import Task
from subtask import Subtask
import os
import re
from jinja2 import Template
from settings import ALLOWED_PRIORITIES, ALLOWED_STATUSES, PROJECT_CATEGORIES, MODEL, OPENAI_API_KEY
from storage import load_projects, save_projects
from utils import create_project_id, create_task_id, create_subtask_id
from openai import OpenAI
import json
from flask import jsonify




def render_prompt_from_file(file_path, context):
    abs_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(abs_path, "r") as f:
        template = Template(f.read())
    return template.render(context)

def ai_generate_project(prompt):

    client = OpenAI(api_key=OPENAI_API_KEY)
    rendered_prompt = render_prompt_from_file("prompts/project_prompt.txt", {"prompt": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert project planner. Return output as valid JSON only."},
            {"role": "user", "content": rendered_prompt}
        ],
        response_format={"type": "json_object"}
    )

    # Save to disk — skip all return logic
    save_generated_project(response.choices[0].message.content)


def save_generated_project(response):
    parsed = json.loads(response)
    if parsed["category"] not in PROJECT_CATEGORIES:
        parsed["category"] = "other"
    project_id = create_project_id()
    project = Project(
        id=project_id,
        name=parsed["name"],
        description=parsed["description"],
        category=parsed["category"],
        tasks=[]
    )

    for task_data in parsed.get("tasks", []):
        task_id = create_task_id()
        task = Task(
            id=task_id,
            name=task_data["name"],
            description=task_data["description"],
            due_by=task_data.get("due_by", ""),
            priority=task_data.get("priority", "medium"),
            status="to-do",
            project_id=project_id,
            subtasks=[]
        )

        for sub_data in task_data.get("subtasks", []):
            subtask = Subtask(
                id=create_subtask_id(),
                name=sub_data["name"],
                description=sub_data["description"],
                estimate=sub_data.get("estimate", ""),
                status="to-do",
                task_id=task_id
            )
            task.subtasks.append(subtask)

        project.tasks.append(task)

    # Save
    projects = load_projects()
    projects.append(project.to_dict())
    save_projects(projects)
    return "✅ Project saved!"
    # return project


def ai_generate_task(prompt, project):
     pass

def ai_generate_subtasks(prompt, task):
     pass

def generate_response(prompt):
    pass
