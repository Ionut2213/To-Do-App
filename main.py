# Working with json files we need to import the module
import json
file_name = "todo_list.json"


# Function that handle to load the json file

def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}
    

# Function that handle th save in json file


def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("ERROR during saving task")



# Functions that handle to functionality of the app


def add_tasks(tasks):
    description = input("Enter Task Description:").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_task(tasks)
        print("Task was created successfully")
    else:
        print("Please enter a task description")



def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks available")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["completed"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


def delete_tasks(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number that you want to delete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"].pop(task_number - 1)
            save_task(tasks)
            print("Your selected task was deleted successfully")
        else:
            print("Please enter a valid option")
    except:
        print("Please enter a valid option")



def mark_task_completion(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number that you want to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_task(tasks)
            print("Your selected task status has been changed")
        else:
            print("Please enter a valid option")
    except:
        print("Print enter a valid option")
    



# here we gonna handle all the function that was created above
def main():
    tasks = load_task()
    while True:
        print("\n To-Do List Application")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Mark Tasks as completed")
        print("5. Exit")

        choice = input("Enter you choice: ").strip()
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




# Call the main function
main()