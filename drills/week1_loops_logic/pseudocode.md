START

WHILE TRUE
    ASK user for input

    IF input is "q" or "quit"
        DISPLAY exit message
        EXIT program
    END IF

    IF input is invalid
        DISPLAY error message
        CONTINUE loop
    END IF

    IF input is a valid number
        CHECK if number is even or odd
        DISPLAY result
    END IF

END WHILE

END
