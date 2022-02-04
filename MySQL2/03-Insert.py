import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "ForSQL"
)

myCursor = mydb.cursor()

sql = "INSERT INTO favorit 'makanan' VELUES '%s'"
val = 'permen'
myCursor.execute(sql, val)

mydb.commit()

print(myCursor.rowcount, "Data Ditambahkan")