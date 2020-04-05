import folium
import pandas

# population based map
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg_v = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg_v.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup=str(el) + " m",
        fill_color=color_producer(el),
        color='grey',
        fill_opacity=0.7
    ))
map.add_child(fg_v)

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(
    data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties'][
            'POP2005'] < 2000000 else 'red'}
)
)

map.add_child(fg_p)

map.add_child(folium.
              LayerControl()) # should be after adding the future group otherwise other layers disappears
map.save("map06layerControlPanel.html")
