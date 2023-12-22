import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

# print('\nloop')
# for i in cursor:
# 	print(i)

# printing names
items = cursor.fetchall()

names = []
for item in items:
	names.append(item[0])

print(names, sep='\n')


# print('\nfetchall')	
# print(cursor.fetchall())

# whole_table = cursor.fetchall()
# print(whole_table)

# first_person = cursor.fetchmany(1)
# print(first_person)

# because we get a tuple we can add [position]
# print('\nfetchone')
# print(cursor.fetchone()[0])

# print('\nfetchmany')
# print(cursor.fetchmany(3))

connection.commit()
connection.close()