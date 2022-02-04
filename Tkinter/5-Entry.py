from tkinter import *
root = Tk()

root.title("Program Entry")
root.geometry("300x300")

def submit():
    lbl = Label(root, text = e.get())
    lbl.grid()

def delete():
    e.delete(0, END)

e = Entry(root, show = "*")
e.grid()

submit = Button(root, text="Submit", command=submit)
submit.grid()
delete = Button(root, text="Hapus", command=delete)
delete.grid()

root.mainloop()