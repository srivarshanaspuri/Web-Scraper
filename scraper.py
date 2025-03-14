import requests
from bs4 import BeautifulSoup
import sqlite3

# Step 1: Fetch the data from the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Parse the HTML to extract quotes and authors
quotes_data = []
quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    quotes_data.append((text, author))

# Step 3: Create an SQLite database and table
conn = sqlite3.connect('quotes.db')  # Connect to (or create) the SQLite database
cursor = conn.cursor()

# Create a table to store the quotes if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote_text TEXT,
    author TEXT
)
''')

# Step 4: Insert the extracted data into the SQLite table
cursor.executemany('''
INSERT INTO quotes (quote_text, author) VALUES (?, ?)
''', quotes_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data has been successfully scraped and stored in SQLite database.")
