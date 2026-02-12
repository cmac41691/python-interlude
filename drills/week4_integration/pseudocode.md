
START PROGRAM

INITIALIZE application state
    (example: running = true)

INITIALIZE application data (if needed)

DISPLAY welcome message
DISPLAY available commands

WHILE application is running

    ASK user for command input
    NORMALIZE input (trim, lowercase)

    IF input is empty
        DISPLAY error message
        CONTINUE loop
    END IF

    IF input is "help"
        DISPLAY detailed help menu
        CONTINUE loop
    END IF

    IF input is "q" OR "quit"
        DISPLAY exit message
        SAVE data if necessary
        SET application state to stopped
        BREAK loop
    END IF

    IF input is not a known command
        DISPLAY "unknown command"
        CONTINUE loop
    END IF

    IF input is a original command
        ROUTE command to correct handler

        IF handler modifies data
            UPDATE application state
            SAVE data if necessary    
        END IF

    END IF

END WHILE

DISPLAY shutdown message
END PROGRAM