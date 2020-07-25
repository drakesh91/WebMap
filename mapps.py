import folium
map=folium.Map(location=[46.87,-102.78], zoom_start=4, tiles="Stamen Terrain")
folium.Marker(location=[30.1290,77.2674],popup="Yamunanagar",tooltip="Click for more information",icon=folium.Icon(icon="cloud")).add_to(map)
splocation=[40.72829,-73.84]
spicon=folium.features.CustomIcon(r"C:\Users\gaurav\Downloads\python\workspace\project 2\spiderman.png",icon_size=(50,50))
sppopup="<strong>SpiderMan</strong><br>Real Name: Peter parker<br>City of Birth: Queensland"
folium.Marker(location=splocation,popup=sppopup,tooltip="Click for more information",icon=spicon).add_to(map)


map.save("map4.html")
