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
        sql = "INSERT INTO siswa(nis, nama, kelas, alamat) VALUES(%s, %s, %s, %s)"
        val = (nis, nama, kelas, alamat)
        myCursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Informasi", "Data Berhasil Ditambahkan")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()

def update():
    nis = e1.get()
    nama = e2.get()
    kelas = e3.get()
    alamat = e4.get()

    try:
        sql = "UPDATE siswa SET nama=%s, kelas=%s, alamat=%s WHERE nis=%s"
        val = (nama, kelas, alamat, nis)
        myCursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Informasi", "Data Berhasil Diubah")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)

def delete():
    nis = e1.get()

    try:
        sql = "DELETE FROM siswa WHERE nis=%s"
        val = (nis,)
        myCursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Informasi", "Data Berhasil Dihapus")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)

def show():
    myCursor.execute("SELECT * FROM siswa")
    siswas = myCursor.fetchall()
    print(siswas)

    for i, (nis, nama, kelas, alamat) in enumerate(siswas, start=1):
        listBox.insert("", "end", values=(nis, nama, kelas, alamat))

root = Tk()
root.title("CRUD")
root.geometry("820x500")
global e1
global e2
global e3
global e4

Label(root, text="Pendaftaran Murid", fg="Black", font=(None, 30)).place(x=400, y=5)
Label(root, text="NIS").place(x=10, y=10)
Label(root, text="Nama").place(x=10, y=40)
Label(root, text="Kelas").place(x=10, y=70)
Label(root, text="Alamat").place(x=10, y=100)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.place(x=140, y=10)
e2.place(x=140, y=40)
e3.place(x=140, y=70)
e4.place(x=140, y=100)

Button(root, text="Tambah", command=add, height=3, width=10).place(x=30, y=130)
Button(root, text="Perbarui", command=update, height=3, width=10).place(x=160, y=130)
Button(root, text="Hapus", command=delete, height=3, width=10).place(x=290, y=130)

cols = ('nis', 'nama', 'kelas', 'alamat')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', getValue)
root.mainloop()