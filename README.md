# Database Final Project

## Project Structure
DatabaseFinalProject/
│── Library Management System/
│ └── librarymanagementsystemdatabase(question1).sql
│── Task Manager/
│ ├── app/
│ │ ├── init.py
│ │ ├── database.py
│ │ ├── models.py
│ │ └── main.py
│ ├── README.md
│ ├── requirements.txt
│ └── setup_database.sql


## 1. Library Management System

### Project Title
**Library Management Database System**

### Description
A complete relational database system for managing library operations including:
- Member registrations and management
- Book inventory tracking
- Loan transactions
- Fine calculations

### How to Setup
1. Ensure MySQL Server is installed and running
2. Execute the SQL script:
   ```bash
   mysql -u [username] -p < librarymanagementsystemdatabase(question1).sql

The script will:

Create the database

Set up all tables with proper constraints

Insert sample data

## ERD DIAGRAM
![Library management ERD](https://github.com/user-attachments/assets/0845b483-06a9-4dc2-9a2c-be25552b8c11)


## 2. Task Manager API
## Project Title
**Task Manager CRUD API**

## Description
A RESTful API built with FastAPI and MySQL that provides:

User authentication and management

Task creation and assignment

Task status tracking

Priority-based task organization

## How to Run
Prerequisites
Python 3.8+

MySQL Server

pip package manager

## Setup Instructions
Navigate to the Task Manager directory:
# Navigate to project directory
cd taskmanager

# Install dependencies
pip install -r requirements.txt

# Set up the database (replace [username] with your MySQL username)
mysql -u [username] -p < setup_database.sql

# Run the application
uvicorn app.main:app --reload
# Interactive Swagger UI
http://127.0.0.1:8000/docs

# Alternative ReDoc
http://127.0.0.1:8000/redoc

## Configuration
Edit database connection in app/database.py:
# Example configuration
connection = mysql.connector.connect(
    host='localhost',
    database='task_manager',
    user='your_username',  # Change this
    password='your_password'  # Change this
)

## ERD Diagram

![Task manager ERD](https://github.com/user-attachments/assets/947bee6e-6bff-45d4-921a-0e0fa7b9d147)

## Common Commands
# Start MySQL service (Linux)
sudo service mysql start

# Start MySQL service (Windows)
net start mysql

# Create a Python virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate





