from django.contrib import admin

from car.models import Car, Color, Model, Brand, Picture, Property


class CarAdmin(admin.ModelAdmin):
    list_display = ('dealer', 'model', 'price', 'status')


admin.site.register(Car, CarAdmin)
admin.site.register(Color)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Picture)
admin.site.register(Property)
