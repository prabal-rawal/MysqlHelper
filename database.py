import os
import mysql.connector as mcon

db = mcon.connect(host="localhost", user="root", passwd="Bsr4755@", auth_plugin="mysql_native_password")

cur = db.cursor()
def show_all():
    cur.execute("Show databases")
    print("Databases: ")
    for (databases) in cur:
        print(databases[0])
    print()
    print()

def create_new():
    db_name = input("Name of database to be initialized: ")
    query1 = "create database " + db_name
    query2 = "use " + db_name

    os.system("clear")
    try:
        cur.execute(query1)
        print("Database created successfully")
    except:
        print("Error creating the database")

    try:
        cur.execute(query2)
        print("Database changed to " + db_name)
    except:
        print("Error while changing the database ")
    cur.close()


def existing_db():
    os.system("clear")
    show_all()
    db_name = input("Which database would you like to connect? ")
    query = "use " + db_name

    try:
        cur.execute(query)
        print("Database Changed to " + db_name)
    except:
        print("Error while changing the database")
    cur.close()


def connection():
    db.is_connected()
    