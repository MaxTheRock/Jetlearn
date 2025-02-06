import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Arange function - Creates an array of evenly spaced values within a given interval

x = np.arange(0,10,0.2)

print(x)

y1 = x**2
y2 = x**3

plt.plot(x,x**2,"g--",x,x**3,"b--")
plt.show()