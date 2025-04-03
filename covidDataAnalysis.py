import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly   # Higher graphical standards
import plotly.express as px  
import plotly.graph_objects as go # Used when you want more control over graphs and when you want to draw multiple things on a graph
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

topTenDeaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False)) 

fig2 = px.bar(topTenDeaths, y=topTenDeaths.index, x="Deaths", title="Top ten countries with largest deaths", color="Deaths", color_continuous_scale=["red","white"], orientation="h")

fig2.write_html("Figure2.html", auto_open=True)

topTenRecovered = pd.DataFrame(data.groupby("Country")["Recovered"].sum().nlargest(10).sort_values(ascending=False))

fig3 = px.bar(topTenRecovered, y=topTenRecovered.index, x="Recovered", title="Top ten recovered countries", color="Recovered", color_continuous_scale=["white","blue"])

fig3.write_html("Figure3.html", auto_open=True)

topStates = data["Country"] == "US"
topStates = data[topStates].nlargest(5,"Confirmed")

top5UK = data["Country"] == "United Kingdom"
top5UK = data[top5UK].nlargest(5,"Confirmed")

fig4 = px.bar(topStates, y=topStates.index, x="Confirmed", title="Top five states in US with largest Confirmed Cases", color="Confirmed", color_continuous_scale=["Green","Red"])

fig4.write_html("Figure4.html", auto_open=True)

fig5 = go.Figure(data=[go.Bar(name="Confirmed Cases", x=top5UK["Confirmed"], y=top5UK["State"], orientation="h")])

fig5.write_html("Figure5.html", auto_open=True)
