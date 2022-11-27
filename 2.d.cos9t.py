import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
t = np.arange(0, 0.75, 0.05)
n = np.arange(0, 0.75, 0.05)
x = np.cos(9* n)
plt.plot(t, x)
x_Continuous = np.cos(9* t)
plt.stem(t, x, label = "cos[9* n]")
plt.plot(t, x_Continuous, label = "cos(9* t)")
plt.legend()
plt.show()