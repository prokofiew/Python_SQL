import sqlite3

# creating database in memory
# connection_1 = sqlite3.connect(':memory:')

# by making a connection it will create database
connection = sqlite3.connect('customer.db')

# to create table need to use cursor 
cursor = connection.cursor()

cursor.execute("INSERT INTO customers VALUES('Mary', 'Brown', 'tim.smith@gmail.com')")


# commit out command
connection.commit()

# closing connection
connection.close()




