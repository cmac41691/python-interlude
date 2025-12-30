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
    ASK user for input

    IF input is "q" or "quit"
        DISPLAY exit message
        SAVE data
        EXIT loop
    END IF

    UPDATE last_action with user input
    SAVE data
END WHILE

END
