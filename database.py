import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('quotes.db')
cursor = conn.cursor()

# Fetch all quotes from the database
cursor.execute('SELECT * FROM quotes')
rows = cursor.fetchall()

# Print the quotes and authors
for row in rows:
    print(f"ID: {row[0]}, Quote: {row[1]}, Author: {row[2]}")

# Close the connection
conn.close()
