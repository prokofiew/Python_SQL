import sqlite3

# creating database in memory
# connection_1 = sqlite3.connect(':memory:')

# by making a connection it will create database
connection = sqlite3.connect('customer.db')

# to create table need to use cursor 
cursor = connection.cursor()

# create a table
# DATA TYPES: NULL, INTEGER, REAL(FLOAT), TEXR, BLOB(PICTURE)
cursor.execute(""" CREATE TABLE customers (
		first_name TEXT(20),
		last_name TEXT(20),
		email TEXT(50)
	)
""")
# commit out command
connection.commit()

# closing connection
connection.close()

# check


