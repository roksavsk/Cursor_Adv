from django.contrib import admin

from newsletter.models import NewsLetter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(NewsLetter, NewsLetterAdmin)
