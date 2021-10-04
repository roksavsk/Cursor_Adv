from tests.conftest import client
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "c376a81f73mshb9a443574833ecdp1bc627jsnc4245b06df70"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"cities": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_search_weather_mock(client, mocker):
    mocker.patch('requests.requests', side_effect=ApiMock)
    response = client.post("/search", data={"cities": "dnipro"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Dnipro" in response.data


class ApiMock:
    def __init__(self, *args, **kwargs):
        self.data_ = {'message': 'accurate', 'cod': '200', 'count': 1, 'list': [
            {'id': 709930, 'name': 'Dnipro', 'coord': {"lon": 48.45, "lat": 34.9833},
             'main': {'temp': 23.85, 'feels_like': 23.85, 'temp_min': 23.85, 'temp_max': 23.85, 'pressure': 1010,
                      'humidity': 57}, 'dt': 1623499747, 'wind': {'speed': 4, 'deg': 240}, 'sys': {'country': 'UA'},
             'rain': None, 'snow': None, 'clouds': {'all': 75},
             'weather': [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}]}]}
        self.status_code = 200

    def json(self):
        return self.data_
