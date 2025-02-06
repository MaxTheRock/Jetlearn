import matplotlib
import matplotlib.pyplot as plt 

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("Age interval")
plt.ylabel("Frequency")
plt.show()
