### Week 3 – Contact Manager (Early Progress)

This week I focused on designing the contact manager using pseudocode before writing Python.
I defined core helper functions such as `create_contact` and `add_contact` and verified that they work together correctly.

One important realization was understanding that defining functions alone does not execute any logic.
Running the script multiple times produced no output, which helped reinforce how Python executes files top-down and only runs code that is explicitly called.

I also practiced passing data structures (lists and dictionaries) between functions and using helper functions to avoid duplication.
This project is helping me understand how larger programs are built from small, focused pieces.

Next steps will be implementing the remaining contact operations (view, search, update, delete) and adding a main loop to connect everything together.  


Implemented view_contacts after correcting logic errors around empty lists and dictionary access. Learned to check collection state (if not list) instead of invalid sentinel values and to format output using f-strings with dictionary keys.


### Update Contact — Search & Mutation Logic 

Implemented update_contact by identifying contacts via a user-provided key (name) and mutating dictionary values inside a list.

This function was challenging because it required combining multiple concepts at once:
- searching through a list of dictionaries
- comparing dictionary values to user input
- safely mutating dictionary fields in-place
- controlling program flow with early returns and a fallback case

A key realization was that dictionaries inside lists are mutable, so updating the dictionary directly updates the contact in the list without needing to recreate it.

I also reinforced the importance of placing the "Contact not found" message *after* the loop, ensuring it only runs when no match is found.

This function helped connect the upper-level logic (user commands) with lower-level data mutation and clarified how real programs manage state across multiple functions.
