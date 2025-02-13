import pandas as pd

df1 = pd.read_csv("titanic.csv")

ages = df1.loc[df1["Age"]>18,"Name"]

print(ages)

print(df1.iloc[9:25,2:5]) # The first index is for rows, second index is for the column. Slicing here is the same a numpy slicing.

print()

print(df1.iloc[0:11,0:3])

df1.iloc[0:5, 0] = 1

print(df1["Survived"])

df1.to_csv("changed_titanic.csv") # to_csv method allows you to save pandas dataframe as a csv file.

df1["Total fare"] = df1["Fare"] + 2

df1["Multiple"] = df1["Fare"] * df1["Pclass"]

print(df1)

print(df1["Pclass"].value_counts) # Gives you the count of unique values in the column

print(df1.groupby("Sex")["Age"].mean()) # Used to group the data in 1 or more categories and then perform different operations

df3 = df1.sort_values(by="Age", ascending=False)

print(df3)