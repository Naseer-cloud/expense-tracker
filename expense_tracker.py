-- SQL script: Creating Expenses Table and Inserting Sample Data
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
);

-- Inserting sample data
INSERT INTO expenses (category, amount, date) VALUES ('Food', 15.5, '2025-03-25');
INSERT INTO expenses (category, amount, date) VALUES ('Transport', 7.0, '2025-03-24');

-- Fetch all expenses
SELECT * FROM expenses;
