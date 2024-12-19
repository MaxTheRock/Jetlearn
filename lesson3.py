import pandas as pd

d1 = {
    "calories" : [400,300,100],
    "duration" : [50,40,30]
}

df = pd.DataFrame(d1,index=["day1","day2","day3"])
print(df)

print(df.loc["day1"])