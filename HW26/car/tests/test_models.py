from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from car.tests.factories import ColorFactory, BrandFactory, ModelFactory, PropertyFactory, PictureFactory
from car.models import Car, Color, Model, Brand, Picture, Property
from dealer.tests.factories import DealerFactory


class TestCarModel(TestCase):
    def setUp(self) -> None:
        self.dealer = DealerFactory()
        self.picture = PictureFactory()
        self.color = ColorFactory()
        self.model = ModelFactory()
        self.property = PropertyFactory()

    def test_model(self):
        car = Car.objects.create(
            number='AA 1234 AA',
            slug='porsche_1234',
            engine_power=500,
            price=100000,
            capacity=4,
            dealer=self.dealer,
            picture=self.picture,
            color=self.color,
            model=self.model,
        )
        car.property.add(self.property)

        self.assertIsNotNone(car.id)
        self.assertEqual(str(car), 'porsche_1234')
        self.assertEqual(car.number, 'AA 1234 AA')
        self.assertEqual(car.engine_power, 500)
        self.assertEqual(car.price, 100000)
        self.assertEqual(car.capacity, 4)
        self.assertEqual(car.doors, 4)
        self.assertEqual(car.sitting_place, 4)
        self.assertEqual(car.engine_type, Car.ENGINE_GASOLINE)
        self.assertEqual(car.fuel_type, Car.FUEL_GASOLINE)
        self.assertEqual(car.pollutant_type, Car.POLLUTANT_A)
        self.assertEqual(car.status, Car.STATUS_PENDING)
        self.assertEqual(car.gear_case, Car.GEAR_AUTOMATIC)


class TestPictureModel(TestCase):
    def test_model(self):
        picture = Picture.objects.create(
            position=10,
            metadata='some test metadata',
            url=SimpleUploadedFile(
                name='test.jpg',
                content=open('pictures/test.jpg', 'rb').read(),
                content_type='image/jpeg'
            )
        )

        self.assertIsNotNone(picture.id)
        self.assertIsNotNone(picture.url)
        self.assertEqual(picture.position, 10)
        self.assertEqual(picture.metadata, 'some test metadata')


class TestColorModel(TestCase):
    def test_model(self):
        color = Color.objects.create(
            name='Blue',
        )

        self.assertIsNotNone(color.id)
        self.assertEqual(str(color), 'Blue')


class TestModelOfCarModel(TestCase):
    def setUp(self) -> None:
        self.brand = BrandFactory()

    def test_model(self):
        model = Model.objects.create(
            name='Taycan',
            brand=self.brand,
        )

        self.assertIsNotNone(model.id)
        self.assertEqual(str(model), 'Taycan')


class TestBrandModel(TestCase):
    def test_model(self):
        brand = Brand.objects.create(
            name='Porsche',
        )

        self.assertIsNotNone(brand.id)
        self.assertEqual(str(brand), 'Porsche')


class TestPropertyModel(TestCase):
    def test_model(self):
        property = Property.objects.create(
            name='City car',
        )

        self.assertIsNotNone(property.id)
        self.assertEqual(str(property), 'City car')
        self.assertEqual(property.category, Property.CATEGORY_A)
