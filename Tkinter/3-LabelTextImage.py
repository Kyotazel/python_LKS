from tkinter import *
root = Tk()

root.title("Belajar Tkinter")
root.geometry("500x300")

lbl = Label(root, text="Hello World", bg="red", fg="blue", padx=10, pady=10)
lbl.place(x=100, y=100)

photo = PhotoImage(file="pngwing.com.png")
photo = photo.zoom(0.2)
lbl2 = Label(root, image=photo)
lbl2.grid()

root.mainloop()