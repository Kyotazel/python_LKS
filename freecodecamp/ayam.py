import tkinter as tk

root = tk.Tk()

root.title("Harga Ayam")

e = tk.Entry(root)
e.pack()

def hargaAyam():
    f_num = int(e.get())
    harga = f_num * 20000
    harga = str(harga)
    myLabel = tk.Label(root, text="Harga : " + harga)
    myLabel.pack()


myButton = tk.Button(root, text="Hitung Harga", command=hargaAyam)
myButton.pack()

root.mainloop()