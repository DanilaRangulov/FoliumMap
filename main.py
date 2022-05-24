import folium
import pandas as pd
import json
from folium.plugins import Search


# Required data files
geojson = json.load(open('countries.json'))
data = pd.read_csv('2019.csv')
# Create map
m = folium.Map(location=[63.391522, 96.328125], zoom_start=3)
# Creating a layer based on data from a .csv file
rel_ = folium.Choropleth(
    geo_data=geojson,
    data=data,
    columns=['Country or region', 'Score'],
    key_on='properties.name',
    bins=8,
    fill_color='YlGn',
    nan_fill_color='darkblue',
    nan_fill_opacity=0.5,
    fill_opacity=0.7,
    line_opacity=0,
    legend_name='Happiness level',
    highlight=True,
    show=False,
)
# Adding a search button by country name
style_one = lambda x: {'fillColor': '#ff1111'}
geojson_obj = folium.GeoJson(geojson, style_function=style_one).add_to(m)

StateSearch = Search(layer=geojson_obj,
                     geom_type='Point',
                     placeholder="Search",
                     collapsed=True,
                     search_label='name',
                     search_zoom=5,
                     position='topright').add_to(m)
rel_.add_to(m)
# Save map
m.save("map.html")
