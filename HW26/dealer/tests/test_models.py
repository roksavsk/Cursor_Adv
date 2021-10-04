from django.test import TestCase

from dealer.tests.factories import UserFactory, CityFactory, CountryFactory
from dealer.models import Dealer, City, Country


class TestDealerModel(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.city = CityFactory()

    def test_model(self):
        dealer = Dealer.objects.create(
            title='Victoria De Angelis',
            email='test_email@gmail.com',
            user=self.user,
            city=self.city,
        )

        self.assertIsNotNone(dealer.id)
        self.assertEqual(str(dealer), 'Victoria De Angelis')
        self.assertEqual(dealer.email, 'test_email@gmail.com')


class TestCityModel(TestCase):
    def setUp(self) -> None:
        self.country = CountryFactory()

    def test_model(self):
        city = City.objects.create(
            name='Venezia',
            country=self.country,
        )

        self.assertIsNotNone(city.id)
        self.assertEqual(str(city), 'Venezia')


class TestCountryModel(TestCase):
    def test_model(self):
        country = Country.objects.create(
            name='Italy',
            code='39',
        )

        self.assertIsNotNone(country.id)
        self.assertEqual(str(country), 'Italy')
        self.assertEqual(country.code, '39')
