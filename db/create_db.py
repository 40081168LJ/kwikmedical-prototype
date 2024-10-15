import sqlite3
import os

# Get the absolute path to the current directory
db_path = os.path.join(os.path.dirname(__file__), 'patients.db')

# Connect to (or create) the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the patients table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        nhs_number TEXT,
        medical_history TEXT
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO patients (name, nhs_number, medical_history)
    VALUES (?, ?, ?)
''', [
    ('John Doe', 'NHS12345', 'Hypertension, Diabetes'),
    ('Jane Smith', 'NHS54321', 'Asthma'),
    ('Alan Turing', 'NHS98765', 'No known allergies')
])

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created, sample data inserted.")
