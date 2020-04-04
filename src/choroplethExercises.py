# import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from chart_studio import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("..\\files\\2014_World_Power_Consumption")
print(df.head())

data = dict(type="choropleth", locations=df["Country"], locationmode="country names",
            z=df["Power Consumption KWH"], text=df["Text"], colorbar={"title":"Power Consumption KWH"})

layout=dict(title="2014_World_Power_Consumption", geo=dict(projection={"type":"mercator"}))

choromap = go.Figure(data=[data], layout=layout)
# iplot(choromap, validate=False)


df = pd.read_csv("..\\files\\2012_Election_Data")
print(df.head())


data = dict(type="choropleth", colorscale="Viridis", reversescale=True, locationmode="USA-states",
            locations=df["State Abv"], z=df["Voting-Age Population (VAP)"], text=df["State"],
            colorbar={"title": "Voting-Age Population (VAP)"})
layout = dict(title="2012_Election_Data", geo=dict(scope="usa"))

choromap = go.Figure(data=[data], layout=layout)
iplot(choromap, validate=False)

