from django.contrib import admin

from dealer.models import Dealer, City, Country


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')


admin.site.register(Dealer, DealerAdmin)
admin.site.register(City)
admin.site.register(Country)
