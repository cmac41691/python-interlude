import json  

JSON_PATH = "data.json"

# ==========================================================
# TODO (Next Evolution Steps)
# - Replace "updated" placeholder with real application state
# - Improve help output formatting
# - Move CLI loop into main() function
# - Add unit tests for load_data and save_data
# ==========================================================
def load_data():
    try:
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No existing data file found. Starting fresh.")
        return {}
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting fresh.")
        return {}

def save_data(data):
    try:
        with open(JSON_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving data:", e)

def operate_help(data):
    print("Help placeholder")
    return False

def operate_update(data):
    data["updated"] = True
    return True

commands = {  
    "help": operate_help,
    "update": operate_update,
}

data = load_data()
data_modified = False

def user_menu():
    print("\nAvailable commands:")
    for cmd in commands:
        print("-", cmd)
    print("- quit")

user_menu()

print("Welcome to the CLI")
print('The commands that are available: "help", "update", "quit"')

while True:
    command = input('Please input a command (type "quit" to exit): ') \
        .strip() \
        .lower()

    if command == "":
        print("Error: command cannot be empty.")       
        continue

    if command in ("q", "quit"):
        break

    if command in commands:
        modified = commands[command](data)
        if modified:
            data_modified = True
    else:
        print("Unknown command.")

if data_modified:
    print("Data modified. Saving before shutdown...")
    save_data(data)

print("Shutting down cleanly.")