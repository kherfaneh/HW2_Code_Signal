import numpy as np
import matplotlib.pyplot as plot
pi = np.pi
omega = pi / 3
teta = pi / 4
t = np.arange(-5, 5, 0.1)
n = np.arange(-5, 5, 0.1)
x = np.cos((omega * n) + teta)
plt.plot(t, x)
x_Continuous = x = np.cos((omega * t) + teta)
plt.stem(n, x, label = "x[n]")
plt.plot(t, x_Continuous, label = "x(n)")
plt.legend()
plt.show() 