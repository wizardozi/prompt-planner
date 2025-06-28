import click
from utils import create_project_id, create_task_id, create_subtask_id
from storage import load_projects, save_projects
from subtask import Subtask
from task import Task
from project import Project
@click.group
def myCommands():
    pass

@click.command()
@click.option('--name', prompt='Name', help='Write a project name.')
@click.option('--desc', prompt='Description', help='Write a project description.')
def add_project(name, desc):
    project = Project(
        id=create_project_id(),
        name=name,
        description=desc,
        tasks=[]
    )
    all_projects = load_projects()
    all_projects.append(project.to_dict())
    save_projects(all_projects)
    click.echo(f"New project name: {name}")

@click.command()
def add_task():
    projects = load_projects()
    # Print project names with indexes
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    selected_idx = click.prompt("Select project by number", type=int) - 1
    selected_project = projects[selected_idx]

    label = click.prompt("Task label")
    description = click.prompt("Task description")
    task = Task(
        id=create_task_id(),
        label=label,
        description=description,
        due_by=None,
        status="incomplete",
        priority="medium",
        project_id=selected_project['id'],
        subtasks=[],
    )
    selected_project['tasks'].append(task.to_dict())
    save_projects(projects)
    click.echo(f"Added task to project: {selected_project['name']}")

myCommands.add_command(add_project)
myCommands.add_command(add_task)

if __name__ == '__main__':
    myCommands()