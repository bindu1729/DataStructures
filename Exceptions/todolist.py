# Features:
# Add Task: Users can add new tasks to the to-do list with a description and due date.
# Update Task: Users can update the description or due date of an existing task.
# Complete Task: Users can mark tasks as completed.
# Display Tasks: Users can view their to-do list, including task details and completion status.
# Exception Handling: Implement try-except blocks to handle errors related to invalid input,
# task not found, and other unexpected scenarios.

# other rows are not remembered and stored in this dict
from tabulate import tabulate
import argparse

task_dict = {"task1":{"description":"Description of task1",
                      "status": "created",
                      "due_date": ""}
             }


def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise ValueError("One of the argument is None")
        if arg == "":
            raise ValueError("One of the argument is empty")


def add_task(name, desc, due_date):
    check_for_empty_or_none(name)
    if name in task_dict:
        raise ValueError("Task already exists")
    temp_dict = {"description": desc,
                 "status": "created",
                 "due_date": due_date}
    task_dict[name] = temp_dict


def update_task(name, key, value):
    check_for_empty_or_none(name)
    if name not in task_dict:
        raise ValueError("Task not found")
    if key not in task_dict[name]:
        raise ValueError(f"{key} not found in task details")
    task_dict[name][key] = value
    print(f"Updated {key} with {value} for the {name}")


def complete_task(name):
    update_task(name, key="status", value="completed")

def display_tasks():
    headers = ["Task Name", "Description", "Due Date", "Status"]
    rows = []
    for task in task_dict:
        row = [task, task_dict[task]["description"], task_dict[task]["due_date"], task_dict[task]["status"]]
        rows.append(row)
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='To-Do List',
        description='this program keeps track of to-do list')
    parser.add_argument('action', choices=['add_task', 'update_task_desc', 'update_task_due_date', 'complete_task',
                                           'display_todo_list'],
                        help="To-Do List choices")
    parser.add_argument('--task_name', type=str, help="Name of the task")
    parser.add_argument('--task_description', type=str, help="Description of the task", default=None)
    parser.add_argument('--task_due_date', type=str, help="Due Date of the task", default=None)
    args = parser.parse_args()
    if args.action == "add_task":
        add_task(name=args.task_name, desc=args.task_description, due_date=args.task_due_date)
        display_tasks()
    elif args.action == "update_task_desc":
        update_task(name=args.task_name, key="description", value=args.task_description)
        display_tasks()
    elif args.action == "update_task_due_date":
        update_task(name=args.task_name, key="due_date", value=args.task_due_date)
        display_tasks()
    elif args.action == "complete_task":
        complete_task(name=args.task_name)
        display_tasks()
    elif args.action == "display_todo_list":
        display_tasks()