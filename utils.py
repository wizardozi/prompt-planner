import uuid
import click
def ask_yes_no(prompt="Confirm (y/n): "):
    while True:
        choice = click.prompt(prompt).strip().lower()
        if choice in ['y', 'n']:
            if choice == 'y':
                return True
            else:
                return False
        click.echo("Please enter 'y' or 'n'.")


def create_project_id():
    return f"proj_{uuid.uuid4().hex[:6]}"

def create_task_id():
    return f"task_{uuid.uuid4().hex[:6]}"

def create_subtask_id():
    return f"sub_{uuid.uuid4().hex[:6]}"

