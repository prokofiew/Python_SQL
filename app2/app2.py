import sqlite3

connection = sqlite3.connect('coffee.db')

cursor = connection.cursor()

cursor.execute("show tables")

for i in cursor:
	print(i)

connection.execute()
connection.close()