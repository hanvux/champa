import json
import pandas as pd

import plotly.express as px



# Malnutrition data
champa_music  = pd.read_csv("champa_s music.csv")

#Vietnam map
vietnam_geo = json.load(open("vietnam_state.geojson","r"))

# Plotting
fig = px.choropleth_mapbox(
    champa_music,
    locations = 'Code',
    featureidkey="properties.Code",
    geojson = vietnam_geo,
    color = 'Scale',
    color_continuous_scale=["#ffffff","#ffd700","#dc143c"],
    range_color=(0,12),
    hover_name = "Name",
    hover_data = {'Info':True,'Code':False},
    mapbox_style = "carto-positron",
    center = {"lat": 16,"lon": 106},
    zoom = 4.5,
    title = "Music Interference of Champa and Vietnam music based on regions",
)
fig.update_geos(fitbounds = "locations", visible=False)
fig.show()