import factory
from factory import fuzzy
from django.contrib.auth.models import User


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.Country'

    name = fuzzy.FuzzyText(length=16)


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.City'

    name = fuzzy.FuzzyText(length=16)
    country = factory.SubFactory(CountryFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.Dealer'

    title = factory.Sequence(lambda n: f'dealer_{n}')
    email = factory.Sequence(lambda n: f'test_email_{n}@mail.com')
    user = factory.SubFactory(UserFactory)
    city = factory.SubFactory(CityFactory)
