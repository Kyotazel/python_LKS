from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,8,1,10])

plt.plot(x,marker='o', ms=20, mfc='r')
plt.show()