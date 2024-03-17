import json
from datetime import datetime

#functions for inputs with error handelling
def intInput(inputMessage, errorMessage = "Invalid input, please try again.\n"): 
    #Get integer input from the user with error handling.
    while True:
        try:
            num = int(input(inputMessage))
        except ValueError:
            print(errorMessage)
        else:
            return num

def floatInput(inputMessage, errorMessage = "Invalid input, please try again.\n"): 
    #Get floating-point input from the user with error handling.
    while True:
        try:
            num = float(input(inputMessage))
        except ValueError:
            print(errorMessage)
        else:
            return num

def dateInput():
    #Get date input from the user with error handling.
    while True:
        try:
            date_s = input("Enter transaction date (formatted as 'yyyy-mm-dd'): ")
            date_f = "%Y-%m-%d"
            datetime.strptime(date_s, date_f)
        except ValueError:
            print("Invalid input, please enter valid transaction date formatted as 'yyyy-mm-dd'\n")
        else:
            return date_s

def amountInput():
    #Get transaction amount input from the user with error handling.
    while True:
        amount = floatInput("Enter the transaction amount: ", "Please enter a valid transaction amount in numbers.\n")
        fractionalAmount = str(amount).split('.')[1]
        print(fractionalAmount)
        if amount > 0 and len(fractionalAmount) < 3:
            amount_str = "{:.2f}".format(amount)
            return amount_str
            break
        else:
            print("Please enter a valid transaction amount.\n")

#file handelling functions
def loadTransactions():
    #Load transactions from the JSON file.
    transactions = None
    try:
        with open('transactions.json', 'r') as file: #open the file transactions.json in read mode
            transactions = json.load(file)
    except FileNotFoundError:
        print("Saved transactions data file does not exist, Adding a new transaction will create one.")
    except json.JSONDecodeError:
        print("Error decoding existing JSON file.\n")
    finally:
        if transactions == None:
            return False
        elif len(transactions) == 0:
            return False
        else:
            return transactions

def saveTransactions(transactions):
    #Save transactions to a JSON file.
    with open('transactions.json', 'w') as file: # open the file transactions.json in write mode
        json.dump(transactions, file, indent=1)

def returnToMainMenu():
    #Prompt the user to return to the main menu or exit the program.
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

# Feature implementations
def addTransaction():
    #Add a new transaction.
    transactions = loadTransactions() # Load transactions at the start
    if transactions == False:
        transactions = []
    print("\nAdd transaction")
    print('')
    T_amount = amountInput()
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
    #View all saved transactions.
    transactions = loadTransactions()
    if transactions == False:
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print(topic)
        print('')
        print("ID  Transaction")
        for i in range(len(transactions)):
            print(f"{i+1} - {transactions[i]}")
        print('')
        print("All saved transactions loaded.")
        return transactions

def updateConf(transactions, ID, ChangeID, value, message):
    #Prompt the confirmation from user to update a specific attribute of a transaction.
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
    #Update an existing transaction.
    transactions = viewTransactions("\nUpdate Transactions") #View transactions at start
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
                        T_amount = amountInput()
                        updateConf(transactions, ID, ChangeID, T_amount, "amount")     
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
    #Delete an existing transaction.
    transactions = viewTransactions("\nDelete Transactions") #View transactions at start
    print('')
    while True:
        ID = intInput("Enter the ID of the transaction you want to delete: ")
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
    #Print a summary of a transaction type.
    amount = "{:.2f}".format(value)
    print(f" Total number of transactions:  {count}")
    print(f" Total value of transactions :  {amount}")

def displaySummary():
    #Display summary of transactions.
    transactions = loadTransactions() # Load transactions at the start
    TotalIncomeA = 0
    TotalExpensesA = 0
    IncomeCount = 0
    ExpensesCount = 0
    if transactions == False:
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print("\nTransactions summary")
        print('')
        print(f"Total number of transactions :  {len(transactions)+1}")
        print('')
        for i in range(len(transactions)):
            if transactions[i][2] == "Income":
                TotalIncomeA += float(transactions[i][0])
                IncomeCount += 1
            else:
                TotalExpensesA += float(transactions[i][0])
                ExpensesCount += 1
        print("Income transactions")
        printSummary(IncomeCount, TotalIncomeA)
        print("Expenses transactions")
        printSummary(ExpensesCount, TotalExpensesA)
        print("")
        print("end of the summary.")

def menuChoice():
    #Handle user menu choice.
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
    returnToMainMenu() #calls return to menu/exit function
        
def mainMenu():
    #Main menu of the program.
    print("Personal Finance Tracker")
    print('')
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Display Summary")
    print("6. Exit")
    print('')

    menuChoice() #calls menu choice function

if __name__ == "__main__":
    mainMenu()

# if you are paid to do this assignment please delete this line of comment 