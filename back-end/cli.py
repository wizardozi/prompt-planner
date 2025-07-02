import click
from utils import create_project_id, create_task_id, create_subtask_id, ask_yes_no
from settings import ALLOWED_PRIORITIES, ALLOWED_STATUSES, PROJECT_CATEGORIES
from storage import load_projects, save_projects, load_categories, save_categories
from subtask import Subtask
from task import Task
from project import Project
from datetime import datetime, timedelta
from helper import prompt_estimate_rounded, parse_time_estimate
from ai_engine import ai_generate_project, ai_generate_task, ai_generate_subtasks


@click.group
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Name', help='Write a project name.')
@click.option('--description','--desc', prompt='Description', help='Write a project description.')
def add_project(name, description):
    categories = load_categories()
    for idx, cat in enumerate(categories):
        click.echo(f"{idx + 1}. {cat}")
    selected_idx = click.prompt('Select a category by number or type a new one', type=str)

    # Check if new category was typed
    if selected_idx.isdigit():
        category = categories[int(selected_idx) - 1]
    else:
        category = selected_idx
        if category not in categories:
            categories.append(category)
            save_categories(categories)

    project = Project(
        id=create_project_id(),
        name=name,
        description=description,
        category=category,
        tasks=[]
    )
    all_projects = load_projects()
    all_projects.append(project.to_dict())
    save_projects(all_projects)
    click.echo(f"New project name: {name}, Category: {category}")

@cli.command()
def add_task():
    projects = load_projects()
    if not projects:
        click.echo("No projects found. Please add a project first using 'planner add-project'.")
        return
    # Print project names with indexes
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    selected_idx = click.prompt("Select project by number", type=int) - 1
    selected_project = projects[selected_idx]

    label = click.prompt("Task label")
    description = click.prompt("Task description")
    for idx, p in enumerate(ALLOWED_PRIORITIES):
        click.echo(f"{idx + 1}. {p}")
    selected_idx = click.prompt('Select task priorty by number', type=int) - 1
    selected_priority = ALLOWED_PRIORITIES[selected_idx]
    task = Task(
        id=create_task_id(),
        label=label,
        description=description,
        due_by=None,
        status="to-do",
        priority=selected_priority,
        project_id=selected_project['id'],
        subtasks=[],
    )
    selected_project['tasks'].append(task.to_dict())
    save_projects(projects)
    click.echo(f"Added task to project: {selected_project['name']}")

@cli.command()
def add_subtask():
    projects = load_projects()
    # Print project names with indexes
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    selected_idx = click.prompt("Select project by number", type=int) - 1
    selected_project = projects[selected_idx]

    tasks = selected_project["tasks"]
    if not tasks:
        click.echo("No tasks found. Please add a task first using 'planner add-task'.")
        return
    # for idx, task in enumerate(selected_project["tasks"]):
    for idx, task in enumerate(tasks):
        # tasks.append(task)
        click.echo(f"{idx + 1}. {task['label']}")
    selected_idx = click.prompt("Select task by number", type=int) - 1
    selected_task = tasks[selected_idx]

    label = click.prompt("Subtask label")
    description = click.prompt("Subtask description")
    estimate = prompt_estimate_rounded()

    subtask = Subtask(
        id=create_subtask_id(),
        label=label,
        description=description,
        estimate=estimate,
        status="to-do",
        task_id=selected_task['id']
    )
    selected_task['subtasks'].append(subtask.to_dict())
    save_projects(projects)
    click.echo(f"Added subtask to task: {selected_task['label']}")

@cli.command()
def edit_project():
    projects = load_projects()
    if not projects:
        click.echo("No projects found. Please add a project first using 'planner add-project'.")
        return
    for p_idx, proj in enumerate(projects):
        click.echo(f"{p_idx + 1}. {proj['name']}")
    proj_idx = click.prompt("Select project by number", type=int) - 1
    project = projects[proj_idx]

    click.echo("Press enter to keep current value")
    project["name"] = click.prompt("Edit name", default=project["name"])
    project["description"] = click.prompt("Edit description", default=project["description"])

    save_projects(projects)

