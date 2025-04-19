# a. Create a table:
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

conn.commit()
conn.close()

# b. Insert operation:
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
conn.commit()
conn.close()

# c. Select operation:
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# d. Update operation:
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
conn.commit()
conn.close()

# e. Delete table:
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
conn.commit()
conn.close()