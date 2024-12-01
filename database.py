from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from hashlib import sha256

def init_db(db_name):
    """Initialize the SQLite database and create the tables if they don't exist."""
    database = QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName(db_name)

    if not database.open():
        return False

    # Create the expenses table with user_id as a foreign key
    query = QSqlQuery()
    query.exec("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    # Create the users table for registration
    query.exec("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    return True

# User Registration and Login Logic
def register_user(username, password):
    """Register a new user with a hashed password."""
    if user_exists(username):
        return False  # Username already exists
    else:
        hashed_password = hash_password(password)
        save_user_to_db(username, hashed_password)
        return True

def user_exists(username):
    """Check if the username already exists in the database."""
    query = QSqlQuery()
    query.prepare('SELECT * FROM users WHERE username = ?')
    query.addBindValue(username)
    query.exec()

    return query.next()  # If any row exists, return True

def login_user(username, password):
    """Verify user credentials for login."""
    query = QSqlQuery()
    query.prepare('SELECT id, password FROM users WHERE username = ?')
    query.addBindValue(username)
    query.exec()

    if query.next():
        stored_password = query.value(1)  # Get the stored hashed password
        if stored_password == hash_password(password):  # Compare hashed passwords
            return query.value(0)  # Return user_id if login is successful
    return None  # Return None if username or password is incorrect

def hash_password(password):
    """Hash the password using SHA-256."""
    return sha256(password.encode('utf-8')).hexdigest()

def save_user_to_db(username, password):
    """Save the user into the users table."""
    query = QSqlQuery()
    query.prepare('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''')
    query.addBindValue(username)
    query.addBindValue(password)

    return query.exec()

# Expense Management Logic
def fetch_expenses(user_id):
    """Fetch expenses for the given user ID."""
    query = QSqlQuery()
    query.prepare("SELECT id, date, category, amount, description FROM expenses WHERE user_id = ?")
    query.addBindValue(user_id)
    query.exec()

    expenses = []
    while query.next():
        expenses.append([
            query.value(0),  # ID
            query.value(1),  # Date
            query.value(2),  # Category
            query.value(3),  # Amount
            query.value(4),  # Description
        ])
    return expenses


def add_expenses(user_id, date, category, amount, description):
    """Add a new expense to the database for the logged-in user."""
    query = QSqlQuery()
    query.prepare("""
        INSERT INTO expenses (user_id, date, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    """)
    query.addBindValue(user_id)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)

    return query.exec()

def delete_expenses(expense_id):
    """Delete an expense from the database by its ID."""
    query = QSqlQuery()
    query.prepare('DELETE FROM expenses WHERE id = ?')
    query.addBindValue(expense_id)

    return query.exec()

def update_expenses(expense_id, date, category, amount, description):
    """Update an existing expense in the database."""
    query = QSqlQuery()
    query.prepare("""
        UPDATE expenses
        SET date = ?, category = ?, amount = ?, description = ?
        WHERE id = ?
    """)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)
    query.addBindValue(expense_id)

    return query.exec()

