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
        try: # make sure sure inputed date is in a valid format
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
        fractionalAmount = str(amount).split('.')[1] # get the decimal points of the transaction seperatly
        if amount > 0 and len(fractionalAmount) < 3: # make sure inputed transaction amount is valid
            amount_str = "{:.2f}".format(amount) # convert the transaction amount to a string with two decimal points
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
    finally:# check whether there are saved transactions in the file
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
        selection = intInput(" Your choice: ") # ask the user wheather to exit to the menu or exit from the program
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
    if transactions == False: # check wheather there are transactions saved
        transactions = [] # if not create the transactions list
    print("\nAdd transaction")
    print('')
    T_amount = amountInput() # transaction amount input
    while True:
        T_category = input("Enter the category of the transaction: ") # transaction category input
        if len(T_category) > 0:#make sure user inputed a category
            break
        else:
            print("You can't keep transaction category empty.")
    print("Transaction type")
    print(" 1. Income")
    print(" 2. Expense")
    while True:
        T_typeN = intInput("Enter the transaction type (1/2): ", "Input is not valid, check and try again. Input should be 1 or 2.") # transaction type input
        if T_typeN == 1: # income transaction
            T_type = "Income"
            break
        elif T_typeN == 2: # expense transaction
            T_type = "Expense"
            break
        else: # invalid type
            print("Input is not valid, check and try again. Input should be 1 or 2.")
    T_date = dateInput() # transaction date input
    transaction = [T_amount, T_category, T_type, T_date]#create a list from inputted data
    transactions.append(transaction)#append that list to main list
    saveTransactions(transactions)
    print("\nTransaction successfully added.")

def viewTransactions(topic = "\nView Transactions"):
    #View all saved transactions.
    transactions = loadTransactions()# Load transactions at the start
    if transactions == False: # make sure there are transactions saved to continue this action
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print(topic)
        print('')
        print("ID  Transaction")
        for i in range(len(transactions)):
            print(f"{i+1} - {transactions[i]}") # print the list of transactions one by one witha unique ID
        print('')
        print("All saved transactions loaded.")
        return transactions

def updateConf(transactions, ID, ChangeID, value, message):
    #Prompt the confirmation from user to update a specific attribute of a transaction.
    while True:
        yesno = input(f"Are you sure you want to update the transaction {message} (y/n): ").lower()
        if yesno == 'y':
            transactions[ID-1][ChangeID-1] = value # update the trasaction with new values
            saveTransactions(transactions) #save transactions list with updated data
            print(f"Transaction {message} updated successfully.")
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
        if 1 <= (ID) <= len(transactions): #make sure transaction ID inputed by user is valid
            while True:
                print('')
                print(f"{ID} - {transactions[ID-1]}") #sepratly show the transaction user choose to edit
                print('')
                print("1. Amount")
                print("2. Category")
                print("3. Type")
                print("4. Date")
                while True:
                    ChangeID = intInput("Select what data you want change: ")
                    if ChangeID == 1: # if user want to change the amount
                        T_amount = amountInput() # ask the user for the new ammount they want to change
                        updateConf(transactions, ID, ChangeID, T_amount, "amount") #ask the user confirmation to change the data
                        break
                    elif ChangeID == 2: # if user want to change category
                        while True:
                            T_category = input("Enter the new category of the transaction: ") # ask the user for the new category they want to change
                            if len(T_category) > 0:
                                updateConf(transactions, ID, ChangeID, T_category, "category") #ask the user confirmation to change the data
                                break
                            else:
                                print("You can't keep transaction category empty.")
                        break
                    elif ChangeID == 3: # if user want to change the transaction type
                        print("Transaction type")
                        print(" 1. Income")
                        print(" 2. Expense")
                        while True:
                            T_typeN = intInput("Enter the new transaction type (1/2): ", "Input is not valid, check and try again. Input should be 1 or 2.") # ask the user for the type they want to change
                            if T_typeN == 1:
                                T_type = "Income"
                                updateConf(transactions, ID, ChangeID, T_type, "type") #ask the user confirmation to change the type to income
                                break
                            elif T_typeN == 2:
                                T_type = "Expense"
                                updateConf(transactions, ID, ChangeID, T_type, "type") #ask the user confirmation to change the type to expense
                                break
                            else:
                                print("Input is not valid, check and try again. Input should be 1 or 2.")
                        break
                    elif ChangeID == 4: #if the user want to change the date of the trasaction
                        T_date = dateInput()
                        updateConf(transactions, ID, ChangeID, T_date, "date") #ask the user confirmation to change the date
                        break
                    else:
                        print("Please select a valid input.")
                anotherEdit = input("Enter 'A' to change another data type in the selected transaction, Enter any ket to exit : ").lower() #ask the user if they want to make another change in the same transaction
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
        if 1 <= (ID) <= len(transactions): #make sure transaction ID inputted by user is valid
            print('')
            print(f"{ID} - {transactions[ID-1]}")
            print('')
            while True: # ask the users confirmation to delete the trasaction
                yesno = input("Are you sure you want to delete this transaction (y/n): ").lower()
                if yesno == 'y':
                    del transactions[ID-1]
                    saveTransactions(transactions) # save transactions list without the deleted transaction
                    print("Transaction deleted successfully.")
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
    TotalIncomeA = 0 # initiate variabales
    TotalExpensesA = 0
    IncomeCount = 0
    ExpensesCount = 0
    if transactions == False: # make sure there are transactions saved to continue this action
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print("\nTransactions summary")
        print('')
        print(f"Total number of transactions :  {len(transactions)}") 
        print('')
        for i in range(len(transactions)):
            if transactions[i][2] == "Income": # generate the summary for income transactions
                TotalIncomeA += float(transactions[i][0])
                IncomeCount += 1
            else: # generate the summary for expense transactions
                TotalExpensesA += float(transactions[i][0])
                ExpensesCount += 1
        print("Income transactions")
        printSummary(IncomeCount, TotalIncomeA) # print the summary for income transactions
        print("Expenses transactions")
        printSummary(ExpensesCount, TotalExpensesA) # print the summary for expense transactions
        print("")
        print("end of the summary.")

def menuChoice():
    #Handle user menu choice.
    while True:
        choice = intInput("Enter your choice : ")
        if 1 <= choice <= 6: # make sure user entered a valid choice
            break
        else:
            print("Invalid choice, please try again.\n")
        print('')

    if choice == 1:
        addTransaction() # calls add transaction function
    elif choice == 2:
        viewTransactions() # calls view transaction function
    elif choice == 3:
        updateTransaction() # calls update transaction function
    elif choice == 4:
        deleteTransaction() # calls display transaction function
    elif choice == 5:
        displaySummary() # calls display summary function
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