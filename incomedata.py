import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly
import plotly.express as px  
import plotly.graph_objects as go # Used when you want more control over graphs and when you want to draw multiple things on a graph
from plotly.subplots import make_subplots

data = pd.read_csv("adult.csv")

print(data.describe())
print(data.info())
