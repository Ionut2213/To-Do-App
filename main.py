import json

file_name = "todo_list.json"
completed_file_name = "completed_tasks.json"


# Funcția care încarcă task-urile din fișierul principal
def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}


# Funcția care salvează task-urile în fisierul principal
def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("ERROR during saving task")


# Funcția care încarcă task-urile completate
def load_completed_task():
    try:
        with open(completed_file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}


# Funcția care salvează task-urile completate
def save_completed_task(tasks):
    try:
        with open(completed_file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except:
        print("ERROR during saving completed task")


# Adăugarea unui task
def add_tasks(tasks):
    description = input("Enter Task Description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_task(tasks)
        print("Task was created successfully")
    else:
        print("Please enter a task description")


# Vizualizarea task-urilor
def view_tasks(tasks):
    task_list = tasks["tasks"]
    if not task_list:
        print("No tasks available")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["completed"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


# Ștergerea unui task
def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number that you want to delete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"].pop(task_number - 1)
            save_task(tasks)
            print("Your selected task was deleted successfully")
        else:
            print("Please enter a valid option")
    except ValueError:
        print("Please enter a valid option")


def mark_task_completion(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number that you want to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            completed_tasks = load_completed_task()
            completed_task = tasks["tasks"].pop(task_number - 1)
            completed_task["completed"] = True
            completed_tasks["tasks"].append(completed_task)
            save_task(tasks)
            save_completed_task(completed_tasks)  
            print("Your selected task has been MOVED to completed_task.json")
        else:
            print("Please enter a valid option")
    except ValueError:
        print("Please enter a valid option")


# Funcția principală
def main():
    tasks = load_task()
    while True:
        print("\n To-Do List Application")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Mark Tasks as completed")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            mark_task_completion(tasks)
        elif choice == "5":
            print("Exit the program")
            break
        else:
            print("Pick a valid choice")


# Apelarea funcției principale
main()
