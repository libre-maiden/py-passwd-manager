from models import *
from rich.console import Console
from rich.table import Table

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

        print('Entry is create!')
    else:
        print('Entry is exist!')

def update():
    name = input('Name: ')
    new_name = input('New name: ')
    username = input('Username: ')
    password = input('Password: ')
    description = input('Description: ')

    cur.execute(f"SELECT name FROM data WHERE name = '{name}'")        
    cur.execute(f'UPDATE data SET name = "{new_name}", username = "{username}", password = "{password}", description = "{description}" WHERE name = "{name}"')
    conn.commit()
    print('Entry is update!')

def delete():
    name = input('Name: ')

    cur.execute(f"SELECT name FROM data WHERE name = '{name}'")
    cur.execute(f"DELETE FROM data WHERE name = '{name}'")
    conn.commit()
    print("Entry is delete")    

def display():   
    table = Table()
    
    table.add_column("Name", justify="right", style="cyan")
    table.add_column("Username", justify="center", style="cyan")
    table.add_column("Password", justify="left", style="cyan")
    table.add_column("Description", justify="left", style="cyan")

    for value in cur.execute("SELECT * FROM data"):
        table.add_row(value[0], value[1], value[2], value[3])

    console = Console()
    console.print(table)