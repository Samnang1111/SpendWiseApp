# **SPENDWISE - Expense Tracker Application** 💼📊

---

## 🔍 **Overview**

SPENDWISE is a personal finance management tool designed to:
- ✅ Track and categorize expenses.
- 📊 Provide visual insights into spending habits.
- 🕒 Save time by automating expense tracking and reporting.

---

## 🚀 **Current Progress (PDLC Stages)**

- **✔️ Problem Analysis:**
  - Identified issues with manual expense tracking.
- **✔️ Design:**
  - Created database schema and GUI wireframes.
- **✔️ Implementation:**
  - Built core features using Python, SQLite, and PyQt6.
- **🔄 Testing:**
  - Ensuring functionality and reliability.
- **📦 Deployment:**
  - Planned for final project release.

---

## 📋 **Features**

### 🛠️ **Core Features:**
- **👤 User Management:**
  - Secure registration and login.
- **💸 Expense Management:**
  - Add, edit, delete, and categorize expenses.
- **📊 Visualization:**
  - Generate pie charts and spending reports.
- **📁 Database:**
  - SQLite integration for secure storage.

### 🔧 **Additional Tools:**
- SQLite database tools like DB Browser for SQLite or VS Code extensions.

---

## 🗂️ **Project Structure**

```plaintext
SPENDWISE/
├── __pycache__/         # Python bytecode cache
├── images/               # Project images
├── app.py                # Main application logic
├── database.py           # Database handling script
├── expense.db            # SQLite database file
├── login.py              # User login script
├── main.py               # Application entry point
├── Multi_Month_Expense_Report.html # Report template
├── pie_chart.py          # Pie chart generation script
└── register.py           # User registration script
```

---

## 🗄️ **Database Design**

| Table Name | Columns                                 |
|------------|-----------------------------------------|
| `Users`    | `id`, `username`, `password`           |
| `Expenses` | `id`, `user_id`, `category`, `amount`, `date`, `description` |

---

## 💻 **Software and Libraries**

### 🖥️ **Required Software:**
1. Python 3.10+ ([Download](https://www.python.org/downloads))
2. SQLite tools (e.g., [DB Browser](https://sqlitebrowser.org))

### 📦 **Python Libraries:**
```bash
pip install PyQt6 PyQt6-Charts PyQt6-QtSql sqlite3 hashlib
```

### 🔌 **Recommended VS Code Extensions**
1. SQLite Viewer
2. SQLite3 Editor

---

## 📂 **Setup Instructions**

### 🛠️ **Step 1: Install Python**
- Download and install Python 3.10+.
- Verify installation:
  ```bash
  python --version
  ```

### 🔧 **Step 2: Install Libraries**
- Install dependencies:
  ```bash
  pip install PyQt6 PyQt6-Charts PyQt6-QtSql sqlite3 hashlib
  ```

### 📂 **Step 3: Run the Application**
1. Install the recommended SQLite extensions for VS Code (SQLite Viewer, SQLite3 Editor).
2. Navigate to the project directory.
3. Run the main application:
   ```bash
   python main.py
   ```

---

## 🔍 **Testing the Application**

1. **Run Tests:**
   - Verify user registration/login.
   - Test adding, editing, and deleting expenses.
2. **Check Database:**
   - Open `expense.db` in DB Browser to inspect stored data.

---

## 💡 **Common Issues and Fixes**

| Issue                       | Solution                                    |
|-----------------------------|---------------------------------------------|
| Missing module error        | Install the missing library via pip.       |
| File not found error        | Ensure all files are in the correct paths. |

---

## 🎉 **Contributors**

- **Samnang Yorn** 👨‍💻
