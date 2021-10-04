import os


class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    WEATHER_API_URL = os.environ.get("WEATHER_API_URL")
    WEATHER_API_HOST = os.environ.get("WEATHER_API_HOST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOAD_PATH = 'static/uploads/'
    BLOG_TITLE = "Blog Cursor"
    MENU_ITEMS = [
        {
            "name": "Articles",
            "link": "/articles",
        },
        {
            "name": "Categories",
            "link": "/categories",
        },
    ]
    FOOTER_LINKS = [
        {
            "name": "Home",
            "link": "/"
        },
        {
            "name": "Articles",
            "link": "/articles",
        },
        {
            "name": "Categories",
            "link": "/categories",
        },
        {
            "name": "Contacts",
            "link": "/contacts",
        },
        {
            "name": "Our Team",
            "link": "/team",
        },
        {
            "name": "Help",
            "link": "/help",
        },

    ]


def articles():
    return [
        {
            "title": "Test Article",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article'
        },
        {
            "title": "Test Article2",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article2'
        },
    ]
