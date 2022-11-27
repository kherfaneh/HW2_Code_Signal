import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
n = np.arange(0, 6)
t = np.arange(0,  6 , 0.1)
j = complex(0, 1)
res1 = j * 1/3
res2 = j * 4/3
x = np.exp(pi *(res1)* n) + np.exp(pi *(res2)* n)
x_Continuous = np.exp(pi *(res1)* t) + np.exp(pi *(res2)* t)
plt.stem(n, x, label = "e^(pi*(1/3*n)*j) + e^(pi*(4/3*n)*j)")
plt.plot(t, x_Continuous, label = "e^(pi*(1/3*t)*j) + e^(pi*(4/3*t)*j)")
plt.legend()
plt.show()