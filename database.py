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


def delete_expense(name):

    for expense in expenses:

        if expense["title"].lower() == name.lower():

            expenses.remove(expense)
            print("Expense deleted successfully!")

            return

    print("Expense not found!")


def update_price(name, new_price):

    expense = search_expense(name)

    if expense:
        expense["amount"] = new_price
        print("Price updated successfully!")

    else:

        print("Expense not found!")
        