from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
  path('', include(router.urls), name='records')
]