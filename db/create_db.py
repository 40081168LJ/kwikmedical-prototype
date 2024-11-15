# - IMPORTS START ---------------------------------------------------------------------------------------------------- #
import sqlite3
import os
# - IMPORTS END ------------------------------------------------------------------------------------------------------ #

# - PATHING START ---------------------------------------------------------------------------------------------------- #
# Get the absolute path to the current directory
db_path = os.path.join(os.path.dirname(__file__), 'patients.db')
# - PATHING END ------------------------------------------------------------------------------------------------------ #

# - DB CONN START ---------------------------------------------------------------------------------------------------- #
# Connect to/or create the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print("Database Connection created.")
# - DB CONN END ------------------------------------------------------------------------------------------------------ #

# - CREATE TABLE START ----------------------------------------------------------------------------------------------- #
# Create the "patients" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        nhs_number TEXT,
        medical_history TEXT
    )''')
print("Table created.")
# - CREATE TABLE END ------------------------------------------------------------------------------------------------- #

# - INSERT TABLE DATA START ------------------------------------------------------------------------------------------ #
# Insert sample data
cursor.executemany('''
    INSERT INTO patients (name, nhs_number, medical_history)
    VALUES (?, ?, ?)
''', [
    ('John Doe', 'NHS12345', 'Hypertension, Diabetes'),
    ('Jane Smith', 'NHS54321', 'Asthma'),
    ('Barry Allen', 'NHS98765', 'No known allergies')
])
print("Sample data inserted.")
# - INSERT TABLE DATA END -------------------------------------------------------------------------------------------- #

# - COMMIT START ----------------------------------------------------------------------------------------------------- #
# Commit the changes, then close the connection
conn.commit()
conn.close()

print("Database and table created, sample data inserted.")
# - COMMIT END ------------------------------------------------------------------------------------------------------- #