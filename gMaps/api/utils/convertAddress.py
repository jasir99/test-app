import math
import googlemaps
from .keys import getGoogleMapsApiKey

"""Make sure not to publish the API key in GitHub please!!!"""

gmaps = googlemaps.Client(key=getGoogleMapsApiKey())


def fullAddress(data):
    street = data['street']
    city = data['city']
    country = data['country']



    if data['street_number']:
        street_number = data['street_number']
        street = '{} {}'.format(street_number, street)


    if data['zip_code']:
        zip_code = data['zip_code']
        city = '{} {}'.format(zip_code, data['city'])


    if data['state']:
        state = data['state']
        country = '{}, {}'.format(state, country)

    if data['administrative']:
        administrative = data['administrative']
        country = '{}, {}'.format(administrative, country)

    return "{}, {}, {}".format(street, city, country)


def shortGeoCode(lat, lng):
    lat = int(lat)
    lng = int(lng)
    if float(lat) < 0:
        lat = 'n{}'.format(abs(lat))
    if float(lng) < 0:
        lng = 'n{}'.format(abs(lng))
    return '{}m{}'.format(lat, lng)


def reverseAddress(lat, lng):
    lat = float(lat)
    lng = float(lng)
    street_number = None
    street = ''
    city = None
    administrative_area_level_1 = None
    administrative_area_level_2 = None
    administrative_area_level_3 = None
    administrative_area_level_4 = None
    administrative_area_level_5 = None
    country = None
    zip_code = None

    geocode_result = gmaps.reverse_geocode((lat, lng))[0]
    for n in geocode_result['address_components']:
        if 'street_number' in n['types']:
            street_number = n['long_name']
            continue
        if 'route' in n['types']:
            street = n['long_name']
            continue
        if 'locality' in n['types'] or 'postal_town' in n['types'] or 'neighborhood' in n['types']:
            city = n['long_name']
            continue
        if 'administrative_area_level_1' in n['types']:
            administrative_area_level_1 = n['long_name']
            continue
        if 'administrative_area_level_2' in n['types'] and administrative != '':
            administrative_area_level_2 = n['long_name']
            continue
        if 'administrative_area_level_3' in n['types']:
            administrative_area_level_3 = n['long_name']
            continue
        if 'administrative_area_level_4' in n['types']:
            administrative_area_level_4 = n['long_name']
            continue
        if 'administrative_area_level_5' in n['types']:
            administrative_area_level_5 = n['long_name']
            continue
        if 'country' in n['types']:
            country = n['long_name']
            continue
        if 'postal_code' in n['types']:
            zip_code = n['long_name']
            continue

    if city is None:
        city = administrative
    data = {
        'street_number': street_number,
        'street': street,
        'city': city,
        'administrative_area_level_1': administrative_area_level_1,
        'administrative_area_level_2': administrative_area_level_2,
        'administrative_area_level_3': administrative_area_level_3,
        'administrative_area_level_4': administrative_area_level_4,
        'administrative_area_level_5': administrative_area_level_5,
        'country': country,
        'zip_code': zip_code,
        'full_address': geocode_result['formatted_address'],
        'lattitude': lat,
        'longitude': lng,
        'latLong': shortGeoCode(lat, lng)
    }
    return data



