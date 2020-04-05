import folium

map = folium.Map(location=[16.9167268, 76.2280781], zoom_start=8, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for coordinate in [[16.917403, 76.237219], [16.7326328,76.1951765], [16.5326328,76.1551765]]:
    fg.add_child(folium.Marker(location=coordinate, popup="point: " + str(coordinate), tooltip="tootl tip",
                               icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("map0101.html")
