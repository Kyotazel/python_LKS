from tkinter import *

root = Tk()

root.title("Belajar RadioButton")
root.geometry("300x300")

r = StringVar()
r.set("male")

def cetak(nilai):
    Label(root, text = nilai).grid()

rb1 = Radiobutton(root, text = "Laki - Laki", variable=r, value = "male",command=lambda:cetak(r.get())).grid()
rb2 = Radiobutton(root, text = "Perempuan", variable=r, value = "female",command=lambda:cetak(r.get())).grid()

root.mainloop()