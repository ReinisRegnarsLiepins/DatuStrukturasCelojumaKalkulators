def doStartingPromt():
    print("*****************************************************")
    print("Travel reimbursement calculator for Erasmus+ projects")
    print("*****************************************************")
    print("")
    print("Izmanto 'help', lai redzētu pieejamās komandas")

def doHelpPromt():
    print("\n--- Help Menu: List of All Commands ---\n")
    print("General format: command -arg1 -arg2 -arg3 ...\n")

    print("help")
    print("    Shows this help menu.\n")

    print("new -<trip name> -<total reimbursement>")
    print("    Creates a new trip with the given name and reimbursement budget.")
    print("    Example: new -Latvia mobility -300\n")

    print("select -<index>")
    print("    Selects a trip by index for editing or viewing.")
    print("    Example: select -1\n")

    print("deselect")
    print("    Deselects the currently selected trip.\n")

    print("show trip")
    print("    Displays a summary of the selected trip.\n")

    print("show expenses")
    print("    Displays a list of all expenses in the selected trip.\n")

    print("show all")
    print("    Shows a brief overview of all created trips.\n")

    print("edit trip -<field> -<value>")
    print("    Edits the selected trip's name or total reimbursement.")
    print("    Fields: 'name' or 'total reimbursement'")
    print("    Example: edit trip -name -Berlin Mobility")
    print("             edit trip -total reimbursement -400\n")

    print("add expense -<amount> -<transport> [-<can be reimbursed>] [-<notes>]")
    print("    Adds an expense to the selected trip.")
    print("    Optional: 'can be reimbursed' (true/false), notes.")
    print("    Example: add expense -120 -bus -true -to airport\n")

    print("remove expense -<expense number>")
    print("    Removes the expense by number (1-based index).")
    print("    Example: remove expense -2\n")

    print("save")
    print("    Saves all trip data to disk.\n")

    print("exit")
    print("    Exits the program.\n")
