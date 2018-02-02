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
    data_file = pd.read_csv("Dataset/congress-terms.csv")

    data = [
        go.Parcoords(
            line = dict(color = data_file['state'],
                       colorscale = [[0,'#FFFFFF'],[0.5,'#FFFFFF'],[1,'#FFFFFF']]),

            dimensions = list([
                dict(range=[45, 62], label = 'Age', values = data_file['age']),
                dict(range=[75, 115], label = 'Congress', values = data_file['congress']),
            ])
        )
    ]

    layout = go.Layout(
        paper_bgcolor = '#FFFFFF',
        plot_bgcolor = '#000000'
    )

    fig = go.Figure(data = data, layout = layout)
    py.iplot(fig, filename = 'base')

data_file = pd.read_csv('Dataset/congress-terms.csv')
data_file = data_file.drop(['bioguide', 'firstname', 'lastname', 'middlename', 'suffix', 'birthday'], axis =1)

data_file['congress'] = data_file['congress'].astype('category')
data_file['chamber'] = data_file['chamber'].astype('category')
data_file['state'] = data_file['state'].astype('category')
data_file['party'] = data_file['party'].astype('category')
data_file['incumbent'] = data_file['incumbent'].astype('category')
data_file['termstart'] = data_file['termstart'].astype('category')
data = data_file.sample(n = 10)
print(data.head())
data['congress'] = data['congress'].cat.codes
data['chamber'] = data['chamber'].cat.codes
data['state'] = data['state'].cat.codes
data['party'] = data['party'].cat.codes
data['incumbent'] = data['incumbent'].cat.codes
data['termstart'] = data['termstart'].cat.codes
print(data.head())

plt.figure()
parallel_coordinates(data, 'incumbent')
plt.title("Parallel Coordinates plotting to visualize the dataset")
plt.show()