from django.contrib import admin

from restaurant.models import Restaurant, Worker, Dish, Menu, Country, City

admin.site.register(Restaurant)
admin.site.register(Worker)
admin.site.register(Dish)
admin.site.register(Menu)
admin.site.register(Country)
admin.site.register(City)
