import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# The Basemap

# html = """<h4>Volcano information:</h4>
# Height: %s m
# """


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
# coordinates = [[-25.7488121,28.1966848],[-26.7488121,27]]
for lt, ln, el in zip(lat, lon, elev):
    # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # fg.add_child(folium.Marker(location=[lt,ln],popup=iframe,icon=folium.Icon(color='green')))
    # fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+'m' ,icon=folium.Icon(color= color_producer(el))))
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+'m', fill_color=color_producer(el), color='grey', fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read()))
map.add_child(fg)
map.save("Map1.htm")
