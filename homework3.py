# Homework

import pandas as pd

data = pd.read_csv("titanic.csv")

print(data.groupby("Sex")["Age"].mean())

print(data["Pclass"].value_counts())

print(data.iloc[5:10, 2:5])

print(data.loc[data["Age"] > 18, ["Name", "Age"]])

data_sorted = data.sort_values(by="Age", ascending=False)

print(data_sorted.head())

data.to_csv("changedData.csv", index=False)

print(data.agg({"Age": ["min", "max", "median"], "Fare": ["min", "max", "median"]}))

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

data["NameLowercase"] = data["Name"].str.lower()

data["Surname"] = data["Name"].str.split(",").str.get(0)

data["SexShort"] = data["Sex"].replace({"male": "M", "female": "F"})

