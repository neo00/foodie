from django.test import TestCase
from randomizer.models import Restaurant


class RandomizerTest(TestCase):
    """tests for the randomizer"""

    def test_homepage(self):
        """tests the homepage"""
        restaurant1 = Restaurant.objects.create(name='1')
        restaurant2 = Restaurant.objects.create(name='2')
        response = self.client.get('/')
        self.assertIn(response.context['restaurant'],
                      [restaurant1, restaurant2])
