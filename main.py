from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Expense Management API"
    }

@app.get("/expenses")
def get_expenses():

    return database.get_all_expenses()


@app.get("/expenses/{title}")
def search_expense(title: str):

    expense = database.search_expense(title)

    if expense:

        return expense

    return {
        "message": "Expense not found!"
    }


@app.post("/expenses")
def add_expense(
    title: str,
    category: str,
    amount: float,
    date: str
):

    database.insert_expense(
        title,
        category,
        amount,
        date
    )

    return {
        "message": "Expense added successfully!"
    }

@app.delete("/expenses/{title}")
def delete_expense(title: str):

    result = database.delete_expense(title)

    if result:
        return {
            "message": "Expense deleted successfully!"
        }

    return {
        "message": "Expense not found!"
    }

@app.put("/expenses/{title}/amount")
def update_expense_amount(
    title: str,
    new_amount: float
):

    result = database.update_expense_amount(
        title,
        new_amount
    )

    if result:

        return {
            "message": "Amount updated successfully!"
        }

    return {
        "message": "Expense not found!"
    }
