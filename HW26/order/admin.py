from django.contrib import admin

from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status')


admin.site.register(Order, OrderAdmin)

