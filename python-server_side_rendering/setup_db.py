import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Using 'OR IGNORE' to prevent primary key errors if you run this multiple times
    cursor.execute("INSERT OR IGNORE INTO Products VALUES (1, 'Laptop', 'Electronics', 799.99)")
    cursor.execute("INSERT OR IGNORE INTO Products VALUES (2, 'Coffee Mug', 'Home Goods', 15.99)")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()