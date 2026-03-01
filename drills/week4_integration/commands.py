def operate_update(data, commands):
    data["updated"] = True
    return True

def operate_help(data, commands):
    print("\nAvailable commands:")
    for name, meta in commands.items():
        print(f"- {name}: {meta['description']}")
    print("- quit: Exit the CLI")
    return False


commands = {
    "help": {
        "handler": operate_help,
        "description": "Show available commands"
    },
    "update": {
        "handler": operate_update,
        "description": "Mark application state as updated"
    }
}