from django.db import models


class Car(models.Model):
    color = models.ForeignKey('car.Color', on_delete=models.CASCADE)
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE, related_name='cars')
    model = models.ForeignKey('car.Model', on_delete=models.SET_NULL, null=True, related_name='cars')

    ENGINE_GASOLINE = 'Gasoline'
    ENGINE_DIESEL = 'Diesel'
    ENGINE_ROTARY = 'Rotary'
    ENGINE_HYBRID = 'Hybrid'
    ENGINE_ELECTRIC = 'Electric'

    ENGINE_CHOICES = (
        (ENGINE_GASOLINE, 'Gasoline'),
        (ENGINE_DIESEL, 'Diesel'),
        (ENGINE_ROTARY, 'Rotary'),
        (ENGINE_HYBRID, 'Hybrid'),
        (ENGINE_ELECTRIC, 'Electric'),
    )

    engine_type = models.CharField(
        max_length=55,
        choices=ENGINE_CHOICES,
        default=ENGINE_GASOLINE,
        blank=True
    )

    POLLUTANT_A = 'A'
    POLLUTANT_A2 = 'A+'
    POLLUTANT_B = 'B'
    POLLUTANT_C = 'C'
    POLLUTANT_D = 'D'
    POLLUTANT_E = 'E'
    POLLUTANT_F = 'F'
    POLLUTANT_G = 'G'

    POLLUTANT_CHOICES = (
        (POLLUTANT_A, 'A'),
        (POLLUTANT_A2, 'A+'),
        (POLLUTANT_B, 'B'),
        (POLLUTANT_C, 'C'),
        (POLLUTANT_D, 'D'),
        (POLLUTANT_E, 'E'),
        (POLLUTANT_F, 'F'),
        (POLLUTANT_G, 'G'),
    )

    pollutant_type = models.CharField(
        max_length=55,
        choices=POLLUTANT_CHOICES,
        default=POLLUTANT_A,
        blank=True
    )

    price = models.PositiveIntegerField(default=0)

    FUEL_GASOLINE = 'Gasoline'
    FUEL_GAS = 'Gasoline/Gas'
    FUEL_HYBRID = 'Hybrid'
    FUEL_DIESEL = 'Diesel'
    FUEL_ELECTRIC = 'Electric'

    FUEL_CHOICES = (
        (FUEL_GASOLINE, 'Gasoline'),
        (FUEL_GAS, 'Gasoline/Gas'),
        (FUEL_HYBRID, 'Hybrid'),
        (FUEL_DIESEL, 'Diesel'),
        (FUEL_ELECTRIC, 'Electric'),
    )
    fuel_type = models.CharField(
        max_length=55,
        choices=FUEL_CHOICES,
        default=FUEL_GASOLINE,
        blank=True
    )

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
        max_length=55,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    doors = models.PositiveSmallIntegerField(default=4)
    capacity = models.PositiveIntegerField(default=4)

    GEAR_AUTOMATIC = 'Automatic'
    GEAR_SEMI = 'Semi-automatic'
    GEAR_MECHANICAL = 'Mechanical'
    GEAR_ROBOTIC = 'Robotic'

    GEAR_CHOICES = (
        (GEAR_AUTOMATIC, 'Automatic'),
        (GEAR_SEMI, 'Semi-automatic'),
        (GEAR_MECHANICAL, 'Mechanical'),
        (GEAR_ROBOTIC, 'Robotic'),
    )

    gear_case = models.CharField(
        max_length=55,
        choices=GEAR_CHOICES,
        default=GEAR_AUTOMATIC,
        blank=True
    )
    number = models.CharField(max_length=15)
    slug = models.SlugField(max_length=75)
    sitting_place = models.PositiveSmallIntegerField(default=4)
    first_registration_date = models.DateTimeField(auto_now_add=True)
    engine_power = models.PositiveIntegerField()
    picture = models.ForeignKey('car.Picture', on_delete=models.CASCADE, null=True, blank=True)
    property = models.ManyToManyField('car.Property')

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
    brand = models.ForeignKey('car.Brand', on_delete=models.CASCADE, related_name='models')
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
        return self.url.name

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
