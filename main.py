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


def delete_tasks():
    pass



def mark_task_completion():
    pass



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
            delete_tasks()
        elif choice == "4":
            mark_task_completion()
        elif choice == "5":
            print("Exit the program")
            break
        else:
            print("Pick a valid choice")




# Call the main function
main()