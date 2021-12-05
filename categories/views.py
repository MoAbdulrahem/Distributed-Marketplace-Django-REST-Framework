from rest_framework import viewsets
from rest_framework import generics, status
from .models import Category
from .serializers import CategorySerializer
# from rest_framework.response import Response

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer