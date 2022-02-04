import tkinter as tk

root = tk.Tk()
root.title("gridEdit")

kotak1 = tk.Label(root, text="Nama Lengkap: ")
kotak2 = tk.Label(root, text="Alamat : ")
kotak3 = tk.Label(root, text="No Handphone : ")

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

kotak1.grid(row=0, column=0)
kotak2.grid(row=1, column=0)
kotak3.grid(row=2, column=0)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

root.mainloop()