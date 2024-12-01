from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, 
    QGridLayout, QVBoxLayout, QHBoxLayout, QProgressBar, QGraphicsDropShadowEffect, QSizePolicy
)
from PyQt6.QtGui import QFont, QIcon, QLinearGradient, QColor, QPalette
from PyQt6.QtCore import Qt
from database import register_user  # Import the register_user function to handle registration logic


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Register")
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
        self.welcome_label = QLabel('Welcome to <span style="color:#1E90FF;">SpendWise!</span>')
        self.welcome_label.setFont(QFont('Roboto', 16, QFont.Weight.Bold))
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.welcome_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Register Title
        self.register_label = QLabel('Create Your Account')
        self.register_label.setFont(QFont('Roboto', 14, QFont.Weight.Bold))
        card_layout.addWidget(self.register_label, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

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
        self.password_input.textChanged.connect(self.update_password_strength)
        card_layout.addWidget(self.password_label, 3, 0, Qt.AlignmentFlag.AlignRight)
        card_layout.addWidget(self.password_input, 3, 1)

        # Password Strength Feedback
        self.password_strength_bar = QProgressBar()
        self.password_strength_bar.setMaximum(100)
        self.password_strength_bar.setValue(0)
        self.password_strength_bar.setTextVisible(True)
        self.password_strength_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f5f5f5;
            }
            QProgressBar::chunk {
                border-radius: 5px;
                background-color: #ff6b6b;  /* Weak */
            }
        """)
        card_layout.addWidget(self.password_strength_bar, 4, 1)

        # Confirm Password Field
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_label.setFont(QFont('Roboto', 12))
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("🔐Confirm your password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setStyleSheet(self.get_input_style())
        card_layout.addWidget(self.confirm_password_label, 5, 0, Qt.AlignmentFlag.AlignRight)
        card_layout.addWidget(self.confirm_password_input, 5, 1)

        # Buttons
        button_layout = QHBoxLayout()

        self.register_button = QPushButton("Register")
        self.register_button.setFont(QFont('Roboto', 12))
        self.register_button.setStyleSheet(self.get_button_style("#4CAF50", "#45A049"))
        self.register_button.clicked.connect(self.register_user)

        self.back_button = QPushButton("Back To Login")
        self.back_button.setFont(QFont('Roboto', 12))
        self.back_button.setStyleSheet(self.get_button_style("#f44336", "#d32f2f"))
        self.back_button.clicked.connect(self.back_btn)

        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.back_button)
        card_layout.addLayout(button_layout, 6, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)


        self.register_button.setMinimumSize(120, 40)
        self.back_button.setMinimumSize(120, 40)

        # Add card to main layout
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

    def update_password_strength(self):
        """Update the password strength bar based on password quality."""
        password = self.password_input.text()
        if len(password) < 6:
            strength = 20
            color = "#ff6b6b"  # Weak
        elif len(password) < 10:
            strength = 60
            color = "#ffa726"  # Medium
        else:
            strength = 100
            color = "#4caf50"  # Strong

        self.password_strength_bar.setValue(strength)
        self.password_strength_bar.setStyleSheet(f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """)

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

    def register_user(self):
        """Handle the user registration logic."""
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
        elif password != confirm_password:
            QMessageBox.warning(self, "Password Error", "Passwords do not match.")
        else:
            if register_user(username, password):  # Assuming this function returns True if registration is successful
                QMessageBox.information(self, "Registration Successful", "You have been successfully registered.")
                self.close()

                # Open the login window
                from login import LoginWindow  # Avoid circular imports
                self.login_window = LoginWindow()  # Create a persistent reference
                self.login_window.show()
            else:
                QMessageBox.critical(self, "Registration Failed", "Username already exists.")


    def back_btn(self):
        """Navigate back to the login page."""
        from login import LoginWindow  # Ensure this does not cause circular imports
        self.close()
        self.login_window = LoginWindow()  # Make it an instance attribute
        self.login_window.show()

