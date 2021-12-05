from rest_framework import viewsets
from rest_framework import generics, status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
# from rest_framework.response import Response

# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer