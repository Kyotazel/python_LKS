import tkinter as tk

root = tk.Tk()
root.title("Widget")

satu = tk.Label(root, text = "Judul Program", bg = "grey", fg = "black")
satu.pack()

dua = tk.Label(root, text = "Keterangan", bg = "red", fg = "white")
dua.pack(fill = tk.X)

tiga = tk.Label(root, text = "Input", bg="green", fg="white")
tiga.pack(side = tk.RIGHT, fill=tk.Y)

root.mainloop()