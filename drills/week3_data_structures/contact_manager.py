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


