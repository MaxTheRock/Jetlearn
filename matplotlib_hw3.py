import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd

df1 = pd.read_csv("titanic.csv")

'''
class_counts = df1["Sex"].value_counts()

print(class_counts)

c = ["male","female"]
v = [573,314]

plt.bar(c,v)
plt.show()

'''

class_counts = df1.groupby("Sex")["Fare"].mean()

print(class_counts)

class_counts.plot(kind="bar", color=["pink","blue"]) # You can modify the kind parameter so you can plot different types of graphs
plt.show()
