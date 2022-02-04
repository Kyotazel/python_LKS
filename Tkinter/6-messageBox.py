from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Belajar MessageBox")
root.geometry("300x300")

def pesan():
    psn = messagebox.askquestion("info Baru", "Ini adalah sebuah info")
    if psn == "yes":
        Label(root, text = "yes").grid()
    elif psn == "no":
        Label(root, text = "no").grid()

btn = Button(root, text = "Click Me", command=pesan)
btn.grid()

root.mainloop()