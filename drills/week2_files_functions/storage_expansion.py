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


