import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Wates 12", )

myCursor.execute(sql, adr)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)