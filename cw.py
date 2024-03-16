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
            date_s = input("Enter transaction date (formatted as 'yyyy-mm-dd'): ")
            date_f = "%Y-%m-%d"
            datetime.strptime(date_s, date_f)
        except ValueError:
            print("Invalid input, please enter valid transaction date formatted as 'yyyy-mm-dd'")
        else:
            return date_s

#file handelling functions
def loadTransactions():
    transactions = None
    try:
        with open('transactions.json', 'r') as file: #open the file transactions.json in read mode
            transactions = json.load(file)
    except FileNotFoundError:
        print("Saved transactions data file does not exist, Adding a new transaction will create one.")
    except json.JSONDecodeError:
        print("Error decoding exixting JSON file\n")
    finally:
        if transactions == None:
            return False
        elif len(transactions) == 0:
            return False
        else:
            return transactions

def saveTransactions(transactions):
    with open('transactions.json', 'w') as file: # open the file transactions.json in write mode
        json.dump(transactions, file, indent=1)

def returnToMainMenu():
    while True:
        print("\nEnter 1 to return to main menu.\nEnter 0 to exit the program.")
        selection = intInput(" Your choice: ")
        if selection == 1:
            print("Returning to main menu....\n")
            mainMenu()
        elif selection == 0:
            print("Exiting the program....\n")
            exit()
        else:
            print("Please enter a valid number.")
            continue
        break

def addTransaction():
    transactions = loadTransactions()
    if transactions == False:
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

def viewTransactions(topic = "\nView Transactions"):
    transactions = loadTransactions()
    if transactions == False:
        print("There is no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print(topic)
        print('')
        print("ID  Transaction")
        for i in range(len(transactions)):
            print(f"{i+1} - {transactions[i]}")
        print('')
        print("All saved transactions loded.")
        return transactions

def updateConf(transactions, ID, ChangeID, value, message):
    while True:
        yesno = input(f"Are you sure you want to update the transaction {message} (y/n): ").lower()
        if yesno == 'y':
            transactions[ID-1][ChangeID-1] = value
            saveTransactions(transactions)
            print(f"Transaction {message} updated succsessfully.")
            break
        elif yesno == 'n':
            print(f"Transaction {message} did not get updated.")
            break
        else:
            print("Invalid input, Enter 'y' for yes and 'n' for no")

def updateTransaction():
    transactions = viewTransactions("\nUpdate Transactions")
    print('')
    while True:
        ID = intInput("Enter the ID of the transaction you want to update: ")
        if 0 < (ID) < len(transactions):
            while True:
                print('')
                print(f"{ID} - {transactions[ID-1]}")
                print('')
                print("1. Amount")
                print("2. Category")
                print("3. Type")
                print("4. Date")
                while True:
                    ChangeID = intInput("Select what data you want change: ")
                    if ChangeID == 1:
                        while True:
                            T_amount = floatInput("Enter the new transaction amount: ", "Please enter a valid amount in numbers.")
                            if T_amount > 0:
                                updateConf(transactions, ID, ChangeID, T_amount, "amount")
                                break
                            else:
                                print("Please enter a valid amount (amount should be higher than 0).")
                        break
                    elif ChangeID == 2:
                        while True:
                            T_category = input("Enter the new category of the transaction: ")
                            if len(T_category) > 0:
                                updateConf(transactions, ID, ChangeID, T_category, "category")
                                break
                            else:
                                print("You can't keep transaction category empty.")
                        break
                    elif ChangeID == 3:
                        print("Transaction type")
                        print(" 1. Income")
                        print(" 2. Expense")
                        while True:
                            T_typeN = intInput("Enter the new transaction type (1/2): ", "Input is not valid, check and try again. Input should be 1 or 2.")
                            if T_typeN == 1:
                                T_type = "Income"
                                updateConf(transactions, ID, ChangeID, T_type, "type")
                                break
                            elif T_typeN == 2:
                                T_type = "Expense"
                                updateConf(transactions, ID, ChangeID, T_type, "type")
                                break
                            else:
                                print("Input is not valid, check and try again. Input should be 1 or 2.")
                        break
                    elif ChangeID == 4:
                        T_date = dateInput()
                        updateConf(transactions, ID, ChangeID, T_date, "date")
                        break
                    else:
                        print("Please select a valid input.")
                anotherEdit = input("Enter 'A' to change another data type in the selected transaction, Enter any ket to exit : ").lower()
                if anotherEdit == 'a':
                    continue
                else:
                    break
            break
        else:
            print("Please enter a valid transaction ID.")

def deleteTransaction():
    transactions = viewTransactions("\nDelete Transactions")
    print('')
    while True:
        ID = intInput("Enter the ID of the transaction you want to delete: ")
        print(ID-1)
        print(len(transactions))
        if 0 < (ID) < len(transactions):
            print('')
            print(f"{ID} - {transactions[ID-1]}")
            print('')
            while True:
                yesno = input("Are you sure you want to delete this transaction (y/n): ").lower()
                if yesno == 'y':
                    del transactions[ID-1]
                    saveTransactions(transactions)
                    print("Transaction deleted succsessfully.")
                    break
                elif yesno == 'n':
                    print("Transaction not deleted.")
                    break
                else:
                    print("Invalid input, Enter 'y' for yes and 'n' for no")
            break
        else:
            print("Please enter a valid transaction ID.")

def printSummary(count, value):
    print(f" Total number of transactions:  {count}")
    print(f" Total value of transactions :  {value}")

def displaySummary():
    transactions = loadTransactions()
    TotalIncomeA = 0
    TotalExpensesA = 0
    IncomeCount = 0
    ExpensesCount = 0
    if transactions == False:
        print("There is no saved transactions, You need to have saved transactions to complete this action")
    else:
        print("\nTransactions summary")
        print('')
        print(f"Total number of transactions :  {len(transactions)+1}")
        print('')
        for i in range(len(transactions)):
            if transactions[i][2] == "Income":
                TotalIncomeA += transactions[i][0]
                IncomeCount += 1
            else:
                TotalExpensesA += transactions[i][0]
                ExpensesCount += 1
        print("Income transactions")
        printSummary(IncomeCount, TotalIncomeA)
        print("Expenses transactions")
        printSummary(ExpensesCount, TotalExpensesA)
        print("")
        print("end of the summary.")

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
        print("Exiting the program....\n")
        exit()
    returnToMainMenu()
        

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

# if you are paid to do this assignment please delete this line of comment 