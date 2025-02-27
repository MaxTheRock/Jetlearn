import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv("titanic.csv")

class_counts = titanic_data['Pclass'].value_counts()

plt.pie(class_counts, autopct='%1.1f%%')
plt.title('Number of People in Different Classes on the Titanic')
plt.show()
