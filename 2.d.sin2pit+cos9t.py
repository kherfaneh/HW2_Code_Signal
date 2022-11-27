import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
t = np.arange(0, 6.3, 0.1)
n = np.arange(0, 6.3, 0.1)
x = np.sin(2* pi* n) + np.cos(9* n) 
plt.plot(t, x)
x_Continuous = np.sin(2* pi* t) + np.cos(9* t) 
plt.stem(n, x, label = "cos[9* n] + sin[2* pi* n]")
plt.plot(t, x_Continuous, label = "cos(9* t) + sin(2* pi* t)")
plt.legend()
plt.show() 