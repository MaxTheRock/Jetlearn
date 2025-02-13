import matplotlib
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,5,6,11,12],label="Regular")
plt.plot([1,2,3,4,5],[1,25,36,121,144],label="Squared Numbers")
plt.legend()
plt.show()