from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "db_sekolah"
)

myCursor = mydb.cursor()

root = Tk()

root.title("CREATE READ UPDATE DELETE")
root.geometry("820x500")

def getValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['nis'])
    e2.insert(0, select['nama'])
    e3.insert(0, select['kelas'])
    e4.insert(0, select['alamat'])

def add():
    nis = e1.get()
    nama = e2.get()
    kelas = e3.get()
    alamat = e4.get()

    try:
        sql = "INSERT INTO siswa VALUES(%s,%s,%s,%s)"
        val = (nis,nama,kelas,alamat)
        myCursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Informasi","Data Berhasil Ditambahkan")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)

def update():
    nis = e1.get()
    nama = e2.get()
    kelas = e3.get()
    alamat = e4.get()

    try:
        sql = "UPDATE siswa SET nama = %s, kelas = %s, alamat = %s WHERE nis = %s"
        val = (nama,kelas,alamat,nis)
        myCursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Informasi", "Data Berhasil Diperbarui")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
    except Exception as e:
        print(e)

def delete():
    nis = e1.get()
    sql = "DELETE FROM siswa WHERE nis = %s"
    val = (nis,)
    myCursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Informasi", "Data Berhasil dihapus")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def show():
    myCursor.execute("SELECT * FROM siswa")
    siswas = myCursor.fetchall()
    print(siswas)

    for i, (nis,nama,kelas,alamat) in enumerate(siswas, start=1):
        listBox.insert("","end",values = (nis,nama,kelas,alamat))

Label(root, text="Pendaftaran Siswa", font=(None, 30)).place(x = 420, y = 5)
Label(root, text="NIS").place(x = 20, y = 50)
Label(root, text="Nama").place(x = 20, y = 75)
Label(root, text="Kelas").place(x = 20, y = 100)
Label(root, text="Alamat").place(x = 20, y = 125)

global e1, e2, e3, e4

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.place(x = 120, y = 50)
e2.place(x = 120, y = 75)
e3.place(x = 120, y = 100)
e4.place(x = 120, y = 125)

Button(root, text="Tambah", height=2, width=11, command=add).place(x = 20, y = 170)
Button(root, text="Perbarui", height=2, width=11, command=update).place(x = 160, y = 170)
Button(root, text="Hapus", height=2, width=11, command=delete).place(x = 300, y = 170)

cols = ('nis','nama','kelas','alamat')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row = 1, column=0, columnspan=2)
    listBox.place(x = 10, y = 240)

show()
listBox.bind('<Double-Button-1>',getValue)

root.mainloop()