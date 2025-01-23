import pandas as pd

df1 = pd.read_csv("iris.csv")

print(df1.head())
print(df1.info())

print("Petal Length Mean: ", df1["petal_length"].mean())
print("Petal Width Mean: ", df1["petal_width"].mean())
print("Sepal Length Mean: ", df1["sepal_length"].mean())
print("Sepal Width Mean: ", df1["sepal_width"].mean())

print("Petal Length Max: ", df1["petal_length"].max())
print("Petal Width Max: ", df1["petal_width"].max())
print("Sepal Length Max: ", df1["sepal_length"].max())
print("Sepal Width Max: ", df1["sepal_width"].max())

print("Petal Length Min: ", df1["petal_length"].min())
print("Petal Width Min: ", df1["petal_width"].min())
print("Sepal Length Min: ", df1["sepal_length"].min())
print("Sepal Width Min: ", df1["sepal_width"].min())

setosa = df1[df1["species"]=="setosa"] # Creates a new dataframe

print(setosa.shape)

versicolor = df1[df1["species"]=="versicolor"]

print(versicolor.shape)

virginica = df1[df1["species"]=="virginica"]

print(virginica.shape)

df2 = setosa.sort_values(by="sepal_length", ascending=True) # Sort Values will sort a dataset. by = choosing the column and acending = True or False

print(df2)

df_renamed = df1.rename(columns={"sepal_length":"s_length", "petal_length":"p_length"})

print(df_renamed)

print(df_renamed.agg({"s_length":["min","max","median"],"p_length":["min","max","median"]}))
