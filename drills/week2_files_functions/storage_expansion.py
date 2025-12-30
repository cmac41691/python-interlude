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
    user_input = input("Enter an action (or 'q' to quit): ")

    if user_input == "q" or user_input == "quit":
        print("Exiting program")
        save_data(data)
        break

    # update ONE field only
    data["last_action"] = user_input

    save_data(data)
