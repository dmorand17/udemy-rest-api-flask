import sqlite3

DEFAULT_DB = "data.db"

# Testing out interacting with a sqlite db
connection = sqlite3.connect(DEFAULT_DB)

# Query and Store results
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text, email text)"
cursor.execute(create_table)

user = (1, "jose", "asdf")
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, "doug", "12345", "doug@example.com"),
    (3, "anne", "xyz", "anne@example.com"),
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"  # INTEGER PRIMARY KEY allows Auto incrementing id
cursor.execute(create_table)

item = ("test", 10.99)
insert_query = "INSERT INTO items VALUES (NULL, ?, ?)"
cursor.execute(insert_query, (item))

items = [
    ("chair", 59.99),
    ("desk", 199.99),
]

cursor.executemany(insert_query, items)

select_query = "SELECT * FROM items"
for row in cursor.execute(select_query):
    print(row)


connection.commit()

# Close connection
connection.close()
