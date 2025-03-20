import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn import metrics # Metrics is a toolbox from the sklearn lib that helps us measure how good our model is in the sklearn library
from sklearn.tree import DecisionTreeClassifier

file = pd.read_csv("iris.csv") # Reads the iris csv file

print(file.info()) # Prints the information about the file 

file["species"] = file["species"].replace({"setosa": 0, "versicolor": 1, "virginica": 2}) # Replaces the words with a numerical value instead

from sklearn.model_selection import train_test_split # A tool that splits data into training and testing

y = file["species"]
x = file.drop("species", axis=1) # 0 for rows and 1 for columns
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1) # test_size means 20% data is for testing and the rest is for training, random_state makes sure its the same every time

print(x_train.shape)
print(x_test.shape) # Prints the amount of values in the train and the test x

model1 = DecisionTreeClassifier(max_depth=3, random_state=1) # Creates the model
model1.fit(x_train, y_train) # Using the trained data to train the model (learn a pattern)

prediction = model1.predict(x_test) # Making predictions based on the data given

accuracy = metrics.accuracy_score(prediction, y_test) # Tests the accuracy of the model between 0-1

print(accuracy) # Prints the accuracy of the model
# If your answer is closer to 1, the more accurate your model is
