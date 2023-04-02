import folium
import requests as requests

def filter(lat, lon, place, titolare):
    infos = place + ' - ' + "Titolare: " + titolare
    if titolare == "A2A Energy Solutions":
        folium.Marker(location=[lat, lon], popup=infos, icon=folium.Icon(color="green")).add_to(map)
    elif titolare == 'BeCharge':
        folium.Marker(location=[lat, lon], popup=infos, icon=folium.Icon(color="red")).add_to(map)
    elif titolare == 'ENEL X Mobility':
        folium.Marker(location=[lat, lon], popup=infos, icon=folium.Icon(color="blue")).add_to(map)
    elif titolare == "PowerPoint City Car":
        folium.Marker(location=[lat, lon], popup=infos, icon=folium.Icon(color="purple")).add_to(map)


map = folium.Map(location= [45.4636707, 9.1881263], zoom_start= 12)

r = requests.get("https://dati.comune.milano.it/dataset/0c7a321d-6055-4eed-bfb0-9bd2a8dabf88/resource/34ec2509-ee4e-491a-a1e4-839c1b68402f/download/ricarica_colonnine.geojson")

data = r.json()

feat = data['features']
for x in feat:
    titolare = x['properties'] ['titolare']
    place = x['properties'] ['localita']
    lat = x['geometry'] ['coordinates'] [1]
    lon = x['geometry'] ['coordinates'] [0]
    filter(lat, lon, place, titolare)

map.show_in_browser()