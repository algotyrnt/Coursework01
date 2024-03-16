Title: Personal Finance Tracker

Description:
This Python script serves as a simple personal finance tracker, allowing users to add, view, update, delete transactions, and display a summary of their financial activities. The transactions are stored in a JSON file named 'transactions.json'.

Modules:
- json: Provides functions for working with JSON data.
- datetime: Contains classes for manipulating dates and times.

Functions:
1. intInput(inputMessage, errorMessage): Takes user input and converts it into an integer. Handles invalid inputs with an error message.
2. floatInput(inputMessage, errorMessage): Takes user input and converts it into a float. Handles invalid inputs with an error message.
3. dateInput(): Takes user input for a date in 'yyyy-mm-dd' format and validates it.
4. loadTransactions(): Loads transaction data from the 'transactions.json' file.
5. saveTransactions(transactions): Saves transaction data to the 'transactions.json' file.
6. returnToMainMenu(): Prompts the user to return to the main menu or exit the program.
7. addTransaction(): Allows the user to add a new transaction.
8. viewTransactions(topic): Displays all transactions loaded from the file.
9. updateConf(transactions, ID, ChangeID, value, message): Updates a transaction with new data.
10. updateTransaction(): Allows the user to update an existing transaction.
11. deleteTransaction(): Allows the user to delete an existing transaction.
12. printSummary(count, value): Prints a summary of transaction count and total value.
13. displaySummary(): Displays a summary of income and expenses transactions.
14. menuChoice(): Handles user menu choice and calls corresponding functions.
15. mainMenu(): Displays the main menu and controls the flow of the program.

Main Execution:
- The script starts by displaying the main menu.
- The user can choose from various options to perform actions such as adding, viewing, updating, or deleting transactions, and displaying a summary.
- The mainMenu() function handles the user's menu choice and directs the program flow accordingly.

Usage:
- Run the script, and follow the prompts to perform various financial transactions.
- Ensure that the 'transactions.json' file exists in the same directory as the script to store transaction data.
- Follow the specified date format ('yyyy-mm-dd') when entering transaction dates.
