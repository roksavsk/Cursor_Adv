from django.db import models
from django.contrib.auth import get_user_model

AUTH_USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(max_length=75, null=True)
    email = models.EmailField(max_length=75, unique=True, null=True)
    city = models.ForeignKey('dealer.City', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey('dealer.Country', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Country(models.Model):
    name = models.CharField(max_length=75, unique=True)
    code = models.CharField(blank=True, max_length=7, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class NewsLetter(models.Model):
    email = models.EmailField(max_length=75)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letters'
