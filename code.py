import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
number_start = float(input("Please enter the starting point of the domain:"))
number_end = float(input("Please enter the ending point of the domain:"))
if number_start < 0:
    number_start = 0
if number_end < 0:
    number_end = 0
    
if number_start > 5:
    number_start = 5
if number_end > 5:    
    number_end = 5
    
print(number_start)
print(number_end)
t = np.arange(number_start, number_end, 0.1)
#t = np.arange(0, 5, 0.1)
x_Continuous = 3*np.sin(pi*t) + 3*np.absolute(np.cos(7* t))
plt.plot(t, x_Continuous, label = "3*np.sin(pi*t) + 3*|np.cos(7* t)|")
plt.legend()
plt.show() 