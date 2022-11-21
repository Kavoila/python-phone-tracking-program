import geocoder
import folium
g = geocoder.ip("197.156.137.171")
My_address = g.latlng
print(My_address)

myLocation = folium.Map(location=My_address, zoom_start= 12)
folium.CircleMarker(location= My_address,
                    radius= 50,
                    popup =" Kenya").add_to(myLocation)
folium.Marker(My_address,
              popup="Kenya").add_to(myLocation)
myLocation.save("location.html")
