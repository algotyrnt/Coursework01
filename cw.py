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
    finally:
        if len(transactions) == 0:
            return None
        else:
            return transactions

def saveTransactions(transactions):
    #Save transactions to a JSON file.
    with open('transactions.json', 'w') as file: # open the file transactions.json in write mode
        json.dump(transactions, file, indent=1)

def read_bulk_transactions_from_file(filename, transactions):
    # Open and read the file, then parse each line to add to the transactions dictionary.
    try:
        with open(filename, 'r+') as file:
            for data in file:
                transactionFromFile = data.split(',')
                T_amount = transactionFromFile[0].strip() # transaction amount
                T_category = transactionFromFile[1].strip().lower() # transaction category
                T_date = transactionFromFile[2].strip() # transaction date
                transaction = {"amount": T_amount, "date": T_date} # create a dictionary with the transaction details
                if T_category in transactions: # add the transaction to the transactions list
                    transactions[T_category].append(transaction)
                else:
                    transactions[T_category] = [transaction]
            file.truncate(0)
    except FileNotFoundError:
        print(f"\n{filename} not found.")
    else:
        saveTransactions(transactions)
        print("\nTransactions successfully added from the file.")

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
    if transactions == None: # check wheather there are transactions saved
        transactions = {} # if not create the transactions list
    print("\nAdd transactions")
    print('')
    print("1. Add a new transaction") # ask the user wheather to add a new transaction or add a bulk of transactions from a file
    print("2. Add a bulk of transactions from transaction.txt file") 
    print('')
    while True:
        choice = intInput("Enter your choice (1/2): ", "Input is not valid, check and try again. Input should be 1 or 2.") 
        if choice == 1: # if user choose to add a new transaction
            T_amount = amountInput() # transaction amount input
            while True:
                T_category = input("Enter the category of the transaction: ").lower() # transaction category input
                if len(T_category) > 0:#make sure user inputed a category
                    break
                else:
                    print("You can't keep transaction category empty.")
            T_date = dateInput() # transaction date input
            transaction = {"amount": T_amount, "date": T_date} # create a dictionary with the transaction details
            if T_category in transactions: # add the transaction to the transactions list
                transactions[T_category].append(transaction)
            else:
                transactions[T_category] = [transaction]
            saveTransactions(transactions) # save the transaction dictionary with the new transaction
            print("\nTransaction successfully added.")
            break
        elif choice == 2: # if user choose to add a bulk of transactions from a file
            while True:
                filename = input("Enter the file name (transactions.txt): ").lower() # ask the user for the file name
                if len(filename) > 0:#make sure user inputed a file name
                    break
                else:
                    print("You can't keep filename empty.")
            read_bulk_transactions_from_file(filename, transactions) # read transactions from the file 
            break
        else: # invalid type
            print("Input is not valid, check and try again. Input should be 1 or 2.")

def viewTransactions(topic = "\nView Transactions"):
    #View all saved transactions.
    transactions = loadTransactions()# Load transactions at the start
    if transactions == None: # make sure there are transactions saved to continue this action
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print(topic)
        print('')
        for x in transactions:
            print(x) # print the category of the transaction
            for i in range(len(transactions[x])):
                print(f"{i+1} - {str(transactions[x][i]).strip("{}")}") # print the list of transactions one by one witha unique ID
        print('')
        print("All saved transactions loaded.")
        return transactions

def updateConf(transactions, category, ID, ChangeT, value, message):
    #Prompt the confirmation from user to update a specific attribute of a transaction.
    while True:
        yesno = input(f"Are you sure you want to update the transaction {message} (y/n): ").lower()
        if yesno == 'y':
            transactions[category][ID - 1][ChangeT] = value # update the trasaction with new values
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
        category = input("Enter the category of the transaction you want to update: ")
        if category in transactions:
            ID = intInput("Enter the ID of the transaction you want to update: ")
            if 1 <= (ID) <= len(transactions[category]): #make sure transaction ID inputed by user is valid
                while True:
                    print('')
                    print(f"{ID} - {transactions[category][ID-1]}") #sepratly show the transaction user choose to edit
                    print('')
                    print("1. Amount")
                    print("2. Date")
                    while True:
                        ChangeID = intInput("Select what data you want change: ") # ask the user what they want to change in the transaction
                        if ChangeID == 1: # if user want to change the amount of the transaction
                            T_amount = amountInput() # ask the user for the new ammount they want to change
                            updateConf(transactions, category, ID, "amount", T_amount, "amount") #ask the user confirmation to change the data
                            break
                        elif ChangeID == 2: #if the user want to change the date of the trasaction
                            T_date = dateInput()
                            updateConf(transactions, category, ID, "date", T_date, "date") #ask the user confirmation to change the date
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
        else:
            print("Please enter a valid transaction category.")

def deleteTransaction():
    #Delete an existing transaction.
    transactions = viewTransactions("\nDelete Transactions") #View transactions at start
    print('')
    while True:
        category = input("Enter the category of the transaction you want to delete: ")
        if category in transactions:
            ID = intInput("Enter the ID of the transaction you want to delete: ")
            if 1 <= (ID) <= len(transactions[category]): #make sure transaction ID inputed by user is valid
                print('')
                print(f"{ID} - {transactions[category][ID-1]}") #sepratly show the transaction user choose to delete
                print('')
                while True: # ask the users confirmation to delete the trasaction
                    yesno = input("Are you sure you want to delete this transaction (y/n): ").lower()
                    if yesno == 'y':
                        del transactions[category][ID - 1] # delete the transaction from the list inside the dictionary
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
        else:
            print("Please enter a valid transaction category.")

def displaySummary():
    #Display summary of transactions.
    transactions = loadTransactions() # Load transactions at the start
    if transactions == None: # make sure there are transactions saved to continue this action
        print("There are no saved transactions, You need to have saved transactions to complete this action.")
    else:
        print("\nTransactions summary")
        print('')
        for x in transactions:
            TotalValue = 0
            print(f"Transaction Category :  {x}")  # print the category of the transaction
            for i in range(len(transactions[x])):
                TotalValue += float(transactions[x][i]["amount"]) # calculate the total value of the transactions
            amount = "{:.2f}".format(TotalValue)
            print(f"Total number of transactions in the category: {len(transactions[x])}") # print the total number of transactions
            print(f"Total Value of Transactions in the category: {amount}") # print the total value of the transactions
            print('')
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