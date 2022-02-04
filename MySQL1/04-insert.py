import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Arun", "Ngasem 43")
myCursor.execute(sql, val)

mydb.commit()

print("1 Data ditambahkan, ID : ", myCursor.lastrowid)