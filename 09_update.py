import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

update records
cursor.execute(""" UPDATE customers 
	SET first_name = 'Bob' 
	WHERE rowid = 1
	""")

connection.commit()


# query the database
cursor.execute("SELECT rowid, * FROM customers ORDER BY first_name")

items = cursor.fetchall()

for item in items:
	if len(item[2]) < 5:
		print(f"{item[0]}. {item[1]} {item[2]} \t\t | {item[3]} ")
	else:
		print(f"{item[0]}. {item[1]} {item[2]} \t | {item[3]} ")



connection.close()
