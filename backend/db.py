import sqlite3
from werkzeug.security import generate_password_hash

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)''')

# Add a test user (admin/admin123)
hashed_password = generate_password_hash("admin123")
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", hashed_password))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete! ✅")
