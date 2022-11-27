import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
n = np.arange(0, (14 * pi)/3)
t = np.arange(0,  (14 * pi)/3 + 0.1 , 0.1)
j = complex(0, 1)
res = j * 3/7
x = np.exp((res) * n)
x_Continuous = np.exp((res) * t)
plt.stem(n, x, label = "e^((3/7*n)*j)")
plt.plot(t, x_Continuous, label = "e^((j * 3/7)*t)")
plt.legend()
plt.show()