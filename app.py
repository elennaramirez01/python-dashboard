import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
import plotly.graph_objects as go
import os

app = dash.Dash(__name__)
server = app.server
ss
data = pd.read_csv(r"C:\Users\moham\PycharmProjects\pythonProject2\100 Sales Records.csv")

fig = px.bar(data, x="Item Type", y="Total Profit", color="Region", title="Total Profit By Item Type and Region")
fig2 = px.pie(data, values="Total Profit", names="Region", title="Total Profit By Region")

data = data.sort_values(by='Total Revenue', ascending=False)
total_cost_series = data.groupby('Region')['Total Cost'].sum()
total_revenue_series = data.groupby('Region')['Total Revenue'].sum()

fig3 = go.Figure(data=[
    go.Bar(name='Total Revenue', x=total_revenue_series.index.array, y=total_revenue_series.array),
    go.Bar(name='Total Cost', x=total_cost_series.index.array, y=total_cost_series.array)
])
fig3.layout.title = "Total Revenue and Costs By Regions"

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='g1', figure=fig2)
        ], className="gross-profit-graphs"),

        html.Div([
            dcc.Graph(id='g2', figure=fig3)
        ], className="gross-profit-graphs"),
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)

