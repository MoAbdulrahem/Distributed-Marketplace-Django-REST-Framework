from rest_framework import viewsets
from rest_framework import generics, status
from .models import Review, Product
from .serializers import ProductSerializer, ReviewSerializer
# from rest_framework.response import Response

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer