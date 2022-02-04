import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
mylabel = ["apel", "Pisang", "Cherry", "Anggur"]
myExplode = [0.2, 0, 0, 0]

plt.pie(x, labels=mylabel, explode=myExplode, shadow=True)
plt.legend(title="Buah Buahan")
plt.show()