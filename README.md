# 💰 Expense Management System

A simple **Expense Management System** built using **Python** and **FastAPI**. This project allows users to manage their daily expenses by adding, viewing, searching, updating, and deleting expense records.

The project demonstrates practical Python programming concepts and basic REST API development using FastAPI.

## 🚀 Features

* ➕ Add a new expense
* 📋 View all expenses
* 🔍 Search for an expense by title
* ✏️ Update an expense amount
* 🗑️ Delete an expense
* 🌐 Access expense operations through REST API endpoints
* 📖 Test API endpoints using FastAPI Swagger UI


## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **REST API**
* **Swagger UI**
* **Git & GitHub**



## 📁 Project Structure

```text
expense-management-system/
│
├── app.py
├── database.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

### File Description

* **app.py** – Contains the command-line menu and user interaction.
* **database.py** – Contains functions for managing expense data.
* **main.py** – Contains FastAPI endpoints.
* **requirements.txt** – Contains required Python packages.


## 💾 Expense Data Structure

Each expense contains the following information:

* **Title**
* **Category**
* **Amount**
* **Date**

Example:

```json
{
    "title": "Groceries",
    "category": "Food",
    "amount": 500.0,
    "date": "2026-09-01"
}

# 🌐 FastAPI Endpoints

## 🏠 Home

### GET `/`

Returns a welcome message for the Expense Management API.

**Response:**

```json
{
    "message": "Expense Management API"
}


## 📋 Get All Expenses

### GET `/expenses`

Returns all available expenses.

**Example Response:**

```json
[
    {
        "title": "Groceries",
        "category": "Food",
        "amount": 500.0,
        "date": "2026-09-01"
    },
    {
        "title": "Bus Ticket",
        "category": "Travel",
        "amount": 50.0,
        "date": "2026-09-01"
    }
]


## 🔍 Search an Expense

### GET `/expenses/{title}`

Search for an expense using its title.

**Example:**

```text
GET /expenses/Groceries
```

**Response:**

```json
{
    "title": "Groceries",
    "category": "Food",
    "amount": 500.0,
    "date": "2026-09-01"
}
```

---

## ➕ Add a New Expense

### POST `/expenses`

Adds a new expense to the system.

Parameters:

* `title`
* `category`
* `amount`
* `date`

**Example Response:**

```json
{
    "message": "Expense added successfully!"
}


## ✏️ Update Expense Amount

### PUT `/expenses/{title}/amount`

Updates the amount of an existing expense.

**Example:**

```text
PUT /expenses/Groceries/amount
```

**Example Response:**

```json
{
    "message": "Amount updated successfully!"
}


## 🗑️ Delete an Expense

### DELETE `/expenses/{title}`

Deletes an expense using its title.

**Example:**

```text
DELETE /expenses/Groceries
```

**Example Response:**

```json
{
    "message": "Expense deleted successfully!"
}


# 💻 Command-Line Application

The project also includes a command-line interface for managing expenses.

Available options:

```text
a - Add a new expense
l - List all expenses
s - Search for an expense
d - Delete an expense
p - Update expense amount
q - Quit


# ⚙️ Installation and Setup

## 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2️⃣ Navigate to the Project Folder

```bash
cd expense-management-system
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```



# ▶️ Run the FastAPI Application

Run the following command:

```bash
uvicorn main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```


# 📖 API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Open your browser and visit:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can test:

* GET requests
* POST requests
* PUT requests
* DELETE requests

without using any additional software.



# 🧠 Concepts Practiced

Through this project, I practiced:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* CRUD operations
* REST API development
* FastAPI routing
* Path parameters
* Query parameters
* HTTP methods
* JSON responses
* API testing using Swagger UI

# 🔄 CRUD Operations

| Operation | HTTP Method | Description             |
| --------- | ----------- | ----------------------- |
| Create    | POST        | Add a new expense       |
| Read      | GET         | View or search expenses |
| Update    | PUT         | Update expense amount   |
| Delete    | DELETE      | Remove an expense       |


# 🎯 Learning Outcomes

This project helped me understand how a Python application can manage data and how the same functionality can be exposed through REST API endpoints.

I gained hands-on experience with:

* Building backend applications using FastAPI
* Creating and testing API endpoints
* Working with HTTP methods
* Managing data using Python dictionaries and lists
* Connecting application logic with API routes

---

# 🔮 Future Improvements

Planned improvements for the project include:

* Add Pydantic models for data validation
* Add proper HTTP status codes
* Improve error handling
* Store expenses in a database
* Add SQLite or MySQL integration
* Add user authentication
* Add expense categories
* Add monthly expense reports
* Add expense analytics
* Create a frontend interface


# 🎥 Project Demo

You can add a short demo video showing:

1. Starting the FastAPI server
2. Opening Swagger UI
3. Adding an expense
4. Viewing all expenses
5. Searching for an expense
6. Updating an expense amount
7. Deleting an expense

**Demo Video:** [Add your video link here]

## 👩‍💻 Author

**Kunkuma Rekha**

Aspiring Python & Backend Developer


⭐ If you found this project interesting, feel free to star the repository!
