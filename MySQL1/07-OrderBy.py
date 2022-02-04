import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)