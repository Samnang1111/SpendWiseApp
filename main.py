import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db
from login import LoginWindow
from app import ExpenseApp 

def main():
    app = QApplication(sys.argv)

    # Initialize database
    try:
        if not init_db('expense.db'):
            QMessageBox.critical(None, 'Error', 'Could not load your database...')
            sys.exit(1)  # Exit if database initialization fails
    except Exception as e:
        QMessageBox.critical(None, 'Error', f'Database initialization failed: {e}')
        sys.exit(1)  # Exit if an exception occurs during database initialization

    # Start login process
    if not LoginWindow.run_login():  
        sys.exit(0)  # Exit if login fails

    # Launch the main application
    main_window = ExpenseApp()  # Create the main application window
    main_window.show()  # Show the main window

    # Execute the app
    sys.exit(app.exec())  # Enter the application's event loop

if __name__ == "__main__":
    main()
