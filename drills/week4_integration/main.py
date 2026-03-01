from persistence import load_data, save_data
from commands import commands

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