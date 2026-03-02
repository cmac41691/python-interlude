from persistence import load_data, save_data
from commands import commands


def user_menu():
    print("\nAvailable commands:")
    for cmd in commands:
        print("-", cmd)
    print("- quit")


def main():
    data = load_data()
    data_modified = False

    user_menu()

    print("Welcome to the CLI")

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
            modified = commands[command]["handler"](data, commands)
            if modified:
                data_modified = True
        else:
            print("Unknown command.")

    if data_modified:
        print("Data modified. Saving before shutdown...")
        save_data(data)

    print("Shutting down cleanly.")


if __name__ == "__main__":
    main()