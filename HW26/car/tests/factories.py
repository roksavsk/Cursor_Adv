import factory
from factory import fuzzy

from dealer.tests.factories import DealerFactory


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Color'

    name = factory.Sequence(lambda n: f'color_{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Brand'

    name = factory.Sequence(lambda n: f'brand_{n}')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Model'

    name = factory.Sequence(lambda n: f'model_{n}')
    brand = factory.SubFactory(BrandFactory)


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Property'

    name = factory.Sequence(lambda n: f'property_{n}')


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Picture'

    position = fuzzy.FuzzyInteger(0, 100)
    metadata = fuzzy.FuzzyText(length=255)
    url = factory.django.ImageField(from_path='pictures/test.jpg')


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'car.Car'

    number = 'AA 1234 AA'
    slug = factory.Sequence(lambda n: f'slug_{n}')
    engine_power = fuzzy.FuzzyInteger(50, 200)
    dealer = factory.SubFactory(DealerFactory)
    picture = factory.SubFactory(PictureFactory)
    color = factory.SubFactory(ColorFactory)
    model = factory.SubFactory(ModelFactory)
