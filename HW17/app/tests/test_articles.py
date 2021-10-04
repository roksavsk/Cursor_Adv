from tests.conftest import client


def test_delete_article(client):
    response = client.delete("api/articles/1")
    assert response.status_code == 204
    response = client.get("api/articles/1")
    assert response.status_code == 404


def test_article_create(client):
    response = client.get('/article/create')
    data = response.json
    assert response.status_code == 200
    headers = {
        "Content-Type": "application/json"
    }

    json = {
        "title": "Test article",
        "img": "https://www.onlinekittencare.com/wp-content/uploads/2020/07/vChK6pTy3vN3KbYZ7UU7k3-1200-80.jpg",
        "short_description": "bla bla bla",
        "description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla",
        "slug": "test-article",
        "author_id": "-1"
    }
    response = client.post("/article/store", headers=headers, json=json)
    assert response.status_code == 500