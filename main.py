from textPrompts import *
from trip import *
import pickle

doStartingPromt()

try:
    with open("data.pkl", "rb") as f:
        tripList = pickle.load(f)
except:
    tripList = []

currentTripSelection = -1

def displayTripSelection():
    print("---------------------------------------------------------------")
    if currentTripSelection == -1:
        print("-No trip selected-")
    else:
        print(f"Working with trip nr.{currentTripSelection}")

while True:
    displayTripSelection()

    inputValue = input("> ")
    command = inputValue.split("-", 1)[0].rstrip(" ")
    args = inputValue.split("-", 1)[-1]
    args = args.split("-")

    for i in range(len(args)):
        args[i] = args[i].lstrip()
        args[i] = args[i].rstrip()
        args[i] = args[i].lower()

    if command == "help":
        doHelpPromt()
    elif command == "new":
        try:
            trip = Trip(args[0], float(args[1]))
            trip.index = len(tripList)
            tripList.append(trip)

            print(f"Trip '{args[0]}' with a travel reimbursement of {args[1]} Eur was successfully created.")
        except:
            print("Failed to create a trip, please check the arguments given.")

    elif command == "select":
        if (int(args[0]) <= len(tripList)):
            currentTripSelection = int(args[0])
            print(f"Trip {args[0]} selected.")
        else:
            print(f"Trip number {args[0]} does not exist.")

    elif command == "deselect":
        currentTripSelection = -1

    elif command == "show trip":
        tripList[currentTripSelection - 1].displaySummary()

    elif command == "show expenses":
        tripList[currentTripSelection - 1].displayExpenses()
    elif command == "show all":
        if len(tripList) ==0:
            print("No trips added.")
        else:
            print("Showing all trips:")
            i = 0
            for trip in tripList:
                print(f"Nr. {i}: Trip '{trip.tripName}', total reimbursement: {trip.totalReembursment} Eur.")

    elif command == "edit trip":
        try:
            if currentTripSelection == -1:
                print("No trip selected, please select a trip to edit by using 'select -index'.")
            else:
                trip = tripList[currentTripSelection]
                if args[0] == "total reimbursement":
                    trip.totalReembursment = float(args[1])
                    print(f"Changed trip's nr. {currentTripSelection} total reimbursement to {args[1]} Eur.")
                elif args[0] == "name":
                    trip.tripName = args[1]
                    print(f"Changed trip's nr. {currentTripSelection} name to '{args[1]}'.")
                else:
                    print("First argument in not valid.")
        except:
            print(f"Failed to edit trip nr.{currentTripSelection}, please check the arguments given.")

    elif command == "add expense":
        if currentTripSelection == -1:
            print("No trip selected, please select a trip to add the expense to by using 'select -index'.")
        else:
            try:
                if len(args) == 2:
                    expense = Expense(float(args[0]), args[1])
                elif len(args) == 3:
                    expense = Expense(float(args[0]), args[1], args[2])
                else:
                    expense = Expense(float(args[0]), args[1], args[2], args[3])
                tripList[currentTripSelection-1].addExpense(expense)
                print(f"Expense of {args[0]} Eur was added to trip nr.{currentTripSelection}")
            except:
                print(f"Failed to add an expense to trip nr.{currentTripSelection}, please check the arguments given.")
    elif command == "remove expense":
        if currentTripSelection == -1:
            print("No trip selected, please select a trip to add the expense to by using 'select -index'.")
        else:
            try:
                tripList[currentTripSelection-1].removeEpense(int(args[0])-1)
                print(f"Expense nr.{args[0]} was removed from trip nr.{currentTripSelection}")
            except:
                print(f"Failed to remove an expense from trip nr.{currentTripSelection},"
                      f" please check the arguments given.")
    elif command == "save":
        with open("data.pkl", "wb") as f:
            pickle.dump(tripList, f)
        print("All changes saved.")

    elif command == "exit":
        print("Exiting.")
        break
    else:
        print(f"Command '{command}' not recognized use 'help' to view all available commands.")
