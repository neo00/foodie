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

    def test_deleted_restaurant_bug(self):
        """tests a bug that occurs when you delete a restaurant from the DB"""
        restaurant1 = Restaurant.objects.create(name='A terrible place!')
        restaurant2 = Restaurant.objects.create(name='Foodie Heaven')
        restaurant1.delete()
        response = self.client.get('/')
        self.assertEqual(response.context['restaurant'], restaurant2)
