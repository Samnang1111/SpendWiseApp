from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, 
    QGridLayout, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect, QSizePolicy
)
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor, QLinearGradient
from PyQt6.QtCore import Qt
from database import login_user 

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 450)
        self.setWindowIcon(QIcon('images/window_icon_images/login_icon.png'))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Center the window
        self.center_window()

        # Layout setup
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # Create a card layout for the form
        card_layout = QGridLayout()
        card_layout.setContentsMargins(20, 20, 20, 20)

        card_widget = QWidget()
        card_widget.setLayout(card_layout)
        card_widget.setStyleSheet(""" 
            QWidget {
                background-color: white;
                border-radius: 15px;
                padding: 20px;
            }
        """)

        # Add shadow effect to the card
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 50))
        card_widget.setGraphicsEffect(shadow)

        # Welcome Label
        self.welcome_label = QLabel('Welcome Back to <span style="color:#1E90FF;">SpendWise!</span>')
        self.welcome_label.setFont(QFont('Roboto', 16, QFont.Weight.Bold))
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.welcome_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Login Title
        self.login_label = QLabel('Please Login to Your Account')
        self.login_label.setFont(QFont('Roboto', 14, QFont.Weight.Bold))
        card_layout.addWidget(self.login_label, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Username Field
        self.username_label = QLabel("Username:")
        self.username_label.setFont(QFont('Roboto', 12))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("👤Enter your username")
        self.username_input.setStyleSheet(self.get_input_style())
        card_layout.addWidget(self.username_label, 2, 0, Qt.AlignmentFlag.AlignRight)
        card_layout.addWidget(self.username_input, 2, 1)

        # Password Field
        self.password_label = QLabel("Password:")
        self.password_label.setFont(QFont('Roboto', 12))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("🔐Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.get_input_style())
        card_layout.addWidget(self.password_label, 3, 0, Qt.AlignmentFlag.AlignRight)
        card_layout.addWidget(self.password_input, 3, 1)

        # Buttons
        button_layout = QHBoxLayout()

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont('Roboto', 12))
        self.login_button.setStyleSheet(self.get_button_style("#007BFF", "#0056b3"))
        self.login_button.clicked.connect(self.login_user)

        # Register Button
        self.register_button = QPushButton("Create Account")
        self.register_button.setFont(QFont('Roboto', 12))  # Same font size as Login button
        self.register_button.setStyleSheet(self.get_button_style("#28a745", "#218838"))
        self.register_button.clicked.connect(self.register_btn)

        # # Set equal size for both buttons
        self.login_button.setFixedWidth(150)  
        self.register_button.setFixedWidth(170)


        self.login_button.setMinimumSize(120, 40)
        self.register_button.setMinimumSize(120, 40)

        # Add buttons to the layout
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        card_layout.addLayout(button_layout, 4, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Add card widget to the main layout
        main_layout.addWidget(card_widget)
        self.setLayout(main_layout)

        # Set gradient background
        self.set_background_gradient()

    def set_background_gradient(self):
        """Set a gradient background for the window."""
        palette = self.palette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#6a11cb"))
        gradient.setColorAt(1.0, QColor("#2575fc"))
        palette.setBrush(QPalette.ColorRole.Window, gradient)
        self.setPalette(palette)

    def center_window(self):
        """Center the window on the screen."""
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def get_input_style(self):
        """Return a consistent style for input fields."""
        return """
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
            QLineEdit:focus {
                border: 1px solid #1E90FF;
                background-color: #f0f8ff;
            }
        """

    def get_button_style(self, color, hover_color):
        """Return a consistent style for buttons."""
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """

    def login_user(self):
        """Handle the user login logic."""
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
        else:
            user_id = login_user(username, password)  # Get user ID after successful login
            if user_id:  # If user_id is valid (e.g., not None)
                QMessageBox.information(self, "Login Successful", "You have successfully logged in.")
                
                # Launch ExpenseApp with the user ID
                try:
                    from app import ExpenseApp
                    self.expense_app = ExpenseApp(user_id)  # Pass user_id here
                    self.expense_app.show()
                    self.close()  # Close the login window
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Unable to launch the application: {str(e)}")
            else:
                QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

    def register_btn(self):
        """Navigate to the registration page."""
        from register import RegisterWindow 
        self.register_window = RegisterWindow() 
        self.register_window.show()
        self.close()

    def run_login():
        """Run the login application."""
        import sys
        app = QApplication(sys.argv)
        login_window = LoginWindow()
        login_window.show()
        sys.exit(app.exec())
