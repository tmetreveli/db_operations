import sqlite3
from faker import Faker
import random

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE book (
          name text,
          page_number integer,
          cover_type text,
          category text
         )""")

categories = ['Fiction', 'Non-fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Biography', 'History', 'Self-help']
cover_types = ['Hardcover', 'Paperback']

for _ in range(10):
    fake = Faker()
    name = fake.catch_phrase()
    page_number = random.randint(100, 1000)
    category = random.choice(categories)
    cover_type = random.choice(cover_types)
    c.execute("INSERT INTO book VALUES(?, ?, ?, ?)", (name, page_number, cover_type, category))

c.execute("SELECT * FROM book")
print(c.fetchall())

c.execute("SELECT avg(page_number) FROM book")
print(c.fetchone())

c.execute("SELECT max(page_number),name FROM book")
print(c.fetchone())

conn.commit()
conn.close()
