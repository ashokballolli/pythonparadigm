import folium
import pandas
# Reading co-ordinates from external file

data = pandas.read_csv("Volcanoes.txt")
lats = list(data["LAT"])  # converst series to list
lons = list(data["LON"])
location = list(data["LOCATION"])

map = folium.Map(location=[lats[int(len(lats)/2)], lons[int(len(lons)/2)]], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lat, lon, loc in zip(lats, lons, location):
    fg.add_child(folium.Marker(location=[lat, lon], popup="point: " + str(lat) + "," + str(lon), tooltip=loc,
                               icon=folium.Icon(color="orange")))

#     popup - for the string which has ' leads to blank webpage, to avoid this write popup like below
#     popup=folium.Popup("message", parse_html=True)

map.add_child(fg)
map.save("map02.html")
