#!/usr/bin/python
import numpy as np

import my_functions_lib as fun 

x0 = 0.0
t0 = 0.0
t_end = 10.0
dt = (0.01)

def f(x,t):
	return -x**3 + np.sin(t)

t_values_new = fun.euler_method(f, x0, t0, t_end, dt)[0]
x_values_new = fun.euler_method(f, x0, t0, t_end, dt)[1]
import matplotlib.pyplot as plt 
plt.figure(figsize=(8,5))
plt.plot(t_values_new, x_values_new, label="Euler Approximation", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Euler Method Solution for dx/dt = -x^3 - sint")
plt.grid(True)
plt.legend()
plt.show()