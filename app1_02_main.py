import app1_01_database

# func show table content
# app1_01_database.show_all()

# add one record
# app1_01_database.add_one('Filip', 'Maciborski', 'filip.mac@gmail.com')

# delete with name argument
# app1_01_database.delete_by_name("Filip")

# delete record with given id
# app1_01_database.delete_by_id("7")

# add multiple records
# items = [
# 	('Anna', 'Nowak', 'anna.nowak@gmail.com'),
# 	('Marek', 'Brzoza', 'marek.brzoza@gmail.com'),
# 	('Ewa', 'Miska', 'ewa.miska@wp.pl')

# ]
# app1_01_database.add_many(items)


# app1_01_database.show_all()

app1_01_database.email_lookup('ewa.miska@wp.pl')