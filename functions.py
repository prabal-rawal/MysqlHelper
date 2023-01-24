import database as dbd
import os

def menu():
    if dbd.connection:
        while True:
            print("1. Connect to database")
            print("2. Create table")
            print("3. Insert data into table")
            print("4. Update data in table")
            print("5. Delete data from table")
            print("6. Select data from table")
            print("7. Exit")
            choice = int(input("Please enter your choice: "))
            os.system("clear")
            if choice == 1:
                connect_to_database()
            elif choice == 7:
                exit()


def connect_to_database():
    print("1. Create new database")
    print("2. Connect to existing database")
    print("3. Show all databases")
    print("4. Goto previous menu")
    choice = int(input("Enter your choice: "))
    os.system("clear")
    if choice == 1:
        dbd.create_new()
    elif choice == 2:
        dbd.existing_db()
    elif choice == 3:
        dbd.show_all()
    elif choice == 4:
        menu()
