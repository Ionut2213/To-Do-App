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