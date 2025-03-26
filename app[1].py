# Interactive Expense Tracker using SQLite
import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        amount REAL,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
    conn.commit()
    conn.close()
    print("Expense added successfully!\n")

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    
    print("\nExpense Records:")
    for exp in expenses:
        print(exp)

def main():
    init_db()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
