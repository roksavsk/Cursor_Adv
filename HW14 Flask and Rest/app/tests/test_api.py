from tests.conftest import client, todos
import json
from config import Config


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_list(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_update(client):
    update_data = {
        "text": "blablabla"
    }

    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json['1'] == "blablabla"


def test_delete(client):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    response = client.get("/todos/1")
    assert response.status_code == 404


def test_weather(client):
    Config.WEATHER_API_KEY = "c376a81f73mshb9a443574833ecdp1bc627jsnc4245b06df70"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.get('/weather?city=London')
    assert response.status_code == 200
    response = client.get('/weather?city=Lviv,London')
    assert response.status_code == 200
    response = client.get('/weather?city=L')
    assert response.status_code == 404
