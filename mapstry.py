import pandas
import folium
map=folium.Map(location=[46.87,-102.78], zoom_start=4)
df=pandas.read_csv("volcanoes.txt")
lat=list(df.LAT)
lon=list(df.LON)
n=len(lat)
for i in range(n):
    folium.Marker(location=[lat[i],lon[i]],tooltip="Click for more Information",popup="US",icon=folium.Icon(color="red")).add_to(map)
map.save("formaps.html")    
