from django.db import models


class Restaurant(models.Model):
    STATUS_OPEN = 'open'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_CLOSED, 'Closed'),
    )

    name = models.CharField(max_length=75)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_OPEN, blank=True)
    workers = models.ManyToManyField('restaurant.Worker')
    menu = models.ManyToManyField('restaurant.Menu')
    city = models.ForeignKey('restaurant.City', on_delete=models.CASCADE)
    country = models.ForeignKey('restaurant.Country', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name


class Worker(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return self.title


class Dish(models.Model):
    name = models.CharField(max_length=75)
    ingredients = models.TextField()
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name


class Menu(models.Model):

    SEASON_SPRING = 'Spring'
    SEASON_SUMMER = 'Summer'
    SEASON_AUTUMN = 'Autumn'
    SEASON_WINTER = 'Winter'

    SEASON_CHOICES = (
        (SEASON_SPRING, 'Spring'),
        (SEASON_SUMMER, 'Summer'),
        (SEASON_AUTUMN, 'Autumn'),
        (SEASON_WINTER, 'Winter'),
    )

    name = models.CharField(max_length=75)
    dishes = models.ManyToManyField(Dish)
    season = models.CharField(max_length=15, choices=SEASON_CHOICES, default=SEASON_SPRING, blank=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
