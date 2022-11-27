import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
t = np.arange(0, 1.00, 0.05)
n = np.arange(0, 1.00, 0.05)
x = np.sin(2* pi* n)
plt.plot(t, x)
x_Continuous = np.sin(2* pi* t)
plt.stem(t, x, label = "sin[2* pi* n]")
plt.plot(t, x_Continuous, label = "sin(2* pi* t)")
plt.legend()
plt.show()