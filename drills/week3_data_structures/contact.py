def create_contact(name, phone, email):
    """
    Creates and returns a contact dictionary.
    """
    return {
        "name": name,
        "phone": phone,
        "email": email
    }


def add_contact(contact_list):
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    email = input("Enter your email: ")

    contact = create_contact(name, phone, email)
    contact_list.append(contact)


def update_contact(contact_list):
    name_to_discover = input("Enter name to update: ")

    for contact in contact_list:
        if contact["name"] == name_to_discover:
            new_name = input("New name: ")
            new_phone = input("New phone: ")
            new_email = input("New email: ")

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            print("Contact updated")
            return

    print("Contact not found")


def delete_contact(contact_list):
    delete_name = input("Enter name to delete: ")

    for contact in contact_list:
        if contact["name"] == delete_name:
            contact_list.remove(contact)
            print(f"Contact removed: {contact['name']}")
            return

    print("Contact not found")