START

DEFINE load_data()
    IF data file exists
        OPEN file
        READ JSON
        RETURN data
    ELSE
        RETURN default data structure
END FUNCTION

DEFINE save_data(data)
    OPEN file in write mode
    WRITE data as JSON
END FUNCTION

SET data = load_data()

WHILE program is running
    ASK user for command (input)

    IF command is "view"
        DISPLAY current stored data (print data)

    ELSE IF command is "update"
        ASK user for new action
        UPDATE last_action with new action
        SAVE data

    ELSE IF command is "q" or "quit"
        DISPLAY exit message
        SAVE data
        EXIT loop

    ELSE
        DISPLAY "Unknown command"
END WHILE

