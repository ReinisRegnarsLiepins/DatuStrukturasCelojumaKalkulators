from linkedList import LinkedList

class Trip:
    def __init__(self, tripName, totalReembursment):
        self.totalReembursment = totalReembursment
        self.tripName = tripName

        self.expenseList = LinkedList()
        self.remainingBudget = totalReembursment
        self.overDraft = 0
        self.index = 0

    def addExpense(self, expense):
        self.expenseList.append(expense)

    def removeEpense(self, index):
        self.expenseList.pop(index)

    def rename(self, newName):
        self.tripName = newName

    def changeTotalReembursment(self, newAmmount):
        self.totalReembursment = newAmmount

    def displayExpenses(self):
        i = 1
        for expense in self.expenseList:
            print("")
            print(f" - Expense number {i}:")
            expense.display()
            i += 1

    def updateSummary(self):
        totalCost = 0
        for expense in self.expenseList:
            if expense.canBeReembursed:
                totalCost += expense.ammount
            else:
                self.overDraft += expense.ammount
        if totalCost > self.totalReembursment:
            self.overDraft += totalCost - self.totalReembursment

        self.remainingBudget = self.totalReembursment - totalCost

        if (self.remainingBudget < 0):
            self.remainingBudget = 0;

    def displaySummary(self):
        self.updateSummary()

        print(f" - Trip's {self.tripName} summary:")
        print(f"Remaining budget: {self.remainingBudget} Eur")
        print(f"Overdraft: {self.overDraft} Eur")
        print(f"(spent {self.totalReembursment-self.remainingBudget} of {self.totalReembursment} Eur)")
        print("")


class Expense:
    def __init__(self, ammount, modeOfTransport, canBeReembursed = "true", notes = ""):
        if (canBeReembursed.lower() in ["true", "yes", "can", "y"]):
            self.canBeReembursed = True
        elif canBeReembursed.lower in ["false", "no", "can not", "can't", "n"]:
            self.canBeReembursed = False
        else:
            raise ValueError

        self.notes = notes
        self.ammount = ammount
        self.modeOfTransport = modeOfTransport

    def display(self):
        print(f"Cost: {self.ammount} Eur.")
        print(f"Transport: {self.modeOfTransport}.")
        if (self.canBeReembursed):
            print("Can be reimbursed.")
        else:
            print("Can not be reimbursed")
        if (self.notes != ""):
            print(f"Notes: {self.notes}.")