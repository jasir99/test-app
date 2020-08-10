import googlemaps

"""Make sure not to publish the API key in GitHub please!!!"""

gmaps = googlemaps.Client(key='Write the key here')


def geocodeAddress(address):
    geocode_result = gmaps.geocode('Balindolska, Gostivar, Macedonia')
    return geocode_result[0]['geometry']['location']

