import sqlite3

# Query the database and return all records
def show_all():
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("SELECT rowid, * FROM customers")
	
	items = cursor.fetchall()
	for item in items:
		if len(item[2]) < 5:
			print(f"{item[0]}. {item[1]} {item[2]} \t\t\t\t | {item[3]}")
		elif len(item[2]) > 8:
			print(f"{item[0]}. {item[1]} {item[2]} \t | {item[3]}")
		else:
			print(f"{item[0]}. {item[1]} {item[2]} \t\t\t | {item[3]}")

	connection.commit()
	connection.close()


# add new record to the table
def add_one(first, last, email):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
	connection.commit()
	connection.close()


def delete_by_name(first):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()
	# first has to be a tuple to be seen as a single argument
	# if it wouldn't be a tuple it would be recognized as 5 arguments
	cursor.execute("DELETE FROM customers WHERE first_name = ?", (first,))

	connection.commit()
	connection.close()

def delete_by_id(id):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("DELETE FROM customers WHERE rowid = (?)", id)

	connection.commit()
	connection.close()

