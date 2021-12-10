from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import ProductViewSet, ReviewViewSet
# Create your tests here.

class TestURLS(SimpleTestCase):

    def test_products_url(self):
        url = reverse("products")
        self.assertEqual(resolve(url), ProductViewSet)

    def test_reviews_url(self):
        url = reverse("reviews")
        self.assertEqual(resolve(url), ReviewViewSet)
