from django.db import models


class Car(models.Model):
    color = models.ForeignKey('car.Color', on_delete=models.CASCADE)
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE)
    model = models.ForeignKey('car.Model', on_delete=models.SET_NULL, null=True)
    engine_type = models.CharField(max_length=75)
    population_type = models.CharField(max_length=75)
    price = models.PositiveIntegerField(default=0)
    fuel_type = models.CharField(max_length=75)

    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending Car Sell"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    doors = models.PositiveSmallIntegerField(default=4)
    capacity = models.PositiveIntegerField()
    gear_case = models.CharField(max_length=75)
    number = models.CharField(max_length=15)
    slug = models.SlugField(max_length=75)
    sitting_place = models.PositiveSmallIntegerField(default=4)
    first_registration_date = models.DateTimeField(auto_now_add=True)
    engine_power = models.PositiveIntegerField()
    picture = models.ForeignKey('car.Picture', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Color(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Model(models.Model):
    brand = models.ForeignKey('car.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Brand(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Picture(models.Model):
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )
    position = models.IntegerField()
    metadata = models.TextField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class Property(models.Model):

    CATEGORY_A = 'City car'
    CATEGORY_B = 'Supermini'
    CATEGORY_C = 'Small'
    CATEGORY_D = 'Large'
    CATEGORY_E = 'Executive'
    CATEGORY_F = 'Luxury'

    CATEGORY_CHOICES = (
        (CATEGORY_A, 'City car'),
        (CATEGORY_B, 'Supermini'),
        (CATEGORY_C, 'Small'),
        (CATEGORY_D, 'Large'),
        (CATEGORY_E, 'Executive'),
        (CATEGORY_F, 'Luxury'),
    )

    name = models.CharField(max_length=75)
    category = models.CharField(
        max_length=55,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_A,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
