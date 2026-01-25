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

def view_contacts(contact_list):
    if not contact_list:
        print("No contacts found")
    else:
        for contact in contact_list:
            print(f"{contact['name']}, {contact['phone']}, {contact['email']}")  


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
    return


def search_contact(contact_list):
    search_name = input("Searching for contact information: ")

    for contact in contact_list:
        if contact["name"] == search_name:
            print(f"{contact} has been found")
            return

    print("Contact Not Found")

