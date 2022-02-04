import tkinter as tk
from turtle import width

root = tk.Tk()
root.title("Kalkulator Sederhana")

e = tk.Entry(width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def button_click(number):
    first_number = str(e.get())
    e.delete(0, tk.END)
    e.insert(0, first_number + str(number))

def button_tambah():
    first_number = int(e.get())
    global f_num
    global math
    math = "tambah"
    f_num = first_number
    e.delete(0, tk.END)

def button_kurang():
    first_number = int(e.get())
    global f_num
    global math
    math = "kurang"
    f_num = first_number
    e.delete(0, tk.END)

def button_kali():
    first_number = int(e.get())
    global f_num
    global math
    math = "kali"
    f_num = first_number
    e.delete(0, tk.END)

def button_bagi():
    first_number = int(e.get())
    global f_num
    global math
    math = "bagi"
    f_num = first_number
    e.delete(0, tk.END)

def button_clear():
    e.delete(0, tk.END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, tk.END)
    if math == "tambah":
        e.insert(0, f_num + second_number)
    if math == "kurang":
        e.insert(0, f_num - second_number)
    if math == "kali":
        e.insert(0, f_num * second_number)
    if math == "bagi":
        e.insert(0, f_num / second_number)

button_1 = tk.Button(root, padx="40", pady="20", text="1", command=lambda: button_click(1))
button_2 = tk.Button(root, padx="40", pady="20", text="2", command=lambda: button_click(2))
button_3 = tk.Button(root, padx="40", pady="20", text="3", command=lambda: button_click(3))
button_4 = tk.Button(root, padx="40", pady="20", text="4", command=lambda: button_click(4))
button_5 = tk.Button(root, padx="40", pady="20", text="5", command=lambda: button_click(5))
button_6 = tk.Button(root, padx="40", pady="20", text="6", command=lambda: button_click(6))
button_7 = tk.Button(root, padx="40", pady="20", text="7", command=lambda: button_click(7))
button_8 = tk.Button(root, padx="40", pady="20", text="8", command=lambda: button_click(8))
button_9 = tk.Button(root, padx="40", pady="20", text="9", command=lambda: button_click(9))
button_0 = tk.Button(root, padx="40", pady="20", text="0", command=lambda: button_click(0))

button_equal = tk.Button(root, padx="40", pady="20", text="=", command=button_equal)
button_tambah = tk.Button(root, padx="40", pady="20", text="+", command=button_tambah)
button_kurang = tk.Button(root, padx="40", pady="20", text="-", command=button_kurang)
button_kali = tk.Button(root, padx="40", pady="20", text="*", command=button_kali)
button_bagi = tk.Button(root, padx="40", pady="20", text="/", command=button_bagi)
button_clear = tk.Button(root, padx="123", pady="20", text="Clear", command=button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=1)
button_tambah.grid(row=4, column=0)
button_kurang.grid(row=4, column=2)

button_kali.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_bagi.grid(row=5, column=2)

button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()