import tkinter as tk

root = tk.Tk()

root.title("Input Nama")

e = tk.Entry(root, width=50, borderwidth=2)
e.pack()

def klikTombol():
    hello = "Halo {}".format(e.get())
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()

myButton = tk.Button(root, text="Masukkan nama",command=klikTombol )
myButton.pack()

root.mainloop()