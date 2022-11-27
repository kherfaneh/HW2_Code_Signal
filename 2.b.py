import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
t = np.arange(0, 1.50, 0.1)
n = np.arange(0, 1.50, 0.1)
x = np.absolute(np.sin(((2* pi)/3)* n)) + np.cos((4* pi)/3* n) 
plt.plot(t, x)
x_Continuous = np.absolute(np.sin(((2* pi)/3)* t)) + np.cos((4* pi)/3* t) 
plt.stem(n, x, label = "sin[((2* pi)/3)* t) + cos[(4* pi)/3* t]")
plt.plot(t, x_Continuous, label = "sin(((2* pi)/3)* t)) + cos( (4* pi)/3* t)")
plt.legend()
plt.show() 