from django.test import TestCase

from newsletter.models import NewsLetter


class TestNewsLetterModel(TestCase):
    def test_model(self):
        newsletter = NewsLetter.objects.create(
            email='test@gmail.com',
        )

        self.assertIsNotNone(newsletter.id)
        self.assertEqual(str(newsletter), 'test@gmail.com')
