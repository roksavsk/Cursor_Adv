import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Car'

    color_id = 1
    dealer_id = 1
    model_id = 1
    picture_id = 1
    number = 'AE 1234 AE'
    slug = 'ford-f_150'
    engine_power = 80


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Color'

    name = 'Blue'


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Model'

    name = 'pickup'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Brand'

    name = 'Ford'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Property'

    name = 'Small car'
