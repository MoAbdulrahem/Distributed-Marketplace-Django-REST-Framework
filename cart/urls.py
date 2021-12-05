from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

# Creating a router and registering our Viewset with it
router = SimpleRouter()
router.register(r'cart', views.CartViewSet)
router.register(r'cartproducts', views.CartItemViewSet)

urlpatterns = [
  path('', include(router.urls)),
]