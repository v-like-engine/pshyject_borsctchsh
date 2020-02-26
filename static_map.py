import requests


def get_map(params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    if not response:
        raise RuntimeError('Eror on requesting static map')

    return response.content