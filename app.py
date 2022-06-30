import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
import plotly.graph_objects as go
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def app():
    return 'Hello, World!'