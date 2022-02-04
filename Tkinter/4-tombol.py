from tkinter import *
root = Tk()

root.geometry("500x300")
root.title("Belajar Tombol")

def fungsinya():
    label = Label(root, text="Kata Setelah Klik")
    label.grid()
    btn2 = Button(root, text="Tombol Baru")
    btn2.grid()

btn = Button(root, text="Click Me", command=fungsinya, padx=10, pady=10)
btn.grid()

root.mainloop()