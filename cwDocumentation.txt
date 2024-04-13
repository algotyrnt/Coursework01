This Python program serves as a simple personal finance tracker, allowing users to add, view, update, delete transactions, and display a summary of their financial activities. 
The transactions are stored in a JSON file named 'transactions.json'.
If the programm isn't used befor there will be no saved transactions in the saved file.
User can add transactions from the option given in the add transactions menu.
To add bulk transactions, users have to save the amount, category, and date, respectively, to the order.
	Example - 200.00, salary, 2024-04-06
		- 500.00, health, 2024-04-10
Program requires to have saved transaction to  view, update, delete transactions, and display a summary of transactions.

Libraries used:
1. json: Provides functions for working with JSON data.
2. datetime: Contains classes for manipulating dates and times.

1. Input Functions:
    a. intInput(inputMessage, errorMessage)
        This function prompts the user for an integer input and handles any ValueError exceptions by displaying the specified error message. 
        It repeats the process until a valid integer input is received.
    b. floatInput(inputMessage, errorMessage)
        Similar to intInput, this function prompts the user for a float input and handles any ValueError exceptions. 
        It repeats the process until a valid float input is received.
    c. dateInput()
        This function prompts the user for a date input in the format 'yyyy-mm-dd' and validates the input using datetime.strptime. 
        It ensures that the input is a valid date and repeats the process until a valid date input is received.
    d. amountInput()
        This function prompts the user for a transaction amount and validates the input. 
        It ensures that the amount is a positive number with no more than two decimal places. 
        It repeats the process until a valid amount input is received.

2. File Handling Functions:
    a. loadTransactions()
        This function attempts to load transactions from a JSON file named 'transactions.json'. 
        If the file is not found or cannot be decoded, it returns None. 
        Otherwise, it returns the loaded transactions as a dictionary.
    b. saveTransactions(transactions)
        This function saves the provided transactions list to a JSON file named 'transactions.json'.
    c. read_bulk_transactions_from_file(filename, transactions):
        This function reads transactions from a file named `filename` 
        It iterates through each line of the file, parsing the transaction details and adding them to the dictionary.
        Then empty the file by deleting transactions after they get added to the program.
    

3. Transaction feature implementations Functions:
    a. addTransaction()
        This function allows the user to add a new transaction or add bulk of transactions from file. 
        It prompts the user for transaction details (amount, category, date) and adds the transaction to the dictionary of transactions.
        Or it calls read_bulk_transactions_from_file() function if user wante to add bulk of transactions.
    b. viewTransactions(topic)
        This function displays the list of transactions loaded from the file. 
        If there are no transactions, it prints an error message. 
        It returns the dictionary of transactions for further processing.
    c. updateConf(transactions, ID, ChangeID, value, message)
        This function updates a specific transaction attribute (amount, date) based on user input.
    d. updateTransaction()
        This function allows the user to update an existing transaction. 
        It displays transactions, prompts the user for the Category and ID of the transaction to update, and then prompts for the attribute to update.
    e. deleteTransaction()
        This function allows the user to delete an existing transaction. 
        It displays transactions, prompts the user for the Category and ID of the transaction to delete, and then confirms the deletion.
    f. displaySummary()
        This function displays a summary of transactions according to their category, including their counts and total values.

4. Menu Functions:
    a. menuChoice()
        This function handles the main menu choices entered by the user and calls the corresponding functions based on the choice.
    b. mainMenu()
        This function displays the main menu options and calls menuChoice to handle user input.

5. Execution:
    The script executes the mainMenu function when run directly, starting the program execution.