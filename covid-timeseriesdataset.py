import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly
import plotly.express as px  
import plotly.graph_objects as go # Used when you want more control over graphs and when you want to draw multiple things on a graph
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data2.csv")

data["DateReported"] = pd.to_datetime(data["DateReported"]) # Converting simple plain string into a date time format

time_series_dates = data.groupby("DateReported").sum()

print(time_series_dates)

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=time_series_dates.index, y=data["Cumulative_cases"]))

fig1.write_html("Figure_1.html", auto_open=True)

# Homework - Draw a figure on cumulative deaths, new cases and new deaths
