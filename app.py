import database

USER_CHOICE = """
Enter:

- 'a' to add a new expense
- 'l' to list all expenses
- 's' to search for an expense
- 'd' to delete an expense
- 'p' to update expense amount
- 'q' to quit

Your choice: """

# Add Expense
def prompt_add_expense():
    title = input("Enter expense title: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date: ")
    
    database.insert_expense(title,category,amount,date)

# List Expenses
def list_expenses():
    expenses = database.get_all_expenses()

    for expense in expenses:
        print(
            f"{expense['title']} - {expense['category']} "
            f"| Amount: ${expense['amount']} "
            f"| Date: {expense['date']}"
        )


# Search Expense
def prompt_search_expense():
    title = input("Enter expense title: ")
    expense = database.search_expense(title)

    if expense:
        print("\nExpense Found!")
        print(f"Title   : {expense['title']}")
        print(f"Category : {expense['category']}")
        print(f"Amount   : ${expense['amount']}")
        print(f"Date  : {expense['date']}")
    else:
        print("Expense not found!")


# Delete Expense
def prompt_delete_expense():
    title = input("Enter the expense title to delete: ")
    database.delete_expense(title)


# Update Amount
def prompt_update_amount():
    title = input("Enter expense title: ")
    new_amount = float(input("Enter new amount: "))

    database.update_amount(title, new_amount)

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            prompt_add_expense()
        elif user_input == "l":
            list_expenses()
        elif user_input == "s":
            prompt_search_expense()
        elif user_input == "d":
            prompt_delete_expense()
        elif user_input == "p":
            prompt_update_amount()
        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)

menu()