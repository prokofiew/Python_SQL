import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")

# brings one record - one tuple, so we can acces it with indexes
# print(cursor.fetchone()[0])

names_and_surnames = cursor.fetchall()
counter = 1
for i in names_and_surnames:
	if len(i[1]) < 5:
		print(f"{counter}. {i[0]} {i[1]} \t\t | email: {i[2]}")
		counter += 1 
	else:
		print(f"{counter}. {i[0]} {i[1]} \t | email: {i[2]}")
		counter += 1


connection.commit()
connection.close()
