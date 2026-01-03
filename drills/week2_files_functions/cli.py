from storage_expansion import save_data

def run_cli(data):
    while True:
        command = input("Enter a command (view, update, q): ").strip().lower()

        if command == "view":
            print("\n=== Stored Data ===")
            print(f"Total Sessions: {data['total_sessions']}")
            print(f"Last Action: {data['last_action']}")
            print("====================\n")

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
