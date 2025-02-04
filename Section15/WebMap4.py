import folium
import pandas

fg=folium.FeatureGroup(name="Mapa")
fg2=folium.FeatureGroup(name="Mapa2")
fg3=folium.FeatureGroup(name="Mapa3")

data = pandas.read_csv("./Section15/Webmap_datasources/Volcanoes.txt")

lat=list(data["LAT"])
lon=list(data["LON"])
elev= list(data["ELEV"])

for lt,ln,el in zip(lat,lon,elev):
    fg3.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(el) +"meters",parse_html=True), icon=folium.Icon(color="red")))


map = folium.Map(location=[42.95501359560747, -7.946965705281243] , zoom_start=10, tiles='OpenStreetMap.Mapnik')

# map.add_child(folium.Marker(location=[43.32486212802953, -8.402614002382292],popup="1", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[43.32486212802953, -8.402614002382292],popup="1", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[43.323226212802953, -8.4026140442382292],popup="1", icon=folium.Icon(color="green")))

for coordinates in [[43.3244212802953, -8.45026140482292], [43.324446212802953, -8.43261406682292]]:
    fg2.add_child(folium.Marker(location=coordinates,popup="2", icon=folium.Icon(color="blue")))

map.add_child(fg)
map.add_child(fg2)
map.add_child(fg3)
map.save("./Section15/Map2.html")