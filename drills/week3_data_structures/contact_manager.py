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
