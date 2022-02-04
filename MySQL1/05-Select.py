import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT name, address FROM customers")

myResult = myCursor.fetchone()

print(myResult)