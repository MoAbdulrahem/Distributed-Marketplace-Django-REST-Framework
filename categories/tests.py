from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import CategoryViewSet
# Create your tests here.

class TestURLS(SimpleTestCase):

    def test_categories_url(self):
        url = reverse("categories")
        self.assertEqual(resolve(url), CategoryViewSet)
