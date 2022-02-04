from tkinter import *

root= Tk()
root.title("Belajar New Window")
root.geometry("400x400")

newWindow = Toplevel(root)
newWindow.title("Window Baru")
newWindow.geometry("300x300")

lbl = Label(newWindow, text = "Ini Text dalam new Window").grid()

root.mainloop()