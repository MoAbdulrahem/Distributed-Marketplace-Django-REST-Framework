from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts import views

# Creating a router and registering our Viewset with it
router = SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
  # path('register/', views.RegisterView.as_view(), name='register')
]