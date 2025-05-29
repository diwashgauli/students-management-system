# Student Management System

This is a simple command-line Student Management System built using Python and SQLite.  
It allows users to add, update, delete, search, and view student records stored in a database.

## Features

- Add new student records
- Update existing student details
- Delete student records
- Search students by name
- View all students
- Simple and user-friendly CLI interface
- Data is stored in a local SQLite database (`students.db`)

## Technologies Used

- Python
- SQLite (via `sqlite3` module)

## Project Structure
STUDENT_MANAGEMENT_SYSTEM/
│
├── database.py         # Handles database setup and basic DB operations (CRUD)
├── student.py          # Contains the Student class with data handling logic
├── file_handler.py     # Handles file operations like exporting to CSV/JSON
├── main.py             # CLI interface for interacting with the user
└── README.md           # Project documentation


## How to Run

1. Make sure Python is installed.
2. Navigate to the project folder.
3. Run the program: "bash
python main.py"

## Example Usage
Record income or expense

Check balance

Export your data for analysis

## What I Learned
- How to design and organize a simple database schema using SQLite

- Creating and managing tables with SQL commands in Python

- Writing Python classes to represent real-world entities (like students)

- Performing basic CRUD (Create, Read, Update, Delete) operations using SQL in Python

- Structuring code into multiple files for better readability and maintainability

- Implementing a simple command-line interface for user interaction

- Committing and managing database transactions with conn.commit()

- Using exception handling (optional next step) to make the app more robust

## Future Improvements
Add charts using Matplotlib

Add monthly summaries

Add user login support




