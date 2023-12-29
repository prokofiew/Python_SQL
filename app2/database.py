import sqlite3


CREATE_BEANS_TABLE = """CREATE TABLE beans (
			id INTEGER PRIMARY KEY,
			name TEXT,
			method TEXT,
			rating INTEGER
			)
			"""

INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

def connect():
	return sqlite3.connect('coffee.db')


def create_tables(connection):
	with connection:
		connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
	with connection:
		connection.execute(INSERT_BEAN, (name, method, rating))


# python functions have to return something other way on default
# they return None. Thats why return and fetchall()
def get_all_beans(connection):
	with connection:
		return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name)
	with connection:
		return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()







