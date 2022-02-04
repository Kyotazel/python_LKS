from tkinter import *
import tkinter.font

root = Tk()
root.title("Register Sederhana")
root.geometry("300x600")

def cetak():
    return

changeFont = tkinter.font.Font(size=20)

Label(root, text = "PENDAFTARAN", font=changeFont).place(x = 50, y = 10)

labelFr = LabelFrame(root, text = "Hasil", padx=20,pady=20)
labelFr.place(x = 60, y = 380)

firstName = Label(root, text = "FirstName").place(x = 20, y = 50)
lastName  = Label(root, text = "LastName").place(x = 20, y = 90)
userName  = Label(root, text = "UserName").place(x = 20, y = 130)
age       = Label(root, text = "Age").place(x = 20, y = 170)
email     = Label(root, text = "Email").place(x = 20, y = 210)
password  = Label(root, text = "Password").place(x = 20, y = 250)
gender    = Label(root, text = "Gender").place(x = 20, y = 290)

e1 = Entry(root, width = 30)
e2 = Entry(root, width = 30)
e3 = Entry(root, width = 30)
e4 = Entry(root)
e5 = Entry(root, width = 30)
e6 = Entry(root, width = 30, show = "*")

e1.place(x = 20, y =70)
e2.place(x = 20, y =110)
e3.place(x = 20, y =150)
e4.place(x = 20, y =190)
e5.place(x = 20, y =230)
e6.place(x = 20, y =270)

r = StringVar()
r.set("Pria")

male = Radiobutton(root, text = "Pria", variable=r, value = "Pria").place(x = 15, y = 310)
female = Radiobutton(root, text = "Wanita", variable=r, value = "Wanita").place(x = 80, y = 310)

def cetak():
    class orang:
        def __init__(self, firstName, lastName, userName, age, email, password, gender):
            self.firstName = firstName
            self.lastName = lastName
            self.userName = userName
            self.age = age
            self.email = email
            self.password = password
            self.gender = gender

        def hasil(self):
            lbl = Label(labelFr, text = "firstName = " + self.firstName + "\n" + 
            "lastName = " + self.lastName + "\n" +
            "age = " + self.age + "\n" + 
            "email = " + self.email + "\n" +
            "password = " + self.password + "\n" + 
            "Gender = " + self.gender).grid()

    tampil = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),r.get()).hasil()

btn = Button(root, text = "Submit", command=cetak, width=20).place(x = 50, y = 350)

root.mainloop()
