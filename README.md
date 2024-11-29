# SPENDWISE-Expense-Tracker-Project

```
Project Documentation
1. Project Overview
Project Title

SPENDWISE-Expense Tracker Application

Problem to Be Solved

Managing personal finances can be challenging without proper tools. This project aims to simplify financial management by providing an application to:

Track and manage expenses efficiently.
Address common issues like lack of real-time tracking, poor categorization of expenses, and absence of visual insights into spending habits.
2. Current Progress (PDLC Stages)

Problem Analysis:

Identified the challenges of manual expense tracking.
Requirements include user authentication, a SQLite 3 database for managing expenses, and visual tools for reports.

Design:

Created a database schema with tables for users, expenses, and categories.
Designed a user-friendly graphical user interface (GUI) using PyQt6.

Implementation:

Developed key features such as adding, editing, deleting, and viewing expenses.
Integrated SQLite for database interaction and PyQt6 for the graphical interface.

Testing:

Conducted tests for user registration, login functionality, and database operations.
Verified data integrity in the SQLite database.

Deployment (Planned):

Completing final configurations for deployment, including environment variables and packaging.
3. Project Functions and Features
Core Features

User Management:

Secure user registration with hashed passwords.
Login functionality with session management.

Expense Management:

Add, edit, delete, and view expenses.
Categorize expenses for easier organization and tracking.

Data Visualization:

Generate pie charts by displaying the percentage of each category.
Monthly and yearly reports for detailed expense summaries.

Database Features:

Use SQLite to store user and expense data securely.
Ensure reliable and consistent data operations.
Additional Tools and Integrations
Support for viewing and managing the database using tools like DB Browser for SQLite and VS Code extensions.

4. Expected No. of Pages
Home Page: Displays a quick summary of user data and links to key sections.
Signup Page: User registration form.
Login Page: Secure user login interface.
Dashboard:
Displays total expenses, recent transactions, and summary charts.
Expense Management Page:
Interface for adding, editing, deleting.
Reports Page: Visualization of monthly or yearly expenses.
5. Database Overview
Database Applied
SQLite Database:
File name: expense.db
Database Tables

Users:

Fields: id, username, password
Stores user credentials.

Expenses:

Fields: id, user_id, category, amount, date, description
Tracks expense records linked to specific users.

Data Records
Initial records include a default user and sample expenses for testing purposes.
6. Required Software and Libraries
Software
Python 3.10+: Core runtime for the application.
Download: python.org.
SQLite Tools:

SQLite Viewer & SQLite3 Editor Extensions (Recommend):
Available in the VS Code Extensions marketplace.

DB Browser for SQLite (Optional): For managing the SQLite database.
Download: sqlitebrowser.org.

Python Libraries
PyQt6: For the graphical interface.
PyQt6-Charts: For creating pie charts and visualizations.
PyQt6-QtSql: For database connectivity.
sqlite3: Built-in library for SQLite interaction.
hashlib: For secure password hashing.
os: Built-in library for file operations.
7. Installation Instructions
Step 1: Install Python
Download: Visit python.org/downloads and download Python 3.10+.
Install: Run the installer and check "Add Python to PATH".
Verify Installation: Run the following command in a terminal:
python --version
Step 2: Install Required Python Libraries
Open a terminal or command prompt.
Install dependencies:
pip install PyQt6
pip install PyQt6-Charts
pip install PyQt6-QtSql
Verify installation with this script:
python
from PyQt6.QtWidgets import QApplication from PyQt6.QtCharts import QChart from PyQt6.QtSql import QSqlDatabase import sqlite3 print("All libraries installed correctly!")
Step 3: Install SQLite Tools
VS Code Extensions: Install SQLite Viewer and SQLite3 Editor.
DB Browser for SQLite: Download and install from sqlitebrowser.org.
8. Running the Application
Option 1: Running in Visual Studio Code (VS Code)
Open VS Code and load the project folder.
Install the Python extension (if not already installed).
Run the application by opening main.py and clicking the Run button.
Option 2: Running in PyCharm
Open PyCharm and load the project.
Configure the Python Interpreter.
Right-click on main.py and select Run 'main'.
9. Verifying the Application
Initial Tests
Launch the app to ensure it runs without errors.
Test features:
User registration and login.
Adding, editing, and deleting expenses.
Generating pie charts and reports.
Database Inspection
Use DB Browser for SQLite to inspect the expense.db file and verify that data is being saved correctly.
10. Common Issues and Fixes

Missing Module Error:
Install the missing module:

pip install <module_name>

File Not Found Errors:
Verify that all files (e.g., database, icons, stylesheets) are in the correct directories.
```
