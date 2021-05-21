import pandas
import folium

from geopy import Nominatim

df = pandas.read_csv('orase.csv')


locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("cluj")
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

m = folium.Map(location=[45.7583255,21.2346139],tiles='OpenStreetMap', zoom_start=10)

folium.Marker(location=[location.latitude,location.longitude],popup='TEXT',icon = folium.Icon(color='blue')).add_to(m)




for i in range (500,len(df['Orase'])):
    try:
        location = locator.geocode(df['Orase'][i])
        folium.Marker(location=[location.latitude, location.longitude], popup='Vreme',icon=folium.Icon(color='blue')).add_to(m)
    except AttributeError:
        print(df['Orase'][i])


m.save('index.html')

