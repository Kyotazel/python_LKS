import numpy as np
import matplotlib.pyplot as plt


masuk = int(input("masukan data yang di inginkan : "))
datamasuk= [int(input())for i in range (masuk)]

print("berikut hasil data sebelum di sortir : ",end=' ')
print(datamasuk)

datamasuk.sort(reverse=True)
print("berikut hasil data sesudah di sortir : ", end=' ')
print(datamasuk)

plt.plot(datamasuk)
plt.show()