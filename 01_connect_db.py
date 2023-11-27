import mysql.connector


mydb1 = mysql.connector.connect(host="localhost", user="filip", passwd="1234")

mycurson1 = mydb1.cursor()

# print databases
print('---------- printing databases with SHOW DATABASES---------')
mycurson1.execute("show databases")

# the same with
for i in mycurson1:
	print(i)


print('\n--------- connecting to databse and printing all from employees db--------')
# getting from particular database
mydb2 = mysql.connector.connect(host="localhost", user="filip", passwd="1234", database="sql_course")

mycursor2 = mydb2.cursor()
mycursor2.execute("SELECT * FROM employees")
# other way
result_1 = mycursor2.fetchall()
for i in result_1:
	print(i)

print('\n---------- printing one row --------------------')
mycursor2.execute("SELECT * FROM employees")
result_2 = mycursor2.fetchone()
for i in result_2:
	print(i)