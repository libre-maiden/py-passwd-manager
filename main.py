from commands import *
import time

def main():
    print(""" 
Commands:
"create" - create data
"display" - display database
"update" - update data
"delete" - delete data
"exit" - exit from programm
""")

    select = input("Select command: ")

    if select == "create":
        create()
        display()
        time.sleep(0.4)
        main()

    elif select == "display":    
        display()
        time.sleep(0.4)
        main()

    elif select == "update":
        update()
        display()
        time.sleep(0.4)
        main()

    elif select == "delete":
        delete()
        display()
        time.sleep(0.4)
        main()

    elif select == "exit":
        exit()    

main()