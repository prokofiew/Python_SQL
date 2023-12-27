import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()

# displaying content with primary KEY - item[0] will be rowid 
for item in items:
	print(f"{item[0]}. {item[1]} {item[2]} {item[3]}")


connection.commit()
connection.close()