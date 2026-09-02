expenses = []

def insert_expense(title,category,amount,date):

    expense = { "title": title, "category": category, "amount": amount, "date": date }

    expenses.append(expense)
    print("Expense added successfully!")


def get_all_expenses():
    return expenses


def search_expense(name):

    for expense in expenses:

        if expense["title"].lower() == name.lower():
            return expense

    return None


def delete_expense(title):

    for expense in expenses:

        if expense["title"].lower() == title.lower():

            expenses.remove(expense)

            return True

    return False


def update_expense_amount(title, new_amount):

    expense = search_expense(title)

    if expense:
        expense["amount"] = new_amount
        print("Amount updated successfully!")

    else:

        print("Expense not found!")
        
