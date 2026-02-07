from contact import add_contact, update_contact, delete_contact
from operations import view_contacts, search_contact


def run_contact_manager():
    contacts = []

    while True:
        command = input(
            "add, view, search, update, delete, q: "
        ).strip().lower()

        if command == "add":
            add_contact(contacts)

        elif command == "view":
            view_contacts(contacts)

        elif command == "search":
            search_contact(contacts)

        elif command == "update":
            update_contact(contacts)

        elif command == "delete":
            delete_contact(contacts)

        elif command == "q":
            break

        else:
            print("Unknown command")

if __name__ == "__main__": 
    run_contact_manager()