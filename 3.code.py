import numpy as np
import matplotlib.pyplot as plt

def print_odd_even_chart(signal):
    signal_posetive = np.absolute(signal)
    x_odd = (signal - signal_posetive) / 2
    x_even = (signal + signal_posetive) / 2
    figure, axis = plt.subplots(3, 1)
    axis[0].stem(n, signal, use_line_collection=True)
    axis[0].set_title("x(n)")
    axis[1].stem(n, x_odd, use_line_collection=True)
    axis[1].set_title("x_odd")
    axis[2].stem(n, x_even, use_line_collection=True)
    axis[2].set_title("x_even")
    plt.show()
    
def x_sin_withB(n: np.ndarray, A, B):
    return A* np.sin((B*np.pi)*n)
def x_sin(n: np.ndarray, A):
    return A* np.sin(n)

def x_cos_withB(n: np.ndarray, A, B):
    return A* np.cos((B*np.pi)*n)
def x_cos(n: np.ndarray, A):
    return A* np.cos(n)

def e(n: np.ndarray, A, B):
    return A*(np.exp(B*j*n))
def e_withC(n: np.ndarray, A, B, C):
    return A*(np.exp(B*j*(C*(np.pi))*n))

def choice_1(n):
    print("A*sin((B*pi)*n)")
    A = float(input("A:"))
    B = float(input("B:"))
    if B == 0:
        return x_sin(n, A)
    else:
        return x_sin_withB(n, A, B)      
    #plt.stem(n, x_sin_withB(n, A, B), use_line_collection = True)
    #plt.show()

def choice_2(n):
    print("A*cos((B*pi)*n)")
    A = float(input("A:"))
    B = float(input("B:"))
    if B == 0:
        return x_cos(n, A)
    else:
        return x_cos_withB(n, A, B)      
    #plt.stem(n, x_cos_withB(n, A, B), use_line_collection = True)
    #plt.show()    

def choice_3(n):
    print("A*(e^ B*j*(C*pi)*n)")
    A = float(input("A:"))
    B = float(input("B:"))
    C = float(input("C:"))
    if C == 0:
        return e(n, A, B)
    else:
        return e_withC(n, A, B, C)      
    #plt.stem(n, x_cos_withB(n, A, B), use_line_collection = True)
    #plt.show() 
    
print("1.sin")
print("2.cos")
print("3.e")
pi = np.pi
number_choice = input("Please select your desired option:")
print("Please enter the range in which you want the chart to be drawn:")
start_point = float(input("starting point:"))
end_point = float(input("end point:"))
n = np.arange(start_point , end_point)
j = complex(0, 1)
if number_choice == "1":
    signal = choice_1(n)
if number_choice == "2":
    signal = choice_2(n)
if number_choice == "3":
    signal = choice_3(n)
    

print_odd_even_chart(signal)