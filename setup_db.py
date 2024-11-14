import sqlite3

def create_database():
    conn = sqlite3.connect('contacts.db')  # Creates a new database file
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT NOT NULL,
            message TEXT
        )
    ''')
    conn.commit()  # Save changes
    conn.close()  # Close the connection

if __name__ == '__main__':
    create_database()
