"""
Drawing a folium map with drawing options and json export, using folium with 'Stamen Terrain', 
openstreetmap, esri satellite, 

"""


import folium
from folium.plugins import Draw

# define map center, ~ center of bavaria
y_center = 49
x_center = 11


# define polygon style
style = {'fillColor': '#ffffffff', 'color': '#000000'}


# open map 'm' with defined center and zomm level
m = folium.Map([y_center,x_center], zoom_start=7)#, tiles='Stamen Terrain')

# load esris satellite map
folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True
       ).add_to(m)

# add geojson
folium.GeoJson(gdf.to_json(), style_function=lambda x: style).add_to(m)

# load openstreet map
folium.TileLayer('openstreetmap').add_to(m)

# load terrain map
folium.TileLayer('Stamen Terrain').add_to(m)

# add lat/lon popup after click on maps
folium.LatLngPopup().add_to(m)

#
#folium.ClickForMarker().add_to(m)
# open layer control in upper right corner of the map
folium.LayerControl().add_to(m)
# draw plugin
Draw(
    export=True,
    filename='my_data.geojson',
    position='topleft',
    draw_options={'polyline': {'allowIntersection': False}},
    edit_options={'poly': {'allowIntersection': False}}
).add_to(m)
