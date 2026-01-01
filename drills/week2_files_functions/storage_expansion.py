import os
import json

FILE_PATH = "data.json"


def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return {
            "total_sessions": 0,
            "last_action": "none"
        }


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


data = load_data()

while True:
    command = input("Enter a command (view, update, q): ").strip().lower()

    if command == "view":
        print("\n=== Stored Data ===")
        print(f"Total Sessions: {data['total_sessions']}")
        print(f"Last Action: {data['last_action']}")
        print("===================\n")

    elif command == "update":
        new_action = input("Enter new action: ").strip()
        data["last_action"] = new_action
        save_data(data)
        print("Action updated.\n")

    elif command == "q":
        print("Exiting program.")
        save_data(data)
        break

    else:
        print("Unknown command.\n")
