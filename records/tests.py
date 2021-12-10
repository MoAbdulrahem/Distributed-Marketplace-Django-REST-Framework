from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import RecordViewSet
# Create your tests here.

class TestURLS(SimpleTestCase):

    def test_records_url(self):
        url = reverse("records")
        self.assertEqual(resolve(url), RecordViewSet)
