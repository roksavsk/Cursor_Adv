from django.test import TestCase

from car.tests.factories import CarFactory
from order.models import Order


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Dana',
            last_name='Scully',
            email='test@gmail.com',
            phone='+12345678901',
            message='text message',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Dana Scully')
        self.assertEqual(order.email, 'test@gmail.com')
        self.assertEqual(order.phone, '+12345678901')
        self.assertEqual(order.message, 'text message')
