import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.Order'

    first_name = 'Oksana'
    last_name = 'Vaskovska'
    email = 'test@gmail.com'
    phone = '+380123456789'
    car_id = 1