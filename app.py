# app.py
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, 
                             QDateEdit, QLineEdit, QComboBox, 
                             QTableWidget, QVBoxLayout, QHBoxLayout, 
                             QMessageBox, QTableWidgetItem, QHeaderView)
from PyQt6.QtCore import QDate, QSize, Qt
from PyQt6.QtGui import QIcon
from database import (fetch_expenses, add_expenses, delete_expenses, 
                      update_expenses)  
from pie_chart import Window  

class ExpenseApp(QWidget):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id 
        super().__init__()
        self.settings()
        self.initUI()
        self.load_table_data(user_id)

    def settings(self):
        self.setGeometry(0, 0, 900, 550)
        self.setWindowTitle('SpendWise')
        self.setWindowIcon(QIcon('images/window_icon_images/app_icon.png'))

    def initUI(self):
        # Create all UI objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton('Add Expense')
        self.btn_edit = QPushButton('Edit Expense')  # New button to edit
        self.btn_delete = QPushButton('Delete Expense')
        self.btn_show_pie_chart = QPushButton('Show Pie Chart')  # Button to show the pie chart
        self.btn_generate_report = QPushButton('Generate Monthly Report')
        self.btn_logout = QPushButton('Logout')  # Logout button

        self.btn_add.setIcon(QIcon('images/btn_icon_images/btn_add.png'))
        self.btn_edit.setIcon(QIcon('images/btn_icon_images/btn_edit.png'))
        self.btn_delete.setIcon(QIcon('images/btn_icon_images/btn_delete.png'))
        self.btn_show_pie_chart.setIcon(QIcon('images/btn_icon_images/btn_show_pie_chart.png'))
        self.btn_generate_report.setIcon(QIcon('images/btn_icon_images/monthly_report_btn.png'))

        # Optionally set an icon size
        self.btn_add.setIconSize(QSize(20, 20))
        self.btn_edit.setIconSize(QSize(20, 20)) 
        self.btn_delete.setIconSize(QSize(20, 20)) 
        self.btn_show_pie_chart.setIconSize(QSize(20, 20)) 
        self.btn_generate_report.setIconSize(QSize(20, 20)) 
        self.btn_logout.setIconSize(QSize(20, 20))  # Icon size for logout

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['ID', 'Date', 'Category', 'Amount', 'Description'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.total_label = QLabel("Total Expenses: $0")  # Label for showing the total expenses

        self.populate_dropdown()

        # Connect buttons to their respective functions
        self.btn_add.clicked.connect(self.add_expense)
        self.btn_delete.clicked.connect(self.delete_expense)
        self.btn_edit.clicked.connect(self.edit_expense)
        self.btn_show_pie_chart.clicked.connect(self.show_pie_chart)  # Connect pie chart button
        self.btn_generate_report.clicked.connect(self.generate_multi_month_report)  # Connect button
        self.btn_logout.clicked.connect(self.logout_from_app)  # Connect logout button

        from PyQt6.QtCore import Qt

        # Add Expense Button
        self.btn_add.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_add.setToolTip("Add a new expense to the tracker")

        # Delete Expense Button
        self.btn_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_delete.setToolTip("Remove the selected expense from the tracker")

        # Edit Expense Button
        self.btn_edit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_edit.setToolTip("Edit the details of the selected expense")

        # Show Pie Chart Button
        self.btn_show_pie_chart.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_show_pie_chart.setToolTip("View a pie chart of your expenses by category")

        # Generate Report Button
        self.btn_generate_report.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_generate_report.setToolTip("Generate a detailed report of your expenses")
    
        # Logout button
        self.btn_logout.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_logout.setToolTip("Logout from the application")

        # Set up layout
        self.setup_layout()
        self.apply_style()

    def setup_layout(self):
        master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row1
        row1.addWidget(QLabel('Date'))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel('Category'))
        row1.addWidget(self.dropdown)

        # Row2
        row2.addWidget(QLabel('Amount'))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel('Description'))
        row2.addWidget(self.description)

        # Row3
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_edit)
        row3.addWidget(self.btn_delete)
        row3.addWidget(self.btn_show_pie_chart)  # Add Pie Chart button here
        row3.addWidget(self.btn_generate_report)  # Add to the same row as other buttons
        row3.addWidget(self.btn_logout)  # Add logout button here

        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addWidget(self.table)
        master.addWidget(self.total_label)  # Add total label to layout

        self.setLayout(master)

    def apply_style(self):
        self.btn_add.setObjectName("btn_add")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_edit.setObjectName("btn_edit")
        self.btn_show_pie_chart.setObjectName("btn_show_pie_chart")  # Add style for Pie Chart button
        self.btn_generate_report.setObjectName("btn_generate_report")
        self.btn_logout.setObjectName("btn_logout")  # Apply style for logout button

        self.setStyleSheet("""
            /* General Styles */
            QWidget {
                background-color: #e3e9f2;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #333;
            }

            /* Label Styles */
            QLabel {
                font-size: 16px;
                color: #2c3e50;
                font-weight: bold;
                padding: 5px;
            }

            /* Input Field Styles */
            QLineEdit, QComboBox, QDateEdit {
                background-color: #fff;
                font-size: 14px;
                color: #333;
                border: 1px solid #b0bfc6;
                border-radius: 8px;
                padding: 5px;
            }

            /* Hover Effects for Input Fields */
            QLineEdit:hover, QDateEdit:hover, QComboBox:hover {
                background-color: #ecf0f1;
            }

            /* Button Styles */
            QPushButton {
                background-color: #d3e0ea;
                font-size: 14px;
                color: #333;
                border: 1px solid #b0bfc6;
                border-radius: 10px;
                padding: 6px 12px;
            }

            /* Button Hover Effects */
            QPushButton:hover {
                background-color: #c2d6e8;
            }

            /* Table Styles */
            QTableWidget {
                background-color: #fff;
                alternate-background-color: #f2f7fb;
                gridline-color: #c0c9d0;
                selection-background-color: #4caf50;
                selection-color: white;
                font-size: 14px;
                border: 1px solid #cfd9e1;
                padding: 5px;
            }

            /* Table Header Styles */
            QHeaderView::section {
                background-color: #e3e9f2;
                font-weight: bold;
                font-size: 14px;
                color: #2c3e50;
                padding: 5px;
                border: 1px solid #cfd9e1;
            }

            /* Button Custom Styles */
            #btn_add {
                background-color: green;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            #btn_add:hover {
                background-color: #218838;
            }

            #btn_delete {
                background-color: #f70707;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            #btn_delete:hover {
                background-color: #c82333;
            }

            #btn_edit {
                background-color: #ff9800;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            #btn_edit:hover {
                background-color: #e69500;
            }

            #btn_show_pie_chart {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            #btn_show_pie_chart:hover {
                background-color: #2980b9;
            }

            #btn_generate_report {
                background-color: #8e44ad;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }
            #btn_generate_report:hover {
                background-color: #732d91;
            }

            #btn_logout {
                background-color: #f39c12;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }

            #btn_logout:hover {
                background-color: #e67e22;
            }
        """)

    def logout_from_app(self):
        response = QMessageBox.question(
            self, 'Logout', 'Are you sure you want to log out?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if response == QMessageBox.StandardButton.Yes:
            self.close()  # Close the application upon logging out

    def populate_dropdown(self):
        categories = ['Food', 'Housing', 'Transportation', 'Health & Insurance', 'Entertainment', 'Others']
        self.dropdown.addItems(categories)

    def load_table_data(self, user_id):
        expenses = fetch_expenses(user_id)  # Pass the user_id
        self.table.setRowCount(0)
        total_expense = 0

        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
            
            try:
                # Assuming the amount is in column 3, adjust if necessary
                total_expense += float(expense[3])  # Sum up the amounts (make sure it's a valid float)
            except ValueError:
                # Handle cases where the value cannot be converted to float (e.g., a category name)
                pass  # You can log this or handle it differently if necessary

        self.update_total_label(total_expense)  # Update total expense label
        # Update total expense label


    def update_total_label(self, total):
        self.total_label.setText(f"<span style='font-size:16px; font-weight:bold; color:#2E86C1;'>"
                                f"Total Expenses: <span style='color:#D35400;'>${total:.2f}</span>"
                                f"</span>")



    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

    def add_expense(self):
        date = self.date_box.date().toString('yyyy-MM-dd')
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        # Validate all inputs are provided
        if not (date and category and amount and description):
            QMessageBox.warning(self, 'Input Error', 'All fields must be filled!')
            return

        # Validate if the amount is a number
        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Amount must be a valid number!')
            return

        # Proceed to add the expense
        if add_expenses(self.user_id, date, category, amount, description):
            self.load_table_data(self.user_id)  # Make sure user_id is passed
            self.clear_inputs()
            QMessageBox.information(self, 'Success', 'Expense added successfully!')
        else:
            QMessageBox.critical(self, 'Error', 'Failed to add expense!')

    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1: # Check if user does not select any row
            QMessageBox.warning(self, 'Uh oh', 'You need to choose a row to delete.')
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, 'Confirm', 'Are you sure you want to delete?', 
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            if delete_expenses(expense_id):
                self.load_table_data(self.user_id)  # Refresh table data
                QMessageBox.information(self, 'Success', 'Expense deleted successfully!')
            else:
                QMessageBox.critical(self, 'Error', 'Failed to delete expense!')

    def edit_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, 'Selection Error', 'Please select a row to edit.')
            return

        # Fetch the existing data
        expense_id = int(self.table.item(selected_row, 0).text())
        date = self.date_box.date().toString('yyyy-MM-dd')
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        # Validate if the amount is a number
        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Amount must be a valid number!')
            return

        if update_expenses(expense_id, date, category, amount, description):
            self.load_table_data(self.user_id)  # Refresh table data
            QMessageBox.information(self, 'Success', 'Expense updated successfully!')
        else:
            QMessageBox.critical(self, 'Error', 'Failed to update expense!')

    def show_pie_chart(self):
        # Create and show the pie chart window
        self.pie_chart_window = Window(self.user_id)
        self.pie_chart_window.show()

    def logout_from_app(self):
        self.close()
        from login import LoginWindow  # Assuming your login window is in login.py
        self.login_window = LoginWindow()
        self.login_window.show()
        


    def categories_data(self):
        categories = ['Food', 'Housing', 'Transportation', 'Health & Insurance', 'Entertainment', 'Others']
        category_totals = {category: 0 for category in categories}
        
        expenses = fetch_expenses(self.user_id)  # Use self.user_id to fetch expenses for the logged-in user
        total_expense = 0

        # Sum up the total expense and categorize
        for expense in expenses:
            category = expense[2]  # Assuming category is in the third column (index 2)
            amount = float(expense[3])  # Assuming amount is in the fourth column (index 3)
            
            total_expense += amount
            if category in category_totals:
                category_totals[category] += amount

        # Calculate percentage for each category
        category_percentages = {}
        if total_expense > 0:  # Avoid division by zero
            for category, total in category_totals.items():
                category_percentages[category] = (total / total_expense) * 100

        return category_percentages
    

                
    def generate_multi_month_report(self):
        from collections import defaultdict

        # Constants for formatting and emojis
        CATEGORY_EMOJIS = {
            'Food': '🍽️',
            'Housing': '🏠',
            'Transportation': '🚗',
            'Health & Insurance': '💊',
            'Entertainment': '🎉',
            'Others': '🛠️'
        }
        REPORT_HEADER = "<h3>🌟 Multi-Month Expense Summary 🌟</h3>"
        REPORT_FILE_NAME = "Multi_Month_Expense_Report.html"

        # Fetch all expenses
        expenses = fetch_expenses(self.user_id)  # Assuming this fetches all expenses

        # Group expenses by month and year
        expenses_by_month = defaultdict(list)
        for expense in expenses:
            date = QDate.fromString(expense[1], 'yyyy-MM-dd')
            month_year = (date.month(), date.year())
            expenses_by_month[month_year].append(expense)

        # Generate reports for each month
        report_lines = [REPORT_HEADER]
        for (month, year), monthly_expenses in sorted(expenses_by_month.items()):
            month_name = QDate(year, month, 1).toString('MMMM')

            # Calculate total and category-wise breakdown
            total_expenses = sum(float(expense[3]) for expense in monthly_expenses)
            category_totals = defaultdict(float)
            for expense in monthly_expenses:
                category_totals[expense[2]] += float(expense[3])

            # Append report for the current month
            report_lines.append(f"<h3>📅 <b>{month_name} {year}</b></h3>")
            report_lines.append(f"<p>- Total Spending: <span style='color: red;'><b>${total_expenses:.2f}</b></span></p>")
            report_lines.append("<p>- Breakdown:</p><ul>")

            for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
                emoji = CATEGORY_EMOJIS.get(category, '❓')
                percentage = (total / total_expenses) * 100 if total_expenses > 0 else 0
                report_lines.append(
                    f"<li>{emoji} {category}: <b>${total:.2f}</b> "
                    f"(<span style='color: green;'>{percentage:.2f}%</span>)</li>"
                )

            report_lines.append("</ul>")

        # Combine the full report into a single HTML string
        full_report = "".join(report_lines)

        # Display the full report in a message box (supports HTML)
        QMessageBox.information(self, "Multi-Month Report", full_report)

        # Save the report as a text file
        try:
            with open(REPORT_FILE_NAME, "w", encoding="utf-8") as file:
                file.write(full_report.replace('<br>', '\n').replace('<ul>', '').replace('</ul>', '').replace('<li>', '').replace('</li>', ''))
            QMessageBox.information(self, 'Report Saved', f"The report has been saved as '{REPORT_FILE_NAME}'.")
        except Exception as e:
            QMessageBox.warning(self, 'Error', f"Failed to save the report: {e}")
