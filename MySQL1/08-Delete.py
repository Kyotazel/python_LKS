import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Ngasem 43'"

myCursor.execute(sql)

mydb.commit()

print(myCursor.rowcount, "Rekaman terhapus")