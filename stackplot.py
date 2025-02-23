import matplotlib
import matplotlib.pyplot as plt 

days = [1,2,3,4,5]
eating = [2,3,1,4,2]
sleeping = [6,7,8,5,6]
working = [7,8,9,8,6]
playing = [5,4,2,6,4]

plt.plot([], [], color = 'm', label = 'Eating', linewidth = 5)
plt.plot([], [], color = 'c', label = 'Sleeping', linewidth = 5)
plt.plot([], [], color = 'r', label = 'Working', linewidth = 5)
plt.plot([], [], color = 'b', label = 'Playing', linewidth = 5)

plt.stackplot(days, eating, sleeping, working, playing, colors=["m","c","r","b"])
plt.xlabel("Days")
plt.ylabel("Hours spent")
plt.title("Daily activity breakdown")
plt.legend()

plt.show()
