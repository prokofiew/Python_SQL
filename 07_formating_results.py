import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")

# brings one record - one tuple, so we can acces it with indexes
# print(cursor.fetchone()[0])

f_and_l_names = cursor.fetchall()
counter = 1
for i in f_and_l_names:
	print(counter, i[0] + ', ' + i[1])
	counter += 1


connection.commit()
connection.close()
