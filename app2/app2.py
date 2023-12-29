import database as db

MENU_PROMPT = """-- Coffe Bean App --

 PLease choose one of three options:

 1) Add a new bean.
 2) See all beans.
 3) Find bean by name.
 4) See which preparation method is best for a bean.
 5) Exit.

 Your selection:"""


def menu():
    connection = db.connect()
    db.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            promt_add_new_bean(connection)
        elif user_input == "2":
            promt_see_all_beans(connection)
        elif user_input == "3":
            promt_find_bean(connection)
        elif user_input == "4":
            promt_find_best_method(connection)
        else:
            print('Choose option 1 to 5')


def display_query_result(result):
    for item in result:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}/100")


def promt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")
    rating = int(input("Enter rating score (0-100): "))
    db.add_bean(connection, name, method, rating)


def promt_see_all_beans(connection):
    all_beans = db.get_all_beans(connection)

    display_query_result(all_beans)


def promt_find_bean(connection):
    name = input("Enter name of bean you're looking for: ")
    bean_by_name = db.get_beans_by_name(connection, name)

    display_query_result(bean_by_name)


def promt_find_best_method(connection):
    name = input("Which bean you want to check?: ")
    best_method = db.get_best_preparation_for_bean(connection, name)
    print(f"Best preparation method for {name} is: {best_method[2]}")


menu()
