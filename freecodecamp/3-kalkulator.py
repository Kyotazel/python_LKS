import tkinter as tk

root = tk.Tk()
root.title("Kalkulator Sederhana")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # e.delete(0, tk.END)
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "tambah"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_kurang():
    first_number = e.get()
    global f_num
    global math
    math = "kurang"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_kali():
    first_number = e.get()
    global f_num
    global math
    math = "kali"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_bagi():
    first_number = e.get()
    global f_num
    global math
    math = "bagi"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)
    if math == "tambah":
        e.insert(0, f_num + int(second_number))
    elif math == "kurang":
        e.insert(0, f_num - int(second_number))
    elif math == "kali":
        e.insert(0, f_num * int(second_number))
    elif math == "bagi":
        e.insert(0, f_num / int(second_number))

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=130, pady=20, command=button_clear)

button_kurang = tk.Button(root, text="-", padx=40, pady=20, command=button_kurang)
button_kali = tk.Button(root, text="*", padx=40, pady=20, command=button_kali)
button_bagi = tk.Button(root, text="/", padx=40, pady=20, command=button_bagi)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=6, column=0, columnspan=3)
button_add.grid(row=4, column=0)
button_equal.grid(row=5, column=1, columnspan=1)

button_kurang.grid(row=4, column=2)
button_kali.grid(row=5, column=0)
button_bagi.grid(row=5, column=2)

root.mainloop()