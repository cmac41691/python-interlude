import os
import json

FILE_PATH = "data.json"


def get_default_data():
    """
    Returns the default data structure used when no data file exists.
    """
    return {
        "total_sessions": 0,
        "last_action": "none"
    }


def load_data():
    """
    Loads stored data from disk if it exists.
    Returns default data if the file is missing or unreadable.
    """
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return get_default_data()


def save_data(data):
    """
    Saves the provided data dictionary to disk as JSON.
    """
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

