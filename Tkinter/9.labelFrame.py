from tkinter import *

root = Tk()
root.title("Belajar LabelFrame")
root.geometry("400x400")

fr1 = LabelFrame(root, text = "Text 1", padx = 20, pady = 40)
fr1.grid()

lbl = Label(fr1, text = "Ini adalah LabelFrame").grid()

root.mainloop()