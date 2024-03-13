import json
from datetime import datetime

#functions for inputs and error handelling
def intInput(inputMessage, errorMessage = "Invalid input, please try again.\n"):
    while True:
        try:
            num = int(input(inputMessage))
        except ValueError:
            print(errorMessage)
        else:
            return num
def floatInput(inputMessage, errorMessage = "Invalid input, please try again.\n"):
    while True:
        try:
            num = float(input(inputMessage))
        except ValueError:
            print(errorMessage)
        else:
            return num
def dateInput():
    while True:
        try:
            date_s = input("Enter transaction date (formated as 'yyyy-mm-dd'): ")
            date_f = "%Y-%m-%d"
            datetime.strptime(date_s, date_f)
        except ValueError:
            print("Invalid input, please enter transaction date formated as 'yyyy-mm-dd'")
        else:
            return date_s

#file handelling functions
def loadTransactions():
    try:
        with open('transactions.json', 'r') as file: #open the file transactions.json in read mode
            transactions = json.load(file)
    except FileNotFoundError:
        print("Saved transactions data file does not exits, Adding a new transaction will create one.\n")
    except json.JSONDecodeError:
        print("Error decoding exixting JSON file\n")
    else:
        return transactions

def saveTransactions(transactions):
    with open('transactions.json', 'w') as file: # open the file transactions.json in write mode
        json.dump(transactions, file)

def checkfordata():
    transactions = loadTransactions()
    if transactions == None:
        print("There is no saved transactions.")
        return False
    else:
        if len(transactions) > 0:
            return transactions
        else:
            return False

def returnToMainMenu():
    while True:
        print("\nEnter 1 to return to main menu.\nEnter 0 to exit the program.")
        selection = intInput(" Your choice: ")
        if selection == 1:
            print("Returning to main menu....\n")
            mainMenu()
        elif selection == 0:
            exit()
        else:
            print("Please enter a valid number.")
            continue
        break

def addTransaction():
    transactions = loadTransactions()
    if transactions == None:
        transactions = []
    print("\nAdd transaction")
    print('')
    while True:
        T_amount = floatInput("Enter the transaction amount: ", "Please enter a valid amount in numbers.")
        if T_amount > 0:
            break
        else:
            print("Please enter a valid amount (amount should be higher than 0).")
    while True:
        T_category = input("Enter the category of the transaction: ")
        if len(T_category) > 0:
            break
        else:
            print("You can't keep transaction category empty.")
    print("Transaction type")
    print(" 1. Income")
    print(" 2. Expense")
    while True:
        T_typeN = intInput("Enter the transaction type (1/2): ", "Input is not valid, check and try again. Input should be 1 or 2.")
        if T_typeN == 1:
            T_type = "Income"
            break
        elif T_typeN == 2:
            T_type = "Expense"
            break
        else:
            print("Input is not valid, check and try again. Input should be 1 or 2.")
    T_date = dateInput()

    transaction = [T_amount, T_category, T_type, T_date]
    transactions.append(transaction)
    saveTransactions(transactions)

    print("\nTransaction successfully added.")
    returnToMainMenu()


def viewTransactions():
    if checkfordata() == False:
        print("You need saved transaction data to complete this action")
        returnToMainMenu()
    else:
        transactions = checkfordata()
        print("\nView transactions")
        print('')
        for i in range(len(transactions)):
            print(f"{i+1} - {transactions[i]}")
        print("")
        print("All transactions loded.")
        returnToMainMenu()

def updateTransaction():
    pass

def deleteTransaction():
    pass

def displaySummary():
    transactions = loadTransactions()
    print(f"{transactions.count("Income")}")

    print()

def menuChoice():
    while True:
        choice = intInput("Enter your choice : ")
        if 1 <= choice <= 6:
            break
        else:
            print("Invalid choice, please try again.\n")
        print('')

    if choice == 1:
        addTransaction()
    elif choice == 2:
        viewTransactions()
    elif choice == 3:
        updateTransaction()
    elif choice == 4:
        deleteTransaction()
    elif choice == 5:
        displaySummary()
    else:
        print("Exiting program.")
        

def mainMenu():

    print("Personal Finance Tracker")
    print('')
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Display Summary")
    print("6. Exit")
    print('')

    menuChoice()

if __name__ == "__main__":
    mainMenu()