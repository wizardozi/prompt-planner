from yaspin import yaspin
# from ai_engine import generate_project_response
# from parser import parse_response_to_project
# from storage import save_project
from cli import cli

def display_tasks(structured):
    for section in structured:
        print(f"\n{section['label']}")
        for i, sub in enumerate(section["subtasks"], 1):
            print(f"  {i}. {sub}")

def main():
    pass
    # print("[MOCK] What's your task?")
    # prompt = "Break this task into a sequence of subtasks scheduled over time. Include estimated durations or target dates. Task: "
    # task = "I want to integrate an AI model into my planning app to assist with generating subtasks associated with a project or tasks."
    # prompt += task
    # print(prompt)
    # with yaspin(text="Thinking...", color="cyan") as spinner:
    #     response = generate_project_response(prompt)

    #     project = parse_response_to_project(response)

    #     save_project(project)

    # print("\nSuggested subtasks:")
    # display_tasks(response)

if __name__ == "__main__":
    cli()
    # main()