@cli.command()
def edit_task():
    projects = load_projects()
    if not projects:
        click.echo("No projects found. Please add a project first using 'planner add-project'.")
        return
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    proj_idx = click.prompt("Select project by number", type=int) - 1
    project = projects[proj_idx]
    tasks = project['tasks']

    for idx, t in enumerate(tasks):
        click.echo(f"{idx + 1}. {t['label']}")
    task_idx = click.prompt("Select task by number", type=int) - 1
    task = tasks[task_idx]

    click.echo("Press enter to keep current value")
    task["label"] = click.prompt("Edit label", default=task["label"])
    task["description"] = click.prompt("Edit description", default=task["description"])
    task["due_by"] = click.prompt("Edit due by date (YYYY-MM-DD)", default=task["due_by"])
    task["status"] = click.prompt(
        "Edit status",
        type=click.Choice(ALLOWED_STATUSES, case_sensitive=False),
        default=task["status"]
    )
    task["priority"] = click.prompt(
        "Edit priority",
        type=click.Choice(ALLOWED_PRIORITIES, case_sensitive=False),
        default=task["priority"]
    )
    save_projects(projects)

@cli.command()
def edit_subtask():
    projects = load_projects()
    if not projects:
        click.echo("No projects found. Please add a project first using 'planner add-project'.")
        return

    for idx, p in enumerate(projects):
        click.echo(f"{idx + 1}. {p['name']}")
    p_idx = click.prompt("Select project by number", type=int) - 1
    project = projects[p_idx]

    tasks = project['tasks']
    for idx, t in enumerate(tasks):
        click.echo(f"{idx + 1}. {t['label']}")
    t_idx = click.prompt("Select task by number", type=int) - 1
    task = tasks[t_idx]

    subtasks = task["subtasks"]
    if not subtasks:
        click.echo("No subtasks found for selected task. Please add a subtask first using 'planner add-subtask'.")
        return

    for idx, s in enumerate(subtasks):
        click.echo(f"{idx + 1}. {s['label']}")
    s_idx = click.prompt("Select subtask by number", type=int) - 1
    subtask = subtasks[s_idx]

    click.echo("Press enter to keep current value")
    subtask["label"] = click.prompt(
        "Edit label",
        default=subtask["label"]
    )
    subtask["description"] = click.prompt(
        "Edit description",
        default=subtask["description"]
    )
    estimate_input = click.prompt(
        "Edit time estimate (e.g., 1.5, 90m, 1h, 1:15)",
        default="",
        show_default=False
    )
    if estimate_input.strip():
        try:
            subtask["estimate"] = str(parse_time_estimate(estimate_input.strip()))
        except ValueError:
            click.echo("Invalid time format. Estimate unchanged.")
    else:
        click.echo("Estimate unchanged.")

    subtask["status"] = click.prompt(
        "Edit status",
        type=click.Choice(ALLOWED_STATUSES, case_sensitive=False),
        default=subtask["status"]
    )
    save_projects(projects)

@cli.command()
def delete_project():
    projects = load_projects()
    if not projects:
        click.echo("No projects to delete.")
        return

    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    proj_idx = click.prompt("Select project to delete by number", type=int) - 1
    project = projects[proj_idx]

    if ask_yes_no(f"Are you sure you want to delete project '{project['name']}'? (y/n)"):
        projects.pop(proj_idx)
        save_projects(projects)
        click.echo("Project deleted.")

@cli.command()
def delete_task():
    projects = load_projects()
    if not projects:
        click.echo("No projects found.")
        return

    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    proj_idx = click.prompt("Select project by number", type=int) - 1
    project = projects[proj_idx]
    tasks = project['tasks']

    if not tasks:
        click.echo("No tasks to delete.")
        return

    for idx, task in enumerate(tasks):
        click.echo(f"{idx + 1}. {task['label']}")
    task_idx = click.prompt("Select task to delete by number", type=int) - 1
    task = tasks[task_idx]

    if ask_yes_no(f"Delete task '{task['label']} (y/n)'?"):
        tasks.pop(task_idx)
        save_projects(projects)
        click.echo("Task deleted.")

@cli.command()
def delete_subtask():
    projects = load_projects()
    if not projects:
        click.echo("No projects found.")
        return

    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    proj_idx = click.prompt("Select project by number", type=int) - 1
    project = projects[proj_idx]

    tasks = project["tasks"]
    for idx, task in enumerate(tasks):
        click.echo(f"{idx + 1}. {task['label']}")
    task_idx = click.prompt("Select task by number", type=int) - 1
    task = tasks[task_idx]

    subtasks = task["subtasks"]
    if not subtasks:
        click.echo("No subtasks to delete.")
        return

    for idx, sub in enumerate(subtasks):
        click.echo(f"{idx + 1}. {sub['label']}")
    sub_idx = click.prompt("Select subtask to delete by number", type=int) - 1
    subtask = subtasks[sub_idx]

    if ask_yes_no(f"Delete subtask '{subtask['label']}'? (y/n)"):
        subtasks.pop(sub_idx)
        save_projects(projects)
        click.echo("Subtask deleted.")

@cli.command()
def show_projects():
    projects = load_projects()
    # Print project names with indexes
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")

