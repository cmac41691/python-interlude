START

DEFINE create_contact(name, phone, email)
    RETURN {
        "name": name,
        "phone": phone,
        "email": email
    }
END FUNCTION


DEFINE add_contact(contact_list)
    ASK user for name
    ASK user for phone
    ASK user for email

    CREATE contact using create_contact
    ADD contact to contact_list
END FUNCTION


DEFINE view_contacts(contact_list)
    IF contact_list is empty
        DISPLAY "No contacts found"
    ELSE
        FOR each contact in contact_list
            DISPLAY name, phone, email
END FUNCTION


DEFINE search_contact(contact_list)
    ASK user for name to search

    FOR each contact in contact_list
        IF contact name matches search term
            DISPLAY contact
            RETURN

    DISPLAY "Contact not found"
END FUNCTION


DEFINE delete_contact(contact_list)
    ASK user for name to delete

    FOR each contact in contact_list
        IF contact name matches
            REMOVE contact from contact_list
            DISPLAY "Contact removed"
            RETURN

    DISPLAY "Contact not found"
END FUNCTION


DEFINE run_contact_manager
    SET contacts = empty list

    WHILE program is running
        ASK user for command (add, view, search, delete, q)

        IF command is "add"
            CALL add_contact

        ELSE IF command is "view"
            CALL view_contacts

        ELSE IF command is "search"
            CALL search_contact

        ELSE IF command is "delete"
            CALL delete_contact

        ELSE IF command is "q"
            EXIT program

        ELSE
            DISPLAY "Unknown command"
END WHILE

END
