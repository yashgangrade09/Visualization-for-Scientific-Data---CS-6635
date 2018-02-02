import csv
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import plotly.plotly as py
import plotly as ppy
import plotly.graph_objs as go
import pandas as pd
from pandas.plotting import parallel_coordinates
ppy.tools.set_credentials_file(username='yashgangrade09', api_key='iCRe8RkQlDNOkQzNYmbS')

def method1():
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

df = pd.read_csv('Dataset/congress-terms.csv')
df = df.drop(['bioguide', 'firstname', 'lastname', 'middlename', 'suffix', 'birthday'], axis =1)

df['congress'] = df['congress'].astype('category')
df['chamber'] = df['chamber'].astype('category')
df['state'] = df['state'].astype('category')
df['party'] = df['party'].astype('category')
df['incumbent'] = df['incumbent'].astype('category')
df['termstart'] = df['termstart'].astype('category')
data = df.sample(n = 10)
print(data.head())
data['congress'] = data['congress'].cat.codes
data['chamber'] = data['chamber'].cat.codes
data['state'] = data['state'].cat.codes
data['party'] = data['party'].cat.codes
data['incumbent'] = data['incumbent'].cat.codes
data['termstart'] = data['termstart'].cat.codes
print(data.head())

plt.figure()
parallel_coordinates(data, 'congress')
plt.show()