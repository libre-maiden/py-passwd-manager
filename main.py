from models import *


def create():
    name = input('Name: ')
    username = input('Username: ')
    password = input('Password: ')
    description = input('Description: ')

    cur.execute(f"SELECT name FROM data WHERE name = '{name}'")
    if cur.fetchone() is None:
        cur.execute(f"""INSERT INTO data(name, username, password, description) 
            VALUES('{name}', '{username}', '{password}', '{description}')""")
        conn.commit()

        print('Data is create!')
    else:
        print('Data is exist!')

def display():   
    for value in cur.execute("SELECT * FROM data"):
        print(f"Name: {value[0]}, Username: {value[1]}, Password: {value[2]}, Description: {value[3]}")

def main():
    print(""" 
Commands:
"create" - create data
"display" - display database
""")

    select = input("Select command: ")

    if select == "create":
        create()
        display()

    elif select == "display":    
        display()    

main()