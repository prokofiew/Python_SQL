import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

print('\nloop')
for i in cursor:
	print(i)


# print('\nfetchall')	
# print(cursor.fetchall())

# print('\nfetchone')
# print(cursor.fetchone())

# print('\nfetchmany')
# print(cursor.fetchmany(3))

connection.commit()
connection.close()