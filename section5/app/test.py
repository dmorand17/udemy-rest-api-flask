import sqlite3
from sqlite3.dbapi2 import connect

# Testing out interacting with a sqlite db
connection = sqlite3.connect("data.db")

# Query and Store results
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "jose", "asdf")
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, "doug", "12345"),
    (3, "anne", "xyz"),
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

# Close connection
connection.close()
