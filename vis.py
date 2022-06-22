import pandas as pd
import plotly.express as px
from plotly.graph_objects import Scatter, Figure
import numpy as np

# reading the database
data = pd.read_csv(r"C:\Users\moham\PycharmProjects\pythonProject2\100 Sales Records.csv")


fig = px.bar(data, x="Item Type", y="Total Profit", color="Region", title="Total Profit By Item Type and Region")

fig.show()

# Second Chart Scatter plot
###data = pd.read_csv(r"C:\Users\moham\PycharmProjects\pythonProject2\100 Sales Records.csv")


#data = pd.read_csv(r"C:\Users\moham\PycharmProjects\pythonProject2\100 Sales Records.csv")

#fig = px.scatter(data, x="Total Cost", y="Unit Price",
                 #size="Units Sold", color="Region",
                 #hover_name="Region", log_x=True, size_max=60)

#fig.show()
