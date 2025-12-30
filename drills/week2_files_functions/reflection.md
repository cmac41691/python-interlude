# Week 2 Reflection — Files & Functions (JSON Storage)

This week focused on persistent storage using files and JSON.

I successfully implemented:
- A `load_data()` function that checks if a file exists and loads JSON safely
- A `save_data(data)` function that writes updated state back to disk
- A `while True` loop that continuously accepts user input
- A clean exit condition (`q` / `quit`)
- Controlled updates to a single data field (`last_action`)

Key things I learned:
- File existence checks (`os.path.exists`) are critical before reading
- JSON acts like a lightweight database when combined with dictionaries
- Separating read/write logic into functions makes the code easier to extend
- Persistence changes how programs are designed compared to stateless scripts

This code now forms a stable foundation for:
- Viewing stored data
- Expanding into a CLI menu
- Tracking session counts or user actions over time

Overall, this felt like real backend work rather than a toy exercise.
