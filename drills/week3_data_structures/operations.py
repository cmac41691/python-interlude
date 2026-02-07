def view_contacts(contact_list):
    if not contact_list:
        print("No contacts found")
    else:
        for contact in contact_list:
            print(f"{contact['name']}, {contact['phone']}, {contact['email']}")


def search_contact(contact_list):
    search_name = input("Searching for contact information: ")

    for contact in contact_list:
        if contact["name"] == search_name:
            print(f"{contact} has been found")
            return

    print("Contact Not Found")