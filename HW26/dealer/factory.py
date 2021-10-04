import factory


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.Dealer'

    title = 'Ukrainian Car Dealer'
    email = 'test@mail.com'
    city_id = 1
    user_id = 1


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.Country'

    name = 'Ukraine'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.City'

    name = 'Dnipro'

