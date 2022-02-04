import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Pagu 03' WHERE address = 'Pagu 21'"

myCursor.execute(sql)

mydb.commit()

print(myCursor.rowcount, "Data Dirubah")