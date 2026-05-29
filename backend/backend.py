import sqlite3

conn = sqlite3.connect('registration.db')
# conn.row_factory = sqlite3.Row

cursor = conn.sursor()

cursor.execute('''create table registratio(
               id integer primary key autoincrement,
               username Nvarchar(50),
               email Nvarchar(100),
               password Nvarchar(50),
               )''')

git add backend/backend.py