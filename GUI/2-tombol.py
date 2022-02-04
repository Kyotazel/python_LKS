import tkinter as tk

root = tk.Tk()
root.title("Tombol")

button_1 = tk.Button(root, text="Tombol_1", fg="red", )
button_1.pack(side=tk.TOP)
button_2 = tk.Button(root, text="Tombol_2", fg="blue")
button_2.pack(side=tk.LEFT)
button_3 = tk.Button(root, text="Tombol_3", fg="green")
button_3.pack(side=tk.RIGHT)
button_4 = tk.Button(root, text="Tombol_4", fg="yellow")
button_4.pack(side=tk.BOTTOM)

root.mainloop()