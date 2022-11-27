import numpy as np
import matplotlib.pyplot as plot
pi = np.pi
r = 1
c = 2
teta = pi/4
omega = pi/3
t = np.arange(-5, 5)
n = np.arange(-5, 5)
x = np.absolute(c)*np.exp(r * n) * np.cos(omega * n + teta)
plt.plot(t, x)
x_Continuous = np.absolute(c) * np.exp(r * t) * np.cos(omega * t + teta)
plt.stem(n, x, label = "x[n]")
plt.plot(t, x_Continuous, label = "x(t)")
plt.legend()
plt.show() 