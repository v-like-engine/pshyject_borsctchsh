import requests


def get_toponym(search):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": search,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        raise RuntimeError('Error on sending Geocode Request')

    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]


def get_spn(toponym):
    lowerCorner = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    upperCorner = toponym['boundedBy']['Envelope']['upperCorner'].split()
    width = abs(float(upperCorner[0]) - float(lowerCorner[0]))
    height = abs(float(upperCorner[1]) - float(lowerCorner[1]))
    return str(max(width, height) / 2)


def get_coordinates(toponym):
    return toponym["Point"]["pos"].split()
