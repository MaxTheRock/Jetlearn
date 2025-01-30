import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

# plt.plot(x,y,'ro')
# plt.plot(x,y)
# plt.axis([0,10,0,200])

plt.plot(x,y,'r--',label='y = x',linewidth=4)
plt.axis([0,10,0,50])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample")
plt.legend() # This function is a utility in a given library that gives a way to label and differentiate multiple labels in a given graph
plt.show()