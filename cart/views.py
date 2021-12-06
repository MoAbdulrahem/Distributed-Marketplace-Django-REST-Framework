from rest_framework import viewsets
from rest_framework import generics, status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.response import Response

# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer





class CartItemViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  @action(detail=False, methods=['post'])
  def itemInTheCart(self, request):
      items = CartItem.objects.filter(cart =request.data['cart'])


      try:
          serializer = CartItemSerializer(items , many=True)
          return Response(serializer.data)
      except:
          return Response(status.Http404)




