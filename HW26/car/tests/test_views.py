from django.test import TestCase

from car.tests.factories import CarFactory


class CarsListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = CarFactory()
        cls.url = f'/car/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class CarsDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = CarFactory()
        cls.url = f'/car/{cls.car.slug}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.number)

    def test_not_found(self):
        response = self.client.get('/car/wrong-slug/')
        self.assertEqual(response.status_code, 404)
