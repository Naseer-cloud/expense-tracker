# 💰 Expense Tracker

A simple expense tracker built using Python and SQLite. Users can add and view expenses through a command-line interface.

## 📌 Features
✅ Add expenses with category, amount, and date  
✅ View all recorded expenses  
✅ Uses SQLite for data storage  
✅ Simple and lightweight  

## 🚀 Installation & Usage  
### **1. Clone the Repository**  
```sh
git clone https://github.com/Naseer-cloud/expense-tracker.git
cd expense-tracker
```

### **2. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3. Run the Application**  
```sh
python app.py
```

## 📂 Database Schema  
```sql
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
);
```

## 🤝 Contributing  
Want to improve this project? Fork it, make your changes, and submit a Pull Request! 🚀  
