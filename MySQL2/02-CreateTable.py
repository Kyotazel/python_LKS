import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

myCursor.execute("SHOW TABLES")

for x in myCursor:
    print(x)