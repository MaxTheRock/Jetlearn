import pandas as pd

d1 = {
    "calories" : [400,300,100],
    "duration" : [50,40,30]
}

# Data Frame
df = pd.DataFrame(d1,index=["day1","day2","day3"])
print(df)

print(df.loc["day1"])

d2 = {
    "cars" : ["audi","bmw","nissan"],
    "models" : ["R18","Charger","GTR"]
}

print()

df2 = pd.DataFrame(d2)
print(df2)

a1 = [1,2,3,4]

# Series
s1 = pd.Series(a1,index=["w","x","y","z"])
print(s1)

print(s1["y"])

d3 = {
    "d1" : 100,
    "d2" : 200,
    "d3" : 300
}

s2 = pd.Series(d3)
print(s2)

df3 = pd.read_csv("data.csv")
print(df3)

print(pd.options.display.max_rows)

# to_string() to print the whole csv file
# If under 60 then it prints the whole file else it prints first 5 and last 5.

# Comma Separated Value files - CSV
# JavaScript Object Notation  - JSON

print(df3.head(10)) # Head method returns the headers and the specified number of rows starting from the top

print(df3.shape) # Returns the tuple telling how many rows and collumns there are

print(df3[["Pulse","Calories"]])

print(df3.info()) # The info gives the the consise summary of the dataframe

print(df3.describe()) # Gives you descriptive statistics for numerical values

print(df3.isin([60])) # Checks if the value is there on not and it alwals returns a dataframe similar to hte origin but it replaces the values with True or False
# In the isin function the parameter can be a value, a list, dictionary, series or dataframe

d = {
    'name': ['bob','jack','bill'],
    'age': [30,40,50]
}

df4 = pd.DataFrame(d)

s = pd.Series({'age':30,'age':40})

print(df4.isin(s))

# In this case, the result will only work if there is only 1 row in case of dataframe or series 

print(df3["Calories"].max())

above500 = df3[df3["Calories"]>500]

print(above500.shape)

above300less1000 = df3[(df3["Calories"]>500) & (df3["Calories"]<1000)] # and=&  or=|

print(above300less1000)