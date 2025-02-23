import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 5))
plt.subplot(3,2,1) # [First]=number of rows  [Second]=number of columns  [Third]=index
plt.plot([1,2,3,4,5], [10,20,30,40,50], "b")
plt.title("Lineplot")

plt.subplot(1,2,2)
plt.bar(["a","b","c","d"], [1,2,3,4], color="red")
plt.title("Bar chart")

plt.tight_layout() # Adjusts the layout so there isnt any overlapping

plt.show()