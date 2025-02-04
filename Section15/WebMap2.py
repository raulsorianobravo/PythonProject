import folium

map = folium.Map(location=[42.95501359560747, -7.946965705281243] , zoom_start=10, tiles='OpenStreetMap.Mapnik')

fg=folium.FeatureGroup(name="Mapa")

# map.add_child(folium.Marker(location=[43.32486212802953, -8.402614002382292],popup="1", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[43.32486212802953, -8.402614002382292],popup="1", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("./Section15/Map2.html")