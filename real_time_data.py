from geopy.geocoders import Nominatim
import requests
import json

geolocator = Nominatim(user_agent="forestfireapp")


def fetch_data(loc="Kaziranga National Park"):
    location = geolocator.geocode({loc}) #Plug User Input Here
    res = requests.get(f'https://api.darksky.net/forecast/1c9424849fc849dc22a73f5c96032111/{location.latitude},{location.longitude}')
    json_data = json.loads(res.text)

    # temp = json_data['currently']['temperature']
    # humidity = json_data['currently']['humidity']
    # wind_vel = json_data['currently']['windSpeed']

    return json_data['currently'].items()

# ---------------Print All Real-Time Data--------------#
# for key,value in json_data['currently'].items():
#     print(key,' -> ',value)
