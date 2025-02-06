# Task - Plot the graph of count of passengers in different Pclass on a bar plot

import matplotlib.pyplot as plt 
import pandas as pd

df1 = pd.read_csv("titanic.csv")

class_counts = df1["Pclass"].value_counts().sort_index()

plt.bar(class_counts.index,class_counts.values)

plt.xlabel("Pclass")
plt.ylabel("Passenger count")

plt.show()

d1 = {
  "name": [1,2,3,4,5,6,7,8,9,10],
  "id": [1,2,3,4,5,6,7,8,9,10]
}