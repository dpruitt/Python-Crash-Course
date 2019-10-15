import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = './data/eq_data_30_day_m1.json'
with open(filename) as file:
    all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']

magnitudes, longitudes, latitudes, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    magnitude = eq_dict['properties']['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    hover_text = eq_dict['properties']['title']
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    hover_texts.append(hover_text)

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_texts,
    'marker': {
        'size': [5 * magnitude for magnitude in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')