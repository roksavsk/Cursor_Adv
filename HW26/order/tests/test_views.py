from django.test import TestCase

from order.tests.factories import OrderFactory


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = OrderFactory()
        cls.url = f'/order/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class DealersDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.order = OrderFactory()
        cls.url = f'/order/{cls.order.id}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.email)

    def test_not_found(self):
        response = self.client.get('/dealer/698589134/')
        self.assertEqual(response.status_code, 404)
