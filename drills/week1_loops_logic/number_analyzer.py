def integer_input(text):
    if not text.isdigit():
        print("Error: enter a valid number")
        return None
    return int(text)


while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    # Quit condition
    if user_input == "q" or user_input == "quit":
        print("Quit session")
        break

    # Convert input
    number = integer_input(user_input)
    if number is None:
        continue

    # Even / odd check
    is_even = (number % 2 == 0)

    if is_even:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
