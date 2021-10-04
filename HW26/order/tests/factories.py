import factory

from car.tests.factories import CarFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.Order'

    first_name = factory.Sequence(lambda n: f'first_name_{n}')
    last_name = factory.Sequence(lambda n: f'last_name_{n}')
    email = factory.Sequence(lambda n: f'test_email_{n}@mail.com')
    phone = '+12345678901'
    car = factory.SubFactory(CarFactory)
