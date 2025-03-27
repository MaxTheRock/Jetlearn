import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly   # Higher graphical standards
import plotly.express as px  
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

data.columns = ("State","Country","LastUpdate","Lat","Long","Confirmed","Recovered","Deaths","Active")
data["State"] = data["State"].fillna(value=" ") # Replaces empty data with an empty string
#data.fillna({"State": value}, inplace=True)
topTen = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False)) # Giving top ten countries with most cases

fig1 = px.scatter(topTen, x=topTen.index, y="Confirmed", size="Confirmed", size_max=120, title="Top ten countries with confirmed cases", color=topTen.index)
# color assining different colours to different categories

fig1.write_html("Figure1.html",auto_open=True) # Saves plot to a html file and opens in your browser

