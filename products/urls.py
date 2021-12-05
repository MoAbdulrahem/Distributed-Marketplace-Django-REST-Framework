from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

# Creating a router and registering our Viewset with it
router = SimpleRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'reviews', views.ReviewViewSet) #Just for testing, this should not make it to the final version


urlpatterns = [
  path('', include(router.urls)),
]