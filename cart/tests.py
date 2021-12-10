from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import CartViewSet, CartItemViewSet
# Create your tests here.

class TestURLS(SimpleTestCase):

    def test_cart_url(self):
        url = reverse("cart")
        self.assertEqual(resolve(url), CartViewSet)

    def test_cartitems_url(self):
        url = reverse("cartitems")
        self.assertEqual(resolve(url), CartViewSet)