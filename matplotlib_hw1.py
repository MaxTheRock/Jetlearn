import matplotlib.pyplot as plt

x = [i for i in range(51)]
a, b = map(float, input("Enter coefficients a and b (ax + b): ").split())

y = [a * i + b for i in x]

plt.plot(x, y, 'b-', label='Linear Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Equation')
plt.legend()
plt.grid()
plt.show()
