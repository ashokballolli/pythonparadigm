import folium as fl

map = fl.Map(location=[16.9167268,76.2280781], zoom_start=10, tiles="Stamen Terrain")
map.add_child(fl.Marker(location=[16.917403, 76.237219], popup="le na Sindagige bandini", tooltip="mangya", icon=fl.Icon(color="green")))
map.save("map02.html")
