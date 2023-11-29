import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()


many_customers = [
					('Wes', 'Brown', 'wes@brown.com'), 
					('Steph', 'Kuewa', 'steph@kuewa.com'), 
					('Dan', 'Pas', 'dan@pas.com'),
				]

# '?' is a placeholder in sqlite3. its name, last_name and email. Then we pass the variable with list
# IMPORTANT - use EXECUTEMANY()
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)





print('Command executed')
connection.commit()

connection.close()




