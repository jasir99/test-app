import math
import googlemaps
from .keys import getGoogleMapsApiKey
"""Make sure not to publish the API key in GitHub please!!!"""

gmaps = googlemaps.Client(key=getGoogleMapsApiKey())

def fullAddress(data):
    street = city = country = ''


    if 'street' in data:
        street = data['street']
    if 'street_number' in data:
        street_number = data['street_number']
        street = '{} {}'.format(street_number, street)
    if 'city' in data:
        city = data['city']
    if 'zip_code' in data:
        zip_code = data['zip_code']
        city = '{} {}'.format(zip_code, city)
    if 'country' in data:
        country = data['country']
    if 'state' in data:
        state = data['state']
        country = '{}, {}'.format(state, country)

    return "{}, {}, {}".format(street, city, country)

def geocodeAddress(address):
    geocode_result = gmaps.geocode(address)[0]['geometry']['location']
    lat = geocode_result['lat']
    lng = geocode_result['lng']
    return lat, lng, '{}{}'.format(int(lat), int(lng))

