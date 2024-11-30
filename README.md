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
├── main.py           # Application entry point
├── gui/              # PyQt6 GUI components
├── database/         # SQLite database files
├── assets/           # Images, icons, and stylesheets
└── README.md         # Documentation
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
1. Navigate to the project directory.
2. Run the main application:
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
