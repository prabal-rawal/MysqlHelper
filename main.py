import mysql.connector
from mysql.connector.plugins import mysql_native_password

default_authentication_plugin = mysql_native_password
db = mysql.connector.connect(host="localhost", user="root", passwd="Bsr4755@")

if db.is_connected():
    print("Connected")
else:
    print("Not connected")

db.close()