@cli.command()
def move_task():
    projects = load_projects()
    if not projects:
        click.echo("No projects found.")
        return

    # Select source project
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    src_proj_idx = click.prompt("Select source project by number", type=int) - 1
    src_project = projects[src_proj_idx]

    if not src_project['tasks']:
        click.echo("No tasks found in this project.")
        return

    # Select task to move
    for idx, task in enumerate(src_project['tasks']):
        click.echo(f"{idx + 1}. {task['label']}")
    task_idx = click.prompt("Select task to move by number", type=int) - 1
    task = src_project['tasks'].pop(task_idx)

    # Select destination project
    for idx, proj in enumerate(projects):
        click.echo(f"{idx + 1}. {proj['name']}")
    dest_proj_idx = click.prompt("Select destination project by number", type=int) - 1
    dest_project = projects[dest_proj_idx]

    # Update task's project_id and move it
    task['project_id'] = dest_project['id']
    dest_project['tasks'].append(task)

    save_projects(projects)
    click.echo(f"Moved task '{task['label']}' to project '{dest_project['name']}'.")

@cli.command()
@click.option(
    "--view",
    type=click.Choice(["today", "week", "range"], case_sensitive=False),
    prompt="View tasks for",
    help="Choose a time filter: today, week, or range."
)
def show_tasks(view):
    projects = load_projects()
    now = datetime.now()

    if view == "today":
        target_date = now.date()
        click.echo("Tasks due today:")
    elif view == "week":
        start = now.date()
        end = (now + timedelta(days=7)).date()
        click.echo("Tasks due this week:")
    elif view == "range":
        start_str = click.prompt("Start date (YYYY-MM-DD)")
        end_str = click.prompt("End date (YYYY-MM-DD)")
        try:
            start = datetime.strptime(start_str, "%Y-%m-%d").date()
            end = datetime.strptime(end_str, "%Y-%m-%d").date()
        except ValueError:
            click.echo("Invalid date format. Use YYYY-MM-DD.")
            return
        click.echo(f"Tasks due from {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}:")

    for proj in projects:
        for task in proj["tasks"]:
            due_str = task.get("due_by")
            if due_str:
                try:
                    due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
                except ValueError:
                    continue  # skip tasks with invalid date format
                show = False
                if view == "today":
                    show = due_date == now.date()
                elif view == "week":
                    show = start <= due_date <= end
                elif view == "range":
                    show = start <= due_date <= end
                if show:
                    total_estimate = 0
                    for subtask in task["subtasks"]:
                        if subtask["status"] != "done":
                            total_estimate += float(subtask["estimate"])

                    click.echo(f"- [{task['status']}] {task['name']} (Project: {proj['name']}) (Due: {due_date.strftime('%Y-%m-%d')}) (Estimate: {total_estimate}h)")
                    click.echo(f"   {task['description']}\n")
@cli.command()
@click.option('--project', '--proj', is_flag=True, help="Generate a new Project with Tasks and Subtasks")
@click.option('--task', is_flag=True, help="Generate Tasks for selected project")
@click.option('--subtask', '--sub', is_flag=True, help="Generate Subtasks for selected Task")
def generate(project, task, subtask):
    # Generates a Project, Tasks or Subtasks from a prompt
    if not project and not task and not subtask:
        click.echo("Please use one of the flags. 'planner generate --help'")
        return
    # prompt = click.prompt('prompt')
    prompt = "Build a time-tracking tool for freelancers. It should help users log billable hours by project and task, set priorities, and view weekly summaries. I would like to have this project done in the next month."
    click.echo(f"[MOCK PROMPT] {prompt}")
    if project:
        # ai_generate_project(prompt)
        click.echo(ai_generate_project(prompt))
    else:
        projects = load_projects()
        # Print project names with indexes
        for idx, proj in enumerate(projects):
            click.echo(f"{idx + 1}. {proj['name']}")
        selected_idx = click.prompt("Select project by number", type=int) - 1
        selected_project = projects[selected_idx]

        if task:
            ai_generate_task(prompt, selected_project)
        else:
            tasks = selected_project["tasks"]
            if not tasks:
                click.echo("No tasks found. Please add a task first using 'planner add-task' or 'planner generate --task'.")
                return
            for idx, task in enumerate(tasks):
                click.echo(f"{idx + 1}. {task['label']}")
            selected_idx = click.prompt("Select task by number", type=int) - 1
            selected_task = tasks[selected_idx]
            ai_generate_subtasks(prompt, selected_task)

@cli.command()
def done():
    pass
    # mark task or subtask as done


if __name__ == '__main__':
    cli()