import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
# from Number import phone_number
from opencage.geocoder import OpenCageGeocode

phone_number = input("To Track Enter Valid Phone Number Location with Country Code : ")
Key = "gd2b385k5a40c794f85c9f3927s22a31f8169dk"

check_phonenumber = phonenumbers.parse(phone_number)
print("Check Phone Number => ", check_phonenumber)
phonenumber_location = geocoder.description_for_number(check_phonenumber,"en")
print("Phonenumber Location => ", phonenumber_location)

country_code = phonenumbers.parse(phone_number)
print("Country name for Phone Number => ", geocoder.country_name_for_number(country_code, "en"))
print("Description for Phone number => ",geocoder.description_for_number(country_code, "en"))

service_provider = phonenumbers.parse(phone_number)
print("Service Provider Name => ", carrier.name_for_number(service_provider,"en"))

print("Name for valid number => ", carrier.name_for_valid_number(service_provider,"en"))

geocoder = OpenCageGeocode(Key)
query = str(phonenumber_location)
results = geocoder.geocode(query)
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print("Exact Phone Number Location (latitude) => ", latitude)
print("Exact Phone Number Location (longitude) => ", longitude)

### To get the exaction pointer on MAP
map_location = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=phonenumber_location).add_to(map_location)
map_location.save("currentlocation.html")