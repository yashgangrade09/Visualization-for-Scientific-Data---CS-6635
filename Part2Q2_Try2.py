import csv
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import plotly.plotly as py
import plotly as ppy
import plotly.graph_objs as go
import pandas as pd
ppy.tools.set_credentials_file(username='yashgangrade09', api_key='iCRe8RkQlDNOkQzNYmbS')

df = pd.read_csv("Dataset/congress-terms.csv")

data = [
    go.Parcoords(
        line = dict(color = df['state'],
                   colorscale = [[0,'#FFFFFF'],[0.5,'#FFFFFF'],[1,'#FFFFFF']]),

        dimensions = list([
            dict(range=[45, 62], label = 'Age', values = df['age']),
            dict(range=[75, 115], label = 'Congress', values = df['congress']),
        ])
    )
]

layout = go.Layout(
    paper_bgcolor = '#FFFFFF',
    plot_bgcolor = '#000000'
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = 'base')