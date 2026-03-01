import json  

JSON_PATH = "data.json"

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

