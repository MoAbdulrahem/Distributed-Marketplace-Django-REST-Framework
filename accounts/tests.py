from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import UserViewSet
# Create your tests here.

class TestURLS(SimpleTestCase):

    def test_users_url(self):
        url = reverse("users")
        self.assertEqual(resolve(url), UserViewSet)