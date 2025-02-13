import pandas as pd

df1 = pd.read_csv("titanic.csv")

print(df1["Pclass"].mean())