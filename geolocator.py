from turtle import color
import geocoder
import folium
import ipaddress

print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-= GEOCODER =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def ip_check(ip):
    try:
        ip_validity = ipaddress.ip_address(ip)
        print(f"\n{ip} is a valid IP address. Following are the location details :-\n")
    except ValueError:
        print(f"\n{ip} is not a valid IP address")
        exit()

ip_string = input("\nPlease enter an IP address : ")
ip_check(ip_string)
ip_assign = geocoder.ip(ip_string)
print(f"\nCity : {ip_assign.city}\nCoordinates : {ip_assign.latlng}")

print("\nFor further reference of the exact location, a map has been provided as an HTML file")

ip_map = folium.Map(location = ip_assign.latlng)
folium.CircleMarker(location = ip_assign.latlng, color = "Green", radius = 40).add_to(ip_map)
folium.Marker(ip_assign.latlng).add_to(ip_map)

ip_map.save("Python_Microproject.html")
